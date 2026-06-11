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
def _f28_daily_ffill(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f28_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f28_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# 21d std of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_std_21d_base_v001_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 21)
    result = _std(dd, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_std_63d_base_v002_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 63)
    result = _std(dd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_std_126d_base_v003_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 126)
    result = _std(dd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_std_252d_base_v004_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 252)
    result = _std(dd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_std_504d_base_v005_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 504)
    result = _std(dd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_std_21d_base_v006_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 21)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _std(dd, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_std_63d_base_v007_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 63)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _std(dd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_std_126d_base_v008_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 126)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _std(dd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_std_252d_base_v009_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 252)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _std(dd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_std_504d_base_v010_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 504)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _std(dd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_skew_21d_base_v011_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 21)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.rolling(21, min_periods=max(1, 21//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_skew_63d_base_v012_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 63)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.rolling(63, min_periods=max(1, 63//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_skew_126d_base_v013_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 126)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.rolling(126, min_periods=max(1, 126//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_skew_252d_base_v014_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 252)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_skew_504d_base_v015_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 504)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurt of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_kurt_21d_base_v016_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 21)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.rolling(21, min_periods=max(1, 21//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurt of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_kurt_63d_base_v017_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 63)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.rolling(63, min_periods=max(1, 63//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurt of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_kurt_126d_base_v018_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 126)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.rolling(126, min_periods=max(1, 126//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurt of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_kurt_252d_base_v019_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 252)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurt of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_kurt_504d_base_v020_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 504)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_rng_21d_base_v021_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 21)
    result = _max(dd, 21) - _min(dd, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_rng_63d_base_v022_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 63)
    result = _max(dd, 63) - _min(dd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_rng_126d_base_v023_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 126)
    result = _max(dd, 126) - _min(dd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_rng_252d_base_v024_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 252)
    result = _max(dd, 252) - _min(dd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_rng_504d_base_v025_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 504)
    result = _max(dd, 504) - _min(dd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_rng_21d_base_v026_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 21)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _max(dd, 21) - _min(dd, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_rng_63d_base_v027_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 63)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _max(dd, 63) - _min(dd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_rng_126d_base_v028_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 126)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _max(dd, 126) - _min(dd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_rng_252d_base_v029_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 252)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _max(dd, 252) - _min(dd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of relative capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_rng_504d_base_v030_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 504)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _max(dd, 504) - _min(dd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position-in-range of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_pos_21d_base_v031_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 21)
    lo = _min(dd, 21)
    hi = _max(dd, 21)
    result = (dd - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position-in-range of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_pos_63d_base_v032_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 63)
    lo = _min(dd, 63)
    hi = _max(dd, 63)
    result = (dd - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position-in-range of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_pos_126d_base_v033_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 126)
    lo = _min(dd, 126)
    hi = _max(dd, 126)
    result = (dd - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_pos_252d_base_v034_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 252)
    lo = _min(dd, 252)
    hi = _max(dd, 252)
    result = (dd - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_pos_504d_base_v035_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 504)
    lo = _min(dd, 504)
    hi = _max(dd, 504)
    result = (dd - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position-in-range of rel drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_pos_21d_base_v036_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 21)
    dd = cx / peak.replace(0, np.nan) - 1.0
    lo = _min(dd, 21)
    hi = _max(dd, 21)
    result = (dd - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position-in-range of rel drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_pos_63d_base_v037_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 63)
    dd = cx / peak.replace(0, np.nan) - 1.0
    lo = _min(dd, 63)
    hi = _max(dd, 63)
    result = (dd - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position-in-range of rel drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_pos_126d_base_v038_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 126)
    dd = cx / peak.replace(0, np.nan) - 1.0
    lo = _min(dd, 126)
    hi = _max(dd, 126)
    result = (dd - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of rel drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_pos_252d_base_v039_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 252)
    dd = cx / peak.replace(0, np.nan) - 1.0
    lo = _min(dd, 252)
    hi = _max(dd, 252)
    result = (dd - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of rel drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_pos_504d_base_v040_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 504)
    dd = cx / peak.replace(0, np.nan) - 1.0
    lo = _min(dd, 504)
    hi = _max(dd, 504)
    result = (dd - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d duration at peak (drawdown == 0)
def f28cdd_f28_semi_capex_drawdown_cdd_durzero_21d_base_v041_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 21)
    atpeak = (cx >= peak).astype(float)
    result = atpeak.rolling(21, min_periods=max(1, 21//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration at peak (drawdown == 0)
def f28cdd_f28_semi_capex_drawdown_cdd_durzero_63d_base_v042_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 63)
    atpeak = (cx >= peak).astype(float)
    result = atpeak.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d duration at peak (drawdown == 0)
def f28cdd_f28_semi_capex_drawdown_cdd_durzero_126d_base_v043_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 126)
    atpeak = (cx >= peak).astype(float)
    result = atpeak.rolling(126, min_periods=max(1, 126//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d duration at peak (drawdown == 0)
def f28cdd_f28_semi_capex_drawdown_cdd_durzero_252d_base_v044_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 252)
    atpeak = (cx >= peak).astype(float)
    result = atpeak.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d duration at peak (drawdown == 0)
def f28cdd_f28_semi_capex_drawdown_cdd_durzero_504d_base_v045_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 504)
    atpeak = (cx >= peak).astype(float)
    result = atpeak.rolling(504, min_periods=max(1, 504//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d duration since last peak (lag in days)
def f28cdd_f28_semi_capex_drawdown_cdd_recovery_21d_base_v046_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 21)
    atpeak = (cx >= peak).astype(float)
    result = atpeak.groupby(atpeak.cumsum()).cumcount().astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration since last peak (lag in days)
def f28cdd_f28_semi_capex_drawdown_cdd_recovery_63d_base_v047_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 63)
    atpeak = (cx >= peak).astype(float)
    result = atpeak.groupby(atpeak.cumsum()).cumcount().astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d duration since last peak (lag in days)
def f28cdd_f28_semi_capex_drawdown_cdd_recovery_126d_base_v048_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 126)
    atpeak = (cx >= peak).astype(float)
    result = atpeak.groupby(atpeak.cumsum()).cumcount().astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d duration since last peak (lag in days)
def f28cdd_f28_semi_capex_drawdown_cdd_recovery_252d_base_v049_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 252)
    atpeak = (cx >= peak).astype(float)
    result = atpeak.groupby(atpeak.cumsum()).cumcount().astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d duration since last peak (lag in days)
def f28cdd_f28_semi_capex_drawdown_cdd_recovery_504d_base_v050_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 504)
    atpeak = (cx >= peak).astype(float)
    result = atpeak.groupby(atpeak.cumsum()).cumcount().astype(float)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d underwater area (sum of negative drawdowns)
