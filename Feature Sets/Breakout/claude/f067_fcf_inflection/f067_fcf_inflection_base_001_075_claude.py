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


# sign_5d_x_close base
def f067fcf_f067_fcf_inflection_sign_5d_x_close_base_v001_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 5)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_10d_x_close base
def f067fcf_f067_fcf_inflection_sign_10d_x_close_base_v002_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 10)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_21d_x_close base
def f067fcf_f067_fcf_inflection_sign_21d_x_close_base_v003_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 21)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_42d_x_close base
def f067fcf_f067_fcf_inflection_sign_42d_x_close_base_v004_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 42)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_63d_x_close base
def f067fcf_f067_fcf_inflection_sign_63d_x_close_base_v005_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 63)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_126d_x_close base
def f067fcf_f067_fcf_inflection_sign_126d_x_close_base_v006_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 126)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_189d_x_close base
def f067fcf_f067_fcf_inflection_sign_189d_x_close_base_v007_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 189)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_252d_x_close base
def f067fcf_f067_fcf_inflection_sign_252d_x_close_base_v008_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 252)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_378d_x_close base
def f067fcf_f067_fcf_inflection_sign_378d_x_close_base_v009_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 378)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_504d_x_close base
def f067fcf_f067_fcf_inflection_sign_504d_x_close_base_v010_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 504)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_5d_x_close base
def f067fcf_f067_fcf_inflection_inflection_5d_x_close_base_v011_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_10d_x_close base
def f067fcf_f067_fcf_inflection_inflection_10d_x_close_base_v012_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_21d_x_close base
def f067fcf_f067_fcf_inflection_inflection_21d_x_close_base_v013_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_42d_x_close base
def f067fcf_f067_fcf_inflection_inflection_42d_x_close_base_v014_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_63d_x_close base
def f067fcf_f067_fcf_inflection_inflection_63d_x_close_base_v015_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_126d_x_close base
def f067fcf_f067_fcf_inflection_inflection_126d_x_close_base_v016_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_189d_x_close base
def f067fcf_f067_fcf_inflection_inflection_189d_x_close_base_v017_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_252d_x_close base
def f067fcf_f067_fcf_inflection_inflection_252d_x_close_base_v018_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_378d_x_close base
def f067fcf_f067_fcf_inflection_inflection_378d_x_close_base_v019_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_504d_x_close base
def f067fcf_f067_fcf_inflection_inflection_504d_x_close_base_v020_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_5d_x_close base
def f067fcf_f067_fcf_inflection_selffund_5d_x_close_base_v021_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_10d_x_close base
def f067fcf_f067_fcf_inflection_selffund_10d_x_close_base_v022_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_21d_x_close base
def f067fcf_f067_fcf_inflection_selffund_21d_x_close_base_v023_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_42d_x_close base
def f067fcf_f067_fcf_inflection_selffund_42d_x_close_base_v024_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_63d_x_close base
def f067fcf_f067_fcf_inflection_selffund_63d_x_close_base_v025_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_126d_x_close base
def f067fcf_f067_fcf_inflection_selffund_126d_x_close_base_v026_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_189d_x_close base
def f067fcf_f067_fcf_inflection_selffund_189d_x_close_base_v027_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_252d_x_close base
def f067fcf_f067_fcf_inflection_selffund_252d_x_close_base_v028_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_378d_x_close base
def f067fcf_f067_fcf_inflection_selffund_378d_x_close_base_v029_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_504d_x_close base
def f067fcf_f067_fcf_inflection_selffund_504d_x_close_base_v030_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sign_5d_x_logclose base
def f067fcf_f067_fcf_inflection_sign_5d_x_logclose_base_v031_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 5)
    result = base * np.log(_safe_div(closeadj, _mean(closeadj, 252)).abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_10d_x_logclose base
def f067fcf_f067_fcf_inflection_sign_10d_x_logclose_base_v032_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 10)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_21d_x_logclose base
def f067fcf_f067_fcf_inflection_sign_21d_x_logclose_base_v033_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_42d_x_logclose base
def f067fcf_f067_fcf_inflection_sign_42d_x_logclose_base_v034_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_63d_x_logclose base
def f067fcf_f067_fcf_inflection_sign_63d_x_logclose_base_v035_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_126d_x_logclose base
def f067fcf_f067_fcf_inflection_sign_126d_x_logclose_base_v036_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_189d_x_logclose base
def f067fcf_f067_fcf_inflection_sign_189d_x_logclose_base_v037_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_252d_x_logclose base
def f067fcf_f067_fcf_inflection_sign_252d_x_logclose_base_v038_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_378d_x_logclose base
def f067fcf_f067_fcf_inflection_sign_378d_x_logclose_base_v039_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 378)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_504d_x_logclose base
def f067fcf_f067_fcf_inflection_sign_504d_x_logclose_base_v040_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_5d_x_logclose base
def f067fcf_f067_fcf_inflection_inflection_5d_x_logclose_base_v041_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 5)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_10d_x_logclose base
def f067fcf_f067_fcf_inflection_inflection_10d_x_logclose_base_v042_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 10)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_21d_x_logclose base
def f067fcf_f067_fcf_inflection_inflection_21d_x_logclose_base_v043_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_42d_x_logclose base
def f067fcf_f067_fcf_inflection_inflection_42d_x_logclose_base_v044_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_63d_x_logclose base
def f067fcf_f067_fcf_inflection_inflection_63d_x_logclose_base_v045_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_126d_x_logclose base
def f067fcf_f067_fcf_inflection_inflection_126d_x_logclose_base_v046_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_189d_x_logclose base
def f067fcf_f067_fcf_inflection_inflection_189d_x_logclose_base_v047_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_252d_x_logclose base
def f067fcf_f067_fcf_inflection_inflection_252d_x_logclose_base_v048_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_378d_x_logclose base
def f067fcf_f067_fcf_inflection_inflection_378d_x_logclose_base_v049_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 378)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_504d_x_logclose base
def f067fcf_f067_fcf_inflection_inflection_504d_x_logclose_base_v050_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_5d_x_logclose base
def f067fcf_f067_fcf_inflection_selffund_5d_x_logclose_base_v051_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 5)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_10d_x_logclose base
def f067fcf_f067_fcf_inflection_selffund_10d_x_logclose_base_v052_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 10)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_21d_x_logclose base
def f067fcf_f067_fcf_inflection_selffund_21d_x_logclose_base_v053_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_42d_x_logclose base
def f067fcf_f067_fcf_inflection_selffund_42d_x_logclose_base_v054_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 42)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_63d_x_logclose base
def f067fcf_f067_fcf_inflection_selffund_63d_x_logclose_base_v055_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_126d_x_logclose base
def f067fcf_f067_fcf_inflection_selffund_126d_x_logclose_base_v056_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 126)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_189d_x_logclose base
def f067fcf_f067_fcf_inflection_selffund_189d_x_logclose_base_v057_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 189)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_252d_x_logclose base
def f067fcf_f067_fcf_inflection_selffund_252d_x_logclose_base_v058_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_378d_x_logclose base
def f067fcf_f067_fcf_inflection_selffund_378d_x_logclose_base_v059_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 378)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_504d_x_logclose base
def f067fcf_f067_fcf_inflection_selffund_504d_x_logclose_base_v060_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan) + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_5d_x_meanclose base
def f067fcf_f067_fcf_inflection_sign_5d_x_meanclose_base_v061_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 5)
    result = base * _safe_div(_mean(closeadj, 5), _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_10d_x_meanclose base
def f067fcf_f067_fcf_inflection_sign_10d_x_meanclose_base_v062_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 10)
    result = base * _safe_div(_mean(closeadj, 10), _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_21d_x_meanclose base
def f067fcf_f067_fcf_inflection_sign_21d_x_meanclose_base_v063_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_42d_x_meanclose base
def f067fcf_f067_fcf_inflection_sign_42d_x_meanclose_base_v064_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 42)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_63d_x_meanclose base
def f067fcf_f067_fcf_inflection_sign_63d_x_meanclose_base_v065_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_126d_x_meanclose base
def f067fcf_f067_fcf_inflection_sign_126d_x_meanclose_base_v066_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 126)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_189d_x_meanclose base
def f067fcf_f067_fcf_inflection_sign_189d_x_meanclose_base_v067_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 189)
    result = base * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_252d_x_meanclose base
