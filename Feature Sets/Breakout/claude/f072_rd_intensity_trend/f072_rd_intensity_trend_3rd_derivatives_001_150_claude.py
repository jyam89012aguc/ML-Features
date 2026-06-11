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

def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)

# ===== folder domain primitives =====
def _f072_rd_ratio(rnd, revenue):
    return rnd / revenue.replace(0, np.nan).abs() * rnd


def _f072_rd_trend(rnd, revenue, w):
    ratio = rnd / revenue.replace(0, np.nan).abs()
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean() * rnd


def _f072_investment_growth(rnd, revenue, w):
    rnd_growth = rnd.pct_change(periods=w)
    rev_growth = revenue.pct_change(periods=w)
    return (rnd_growth - rev_growth) * rnd

def f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v001_signal(rnd, revenue, closeadj):
    base = _f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v002_signal(rnd, revenue, closeadj):
    base = _f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v003_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean(), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v004_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean(), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v005_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean(), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v006_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean(), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v007_signal(rnd, revenue, closeadj):
    base = (_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v008_signal(rnd, revenue, closeadj):
    base = (_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v009_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean(), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v010_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean(), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v011_signal(rnd, revenue, closeadj):
    base = _f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v012_signal(rnd, revenue, closeadj):
    base = _f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v013_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean(), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v014_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean(), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v015_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean(), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v016_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean(), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v017_signal(rnd, revenue, closeadj):
    base = (_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v018_signal(rnd, revenue, closeadj):
    base = (_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v019_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean(), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v020_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean(), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v021_signal(rnd, revenue, closeadj):
    base = _f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v022_signal(rnd, revenue, closeadj):
    base = _f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v023_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean(), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v024_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean(), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v025_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean(), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v026_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean(), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v027_signal(rnd, revenue, closeadj):
    base = (_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v028_signal(rnd, revenue, closeadj):
    base = (_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v029_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean(), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v030_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean(), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v031_signal(rnd, revenue, closeadj):
    base = _f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v032_signal(rnd, revenue, closeadj):
    base = _f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v033_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean(), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v034_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean(), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v035_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean(), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v036_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean(), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v037_signal(rnd, revenue, closeadj):
    base = (_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v038_signal(rnd, revenue, closeadj):
    base = (_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v039_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean(), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v040_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean(), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v041_signal(rnd, revenue, closeadj):
    base = _f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v042_signal(rnd, revenue, closeadj):
    base = _f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v043_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean(), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v044_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean(), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v045_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean(), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v046_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean(), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v047_signal(rnd, revenue, closeadj):
    base = (_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v048_signal(rnd, revenue, closeadj):
    base = (_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v049_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean(), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v050_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean(), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v051_signal(rnd, revenue, closeadj):
    base = _f072_rd_trend(rnd, revenue, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v052_signal(rnd, revenue, closeadj):
    base = _f072_rd_trend(rnd, revenue, 5) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v053_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_trend(rnd, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v054_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_trend(rnd, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v055_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_trend(rnd, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v056_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_trend(rnd, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v057_signal(rnd, revenue, closeadj):
    base = (_f072_rd_trend(rnd, revenue, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v058_signal(rnd, revenue, closeadj):
    base = (_f072_rd_trend(rnd, revenue, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v059_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_trend(rnd, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v060_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_trend(rnd, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v061_signal(rnd, revenue, closeadj):
    base = _f072_rd_trend(rnd, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v062_signal(rnd, revenue, closeadj):
    base = _f072_rd_trend(rnd, revenue, 21) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v063_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_trend(rnd, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v064_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_trend(rnd, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v065_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_trend(rnd, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v066_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_trend(rnd, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v067_signal(rnd, revenue, closeadj):
    base = (_f072_rd_trend(rnd, revenue, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v068_signal(rnd, revenue, closeadj):
    base = (_f072_rd_trend(rnd, revenue, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v069_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_trend(rnd, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v070_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_trend(rnd, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v071_signal(rnd, revenue, closeadj):
    base = _f072_rd_trend(rnd, revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v072_signal(rnd, revenue, closeadj):
    base = _f072_rd_trend(rnd, revenue, 63) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v073_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_trend(rnd, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v074_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_trend(rnd, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v075_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_trend(rnd, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v076_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_trend(rnd, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v077_signal(rnd, revenue, closeadj):
    base = (_f072_rd_trend(rnd, revenue, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v078_signal(rnd, revenue, closeadj):
    base = (_f072_rd_trend(rnd, revenue, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v079_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_trend(rnd, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v080_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_trend(rnd, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v081_signal(rnd, revenue, closeadj):
    base = _f072_rd_trend(rnd, revenue, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v082_signal(rnd, revenue, closeadj):
    base = _f072_rd_trend(rnd, revenue, 126) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v083_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_trend(rnd, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v084_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_trend(rnd, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v085_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_trend(rnd, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v086_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_trend(rnd, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v087_signal(rnd, revenue, closeadj):
    base = (_f072_rd_trend(rnd, revenue, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v088_signal(rnd, revenue, closeadj):
    base = (_f072_rd_trend(rnd, revenue, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v089_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_trend(rnd, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v090_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_trend(rnd, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v091_signal(rnd, revenue, closeadj):
    base = _f072_rd_trend(rnd, revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v092_signal(rnd, revenue, closeadj):
    base = _f072_rd_trend(rnd, revenue, 252) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v093_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_trend(rnd, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v094_signal(rnd, revenue, closeadj):
    base = _mean(_f072_rd_trend(rnd, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v095_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_trend(rnd, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v096_signal(rnd, revenue, closeadj):
    base = _std(_f072_rd_trend(rnd, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v097_signal(rnd, revenue, closeadj):
    base = (_f072_rd_trend(rnd, revenue, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v098_signal(rnd, revenue, closeadj):
    base = (_f072_rd_trend(rnd, revenue, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v099_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_trend(rnd, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v100_signal(rnd, revenue, closeadj):
    base = _z(_f072_rd_trend(rnd, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v101_signal(rnd, revenue, closeadj):
    base = _f072_investment_growth(rnd, revenue, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v102_signal(rnd, revenue, closeadj):
    base = _f072_investment_growth(rnd, revenue, 5) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v103_signal(rnd, revenue, closeadj):
    base = _mean(_f072_investment_growth(rnd, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v104_signal(rnd, revenue, closeadj):
    base = _mean(_f072_investment_growth(rnd, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v105_signal(rnd, revenue, closeadj):
    base = _std(_f072_investment_growth(rnd, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v106_signal(rnd, revenue, closeadj):
    base = _std(_f072_investment_growth(rnd, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v107_signal(rnd, revenue, closeadj):
    base = (_f072_investment_growth(rnd, revenue, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v108_signal(rnd, revenue, closeadj):
    base = (_f072_investment_growth(rnd, revenue, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v109_signal(rnd, revenue, closeadj):
    base = _z(_f072_investment_growth(rnd, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v110_signal(rnd, revenue, closeadj):
    base = _z(_f072_investment_growth(rnd, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v111_signal(rnd, revenue, closeadj):
    base = _f072_investment_growth(rnd, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v112_signal(rnd, revenue, closeadj):
    base = _f072_investment_growth(rnd, revenue, 21) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v113_signal(rnd, revenue, closeadj):
    base = _mean(_f072_investment_growth(rnd, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v114_signal(rnd, revenue, closeadj):
    base = _mean(_f072_investment_growth(rnd, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v115_signal(rnd, revenue, closeadj):
    base = _std(_f072_investment_growth(rnd, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v116_signal(rnd, revenue, closeadj):
    base = _std(_f072_investment_growth(rnd, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v117_signal(rnd, revenue, closeadj):
    base = (_f072_investment_growth(rnd, revenue, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v118_signal(rnd, revenue, closeadj):
    base = (_f072_investment_growth(rnd, revenue, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v119_signal(rnd, revenue, closeadj):
    base = _z(_f072_investment_growth(rnd, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v120_signal(rnd, revenue, closeadj):
    base = _z(_f072_investment_growth(rnd, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v121_signal(rnd, revenue, closeadj):
    base = _f072_investment_growth(rnd, revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v122_signal(rnd, revenue, closeadj):
    base = _f072_investment_growth(rnd, revenue, 63) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v123_signal(rnd, revenue, closeadj):
    base = _mean(_f072_investment_growth(rnd, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v124_signal(rnd, revenue, closeadj):
    base = _mean(_f072_investment_growth(rnd, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v125_signal(rnd, revenue, closeadj):
    base = _std(_f072_investment_growth(rnd, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v126_signal(rnd, revenue, closeadj):
    base = _std(_f072_investment_growth(rnd, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v127_signal(rnd, revenue, closeadj):
    base = (_f072_investment_growth(rnd, revenue, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v128_signal(rnd, revenue, closeadj):
    base = (_f072_investment_growth(rnd, revenue, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v129_signal(rnd, revenue, closeadj):
    base = _z(_f072_investment_growth(rnd, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v130_signal(rnd, revenue, closeadj):
    base = _z(_f072_investment_growth(rnd, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v131_signal(rnd, revenue, closeadj):
    base = _f072_investment_growth(rnd, revenue, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v132_signal(rnd, revenue, closeadj):
    base = _f072_investment_growth(rnd, revenue, 126) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v133_signal(rnd, revenue, closeadj):
    base = _mean(_f072_investment_growth(rnd, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v134_signal(rnd, revenue, closeadj):
    base = _mean(_f072_investment_growth(rnd, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v135_signal(rnd, revenue, closeadj):
    base = _std(_f072_investment_growth(rnd, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v136_signal(rnd, revenue, closeadj):
    base = _std(_f072_investment_growth(rnd, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v137_signal(rnd, revenue, closeadj):
    base = (_f072_investment_growth(rnd, revenue, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v138_signal(rnd, revenue, closeadj):
    base = (_f072_investment_growth(rnd, revenue, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v139_signal(rnd, revenue, closeadj):
    base = _z(_f072_investment_growth(rnd, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v140_signal(rnd, revenue, closeadj):
    base = _z(_f072_investment_growth(rnd, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v141_signal(rnd, revenue, closeadj):
    base = _f072_investment_growth(rnd, revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v142_signal(rnd, revenue, closeadj):
    base = _f072_investment_growth(rnd, revenue, 252) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v143_signal(rnd, revenue, closeadj):
    base = _mean(_f072_investment_growth(rnd, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v144_signal(rnd, revenue, closeadj):
    base = _mean(_f072_investment_growth(rnd, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v145_signal(rnd, revenue, closeadj):
    base = _std(_f072_investment_growth(rnd, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v146_signal(rnd, revenue, closeadj):
    base = _std(_f072_investment_growth(rnd, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v147_signal(rnd, revenue, closeadj):
    base = (_f072_investment_growth(rnd, revenue, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v148_signal(rnd, revenue, closeadj):
    base = (_f072_investment_growth(rnd, revenue, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v149_signal(rnd, revenue, closeadj):
    base = _z(_f072_investment_growth(rnd, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v150_signal(rnd, revenue, closeadj):
    base = _z(_f072_investment_growth(rnd, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v001_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v002_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v003_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v004_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v005_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v006_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v007_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v008_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v009_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_jerk_v010_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v011_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v012_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v013_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v014_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v015_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v016_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v017_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v018_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v019_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_jerk_v020_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v021_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v022_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v023_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v024_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v025_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v026_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v027_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v028_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v029_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_jerk_v030_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v031_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v032_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v033_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v034_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v035_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v036_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v037_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v038_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v039_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_jerk_v040_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v041_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v042_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v043_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v044_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v045_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v046_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v047_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v048_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v049_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_jerk_v050_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v051_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v052_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v053_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v054_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v055_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v056_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v057_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v058_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v059_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_jerk_v060_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v061_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v062_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v063_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v064_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v065_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v066_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v067_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v068_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v069_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_jerk_v070_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v071_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v072_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v073_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v074_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v075_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v076_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v077_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v078_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v079_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_jerk_v080_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v081_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v082_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v083_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v084_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v085_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v086_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v087_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v088_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v089_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_jerk_v090_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v091_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v092_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v093_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v094_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v095_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v096_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v097_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v098_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v099_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_jerk_v100_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v101_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v102_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v103_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v104_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v105_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v106_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v107_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v108_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v109_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_jerk_v110_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v111_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v112_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v113_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v114_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v115_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v116_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v117_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v118_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v119_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_jerk_v120_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v121_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v122_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v123_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v124_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v125_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v126_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v127_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v128_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v129_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_jerk_v130_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v131_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v132_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v133_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v134_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v135_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v136_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v137_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v138_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v139_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_jerk_v140_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v141_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v142_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v143_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v144_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v145_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v146_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v147_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v148_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v149_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F072_RD_INTENSITY_TREND_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    rnd = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    cols = {"rnd": rnd, "revenue": revenue, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f072_rd_ratio", "_f072_rd_trend", "_f072_investment_growth")
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
    print(f"OK f072_rd_intensity_trend_jerk_001_150_claude: {n_features} features pass")
