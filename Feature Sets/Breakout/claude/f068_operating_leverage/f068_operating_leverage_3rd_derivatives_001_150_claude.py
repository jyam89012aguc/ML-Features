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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)



# ===== folder domain primitives =====
def _f068_revenue_growth(revenue, w):
    return revenue.pct_change(periods=w)


def _f068_opex_growth(opex, w):
    return opex.pct_change(periods=w)


def _f068_operating_leverage(revenue, opex, w):
    # gap between revenue growth and opex growth — operating leverage
    rg = revenue.pct_change(periods=w)
    og = opex.pct_change(periods=w)
    return rg - og


# opexgrow_5d_x_close_5d jerk
def f068opl_f068_operating_leverage_opexgrow_5d_x_close_5d_jerk_v001_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 5)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_5d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_opexgrow_5d_x_logclose_21d_jerk_v002_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 5)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_5d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_opexgrow_5d_x_meanclose_63d_jerk_v003_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 5)
    mid = base * _mean(closeadj, 5)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_5d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_opexgrow_5d_x_closedif_10d_jerk_v004_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 5)
    mid = base * closeadj.diff(1).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_5d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_opexgrow_5d_ema_x_close_42d_jerk_v005_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 5)
    mid = _ema(base, 2) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_10d_x_close_5d jerk
def f068opl_f068_operating_leverage_opexgrow_10d_x_close_5d_jerk_v006_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 10)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_10d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_opexgrow_10d_x_logclose_21d_jerk_v007_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 10)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_10d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_opexgrow_10d_x_meanclose_63d_jerk_v008_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 10)
    mid = base * _mean(closeadj, 10)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_10d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_opexgrow_10d_x_closedif_10d_jerk_v009_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 10)
    mid = base * closeadj.diff(2).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_10d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_opexgrow_10d_ema_x_close_42d_jerk_v010_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 10)
    mid = _ema(base, 5) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_21d_x_close_5d jerk
def f068opl_f068_operating_leverage_opexgrow_21d_x_close_5d_jerk_v011_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 21)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_21d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_opexgrow_21d_x_logclose_21d_jerk_v012_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 21)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_21d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_opexgrow_21d_x_meanclose_63d_jerk_v013_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 21)
    mid = base * _mean(closeadj, 21)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_21d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_opexgrow_21d_x_closedif_10d_jerk_v014_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 21)
    mid = base * closeadj.diff(5).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_21d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_opexgrow_21d_ema_x_close_42d_jerk_v015_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 21)
    mid = _ema(base, 10) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_42d_x_close_5d jerk
def f068opl_f068_operating_leverage_opexgrow_42d_x_close_5d_jerk_v016_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 42)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_42d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_opexgrow_42d_x_logclose_21d_jerk_v017_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 42)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_42d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_opexgrow_42d_x_meanclose_63d_jerk_v018_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 42)
    mid = base * _mean(closeadj, 42)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_42d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_opexgrow_42d_x_closedif_10d_jerk_v019_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 42)
    mid = base * closeadj.diff(10).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_42d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_opexgrow_42d_ema_x_close_42d_jerk_v020_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 42)
    mid = _ema(base, 21) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_63d_x_close_5d jerk
def f068opl_f068_operating_leverage_opexgrow_63d_x_close_5d_jerk_v021_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 63)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_63d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_opexgrow_63d_x_logclose_21d_jerk_v022_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 63)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_63d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_opexgrow_63d_x_meanclose_63d_jerk_v023_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 63)
    mid = base * _mean(closeadj, 63)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_63d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_opexgrow_63d_x_closedif_10d_jerk_v024_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 63)
    mid = base * closeadj.diff(15).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_63d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_opexgrow_63d_ema_x_close_42d_jerk_v025_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 63)
    mid = _ema(base, 31) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_126d_x_close_5d jerk
def f068opl_f068_operating_leverage_opexgrow_126d_x_close_5d_jerk_v026_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 126)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_126d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_opexgrow_126d_x_logclose_21d_jerk_v027_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 126)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_126d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_opexgrow_126d_x_meanclose_63d_jerk_v028_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 126)
    mid = base * _mean(closeadj, 126)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_126d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_opexgrow_126d_x_closedif_10d_jerk_v029_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 126)
    mid = base * closeadj.diff(31).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_126d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_opexgrow_126d_ema_x_close_42d_jerk_v030_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 126)
    mid = _ema(base, 63) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_189d_x_close_5d jerk
