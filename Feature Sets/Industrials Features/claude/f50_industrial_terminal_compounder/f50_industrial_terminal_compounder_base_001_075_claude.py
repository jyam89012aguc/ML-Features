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
def _f50_quality_composite(roic, fcf, revenue, w):
    fcfm = fcf / revenue.replace(0, np.nan).abs()
    return _mean(roic + fcfm, w)


def _f50_compounder_score(roic, ebitdamargin, w):
    return _mean(roic * ebitdamargin, w)


def _f50_terminal_quality(fcf, revenue, roic, w):
    fcfm = fcf / revenue.replace(0, np.nan).abs()
    rev_stab = 1.0 / (_std(revenue.pct_change(), w).replace(0, np.nan) + 1e-6)
    return _mean(fcfm * roic, w) * _mean(rev_stab, w)


# v001-v009 quality composite
def f50itc_f50_industrial_terminal_compounder_qcomp_21d_base_v001_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_63d_base_v002_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_126d_base_v003_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_252d_base_v004_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_504d_base_v005_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_5d_base_v006_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_42d_base_v007_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_189d_base_v008_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_378d_base_v009_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010-v018 compounder score
def f50itc_f50_industrial_terminal_compounder_cscore_21d_base_v010_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 21)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_63d_base_v011_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 63)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_126d_base_v012_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 126)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_252d_base_v013_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 252)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_504d_base_v014_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 504)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_5d_base_v015_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 5)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_42d_base_v016_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 42)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_189d_base_v017_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 189)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_378d_base_v018_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 378)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


