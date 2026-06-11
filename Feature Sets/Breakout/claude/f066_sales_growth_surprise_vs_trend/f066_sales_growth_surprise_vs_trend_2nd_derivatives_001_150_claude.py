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
def _f066_trailing_growth(revenue, w):
    # long-window trailing growth (pct change)
    return revenue.pct_change(periods=w)


def _f066_recent_growth(revenue, w):
    # short-window recent growth, smaller window than trailing
    sw = max(2, w // 4)
    return revenue.pct_change(periods=sw)


def _f066_growth_surprise(revenue, w):
    # recent growth minus trailing growth — sales surprise vs trend
    sw = max(2, w // 4)
    rec = revenue.pct_change(periods=sw)
    trl = revenue.pct_change(periods=w)
    return rec - trl


# recent_5d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_5d_x_close_5d_slope_v001_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 5)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_5d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_5d_x_logclose_21d_slope_v002_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 5)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_5d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_5d_x_meanclose_63d_slope_v003_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 5)
    mid = base * _mean(closeadj, 5)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_5d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_5d_x_closedif_10d_slope_v004_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 5)
    mid = base * closeadj.diff(1).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_5d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_5d_ema_x_close_42d_slope_v005_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 5)
    mid = _ema(base, 2) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_10d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_10d_x_close_5d_slope_v006_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 10)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_10d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_10d_x_logclose_21d_slope_v007_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 10)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_10d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_10d_x_meanclose_63d_slope_v008_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 10)
    mid = base * _mean(closeadj, 10)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_10d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_10d_x_closedif_10d_slope_v009_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 10)
    mid = base * closeadj.diff(2).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_10d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_10d_ema_x_close_42d_slope_v010_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 10)
    mid = _ema(base, 5) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_21d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_21d_x_close_5d_slope_v011_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 21)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_21d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_21d_x_logclose_21d_slope_v012_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 21)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_21d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_21d_x_meanclose_63d_slope_v013_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 21)
    mid = base * _mean(closeadj, 21)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_21d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_21d_x_closedif_10d_slope_v014_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 21)
    mid = base * closeadj.diff(5).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_21d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_21d_ema_x_close_42d_slope_v015_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 21)
    mid = _ema(base, 10) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_42d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_42d_x_close_5d_slope_v016_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 42)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_42d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_42d_x_logclose_21d_slope_v017_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 42)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_42d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_42d_x_meanclose_63d_slope_v018_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 42)
    mid = base * _mean(closeadj, 42)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_42d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_42d_x_closedif_10d_slope_v019_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 42)
    mid = base * closeadj.diff(10).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_42d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_42d_ema_x_close_42d_slope_v020_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 42)
    mid = _ema(base, 21) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_63d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_63d_x_close_5d_slope_v021_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 63)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_63d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_63d_x_logclose_21d_slope_v022_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 63)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_63d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_63d_x_meanclose_63d_slope_v023_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 63)
    mid = base * _mean(closeadj, 63)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_63d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_63d_x_closedif_10d_slope_v024_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 63)
    mid = base * closeadj.diff(15).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_63d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_63d_ema_x_close_42d_slope_v025_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 63)
    mid = _ema(base, 31) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_126d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_x_close_5d_slope_v026_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 126)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_126d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_x_logclose_21d_slope_v027_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 126)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_126d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_x_meanclose_63d_slope_v028_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 126)
    mid = base * _mean(closeadj, 126)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_126d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_x_closedif_10d_slope_v029_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 126)
    mid = base * closeadj.diff(31).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_126d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_ema_x_close_42d_slope_v030_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 126)
    mid = _ema(base, 63) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_189d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_x_close_5d_slope_v031_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 189)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_189d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_x_logclose_21d_slope_v032_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 189)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_189d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_x_meanclose_63d_slope_v033_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 189)
    mid = base * _mean(closeadj, 189)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_189d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_x_closedif_10d_slope_v034_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 189)
    mid = base * closeadj.diff(47).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_189d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_ema_x_close_42d_slope_v035_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 189)
    mid = _ema(base, 94) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_252d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_x_close_5d_slope_v036_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 252)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_252d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_x_logclose_21d_slope_v037_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 252)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_252d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_x_meanclose_63d_slope_v038_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 252)
    mid = base * _mean(closeadj, 252)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_252d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_x_closedif_10d_slope_v039_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 252)
    mid = base * closeadj.diff(63).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_252d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_ema_x_close_42d_slope_v040_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 252)
    mid = _ema(base, 126) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_378d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_x_close_5d_slope_v041_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 378)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_378d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_x_logclose_21d_slope_v042_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 378)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_378d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_x_meanclose_63d_slope_v043_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 378)
    mid = base * _mean(closeadj, 378)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_378d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_x_closedif_10d_slope_v044_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 378)
    mid = base * closeadj.diff(94).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_378d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_ema_x_close_42d_slope_v045_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 378)
    mid = _ema(base, 189) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_504d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_x_close_5d_slope_v046_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 504)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_504d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_x_logclose_21d_slope_v047_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 504)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_504d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_x_meanclose_63d_slope_v048_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 504)
    mid = base * _mean(closeadj, 504)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_504d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_x_closedif_10d_slope_v049_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 504)
    mid = base * closeadj.diff(126).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_504d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_ema_x_close_42d_slope_v050_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 504)
    mid = _ema(base, 252) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_5d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_x_close_5d_slope_v051_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 5)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_5d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_x_logclose_21d_slope_v052_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 5)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_5d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_x_meanclose_63d_slope_v053_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 5)
    mid = base * _mean(closeadj, 5)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_5d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_x_closedif_10d_slope_v054_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 5)
    mid = base * closeadj.diff(1).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_5d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_ema_x_close_42d_slope_v055_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 5)
    mid = _ema(base, 2) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_10d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_x_close_5d_slope_v056_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 10)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_10d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_x_logclose_21d_slope_v057_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 10)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_10d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_x_meanclose_63d_slope_v058_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 10)
    mid = base * _mean(closeadj, 10)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_10d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_x_closedif_10d_slope_v059_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 10)
    mid = base * closeadj.diff(2).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_10d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_ema_x_close_42d_slope_v060_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 10)
    mid = _ema(base, 5) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_21d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_x_close_5d_slope_v061_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 21)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_21d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_x_logclose_21d_slope_v062_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 21)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_21d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_x_meanclose_63d_slope_v063_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 21)
    mid = base * _mean(closeadj, 21)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_21d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_x_closedif_10d_slope_v064_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 21)
    mid = base * closeadj.diff(5).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_21d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_ema_x_close_42d_slope_v065_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 21)
    mid = _ema(base, 10) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_42d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_x_close_5d_slope_v066_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 42)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_42d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_x_logclose_21d_slope_v067_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 42)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_42d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_x_meanclose_63d_slope_v068_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 42)
    mid = base * _mean(closeadj, 42)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_42d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_x_closedif_10d_slope_v069_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 42)
    mid = base * closeadj.diff(10).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_42d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_ema_x_close_42d_slope_v070_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 42)
    mid = _ema(base, 21) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_63d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_x_close_5d_slope_v071_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 63)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_63d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_x_logclose_21d_slope_v072_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 63)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_63d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_x_meanclose_63d_slope_v073_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 63)
    mid = base * _mean(closeadj, 63)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_63d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_x_closedif_10d_slope_v074_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 63)
    mid = base * closeadj.diff(15).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_63d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_ema_x_close_42d_slope_v075_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 63)
    mid = _ema(base, 31) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_126d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_x_close_5d_slope_v076_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 126)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_126d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_x_logclose_21d_slope_v077_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 126)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_126d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_x_meanclose_63d_slope_v078_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 126)
    mid = base * _mean(closeadj, 126)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_126d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_x_closedif_10d_slope_v079_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 126)
    mid = base * closeadj.diff(31).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_126d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_ema_x_close_42d_slope_v080_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 126)
    mid = _ema(base, 63) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_189d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_x_close_5d_slope_v081_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 189)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_189d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_x_logclose_21d_slope_v082_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 189)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_189d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_x_meanclose_63d_slope_v083_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 189)
    mid = base * _mean(closeadj, 189)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_189d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_x_closedif_10d_slope_v084_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 189)
    mid = base * closeadj.diff(47).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_189d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_ema_x_close_42d_slope_v085_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 189)
    mid = _ema(base, 94) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_252d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_x_close_5d_slope_v086_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 252)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_252d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_x_logclose_21d_slope_v087_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 252)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_252d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_x_meanclose_63d_slope_v088_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 252)
    mid = base * _mean(closeadj, 252)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_252d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_x_closedif_10d_slope_v089_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 252)
    mid = base * closeadj.diff(63).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_252d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_ema_x_close_42d_slope_v090_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 252)
    mid = _ema(base, 126) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_378d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_x_close_5d_slope_v091_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 378)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_378d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_x_logclose_21d_slope_v092_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 378)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_378d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_x_meanclose_63d_slope_v093_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 378)
    mid = base * _mean(closeadj, 378)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_378d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_x_closedif_10d_slope_v094_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 378)
    mid = base * closeadj.diff(94).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_378d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_ema_x_close_42d_slope_v095_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 378)
    mid = _ema(base, 189) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_504d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_x_close_5d_slope_v096_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 504)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_504d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_x_logclose_21d_slope_v097_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 504)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_504d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_x_meanclose_63d_slope_v098_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 504)
    mid = base * _mean(closeadj, 504)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_504d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_x_closedif_10d_slope_v099_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 504)
    mid = base * closeadj.diff(126).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_504d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_ema_x_close_42d_slope_v100_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 504)
    mid = _ema(base, 252) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_5d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_5d_x_close_5d_slope_v101_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 5)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_5d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_5d_x_logclose_21d_slope_v102_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 5)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_5d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_5d_x_meanclose_63d_slope_v103_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 5)
    mid = base * _mean(closeadj, 5)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_5d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_5d_x_closedif_10d_slope_v104_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 5)
    mid = base * closeadj.diff(1).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_5d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_5d_ema_x_close_42d_slope_v105_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 5)
    mid = _ema(base, 2) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_10d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_10d_x_close_5d_slope_v106_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 10)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_10d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_10d_x_logclose_21d_slope_v107_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 10)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_10d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_10d_x_meanclose_63d_slope_v108_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 10)
    mid = base * _mean(closeadj, 10)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_10d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_10d_x_closedif_10d_slope_v109_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 10)
    mid = base * closeadj.diff(2).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_10d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_10d_ema_x_close_42d_slope_v110_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 10)
    mid = _ema(base, 5) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_21d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_21d_x_close_5d_slope_v111_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 21)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_21d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_21d_x_logclose_21d_slope_v112_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 21)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_21d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_21d_x_meanclose_63d_slope_v113_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 21)
    mid = base * _mean(closeadj, 21)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_21d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_21d_x_closedif_10d_slope_v114_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 21)
    mid = base * closeadj.diff(5).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_21d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_21d_ema_x_close_42d_slope_v115_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 21)
    mid = _ema(base, 10) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_42d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_42d_x_close_5d_slope_v116_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 42)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_42d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_42d_x_logclose_21d_slope_v117_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 42)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_42d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_42d_x_meanclose_63d_slope_v118_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 42)
    mid = base * _mean(closeadj, 42)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_42d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_42d_x_closedif_10d_slope_v119_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 42)
    mid = base * closeadj.diff(10).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_42d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_42d_ema_x_close_42d_slope_v120_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 42)
    mid = _ema(base, 21) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_63d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_63d_x_close_5d_slope_v121_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 63)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_63d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_63d_x_logclose_21d_slope_v122_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 63)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_63d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_63d_x_meanclose_63d_slope_v123_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 63)
    mid = base * _mean(closeadj, 63)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_63d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_63d_x_closedif_10d_slope_v124_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 63)
    mid = base * closeadj.diff(15).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_63d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_63d_ema_x_close_42d_slope_v125_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 63)
    mid = _ema(base, 31) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_126d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_126d_x_close_5d_slope_v126_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 126)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_126d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_126d_x_logclose_21d_slope_v127_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 126)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_126d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_126d_x_meanclose_63d_slope_v128_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 126)
    mid = base * _mean(closeadj, 126)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_126d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_126d_x_closedif_10d_slope_v129_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 126)
    mid = base * closeadj.diff(31).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_126d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_126d_ema_x_close_42d_slope_v130_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 126)
    mid = _ema(base, 63) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_189d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_189d_x_close_5d_slope_v131_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 189)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_189d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_189d_x_logclose_21d_slope_v132_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 189)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_189d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_189d_x_meanclose_63d_slope_v133_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 189)
    mid = base * _mean(closeadj, 189)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_189d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_189d_x_closedif_10d_slope_v134_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 189)
    mid = base * closeadj.diff(47).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_189d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_189d_ema_x_close_42d_slope_v135_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 189)
    mid = _ema(base, 94) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_252d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_252d_x_close_5d_slope_v136_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 252)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_252d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_252d_x_logclose_21d_slope_v137_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 252)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_252d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_252d_x_meanclose_63d_slope_v138_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 252)
    mid = base * _mean(closeadj, 252)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_252d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_252d_x_closedif_10d_slope_v139_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 252)
    mid = base * closeadj.diff(63).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_252d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_252d_ema_x_close_42d_slope_v140_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 252)
    mid = _ema(base, 126) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_378d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_378d_x_close_5d_slope_v141_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 378)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_378d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_378d_x_logclose_21d_slope_v142_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 378)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_378d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_378d_x_meanclose_63d_slope_v143_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 378)
    mid = base * _mean(closeadj, 378)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_378d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_378d_x_closedif_10d_slope_v144_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 378)
    mid = base * closeadj.diff(94).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_378d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_378d_ema_x_close_42d_slope_v145_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 378)
    mid = _ema(base, 189) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_504d_x_close_5d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_504d_x_close_5d_slope_v146_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 504)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_504d_x_logclose_21d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_504d_x_logclose_21d_slope_v147_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 504)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_504d_x_meanclose_63d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_504d_x_meanclose_63d_slope_v148_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 504)
    mid = base * _mean(closeadj, 504)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_504d_x_closedif_10d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_504d_x_closedif_10d_slope_v149_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 504)
    mid = base * closeadj.diff(126).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_504d_ema_x_close_42d slope
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_504d_ema_x_close_42d_slope_v150_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 504)
    mid = _ema(base, 252) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_5d_x_close_5d_slope_v001_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_5d_x_logclose_21d_slope_v002_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_5d_x_meanclose_63d_slope_v003_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_5d_x_closedif_10d_slope_v004_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_5d_ema_x_close_42d_slope_v005_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_10d_x_close_5d_slope_v006_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_10d_x_logclose_21d_slope_v007_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_10d_x_meanclose_63d_slope_v008_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_10d_x_closedif_10d_slope_v009_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_10d_ema_x_close_42d_slope_v010_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_21d_x_close_5d_slope_v011_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_21d_x_logclose_21d_slope_v012_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_21d_x_meanclose_63d_slope_v013_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_21d_x_closedif_10d_slope_v014_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_21d_ema_x_close_42d_slope_v015_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_42d_x_close_5d_slope_v016_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_42d_x_logclose_21d_slope_v017_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_42d_x_meanclose_63d_slope_v018_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_42d_x_closedif_10d_slope_v019_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_42d_ema_x_close_42d_slope_v020_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_63d_x_close_5d_slope_v021_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_63d_x_logclose_21d_slope_v022_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_63d_x_meanclose_63d_slope_v023_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_63d_x_closedif_10d_slope_v024_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_63d_ema_x_close_42d_slope_v025_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_x_close_5d_slope_v026_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_x_logclose_21d_slope_v027_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_x_meanclose_63d_slope_v028_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_x_closedif_10d_slope_v029_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_ema_x_close_42d_slope_v030_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_x_close_5d_slope_v031_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_x_logclose_21d_slope_v032_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_x_meanclose_63d_slope_v033_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_x_closedif_10d_slope_v034_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_ema_x_close_42d_slope_v035_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_x_close_5d_slope_v036_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_x_logclose_21d_slope_v037_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_x_meanclose_63d_slope_v038_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_x_closedif_10d_slope_v039_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_ema_x_close_42d_slope_v040_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_x_close_5d_slope_v041_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_x_logclose_21d_slope_v042_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_x_meanclose_63d_slope_v043_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_x_closedif_10d_slope_v044_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_ema_x_close_42d_slope_v045_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_x_close_5d_slope_v046_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_x_logclose_21d_slope_v047_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_x_meanclose_63d_slope_v048_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_x_closedif_10d_slope_v049_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_ema_x_close_42d_slope_v050_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_x_close_5d_slope_v051_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_x_logclose_21d_slope_v052_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_x_meanclose_63d_slope_v053_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_x_closedif_10d_slope_v054_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_ema_x_close_42d_slope_v055_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_x_close_5d_slope_v056_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_x_logclose_21d_slope_v057_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_x_meanclose_63d_slope_v058_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_x_closedif_10d_slope_v059_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_ema_x_close_42d_slope_v060_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_x_close_5d_slope_v061_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_x_logclose_21d_slope_v062_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_x_meanclose_63d_slope_v063_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_x_closedif_10d_slope_v064_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_ema_x_close_42d_slope_v065_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_x_close_5d_slope_v066_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_x_logclose_21d_slope_v067_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_x_meanclose_63d_slope_v068_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_x_closedif_10d_slope_v069_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_ema_x_close_42d_slope_v070_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_x_close_5d_slope_v071_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_x_logclose_21d_slope_v072_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_x_meanclose_63d_slope_v073_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_x_closedif_10d_slope_v074_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_ema_x_close_42d_slope_v075_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_x_close_5d_slope_v076_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_x_logclose_21d_slope_v077_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_x_meanclose_63d_slope_v078_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_x_closedif_10d_slope_v079_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_ema_x_close_42d_slope_v080_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_x_close_5d_slope_v081_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_x_logclose_21d_slope_v082_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_x_meanclose_63d_slope_v083_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_x_closedif_10d_slope_v084_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_ema_x_close_42d_slope_v085_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_x_close_5d_slope_v086_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_x_logclose_21d_slope_v087_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_x_meanclose_63d_slope_v088_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_x_closedif_10d_slope_v089_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_ema_x_close_42d_slope_v090_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_x_close_5d_slope_v091_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_x_logclose_21d_slope_v092_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_x_meanclose_63d_slope_v093_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_x_closedif_10d_slope_v094_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_ema_x_close_42d_slope_v095_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_x_close_5d_slope_v096_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_x_logclose_21d_slope_v097_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_x_meanclose_63d_slope_v098_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_x_closedif_10d_slope_v099_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_ema_x_close_42d_slope_v100_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_5d_x_close_5d_slope_v101_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_5d_x_logclose_21d_slope_v102_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_5d_x_meanclose_63d_slope_v103_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_5d_x_closedif_10d_slope_v104_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_5d_ema_x_close_42d_slope_v105_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_10d_x_close_5d_slope_v106_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_10d_x_logclose_21d_slope_v107_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_10d_x_meanclose_63d_slope_v108_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_10d_x_closedif_10d_slope_v109_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_10d_ema_x_close_42d_slope_v110_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_21d_x_close_5d_slope_v111_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_21d_x_logclose_21d_slope_v112_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_21d_x_meanclose_63d_slope_v113_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_21d_x_closedif_10d_slope_v114_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_21d_ema_x_close_42d_slope_v115_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_42d_x_close_5d_slope_v116_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_42d_x_logclose_21d_slope_v117_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_42d_x_meanclose_63d_slope_v118_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_42d_x_closedif_10d_slope_v119_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_42d_ema_x_close_42d_slope_v120_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_63d_x_close_5d_slope_v121_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_63d_x_logclose_21d_slope_v122_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_63d_x_meanclose_63d_slope_v123_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_63d_x_closedif_10d_slope_v124_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_63d_ema_x_close_42d_slope_v125_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_126d_x_close_5d_slope_v126_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_126d_x_logclose_21d_slope_v127_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_126d_x_meanclose_63d_slope_v128_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_126d_x_closedif_10d_slope_v129_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_126d_ema_x_close_42d_slope_v130_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_189d_x_close_5d_slope_v131_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_189d_x_logclose_21d_slope_v132_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_189d_x_meanclose_63d_slope_v133_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_189d_x_closedif_10d_slope_v134_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_189d_ema_x_close_42d_slope_v135_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_252d_x_close_5d_slope_v136_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_252d_x_logclose_21d_slope_v137_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_252d_x_meanclose_63d_slope_v138_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_252d_x_closedif_10d_slope_v139_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_252d_ema_x_close_42d_slope_v140_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_378d_x_close_5d_slope_v141_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_378d_x_logclose_21d_slope_v142_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_378d_x_meanclose_63d_slope_v143_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_378d_x_closedif_10d_slope_v144_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_378d_ema_x_close_42d_slope_v145_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_504d_x_close_5d_slope_v146_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_504d_x_logclose_21d_slope_v147_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_504d_x_meanclose_63d_slope_v148_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_504d_x_closedif_10d_slope_v149_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_504d_ema_x_close_42d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F066_SALES_GROWTH_SURPRISE_VS_TREND_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ('_f066_trailing_growth', '_f066_recent_growth', '_f066_growth_surprise')
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
    print(f"OK f066_sales_growth_surprise_vs_trend_slope_2nd_derivatives_001_150_claude: {n_features} features pass")
