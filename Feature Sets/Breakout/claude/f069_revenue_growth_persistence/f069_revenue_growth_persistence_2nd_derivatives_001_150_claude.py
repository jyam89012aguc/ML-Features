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


def _ema(s, w):
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()


def _signlike(s):
    return np.tanh(s)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)



# ===== folder domain primitives =====
def _f069_growth_rate(revenue, w):
    return revenue.pct_change(periods=w)


def _f069_consec_accelerating(revenue, w):
    # count of periods within window where growth is accelerating
    g = revenue.pct_change(periods=max(2, w // 4))
    accel = (g.diff() > 0).astype(float)
    return accel.rolling(w, min_periods=max(1, w // 2)).sum()


def _f069_persistence_count(revenue, w):
    # rolling fraction of periods with positive growth, scaled
    g = revenue.pct_change(periods=max(2, w // 4))
    pos = (g > 0).astype(float)
    sm = pos.rolling(w, min_periods=max(1, w // 2)).mean()
    return sm * g.rolling(w, min_periods=max(1, w // 2)).mean()


# accel_5d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_accel_5d_x_close_5d_slope_v001_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 5)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_5d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_accel_5d_x_logclose_21d_slope_v002_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 5)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_5d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_accel_5d_x_meanclose_63d_slope_v003_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 5)
    mid = base * _mean(closeadj, 5)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_5d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_accel_5d_x_closedif_10d_slope_v004_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 5)
    mid = base * closeadj.diff(1).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_5d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_accel_5d_ema_x_close_42d_slope_v005_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 5)
    mid = _ema(base, 2) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_10d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_accel_10d_x_close_5d_slope_v006_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 10)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_10d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_accel_10d_x_logclose_21d_slope_v007_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 10)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_10d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_accel_10d_x_meanclose_63d_slope_v008_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 10)
    mid = base * _mean(closeadj, 10)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_10d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_accel_10d_x_closedif_10d_slope_v009_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 10)
    mid = base * closeadj.diff(2).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_10d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_accel_10d_ema_x_close_42d_slope_v010_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 10)
    mid = _ema(base, 5) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_21d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_accel_21d_x_close_5d_slope_v011_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 21)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_21d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_accel_21d_x_logclose_21d_slope_v012_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 21)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_21d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_accel_21d_x_meanclose_63d_slope_v013_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 21)
    mid = base * _mean(closeadj, 21)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_21d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_accel_21d_x_closedif_10d_slope_v014_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 21)
    mid = base * closeadj.diff(5).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_21d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_accel_21d_ema_x_close_42d_slope_v015_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 21)
    mid = _ema(base, 10) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_42d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_accel_42d_x_close_5d_slope_v016_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 42)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_42d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_accel_42d_x_logclose_21d_slope_v017_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 42)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_42d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_accel_42d_x_meanclose_63d_slope_v018_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 42)
    mid = base * _mean(closeadj, 42)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_42d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_accel_42d_x_closedif_10d_slope_v019_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 42)
    mid = base * closeadj.diff(10).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_42d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_accel_42d_ema_x_close_42d_slope_v020_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 42)
    mid = _ema(base, 21) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_63d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_accel_63d_x_close_5d_slope_v021_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 63)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_63d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_accel_63d_x_logclose_21d_slope_v022_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 63)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_63d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_accel_63d_x_meanclose_63d_slope_v023_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 63)
    mid = base * _mean(closeadj, 63)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_63d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_accel_63d_x_closedif_10d_slope_v024_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 63)
    mid = base * closeadj.diff(15).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_63d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_accel_63d_ema_x_close_42d_slope_v025_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 63)
    mid = _ema(base, 31) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_126d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_accel_126d_x_close_5d_slope_v026_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 126)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_126d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_accel_126d_x_logclose_21d_slope_v027_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 126)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_126d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_accel_126d_x_meanclose_63d_slope_v028_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 126)
    mid = base * _mean(closeadj, 126)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_126d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_accel_126d_x_closedif_10d_slope_v029_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 126)
    mid = base * closeadj.diff(31).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_126d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_accel_126d_ema_x_close_42d_slope_v030_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 126)
    mid = _ema(base, 63) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_189d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_accel_189d_x_close_5d_slope_v031_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 189)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_189d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_accel_189d_x_logclose_21d_slope_v032_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 189)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_189d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_accel_189d_x_meanclose_63d_slope_v033_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 189)
    mid = base * _mean(closeadj, 189)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_189d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_accel_189d_x_closedif_10d_slope_v034_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 189)
    mid = base * closeadj.diff(47).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_189d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_accel_189d_ema_x_close_42d_slope_v035_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 189)
    mid = _ema(base, 94) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_252d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_accel_252d_x_close_5d_slope_v036_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 252)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_252d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_accel_252d_x_logclose_21d_slope_v037_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 252)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_252d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_accel_252d_x_meanclose_63d_slope_v038_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 252)
    mid = base * _mean(closeadj, 252)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_252d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_accel_252d_x_closedif_10d_slope_v039_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 252)
    mid = base * closeadj.diff(63).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_252d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_accel_252d_ema_x_close_42d_slope_v040_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 252)
    mid = _ema(base, 126) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_378d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_accel_378d_x_close_5d_slope_v041_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 378)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_378d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_accel_378d_x_logclose_21d_slope_v042_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 378)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_378d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_accel_378d_x_meanclose_63d_slope_v043_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 378)
    mid = base * _mean(closeadj, 378)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_378d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_accel_378d_x_closedif_10d_slope_v044_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 378)
    mid = base * closeadj.diff(94).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_378d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_accel_378d_ema_x_close_42d_slope_v045_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 378)
    mid = _ema(base, 189) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_504d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_accel_504d_x_close_5d_slope_v046_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 504)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_504d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_accel_504d_x_logclose_21d_slope_v047_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 504)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_504d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_accel_504d_x_meanclose_63d_slope_v048_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 504)
    mid = base * _mean(closeadj, 504)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_504d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_accel_504d_x_closedif_10d_slope_v049_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 504)
    mid = base * closeadj.diff(126).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# accel_504d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_accel_504d_ema_x_close_42d_slope_v050_signal(revenue, closeadj):
    base = _f069_consec_accelerating(revenue, 504)
    mid = _ema(base, 252) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_5d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_growth_5d_x_close_5d_slope_v051_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 5)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_5d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_growth_5d_x_logclose_21d_slope_v052_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 5)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_5d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_growth_5d_x_meanclose_63d_slope_v053_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 5)
    mid = base * _mean(closeadj, 5)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_5d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_growth_5d_x_closedif_10d_slope_v054_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 5)
    mid = base * closeadj.diff(1).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_5d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_growth_5d_ema_x_close_42d_slope_v055_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 5)
    mid = _ema(base, 2) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_10d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_growth_10d_x_close_5d_slope_v056_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 10)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_10d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_growth_10d_x_logclose_21d_slope_v057_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 10)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_10d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_growth_10d_x_meanclose_63d_slope_v058_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 10)
    mid = base * _mean(closeadj, 10)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_10d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_growth_10d_x_closedif_10d_slope_v059_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 10)
    mid = base * closeadj.diff(2).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_10d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_growth_10d_ema_x_close_42d_slope_v060_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 10)
    mid = _ema(base, 5) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_21d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_growth_21d_x_close_5d_slope_v061_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 21)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_21d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_growth_21d_x_logclose_21d_slope_v062_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 21)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_21d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_growth_21d_x_meanclose_63d_slope_v063_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 21)
    mid = base * _mean(closeadj, 21)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_21d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_growth_21d_x_closedif_10d_slope_v064_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 21)
    mid = base * closeadj.diff(5).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_21d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_growth_21d_ema_x_close_42d_slope_v065_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 21)
    mid = _ema(base, 10) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_42d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_growth_42d_x_close_5d_slope_v066_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 42)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_42d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_growth_42d_x_logclose_21d_slope_v067_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 42)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_42d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_growth_42d_x_meanclose_63d_slope_v068_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 42)
    mid = base * _mean(closeadj, 42)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_42d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_growth_42d_x_closedif_10d_slope_v069_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 42)
    mid = base * closeadj.diff(10).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_42d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_growth_42d_ema_x_close_42d_slope_v070_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 42)
    mid = _ema(base, 21) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_63d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_growth_63d_x_close_5d_slope_v071_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 63)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_63d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_growth_63d_x_logclose_21d_slope_v072_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 63)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_63d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_growth_63d_x_meanclose_63d_slope_v073_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 63)
    mid = base * _mean(closeadj, 63)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_63d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_growth_63d_x_closedif_10d_slope_v074_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 63)
    mid = base * closeadj.diff(15).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_63d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_growth_63d_ema_x_close_42d_slope_v075_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 63)
    mid = _ema(base, 31) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_126d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_growth_126d_x_close_5d_slope_v076_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 126)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_126d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_growth_126d_x_logclose_21d_slope_v077_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 126)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_126d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_growth_126d_x_meanclose_63d_slope_v078_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 126)
    mid = base * _mean(closeadj, 126)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_126d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_growth_126d_x_closedif_10d_slope_v079_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 126)
    mid = base * closeadj.diff(31).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_126d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_growth_126d_ema_x_close_42d_slope_v080_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 126)
    mid = _ema(base, 63) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_189d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_growth_189d_x_close_5d_slope_v081_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 189)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_189d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_growth_189d_x_logclose_21d_slope_v082_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 189)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_189d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_growth_189d_x_meanclose_63d_slope_v083_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 189)
    mid = base * _mean(closeadj, 189)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_189d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_growth_189d_x_closedif_10d_slope_v084_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 189)
    mid = base * closeadj.diff(47).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_189d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_growth_189d_ema_x_close_42d_slope_v085_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 189)
    mid = _ema(base, 94) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_252d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_growth_252d_x_close_5d_slope_v086_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 252)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_252d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_growth_252d_x_logclose_21d_slope_v087_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 252)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_252d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_growth_252d_x_meanclose_63d_slope_v088_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 252)
    mid = base * _mean(closeadj, 252)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_252d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_growth_252d_x_closedif_10d_slope_v089_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 252)
    mid = base * closeadj.diff(63).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_252d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_growth_252d_ema_x_close_42d_slope_v090_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 252)
    mid = _ema(base, 126) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_378d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_growth_378d_x_close_5d_slope_v091_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 378)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_378d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_growth_378d_x_logclose_21d_slope_v092_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 378)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_378d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_growth_378d_x_meanclose_63d_slope_v093_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 378)
    mid = base * _mean(closeadj, 378)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_378d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_growth_378d_x_closedif_10d_slope_v094_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 378)
    mid = base * closeadj.diff(94).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_378d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_growth_378d_ema_x_close_42d_slope_v095_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 378)
    mid = _ema(base, 189) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_504d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_growth_504d_x_close_5d_slope_v096_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 504)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_504d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_growth_504d_x_logclose_21d_slope_v097_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 504)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_504d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_growth_504d_x_meanclose_63d_slope_v098_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 504)
    mid = base * _mean(closeadj, 504)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_504d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_growth_504d_x_closedif_10d_slope_v099_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 504)
    mid = base * closeadj.diff(126).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# growth_504d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_growth_504d_ema_x_close_42d_slope_v100_signal(revenue, closeadj):
    base = _f069_growth_rate(revenue, 504)
    mid = _ema(base, 252) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_5d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_persist_5d_x_close_5d_slope_v101_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 5)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_5d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_persist_5d_x_logclose_21d_slope_v102_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 5)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_5d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_persist_5d_x_meanclose_63d_slope_v103_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 5)
    mid = base * _mean(closeadj, 5)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_5d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_persist_5d_x_closedif_10d_slope_v104_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 5)
    mid = base * closeadj.diff(1).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_5d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_persist_5d_ema_x_close_42d_slope_v105_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 5)
    mid = _ema(base, 2) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_10d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_persist_10d_x_close_5d_slope_v106_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 10)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_10d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_persist_10d_x_logclose_21d_slope_v107_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 10)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_10d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_persist_10d_x_meanclose_63d_slope_v108_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 10)
    mid = base * _mean(closeadj, 10)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_10d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_persist_10d_x_closedif_10d_slope_v109_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 10)
    mid = base * closeadj.diff(2).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_10d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_persist_10d_ema_x_close_42d_slope_v110_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 10)
    mid = _ema(base, 5) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_21d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_persist_21d_x_close_5d_slope_v111_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 21)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_21d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_persist_21d_x_logclose_21d_slope_v112_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 21)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_21d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_persist_21d_x_meanclose_63d_slope_v113_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 21)
    mid = base * _mean(closeadj, 21)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_21d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_persist_21d_x_closedif_10d_slope_v114_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 21)
    mid = base * closeadj.diff(5).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_21d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_persist_21d_ema_x_close_42d_slope_v115_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 21)
    mid = _ema(base, 10) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_42d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_persist_42d_x_close_5d_slope_v116_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 42)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_42d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_persist_42d_x_logclose_21d_slope_v117_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 42)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_42d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_persist_42d_x_meanclose_63d_slope_v118_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 42)
    mid = base * _mean(closeadj, 42)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_42d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_persist_42d_x_closedif_10d_slope_v119_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 42)
    mid = base * closeadj.diff(10).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_42d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_persist_42d_ema_x_close_42d_slope_v120_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 42)
    mid = _ema(base, 21) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_63d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_persist_63d_x_close_5d_slope_v121_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 63)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_63d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_persist_63d_x_logclose_21d_slope_v122_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 63)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_63d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_persist_63d_x_meanclose_63d_slope_v123_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 63)
    mid = base * _mean(closeadj, 63)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_63d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_persist_63d_x_closedif_10d_slope_v124_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 63)
    mid = base * closeadj.diff(15).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_63d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_persist_63d_ema_x_close_42d_slope_v125_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 63)
    mid = _ema(base, 31) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_126d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_persist_126d_x_close_5d_slope_v126_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 126)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_126d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_persist_126d_x_logclose_21d_slope_v127_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 126)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_126d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_persist_126d_x_meanclose_63d_slope_v128_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 126)
    mid = base * _mean(closeadj, 126)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_126d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_persist_126d_x_closedif_10d_slope_v129_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 126)
    mid = base * closeadj.diff(31).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_126d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_persist_126d_ema_x_close_42d_slope_v130_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 126)
    mid = _ema(base, 63) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_189d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_persist_189d_x_close_5d_slope_v131_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 189)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_189d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_persist_189d_x_logclose_21d_slope_v132_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 189)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_189d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_persist_189d_x_meanclose_63d_slope_v133_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 189)
    mid = base * _mean(closeadj, 189)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_189d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_persist_189d_x_closedif_10d_slope_v134_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 189)
    mid = base * closeadj.diff(47).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_189d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_persist_189d_ema_x_close_42d_slope_v135_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 189)
    mid = _ema(base, 94) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_252d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_persist_252d_x_close_5d_slope_v136_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 252)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_252d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_persist_252d_x_logclose_21d_slope_v137_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 252)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_252d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_persist_252d_x_meanclose_63d_slope_v138_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 252)
    mid = base * _mean(closeadj, 252)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_252d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_persist_252d_x_closedif_10d_slope_v139_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 252)
    mid = base * closeadj.diff(63).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_252d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_persist_252d_ema_x_close_42d_slope_v140_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 252)
    mid = _ema(base, 126) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_378d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_persist_378d_x_close_5d_slope_v141_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 378)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_378d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_persist_378d_x_logclose_21d_slope_v142_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 378)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_378d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_persist_378d_x_meanclose_63d_slope_v143_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 378)
    mid = base * _mean(closeadj, 378)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_378d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_persist_378d_x_closedif_10d_slope_v144_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 378)
    mid = base * closeadj.diff(94).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_378d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_persist_378d_ema_x_close_42d_slope_v145_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 378)
    mid = _ema(base, 189) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_504d_x_close_5d slope
