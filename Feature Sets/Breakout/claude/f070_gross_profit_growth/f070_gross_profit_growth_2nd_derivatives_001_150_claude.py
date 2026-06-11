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
def _f070_gp_yoy(gp, w):
    return gp.pct_change(periods=w)


def _f070_gp_acceleration(gp, w):
    # acceleration of gross profit growth
    sw = max(2, w // 4)
    short = gp.pct_change(periods=sw)
    long = gp.pct_change(periods=w)
    return short - long


def _f070_quality_growth(gp, revenue, w):
    # gp growth minus revenue growth — quality of growth (margin expansion)
    gg = gp.pct_change(periods=w)
    rg = revenue.pct_change(periods=w)
    return gg - rg


# gpaccel_5d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpaccel_5d_x_close_5d_slope_v001_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 5)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_5d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpaccel_5d_x_logclose_21d_slope_v002_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 5)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_5d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpaccel_5d_x_meanclose_63d_slope_v003_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 5)
    mid = base * _mean(closeadj, 5)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_5d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpaccel_5d_x_closedif_10d_slope_v004_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 5)
    mid = base * closeadj.diff(1).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_5d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpaccel_5d_ema_x_close_42d_slope_v005_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 5)
    mid = _ema(base, 2) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_10d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpaccel_10d_x_close_5d_slope_v006_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 10)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_10d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpaccel_10d_x_logclose_21d_slope_v007_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 10)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_10d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpaccel_10d_x_meanclose_63d_slope_v008_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 10)
    mid = base * _mean(closeadj, 10)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_10d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpaccel_10d_x_closedif_10d_slope_v009_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 10)
    mid = base * closeadj.diff(2).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_10d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpaccel_10d_ema_x_close_42d_slope_v010_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 10)
    mid = _ema(base, 5) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_21d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpaccel_21d_x_close_5d_slope_v011_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 21)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_21d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpaccel_21d_x_logclose_21d_slope_v012_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 21)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_21d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpaccel_21d_x_meanclose_63d_slope_v013_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 21)
    mid = base * _mean(closeadj, 21)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_21d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpaccel_21d_x_closedif_10d_slope_v014_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 21)
    mid = base * closeadj.diff(5).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_21d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpaccel_21d_ema_x_close_42d_slope_v015_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 21)
    mid = _ema(base, 10) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_42d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpaccel_42d_x_close_5d_slope_v016_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 42)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_42d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpaccel_42d_x_logclose_21d_slope_v017_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 42)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_42d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpaccel_42d_x_meanclose_63d_slope_v018_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 42)
    mid = base * _mean(closeadj, 42)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_42d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpaccel_42d_x_closedif_10d_slope_v019_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 42)
    mid = base * closeadj.diff(10).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_42d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpaccel_42d_ema_x_close_42d_slope_v020_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 42)
    mid = _ema(base, 21) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_63d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpaccel_63d_x_close_5d_slope_v021_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 63)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_63d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpaccel_63d_x_logclose_21d_slope_v022_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 63)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_63d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpaccel_63d_x_meanclose_63d_slope_v023_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 63)
    mid = base * _mean(closeadj, 63)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_63d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpaccel_63d_x_closedif_10d_slope_v024_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 63)
    mid = base * closeadj.diff(15).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_63d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpaccel_63d_ema_x_close_42d_slope_v025_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 63)
    mid = _ema(base, 31) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_126d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpaccel_126d_x_close_5d_slope_v026_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 126)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_126d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpaccel_126d_x_logclose_21d_slope_v027_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 126)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_126d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpaccel_126d_x_meanclose_63d_slope_v028_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 126)
    mid = base * _mean(closeadj, 126)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_126d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpaccel_126d_x_closedif_10d_slope_v029_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 126)
    mid = base * closeadj.diff(31).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_126d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpaccel_126d_ema_x_close_42d_slope_v030_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 126)
    mid = _ema(base, 63) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_189d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpaccel_189d_x_close_5d_slope_v031_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 189)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_189d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpaccel_189d_x_logclose_21d_slope_v032_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 189)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_189d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpaccel_189d_x_meanclose_63d_slope_v033_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 189)
    mid = base * _mean(closeadj, 189)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_189d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpaccel_189d_x_closedif_10d_slope_v034_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 189)
    mid = base * closeadj.diff(47).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_189d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpaccel_189d_ema_x_close_42d_slope_v035_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 189)
    mid = _ema(base, 94) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_252d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpaccel_252d_x_close_5d_slope_v036_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 252)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_252d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpaccel_252d_x_logclose_21d_slope_v037_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 252)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_252d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpaccel_252d_x_meanclose_63d_slope_v038_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 252)
    mid = base * _mean(closeadj, 252)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_252d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpaccel_252d_x_closedif_10d_slope_v039_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 252)
    mid = base * closeadj.diff(63).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_252d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpaccel_252d_ema_x_close_42d_slope_v040_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 252)
    mid = _ema(base, 126) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_378d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpaccel_378d_x_close_5d_slope_v041_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 378)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_378d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpaccel_378d_x_logclose_21d_slope_v042_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 378)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_378d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpaccel_378d_x_meanclose_63d_slope_v043_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 378)
    mid = base * _mean(closeadj, 378)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_378d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpaccel_378d_x_closedif_10d_slope_v044_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 378)
    mid = base * closeadj.diff(94).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_378d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpaccel_378d_ema_x_close_42d_slope_v045_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 378)
    mid = _ema(base, 189) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_504d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpaccel_504d_x_close_5d_slope_v046_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 504)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_504d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpaccel_504d_x_logclose_21d_slope_v047_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 504)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_504d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpaccel_504d_x_meanclose_63d_slope_v048_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 504)
    mid = base * _mean(closeadj, 504)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_504d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpaccel_504d_x_closedif_10d_slope_v049_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 504)
    mid = base * closeadj.diff(126).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_504d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpaccel_504d_ema_x_close_42d_slope_v050_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 504)
    mid = _ema(base, 252) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_5d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpyoy_5d_x_close_5d_slope_v051_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 5)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_5d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpyoy_5d_x_logclose_21d_slope_v052_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 5)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_5d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpyoy_5d_x_meanclose_63d_slope_v053_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 5)
    mid = base * _mean(closeadj, 5)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_5d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpyoy_5d_x_closedif_10d_slope_v054_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 5)
    mid = base * closeadj.diff(1).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_5d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpyoy_5d_ema_x_close_42d_slope_v055_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 5)
    mid = _ema(base, 2) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_10d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpyoy_10d_x_close_5d_slope_v056_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 10)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_10d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpyoy_10d_x_logclose_21d_slope_v057_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 10)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_10d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpyoy_10d_x_meanclose_63d_slope_v058_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 10)
    mid = base * _mean(closeadj, 10)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_10d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpyoy_10d_x_closedif_10d_slope_v059_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 10)
    mid = base * closeadj.diff(2).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_10d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpyoy_10d_ema_x_close_42d_slope_v060_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 10)
    mid = _ema(base, 5) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_21d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpyoy_21d_x_close_5d_slope_v061_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 21)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_21d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpyoy_21d_x_logclose_21d_slope_v062_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 21)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_21d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpyoy_21d_x_meanclose_63d_slope_v063_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 21)
    mid = base * _mean(closeadj, 21)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_21d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpyoy_21d_x_closedif_10d_slope_v064_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 21)
    mid = base * closeadj.diff(5).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_21d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpyoy_21d_ema_x_close_42d_slope_v065_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 21)
    mid = _ema(base, 10) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_42d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpyoy_42d_x_close_5d_slope_v066_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 42)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_42d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpyoy_42d_x_logclose_21d_slope_v067_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 42)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_42d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpyoy_42d_x_meanclose_63d_slope_v068_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 42)
    mid = base * _mean(closeadj, 42)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_42d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpyoy_42d_x_closedif_10d_slope_v069_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 42)
    mid = base * closeadj.diff(10).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_42d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpyoy_42d_ema_x_close_42d_slope_v070_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 42)
    mid = _ema(base, 21) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_63d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpyoy_63d_x_close_5d_slope_v071_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 63)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_63d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpyoy_63d_x_logclose_21d_slope_v072_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 63)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_63d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpyoy_63d_x_meanclose_63d_slope_v073_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 63)
    mid = base * _mean(closeadj, 63)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_63d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpyoy_63d_x_closedif_10d_slope_v074_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 63)
    mid = base * closeadj.diff(15).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_63d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpyoy_63d_ema_x_close_42d_slope_v075_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 63)
    mid = _ema(base, 31) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_126d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpyoy_126d_x_close_5d_slope_v076_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 126)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_126d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpyoy_126d_x_logclose_21d_slope_v077_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 126)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_126d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpyoy_126d_x_meanclose_63d_slope_v078_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 126)
    mid = base * _mean(closeadj, 126)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_126d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpyoy_126d_x_closedif_10d_slope_v079_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 126)
    mid = base * closeadj.diff(31).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_126d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpyoy_126d_ema_x_close_42d_slope_v080_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 126)
    mid = _ema(base, 63) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_189d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpyoy_189d_x_close_5d_slope_v081_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 189)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_189d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpyoy_189d_x_logclose_21d_slope_v082_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 189)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_189d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpyoy_189d_x_meanclose_63d_slope_v083_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 189)
    mid = base * _mean(closeadj, 189)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_189d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpyoy_189d_x_closedif_10d_slope_v084_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 189)
    mid = base * closeadj.diff(47).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_189d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpyoy_189d_ema_x_close_42d_slope_v085_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 189)
    mid = _ema(base, 94) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_252d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpyoy_252d_x_close_5d_slope_v086_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 252)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_252d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpyoy_252d_x_logclose_21d_slope_v087_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 252)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_252d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpyoy_252d_x_meanclose_63d_slope_v088_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 252)
    mid = base * _mean(closeadj, 252)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_252d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpyoy_252d_x_closedif_10d_slope_v089_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 252)
    mid = base * closeadj.diff(63).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_252d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpyoy_252d_ema_x_close_42d_slope_v090_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 252)
    mid = _ema(base, 126) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_378d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpyoy_378d_x_close_5d_slope_v091_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 378)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_378d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpyoy_378d_x_logclose_21d_slope_v092_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 378)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_378d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpyoy_378d_x_meanclose_63d_slope_v093_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 378)
    mid = base * _mean(closeadj, 378)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_378d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpyoy_378d_x_closedif_10d_slope_v094_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 378)
    mid = base * closeadj.diff(94).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_378d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpyoy_378d_ema_x_close_42d_slope_v095_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 378)
    mid = _ema(base, 189) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_504d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_gpyoy_504d_x_close_5d_slope_v096_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 504)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_504d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_gpyoy_504d_x_logclose_21d_slope_v097_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 504)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_504d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_gpyoy_504d_x_meanclose_63d_slope_v098_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 504)
    mid = base * _mean(closeadj, 504)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_504d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_gpyoy_504d_x_closedif_10d_slope_v099_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 504)
    mid = base * closeadj.diff(126).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_504d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_gpyoy_504d_ema_x_close_42d_slope_v100_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 504)
    mid = _ema(base, 252) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_5d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_qualgrow_5d_x_close_5d_slope_v101_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 5)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_5d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_qualgrow_5d_x_logclose_21d_slope_v102_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 5)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_5d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_qualgrow_5d_x_meanclose_63d_slope_v103_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 5)
    mid = base * _mean(closeadj, 5)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_5d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_qualgrow_5d_x_closedif_10d_slope_v104_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 5)
    mid = base * closeadj.diff(1).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_5d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_qualgrow_5d_ema_x_close_42d_slope_v105_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 5)
    mid = _ema(base, 2) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_10d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_qualgrow_10d_x_close_5d_slope_v106_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 10)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_10d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_qualgrow_10d_x_logclose_21d_slope_v107_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 10)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_10d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_qualgrow_10d_x_meanclose_63d_slope_v108_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 10)
    mid = base * _mean(closeadj, 10)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_10d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_qualgrow_10d_x_closedif_10d_slope_v109_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 10)
    mid = base * closeadj.diff(2).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_10d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_qualgrow_10d_ema_x_close_42d_slope_v110_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 10)
    mid = _ema(base, 5) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_21d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_qualgrow_21d_x_close_5d_slope_v111_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 21)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_21d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_qualgrow_21d_x_logclose_21d_slope_v112_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 21)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_21d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_qualgrow_21d_x_meanclose_63d_slope_v113_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 21)
    mid = base * _mean(closeadj, 21)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_21d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_qualgrow_21d_x_closedif_10d_slope_v114_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 21)
    mid = base * closeadj.diff(5).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_21d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_qualgrow_21d_ema_x_close_42d_slope_v115_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 21)
    mid = _ema(base, 10) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_42d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_qualgrow_42d_x_close_5d_slope_v116_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 42)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_42d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_qualgrow_42d_x_logclose_21d_slope_v117_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 42)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_42d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_qualgrow_42d_x_meanclose_63d_slope_v118_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 42)
    mid = base * _mean(closeadj, 42)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_42d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_qualgrow_42d_x_closedif_10d_slope_v119_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 42)
    mid = base * closeadj.diff(10).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_42d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_qualgrow_42d_ema_x_close_42d_slope_v120_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 42)
    mid = _ema(base, 21) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_63d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_qualgrow_63d_x_close_5d_slope_v121_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 63)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_63d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_qualgrow_63d_x_logclose_21d_slope_v122_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 63)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_63d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_qualgrow_63d_x_meanclose_63d_slope_v123_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 63)
    mid = base * _mean(closeadj, 63)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_63d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_qualgrow_63d_x_closedif_10d_slope_v124_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 63)
    mid = base * closeadj.diff(15).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_63d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_qualgrow_63d_ema_x_close_42d_slope_v125_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 63)
    mid = _ema(base, 31) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_126d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_qualgrow_126d_x_close_5d_slope_v126_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 126)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_126d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_qualgrow_126d_x_logclose_21d_slope_v127_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 126)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_126d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_qualgrow_126d_x_meanclose_63d_slope_v128_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 126)
    mid = base * _mean(closeadj, 126)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_126d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_qualgrow_126d_x_closedif_10d_slope_v129_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 126)
    mid = base * closeadj.diff(31).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_126d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_qualgrow_126d_ema_x_close_42d_slope_v130_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 126)
    mid = _ema(base, 63) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_189d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_qualgrow_189d_x_close_5d_slope_v131_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 189)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_189d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_qualgrow_189d_x_logclose_21d_slope_v132_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 189)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_189d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_qualgrow_189d_x_meanclose_63d_slope_v133_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 189)
    mid = base * _mean(closeadj, 189)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_189d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_qualgrow_189d_x_closedif_10d_slope_v134_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 189)
    mid = base * closeadj.diff(47).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_189d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_qualgrow_189d_ema_x_close_42d_slope_v135_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 189)
    mid = _ema(base, 94) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_252d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_qualgrow_252d_x_close_5d_slope_v136_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 252)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_252d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_qualgrow_252d_x_logclose_21d_slope_v137_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 252)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_252d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_qualgrow_252d_x_meanclose_63d_slope_v138_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 252)
    mid = base * _mean(closeadj, 252)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_252d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_qualgrow_252d_x_closedif_10d_slope_v139_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 252)
    mid = base * closeadj.diff(63).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_252d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_qualgrow_252d_ema_x_close_42d_slope_v140_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 252)
    mid = _ema(base, 126) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_378d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_qualgrow_378d_x_close_5d_slope_v141_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 378)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_378d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_qualgrow_378d_x_logclose_21d_slope_v142_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 378)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_378d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_qualgrow_378d_x_meanclose_63d_slope_v143_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 378)
    mid = base * _mean(closeadj, 378)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_378d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_qualgrow_378d_x_closedif_10d_slope_v144_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 378)
    mid = base * closeadj.diff(94).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_378d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_qualgrow_378d_ema_x_close_42d_slope_v145_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 378)
    mid = _ema(base, 189) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_504d_x_close_5d slope
