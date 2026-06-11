import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f49_evebitda_dynamics(evebitda, w):
    return _mean(evebitda, w)


def _f49_premium_discount(evebitda, ebitdamargin, w):
    return _mean(evebitda * ebitdamargin, w)


def _f49_sotp_proxy(ev, ebitda, revenue, w):
    return _mean((ev / ebitda.replace(0, np.nan).abs()) * (revenue / ev.replace(0, np.nan).abs()), w)


# v001-v009: EV/EBITDA at various windows × closeadj
def f49cpd_f49_conglomerate_premium_discount_evebitda_21d_base_v001_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_63d_base_v002_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_126d_base_v003_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_252d_base_v004_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_504d_base_v005_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_5d_base_v006_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_42d_base_v007_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_189d_base_v008_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_378d_base_v009_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010-v018: premium/discount × close
def f49cpd_f49_conglomerate_premium_discount_premdisc_21d_base_v010_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_63d_base_v011_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_126d_base_v012_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_252d_base_v013_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_504d_base_v014_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_5d_base_v015_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_42d_base_v016_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_189d_base_v017_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_378d_base_v018_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019-v027: SOTP proxy × close
def f49cpd_f49_conglomerate_premium_discount_sotp_21d_base_v019_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_63d_base_v020_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_126d_base_v021_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_252d_base_v022_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_504d_base_v023_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_5d_base_v024_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_42d_base_v025_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_189d_base_v026_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_378d_base_v027_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028-v034: z-scores
def f49cpd_f49_conglomerate_premium_discount_evebitda_z_63d_base_v028_signal(evebitda, closeadj):
    base = _z(_f49_evebitda_dynamics(evebitda, 63), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_z_252d_base_v029_signal(evebitda, closeadj):
    base = _z(_f49_evebitda_dynamics(evebitda, 252), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_z_63d_base_v030_signal(evebitda, ebitdamargin, closeadj):
    base = _z(_f49_premium_discount(evebitda, ebitdamargin, 63), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_z_252d_base_v031_signal(evebitda, ebitdamargin, closeadj):
    base = _z(_f49_premium_discount(evebitda, ebitdamargin, 252), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_z_63d_base_v032_signal(ev, ebitda, revenue, closeadj):
    base = _z(_f49_sotp_proxy(ev, ebitda, revenue, 63), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_z_252d_base_v033_signal(ev, ebitda, revenue, closeadj):
    base = _z(_f49_sotp_proxy(ev, ebitda, revenue, 252), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_z_21d_base_v034_signal(evebitda, closeadj):
    base = _z(_f49_evebitda_dynamics(evebitda, 21), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v035-v040: std
def f49cpd_f49_conglomerate_premium_discount_evebitda_std_252d_base_v035_signal(evebitda, closeadj):
    base = _std(_f49_evebitda_dynamics(evebitda, 21), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_std_252d_base_v036_signal(evebitda, ebitdamargin, closeadj):
    base = _std(_f49_premium_discount(evebitda, ebitdamargin, 21), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_std_252d_base_v037_signal(ev, ebitda, revenue, closeadj):
    base = _std(_f49_sotp_proxy(ev, ebitda, revenue, 21), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_std_63d_base_v038_signal(evebitda, closeadj):
    base = _std(_f49_evebitda_dynamics(evebitda, 5), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_std_504d_base_v039_signal(evebitda, closeadj):
    base = _std(_f49_evebitda_dynamics(evebitda, 63), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_std_504d_base_v040_signal(evebitda, ebitdamargin, closeadj):
    base = _std(_f49_premium_discount(evebitda, ebitdamargin, 63), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041-v046: diffs and ratios
def f49cpd_f49_conglomerate_premium_discount_evebitda_diff_63m252_base_v041_signal(evebitda, closeadj):
    sh = _f49_evebitda_dynamics(evebitda, 63)
    lg = _f49_evebitda_dynamics(evebitda, 252)
    result = (sh - lg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_diff_21m63_base_v042_signal(evebitda, closeadj):
    sh = _f49_evebitda_dynamics(evebitda, 21)
    lg = _f49_evebitda_dynamics(evebitda, 63)
    result = (sh - lg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_diff_252m504_base_v043_signal(evebitda, closeadj):
    sh = _f49_evebitda_dynamics(evebitda, 252)
    lg = _f49_evebitda_dynamics(evebitda, 504)
    result = (sh - lg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_diff_63m252_base_v044_signal(evebitda, ebitdamargin, closeadj):
    sh = _f49_premium_discount(evebitda, ebitdamargin, 63)
    lg = _f49_premium_discount(evebitda, ebitdamargin, 252)
    result = (sh - lg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_diff_63m252_base_v045_signal(ev, ebitda, revenue, closeadj):
    sh = _f49_sotp_proxy(ev, ebitda, revenue, 63)
    lg = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    result = (sh - lg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_ratio_63v252_base_v046_signal(evebitda, closeadj):
    sh = _f49_evebitda_dynamics(evebitda, 63)
    lg = _f49_evebitda_dynamics(evebitda, 252)
    result = sh / lg.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v047-v053: EMAs
def f49cpd_f49_conglomerate_premium_discount_evebitda_ema_63d_base_v047_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_ema_252d_base_v048_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_ema_63d_base_v049_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_ema_252d_base_v050_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_ema_63d_base_v051_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_ema_252d_base_v052_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_ema_21d_base_v053_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 5)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


# v054-v058: ranks
def f49cpd_f49_conglomerate_premium_discount_evebitda_rank_252d_base_v054_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_rank_252d_base_v055_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_rank_252d_base_v056_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_rank_504d_base_v057_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_rank_504d_base_v058_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


# v059-v066: mix-change × multiple
def f49cpd_f49_conglomerate_premium_discount_evebitdaxrevmix_252d_base_v059_signal(evebitda, ev, revenue, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 252)
    rev_mix = revenue / ev.replace(0, np.nan).abs()
    return (base * rev_mix * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxrevmix_63d_base_v060_signal(evebitda, ev, revenue, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 63)
    rev_mix = revenue / ev.replace(0, np.nan).abs()
    return (base * rev_mix * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxrevmix_252d_base_v061_signal(evebitda, ebitdamargin, ev, revenue, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 252)
    rev_mix = revenue / ev.replace(0, np.nan).abs()
    return (base * rev_mix * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotpxrevmix_252d_base_v062_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    return (base * (revenue / ev.replace(0, np.nan).abs()) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_chg_252d_base_v063_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 252)
    chg = evebitda - evebitda.shift(252)
    return (base + chg) * closeadj


def f49cpd_f49_conglomerate_premium_discount_evebitda_pctchg_252d_base_v064_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 252)
    pct = evebitda.pct_change(252)
    return ((base * (1.0 + pct)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxmargin_252d_base_v065_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 252)
    return (base * ebitdamargin * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxmargin_63d_base_v066_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 63)
    return (base * ebitdamargin * closeadj).replace([np.inf, -np.inf], np.nan)


# v067-v075: hi/lo, skew/kurt, log
def f49cpd_f49_conglomerate_premium_discount_evebitda_med_252d_base_v067_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    med = g.rolling(252, min_periods=63).median()
    return ((g - med) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_hi_252d_base_v068_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    return ((hi * g + g * 0.5) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_hi_252d_base_v069_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    return ((hi * g + g * 0.5) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaskew_252d_base_v070_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 21)
    base = g.rolling(252, min_periods=63).skew()
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdakurt_252d_base_v071_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 21)
    base = g.rolling(252, min_periods=63).kurt()
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sqevebitda_252d_base_v072_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    return (g * g.abs() * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_logevebitda_252d_base_v073_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    return (np.sign(g) * np.log1p(g.abs()) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_range_252d_base_v074_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    return (rng * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_composite_252d_base_v075_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    a = _f49_evebitda_dynamics(evebitda, 252)
    b = _f49_premium_discount(evebitda, ebitdamargin, 252)
    c = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    return ((a + b + c) * closeadj).replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f49cpd_f49_conglomerate_premium_discount_evebitda_21d_base_v001_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_63d_base_v002_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_126d_base_v003_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_252d_base_v004_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_504d_base_v005_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_5d_base_v006_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_42d_base_v007_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_189d_base_v008_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_378d_base_v009_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_21d_base_v010_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_63d_base_v011_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_126d_base_v012_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_252d_base_v013_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_504d_base_v014_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_5d_base_v015_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_42d_base_v016_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_189d_base_v017_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_378d_base_v018_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_21d_base_v019_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_63d_base_v020_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_126d_base_v021_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_252d_base_v022_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_504d_base_v023_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_5d_base_v024_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_42d_base_v025_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_189d_base_v026_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_378d_base_v027_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_z_63d_base_v028_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_z_252d_base_v029_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_z_63d_base_v030_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_z_252d_base_v031_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_z_63d_base_v032_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_z_252d_base_v033_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_z_21d_base_v034_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_std_252d_base_v035_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_std_252d_base_v036_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_std_252d_base_v037_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_std_63d_base_v038_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_std_504d_base_v039_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_std_504d_base_v040_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_diff_63m252_base_v041_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_diff_21m63_base_v042_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_diff_252m504_base_v043_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_diff_63m252_base_v044_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_diff_63m252_base_v045_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_ratio_63v252_base_v046_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_ema_63d_base_v047_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_ema_252d_base_v048_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_ema_63d_base_v049_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_ema_252d_base_v050_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_ema_63d_base_v051_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_ema_252d_base_v052_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_ema_21d_base_v053_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_rank_252d_base_v054_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_rank_252d_base_v055_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_rank_252d_base_v056_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_rank_504d_base_v057_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_rank_504d_base_v058_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxrevmix_252d_base_v059_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxrevmix_63d_base_v060_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxrevmix_252d_base_v061_signal,
    f49cpd_f49_conglomerate_premium_discount_sotpxrevmix_252d_base_v062_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_chg_252d_base_v063_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_pctchg_252d_base_v064_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxmargin_252d_base_v065_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxmargin_63d_base_v066_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_med_252d_base_v067_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_hi_252d_base_v068_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_hi_252d_base_v069_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaskew_252d_base_v070_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdakurt_252d_base_v071_signal,
    f49cpd_f49_conglomerate_premium_discount_sqevebitda_252d_base_v072_signal,
    f49cpd_f49_conglomerate_premium_discount_logevebitda_252d_base_v073_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_range_252d_base_v074_signal,
    f49cpd_f49_conglomerate_premium_discount_composite_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_CONGLOMERATE_PREMIUM_DISCOUNT_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    debt    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    ev      = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    evebitda = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ev": ev, "evebitda": evebitda,
        "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f49_evebitda_dynamics", "_f49_premium_discount", "_f49_sotp_proxy")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f49_conglomerate_premium_discount_base_001_075_claude: {n_features} features pass")