def f067fcf_f067_fcf_inflection_sign_252d_x_meanclose_base_v068_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_378d_x_meanclose base
def f067fcf_f067_fcf_inflection_sign_378d_x_meanclose_base_v069_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 378)
    result = base * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_504d_x_meanclose base
def f067fcf_f067_fcf_inflection_sign_504d_x_meanclose_base_v070_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 504)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_5d_x_meanclose base
def f067fcf_f067_fcf_inflection_inflection_5d_x_meanclose_base_v071_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 5)
    result = base * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_10d_x_meanclose base
def f067fcf_f067_fcf_inflection_inflection_10d_x_meanclose_base_v072_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 10)
    result = base * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_21d_x_meanclose base
def f067fcf_f067_fcf_inflection_inflection_21d_x_meanclose_base_v073_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_42d_x_meanclose base
def f067fcf_f067_fcf_inflection_inflection_42d_x_meanclose_base_v074_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 42)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_63d_x_meanclose base
def f067fcf_f067_fcf_inflection_inflection_63d_x_meanclose_base_v075_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f067fcf_f067_fcf_inflection_sign_5d_x_close_base_v001_signal,
    f067fcf_f067_fcf_inflection_sign_10d_x_close_base_v002_signal,
    f067fcf_f067_fcf_inflection_sign_21d_x_close_base_v003_signal,
    f067fcf_f067_fcf_inflection_sign_42d_x_close_base_v004_signal,
    f067fcf_f067_fcf_inflection_sign_63d_x_close_base_v005_signal,
    f067fcf_f067_fcf_inflection_sign_126d_x_close_base_v006_signal,
    f067fcf_f067_fcf_inflection_sign_189d_x_close_base_v007_signal,
    f067fcf_f067_fcf_inflection_sign_252d_x_close_base_v008_signal,
    f067fcf_f067_fcf_inflection_sign_378d_x_close_base_v009_signal,
    f067fcf_f067_fcf_inflection_sign_504d_x_close_base_v010_signal,
    f067fcf_f067_fcf_inflection_inflection_5d_x_close_base_v011_signal,
    f067fcf_f067_fcf_inflection_inflection_10d_x_close_base_v012_signal,
    f067fcf_f067_fcf_inflection_inflection_21d_x_close_base_v013_signal,
    f067fcf_f067_fcf_inflection_inflection_42d_x_close_base_v014_signal,
    f067fcf_f067_fcf_inflection_inflection_63d_x_close_base_v015_signal,
    f067fcf_f067_fcf_inflection_inflection_126d_x_close_base_v016_signal,
    f067fcf_f067_fcf_inflection_inflection_189d_x_close_base_v017_signal,
    f067fcf_f067_fcf_inflection_inflection_252d_x_close_base_v018_signal,
    f067fcf_f067_fcf_inflection_inflection_378d_x_close_base_v019_signal,
    f067fcf_f067_fcf_inflection_inflection_504d_x_close_base_v020_signal,
    f067fcf_f067_fcf_inflection_selffund_5d_x_close_base_v021_signal,
    f067fcf_f067_fcf_inflection_selffund_10d_x_close_base_v022_signal,
    f067fcf_f067_fcf_inflection_selffund_21d_x_close_base_v023_signal,
    f067fcf_f067_fcf_inflection_selffund_42d_x_close_base_v024_signal,
    f067fcf_f067_fcf_inflection_selffund_63d_x_close_base_v025_signal,
    f067fcf_f067_fcf_inflection_selffund_126d_x_close_base_v026_signal,
    f067fcf_f067_fcf_inflection_selffund_189d_x_close_base_v027_signal,
    f067fcf_f067_fcf_inflection_selffund_252d_x_close_base_v028_signal,
    f067fcf_f067_fcf_inflection_selffund_378d_x_close_base_v029_signal,
    f067fcf_f067_fcf_inflection_selffund_504d_x_close_base_v030_signal,
    f067fcf_f067_fcf_inflection_sign_5d_x_logclose_base_v031_signal,
    f067fcf_f067_fcf_inflection_sign_10d_x_logclose_base_v032_signal,
    f067fcf_f067_fcf_inflection_sign_21d_x_logclose_base_v033_signal,
    f067fcf_f067_fcf_inflection_sign_42d_x_logclose_base_v034_signal,
    f067fcf_f067_fcf_inflection_sign_63d_x_logclose_base_v035_signal,
    f067fcf_f067_fcf_inflection_sign_126d_x_logclose_base_v036_signal,
    f067fcf_f067_fcf_inflection_sign_189d_x_logclose_base_v037_signal,
    f067fcf_f067_fcf_inflection_sign_252d_x_logclose_base_v038_signal,
    f067fcf_f067_fcf_inflection_sign_378d_x_logclose_base_v039_signal,
    f067fcf_f067_fcf_inflection_sign_504d_x_logclose_base_v040_signal,
    f067fcf_f067_fcf_inflection_inflection_5d_x_logclose_base_v041_signal,
    f067fcf_f067_fcf_inflection_inflection_10d_x_logclose_base_v042_signal,
    f067fcf_f067_fcf_inflection_inflection_21d_x_logclose_base_v043_signal,
    f067fcf_f067_fcf_inflection_inflection_42d_x_logclose_base_v044_signal,
    f067fcf_f067_fcf_inflection_inflection_63d_x_logclose_base_v045_signal,
    f067fcf_f067_fcf_inflection_inflection_126d_x_logclose_base_v046_signal,
    f067fcf_f067_fcf_inflection_inflection_189d_x_logclose_base_v047_signal,
    f067fcf_f067_fcf_inflection_inflection_252d_x_logclose_base_v048_signal,
    f067fcf_f067_fcf_inflection_inflection_378d_x_logclose_base_v049_signal,
    f067fcf_f067_fcf_inflection_inflection_504d_x_logclose_base_v050_signal,
    f067fcf_f067_fcf_inflection_selffund_5d_x_logclose_base_v051_signal,
    f067fcf_f067_fcf_inflection_selffund_10d_x_logclose_base_v052_signal,
    f067fcf_f067_fcf_inflection_selffund_21d_x_logclose_base_v053_signal,
    f067fcf_f067_fcf_inflection_selffund_42d_x_logclose_base_v054_signal,
    f067fcf_f067_fcf_inflection_selffund_63d_x_logclose_base_v055_signal,
    f067fcf_f067_fcf_inflection_selffund_126d_x_logclose_base_v056_signal,
    f067fcf_f067_fcf_inflection_selffund_189d_x_logclose_base_v057_signal,
    f067fcf_f067_fcf_inflection_selffund_252d_x_logclose_base_v058_signal,
    f067fcf_f067_fcf_inflection_selffund_378d_x_logclose_base_v059_signal,
    f067fcf_f067_fcf_inflection_selffund_504d_x_logclose_base_v060_signal,
    f067fcf_f067_fcf_inflection_sign_5d_x_meanclose_base_v061_signal,
    f067fcf_f067_fcf_inflection_sign_10d_x_meanclose_base_v062_signal,
    f067fcf_f067_fcf_inflection_sign_21d_x_meanclose_base_v063_signal,
    f067fcf_f067_fcf_inflection_sign_42d_x_meanclose_base_v064_signal,
    f067fcf_f067_fcf_inflection_sign_63d_x_meanclose_base_v065_signal,
    f067fcf_f067_fcf_inflection_sign_126d_x_meanclose_base_v066_signal,
    f067fcf_f067_fcf_inflection_sign_189d_x_meanclose_base_v067_signal,
    f067fcf_f067_fcf_inflection_sign_252d_x_meanclose_base_v068_signal,
    f067fcf_f067_fcf_inflection_sign_378d_x_meanclose_base_v069_signal,
    f067fcf_f067_fcf_inflection_sign_504d_x_meanclose_base_v070_signal,
    f067fcf_f067_fcf_inflection_inflection_5d_x_meanclose_base_v071_signal,
    f067fcf_f067_fcf_inflection_inflection_10d_x_meanclose_base_v072_signal,
    f067fcf_f067_fcf_inflection_inflection_21d_x_meanclose_base_v073_signal,
    f067fcf_f067_fcf_inflection_inflection_42d_x_meanclose_base_v074_signal,
    f067fcf_f067_fcf_inflection_inflection_63d_x_meanclose_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F067_FCF_INFLECTION_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f067_fcf_inflection_base_001_075_claude: {n_features} features pass")