def f068opl_f068_operating_leverage_opexgrow_189d_x_close_5d_jerk_v031_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 189)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_189d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_opexgrow_189d_x_logclose_21d_jerk_v032_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 189)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_189d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_opexgrow_189d_x_meanclose_63d_jerk_v033_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 189)
    mid = base * _mean(closeadj, 189)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_189d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_opexgrow_189d_x_closedif_10d_jerk_v034_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 189)
    mid = base * closeadj.diff(47).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_189d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_opexgrow_189d_ema_x_close_42d_jerk_v035_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 189)
    mid = _ema(base, 94) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_252d_x_close_5d jerk
def f068opl_f068_operating_leverage_opexgrow_252d_x_close_5d_jerk_v036_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 252)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_252d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_opexgrow_252d_x_logclose_21d_jerk_v037_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 252)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_252d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_opexgrow_252d_x_meanclose_63d_jerk_v038_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 252)
    mid = base * _mean(closeadj, 252)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_252d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_opexgrow_252d_x_closedif_10d_jerk_v039_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 252)
    mid = base * closeadj.diff(63).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_252d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_opexgrow_252d_ema_x_close_42d_jerk_v040_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 252)
    mid = _ema(base, 126) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_378d_x_close_5d jerk
def f068opl_f068_operating_leverage_opexgrow_378d_x_close_5d_jerk_v041_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 378)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_378d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_opexgrow_378d_x_logclose_21d_jerk_v042_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 378)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_378d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_opexgrow_378d_x_meanclose_63d_jerk_v043_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 378)
    mid = base * _mean(closeadj, 378)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_378d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_opexgrow_378d_x_closedif_10d_jerk_v044_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 378)
    mid = base * closeadj.diff(94).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_378d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_opexgrow_378d_ema_x_close_42d_jerk_v045_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 378)
    mid = _ema(base, 189) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_504d_x_close_5d jerk
def f068opl_f068_operating_leverage_opexgrow_504d_x_close_5d_jerk_v046_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 504)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_504d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_opexgrow_504d_x_logclose_21d_jerk_v047_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 504)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_504d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_opexgrow_504d_x_meanclose_63d_jerk_v048_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 504)
    mid = base * _mean(closeadj, 504)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_504d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_opexgrow_504d_x_closedif_10d_jerk_v049_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 504)
    mid = base * closeadj.diff(126).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_504d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_opexgrow_504d_ema_x_close_42d_jerk_v050_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 504)
    mid = _ema(base, 252) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_5d_x_close_5d jerk
def f068opl_f068_operating_leverage_oplev_5d_x_close_5d_jerk_v051_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 5)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_5d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_oplev_5d_x_logclose_21d_jerk_v052_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 5)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_5d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_oplev_5d_x_meanclose_63d_jerk_v053_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 5)
    mid = base * _mean(closeadj, 5)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_5d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_oplev_5d_x_closedif_10d_jerk_v054_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 5)
    mid = base * closeadj.diff(1).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_5d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_oplev_5d_ema_x_close_42d_jerk_v055_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 5)
    mid = _ema(base, 2) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_10d_x_close_5d jerk
def f068opl_f068_operating_leverage_oplev_10d_x_close_5d_jerk_v056_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 10)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_10d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_oplev_10d_x_logclose_21d_jerk_v057_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 10)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_10d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_oplev_10d_x_meanclose_63d_jerk_v058_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 10)
    mid = base * _mean(closeadj, 10)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_10d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_oplev_10d_x_closedif_10d_jerk_v059_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 10)
    mid = base * closeadj.diff(2).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_10d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_oplev_10d_ema_x_close_42d_jerk_v060_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 10)
    mid = _ema(base, 5) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_21d_x_close_5d jerk
def f068opl_f068_operating_leverage_oplev_21d_x_close_5d_jerk_v061_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 21)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_21d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_oplev_21d_x_logclose_21d_jerk_v062_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 21)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_21d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_oplev_21d_x_meanclose_63d_jerk_v063_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 21)
    mid = base * _mean(closeadj, 21)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_21d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_oplev_21d_x_closedif_10d_jerk_v064_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 21)
    mid = base * closeadj.diff(5).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_21d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_oplev_21d_ema_x_close_42d_jerk_v065_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 21)
    mid = _ema(base, 10) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_42d_x_close_5d jerk
def f068opl_f068_operating_leverage_oplev_42d_x_close_5d_jerk_v066_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 42)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_42d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_oplev_42d_x_logclose_21d_jerk_v067_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 42)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_42d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_oplev_42d_x_meanclose_63d_jerk_v068_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 42)
    mid = base * _mean(closeadj, 42)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_42d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_oplev_42d_x_closedif_10d_jerk_v069_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 42)
    mid = base * closeadj.diff(10).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_42d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_oplev_42d_ema_x_close_42d_jerk_v070_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 42)
    mid = _ema(base, 21) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_63d_x_close_5d jerk
