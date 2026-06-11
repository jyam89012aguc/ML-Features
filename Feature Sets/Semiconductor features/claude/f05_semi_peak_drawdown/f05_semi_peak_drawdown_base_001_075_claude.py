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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f05_dd(c, w):
    peak = c.rolling(w, min_periods=max(1, w // 2)).max()
    return (c - peak) / peak.replace(0, np.nan)


def _f05_runup(c, w):
    trough = c.rolling(w, min_periods=max(1, w // 2)).min()
    return (c - trough) / trough.replace(0, np.nan)


def _f05_log_dd(c, w):
    peak = c.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(c.replace(0, np.nan) / peak.replace(0, np.nan))

# 21d close drawdown from rolling peak
def f05pd_f05_semi_peak_drawdown_dd_21d_base_v001_signal(closeadj, high, low):
    result = _f05_dd(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d close drawdown from rolling peak
def f05pd_f05_semi_peak_drawdown_dd_63d_base_v002_signal(closeadj, high, low):
    result = _f05_dd(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d close drawdown from rolling peak
def f05pd_f05_semi_peak_drawdown_dd_126d_base_v003_signal(closeadj, high, low):
    result = _f05_dd(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d close drawdown from rolling peak
def f05pd_f05_semi_peak_drawdown_dd_252d_base_v004_signal(closeadj, high, low):
    result = _f05_dd(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d close drawdown from rolling peak
def f05pd_f05_semi_peak_drawdown_dd_504d_base_v005_signal(closeadj, high, low):
    result = _f05_dd(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log drawdown from rolling peak
def f05pd_f05_semi_peak_drawdown_logdd_21d_base_v006_signal(closeadj, high, low):
    result = _f05_log_dd(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log drawdown from rolling peak
def f05pd_f05_semi_peak_drawdown_logdd_63d_base_v007_signal(closeadj, high, low):
    result = _f05_log_dd(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log drawdown from rolling peak
def f05pd_f05_semi_peak_drawdown_logdd_126d_base_v008_signal(closeadj, high, low):
    result = _f05_log_dd(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log drawdown from rolling peak
def f05pd_f05_semi_peak_drawdown_logdd_252d_base_v009_signal(closeadj, high, low):
    result = _f05_log_dd(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log drawdown from rolling peak
def f05pd_f05_semi_peak_drawdown_logdd_504d_base_v010_signal(closeadj, high, low):
    result = _f05_log_dd(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d close run-up from rolling trough
def f05pd_f05_semi_peak_drawdown_runup_21d_base_v011_signal(closeadj, high, low):
    result = _f05_runup(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d close run-up from rolling trough
def f05pd_f05_semi_peak_drawdown_runup_63d_base_v012_signal(closeadj, high, low):
    result = _f05_runup(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d close run-up from rolling trough
def f05pd_f05_semi_peak_drawdown_runup_126d_base_v013_signal(closeadj, high, low):
    result = _f05_runup(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d close run-up from rolling trough
def f05pd_f05_semi_peak_drawdown_runup_252d_base_v014_signal(closeadj, high, low):
    result = _f05_runup(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d close run-up from rolling trough
def f05pd_f05_semi_peak_drawdown_runup_504d_base_v015_signal(closeadj, high, low):
    result = _f05_runup(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of high from rolling peak high
def f05pd_f05_semi_peak_drawdown_highdd_21d_base_v016_signal(closeadj, high, low):
    peak = _max(high, 21)
    result = (high - peak) / peak.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of high from rolling peak high
def f05pd_f05_semi_peak_drawdown_highdd_63d_base_v017_signal(closeadj, high, low):
    peak = _max(high, 63)
    result = (high - peak) / peak.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of high from rolling peak high
def f05pd_f05_semi_peak_drawdown_highdd_126d_base_v018_signal(closeadj, high, low):
    peak = _max(high, 126)
    result = (high - peak) / peak.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of high from rolling peak high
def f05pd_f05_semi_peak_drawdown_highdd_252d_base_v019_signal(closeadj, high, low):
    peak = _max(high, 252)
    result = (high - peak) / peak.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of high from rolling peak high
def f05pd_f05_semi_peak_drawdown_highdd_504d_base_v020_signal(closeadj, high, low):
    peak = _max(high, 504)
    result = (high - peak) / peak.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of low from rolling trough low
def f05pd_f05_semi_peak_drawdown_lowrunup_21d_base_v021_signal(closeadj, high, low):
    trough = _min(low, 21)
    result = (low - trough) / trough.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of low from rolling trough low
def f05pd_f05_semi_peak_drawdown_lowrunup_63d_base_v022_signal(closeadj, high, low):
    trough = _min(low, 63)
    result = (low - trough) / trough.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of low from rolling trough low
def f05pd_f05_semi_peak_drawdown_lowrunup_126d_base_v023_signal(closeadj, high, low):
    trough = _min(low, 126)
    result = (low - trough) / trough.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of low from rolling trough low
def f05pd_f05_semi_peak_drawdown_lowrunup_252d_base_v024_signal(closeadj, high, low):
    trough = _min(low, 252)
    result = (low - trough) / trough.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of low from rolling trough low
def f05pd_f05_semi_peak_drawdown_lowrunup_504d_base_v025_signal(closeadj, high, low):
    trough = _min(low, 504)
    result = (low - trough) / trough.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of new 21d closing highs
def f05pd_f05_semi_peak_drawdown_newhighcnt_21d_base_v026_signal(closeadj, high, low):
    peak = _max(closeadj, 21)
    result = (closeadj >= peak).astype(float).rolling(21, min_periods=max(1, 21 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of new 63d closing highs
def f05pd_f05_semi_peak_drawdown_newhighcnt_63d_base_v027_signal(closeadj, high, low):
    peak = _max(closeadj, 63)
    result = (closeadj >= peak).astype(float).rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of new 126d closing highs
def f05pd_f05_semi_peak_drawdown_newhighcnt_126d_base_v028_signal(closeadj, high, low):
    peak = _max(closeadj, 126)
    result = (closeadj >= peak).astype(float).rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of new 252d closing highs
def f05pd_f05_semi_peak_drawdown_newhighcnt_252d_base_v029_signal(closeadj, high, low):
    peak = _max(closeadj, 252)
    result = (closeadj >= peak).astype(float).rolling(252, min_periods=max(1, 252 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of new 504d closing highs
def f05pd_f05_semi_peak_drawdown_newhighcnt_504d_base_v030_signal(closeadj, high, low):
    peak = _max(closeadj, 504)
    result = (closeadj >= peak).astype(float).rolling(504, min_periods=max(1, 504 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of new 21d closing lows
def f05pd_f05_semi_peak_drawdown_newlowcnt_21d_base_v031_signal(closeadj, high, low):
    trough = _min(closeadj, 21)
    result = (closeadj <= trough).astype(float).rolling(21, min_periods=max(1, 21 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of new 63d closing lows
def f05pd_f05_semi_peak_drawdown_newlowcnt_63d_base_v032_signal(closeadj, high, low):
    trough = _min(closeadj, 63)
    result = (closeadj <= trough).astype(float).rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of new 126d closing lows
def f05pd_f05_semi_peak_drawdown_newlowcnt_126d_base_v033_signal(closeadj, high, low):
    trough = _min(closeadj, 126)
    result = (closeadj <= trough).astype(float).rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of new 252d closing lows
def f05pd_f05_semi_peak_drawdown_newlowcnt_252d_base_v034_signal(closeadj, high, low):
    trough = _min(closeadj, 252)
    result = (closeadj <= trough).astype(float).rolling(252, min_periods=max(1, 252 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of new 504d closing lows
def f05pd_f05_semi_peak_drawdown_newlowcnt_504d_base_v035_signal(closeadj, high, low):
    trough = _min(closeadj, 504)
    result = (closeadj <= trough).astype(float).rolling(504, min_periods=max(1, 504 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d proxy: days since last 21d closing peak (1 - drawdown idx)
def f05pd_f05_semi_peak_drawdown_dayssincepeak_21d_base_v036_signal(closeadj, high, low):
    peak = _max(closeadj, 21)
    at_peak = (closeadj >= peak).astype(float)
    result = at_peak.rolling(21, min_periods=max(1, 21 // 2)).apply(lambda s: (s.size - 1 - np.argmax(s[::-1])) if s.max() > 0 else np.nan, raw=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d proxy: days since last 63d closing peak (1 - drawdown idx)
def f05pd_f05_semi_peak_drawdown_dayssincepeak_63d_base_v037_signal(closeadj, high, low):
    peak = _max(closeadj, 63)
    at_peak = (closeadj >= peak).astype(float)
    result = at_peak.rolling(63, min_periods=max(1, 63 // 2)).apply(lambda s: (s.size - 1 - np.argmax(s[::-1])) if s.max() > 0 else np.nan, raw=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d proxy: days since last 126d closing peak (1 - drawdown idx)
def f05pd_f05_semi_peak_drawdown_dayssincepeak_126d_base_v038_signal(closeadj, high, low):
    peak = _max(closeadj, 126)
    at_peak = (closeadj >= peak).astype(float)
    result = at_peak.rolling(126, min_periods=max(1, 126 // 2)).apply(lambda s: (s.size - 1 - np.argmax(s[::-1])) if s.max() > 0 else np.nan, raw=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d proxy: days since last 252d closing peak (1 - drawdown idx)
def f05pd_f05_semi_peak_drawdown_dayssincepeak_252d_base_v039_signal(closeadj, high, low):
    peak = _max(closeadj, 252)
    at_peak = (closeadj >= peak).astype(float)
    result = at_peak.rolling(252, min_periods=max(1, 252 // 2)).apply(lambda s: (s.size - 1 - np.argmax(s[::-1])) if s.max() > 0 else np.nan, raw=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d proxy: days since last 504d closing peak (1 - drawdown idx)
def f05pd_f05_semi_peak_drawdown_dayssincepeak_504d_base_v040_signal(closeadj, high, low):
    peak = _max(closeadj, 504)
    at_peak = (closeadj >= peak).astype(float)
    result = at_peak.rolling(504, min_periods=max(1, 504 // 2)).apply(lambda s: (s.size - 1 - np.argmax(s[::-1])) if s.max() > 0 else np.nan, raw=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d proxy: days since last 21d closing trough
def f05pd_f05_semi_peak_drawdown_dayssincetrough_21d_base_v041_signal(closeadj, high, low):
    trough = _min(closeadj, 21)
    at_trough = (closeadj <= trough).astype(float)
    result = at_trough.rolling(21, min_periods=max(1, 21 // 2)).apply(lambda s: (s.size - 1 - np.argmax(s[::-1])) if s.max() > 0 else np.nan, raw=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d proxy: days since last 63d closing trough
def f05pd_f05_semi_peak_drawdown_dayssincetrough_63d_base_v042_signal(closeadj, high, low):
    trough = _min(closeadj, 63)
    at_trough = (closeadj <= trough).astype(float)
    result = at_trough.rolling(63, min_periods=max(1, 63 // 2)).apply(lambda s: (s.size - 1 - np.argmax(s[::-1])) if s.max() > 0 else np.nan, raw=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d proxy: days since last 126d closing trough
def f05pd_f05_semi_peak_drawdown_dayssincetrough_126d_base_v043_signal(closeadj, high, low):
    trough = _min(closeadj, 126)
    at_trough = (closeadj <= trough).astype(float)
    result = at_trough.rolling(126, min_periods=max(1, 126 // 2)).apply(lambda s: (s.size - 1 - np.argmax(s[::-1])) if s.max() > 0 else np.nan, raw=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d proxy: days since last 252d closing trough
def f05pd_f05_semi_peak_drawdown_dayssincetrough_252d_base_v044_signal(closeadj, high, low):
    trough = _min(closeadj, 252)
    at_trough = (closeadj <= trough).astype(float)
    result = at_trough.rolling(252, min_periods=max(1, 252 // 2)).apply(lambda s: (s.size - 1 - np.argmax(s[::-1])) if s.max() > 0 else np.nan, raw=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d proxy: days since last 504d closing trough
def f05pd_f05_semi_peak_drawdown_dayssincetrough_504d_base_v045_signal(closeadj, high, low):
    trough = _min(closeadj, 504)
    at_trough = (closeadj <= trough).astype(float)
    result = at_trough.rolling(504, min_periods=max(1, 504 // 2)).apply(lambda s: (s.size - 1 - np.argmax(s[::-1])) if s.max() > 0 else np.nan, raw=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of drawdown
def f05pd_f05_semi_peak_drawdown_ddz_21d_base_v046_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 21)
    result = _z(d, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of drawdown
def f05pd_f05_semi_peak_drawdown_ddz_63d_base_v047_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 63)
    result = _z(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of drawdown
def f05pd_f05_semi_peak_drawdown_ddz_126d_base_v048_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 126)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of drawdown
def f05pd_f05_semi_peak_drawdown_ddz_252d_base_v049_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 252)
    result = _z(d, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of drawdown
def f05pd_f05_semi_peak_drawdown_ddz_504d_base_v050_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 504)
    result = _z(d, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of run-up
def f05pd_f05_semi_peak_drawdown_runupz_21d_base_v051_signal(closeadj, high, low):
    u = _f05_runup(closeadj, 21)
    result = _z(u, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of run-up
def f05pd_f05_semi_peak_drawdown_runupz_63d_base_v052_signal(closeadj, high, low):
    u = _f05_runup(closeadj, 63)
    result = _z(u, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of run-up
def f05pd_f05_semi_peak_drawdown_runupz_126d_base_v053_signal(closeadj, high, low):
    u = _f05_runup(closeadj, 126)
    result = _z(u, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of run-up
def f05pd_f05_semi_peak_drawdown_runupz_252d_base_v054_signal(closeadj, high, low):
    u = _f05_runup(closeadj, 252)
    result = _z(u, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of run-up
def f05pd_f05_semi_peak_drawdown_runupz_504d_base_v055_signal(closeadj, high, low):
    u = _f05_runup(closeadj, 504)
    result = _z(u, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d close position in rolling high-low range
def f05pd_f05_semi_peak_drawdown_closepos_21d_base_v056_signal(closeadj, high, low):
    hi = _max(high, 21)
    lo = _min(low, 21)
    result = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d close position in rolling high-low range
def f05pd_f05_semi_peak_drawdown_closepos_63d_base_v057_signal(closeadj, high, low):
    hi = _max(high, 63)
    lo = _min(low, 63)
    result = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d close position in rolling high-low range
def f05pd_f05_semi_peak_drawdown_closepos_126d_base_v058_signal(closeadj, high, low):
    hi = _max(high, 126)
    lo = _min(low, 126)
    result = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d close position in rolling high-low range
def f05pd_f05_semi_peak_drawdown_closepos_252d_base_v059_signal(closeadj, high, low):
    hi = _max(high, 252)
    lo = _min(low, 252)
    result = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d close position in rolling high-low range
def f05pd_f05_semi_peak_drawdown_closepos_504d_base_v060_signal(closeadj, high, low):
    hi = _max(high, 504)
    lo = _min(low, 504)
    result = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d peak-trough range as fraction of trough
def f05pd_f05_semi_peak_drawdown_ptrng_21d_base_v061_signal(closeadj, high, low):
    hi = _max(high, 21)
    lo = _min(low, 21)
    result = (hi - lo) / lo.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d peak-trough range as fraction of trough
def f05pd_f05_semi_peak_drawdown_ptrng_63d_base_v062_signal(closeadj, high, low):
    hi = _max(high, 63)
    lo = _min(low, 63)
    result = (hi - lo) / lo.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d peak-trough range as fraction of trough
def f05pd_f05_semi_peak_drawdown_ptrng_126d_base_v063_signal(closeadj, high, low):
    hi = _max(high, 126)
    lo = _min(low, 126)
    result = (hi - lo) / lo.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d peak-trough range as fraction of trough
def f05pd_f05_semi_peak_drawdown_ptrng_252d_base_v064_signal(closeadj, high, low):
    hi = _max(high, 252)
    lo = _min(low, 252)
    result = (hi - lo) / lo.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d peak-trough range as fraction of trough
def f05pd_f05_semi_peak_drawdown_ptrng_504d_base_v065_signal(closeadj, high, low):
    hi = _max(high, 504)
    lo = _min(low, 504)
    result = (hi - lo) / lo.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days in drawdown (close < peak)
def f05pd_f05_semi_peak_drawdown_underwaterfrac_21d_base_v066_signal(closeadj, high, low):
    peak = _max(closeadj, 21)
    result = (closeadj < peak).astype(float).rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days in drawdown (close < peak)
def f05pd_f05_semi_peak_drawdown_underwaterfrac_63d_base_v067_signal(closeadj, high, low):
    peak = _max(closeadj, 63)
    result = (closeadj < peak).astype(float).rolling(63, min_periods=max(1, 63 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days in drawdown (close < peak)
def f05pd_f05_semi_peak_drawdown_underwaterfrac_126d_base_v068_signal(closeadj, high, low):
    peak = _max(closeadj, 126)
    result = (closeadj < peak).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days in drawdown (close < peak)
def f05pd_f05_semi_peak_drawdown_underwaterfrac_252d_base_v069_signal(closeadj, high, low):
    peak = _max(closeadj, 252)
    result = (closeadj < peak).astype(float).rolling(252, min_periods=max(1, 252 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days in drawdown (close < peak)
def f05pd_f05_semi_peak_drawdown_underwaterfrac_504d_base_v070_signal(closeadj, high, low):
    peak = _max(closeadj, 504)
    result = (closeadj < peak).astype(float).rolling(504, min_periods=max(1, 504 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 5v21 EMA crossover of 21d drawdown
def f05pd_f05_semi_peak_drawdown_ddema_5v21_base_v071_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 21)
    result = d.ewm(span=5, adjust=False).mean() - d.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 EMA crossover of 63d drawdown
def f05pd_f05_semi_peak_drawdown_ddema_21v63_base_v072_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 63)
    result = d.ewm(span=21, adjust=False).mean() - d.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63v126 EMA crossover of 126d drawdown
def f05pd_f05_semi_peak_drawdown_ddema_63v126_base_v073_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 126)
    result = d.ewm(span=63, adjust=False).mean() - d.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126v252 EMA crossover of 252d drawdown
def f05pd_f05_semi_peak_drawdown_ddema_126v252_base_v074_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 252)
    result = d.ewm(span=126, adjust=False).mean() - d.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 EMA crossover of 504d drawdown
def f05pd_f05_semi_peak_drawdown_ddema_252v504_base_v075_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 504)
    result = d.ewm(span=252, adjust=False).mean() - d.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


