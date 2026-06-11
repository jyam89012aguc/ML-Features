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
def _f067_fcf_sign(fcf, w):
    # smoothed fcf level — proxies sign and magnitude of free cash flow
    sm = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.tanh(sm / sm.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan))


def _f067_fcf_inflection(fcf, w):
    # change in smoothed fcf over the window — inflection signal
    sm = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    return sm.diff(periods=w) / sm.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)


def _f067_self_funding_turn(fcf, w):
    # cumulative fcf normalized — self-funding turn signal
    sw = max(2, w // 4)
    long = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    short = fcf.rolling(sw, min_periods=max(1, sw // 2)).mean()
    denom = long.abs().replace(0, np.nan)
    return (short - long) / denom


# inflection_5d_x_close_5d slope
def f067fcf_f067_fcf_inflection_inflection_5d_x_close_5d_slope_v001_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 5)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_5d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_inflection_5d_x_logclose_21d_slope_v002_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 5)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_5d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_inflection_5d_x_meanclose_63d_slope_v003_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 5)
    mid = base * _mean(closeadj, 5)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_5d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_inflection_5d_x_closedif_10d_slope_v004_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 5)
    mid = base * closeadj.diff(1).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_5d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_inflection_5d_ema_x_close_42d_slope_v005_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 5)
    mid = _ema(base, 2) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_10d_x_close_5d slope
def f067fcf_f067_fcf_inflection_inflection_10d_x_close_5d_slope_v006_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 10)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_10d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_inflection_10d_x_logclose_21d_slope_v007_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 10)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_10d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_inflection_10d_x_meanclose_63d_slope_v008_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 10)
    mid = base * _mean(closeadj, 10)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_10d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_inflection_10d_x_closedif_10d_slope_v009_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 10)
    mid = base * closeadj.diff(2).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_10d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_inflection_10d_ema_x_close_42d_slope_v010_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 10)
    mid = _ema(base, 5) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_21d_x_close_5d slope
def f067fcf_f067_fcf_inflection_inflection_21d_x_close_5d_slope_v011_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 21)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_21d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_inflection_21d_x_logclose_21d_slope_v012_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 21)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_21d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_inflection_21d_x_meanclose_63d_slope_v013_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 21)
    mid = base * _mean(closeadj, 21)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_21d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_inflection_21d_x_closedif_10d_slope_v014_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 21)
    mid = base * closeadj.diff(5).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_21d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_inflection_21d_ema_x_close_42d_slope_v015_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 21)
    mid = _ema(base, 10) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_42d_x_close_5d slope
def f067fcf_f067_fcf_inflection_inflection_42d_x_close_5d_slope_v016_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 42)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_42d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_inflection_42d_x_logclose_21d_slope_v017_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 42)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_42d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_inflection_42d_x_meanclose_63d_slope_v018_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 42)
    mid = base * _mean(closeadj, 42)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_42d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_inflection_42d_x_closedif_10d_slope_v019_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 42)
    mid = base * closeadj.diff(10).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_42d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_inflection_42d_ema_x_close_42d_slope_v020_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 42)
    mid = _ema(base, 21) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_63d_x_close_5d slope
def f067fcf_f067_fcf_inflection_inflection_63d_x_close_5d_slope_v021_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 63)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_63d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_inflection_63d_x_logclose_21d_slope_v022_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 63)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_63d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_inflection_63d_x_meanclose_63d_slope_v023_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 63)
    mid = base * _mean(closeadj, 63)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_63d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_inflection_63d_x_closedif_10d_slope_v024_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 63)
    mid = base * closeadj.diff(15).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_63d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_inflection_63d_ema_x_close_42d_slope_v025_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 63)
    mid = _ema(base, 31) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_126d_x_close_5d slope
def f067fcf_f067_fcf_inflection_inflection_126d_x_close_5d_slope_v026_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 126)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_126d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_inflection_126d_x_logclose_21d_slope_v027_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 126)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_126d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_inflection_126d_x_meanclose_63d_slope_v028_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 126)
    mid = base * _mean(closeadj, 126)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_126d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_inflection_126d_x_closedif_10d_slope_v029_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 126)
    mid = base * closeadj.diff(31).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_126d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_inflection_126d_ema_x_close_42d_slope_v030_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 126)
    mid = _ema(base, 63) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_189d_x_close_5d slope