def f068opl_f068_operating_leverage_oplev_63d_x_close_5d_jerk_v071_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 63)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_63d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_oplev_63d_x_logclose_21d_jerk_v072_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 63)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_63d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_oplev_63d_x_meanclose_63d_jerk_v073_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 63)
    mid = base * _mean(closeadj, 63)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_63d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_oplev_63d_x_closedif_10d_jerk_v074_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 63)
    mid = base * closeadj.diff(15).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_63d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_oplev_63d_ema_x_close_42d_jerk_v075_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 63)
    mid = _ema(base, 31) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_126d_x_close_5d jerk
def f068opl_f068_operating_leverage_oplev_126d_x_close_5d_jerk_v076_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 126)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_126d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_oplev_126d_x_logclose_21d_jerk_v077_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 126)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_126d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_oplev_126d_x_meanclose_63d_jerk_v078_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 126)
    mid = base * _mean(closeadj, 126)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_126d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_oplev_126d_x_closedif_10d_jerk_v079_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 126)
    mid = base * closeadj.diff(31).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_126d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_oplev_126d_ema_x_close_42d_jerk_v080_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 126)
    mid = _ema(base, 63) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_189d_x_close_5d jerk
def f068opl_f068_operating_leverage_oplev_189d_x_close_5d_jerk_v081_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 189)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_189d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_oplev_189d_x_logclose_21d_jerk_v082_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 189)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_189d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_oplev_189d_x_meanclose_63d_jerk_v083_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 189)
    mid = base * _mean(closeadj, 189)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_189d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_oplev_189d_x_closedif_10d_jerk_v084_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 189)
    mid = base * closeadj.diff(47).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_189d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_oplev_189d_ema_x_close_42d_jerk_v085_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 189)
    mid = _ema(base, 94) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_252d_x_close_5d jerk
def f068opl_f068_operating_leverage_oplev_252d_x_close_5d_jerk_v086_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 252)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_252d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_oplev_252d_x_logclose_21d_jerk_v087_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 252)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_252d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_oplev_252d_x_meanclose_63d_jerk_v088_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 252)
    mid = base * _mean(closeadj, 252)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_252d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_oplev_252d_x_closedif_10d_jerk_v089_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 252)
    mid = base * closeadj.diff(63).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_252d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_oplev_252d_ema_x_close_42d_jerk_v090_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 252)
    mid = _ema(base, 126) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_378d_x_close_5d jerk
def f068opl_f068_operating_leverage_oplev_378d_x_close_5d_jerk_v091_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 378)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_378d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_oplev_378d_x_logclose_21d_jerk_v092_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 378)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_378d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_oplev_378d_x_meanclose_63d_jerk_v093_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 378)
    mid = base * _mean(closeadj, 378)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_378d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_oplev_378d_x_closedif_10d_jerk_v094_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 378)
    mid = base * closeadj.diff(94).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_378d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_oplev_378d_ema_x_close_42d_jerk_v095_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 378)
    mid = _ema(base, 189) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_504d_x_close_5d jerk
def f068opl_f068_operating_leverage_oplev_504d_x_close_5d_jerk_v096_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 504)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_504d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_oplev_504d_x_logclose_21d_jerk_v097_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 504)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_504d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_oplev_504d_x_meanclose_63d_jerk_v098_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 504)
    mid = base * _mean(closeadj, 504)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_504d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_oplev_504d_x_closedif_10d_jerk_v099_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 504)
    mid = base * closeadj.diff(126).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_504d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_oplev_504d_ema_x_close_42d_jerk_v100_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 504)
    mid = _ema(base, 252) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_5d_x_close_5d jerk
def f068opl_f068_operating_leverage_revgrow_5d_x_close_5d_jerk_v101_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 5)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_5d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_revgrow_5d_x_logclose_21d_jerk_v102_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 5)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_5d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_revgrow_5d_x_meanclose_63d_jerk_v103_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 5)
    mid = base * _mean(closeadj, 5)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_5d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_revgrow_5d_x_closedif_10d_jerk_v104_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 5)
    mid = base * closeadj.diff(1).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_5d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_revgrow_5d_ema_x_close_42d_jerk_v105_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 5)
    mid = _ema(base, 2) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_10d_x_close_5d jerk
