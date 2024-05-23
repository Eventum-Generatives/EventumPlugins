import json
import logging
import os
from abc import ABC, abstractmethod
from enum import StrEnum
from typing import Iterable, assert_never

from pydantic import BaseModel

logger = logging.getLogger(__name__)


class OutputPluginError(Exception):
    """Base exception for all output plugin errors."""


class OutputPluginConfigurationError(OutputPluginError):
    """Exception for output plugin configuration errors."""


class OutputPluginRuntimeError(OutputPluginError):
    """Exception for output plugin runtime errors."""


class FormatError(OutputPluginRuntimeError):
    """Exception for formatting errors."""


class OutputPluginBaseConfig(BaseModel, extra='forbid', frozen=True):
    """Base config model for output plugins"""


class OutputFormat(StrEnum):
    ORIGINAL = 'original'
    JSON_LINES = 'json-lines'


class BaseOutputPlugin(ABC):
    """Base class for all output plugins."""
    def __init__(self, format: OutputFormat) -> None:
        self._format = format
        self._is_opened = False

    async def open(self) -> None:
        """Open target for async writing."""
        if not self._is_opened:
            await self._open()
            self._is_opened = True

    async def close(self) -> None:
        """Close target and release acquired resources."""
        if self._is_opened:
            await self._close()
            self._is_opened = False

    async def write(self, event: str) -> int:
        """Write single event to output stream. `1` is returned if
        event is successfully written else `0`.
        """
        if not self._is_opened:
            raise OutputPluginRuntimeError(
                'Output plugin is not opened for writing to target'
            )

        try:
            fmt_event = self._format_event(event=event)
        except FormatError:
            return 0

        return await self._write(fmt_event)

    async def write_many(self, events: Iterable[str]) -> int:
        """Write many events to output stream. Number of successfully
        written events is returned.
        """
        if not self._is_opened:
            raise OutputPluginRuntimeError(
                'Output plugin is not opened for writing to target'
            )

        fmt_events = []
        for event in events:
            try:
                fmt_events.append(self._format_event(event=event))
            except FormatError:
                continue

        if len(fmt_events) == 0:
            return 0

        return await self._write_many(events)

    async def _open(self) -> None:
        """Perform open operation."""
        ...

    async def _close(self) -> None:
        """Perform close operation."""
        ...

    @abstractmethod
    async def _write(self, event: str) -> int:
        """Perform write operation."""
        ...

    @abstractmethod
    async def _write_many(self, events: Iterable[str]) -> int:
        """Perform bulk write operation."""
        ...

    def _format_event(self, event: str) -> str:
        """Format `event` to configured `format`"""
        try:
            match self._format:
                case OutputFormat.ORIGINAL:
                    return event
                case OutputFormat.JSON_LINES:
                    return json.dumps(json.loads(event), ensure_ascii=False)
                case val:
                    assert_never(val)
        except Exception as e:
            logger.warning(
                f'Failed to format event to "{self._format}" format: {e}'
                f'{os.linesep}'
                'Original unformatted event: '
                f'{os.linesep}'
                f'{event}'
            )
            raise FormatError(f'Failed to format event: {e}') from e
