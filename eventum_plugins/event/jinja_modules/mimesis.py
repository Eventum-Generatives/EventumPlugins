import mimesis.enums as enums  # noqa
import mimesis.locales as locales  # noqa
import mimesis.providers as providers  # noqa
import mimesis.random as random  # noqa
from mimesis import Generic, Locale
from mimesis.builtins import (BrazilSpecProvider, DenmarkSpecProvider,
                              ItalySpecProvider, NetherlandsSpecProvider,
                              PolandSpecProvider, RussiaSpecProvider,
                              UkraineSpecProvider, USASpecProvider)

generic = Generic()

brazil_spec = BrazilSpecProvider()
denmark_spec = DenmarkSpecProvider()
italy_spec = ItalySpecProvider()
netherlands_spec = NetherlandsSpecProvider()
poland_spec = PolandSpecProvider()
russia_spec = RussiaSpecProvider()
ukraine_spec = UkraineSpecProvider()
usa_spec = USASpecProvider()

cs = Generic(Locale.CS)
da = Generic(Locale.DA)
de = Generic(Locale.DE)
de_at = Generic(Locale.DE_AT)
de_ch = Generic(Locale.DE_CH)
el = Generic(Locale.EL)
en = Generic(Locale.EN)
en_au = Generic(Locale.EN_AU)
en_ca = Generic(Locale.EN_CA)
en_gb = Generic(Locale.EN_GB)
es = Generic(Locale.ES)
es_mx = Generic(Locale.ES_MX)
et = Generic(Locale.ET)
fa = Generic(Locale.FA)
fi = Generic(Locale.FI)
fr = Generic(Locale.FR)
hu = Generic(Locale.HU)
hr = Generic(Locale.HR)
is_ = Generic(Locale.IS)
it = Generic(Locale.IT)
ja = Generic(Locale.JA)
kk = Generic(Locale.KK)
ko = Generic(Locale.KO)
nl = Generic(Locale.NL)
nl_be = Generic(Locale.NL_BE)
no = Generic(Locale.NO)
pl = Generic(Locale.PL)
pt = Generic(Locale.PT)
pt_br = Generic(Locale.PT_BR)
ru = Generic(Locale.RU)
sk = Generic(Locale.SK)
sv = Generic(Locale.SV)
tr = Generic(Locale.TR)
uk = Generic(Locale.UK)
zh = Generic(Locale.ZH)