def f068opl_f068_operating_leverage_revgrow_10d_x_close_5d_jerk_v106_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 10)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_10d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_revgrow_10d_x_logclose_21d_jerk_v107_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 10)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_10d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_revgrow_10d_x_meanclose_63d_jerk_v108_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 10)
    mid = base * _mean(closeadj, 10)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_10d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_revgrow_10d_x_closedif_10d_jerk_v109_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 10)
    mid = base * closeadj.diff(2).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_10d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_revgrow_10d_ema_x_close_42d_jerk_v110_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 10)
    mid = _ema(base, 5) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_21d_x_close_5d jerk
def f068opl_f068_operating_leverage_revgrow_21d_x_close_5d_jerk_v111_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 21)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_21d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_revgrow_21d_x_logclose_21d_jerk_v112_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 21)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_21d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_revgrow_21d_x_meanclose_63d_jerk_v113_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 21)
    mid = base * _mean(closeadj, 21)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_21d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_revgrow_21d_x_closedif_10d_jerk_v114_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 21)
    mid = base * closeadj.diff(5).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_21d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_revgrow_21d_ema_x_close_42d_jerk_v115_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 21)
    mid = _ema(base, 10) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_42d_x_close_5d jerk
def f068opl_f068_operating_leverage_revgrow_42d_x_close_5d_jerk_v116_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 42)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_42d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_revgrow_42d_x_logclose_21d_jerk_v117_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 42)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_42d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_revgrow_42d_x_meanclose_63d_jerk_v118_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 42)
    mid = base * _mean(closeadj, 42)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_42d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_revgrow_42d_x_closedif_10d_jerk_v119_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 42)
    mid = base * closeadj.diff(10).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_42d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_revgrow_42d_ema_x_close_42d_jerk_v120_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 42)
    mid = _ema(base, 21) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_63d_x_close_5d jerk
def f068opl_f068_operating_leverage_revgrow_63d_x_close_5d_jerk_v121_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 63)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_63d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_revgrow_63d_x_logclose_21d_jerk_v122_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 63)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_63d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_revgrow_63d_x_meanclose_63d_jerk_v123_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 63)
    mid = base * _mean(closeadj, 63)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_63d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_revgrow_63d_x_closedif_10d_jerk_v124_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 63)
    mid = base * closeadj.diff(15).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_63d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_revgrow_63d_ema_x_close_42d_jerk_v125_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 63)
    mid = _ema(base, 31) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_126d_x_close_5d jerk
def f068opl_f068_operating_leverage_revgrow_126d_x_close_5d_jerk_v126_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 126)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_126d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_revgrow_126d_x_logclose_21d_jerk_v127_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 126)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_126d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_revgrow_126d_x_meanclose_63d_jerk_v128_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 126)
    mid = base * _mean(closeadj, 126)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_126d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_revgrow_126d_x_closedif_10d_jerk_v129_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 126)
    mid = base * closeadj.diff(31).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_126d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_revgrow_126d_ema_x_close_42d_jerk_v130_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 126)
    mid = _ema(base, 63) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_189d_x_close_5d jerk
def f068opl_f068_operating_leverage_revgrow_189d_x_close_5d_jerk_v131_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 189)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_189d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_revgrow_189d_x_logclose_21d_jerk_v132_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 189)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_189d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_revgrow_189d_x_meanclose_63d_jerk_v133_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 189)
    mid = base * _mean(closeadj, 189)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_189d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_revgrow_189d_x_closedif_10d_jerk_v134_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 189)
    mid = base * closeadj.diff(47).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_189d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_revgrow_189d_ema_x_close_42d_jerk_v135_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 189)
    mid = _ema(base, 94) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_252d_x_close_5d jerk
def f068opl_f068_operating_leverage_revgrow_252d_x_close_5d_jerk_v136_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 252)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_252d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_revgrow_252d_x_logclose_21d_jerk_v137_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 252)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_252d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_revgrow_252d_x_meanclose_63d_jerk_v138_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 252)
    mid = base * _mean(closeadj, 252)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_252d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_revgrow_252d_x_closedif_10d_jerk_v139_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 252)
    mid = base * closeadj.diff(63).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_252d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_revgrow_252d_ema_x_close_42d_jerk_v140_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 252)
    mid = _ema(base, 126) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_378d_x_close_5d jerk
