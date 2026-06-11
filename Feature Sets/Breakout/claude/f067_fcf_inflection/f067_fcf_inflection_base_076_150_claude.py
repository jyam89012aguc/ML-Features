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


# inflection_126d_x_meanclose base
def f067fcf_f067_fcf_inflection_inflection_126d_x_meanclose_base_v076_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 126)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_189d_x_meanclose base
def f067fcf_f067_fcf_inflection_inflection_189d_x_meanclose_base_v077_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 189)
    result = base * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_252d_x_meanclose base
def f067fcf_f067_fcf_inflection_inflection_252d_x_meanclose_base_v078_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_378d_x_meanclose base
def f067fcf_f067_fcf_inflection_inflection_378d_x_meanclose_base_v079_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 378)
    result = base * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_504d_x_meanclose base
def f067fcf_f067_fcf_inflection_inflection_504d_x_meanclose_base_v080_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 504)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_5d_x_meanclose base
def f067fcf_f067_fcf_inflection_selffund_5d_x_meanclose_base_v081_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 5)
    result = base * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_10d_x_meanclose base
def f067fcf_f067_fcf_inflection_selffund_10d_x_meanclose_base_v082_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 10)
    result = base * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_21d_x_meanclose base
def f067fcf_f067_fcf_inflection_selffund_21d_x_meanclose_base_v083_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_42d_x_meanclose base
def f067fcf_f067_fcf_inflection_selffund_42d_x_meanclose_base_v084_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 42)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_63d_x_meanclose base
def f067fcf_f067_fcf_inflection_selffund_63d_x_meanclose_base_v085_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_126d_x_meanclose base
def f067fcf_f067_fcf_inflection_selffund_126d_x_meanclose_base_v086_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 126)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_189d_x_meanclose base
def f067fcf_f067_fcf_inflection_selffund_189d_x_meanclose_base_v087_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 189)
    result = base * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_252d_x_meanclose base
def f067fcf_f067_fcf_inflection_selffund_252d_x_meanclose_base_v088_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_378d_x_meanclose base
def f067fcf_f067_fcf_inflection_selffund_378d_x_meanclose_base_v089_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 378)
    result = base * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_504d_x_meanclose base
def f067fcf_f067_fcf_inflection_selffund_504d_x_meanclose_base_v090_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 504)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# sign_5d_x_closedif base
def f067fcf_f067_fcf_inflection_sign_5d_x_closedif_base_v091_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 5)
    result = base * closeadj.diff(1).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# sign_10d_x_closedif base
def f067fcf_f067_fcf_inflection_sign_10d_x_closedif_base_v092_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 10)
    result = base * closeadj.diff(2).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# sign_21d_x_closedif base
def f067fcf_f067_fcf_inflection_sign_21d_x_closedif_base_v093_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 21)
    result = base * closeadj.diff(5).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# sign_42d_x_closedif base
def f067fcf_f067_fcf_inflection_sign_42d_x_closedif_base_v094_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 42)
    result = base * closeadj.diff(10).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# sign_63d_x_closedif base
def f067fcf_f067_fcf_inflection_sign_63d_x_closedif_base_v095_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 63)
    result = base * closeadj.diff(15).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# sign_126d_x_closedif base
def f067fcf_f067_fcf_inflection_sign_126d_x_closedif_base_v096_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 126)
    result = base * closeadj.diff(31).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# sign_189d_x_closedif base
def f067fcf_f067_fcf_inflection_sign_189d_x_closedif_base_v097_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 189)
    result = base * closeadj.diff(47).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# sign_252d_x_closedif base
def f067fcf_f067_fcf_inflection_sign_252d_x_closedif_base_v098_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 252)
    result = base * closeadj.diff(63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# sign_378d_x_closedif base
def f067fcf_f067_fcf_inflection_sign_378d_x_closedif_base_v099_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 378)
    result = base * closeadj.diff(94).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# sign_504d_x_closedif base