def f070gpg_f070_gross_profit_growth_qualgrow_504d_x_close_5d_slope_v146_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 504)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_504d_x_logclose_21d slope
def f070gpg_f070_gross_profit_growth_qualgrow_504d_x_logclose_21d_slope_v147_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 504)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_504d_x_meanclose_63d slope
def f070gpg_f070_gross_profit_growth_qualgrow_504d_x_meanclose_63d_slope_v148_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 504)
    mid = base * _mean(closeadj, 504)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_504d_x_closedif_10d slope
def f070gpg_f070_gross_profit_growth_qualgrow_504d_x_closedif_10d_slope_v149_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 504)
    mid = base * closeadj.diff(126).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_504d_ema_x_close_42d slope
def f070gpg_f070_gross_profit_growth_qualgrow_504d_ema_x_close_42d_slope_v150_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 504)
    mid = _ema(base, 252) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f070gpg_f070_gross_profit_growth_gpaccel_5d_x_close_5d_slope_v001_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_5d_x_logclose_21d_slope_v002_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_5d_x_meanclose_63d_slope_v003_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_5d_x_closedif_10d_slope_v004_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_5d_ema_x_close_42d_slope_v005_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_10d_x_close_5d_slope_v006_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_10d_x_logclose_21d_slope_v007_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_10d_x_meanclose_63d_slope_v008_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_10d_x_closedif_10d_slope_v009_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_10d_ema_x_close_42d_slope_v010_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_21d_x_close_5d_slope_v011_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_21d_x_logclose_21d_slope_v012_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_21d_x_meanclose_63d_slope_v013_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_21d_x_closedif_10d_slope_v014_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_21d_ema_x_close_42d_slope_v015_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_42d_x_close_5d_slope_v016_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_42d_x_logclose_21d_slope_v017_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_42d_x_meanclose_63d_slope_v018_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_42d_x_closedif_10d_slope_v019_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_42d_ema_x_close_42d_slope_v020_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_63d_x_close_5d_slope_v021_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_63d_x_logclose_21d_slope_v022_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_63d_x_meanclose_63d_slope_v023_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_63d_x_closedif_10d_slope_v024_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_63d_ema_x_close_42d_slope_v025_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_126d_x_close_5d_slope_v026_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_126d_x_logclose_21d_slope_v027_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_126d_x_meanclose_63d_slope_v028_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_126d_x_closedif_10d_slope_v029_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_126d_ema_x_close_42d_slope_v030_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_189d_x_close_5d_slope_v031_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_189d_x_logclose_21d_slope_v032_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_189d_x_meanclose_63d_slope_v033_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_189d_x_closedif_10d_slope_v034_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_189d_ema_x_close_42d_slope_v035_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_252d_x_close_5d_slope_v036_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_252d_x_logclose_21d_slope_v037_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_252d_x_meanclose_63d_slope_v038_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_252d_x_closedif_10d_slope_v039_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_252d_ema_x_close_42d_slope_v040_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_378d_x_close_5d_slope_v041_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_378d_x_logclose_21d_slope_v042_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_378d_x_meanclose_63d_slope_v043_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_378d_x_closedif_10d_slope_v044_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_378d_ema_x_close_42d_slope_v045_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_504d_x_close_5d_slope_v046_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_504d_x_logclose_21d_slope_v047_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_504d_x_meanclose_63d_slope_v048_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_504d_x_closedif_10d_slope_v049_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_504d_ema_x_close_42d_slope_v050_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_5d_x_close_5d_slope_v051_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_5d_x_logclose_21d_slope_v052_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_5d_x_meanclose_63d_slope_v053_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_5d_x_closedif_10d_slope_v054_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_5d_ema_x_close_42d_slope_v055_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_10d_x_close_5d_slope_v056_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_10d_x_logclose_21d_slope_v057_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_10d_x_meanclose_63d_slope_v058_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_10d_x_closedif_10d_slope_v059_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_10d_ema_x_close_42d_slope_v060_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_21d_x_close_5d_slope_v061_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_21d_x_logclose_21d_slope_v062_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_21d_x_meanclose_63d_slope_v063_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_21d_x_closedif_10d_slope_v064_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_21d_ema_x_close_42d_slope_v065_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_42d_x_close_5d_slope_v066_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_42d_x_logclose_21d_slope_v067_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_42d_x_meanclose_63d_slope_v068_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_42d_x_closedif_10d_slope_v069_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_42d_ema_x_close_42d_slope_v070_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_63d_x_close_5d_slope_v071_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_63d_x_logclose_21d_slope_v072_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_63d_x_meanclose_63d_slope_v073_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_63d_x_closedif_10d_slope_v074_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_63d_ema_x_close_42d_slope_v075_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_126d_x_close_5d_slope_v076_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_126d_x_logclose_21d_slope_v077_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_126d_x_meanclose_63d_slope_v078_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_126d_x_closedif_10d_slope_v079_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_126d_ema_x_close_42d_slope_v080_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_189d_x_close_5d_slope_v081_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_189d_x_logclose_21d_slope_v082_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_189d_x_meanclose_63d_slope_v083_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_189d_x_closedif_10d_slope_v084_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_189d_ema_x_close_42d_slope_v085_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_252d_x_close_5d_slope_v086_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_252d_x_logclose_21d_slope_v087_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_252d_x_meanclose_63d_slope_v088_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_252d_x_closedif_10d_slope_v089_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_252d_ema_x_close_42d_slope_v090_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_378d_x_close_5d_slope_v091_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_378d_x_logclose_21d_slope_v092_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_378d_x_meanclose_63d_slope_v093_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_378d_x_closedif_10d_slope_v094_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_378d_ema_x_close_42d_slope_v095_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_504d_x_close_5d_slope_v096_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_504d_x_logclose_21d_slope_v097_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_504d_x_meanclose_63d_slope_v098_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_504d_x_closedif_10d_slope_v099_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_504d_ema_x_close_42d_slope_v100_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_5d_x_close_5d_slope_v101_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_5d_x_logclose_21d_slope_v102_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_5d_x_meanclose_63d_slope_v103_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_5d_x_closedif_10d_slope_v104_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_5d_ema_x_close_42d_slope_v105_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_10d_x_close_5d_slope_v106_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_10d_x_logclose_21d_slope_v107_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_10d_x_meanclose_63d_slope_v108_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_10d_x_closedif_10d_slope_v109_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_10d_ema_x_close_42d_slope_v110_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_21d_x_close_5d_slope_v111_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_21d_x_logclose_21d_slope_v112_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_21d_x_meanclose_63d_slope_v113_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_21d_x_closedif_10d_slope_v114_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_21d_ema_x_close_42d_slope_v115_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_42d_x_close_5d_slope_v116_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_42d_x_logclose_21d_slope_v117_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_42d_x_meanclose_63d_slope_v118_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_42d_x_closedif_10d_slope_v119_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_42d_ema_x_close_42d_slope_v120_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_63d_x_close_5d_slope_v121_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_63d_x_logclose_21d_slope_v122_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_63d_x_meanclose_63d_slope_v123_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_63d_x_closedif_10d_slope_v124_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_63d_ema_x_close_42d_slope_v125_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_126d_x_close_5d_slope_v126_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_126d_x_logclose_21d_slope_v127_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_126d_x_meanclose_63d_slope_v128_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_126d_x_closedif_10d_slope_v129_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_126d_ema_x_close_42d_slope_v130_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_189d_x_close_5d_slope_v131_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_189d_x_logclose_21d_slope_v132_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_189d_x_meanclose_63d_slope_v133_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_189d_x_closedif_10d_slope_v134_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_189d_ema_x_close_42d_slope_v135_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_252d_x_close_5d_slope_v136_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_252d_x_logclose_21d_slope_v137_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_252d_x_meanclose_63d_slope_v138_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_252d_x_closedif_10d_slope_v139_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_252d_ema_x_close_42d_slope_v140_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_378d_x_close_5d_slope_v141_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_378d_x_logclose_21d_slope_v142_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_378d_x_meanclose_63d_slope_v143_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_378d_x_closedif_10d_slope_v144_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_378d_ema_x_close_42d_slope_v145_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_504d_x_close_5d_slope_v146_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_504d_x_logclose_21d_slope_v147_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_504d_x_meanclose_63d_slope_v148_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_504d_x_closedif_10d_slope_v149_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_504d_ema_x_close_42d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F070_GROSS_PROFIT_GROWTH_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    gp = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.007, n))), name="gp")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    cols = {
        "closeadj": closeadj,
        "gp": gp,
        "revenue": revenue,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f070_gp_yoy', '_f070_gp_acceleration', '_f070_quality_growth')
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
    print(f"OK f070_gross_profit_growth_slope_2nd_derivatives_001_150_claude: {n_features} features pass")