def f067fcf_f067_fcf_inflection_inflection_189d_x_close_5d_slope_v031_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 189)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_189d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_inflection_189d_x_logclose_21d_slope_v032_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 189)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_189d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_inflection_189d_x_meanclose_63d_slope_v033_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 189)
    mid = base * _mean(closeadj, 189)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_189d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_inflection_189d_x_closedif_10d_slope_v034_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 189)
    mid = base * closeadj.diff(47).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_189d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_inflection_189d_ema_x_close_42d_slope_v035_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 189)
    mid = _ema(base, 94) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_252d_x_close_5d slope
def f067fcf_f067_fcf_inflection_inflection_252d_x_close_5d_slope_v036_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 252)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_252d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_inflection_252d_x_logclose_21d_slope_v037_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 252)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_252d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_inflection_252d_x_meanclose_63d_slope_v038_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 252)
    mid = base * _mean(closeadj, 252)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_252d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_inflection_252d_x_closedif_10d_slope_v039_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 252)
    mid = base * closeadj.diff(63).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_252d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_inflection_252d_ema_x_close_42d_slope_v040_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 252)
    mid = _ema(base, 126) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_378d_x_close_5d slope
def f067fcf_f067_fcf_inflection_inflection_378d_x_close_5d_slope_v041_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 378)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_378d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_inflection_378d_x_logclose_21d_slope_v042_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 378)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_378d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_inflection_378d_x_meanclose_63d_slope_v043_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 378)
    mid = base * _mean(closeadj, 378)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_378d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_inflection_378d_x_closedif_10d_slope_v044_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 378)
    mid = base * closeadj.diff(94).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_378d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_inflection_378d_ema_x_close_42d_slope_v045_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 378)
    mid = _ema(base, 189) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_504d_x_close_5d slope
def f067fcf_f067_fcf_inflection_inflection_504d_x_close_5d_slope_v046_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 504)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_504d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_inflection_504d_x_logclose_21d_slope_v047_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 504)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_504d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_inflection_504d_x_meanclose_63d_slope_v048_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 504)
    mid = base * _mean(closeadj, 504)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_504d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_inflection_504d_x_closedif_10d_slope_v049_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 504)
    mid = base * closeadj.diff(126).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_504d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_inflection_504d_ema_x_close_42d_slope_v050_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 504)
    mid = _ema(base, 252) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_5d_x_close_5d slope
def f067fcf_f067_fcf_inflection_selffund_5d_x_close_5d_slope_v051_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 5)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_5d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_selffund_5d_x_logclose_21d_slope_v052_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 5)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_5d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_selffund_5d_x_meanclose_63d_slope_v053_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 5)
    mid = base * _mean(closeadj, 5)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_5d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_selffund_5d_x_closedif_10d_slope_v054_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 5)
    mid = base * closeadj.diff(1).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_5d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_selffund_5d_ema_x_close_42d_slope_v055_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 5)
    mid = _ema(base, 2) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_10d_x_close_5d slope
def f067fcf_f067_fcf_inflection_selffund_10d_x_close_5d_slope_v056_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 10)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_10d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_selffund_10d_x_logclose_21d_slope_v057_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 10)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_10d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_selffund_10d_x_meanclose_63d_slope_v058_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 10)
    mid = base * _mean(closeadj, 10)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_10d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_selffund_10d_x_closedif_10d_slope_v059_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 10)
    mid = base * closeadj.diff(2).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_10d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_selffund_10d_ema_x_close_42d_slope_v060_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 10)
    mid = _ema(base, 5) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_21d_x_close_5d slope
def f067fcf_f067_fcf_inflection_selffund_21d_x_close_5d_slope_v061_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 21)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_21d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_selffund_21d_x_logclose_21d_slope_v062_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 21)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_21d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_selffund_21d_x_meanclose_63d_slope_v063_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 21)
    mid = base * _mean(closeadj, 21)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_21d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_selffund_21d_x_closedif_10d_slope_v064_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 21)
    mid = base * closeadj.diff(5).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_21d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_selffund_21d_ema_x_close_42d_slope_v065_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 21)
    mid = _ema(base, 10) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_42d_x_close_5d slope
def f067fcf_f067_fcf_inflection_selffund_42d_x_close_5d_slope_v066_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 42)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_42d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_selffund_42d_x_logclose_21d_slope_v067_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 42)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_42d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_selffund_42d_x_meanclose_63d_slope_v068_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 42)
    mid = base * _mean(closeadj, 42)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_42d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_selffund_42d_x_closedif_10d_slope_v069_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 42)
    mid = base * closeadj.diff(10).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_42d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_selffund_42d_ema_x_close_42d_slope_v070_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 42)
    mid = _ema(base, 21) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_63d_x_close_5d slope