def f067fcf_f067_fcf_inflection_sign_504d_x_closedif_base_v100_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 504)
    result = base * closeadj.diff(126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_5d_x_closedif base
def f067fcf_f067_fcf_inflection_inflection_5d_x_closedif_base_v101_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 5)
    result = base * closeadj.diff(1).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_10d_x_closedif base
def f067fcf_f067_fcf_inflection_inflection_10d_x_closedif_base_v102_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 10)
    result = base * closeadj.diff(2).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_21d_x_closedif base
def f067fcf_f067_fcf_inflection_inflection_21d_x_closedif_base_v103_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 21)
    result = base * closeadj.diff(5).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_42d_x_closedif base
def f067fcf_f067_fcf_inflection_inflection_42d_x_closedif_base_v104_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 42)
    result = base * closeadj.diff(10).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_63d_x_closedif base
def f067fcf_f067_fcf_inflection_inflection_63d_x_closedif_base_v105_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 63)
    result = base * closeadj.diff(15).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_126d_x_closedif base
def f067fcf_f067_fcf_inflection_inflection_126d_x_closedif_base_v106_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 126)
    result = base * closeadj.diff(31).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_189d_x_closedif base
def f067fcf_f067_fcf_inflection_inflection_189d_x_closedif_base_v107_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 189)
    result = base * closeadj.diff(47).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_252d_x_closedif base
def f067fcf_f067_fcf_inflection_inflection_252d_x_closedif_base_v108_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 252)
    result = base * closeadj.diff(63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_378d_x_closedif base
def f067fcf_f067_fcf_inflection_inflection_378d_x_closedif_base_v109_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 378)
    result = base * closeadj.diff(94).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_504d_x_closedif base
def f067fcf_f067_fcf_inflection_inflection_504d_x_closedif_base_v110_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 504)
    result = base * closeadj.diff(126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_5d_x_closedif base
def f067fcf_f067_fcf_inflection_selffund_5d_x_closedif_base_v111_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 5)
    result = base * closeadj.diff(1).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_10d_x_closedif base
def f067fcf_f067_fcf_inflection_selffund_10d_x_closedif_base_v112_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 10)
    result = base * closeadj.diff(2).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_21d_x_closedif base
def f067fcf_f067_fcf_inflection_selffund_21d_x_closedif_base_v113_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 21)
    result = base * closeadj.diff(5).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_42d_x_closedif base
def f067fcf_f067_fcf_inflection_selffund_42d_x_closedif_base_v114_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 42)
    result = base * closeadj.diff(10).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_63d_x_closedif base
def f067fcf_f067_fcf_inflection_selffund_63d_x_closedif_base_v115_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 63)
    result = base * closeadj.diff(15).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_126d_x_closedif base
def f067fcf_f067_fcf_inflection_selffund_126d_x_closedif_base_v116_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 126)
    result = base * closeadj.diff(31).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_189d_x_closedif base
def f067fcf_f067_fcf_inflection_selffund_189d_x_closedif_base_v117_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 189)
    result = base * closeadj.diff(47).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_252d_x_closedif base
def f067fcf_f067_fcf_inflection_selffund_252d_x_closedif_base_v118_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 252)
    result = base * closeadj.diff(63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_378d_x_closedif base
def f067fcf_f067_fcf_inflection_selffund_378d_x_closedif_base_v119_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 378)
    result = base * closeadj.diff(94).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_504d_x_closedif base
def f067fcf_f067_fcf_inflection_selffund_504d_x_closedif_base_v120_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 504)
    result = base * closeadj.diff(126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# sign_5d_ema_x_close base
def f067fcf_f067_fcf_inflection_sign_5d_ema_x_close_base_v121_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 5)
    result = _ema(base, 2) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_10d_ema_x_close base
def f067fcf_f067_fcf_inflection_sign_10d_ema_x_close_base_v122_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 10)
    result = _ema(base, 5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_21d_ema_x_close base
def f067fcf_f067_fcf_inflection_sign_21d_ema_x_close_base_v123_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 21)
    result = _ema(base, 10) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_42d_ema_x_close base