def f28cdd_f28_semi_capex_drawdown_cdd_underw_21d_base_v051_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 21)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.clip(upper=0).rolling(21, min_periods=max(1, 21//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d underwater area (sum of negative drawdowns)
def f28cdd_f28_semi_capex_drawdown_cdd_underw_63d_base_v052_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 63)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.clip(upper=0).rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d underwater area (sum of negative drawdowns)
def f28cdd_f28_semi_capex_drawdown_cdd_underw_126d_base_v053_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 126)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.clip(upper=0).rolling(126, min_periods=max(1, 126//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d underwater area (sum of negative drawdowns)
def f28cdd_f28_semi_capex_drawdown_cdd_underw_252d_base_v054_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 252)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.clip(upper=0).rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d underwater area (sum of negative drawdowns)
def f28cdd_f28_semi_capex_drawdown_cdd_underw_504d_base_v055_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 504)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.clip(upper=0).rolling(504, min_periods=max(1, 504//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cumulative of drawdown sign
def f28cdd_f28_semi_capex_drawdown_cdd_signcum_21d_base_v056_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 21)
    result = pd.Series(np.sign(dd), index=dd.index).rolling(21, min_periods=max(1, 21//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative of drawdown sign
def f28cdd_f28_semi_capex_drawdown_cdd_signcum_63d_base_v057_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 63)
    result = pd.Series(np.sign(dd), index=dd.index).rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative of drawdown sign
def f28cdd_f28_semi_capex_drawdown_cdd_signcum_126d_base_v058_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 126)
    result = pd.Series(np.sign(dd), index=dd.index).rolling(126, min_periods=max(1, 126//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative of drawdown sign
def f28cdd_f28_semi_capex_drawdown_cdd_signcum_252d_base_v059_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 252)
    result = pd.Series(np.sign(dd), index=dd.index).rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative of drawdown sign
def f28cdd_f28_semi_capex_drawdown_cdd_signcum_504d_base_v060_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 504)
    result = pd.Series(np.sign(dd), index=dd.index).rolling(504, min_periods=max(1, 504//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema(5)-ema(21) of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cdd_ema_21d_base_v061_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 21)
    result = dd.ewm(span=5, adjust=False).mean() - dd.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema(5)-ema(63) of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cdd_ema_63d_base_v062_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 63)
    result = dd.ewm(span=5, adjust=False).mean() - dd.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema(5)-ema(126) of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cdd_ema_126d_base_v063_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 126)
    result = dd.ewm(span=5, adjust=False).mean() - dd.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema(5)-ema(252) of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cdd_ema_252d_base_v064_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 252)
    result = dd.ewm(span=5, adjust=False).mean() - dd.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema(5)-ema(504) of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cdd_ema_504d_base_v065_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 504)
    result = dd.ewm(span=5, adjust=False).mean() - dd.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d deviation of capex from rolling median