def f067fcf_f067_fcf_inflection_selffund_63d_x_close_5d_slope_v071_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 63)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_63d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_selffund_63d_x_logclose_21d_slope_v072_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 63)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_63d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_selffund_63d_x_meanclose_63d_slope_v073_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 63)
    mid = base * _mean(closeadj, 63)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_63d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_selffund_63d_x_closedif_10d_slope_v074_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 63)
    mid = base * closeadj.diff(15).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_63d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_selffund_63d_ema_x_close_42d_slope_v075_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 63)
    mid = _ema(base, 31) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_126d_x_close_5d slope
def f067fcf_f067_fcf_inflection_selffund_126d_x_close_5d_slope_v076_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 126)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_126d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_selffund_126d_x_logclose_21d_slope_v077_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 126)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_126d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_selffund_126d_x_meanclose_63d_slope_v078_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 126)
    mid = base * _mean(closeadj, 126)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_126d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_selffund_126d_x_closedif_10d_slope_v079_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 126)
    mid = base * closeadj.diff(31).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_126d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_selffund_126d_ema_x_close_42d_slope_v080_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 126)
    mid = _ema(base, 63) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_189d_x_close_5d slope
def f067fcf_f067_fcf_inflection_selffund_189d_x_close_5d_slope_v081_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 189)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_189d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_selffund_189d_x_logclose_21d_slope_v082_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 189)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_189d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_selffund_189d_x_meanclose_63d_slope_v083_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 189)
    mid = base * _mean(closeadj, 189)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_189d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_selffund_189d_x_closedif_10d_slope_v084_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 189)
    mid = base * closeadj.diff(47).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_189d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_selffund_189d_ema_x_close_42d_slope_v085_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 189)
    mid = _ema(base, 94) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_252d_x_close_5d slope
def f067fcf_f067_fcf_inflection_selffund_252d_x_close_5d_slope_v086_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 252)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_252d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_selffund_252d_x_logclose_21d_slope_v087_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 252)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_252d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_selffund_252d_x_meanclose_63d_slope_v088_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 252)
    mid = base * _mean(closeadj, 252)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_252d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_selffund_252d_x_closedif_10d_slope_v089_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 252)
    mid = base * closeadj.diff(63).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_252d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_selffund_252d_ema_x_close_42d_slope_v090_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 252)
    mid = _ema(base, 126) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_378d_x_close_5d slope
def f067fcf_f067_fcf_inflection_selffund_378d_x_close_5d_slope_v091_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 378)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_378d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_selffund_378d_x_logclose_21d_slope_v092_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 378)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_378d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_selffund_378d_x_meanclose_63d_slope_v093_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 378)
    mid = base * _mean(closeadj, 378)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_378d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_selffund_378d_x_closedif_10d_slope_v094_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 378)
    mid = base * closeadj.diff(94).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_378d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_selffund_378d_ema_x_close_42d_slope_v095_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 378)
    mid = _ema(base, 189) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_504d_x_close_5d slope
def f067fcf_f067_fcf_inflection_selffund_504d_x_close_5d_slope_v096_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 504)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_504d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_selffund_504d_x_logclose_21d_slope_v097_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 504)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_504d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_selffund_504d_x_meanclose_63d_slope_v098_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 504)
    mid = base * _mean(closeadj, 504)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_504d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_selffund_504d_x_closedif_10d_slope_v099_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 504)
    mid = base * closeadj.diff(126).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_504d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_selffund_504d_ema_x_close_42d_slope_v100_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 504)
    mid = _ema(base, 252) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_5d_x_close_5d slope
def f067fcf_f067_fcf_inflection_sign_5d_x_close_5d_slope_v101_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 5)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_5d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_sign_5d_x_logclose_21d_slope_v102_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 5)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_5d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_sign_5d_x_meanclose_63d_slope_v103_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 5)
    mid = base * _mean(closeadj, 5)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_5d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_sign_5d_x_closedif_10d_slope_v104_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 5)
    mid = base * closeadj.diff(1).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_5d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_sign_5d_ema_x_close_42d_slope_v105_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 5)
    mid = _ema(base, 2) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_10d_x_close_5d slope