def f067fcf_f067_fcf_inflection_sign_42d_ema_x_close_base_v124_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 42)
    result = _ema(base, 21) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_63d_ema_x_close base
def f067fcf_f067_fcf_inflection_sign_63d_ema_x_close_base_v125_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 63)
    result = _ema(base, 31) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_126d_ema_x_close base
def f067fcf_f067_fcf_inflection_sign_126d_ema_x_close_base_v126_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 126)
    result = _ema(base, 63) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_189d_ema_x_close base
def f067fcf_f067_fcf_inflection_sign_189d_ema_x_close_base_v127_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 189)
    result = _ema(base, 94) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_252d_ema_x_close base
def f067fcf_f067_fcf_inflection_sign_252d_ema_x_close_base_v128_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 252)
    result = _ema(base, 126) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_378d_ema_x_close base
def f067fcf_f067_fcf_inflection_sign_378d_ema_x_close_base_v129_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 378)
    result = _ema(base, 189) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# sign_504d_ema_x_close base
def f067fcf_f067_fcf_inflection_sign_504d_ema_x_close_base_v130_signal(fcf, revenue, closeadj):
    base = _f067_fcf_sign(fcf, 504)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_5d_ema_x_close base
def f067fcf_f067_fcf_inflection_inflection_5d_ema_x_close_base_v131_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 5)
    result = _ema(base, 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_10d_ema_x_close base
def f067fcf_f067_fcf_inflection_inflection_10d_ema_x_close_base_v132_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_21d_ema_x_close base
def f067fcf_f067_fcf_inflection_inflection_21d_ema_x_close_base_v133_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 21)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_42d_ema_x_close base
def f067fcf_f067_fcf_inflection_inflection_42d_ema_x_close_base_v134_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 42)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_63d_ema_x_close base
def f067fcf_f067_fcf_inflection_inflection_63d_ema_x_close_base_v135_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 63)
    result = _ema(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_126d_ema_x_close base
def f067fcf_f067_fcf_inflection_inflection_126d_ema_x_close_base_v136_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_189d_ema_x_close base
def f067fcf_f067_fcf_inflection_inflection_189d_ema_x_close_base_v137_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 189)
    result = _ema(base, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_252d_ema_x_close base
def f067fcf_f067_fcf_inflection_inflection_252d_ema_x_close_base_v138_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 252)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_378d_ema_x_close base
def f067fcf_f067_fcf_inflection_inflection_378d_ema_x_close_base_v139_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 378)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inflection_504d_ema_x_close base
def f067fcf_f067_fcf_inflection_inflection_504d_ema_x_close_base_v140_signal(fcf, revenue, closeadj):
    base = _f067_fcf_inflection(fcf, 504)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_5d_ema_x_close base