# v019-v027 terminal quality
def f50itc_f50_industrial_terminal_compounder_tquality_21d_base_v019_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 21)
    return (base * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_63d_base_v020_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 63)
    return (base * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_126d_base_v021_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 126)
    return (base * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_252d_base_v022_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 252)
    return (base * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_504d_base_v023_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 504)
    return (base * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_5d_base_v024_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 5)
    return (base * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_42d_base_v025_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 42)
    return (base * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_189d_base_v026_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 189)
    return (base * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_378d_base_v027_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 378)
    return (base * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


# v028-v033 z-scores
def f50itc_f50_industrial_terminal_compounder_qcompz_63d_base_v028_signal(roic, fcf, revenue, closeadj):
    base = _z(_f50_quality_composite(roic, fcf, revenue, 63), 252)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompz_252d_base_v029_signal(roic, fcf, revenue, closeadj):
    base = _z(_f50_quality_composite(roic, fcf, revenue, 252), 504)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorez_63d_base_v030_signal(roic, ebitdamargin, closeadj):
    base = _z(_f50_compounder_score(roic, ebitdamargin, 63), 252)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorez_252d_base_v031_signal(roic, ebitdamargin, closeadj):
    base = _z(_f50_compounder_score(roic, ebitdamargin, 252), 504)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualityz_63d_base_v032_signal(fcf, revenue, roic, closeadj):
    base = _z(_f50_terminal_quality(fcf, revenue, roic, 63), 252)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualityz_252d_base_v033_signal(fcf, revenue, roic, closeadj):
    base = _z(_f50_terminal_quality(fcf, revenue, roic, 252), 504)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


# v034-v039 std
def f50itc_f50_industrial_terminal_compounder_qcompstd_252d_base_v034_signal(roic, fcf, revenue, closeadj):
    base = _std(_f50_quality_composite(roic, fcf, revenue, 21), 252)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorestd_252d_base_v035_signal(roic, ebitdamargin, closeadj):
    base = _std(_f50_compounder_score(roic, ebitdamargin, 21), 252)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualitystd_252d_base_v036_signal(fcf, revenue, roic, closeadj):
    base = _std(_f50_terminal_quality(fcf, revenue, roic, 21), 252)
    return (base * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompstd_63d_base_v037_signal(roic, fcf, revenue, closeadj):
    base = _std(_f50_quality_composite(roic, fcf, revenue, 5), 63)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorestd_504d_base_v038_signal(roic, ebitdamargin, closeadj):
    base = _std(_f50_compounder_score(roic, ebitdamargin, 63), 504)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompstd_504d_base_v039_signal(roic, fcf, revenue, closeadj):
    base = _std(_f50_quality_composite(roic, fcf, revenue, 63), 504)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


# v040-v045 diffs/ratios
def f50itc_f50_industrial_terminal_compounder_qcompdiff_63m252_base_v040_signal(roic, fcf, revenue, closeadj):
    sh = _f50_quality_composite(roic, fcf, revenue, 63)
    lg = _f50_quality_composite(roic, fcf, revenue, 252)
    return ((sh - lg) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorediff_63m252_base_v041_signal(roic, ebitdamargin, closeadj):
    sh = _f50_compounder_score(roic, ebitdamargin, 63)
    lg = _f50_compounder_score(roic, ebitdamargin, 252)
    return ((sh - lg) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualitydiff_63m252_base_v042_signal(fcf, revenue, roic, closeadj):
    sh = _f50_terminal_quality(fcf, revenue, roic, 63)
    lg = _f50_terminal_quality(fcf, revenue, roic, 252)
    return ((sh - lg) * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompratio_63v252_base_v043_signal(roic, fcf, revenue, closeadj):
    sh = _f50_quality_composite(roic, fcf, revenue, 63)
    lg = _f50_quality_composite(roic, fcf, revenue, 252)
    return (sh / lg.replace(0, np.nan).abs() * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscoreratio_63v252_base_v044_signal(roic, ebitdamargin, closeadj):
    sh = _f50_compounder_score(roic, ebitdamargin, 63)
    lg = _f50_compounder_score(roic, ebitdamargin, 252)
    return (sh / lg.replace(0, np.nan).abs() * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompdiff_21m63_base_v045_signal(roic, fcf, revenue, closeadj):
    sh = _f50_quality_composite(roic, fcf, revenue, 21)
    lg = _f50_quality_composite(roic, fcf, revenue, 63)
    return ((sh - lg) * closeadj).replace([np.inf, -np.inf], np.nan)


# v046-v051 EMAs
def f50itc_f50_industrial_terminal_compounder_qcompema_63d_base_v046_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompema_252d_base_v047_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscoreema_63d_base_v048_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscoreema_252d_base_v049_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualityema_63d_base_v050_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj * 1e-4
    return base.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualityema_252d_base_v051_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj * 1e-4
    return base.replace([np.inf, -np.inf], np.nan)


# v052-v056 ranks
def f50itc_f50_industrial_terminal_compounder_qcomprank_252d_base_v052_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorerank_252d_base_v053_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualityrank_252d_base_v054_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomprank_504d_base_v055_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorerank_504d_base_v056_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True)
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


# v057-v066 combinations / hi-lo / log
def f50itc_f50_industrial_terminal_compounder_compxprice_252d_base_v057_signal(roic, fcf, revenue, ebitdamargin, ebitda, closeadj):
    a = _f50_quality_composite(roic, fcf, revenue, 252)
    b = _f50_compounder_score(roic, ebitdamargin, 252)
    return ((a + b) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_compxprice_63d_base_v058_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    a = _f50_quality_composite(roic, fcf, revenue, 63)
    b = _f50_compounder_score(roic, ebitdamargin, 63)
    return ((a + b) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_compxtqual_252d_base_v059_signal(roic, fcf, revenue, closeadj):
    a = _f50_quality_composite(roic, fcf, revenue, 252)
    c = _f50_terminal_quality(fcf, revenue, roic, 252)
    return ((a + c * 1e-4) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_hi_252d_base_v060_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    return ((hi * g + g * 0.5) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_hi_252d_base_v061_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    return ((hi * g + g * 0.5) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_hi_252d_base_v062_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    return ((hi * g + g * 0.5) * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_skew_252d_base_v063_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    return (g.rolling(252, min_periods=63).skew() * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_skew_252d_base_v064_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    return (g.rolling(252, min_periods=63).skew() * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_kurt_252d_base_v065_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    return (g.rolling(252, min_periods=63).kurt() * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_sqqcomp_252d_base_v066_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    return (g * g.abs() * closeadj).replace([np.inf, -np.inf], np.nan)


# v067-v075 special variants
def f50itc_f50_industrial_terminal_compounder_qcompxvolz_63d_base_v067_signal(roic, fcf, revenue, volume, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    return (g * _z(volume, 63) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexvolz_252d_base_v068_signal(roic, ebitdamargin, volume, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    return (g * _z(volume, 252) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualityxdv_252d_base_v069_signal(fcf, revenue, roic, volume, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 252)
    dv = closeadj * volume
    return (g * _mean(dv, 63) * 1e-12).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxlogprice_252d_base_v070_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    return (g * np.log(closeadj.abs().replace(0, np.nan)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexlogprice_252d_base_v071_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    return (g * np.log(closeadj.abs().replace(0, np.nan)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_lag_252d_base_v072_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    return ((g - g.shift(252)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_lag_252d_base_v073_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 63)
    return ((g - g.shift(252)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_log_252d_base_v074_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    return (np.sign(g) * np.log1p(g.abs()) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_full_composite_252d_base_v075_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    a = _f50_quality_composite(roic, fcf, revenue, 252)
    b = _f50_compounder_score(roic, ebitdamargin, 252)
    c = _f50_terminal_quality(fcf, revenue, roic, 252)
    return ((a + b + c * 1e-4) * closeadj).replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f50itc_f50_industrial_terminal_compounder_qcomp_21d_base_v001_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_63d_base_v002_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_126d_base_v003_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_252d_base_v004_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_504d_base_v005_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_5d_base_v006_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_42d_base_v007_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_189d_base_v008_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_378d_base_v009_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_21d_base_v010_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_63d_base_v011_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_126d_base_v012_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_252d_base_v013_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_504d_base_v014_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_5d_base_v015_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_42d_base_v016_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_189d_base_v017_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_378d_base_v018_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_21d_base_v019_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_63d_base_v020_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_126d_base_v021_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_252d_base_v022_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_504d_base_v023_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_5d_base_v024_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_42d_base_v025_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_189d_base_v026_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_378d_base_v027_signal,
    f50itc_f50_industrial_terminal_compounder_qcompz_63d_base_v028_signal,
    f50itc_f50_industrial_terminal_compounder_qcompz_252d_base_v029_signal,
    f50itc_f50_industrial_terminal_compounder_cscorez_63d_base_v030_signal,
    f50itc_f50_industrial_terminal_compounder_cscorez_252d_base_v031_signal,
    f50itc_f50_industrial_terminal_compounder_tqualityz_63d_base_v032_signal,
    f50itc_f50_industrial_terminal_compounder_tqualityz_252d_base_v033_signal,
    f50itc_f50_industrial_terminal_compounder_qcompstd_252d_base_v034_signal,
    f50itc_f50_industrial_terminal_compounder_cscorestd_252d_base_v035_signal,
    f50itc_f50_industrial_terminal_compounder_tqualitystd_252d_base_v036_signal,
    f50itc_f50_industrial_terminal_compounder_qcompstd_63d_base_v037_signal,
    f50itc_f50_industrial_terminal_compounder_cscorestd_504d_base_v038_signal,
    f50itc_f50_industrial_terminal_compounder_qcompstd_504d_base_v039_signal,
    f50itc_f50_industrial_terminal_compounder_qcompdiff_63m252_base_v040_signal,
    f50itc_f50_industrial_terminal_compounder_cscorediff_63m252_base_v041_signal,
    f50itc_f50_industrial_terminal_compounder_tqualitydiff_63m252_base_v042_signal,
    f50itc_f50_industrial_terminal_compounder_qcompratio_63v252_base_v043_signal,
    f50itc_f50_industrial_terminal_compounder_cscoreratio_63v252_base_v044_signal,
    f50itc_f50_industrial_terminal_compounder_qcompdiff_21m63_base_v045_signal,
    f50itc_f50_industrial_terminal_compounder_qcompema_63d_base_v046_signal,
    f50itc_f50_industrial_terminal_compounder_qcompema_252d_base_v047_signal,
    f50itc_f50_industrial_terminal_compounder_cscoreema_63d_base_v048_signal,
    f50itc_f50_industrial_terminal_compounder_cscoreema_252d_base_v049_signal,
    f50itc_f50_industrial_terminal_compounder_tqualityema_63d_base_v050_signal,
    f50itc_f50_industrial_terminal_compounder_tqualityema_252d_base_v051_signal,
    f50itc_f50_industrial_terminal_compounder_qcomprank_252d_base_v052_signal,
    f50itc_f50_industrial_terminal_compounder_cscorerank_252d_base_v053_signal,
    f50itc_f50_industrial_terminal_compounder_tqualityrank_252d_base_v054_signal,
    f50itc_f50_industrial_terminal_compounder_qcomprank_504d_base_v055_signal,
    f50itc_f50_industrial_terminal_compounder_cscorerank_504d_base_v056_signal,
    f50itc_f50_industrial_terminal_compounder_compxprice_252d_base_v057_signal,
    f50itc_f50_industrial_terminal_compounder_compxprice_63d_base_v058_signal,
    f50itc_f50_industrial_terminal_compounder_compxtqual_252d_base_v059_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_hi_252d_base_v060_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_hi_252d_base_v061_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_hi_252d_base_v062_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_skew_252d_base_v063_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_skew_252d_base_v064_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_kurt_252d_base_v065_signal,
    f50itc_f50_industrial_terminal_compounder_sqqcomp_252d_base_v066_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxvolz_63d_base_v067_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexvolz_252d_base_v068_signal,
    f50itc_f50_industrial_terminal_compounder_tqualityxdv_252d_base_v069_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxlogprice_252d_base_v070_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexlogprice_252d_base_v071_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_lag_252d_base_v072_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_lag_252d_base_v073_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_log_252d_base_v074_signal,
    f50itc_f50_industrial_terminal_compounder_full_composite_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_INDUSTRIAL_TERMINAL_COMPOUNDER_REGISTRY_001_075 = REGISTRY


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
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    roic    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "fcf": fcf,
        "roic": roic, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f50_quality_composite", "_f50_compounder_score", "_f50_terminal_quality")
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
    print(f"OK f50_industrial_terminal_compounder_base_001_075_claude: {n_features} features pass")