def f067fcf_f067_fcf_inflection_sign_10d_x_close_5d_slope_v106_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 10)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_10d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_sign_10d_x_logclose_21d_slope_v107_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 10)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_10d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_sign_10d_x_meanclose_63d_slope_v108_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 10)
    mid = base * _mean(closeadj, 10)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_10d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_sign_10d_x_closedif_10d_slope_v109_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 10)
    mid = base * closeadj.diff(2).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_10d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_sign_10d_ema_x_close_42d_slope_v110_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 10)
    mid = _ema(base, 5) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_21d_x_close_5d slope
def f067fcf_f067_fcf_inflection_sign_21d_x_close_5d_slope_v111_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 21)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_21d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_sign_21d_x_logclose_21d_slope_v112_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 21)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_21d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_sign_21d_x_meanclose_63d_slope_v113_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 21)
    mid = base * _mean(closeadj, 21)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_21d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_sign_21d_x_closedif_10d_slope_v114_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 21)
    mid = base * closeadj.diff(5).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_21d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_sign_21d_ema_x_close_42d_slope_v115_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 21)
    mid = _ema(base, 10) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_42d_x_close_5d slope
def f067fcf_f067_fcf_inflection_sign_42d_x_close_5d_slope_v116_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 42)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_42d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_sign_42d_x_logclose_21d_slope_v117_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 42)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_42d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_sign_42d_x_meanclose_63d_slope_v118_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 42)
    mid = base * _mean(closeadj, 42)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_42d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_sign_42d_x_closedif_10d_slope_v119_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 42)
    mid = base * closeadj.diff(10).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_42d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_sign_42d_ema_x_close_42d_slope_v120_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 42)
    mid = _ema(base, 21) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_63d_x_close_5d slope
def f067fcf_f067_fcf_inflection_sign_63d_x_close_5d_slope_v121_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 63)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_63d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_sign_63d_x_logclose_21d_slope_v122_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 63)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_63d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_sign_63d_x_meanclose_63d_slope_v123_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 63)
    mid = base * _mean(closeadj, 63)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_63d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_sign_63d_x_closedif_10d_slope_v124_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 63)
    mid = base * closeadj.diff(15).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_63d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_sign_63d_ema_x_close_42d_slope_v125_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 63)
    mid = _ema(base, 31) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_126d_x_close_5d slope
def f067fcf_f067_fcf_inflection_sign_126d_x_close_5d_slope_v126_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 126)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_126d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_sign_126d_x_logclose_21d_slope_v127_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 126)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_126d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_sign_126d_x_meanclose_63d_slope_v128_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 126)
    mid = base * _mean(closeadj, 126)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_126d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_sign_126d_x_closedif_10d_slope_v129_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 126)
    mid = base * closeadj.diff(31).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_126d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_sign_126d_ema_x_close_42d_slope_v130_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 126)
    mid = _ema(base, 63) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_189d_x_close_5d slope
def f067fcf_f067_fcf_inflection_sign_189d_x_close_5d_slope_v131_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 189)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_189d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_sign_189d_x_logclose_21d_slope_v132_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 189)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_189d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_sign_189d_x_meanclose_63d_slope_v133_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 189)
    mid = base * _mean(closeadj, 189)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_189d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_sign_189d_x_closedif_10d_slope_v134_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 189)
    mid = base * closeadj.diff(47).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_189d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_sign_189d_ema_x_close_42d_slope_v135_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 189)
    mid = _ema(base, 94) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_252d_x_close_5d slope
def f067fcf_f067_fcf_inflection_sign_252d_x_close_5d_slope_v136_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 252)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_252d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_sign_252d_x_logclose_21d_slope_v137_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 252)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_252d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_sign_252d_x_meanclose_63d_slope_v138_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 252)
    mid = base * _mean(closeadj, 252)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_252d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_sign_252d_x_closedif_10d_slope_v139_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 252)
    mid = base * closeadj.diff(63).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_252d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_sign_252d_ema_x_close_42d_slope_v140_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 252)
    mid = _ema(base, 126) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_378d_x_close_5d slope
def f067fcf_f067_fcf_inflection_sign_378d_x_close_5d_slope_v141_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 378)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_378d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_sign_378d_x_logclose_21d_slope_v142_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 378)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_378d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_sign_378d_x_meanclose_63d_slope_v143_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 378)
    mid = base * _mean(closeadj, 378)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_378d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_sign_378d_x_closedif_10d_slope_v144_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 378)
    mid = base * closeadj.diff(94).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_378d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_sign_378d_ema_x_close_42d_slope_v145_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 378)
    mid = _ema(base, 189) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_504d_x_close_5d slope