def f067fcf_f067_fcf_inflection_selffund_5d_ema_x_close_base_v141_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 5)
    result = _ema(base, 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_10d_ema_x_close base
def f067fcf_f067_fcf_inflection_selffund_10d_ema_x_close_base_v142_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_21d_ema_x_close base
def f067fcf_f067_fcf_inflection_selffund_21d_ema_x_close_base_v143_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 21)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_42d_ema_x_close base
def f067fcf_f067_fcf_inflection_selffund_42d_ema_x_close_base_v144_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 42)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_63d_ema_x_close base
def f067fcf_f067_fcf_inflection_selffund_63d_ema_x_close_base_v145_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 63)
    result = _ema(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_126d_ema_x_close base
def f067fcf_f067_fcf_inflection_selffund_126d_ema_x_close_base_v146_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_189d_ema_x_close base
def f067fcf_f067_fcf_inflection_selffund_189d_ema_x_close_base_v147_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 189)
    result = _ema(base, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_252d_ema_x_close base
def f067fcf_f067_fcf_inflection_selffund_252d_ema_x_close_base_v148_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 252)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_378d_ema_x_close base
def f067fcf_f067_fcf_inflection_selffund_378d_ema_x_close_base_v149_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 378)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# selffund_504d_ema_x_close base
def f067fcf_f067_fcf_inflection_selffund_504d_ema_x_close_base_v150_signal(fcf, revenue, closeadj):
    base = _f067_self_funding_turn(fcf, 504)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f067fcf_f067_fcf_inflection_inflection_126d_x_meanclose_base_v076_signal,
    f067fcf_f067_fcf_inflection_inflection_189d_x_meanclose_base_v077_signal,
    f067fcf_f067_fcf_inflection_inflection_252d_x_meanclose_base_v078_signal,
    f067fcf_f067_fcf_inflection_inflection_378d_x_meanclose_base_v079_signal,
    f067fcf_f067_fcf_inflection_inflection_504d_x_meanclose_base_v080_signal,
    f067fcf_f067_fcf_inflection_selffund_5d_x_meanclose_base_v081_signal,
    f067fcf_f067_fcf_inflection_selffund_10d_x_meanclose_base_v082_signal,
    f067fcf_f067_fcf_inflection_selffund_21d_x_meanclose_base_v083_signal,
    f067fcf_f067_fcf_inflection_selffund_42d_x_meanclose_base_v084_signal,
    f067fcf_f067_fcf_inflection_selffund_63d_x_meanclose_base_v085_signal,
    f067fcf_f067_fcf_inflection_selffund_126d_x_meanclose_base_v086_signal,
    f067fcf_f067_fcf_inflection_selffund_189d_x_meanclose_base_v087_signal,
    f067fcf_f067_fcf_inflection_selffund_252d_x_meanclose_base_v088_signal,
    f067fcf_f067_fcf_inflection_selffund_378d_x_meanclose_base_v089_signal,
    f067fcf_f067_fcf_inflection_selffund_504d_x_meanclose_base_v090_signal,
    f067fcf_f067_fcf_inflection_sign_5d_x_closedif_base_v091_signal,
    f067fcf_f067_fcf_inflection_sign_10d_x_closedif_base_v092_signal,
    f067fcf_f067_fcf_inflection_sign_21d_x_closedif_base_v093_signal,
    f067fcf_f067_fcf_inflection_sign_42d_x_closedif_base_v094_signal,
    f067fcf_f067_fcf_inflection_sign_63d_x_closedif_base_v095_signal,
    f067fcf_f067_fcf_inflection_sign_126d_x_closedif_base_v096_signal,
    f067fcf_f067_fcf_inflection_sign_189d_x_closedif_base_v097_signal,
    f067fcf_f067_fcf_inflection_sign_252d_x_closedif_base_v098_signal,
    f067fcf_f067_fcf_inflection_sign_378d_x_closedif_base_v099_signal,
    f067fcf_f067_fcf_inflection_sign_504d_x_closedif_base_v100_signal,
    f067fcf_f067_fcf_inflection_inflection_5d_x_closedif_base_v101_signal,
    f067fcf_f067_fcf_inflection_inflection_10d_x_closedif_base_v102_signal,
    f067fcf_f067_fcf_inflection_inflection_21d_x_closedif_base_v103_signal,
    f067fcf_f067_fcf_inflection_inflection_42d_x_closedif_base_v104_signal,
    f067fcf_f067_fcf_inflection_inflection_63d_x_closedif_base_v105_signal,
    f067fcf_f067_fcf_inflection_inflection_126d_x_closedif_base_v106_signal,
    f067fcf_f067_fcf_inflection_inflection_189d_x_closedif_base_v107_signal,
    f067fcf_f067_fcf_inflection_inflection_252d_x_closedif_base_v108_signal,
    f067fcf_f067_fcf_inflection_inflection_378d_x_closedif_base_v109_signal,
    f067fcf_f067_fcf_inflection_inflection_504d_x_closedif_base_v110_signal,
    f067fcf_f067_fcf_inflection_selffund_5d_x_closedif_base_v111_signal,
    f067fcf_f067_fcf_inflection_selffund_10d_x_closedif_base_v112_signal,
    f067fcf_f067_fcf_inflection_selffund_21d_x_closedif_base_v113_signal,
    f067fcf_f067_fcf_inflection_selffund_42d_x_closedif_base_v114_signal,
    f067fcf_f067_fcf_inflection_selffund_63d_x_closedif_base_v115_signal,
    f067fcf_f067_fcf_inflection_selffund_126d_x_closedif_base_v116_signal,
    f067fcf_f067_fcf_inflection_selffund_189d_x_closedif_base_v117_signal,
    f067fcf_f067_fcf_inflection_selffund_252d_x_closedif_base_v118_signal,
    f067fcf_f067_fcf_inflection_selffund_378d_x_closedif_base_v119_signal,
    f067fcf_f067_fcf_inflection_selffund_504d_x_closedif_base_v120_signal,
    f067fcf_f067_fcf_inflection_sign_5d_ema_x_close_base_v121_signal,
    f067fcf_f067_fcf_inflection_sign_10d_ema_x_close_base_v122_signal,
    f067fcf_f067_fcf_inflection_sign_21d_ema_x_close_base_v123_signal,
    f067fcf_f067_fcf_inflection_sign_42d_ema_x_close_base_v124_signal,
    f067fcf_f067_fcf_inflection_sign_63d_ema_x_close_base_v125_signal,
    f067fcf_f067_fcf_inflection_sign_126d_ema_x_close_base_v126_signal,
    f067fcf_f067_fcf_inflection_sign_189d_ema_x_close_base_v127_signal,
    f067fcf_f067_fcf_inflection_sign_252d_ema_x_close_base_v128_signal,
    f067fcf_f067_fcf_inflection_sign_378d_ema_x_close_base_v129_signal,
    f067fcf_f067_fcf_inflection_sign_504d_ema_x_close_base_v130_signal,
    f067fcf_f067_fcf_inflection_inflection_5d_ema_x_close_base_v131_signal,
    f067fcf_f067_fcf_inflection_inflection_10d_ema_x_close_base_v132_signal,
    f067fcf_f067_fcf_inflection_inflection_21d_ema_x_close_base_v133_signal,
    f067fcf_f067_fcf_inflection_inflection_42d_ema_x_close_base_v134_signal,
    f067fcf_f067_fcf_inflection_inflection_63d_ema_x_close_base_v135_signal,
    f067fcf_f067_fcf_inflection_inflection_126d_ema_x_close_base_v136_signal,
    f067fcf_f067_fcf_inflection_inflection_189d_ema_x_close_base_v137_signal,
    f067fcf_f067_fcf_inflection_inflection_252d_ema_x_close_base_v138_signal,
    f067fcf_f067_fcf_inflection_inflection_378d_ema_x_close_base_v139_signal,
    f067fcf_f067_fcf_inflection_inflection_504d_ema_x_close_base_v140_signal,
    f067fcf_f067_fcf_inflection_selffund_5d_ema_x_close_base_v141_signal,
    f067fcf_f067_fcf_inflection_selffund_10d_ema_x_close_base_v142_signal,
    f067fcf_f067_fcf_inflection_selffund_21d_ema_x_close_base_v143_signal,
    f067fcf_f067_fcf_inflection_selffund_42d_ema_x_close_base_v144_signal,
    f067fcf_f067_fcf_inflection_selffund_63d_ema_x_close_base_v145_signal,
    f067fcf_f067_fcf_inflection_selffund_126d_ema_x_close_base_v146_signal,
    f067fcf_f067_fcf_inflection_selffund_189d_ema_x_close_base_v147_signal,
    f067fcf_f067_fcf_inflection_selffund_252d_ema_x_close_base_v148_signal,
    f067fcf_f067_fcf_inflection_selffund_378d_ema_x_close_base_v149_signal,
    f067fcf_f067_fcf_inflection_selffund_504d_ema_x_close_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F067_FCF_INFLECTION_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f067_fcf_inflection_base_076_150_claude: {n_features} features pass")