def f068opl_f068_operating_leverage_revgrow_378d_x_close_5d_jerk_v141_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 378)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_378d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_revgrow_378d_x_logclose_21d_jerk_v142_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 378)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_378d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_revgrow_378d_x_meanclose_63d_jerk_v143_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 378)
    mid = base * _mean(closeadj, 378)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_378d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_revgrow_378d_x_closedif_10d_jerk_v144_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 378)
    mid = base * closeadj.diff(94).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_378d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_revgrow_378d_ema_x_close_42d_jerk_v145_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 378)
    mid = _ema(base, 189) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_504d_x_close_5d jerk
def f068opl_f068_operating_leverage_revgrow_504d_x_close_5d_jerk_v146_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 504)
    mid = base * closeadj
    result = _jerk(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_504d_x_logclose_21d jerk
def f068opl_f068_operating_leverage_revgrow_504d_x_logclose_21d_jerk_v147_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 504)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _jerk(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_504d_x_meanclose_63d jerk
def f068opl_f068_operating_leverage_revgrow_504d_x_meanclose_63d_jerk_v148_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 504)
    mid = base * _mean(closeadj, 504)
    result = _jerk(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_504d_x_closedif_10d jerk
def f068opl_f068_operating_leverage_revgrow_504d_x_closedif_10d_jerk_v149_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 504)
    mid = base * closeadj.diff(126).abs()
    result = _jerk(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_504d_ema_x_close_42d jerk
def f068opl_f068_operating_leverage_revgrow_504d_ema_x_close_42d_jerk_v150_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 504)
    mid = _ema(base, 252) * closeadj
    result = _jerk(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f068opl_f068_operating_leverage_opexgrow_5d_x_close_5d_jerk_v001_signal,
    f068opl_f068_operating_leverage_opexgrow_5d_x_logclose_21d_jerk_v002_signal,
    f068opl_f068_operating_leverage_opexgrow_5d_x_meanclose_63d_jerk_v003_signal,
    f068opl_f068_operating_leverage_opexgrow_5d_x_closedif_10d_jerk_v004_signal,
    f068opl_f068_operating_leverage_opexgrow_5d_ema_x_close_42d_jerk_v005_signal,
    f068opl_f068_operating_leverage_opexgrow_10d_x_close_5d_jerk_v006_signal,
    f068opl_f068_operating_leverage_opexgrow_10d_x_logclose_21d_jerk_v007_signal,
    f068opl_f068_operating_leverage_opexgrow_10d_x_meanclose_63d_jerk_v008_signal,
    f068opl_f068_operating_leverage_opexgrow_10d_x_closedif_10d_jerk_v009_signal,
    f068opl_f068_operating_leverage_opexgrow_10d_ema_x_close_42d_jerk_v010_signal,
    f068opl_f068_operating_leverage_opexgrow_21d_x_close_5d_jerk_v011_signal,
    f068opl_f068_operating_leverage_opexgrow_21d_x_logclose_21d_jerk_v012_signal,
    f068opl_f068_operating_leverage_opexgrow_21d_x_meanclose_63d_jerk_v013_signal,
    f068opl_f068_operating_leverage_opexgrow_21d_x_closedif_10d_jerk_v014_signal,
    f068opl_f068_operating_leverage_opexgrow_21d_ema_x_close_42d_jerk_v015_signal,
    f068opl_f068_operating_leverage_opexgrow_42d_x_close_5d_jerk_v016_signal,
    f068opl_f068_operating_leverage_opexgrow_42d_x_logclose_21d_jerk_v017_signal,
    f068opl_f068_operating_leverage_opexgrow_42d_x_meanclose_63d_jerk_v018_signal,
    f068opl_f068_operating_leverage_opexgrow_42d_x_closedif_10d_jerk_v019_signal,
    f068opl_f068_operating_leverage_opexgrow_42d_ema_x_close_42d_jerk_v020_signal,
    f068opl_f068_operating_leverage_opexgrow_63d_x_close_5d_jerk_v021_signal,
    f068opl_f068_operating_leverage_opexgrow_63d_x_logclose_21d_jerk_v022_signal,
    f068opl_f068_operating_leverage_opexgrow_63d_x_meanclose_63d_jerk_v023_signal,
    f068opl_f068_operating_leverage_opexgrow_63d_x_closedif_10d_jerk_v024_signal,
    f068opl_f068_operating_leverage_opexgrow_63d_ema_x_close_42d_jerk_v025_signal,
    f068opl_f068_operating_leverage_opexgrow_126d_x_close_5d_jerk_v026_signal,
    f068opl_f068_operating_leverage_opexgrow_126d_x_logclose_21d_jerk_v027_signal,
    f068opl_f068_operating_leverage_opexgrow_126d_x_meanclose_63d_jerk_v028_signal,
    f068opl_f068_operating_leverage_opexgrow_126d_x_closedif_10d_jerk_v029_signal,
    f068opl_f068_operating_leverage_opexgrow_126d_ema_x_close_42d_jerk_v030_signal,
    f068opl_f068_operating_leverage_opexgrow_189d_x_close_5d_jerk_v031_signal,
    f068opl_f068_operating_leverage_opexgrow_189d_x_logclose_21d_jerk_v032_signal,
    f068opl_f068_operating_leverage_opexgrow_189d_x_meanclose_63d_jerk_v033_signal,
    f068opl_f068_operating_leverage_opexgrow_189d_x_closedif_10d_jerk_v034_signal,
    f068opl_f068_operating_leverage_opexgrow_189d_ema_x_close_42d_jerk_v035_signal,
    f068opl_f068_operating_leverage_opexgrow_252d_x_close_5d_jerk_v036_signal,
    f068opl_f068_operating_leverage_opexgrow_252d_x_logclose_21d_jerk_v037_signal,
    f068opl_f068_operating_leverage_opexgrow_252d_x_meanclose_63d_jerk_v038_signal,
    f068opl_f068_operating_leverage_opexgrow_252d_x_closedif_10d_jerk_v039_signal,
    f068opl_f068_operating_leverage_opexgrow_252d_ema_x_close_42d_jerk_v040_signal,
    f068opl_f068_operating_leverage_opexgrow_378d_x_close_5d_jerk_v041_signal,
    f068opl_f068_operating_leverage_opexgrow_378d_x_logclose_21d_jerk_v042_signal,
    f068opl_f068_operating_leverage_opexgrow_378d_x_meanclose_63d_jerk_v043_signal,
    f068opl_f068_operating_leverage_opexgrow_378d_x_closedif_10d_jerk_v044_signal,
    f068opl_f068_operating_leverage_opexgrow_378d_ema_x_close_42d_jerk_v045_signal,
    f068opl_f068_operating_leverage_opexgrow_504d_x_close_5d_jerk_v046_signal,
    f068opl_f068_operating_leverage_opexgrow_504d_x_logclose_21d_jerk_v047_signal,
    f068opl_f068_operating_leverage_opexgrow_504d_x_meanclose_63d_jerk_v048_signal,
    f068opl_f068_operating_leverage_opexgrow_504d_x_closedif_10d_jerk_v049_signal,
    f068opl_f068_operating_leverage_opexgrow_504d_ema_x_close_42d_jerk_v050_signal,
    f068opl_f068_operating_leverage_oplev_5d_x_close_5d_jerk_v051_signal,
    f068opl_f068_operating_leverage_oplev_5d_x_logclose_21d_jerk_v052_signal,
    f068opl_f068_operating_leverage_oplev_5d_x_meanclose_63d_jerk_v053_signal,
    f068opl_f068_operating_leverage_oplev_5d_x_closedif_10d_jerk_v054_signal,
    f068opl_f068_operating_leverage_oplev_5d_ema_x_close_42d_jerk_v055_signal,
    f068opl_f068_operating_leverage_oplev_10d_x_close_5d_jerk_v056_signal,
    f068opl_f068_operating_leverage_oplev_10d_x_logclose_21d_jerk_v057_signal,
    f068opl_f068_operating_leverage_oplev_10d_x_meanclose_63d_jerk_v058_signal,
    f068opl_f068_operating_leverage_oplev_10d_x_closedif_10d_jerk_v059_signal,
    f068opl_f068_operating_leverage_oplev_10d_ema_x_close_42d_jerk_v060_signal,
    f068opl_f068_operating_leverage_oplev_21d_x_close_5d_jerk_v061_signal,
    f068opl_f068_operating_leverage_oplev_21d_x_logclose_21d_jerk_v062_signal,
    f068opl_f068_operating_leverage_oplev_21d_x_meanclose_63d_jerk_v063_signal,
    f068opl_f068_operating_leverage_oplev_21d_x_closedif_10d_jerk_v064_signal,
    f068opl_f068_operating_leverage_oplev_21d_ema_x_close_42d_jerk_v065_signal,
    f068opl_f068_operating_leverage_oplev_42d_x_close_5d_jerk_v066_signal,
    f068opl_f068_operating_leverage_oplev_42d_x_logclose_21d_jerk_v067_signal,
    f068opl_f068_operating_leverage_oplev_42d_x_meanclose_63d_jerk_v068_signal,
    f068opl_f068_operating_leverage_oplev_42d_x_closedif_10d_jerk_v069_signal,
    f068opl_f068_operating_leverage_oplev_42d_ema_x_close_42d_jerk_v070_signal,
    f068opl_f068_operating_leverage_oplev_63d_x_close_5d_jerk_v071_signal,
    f068opl_f068_operating_leverage_oplev_63d_x_logclose_21d_jerk_v072_signal,
    f068opl_f068_operating_leverage_oplev_63d_x_meanclose_63d_jerk_v073_signal,
    f068opl_f068_operating_leverage_oplev_63d_x_closedif_10d_jerk_v074_signal,
    f068opl_f068_operating_leverage_oplev_63d_ema_x_close_42d_jerk_v075_signal,
    f068opl_f068_operating_leverage_oplev_126d_x_close_5d_jerk_v076_signal,
    f068opl_f068_operating_leverage_oplev_126d_x_logclose_21d_jerk_v077_signal,
    f068opl_f068_operating_leverage_oplev_126d_x_meanclose_63d_jerk_v078_signal,
    f068opl_f068_operating_leverage_oplev_126d_x_closedif_10d_jerk_v079_signal,
    f068opl_f068_operating_leverage_oplev_126d_ema_x_close_42d_jerk_v080_signal,
    f068opl_f068_operating_leverage_oplev_189d_x_close_5d_jerk_v081_signal,
    f068opl_f068_operating_leverage_oplev_189d_x_logclose_21d_jerk_v082_signal,
    f068opl_f068_operating_leverage_oplev_189d_x_meanclose_63d_jerk_v083_signal,
    f068opl_f068_operating_leverage_oplev_189d_x_closedif_10d_jerk_v084_signal,
    f068opl_f068_operating_leverage_oplev_189d_ema_x_close_42d_jerk_v085_signal,
    f068opl_f068_operating_leverage_oplev_252d_x_close_5d_jerk_v086_signal,
    f068opl_f068_operating_leverage_oplev_252d_x_logclose_21d_jerk_v087_signal,
    f068opl_f068_operating_leverage_oplev_252d_x_meanclose_63d_jerk_v088_signal,
    f068opl_f068_operating_leverage_oplev_252d_x_closedif_10d_jerk_v089_signal,
    f068opl_f068_operating_leverage_oplev_252d_ema_x_close_42d_jerk_v090_signal,
    f068opl_f068_operating_leverage_oplev_378d_x_close_5d_jerk_v091_signal,
    f068opl_f068_operating_leverage_oplev_378d_x_logclose_21d_jerk_v092_signal,
    f068opl_f068_operating_leverage_oplev_378d_x_meanclose_63d_jerk_v093_signal,
    f068opl_f068_operating_leverage_oplev_378d_x_closedif_10d_jerk_v094_signal,
    f068opl_f068_operating_leverage_oplev_378d_ema_x_close_42d_jerk_v095_signal,
    f068opl_f068_operating_leverage_oplev_504d_x_close_5d_jerk_v096_signal,
    f068opl_f068_operating_leverage_oplev_504d_x_logclose_21d_jerk_v097_signal,
    f068opl_f068_operating_leverage_oplev_504d_x_meanclose_63d_jerk_v098_signal,
    f068opl_f068_operating_leverage_oplev_504d_x_closedif_10d_jerk_v099_signal,
    f068opl_f068_operating_leverage_oplev_504d_ema_x_close_42d_jerk_v100_signal,
    f068opl_f068_operating_leverage_revgrow_5d_x_close_5d_jerk_v101_signal,
    f068opl_f068_operating_leverage_revgrow_5d_x_logclose_21d_jerk_v102_signal,
    f068opl_f068_operating_leverage_revgrow_5d_x_meanclose_63d_jerk_v103_signal,
    f068opl_f068_operating_leverage_revgrow_5d_x_closedif_10d_jerk_v104_signal,
    f068opl_f068_operating_leverage_revgrow_5d_ema_x_close_42d_jerk_v105_signal,
    f068opl_f068_operating_leverage_revgrow_10d_x_close_5d_jerk_v106_signal,
    f068opl_f068_operating_leverage_revgrow_10d_x_logclose_21d_jerk_v107_signal,
    f068opl_f068_operating_leverage_revgrow_10d_x_meanclose_63d_jerk_v108_signal,
    f068opl_f068_operating_leverage_revgrow_10d_x_closedif_10d_jerk_v109_signal,
    f068opl_f068_operating_leverage_revgrow_10d_ema_x_close_42d_jerk_v110_signal,
    f068opl_f068_operating_leverage_revgrow_21d_x_close_5d_jerk_v111_signal,
    f068opl_f068_operating_leverage_revgrow_21d_x_logclose_21d_jerk_v112_signal,
    f068opl_f068_operating_leverage_revgrow_21d_x_meanclose_63d_jerk_v113_signal,
    f068opl_f068_operating_leverage_revgrow_21d_x_closedif_10d_jerk_v114_signal,
    f068opl_f068_operating_leverage_revgrow_21d_ema_x_close_42d_jerk_v115_signal,
    f068opl_f068_operating_leverage_revgrow_42d_x_close_5d_jerk_v116_signal,
    f068opl_f068_operating_leverage_revgrow_42d_x_logclose_21d_jerk_v117_signal,
    f068opl_f068_operating_leverage_revgrow_42d_x_meanclose_63d_jerk_v118_signal,
    f068opl_f068_operating_leverage_revgrow_42d_x_closedif_10d_jerk_v119_signal,
    f068opl_f068_operating_leverage_revgrow_42d_ema_x_close_42d_jerk_v120_signal,
    f068opl_f068_operating_leverage_revgrow_63d_x_close_5d_jerk_v121_signal,
    f068opl_f068_operating_leverage_revgrow_63d_x_logclose_21d_jerk_v122_signal,
    f068opl_f068_operating_leverage_revgrow_63d_x_meanclose_63d_jerk_v123_signal,
    f068opl_f068_operating_leverage_revgrow_63d_x_closedif_10d_jerk_v124_signal,
    f068opl_f068_operating_leverage_revgrow_63d_ema_x_close_42d_jerk_v125_signal,
    f068opl_f068_operating_leverage_revgrow_126d_x_close_5d_jerk_v126_signal,
    f068opl_f068_operating_leverage_revgrow_126d_x_logclose_21d_jerk_v127_signal,
    f068opl_f068_operating_leverage_revgrow_126d_x_meanclose_63d_jerk_v128_signal,
    f068opl_f068_operating_leverage_revgrow_126d_x_closedif_10d_jerk_v129_signal,
    f068opl_f068_operating_leverage_revgrow_126d_ema_x_close_42d_jerk_v130_signal,
    f068opl_f068_operating_leverage_revgrow_189d_x_close_5d_jerk_v131_signal,
    f068opl_f068_operating_leverage_revgrow_189d_x_logclose_21d_jerk_v132_signal,
    f068opl_f068_operating_leverage_revgrow_189d_x_meanclose_63d_jerk_v133_signal,
    f068opl_f068_operating_leverage_revgrow_189d_x_closedif_10d_jerk_v134_signal,
    f068opl_f068_operating_leverage_revgrow_189d_ema_x_close_42d_jerk_v135_signal,
    f068opl_f068_operating_leverage_revgrow_252d_x_close_5d_jerk_v136_signal,
    f068opl_f068_operating_leverage_revgrow_252d_x_logclose_21d_jerk_v137_signal,
    f068opl_f068_operating_leverage_revgrow_252d_x_meanclose_63d_jerk_v138_signal,
    f068opl_f068_operating_leverage_revgrow_252d_x_closedif_10d_jerk_v139_signal,
    f068opl_f068_operating_leverage_revgrow_252d_ema_x_close_42d_jerk_v140_signal,
    f068opl_f068_operating_leverage_revgrow_378d_x_close_5d_jerk_v141_signal,
    f068opl_f068_operating_leverage_revgrow_378d_x_logclose_21d_jerk_v142_signal,
    f068opl_f068_operating_leverage_revgrow_378d_x_meanclose_63d_jerk_v143_signal,
    f068opl_f068_operating_leverage_revgrow_378d_x_closedif_10d_jerk_v144_signal,
    f068opl_f068_operating_leverage_revgrow_378d_ema_x_close_42d_jerk_v145_signal,
    f068opl_f068_operating_leverage_revgrow_504d_x_close_5d_jerk_v146_signal,
    f068opl_f068_operating_leverage_revgrow_504d_x_logclose_21d_jerk_v147_signal,
    f068opl_f068_operating_leverage_revgrow_504d_x_meanclose_63d_jerk_v148_signal,
    f068opl_f068_operating_leverage_revgrow_504d_x_closedif_10d_jerk_v149_signal,
    f068opl_f068_operating_leverage_revgrow_504d_ema_x_close_42d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F068_OPERATING_LEVERAGE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    opex = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="opex")
    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "opex": opex,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f068_revenue_growth', '_f068_opex_growth', '_f068_operating_leverage')
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
    print(f"OK f068_operating_leverage_jerk_3rd_derivatives_001_150_claude: {n_features} features pass")