def f067fcf_f067_fcf_inflection_sign_504d_x_close_5d_slope_v146_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 504)
    mid = base * closeadj
    result = _slope_diff_norm(mid, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_504d_x_logclose_21d slope
def f067fcf_f067_fcf_inflection_sign_504d_x_logclose_21d_slope_v147_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 504)
    mid = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    result = _slope_diff_norm(mid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_504d_x_meanclose_63d slope
def f067fcf_f067_fcf_inflection_sign_504d_x_meanclose_63d_slope_v148_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 504)
    mid = base * _mean(closeadj, 504)
    result = _slope_diff_norm(mid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_504d_x_closedif_10d slope
def f067fcf_f067_fcf_inflection_sign_504d_x_closedif_10d_slope_v149_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 504)
    mid = base * closeadj.diff(126).abs()
    result = _slope_diff_norm(mid, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_504d_ema_x_close_42d slope
def f067fcf_f067_fcf_inflection_sign_504d_ema_x_close_42d_slope_v150_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 504)
    mid = _ema(base, 252) * closeadj
    result = _slope_diff_norm(mid, 42)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f067fcf_f067_fcf_inflection_inflection_5d_x_close_5d_slope_v001_signal,
    f067fcf_f067_fcf_inflection_inflection_5d_x_logclose_21d_slope_v002_signal,
    f067fcf_f067_fcf_inflection_inflection_5d_x_meanclose_63d_slope_v003_signal,
    f067fcf_f067_fcf_inflection_inflection_5d_x_closedif_10d_slope_v004_signal,
    f067fcf_f067_fcf_inflection_inflection_5d_ema_x_close_42d_slope_v005_signal,
    f067fcf_f067_fcf_inflection_inflection_10d_x_close_5d_slope_v006_signal,
    f067fcf_f067_fcf_inflection_inflection_10d_x_logclose_21d_slope_v007_signal,
    f067fcf_f067_fcf_inflection_inflection_10d_x_meanclose_63d_slope_v008_signal,
    f067fcf_f067_fcf_inflection_inflection_10d_x_closedif_10d_slope_v009_signal,
    f067fcf_f067_fcf_inflection_inflection_10d_ema_x_close_42d_slope_v010_signal,
    f067fcf_f067_fcf_inflection_inflection_21d_x_close_5d_slope_v011_signal,
    f067fcf_f067_fcf_inflection_inflection_21d_x_logclose_21d_slope_v012_signal,
    f067fcf_f067_fcf_inflection_inflection_21d_x_meanclose_63d_slope_v013_signal,
    f067fcf_f067_fcf_inflection_inflection_21d_x_closedif_10d_slope_v014_signal,
    f067fcf_f067_fcf_inflection_inflection_21d_ema_x_close_42d_slope_v015_signal,
    f067fcf_f067_fcf_inflection_inflection_42d_x_close_5d_slope_v016_signal,
    f067fcf_f067_fcf_inflection_inflection_42d_x_logclose_21d_slope_v017_signal,
    f067fcf_f067_fcf_inflection_inflection_42d_x_meanclose_63d_slope_v018_signal,
    f067fcf_f067_fcf_inflection_inflection_42d_x_closedif_10d_slope_v019_signal,
    f067fcf_f067_fcf_inflection_inflection_42d_ema_x_close_42d_slope_v020_signal,
    f067fcf_f067_fcf_inflection_inflection_63d_x_close_5d_slope_v021_signal,
    f067fcf_f067_fcf_inflection_inflection_63d_x_logclose_21d_slope_v022_signal,
    f067fcf_f067_fcf_inflection_inflection_63d_x_meanclose_63d_slope_v023_signal,
    f067fcf_f067_fcf_inflection_inflection_63d_x_closedif_10d_slope_v024_signal,
    f067fcf_f067_fcf_inflection_inflection_63d_ema_x_close_42d_slope_v025_signal,
    f067fcf_f067_fcf_inflection_inflection_126d_x_close_5d_slope_v026_signal,
    f067fcf_f067_fcf_inflection_inflection_126d_x_logclose_21d_slope_v027_signal,
    f067fcf_f067_fcf_inflection_inflection_126d_x_meanclose_63d_slope_v028_signal,
    f067fcf_f067_fcf_inflection_inflection_126d_x_closedif_10d_slope_v029_signal,
    f067fcf_f067_fcf_inflection_inflection_126d_ema_x_close_42d_slope_v030_signal,
    f067fcf_f067_fcf_inflection_inflection_189d_x_close_5d_slope_v031_signal,
    f067fcf_f067_fcf_inflection_inflection_189d_x_logclose_21d_slope_v032_signal,
    f067fcf_f067_fcf_inflection_inflection_189d_x_meanclose_63d_slope_v033_signal,
    f067fcf_f067_fcf_inflection_inflection_189d_x_closedif_10d_slope_v034_signal,
    f067fcf_f067_fcf_inflection_inflection_189d_ema_x_close_42d_slope_v035_signal,
    f067fcf_f067_fcf_inflection_inflection_252d_x_close_5d_slope_v036_signal,
    f067fcf_f067_fcf_inflection_inflection_252d_x_logclose_21d_slope_v037_signal,
    f067fcf_f067_fcf_inflection_inflection_252d_x_meanclose_63d_slope_v038_signal,
    f067fcf_f067_fcf_inflection_inflection_252d_x_closedif_10d_slope_v039_signal,
    f067fcf_f067_fcf_inflection_inflection_252d_ema_x_close_42d_slope_v040_signal,
    f067fcf_f067_fcf_inflection_inflection_378d_x_close_5d_slope_v041_signal,
    f067fcf_f067_fcf_inflection_inflection_378d_x_logclose_21d_slope_v042_signal,
    f067fcf_f067_fcf_inflection_inflection_378d_x_meanclose_63d_slope_v043_signal,
    f067fcf_f067_fcf_inflection_inflection_378d_x_closedif_10d_slope_v044_signal,
    f067fcf_f067_fcf_inflection_inflection_378d_ema_x_close_42d_slope_v045_signal,
    f067fcf_f067_fcf_inflection_inflection_504d_x_close_5d_slope_v046_signal,
    f067fcf_f067_fcf_inflection_inflection_504d_x_logclose_21d_slope_v047_signal,
    f067fcf_f067_fcf_inflection_inflection_504d_x_meanclose_63d_slope_v048_signal,
    f067fcf_f067_fcf_inflection_inflection_504d_x_closedif_10d_slope_v049_signal,
    f067fcf_f067_fcf_inflection_inflection_504d_ema_x_close_42d_slope_v050_signal,
    f067fcf_f067_fcf_inflection_selffund_5d_x_close_5d_slope_v051_signal,
    f067fcf_f067_fcf_inflection_selffund_5d_x_logclose_21d_slope_v052_signal,
    f067fcf_f067_fcf_inflection_selffund_5d_x_meanclose_63d_slope_v053_signal,
    f067fcf_f067_fcf_inflection_selffund_5d_x_closedif_10d_slope_v054_signal,
    f067fcf_f067_fcf_inflection_selffund_5d_ema_x_close_42d_slope_v055_signal,
    f067fcf_f067_fcf_inflection_selffund_10d_x_close_5d_slope_v056_signal,
    f067fcf_f067_fcf_inflection_selffund_10d_x_logclose_21d_slope_v057_signal,
    f067fcf_f067_fcf_inflection_selffund_10d_x_meanclose_63d_slope_v058_signal,
    f067fcf_f067_fcf_inflection_selffund_10d_x_closedif_10d_slope_v059_signal,
    f067fcf_f067_fcf_inflection_selffund_10d_ema_x_close_42d_slope_v060_signal,
    f067fcf_f067_fcf_inflection_selffund_21d_x_close_5d_slope_v061_signal,
    f067fcf_f067_fcf_inflection_selffund_21d_x_logclose_21d_slope_v062_signal,
    f067fcf_f067_fcf_inflection_selffund_21d_x_meanclose_63d_slope_v063_signal,
    f067fcf_f067_fcf_inflection_selffund_21d_x_closedif_10d_slope_v064_signal,
    f067fcf_f067_fcf_inflection_selffund_21d_ema_x_close_42d_slope_v065_signal,
    f067fcf_f067_fcf_inflection_selffund_42d_x_close_5d_slope_v066_signal,
    f067fcf_f067_fcf_inflection_selffund_42d_x_logclose_21d_slope_v067_signal,
    f067fcf_f067_fcf_inflection_selffund_42d_x_meanclose_63d_slope_v068_signal,
    f067fcf_f067_fcf_inflection_selffund_42d_x_closedif_10d_slope_v069_signal,
    f067fcf_f067_fcf_inflection_selffund_42d_ema_x_close_42d_slope_v070_signal,
    f067fcf_f067_fcf_inflection_selffund_63d_x_close_5d_slope_v071_signal,
    f067fcf_f067_fcf_inflection_selffund_63d_x_logclose_21d_slope_v072_signal,
    f067fcf_f067_fcf_inflection_selffund_63d_x_meanclose_63d_slope_v073_signal,
    f067fcf_f067_fcf_inflection_selffund_63d_x_closedif_10d_slope_v074_signal,
    f067fcf_f067_fcf_inflection_selffund_63d_ema_x_close_42d_slope_v075_signal,
    f067fcf_f067_fcf_inflection_selffund_126d_x_close_5d_slope_v076_signal,
    f067fcf_f067_fcf_inflection_selffund_126d_x_logclose_21d_slope_v077_signal,
    f067fcf_f067_fcf_inflection_selffund_126d_x_meanclose_63d_slope_v078_signal,
    f067fcf_f067_fcf_inflection_selffund_126d_x_closedif_10d_slope_v079_signal,
    f067fcf_f067_fcf_inflection_selffund_126d_ema_x_close_42d_slope_v080_signal,
    f067fcf_f067_fcf_inflection_selffund_189d_x_close_5d_slope_v081_signal,
    f067fcf_f067_fcf_inflection_selffund_189d_x_logclose_21d_slope_v082_signal,
    f067fcf_f067_fcf_inflection_selffund_189d_x_meanclose_63d_slope_v083_signal,
    f067fcf_f067_fcf_inflection_selffund_189d_x_closedif_10d_slope_v084_signal,
    f067fcf_f067_fcf_inflection_selffund_189d_ema_x_close_42d_slope_v085_signal,
    f067fcf_f067_fcf_inflection_selffund_252d_x_close_5d_slope_v086_signal,
    f067fcf_f067_fcf_inflection_selffund_252d_x_logclose_21d_slope_v087_signal,
    f067fcf_f067_fcf_inflection_selffund_252d_x_meanclose_63d_slope_v088_signal,
    f067fcf_f067_fcf_inflection_selffund_252d_x_closedif_10d_slope_v089_signal,
    f067fcf_f067_fcf_inflection_selffund_252d_ema_x_close_42d_slope_v090_signal,
    f067fcf_f067_fcf_inflection_selffund_378d_x_close_5d_slope_v091_signal,
    f067fcf_f067_fcf_inflection_selffund_378d_x_logclose_21d_slope_v092_signal,
    f067fcf_f067_fcf_inflection_selffund_378d_x_meanclose_63d_slope_v093_signal,
    f067fcf_f067_fcf_inflection_selffund_378d_x_closedif_10d_slope_v094_signal,
    f067fcf_f067_fcf_inflection_selffund_378d_ema_x_close_42d_slope_v095_signal,
    f067fcf_f067_fcf_inflection_selffund_504d_x_close_5d_slope_v096_signal,
    f067fcf_f067_fcf_inflection_selffund_504d_x_logclose_21d_slope_v097_signal,
    f067fcf_f067_fcf_inflection_selffund_504d_x_meanclose_63d_slope_v098_signal,
    f067fcf_f067_fcf_inflection_selffund_504d_x_closedif_10d_slope_v099_signal,
    f067fcf_f067_fcf_inflection_selffund_504d_ema_x_close_42d_slope_v100_signal,
    f067fcf_f067_fcf_inflection_sign_5d_x_close_5d_slope_v101_signal,
    f067fcf_f067_fcf_inflection_sign_5d_x_logclose_21d_slope_v102_signal,
    f067fcf_f067_fcf_inflection_sign_5d_x_meanclose_63d_slope_v103_signal,
    f067fcf_f067_fcf_inflection_sign_5d_x_closedif_10d_slope_v104_signal,
    f067fcf_f067_fcf_inflection_sign_5d_ema_x_close_42d_slope_v105_signal,
    f067fcf_f067_fcf_inflection_sign_10d_x_close_5d_slope_v106_signal,
    f067fcf_f067_fcf_inflection_sign_10d_x_logclose_21d_slope_v107_signal,
    f067fcf_f067_fcf_inflection_sign_10d_x_meanclose_63d_slope_v108_signal,
    f067fcf_f067_fcf_inflection_sign_10d_x_closedif_10d_slope_v109_signal,
    f067fcf_f067_fcf_inflection_sign_10d_ema_x_close_42d_slope_v110_signal,
    f067fcf_f067_fcf_inflection_sign_21d_x_close_5d_slope_v111_signal,
    f067fcf_f067_fcf_inflection_sign_21d_x_logclose_21d_slope_v112_signal,
    f067fcf_f067_fcf_inflection_sign_21d_x_meanclose_63d_slope_v113_signal,
    f067fcf_f067_fcf_inflection_sign_21d_x_closedif_10d_slope_v114_signal,
    f067fcf_f067_fcf_inflection_sign_21d_ema_x_close_42d_slope_v115_signal,
    f067fcf_f067_fcf_inflection_sign_42d_x_close_5d_slope_v116_signal,
    f067fcf_f067_fcf_inflection_sign_42d_x_logclose_21d_slope_v117_signal,
    f067fcf_f067_fcf_inflection_sign_42d_x_meanclose_63d_slope_v118_signal,
    f067fcf_f067_fcf_inflection_sign_42d_x_closedif_10d_slope_v119_signal,
    f067fcf_f067_fcf_inflection_sign_42d_ema_x_close_42d_slope_v120_signal,
    f067fcf_f067_fcf_inflection_sign_63d_x_close_5d_slope_v121_signal,
    f067fcf_f067_fcf_inflection_sign_63d_x_logclose_21d_slope_v122_signal,
    f067fcf_f067_fcf_inflection_sign_63d_x_meanclose_63d_slope_v123_signal,
    f067fcf_f067_fcf_inflection_sign_63d_x_closedif_10d_slope_v124_signal,
    f067fcf_f067_fcf_inflection_sign_63d_ema_x_close_42d_slope_v125_signal,
    f067fcf_f067_fcf_inflection_sign_126d_x_close_5d_slope_v126_signal,
    f067fcf_f067_fcf_inflection_sign_126d_x_logclose_21d_slope_v127_signal,
    f067fcf_f067_fcf_inflection_sign_126d_x_meanclose_63d_slope_v128_signal,
    f067fcf_f067_fcf_inflection_sign_126d_x_closedif_10d_slope_v129_signal,
    f067fcf_f067_fcf_inflection_sign_126d_ema_x_close_42d_slope_v130_signal,
    f067fcf_f067_fcf_inflection_sign_189d_x_close_5d_slope_v131_signal,
    f067fcf_f067_fcf_inflection_sign_189d_x_logclose_21d_slope_v132_signal,
    f067fcf_f067_fcf_inflection_sign_189d_x_meanclose_63d_slope_v133_signal,
    f067fcf_f067_fcf_inflection_sign_189d_x_closedif_10d_slope_v134_signal,
    f067fcf_f067_fcf_inflection_sign_189d_ema_x_close_42d_slope_v135_signal,
    f067fcf_f067_fcf_inflection_sign_252d_x_close_5d_slope_v136_signal,
    f067fcf_f067_fcf_inflection_sign_252d_x_logclose_21d_slope_v137_signal,
    f067fcf_f067_fcf_inflection_sign_252d_x_meanclose_63d_slope_v138_signal,
    f067fcf_f067_fcf_inflection_sign_252d_x_closedif_10d_slope_v139_signal,
    f067fcf_f067_fcf_inflection_sign_252d_ema_x_close_42d_slope_v140_signal,
    f067fcf_f067_fcf_inflection_sign_378d_x_close_5d_slope_v141_signal,
    f067fcf_f067_fcf_inflection_sign_378d_x_logclose_21d_slope_v142_signal,
    f067fcf_f067_fcf_inflection_sign_378d_x_meanclose_63d_slope_v143_signal,
    f067fcf_f067_fcf_inflection_sign_378d_x_closedif_10d_slope_v144_signal,
    f067fcf_f067_fcf_inflection_sign_378d_ema_x_close_42d_slope_v145_signal,
    f067fcf_f067_fcf_inflection_sign_504d_x_close_5d_slope_v146_signal,
    f067fcf_f067_fcf_inflection_sign_504d_x_logclose_21d_slope_v147_signal,
    f067fcf_f067_fcf_inflection_sign_504d_x_meanclose_63d_slope_v148_signal,
    f067fcf_f067_fcf_inflection_sign_504d_x_closedif_10d_slope_v149_signal,
    f067fcf_f067_fcf_inflection_sign_504d_ema_x_close_42d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F067_FCF_INFLECTION_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    fcf = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="fcf")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    cols = {
        "closeadj": closeadj,
        "fcf": fcf,
        "revenue": revenue,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f067_fcf_sign', '_f067_fcf_inflection', '_f067_self_funding_turn')
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
    print(f"OK f067_fcf_inflection_slope_2nd_derivatives_001_150_claude: {n_features} features pass")
