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


def _diff(s, n):
    return s.diff(periods=n)


def _jerk(s, w):
    return s.pct_change(periods=w)


def _jerk(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _f50_quality_composite(roic, fcf, revenue, w):
    fcfm = fcf / revenue.replace(0, np.nan).abs()
    return _mean(roic + fcfm, w)


def _f50_compounder_score(roic, ebitdamargin, w):
    return _mean(roic * ebitdamargin, w)


def _f50_terminal_quality(fcf, revenue, roic, w):
    fcfm = fcf / revenue.replace(0, np.nan).abs()
    rev_stab = 1.0 / (_std(revenue.pct_change(), w).replace(0, np.nan) + 1e-6)
    return _mean(fcfm * roic, w) * _mean(rev_stab, w)


def f50itc_f50_industrial_terminal_compounder_qcomp_21d_jerk_v001_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_63d_jerk_v002_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_126d_jerk_v003_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_252d_jerk_v004_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_504d_jerk_v005_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_5d_jerk_v006_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_42d_jerk_v007_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_189d_jerk_v008_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_378d_jerk_v009_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_21d_jerk_v010_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_21d_jerk_v011_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_63d_jerk_v012_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_252d_jerk_v013_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_504d_jerk_v014_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_126d_jerk_v015_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_5d_jerk_v016_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_42d_jerk_v017_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_189d_jerk_v018_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_378d_jerk_v019_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_21d_jerk_v020_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 21) * closeadj * 1e-4
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_63d_jerk_v021_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 63) * closeadj * 1e-4
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_252d_jerk_v022_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 252) * closeadj * 1e-4
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_504d_jerk_v023_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 504) * closeadj * 1e-4
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_126d_jerk_v024_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 126) * closeadj * 1e-4
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_42d_jerk_v025_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 42) * closeadj * 1e-4
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_189d_jerk_v026_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 189) * closeadj * 1e-4
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompz_63d_jerk_v027_signal(roic, fcf, revenue, closeadj):
    base = _z(_f50_quality_composite(roic, fcf, revenue, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompz_252d_jerk_v028_signal(roic, fcf, revenue, closeadj):
    base = _z(_f50_quality_composite(roic, fcf, revenue, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorez_63d_jerk_v029_signal(roic, ebitdamargin, closeadj):
    base = _z(_f50_compounder_score(roic, ebitdamargin, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorez_252d_jerk_v030_signal(roic, ebitdamargin, closeadj):
    base = _z(_f50_compounder_score(roic, ebitdamargin, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualityz_252d_jerk_v031_signal(fcf, revenue, roic, closeadj):
    base = _z(_f50_terminal_quality(fcf, revenue, roic, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompstd_252d_jerk_v032_signal(roic, fcf, revenue, closeadj):
    base = _std(_f50_quality_composite(roic, fcf, revenue, 21), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorestd_252d_jerk_v033_signal(roic, ebitdamargin, closeadj):
    base = _std(_f50_compounder_score(roic, ebitdamargin, 21), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualitystd_252d_jerk_v034_signal(fcf, revenue, roic, closeadj):
    base = _std(_f50_terminal_quality(fcf, revenue, roic, 21), 252) * closeadj * 1e-4
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompdiff_63m252_jerk_v035_signal(roic, fcf, revenue, closeadj):
    sh = _f50_quality_composite(roic, fcf, revenue, 63)
    lg = _f50_quality_composite(roic, fcf, revenue, 252)
    base = (sh - lg) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorediff_63m252_jerk_v036_signal(roic, ebitdamargin, closeadj):
    sh = _f50_compounder_score(roic, ebitdamargin, 63)
    lg = _f50_compounder_score(roic, ebitdamargin, 252)
    base = (sh - lg) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualitydiff_63m252_jerk_v037_signal(fcf, revenue, roic, closeadj):
    sh = _f50_terminal_quality(fcf, revenue, roic, 63)
    lg = _f50_terminal_quality(fcf, revenue, roic, 252)
    base = (sh - lg) * closeadj * 1e-4
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompema_63d_jerk_v038_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompema_252d_jerk_v039_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscoreema_63d_jerk_v040_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscoreema_252d_jerk_v041_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualityema_63d_jerk_v042_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj * 1e-4
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualityema_252d_jerk_v043_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj * 1e-4
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomprank_252d_jerk_v044_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorerank_252d_jerk_v045_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualityrank_252d_jerk_v046_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_compxprice_252d_jerk_v047_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    a = _f50_quality_composite(roic, fcf, revenue, 252)
    b = _f50_compounder_score(roic, ebitdamargin, 252)
    base = (a + b) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_compxtqual_252d_jerk_v048_signal(roic, fcf, revenue, closeadj):
    a = _f50_quality_composite(roic, fcf, revenue, 252)
    c = _f50_terminal_quality(fcf, revenue, roic, 252)
    base = (a + c * 1e-4) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_hi_252d_jerk_v049_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    base = (hi * g + g * 0.5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_hi_252d_jerk_v050_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    base = (hi * g + g * 0.5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxvolz_63d_jerk_v051_signal(roic, fcf, revenue, volume, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63) * _z(volume, 63) * closeadj
    result = _jerk(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexvolz_252d_jerk_v052_signal(roic, ebitdamargin, volume, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252) * _z(volume, 252) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxlogprice_252d_jerk_v053_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252) * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexlogprice_252d_jerk_v054_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252) * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_lag_252d_jerk_v055_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    base = (g - g.shift(252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_lag_252d_jerk_v056_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 63)
    base = (g - g.shift(252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_full_composite_252d_jerk_v057_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    a = _f50_quality_composite(roic, fcf, revenue, 252)
    b = _f50_compounder_score(roic, ebitdamargin, 252)
    c = _f50_terminal_quality(fcf, revenue, roic, 252)
    base = (a + b + c * 1e-4) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_skew_252d_jerk_v058_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    base = g.rolling(252, min_periods=63).skew() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_skew_252d_jerk_v059_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    base = g.rolling(252, min_periods=63).skew() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_sqqcomp_252d_jerk_v060_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    base = g * g.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_log_252d_jerk_v061_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    base = np.sign(g) * np.log1p(g.abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_med_252d_jerk_v062_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    med = g.rolling(252, min_periods=63).median()
    base = (g - med) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_lo_252d_jerk_v063_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    med = g.rolling(252, min_periods=63).median()
    lo = (g < med).astype(float)
    base = (lo * g + g * 0.5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_event_hi_252d_jerk_v064_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    med = g.rolling(252, min_periods=63).median()
    flag = (g > med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    base = (cnt + g * 10.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_min_63d_jerk_v065_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    base = (g.rolling(63, min_periods=21).min() + g * 0.1) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_max_252d_jerk_v066_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    base = (g.rolling(252, min_periods=63).max() + g * 0.1) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_range_252d_jerk_v067_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    base = rng * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_range_252d_jerk_v068_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    base = rng * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_x_revgrowth_252d_jerk_v069_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252) * revenue.pct_change(252) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_x_revgrowth_252d_jerk_v070_signal(roic, ebitdamargin, revenue, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252) * revenue.pct_change(252) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxsqrtprice_252d_jerk_v071_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252) * np.sqrt(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexsqrtprice_252d_jerk_v072_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252) * np.sqrt(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_voladj_252d_jerk_v073_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    vol = _std(revenue.pct_change(), 252)
    base = g / vol.replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_voladj_252d_jerk_v074_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    vol = _std((roic * ebitdamargin).pct_change(), 252)
    base = g / vol.replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_trend_252d_jerk_v075_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    trend = g.rolling(252, min_periods=63).mean() - g.rolling(504, min_periods=126).mean()
    result = _jerk(trend * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_diff_252m504_jerk_v076_signal(roic, fcf, revenue, closeadj):
    sh = _f50_quality_composite(roic, fcf, revenue, 252)
    lg = _f50_quality_composite(roic, fcf, revenue, 504)
    base = (sh - lg) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_diff_252m504_jerk_v077_signal(roic, ebitdamargin, closeadj):
    sh = _f50_compounder_score(roic, ebitdamargin, 252)
    lg = _f50_compounder_score(roic, ebitdamargin, 504)
    base = (sh - lg) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_x_logrevenue_252d_jerk_v078_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252) * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_x_logrevenue_252d_jerk_v079_signal(roic, ebitdamargin, revenue, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252) * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_volgrowth_252d_jerk_v080_signal(roic, fcf, revenue, volume, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252) * volume.pct_change(252) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_volgrowth_252d_jerk_v081_signal(roic, ebitdamargin, volume, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252) * volume.pct_change(252) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxebitda_252d_jerk_v082_signal(roic, fcf, revenue, ebitda, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252) * np.log(ebitda.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexebitda_252d_jerk_v083_signal(roic, ebitdamargin, ebitda, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252) * np.log(ebitda.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxfcf_252d_jerk_v084_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252) * np.log(fcf.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxprice_504d_jerk_v085_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 504) * closeadj * closeadj
    result = _jerk(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexprice_504d_jerk_v086_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 504) * closeadj * closeadj
    result = _jerk(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_voladj_63d_jerk_v087_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    vol = _std(revenue.pct_change(), 63)
    base = g / vol.replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_voladj_63d_jerk_v088_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 63)
    vol = _std((roic * ebitdamargin).pct_change(), 63)
    base = g / vol.replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_med_504d_jerk_v089_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 504)
    med = g.rolling(504, min_periods=126).median()
    base = (g - med) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_med_504d_jerk_v090_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 504)
    med = g.rolling(504, min_periods=126).median()
    base = (g - med) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_max_504d_jerk_v091_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    base = (g.rolling(504, min_periods=126).max() + g * 0.1) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_max_504d_jerk_v092_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    base = (g.rolling(504, min_periods=126).max() + g * 0.1) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_range_504d_jerk_v093_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    rng = g.rolling(504, min_periods=126).max() - g.rolling(504, min_periods=126).min()
    result = _jerk(rng * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_ema_21d_jerk_v094_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 5)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_ema_21d_jerk_v095_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 5)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_minus_const_252d_jerk_v096_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    base = (g - 0.2) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_minus_const_252d_jerk_v097_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    base = (g - 0.025) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_sotp_x_252d_jerk_v098_signal(roic, fcf, revenue, ebitda, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252) * (revenue / ebitda.replace(0, np.nan).abs()) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_sotp_x_252d_jerk_v099_signal(roic, ebitdamargin, revenue, ebitda, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252) * (revenue / ebitda.replace(0, np.nan).abs()) * closeadj
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_long_ema_504d_jerk_v100_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    base = g.ewm(span=504, adjust=False).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_full_composite_504d_jerk_v101_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    a = _f50_quality_composite(roic, fcf, revenue, 504)
    b = _f50_compounder_score(roic, ebitdamargin, 504)
    c = _f50_terminal_quality(fcf, revenue, roic, 504)
    base = (a + b + c * 1e-4) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_terminal_value_proxy_252d_jerk_v102_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    a = _f50_quality_composite(roic, fcf, revenue, 252)
    b = _f50_compounder_score(roic, ebitdamargin, 252)
    base = a * b * closeadj * 10.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_chg_252d_jerk_v103_signal(roic, fcf, revenue, closeadj):
    base_v = _f50_quality_composite(roic, fcf, revenue, 252)
    inner = roic + fcf / revenue.replace(0, np.nan).abs()
    base = (base_v + (inner - inner.shift(252))) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_lograw_252d_jerk_v104_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    base = np.log(g.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_lograw_252d_jerk_v105_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    base = np.log(g.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_lograw_252d_jerk_v106_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 252)
    base = np.log(g.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_kurt_252d_jerk_v107_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    base = g.rolling(252, min_periods=63).kurt() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_kurt_252d_jerk_v108_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    base = g.rolling(252, min_periods=63).kurt() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_skew_504d_jerk_v109_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    base = g.rolling(504, min_periods=126).skew() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompdiff_21m63_jerk_v110_signal(roic, fcf, revenue, closeadj):
    sh = _f50_quality_composite(roic, fcf, revenue, 21)
    lg = _f50_quality_composite(roic, fcf, revenue, 63)
    base = (sh - lg) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorediff_21m63_jerk_v111_signal(roic, ebitdamargin, closeadj):
    sh = _f50_compounder_score(roic, ebitdamargin, 21)
    lg = _f50_compounder_score(roic, ebitdamargin, 63)
    base = (sh - lg) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompratio_63v252_jerk_v112_signal(roic, fcf, revenue, closeadj):
    sh = _f50_quality_composite(roic, fcf, revenue, 63)
    lg = _f50_quality_composite(roic, fcf, revenue, 252)
    base = sh / lg.replace(0, np.nan).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscoreratio_63v252_jerk_v113_signal(roic, ebitdamargin, closeadj):
    sh = _f50_compounder_score(roic, ebitdamargin, 63)
    lg = _f50_compounder_score(roic, ebitdamargin, 252)
    base = sh / lg.replace(0, np.nan).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_minus_smoothed_252d_jerk_v114_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    sm = _mean(g, 252)
    base = (g - sm) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_minus_smoothed_252d_jerk_v115_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 63)
    sm = _mean(g, 252)
    base = (g - sm) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_compxprice_63d_jerk_v116_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    a = _f50_quality_composite(roic, fcf, revenue, 63)
    b = _f50_compounder_score(roic, ebitdamargin, 63)
    base = (a + b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxprice_log_252d_jerk_v117_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252) * np.log(closeadj.abs().replace(0, np.nan)) * closeadj * 1.5
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexprice_log_252d_jerk_v118_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252) * np.log(closeadj.abs().replace(0, np.nan)) * closeadj * 1.5
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxvol_dv_252d_jerk_v119_signal(roic, fcf, revenue, volume, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252) * _mean(closeadj * volume, 63)
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexvol_dv_252d_jerk_v120_signal(roic, ebitdamargin, volume, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252) * _mean(closeadj * volume, 63)
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_x_logrevenue_252d_jerk_v121_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 252) * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj * 1e-4
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_trend_252d_jerk_v122_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 21)
    trend = g.rolling(252, min_periods=63).mean() - g.rolling(504, min_periods=126).mean()
    result = _jerk(trend * closeadj * 1e-4, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_long_ema_504d_jerk_v123_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 63)
    base = g.ewm(span=504, adjust=False).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_x_revgrowth_504d_jerk_v124_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 504) * revenue.pct_change(252) * closeadj
    result = _jerk(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_x_revgrowth_504d_jerk_v125_signal(roic, ebitdamargin, revenue, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 504) * revenue.pct_change(252) * closeadj
    result = _jerk(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_negativity_252d_jerk_v126_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    med = g.rolling(252, min_periods=63).median()
    neg = (g < med).astype(float)
    base = (neg * g + g * 0.5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_event_lo_252d_jerk_v127_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 63)
    med = g.rolling(252, min_periods=63).median()
    flag = (g < med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    base = (cnt + g * 10.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_chg_252d_jerk_v128_signal(fcf, revenue, roic, closeadj):
    base_v = _f50_terminal_quality(fcf, revenue, roic, 252)
    inner = (fcf / revenue.replace(0, np.nan).abs()) * roic
    base = (base_v + (inner - inner.shift(252))) * closeadj * 1e-4
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompstd_63d_jerk_v129_signal(roic, fcf, revenue, closeadj):
    base = _std(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorestd_504d_jerk_v130_signal(roic, ebitdamargin, closeadj):
    base = _std(_f50_compounder_score(roic, ebitdamargin, 63), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompstd_504d_jerk_v131_signal(roic, fcf, revenue, closeadj):
    base = _std(_f50_quality_composite(roic, fcf, revenue, 63), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_x_revgrowth_252d_jerk_v132_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 252) * revenue.pct_change(252) * closeadj * 1e-4
    result = _jerk(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_log_504d_jerk_v133_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 504)
    base = np.sign(g) * np.log1p(g.abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_log_504d_jerk_v134_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 504)
    base = np.sign(g) * np.log1p(g.abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualityz_63d_jerk_v135_signal(fcf, revenue, roic, closeadj):
    base = _z(_f50_terminal_quality(fcf, revenue, roic, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_event_hi_504d_jerk_v136_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    med = g.rolling(504, min_periods=126).median()
    flag = (g > med).astype(float)
    cnt = flag.rolling(504, min_periods=126).sum()
    base = (cnt + g * 10.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_x_logrevenue_504d_jerk_v137_signal(roic, ebitdamargin, revenue, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 504) * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _jerk(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_x_logrevenue_504d_jerk_v138_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 504) * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _jerk(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxsqrtprice_504d_jerk_v139_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 504) * np.sqrt(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _jerk(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexsqrtprice_504d_jerk_v140_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 504) * np.sqrt(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _jerk(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomprank_504d_jerk_v141_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorerank_504d_jerk_v142_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_hi_252d_jerk_v143_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    base = (hi * g + g * 0.5) * closeadj * 1e-4
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_ema_504d_alt_jerk_v144_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    base = g.ewm(span=504, adjust=False).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_ema_504d_alt_jerk_v145_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    base = g.ewm(span=504, adjust=False).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tqualityema_504d_jerk_v146_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 21)
    base = g.ewm(span=504, adjust=False).mean() * closeadj * 1e-4
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxprice_63d_jerk_v147_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63) * closeadj * closeadj
    result = _jerk(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexprice_63d_jerk_v148_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 63) * closeadj * closeadj
    result = _jerk(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_alt_skew_jerk_v149_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    base = g.rolling(252, min_periods=63).skew() * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_alt_kurt_jerk_v150_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    base = g.rolling(252, min_periods=63).kurt() * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f50itc_f50_industrial_terminal_compounder_qcomp_21d_jerk_v001_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_63d_jerk_v002_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_126d_jerk_v003_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_252d_jerk_v004_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_504d_jerk_v005_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_5d_jerk_v006_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_42d_jerk_v007_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_189d_jerk_v008_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_378d_jerk_v009_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_21d_jerk_v010_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_21d_jerk_v011_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_63d_jerk_v012_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_252d_jerk_v013_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_504d_jerk_v014_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_126d_jerk_v015_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_5d_jerk_v016_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_42d_jerk_v017_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_189d_jerk_v018_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_378d_jerk_v019_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_21d_jerk_v020_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_63d_jerk_v021_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_252d_jerk_v022_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_504d_jerk_v023_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_126d_jerk_v024_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_42d_jerk_v025_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_189d_jerk_v026_signal,
    f50itc_f50_industrial_terminal_compounder_qcompz_63d_jerk_v027_signal,
    f50itc_f50_industrial_terminal_compounder_qcompz_252d_jerk_v028_signal,
    f50itc_f50_industrial_terminal_compounder_cscorez_63d_jerk_v029_signal,
    f50itc_f50_industrial_terminal_compounder_cscorez_252d_jerk_v030_signal,
    f50itc_f50_industrial_terminal_compounder_tqualityz_252d_jerk_v031_signal,
    f50itc_f50_industrial_terminal_compounder_qcompstd_252d_jerk_v032_signal,
    f50itc_f50_industrial_terminal_compounder_cscorestd_252d_jerk_v033_signal,
    f50itc_f50_industrial_terminal_compounder_tqualitystd_252d_jerk_v034_signal,
    f50itc_f50_industrial_terminal_compounder_qcompdiff_63m252_jerk_v035_signal,
    f50itc_f50_industrial_terminal_compounder_cscorediff_63m252_jerk_v036_signal,
    f50itc_f50_industrial_terminal_compounder_tqualitydiff_63m252_jerk_v037_signal,
    f50itc_f50_industrial_terminal_compounder_qcompema_63d_jerk_v038_signal,
    f50itc_f50_industrial_terminal_compounder_qcompema_252d_jerk_v039_signal,
    f50itc_f50_industrial_terminal_compounder_cscoreema_63d_jerk_v040_signal,
    f50itc_f50_industrial_terminal_compounder_cscoreema_252d_jerk_v041_signal,
    f50itc_f50_industrial_terminal_compounder_tqualityema_63d_jerk_v042_signal,
    f50itc_f50_industrial_terminal_compounder_tqualityema_252d_jerk_v043_signal,
    f50itc_f50_industrial_terminal_compounder_qcomprank_252d_jerk_v044_signal,
    f50itc_f50_industrial_terminal_compounder_cscorerank_252d_jerk_v045_signal,
    f50itc_f50_industrial_terminal_compounder_tqualityrank_252d_jerk_v046_signal,
    f50itc_f50_industrial_terminal_compounder_compxprice_252d_jerk_v047_signal,
    f50itc_f50_industrial_terminal_compounder_compxtqual_252d_jerk_v048_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_hi_252d_jerk_v049_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_hi_252d_jerk_v050_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxvolz_63d_jerk_v051_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexvolz_252d_jerk_v052_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxlogprice_252d_jerk_v053_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexlogprice_252d_jerk_v054_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_lag_252d_jerk_v055_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_lag_252d_jerk_v056_signal,
    f50itc_f50_industrial_terminal_compounder_full_composite_252d_jerk_v057_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_skew_252d_jerk_v058_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_skew_252d_jerk_v059_signal,
    f50itc_f50_industrial_terminal_compounder_sqqcomp_252d_jerk_v060_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_log_252d_jerk_v061_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_med_252d_jerk_v062_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_lo_252d_jerk_v063_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_event_hi_252d_jerk_v064_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_min_63d_jerk_v065_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_max_252d_jerk_v066_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_range_252d_jerk_v067_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_range_252d_jerk_v068_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_x_revgrowth_252d_jerk_v069_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_x_revgrowth_252d_jerk_v070_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxsqrtprice_252d_jerk_v071_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexsqrtprice_252d_jerk_v072_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_voladj_252d_jerk_v073_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_voladj_252d_jerk_v074_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_trend_252d_jerk_v075_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_diff_252m504_jerk_v076_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_diff_252m504_jerk_v077_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_x_logrevenue_252d_jerk_v078_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_x_logrevenue_252d_jerk_v079_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_volgrowth_252d_jerk_v080_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_volgrowth_252d_jerk_v081_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxebitda_252d_jerk_v082_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexebitda_252d_jerk_v083_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxfcf_252d_jerk_v084_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxprice_504d_jerk_v085_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexprice_504d_jerk_v086_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_voladj_63d_jerk_v087_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_voladj_63d_jerk_v088_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_med_504d_jerk_v089_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_med_504d_jerk_v090_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_max_504d_jerk_v091_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_max_504d_jerk_v092_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_range_504d_jerk_v093_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_ema_21d_jerk_v094_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_ema_21d_jerk_v095_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_minus_const_252d_jerk_v096_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_minus_const_252d_jerk_v097_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_sotp_x_252d_jerk_v098_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_sotp_x_252d_jerk_v099_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_long_ema_504d_jerk_v100_signal,
    f50itc_f50_industrial_terminal_compounder_full_composite_504d_jerk_v101_signal,
    f50itc_f50_industrial_terminal_compounder_terminal_value_proxy_252d_jerk_v102_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_chg_252d_jerk_v103_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_lograw_252d_jerk_v104_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_lograw_252d_jerk_v105_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_lograw_252d_jerk_v106_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_kurt_252d_jerk_v107_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_kurt_252d_jerk_v108_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_skew_504d_jerk_v109_signal,
    f50itc_f50_industrial_terminal_compounder_qcompdiff_21m63_jerk_v110_signal,
    f50itc_f50_industrial_terminal_compounder_cscorediff_21m63_jerk_v111_signal,
    f50itc_f50_industrial_terminal_compounder_qcompratio_63v252_jerk_v112_signal,
    f50itc_f50_industrial_terminal_compounder_cscoreratio_63v252_jerk_v113_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_minus_smoothed_252d_jerk_v114_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_minus_smoothed_252d_jerk_v115_signal,
    f50itc_f50_industrial_terminal_compounder_compxprice_63d_jerk_v116_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxprice_log_252d_jerk_v117_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexprice_log_252d_jerk_v118_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxvol_dv_252d_jerk_v119_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexvol_dv_252d_jerk_v120_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_x_logrevenue_252d_jerk_v121_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_trend_252d_jerk_v122_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_long_ema_504d_jerk_v123_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_x_revgrowth_504d_jerk_v124_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_x_revgrowth_504d_jerk_v125_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_negativity_252d_jerk_v126_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_event_lo_252d_jerk_v127_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_chg_252d_jerk_v128_signal,
    f50itc_f50_industrial_terminal_compounder_qcompstd_63d_jerk_v129_signal,
    f50itc_f50_industrial_terminal_compounder_cscorestd_504d_jerk_v130_signal,
    f50itc_f50_industrial_terminal_compounder_qcompstd_504d_jerk_v131_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_x_revgrowth_252d_jerk_v132_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_log_504d_jerk_v133_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_log_504d_jerk_v134_signal,
    f50itc_f50_industrial_terminal_compounder_tqualityz_63d_jerk_v135_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_event_hi_504d_jerk_v136_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_x_logrevenue_504d_jerk_v137_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_x_logrevenue_504d_jerk_v138_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxsqrtprice_504d_jerk_v139_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexsqrtprice_504d_jerk_v140_signal,
    f50itc_f50_industrial_terminal_compounder_qcomprank_504d_jerk_v141_signal,
    f50itc_f50_industrial_terminal_compounder_cscorerank_504d_jerk_v142_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_hi_252d_jerk_v143_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_ema_504d_alt_jerk_v144_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_ema_504d_alt_jerk_v145_signal,
    f50itc_f50_industrial_terminal_compounder_tqualityema_504d_jerk_v146_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxprice_63d_jerk_v147_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexprice_63d_jerk_v148_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_alt_skew_jerk_v149_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_alt_kurt_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_INDUSTRIAL_TERMINAL_COMPOUNDER_REGISTRY_jerk_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f50_industrial_terminal_compounder_3rd_derivatives_001_150_claude: {n_features} features pass")

