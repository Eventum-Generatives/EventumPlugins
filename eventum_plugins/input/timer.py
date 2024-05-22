from datetime import datetime
import time
from typing import Any, Callable

from numpy import datetime64
from pydantic import Field
from pytz.tzinfo import DstTzInfo

from eventum_plugins.input.base import (InputPluginBaseConfig,
                                        LiveInputPluginMixin)


class TimerInputConfig(InputPluginBaseConfig):
    seconds: int = Field(..., ge=1)
    count: int = Field(..., ge=1)
    repeat: bool


class TimerInputPlugin(LiveInputPluginMixin):
    """Input plugin for generating events after specified number of
    seconds.
    """

    def __init__(self, config: TimerInputConfig, tz: DstTzInfo) -> None:
        self._seconds = config.seconds
        self._count = config.count
        self._repeat = config.repeat
        self._tz = tz

    def live(self, on_event: Callable[[datetime64], Any]) -> None:
        while True:
            if not self._repeat:
                break

            time.sleep(self._seconds)

            timestamp = datetime64(
                datetime.now(tz=self._tz).replace(tzinfo=None)
            )
            for _ in range(self._count):
                on_event(timestamp)


PLUGIN_CLASS = TimerInputPlugin
CONFIG_CLASS = TimerInputConfig