def f28cdd_f28_semi_capex_drawdown_cdd_devmed_21d_base_v066_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    med = cx.rolling(21, min_periods=max(1, 21//2)).median()
    result = cx - med
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deviation of capex from rolling median
def f28cdd_f28_semi_capex_drawdown_cdd_devmed_63d_base_v067_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    med = cx.rolling(63, min_periods=max(1, 63//2)).median()
    result = cx - med
    return result.replace([np.inf, -np.inf], np.nan)


# 126d deviation of capex from rolling median
def f28cdd_f28_semi_capex_drawdown_cdd_devmed_126d_base_v068_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    med = cx.rolling(126, min_periods=max(1, 126//2)).median()
    result = cx - med
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deviation of capex from rolling median
def f28cdd_f28_semi_capex_drawdown_cdd_devmed_252d_base_v069_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    med = cx.rolling(252, min_periods=max(1, 252//2)).median()
    result = cx - med
    return result.replace([np.inf, -np.inf], np.nan)


# 504d deviation of capex from rolling median
def f28cdd_f28_semi_capex_drawdown_cdd_devmed_504d_base_v070_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    med = cx.rolling(504, min_periods=max(1, 504//2)).median()
    result = cx - med
    return result.replace([np.inf, -np.inf], np.nan)


# 21d quartile rank of relative drawdown
def f28cdd_f28_semi_capex_drawdown_cdd_quart_21d_base_v071_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 21)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.rolling(21, min_periods=max(1, 21//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d quartile rank of relative drawdown
def f28cdd_f28_semi_capex_drawdown_cdd_quart_63d_base_v072_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 63)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d quartile rank of relative drawdown
def f28cdd_f28_semi_capex_drawdown_cdd_quart_126d_base_v073_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 126)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d quartile rank of relative drawdown
def f28cdd_f28_semi_capex_drawdown_cdd_quart_252d_base_v074_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 252)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d quartile rank of relative drawdown
def f28cdd_f28_semi_capex_drawdown_cdd_quart_504d_base_v075_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 504)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = dd.rolling(504, min_periods=max(1, 504//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)