def f069rgp_f069_revenue_growth_persistence_persist_504d_x_close_5d_slope_v146_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 504)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_504d_x_logclose_21d slope
def f069rgp_f069_revenue_growth_persistence_persist_504d_x_logclose_21d_slope_v147_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 504)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_504d_x_meanclose_63d slope
def f069rgp_f069_revenue_growth_persistence_persist_504d_x_meanclose_63d_slope_v148_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 504)
    mid = base * _mean(closeadj, 504)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_504d_x_closedif_10d slope
def f069rgp_f069_revenue_growth_persistence_persist_504d_x_closedif_10d_slope_v149_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 504)
    mid = base * closeadj.diff(126).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# persist_504d_ema_x_close_42d slope
def f069rgp_f069_revenue_growth_persistence_persist_504d_ema_x_close_42d_slope_v150_signal(revenue, closeadj):
    base = _f069_persistence_count(revenue, 504)
    mid = _ema(base, 252) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f069rgp_f069_revenue_growth_persistence_accel_5d_x_close_5d_slope_v001_signal,
    f069rgp_f069_revenue_growth_persistence_accel_5d_x_logclose_21d_slope_v002_signal,
    f069rgp_f069_revenue_growth_persistence_accel_5d_x_meanclose_63d_slope_v003_signal,
    f069rgp_f069_revenue_growth_persistence_accel_5d_x_closedif_10d_slope_v004_signal,
    f069rgp_f069_revenue_growth_persistence_accel_5d_ema_x_close_42d_slope_v005_signal,
    f069rgp_f069_revenue_growth_persistence_accel_10d_x_close_5d_slope_v006_signal,
    f069rgp_f069_revenue_growth_persistence_accel_10d_x_logclose_21d_slope_v007_signal,
    f069rgp_f069_revenue_growth_persistence_accel_10d_x_meanclose_63d_slope_v008_signal,
    f069rgp_f069_revenue_growth_persistence_accel_10d_x_closedif_10d_slope_v009_signal,
    f069rgp_f069_revenue_growth_persistence_accel_10d_ema_x_close_42d_slope_v010_signal,
    f069rgp_f069_revenue_growth_persistence_accel_21d_x_close_5d_slope_v011_signal,
    f069rgp_f069_revenue_growth_persistence_accel_21d_x_logclose_21d_slope_v012_signal,
    f069rgp_f069_revenue_growth_persistence_accel_21d_x_meanclose_63d_slope_v013_signal,
    f069rgp_f069_revenue_growth_persistence_accel_21d_x_closedif_10d_slope_v014_signal,
    f069rgp_f069_revenue_growth_persistence_accel_21d_ema_x_close_42d_slope_v015_signal,
    f069rgp_f069_revenue_growth_persistence_accel_42d_x_close_5d_slope_v016_signal,
    f069rgp_f069_revenue_growth_persistence_accel_42d_x_logclose_21d_slope_v017_signal,
    f069rgp_f069_revenue_growth_persistence_accel_42d_x_meanclose_63d_slope_v018_signal,
    f069rgp_f069_revenue_growth_persistence_accel_42d_x_closedif_10d_slope_v019_signal,
    f069rgp_f069_revenue_growth_persistence_accel_42d_ema_x_close_42d_slope_v020_signal,
    f069rgp_f069_revenue_growth_persistence_accel_63d_x_close_5d_slope_v021_signal,
    f069rgp_f069_revenue_growth_persistence_accel_63d_x_logclose_21d_slope_v022_signal,
    f069rgp_f069_revenue_growth_persistence_accel_63d_x_meanclose_63d_slope_v023_signal,
    f069rgp_f069_revenue_growth_persistence_accel_63d_x_closedif_10d_slope_v024_signal,
    f069rgp_f069_revenue_growth_persistence_accel_63d_ema_x_close_42d_slope_v025_signal,
    f069rgp_f069_revenue_growth_persistence_accel_126d_x_close_5d_slope_v026_signal,
    f069rgp_f069_revenue_growth_persistence_accel_126d_x_logclose_21d_slope_v027_signal,
    f069rgp_f069_revenue_growth_persistence_accel_126d_x_meanclose_63d_slope_v028_signal,
    f069rgp_f069_revenue_growth_persistence_accel_126d_x_closedif_10d_slope_v029_signal,
    f069rgp_f069_revenue_growth_persistence_accel_126d_ema_x_close_42d_slope_v030_signal,
    f069rgp_f069_revenue_growth_persistence_accel_189d_x_close_5d_slope_v031_signal,
    f069rgp_f069_revenue_growth_persistence_accel_189d_x_logclose_21d_slope_v032_signal,
    f069rgp_f069_revenue_growth_persistence_accel_189d_x_meanclose_63d_slope_v033_signal,
    f069rgp_f069_revenue_growth_persistence_accel_189d_x_closedif_10d_slope_v034_signal,
    f069rgp_f069_revenue_growth_persistence_accel_189d_ema_x_close_42d_slope_v035_signal,
    f069rgp_f069_revenue_growth_persistence_accel_252d_x_close_5d_slope_v036_signal,
    f069rgp_f069_revenue_growth_persistence_accel_252d_x_logclose_21d_slope_v037_signal,
    f069rgp_f069_revenue_growth_persistence_accel_252d_x_meanclose_63d_slope_v038_signal,
    f069rgp_f069_revenue_growth_persistence_accel_252d_x_closedif_10d_slope_v039_signal,
    f069rgp_f069_revenue_growth_persistence_accel_252d_ema_x_close_42d_slope_v040_signal,
    f069rgp_f069_revenue_growth_persistence_accel_378d_x_close_5d_slope_v041_signal,
    f069rgp_f069_revenue_growth_persistence_accel_378d_x_logclose_21d_slope_v042_signal,
    f069rgp_f069_revenue_growth_persistence_accel_378d_x_meanclose_63d_slope_v043_signal,
    f069rgp_f069_revenue_growth_persistence_accel_378d_x_closedif_10d_slope_v044_signal,
    f069rgp_f069_revenue_growth_persistence_accel_378d_ema_x_close_42d_slope_v045_signal,
    f069rgp_f069_revenue_growth_persistence_accel_504d_x_close_5d_slope_v046_signal,
    f069rgp_f069_revenue_growth_persistence_accel_504d_x_logclose_21d_slope_v047_signal,
    f069rgp_f069_revenue_growth_persistence_accel_504d_x_meanclose_63d_slope_v048_signal,
    f069rgp_f069_revenue_growth_persistence_accel_504d_x_closedif_10d_slope_v049_signal,
    f069rgp_f069_revenue_growth_persistence_accel_504d_ema_x_close_42d_slope_v050_signal,
    f069rgp_f069_revenue_growth_persistence_growth_5d_x_close_5d_slope_v051_signal,
    f069rgp_f069_revenue_growth_persistence_growth_5d_x_logclose_21d_slope_v052_signal,
    f069rgp_f069_revenue_growth_persistence_growth_5d_x_meanclose_63d_slope_v053_signal,
    f069rgp_f069_revenue_growth_persistence_growth_5d_x_closedif_10d_slope_v054_signal,
    f069rgp_f069_revenue_growth_persistence_growth_5d_ema_x_close_42d_slope_v055_signal,
    f069rgp_f069_revenue_growth_persistence_growth_10d_x_close_5d_slope_v056_signal,
    f069rgp_f069_revenue_growth_persistence_growth_10d_x_logclose_21d_slope_v057_signal,
    f069rgp_f069_revenue_growth_persistence_growth_10d_x_meanclose_63d_slope_v058_signal,
    f069rgp_f069_revenue_growth_persistence_growth_10d_x_closedif_10d_slope_v059_signal,
    f069rgp_f069_revenue_growth_persistence_growth_10d_ema_x_close_42d_slope_v060_signal,
    f069rgp_f069_revenue_growth_persistence_growth_21d_x_close_5d_slope_v061_signal,
    f069rgp_f069_revenue_growth_persistence_growth_21d_x_logclose_21d_slope_v062_signal,
    f069rgp_f069_revenue_growth_persistence_growth_21d_x_meanclose_63d_slope_v063_signal,
    f069rgp_f069_revenue_growth_persistence_growth_21d_x_closedif_10d_slope_v064_signal,
    f069rgp_f069_revenue_growth_persistence_growth_21d_ema_x_close_42d_slope_v065_signal,
    f069rgp_f069_revenue_growth_persistence_growth_42d_x_close_5d_slope_v066_signal,
    f069rgp_f069_revenue_growth_persistence_growth_42d_x_logclose_21d_slope_v067_signal,
    f069rgp_f069_revenue_growth_persistence_growth_42d_x_meanclose_63d_slope_v068_signal,
    f069rgp_f069_revenue_growth_persistence_growth_42d_x_closedif_10d_slope_v069_signal,
    f069rgp_f069_revenue_growth_persistence_growth_42d_ema_x_close_42d_slope_v070_signal,
    f069rgp_f069_revenue_growth_persistence_growth_63d_x_close_5d_slope_v071_signal,
    f069rgp_f069_revenue_growth_persistence_growth_63d_x_logclose_21d_slope_v072_signal,
    f069rgp_f069_revenue_growth_persistence_growth_63d_x_meanclose_63d_slope_v073_signal,
    f069rgp_f069_revenue_growth_persistence_growth_63d_x_closedif_10d_slope_v074_signal,
    f069rgp_f069_revenue_growth_persistence_growth_63d_ema_x_close_42d_slope_v075_signal,
    f069rgp_f069_revenue_growth_persistence_growth_126d_x_close_5d_slope_v076_signal,
    f069rgp_f069_revenue_growth_persistence_growth_126d_x_logclose_21d_slope_v077_signal,
    f069rgp_f069_revenue_growth_persistence_growth_126d_x_meanclose_63d_slope_v078_signal,
    f069rgp_f069_revenue_growth_persistence_growth_126d_x_closedif_10d_slope_v079_signal,
    f069rgp_f069_revenue_growth_persistence_growth_126d_ema_x_close_42d_slope_v080_signal,
    f069rgp_f069_revenue_growth_persistence_growth_189d_x_close_5d_slope_v081_signal,
    f069rgp_f069_revenue_growth_persistence_growth_189d_x_logclose_21d_slope_v082_signal,
    f069rgp_f069_revenue_growth_persistence_growth_189d_x_meanclose_63d_slope_v083_signal,
    f069rgp_f069_revenue_growth_persistence_growth_189d_x_closedif_10d_slope_v084_signal,
    f069rgp_f069_revenue_growth_persistence_growth_189d_ema_x_close_42d_slope_v085_signal,
    f069rgp_f069_revenue_growth_persistence_growth_252d_x_close_5d_slope_v086_signal,
    f069rgp_f069_revenue_growth_persistence_growth_252d_x_logclose_21d_slope_v087_signal,
    f069rgp_f069_revenue_growth_persistence_growth_252d_x_meanclose_63d_slope_v088_signal,
    f069rgp_f069_revenue_growth_persistence_growth_252d_x_closedif_10d_slope_v089_signal,
    f069rgp_f069_revenue_growth_persistence_growth_252d_ema_x_close_42d_slope_v090_signal,
    f069rgp_f069_revenue_growth_persistence_growth_378d_x_close_5d_slope_v091_signal,
    f069rgp_f069_revenue_growth_persistence_growth_378d_x_logclose_21d_slope_v092_signal,
    f069rgp_f069_revenue_growth_persistence_growth_378d_x_meanclose_63d_slope_v093_signal,
    f069rgp_f069_revenue_growth_persistence_growth_378d_x_closedif_10d_slope_v094_signal,
    f069rgp_f069_revenue_growth_persistence_growth_378d_ema_x_close_42d_slope_v095_signal,
    f069rgp_f069_revenue_growth_persistence_growth_504d_x_close_5d_slope_v096_signal,
    f069rgp_f069_revenue_growth_persistence_growth_504d_x_logclose_21d_slope_v097_signal,
    f069rgp_f069_revenue_growth_persistence_growth_504d_x_meanclose_63d_slope_v098_signal,
    f069rgp_f069_revenue_growth_persistence_growth_504d_x_closedif_10d_slope_v099_signal,
    f069rgp_f069_revenue_growth_persistence_growth_504d_ema_x_close_42d_slope_v100_signal,
    f069rgp_f069_revenue_growth_persistence_persist_5d_x_close_5d_slope_v101_signal,
    f069rgp_f069_revenue_growth_persistence_persist_5d_x_logclose_21d_slope_v102_signal,
    f069rgp_f069_revenue_growth_persistence_persist_5d_x_meanclose_63d_slope_v103_signal,
    f069rgp_f069_revenue_growth_persistence_persist_5d_x_closedif_10d_slope_v104_signal,
    f069rgp_f069_revenue_growth_persistence_persist_5d_ema_x_close_42d_slope_v105_signal,
    f069rgp_f069_revenue_growth_persistence_persist_10d_x_close_5d_slope_v106_signal,
    f069rgp_f069_revenue_growth_persistence_persist_10d_x_logclose_21d_slope_v107_signal,
    f069rgp_f069_revenue_growth_persistence_persist_10d_x_meanclose_63d_slope_v108_signal,
    f069rgp_f069_revenue_growth_persistence_persist_10d_x_closedif_10d_slope_v109_signal,
    f069rgp_f069_revenue_growth_persistence_persist_10d_ema_x_close_42d_slope_v110_signal,
    f069rgp_f069_revenue_growth_persistence_persist_21d_x_close_5d_slope_v111_signal,
    f069rgp_f069_revenue_growth_persistence_persist_21d_x_logclose_21d_slope_v112_signal,
    f069rgp_f069_revenue_growth_persistence_persist_21d_x_meanclose_63d_slope_v113_signal,
    f069rgp_f069_revenue_growth_persistence_persist_21d_x_closedif_10d_slope_v114_signal,
    f069rgp_f069_revenue_growth_persistence_persist_21d_ema_x_close_42d_slope_v115_signal,
    f069rgp_f069_revenue_growth_persistence_persist_42d_x_close_5d_slope_v116_signal,
    f069rgp_f069_revenue_growth_persistence_persist_42d_x_logclose_21d_slope_v117_signal,
    f069rgp_f069_revenue_growth_persistence_persist_42d_x_meanclose_63d_slope_v118_signal,
    f069rgp_f069_revenue_growth_persistence_persist_42d_x_closedif_10d_slope_v119_signal,
    f069rgp_f069_revenue_growth_persistence_persist_42d_ema_x_close_42d_slope_v120_signal,
    f069rgp_f069_revenue_growth_persistence_persist_63d_x_close_5d_slope_v121_signal,
    f069rgp_f069_revenue_growth_persistence_persist_63d_x_logclose_21d_slope_v122_signal,
    f069rgp_f069_revenue_growth_persistence_persist_63d_x_meanclose_63d_slope_v123_signal,
    f069rgp_f069_revenue_growth_persistence_persist_63d_x_closedif_10d_slope_v124_signal,
    f069rgp_f069_revenue_growth_persistence_persist_63d_ema_x_close_42d_slope_v125_signal,
    f069rgp_f069_revenue_growth_persistence_persist_126d_x_close_5d_slope_v126_signal,
    f069rgp_f069_revenue_growth_persistence_persist_126d_x_logclose_21d_slope_v127_signal,
    f069rgp_f069_revenue_growth_persistence_persist_126d_x_meanclose_63d_slope_v128_signal,
    f069rgp_f069_revenue_growth_persistence_persist_126d_x_closedif_10d_slope_v129_signal,
    f069rgp_f069_revenue_growth_persistence_persist_126d_ema_x_close_42d_slope_v130_signal,
    f069rgp_f069_revenue_growth_persistence_persist_189d_x_close_5d_slope_v131_signal,
    f069rgp_f069_revenue_growth_persistence_persist_189d_x_logclose_21d_slope_v132_signal,
    f069rgp_f069_revenue_growth_persistence_persist_189d_x_meanclose_63d_slope_v133_signal,
    f069rgp_f069_revenue_growth_persistence_persist_189d_x_closedif_10d_slope_v134_signal,
    f069rgp_f069_revenue_growth_persistence_persist_189d_ema_x_close_42d_slope_v135_signal,
    f069rgp_f069_revenue_growth_persistence_persist_252d_x_close_5d_slope_v136_signal,
    f069rgp_f069_revenue_growth_persistence_persist_252d_x_logclose_21d_slope_v137_signal,
    f069rgp_f069_revenue_growth_persistence_persist_252d_x_meanclose_63d_slope_v138_signal,
    f069rgp_f069_revenue_growth_persistence_persist_252d_x_closedif_10d_slope_v139_signal,
    f069rgp_f069_revenue_growth_persistence_persist_252d_ema_x_close_42d_slope_v140_signal,
    f069rgp_f069_revenue_growth_persistence_persist_378d_x_close_5d_slope_v141_signal,
    f069rgp_f069_revenue_growth_persistence_persist_378d_x_logclose_21d_slope_v142_signal,
    f069rgp_f069_revenue_growth_persistence_persist_378d_x_meanclose_63d_slope_v143_signal,
    f069rgp_f069_revenue_growth_persistence_persist_378d_x_closedif_10d_slope_v144_signal,
    f069rgp_f069_revenue_growth_persistence_persist_378d_ema_x_close_42d_slope_v145_signal,
    f069rgp_f069_revenue_growth_persistence_persist_504d_x_close_5d_slope_v146_signal,
    f069rgp_f069_revenue_growth_persistence_persist_504d_x_logclose_21d_slope_v147_signal,
    f069rgp_f069_revenue_growth_persistence_persist_504d_x_meanclose_63d_slope_v148_signal,
    f069rgp_f069_revenue_growth_persistence_persist_504d_x_closedif_10d_slope_v149_signal,
    f069rgp_f069_revenue_growth_persistence_persist_504d_ema_x_close_42d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F069_REVENUE_GROWTH_PERSISTENCE_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f069_growth_rate', '_f069_consec_accelerating', '_f069_persistence_count')
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
    print(f"OK f069_revenue_growth_persistence_slope_2nd_derivatives_001_150_claude: {n_features} features pass")
