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
def _f068_revenue_growth(revenue, w):
    return revenue.pct_change(periods=w)


def _f068_opex_growth(opex, w):
    return opex.pct_change(periods=w)


def _f068_operating_leverage(revenue, opex, w):
    # gap between revenue growth and opex growth — operating leverage
    rg = revenue.pct_change(periods=w)
    og = opex.pct_change(periods=w)
    return rg - og


# opexgrow_126d_x_meanclose base
def f068opl_f068_operating_leverage_opexgrow_126d_x_meanclose_base_v076_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 126)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_189d_x_meanclose base
def f068opl_f068_operating_leverage_opexgrow_189d_x_meanclose_base_v077_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 189)
    result = base * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_252d_x_meanclose base
def f068opl_f068_operating_leverage_opexgrow_252d_x_meanclose_base_v078_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_378d_x_meanclose base
def f068opl_f068_operating_leverage_opexgrow_378d_x_meanclose_base_v079_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 378)
    result = base * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_504d_x_meanclose base
def f068opl_f068_operating_leverage_opexgrow_504d_x_meanclose_base_v080_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 504)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_5d_x_meanclose base
def f068opl_f068_operating_leverage_oplev_5d_x_meanclose_base_v081_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 5)
    result = base * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_10d_x_meanclose base
def f068opl_f068_operating_leverage_oplev_10d_x_meanclose_base_v082_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 10)
    result = base * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_21d_x_meanclose base
def f068opl_f068_operating_leverage_oplev_21d_x_meanclose_base_v083_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_42d_x_meanclose base
def f068opl_f068_operating_leverage_oplev_42d_x_meanclose_base_v084_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 42)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_63d_x_meanclose base
def f068opl_f068_operating_leverage_oplev_63d_x_meanclose_base_v085_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_126d_x_meanclose base
def f068opl_f068_operating_leverage_oplev_126d_x_meanclose_base_v086_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 126)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_189d_x_meanclose base
def f068opl_f068_operating_leverage_oplev_189d_x_meanclose_base_v087_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 189)
    result = base * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_252d_x_meanclose base
def f068opl_f068_operating_leverage_oplev_252d_x_meanclose_base_v088_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_378d_x_meanclose base
def f068opl_f068_operating_leverage_oplev_378d_x_meanclose_base_v089_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 378)
    result = base * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_504d_x_meanclose base
def f068opl_f068_operating_leverage_oplev_504d_x_meanclose_base_v090_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 504)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_5d_x_closedif base
def f068opl_f068_operating_leverage_revgrow_5d_x_closedif_base_v091_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 5)
    result = base * closeadj.diff(1).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_10d_x_closedif base
def f068opl_f068_operating_leverage_revgrow_10d_x_closedif_base_v092_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 10)
    result = base * closeadj.diff(2).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_21d_x_closedif base
def f068opl_f068_operating_leverage_revgrow_21d_x_closedif_base_v093_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 21)
    result = base * closeadj.diff(5).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_42d_x_closedif base
def f068opl_f068_operating_leverage_revgrow_42d_x_closedif_base_v094_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 42)
    result = base * closeadj.diff(10).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_63d_x_closedif base
def f068opl_f068_operating_leverage_revgrow_63d_x_closedif_base_v095_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 63)
    result = base * closeadj.diff(15).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_126d_x_closedif base
def f068opl_f068_operating_leverage_revgrow_126d_x_closedif_base_v096_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 126)
    result = base * closeadj.diff(31).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_189d_x_closedif base
def f068opl_f068_operating_leverage_revgrow_189d_x_closedif_base_v097_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 189)
    result = base * closeadj.diff(47).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_252d_x_closedif base
def f068opl_f068_operating_leverage_revgrow_252d_x_closedif_base_v098_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 252)
    result = base * closeadj.diff(63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_378d_x_closedif base
def f068opl_f068_operating_leverage_revgrow_378d_x_closedif_base_v099_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 378)
    result = base * closeadj.diff(94).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_504d_x_closedif base
def f068opl_f068_operating_leverage_revgrow_504d_x_closedif_base_v100_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 504)
    result = base * closeadj.diff(126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_5d_x_closedif base
def f068opl_f068_operating_leverage_opexgrow_5d_x_closedif_base_v101_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 5)
    result = base * closeadj.diff(1).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_10d_x_closedif base
def f068opl_f068_operating_leverage_opexgrow_10d_x_closedif_base_v102_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 10)
    result = base * closeadj.diff(2).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_21d_x_closedif base
def f068opl_f068_operating_leverage_opexgrow_21d_x_closedif_base_v103_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 21)
    result = base * closeadj.diff(5).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_42d_x_closedif base
def f068opl_f068_operating_leverage_opexgrow_42d_x_closedif_base_v104_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 42)
    result = base * closeadj.diff(10).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_63d_x_closedif base
def f068opl_f068_operating_leverage_opexgrow_63d_x_closedif_base_v105_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 63)
    result = base * closeadj.diff(15).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_126d_x_closedif base
def f068opl_f068_operating_leverage_opexgrow_126d_x_closedif_base_v106_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 126)
    result = base * closeadj.diff(31).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_189d_x_closedif base
def f068opl_f068_operating_leverage_opexgrow_189d_x_closedif_base_v107_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 189)
    result = base * closeadj.diff(47).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_252d_x_closedif base
def f068opl_f068_operating_leverage_opexgrow_252d_x_closedif_base_v108_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 252)
    result = base * closeadj.diff(63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_378d_x_closedif base
def f068opl_f068_operating_leverage_opexgrow_378d_x_closedif_base_v109_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 378)
    result = base * closeadj.diff(94).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_504d_x_closedif base
def f068opl_f068_operating_leverage_opexgrow_504d_x_closedif_base_v110_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 504)
    result = base * closeadj.diff(126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_5d_x_closedif base
def f068opl_f068_operating_leverage_oplev_5d_x_closedif_base_v111_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 5)
    result = base * closeadj.diff(1).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_10d_x_closedif base
def f068opl_f068_operating_leverage_oplev_10d_x_closedif_base_v112_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 10)
    result = base * closeadj.diff(2).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_21d_x_closedif base
def f068opl_f068_operating_leverage_oplev_21d_x_closedif_base_v113_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 21)
    result = base * closeadj.diff(5).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_42d_x_closedif base
def f068opl_f068_operating_leverage_oplev_42d_x_closedif_base_v114_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 42)
    result = base * closeadj.diff(10).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_63d_x_closedif base
def f068opl_f068_operating_leverage_oplev_63d_x_closedif_base_v115_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 63)
    result = base * closeadj.diff(15).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_126d_x_closedif base
def f068opl_f068_operating_leverage_oplev_126d_x_closedif_base_v116_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 126)
    result = base * closeadj.diff(31).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_189d_x_closedif base
def f068opl_f068_operating_leverage_oplev_189d_x_closedif_base_v117_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 189)
    result = base * closeadj.diff(47).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_252d_x_closedif base
def f068opl_f068_operating_leverage_oplev_252d_x_closedif_base_v118_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 252)
    result = base * closeadj.diff(63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_378d_x_closedif base
def f068opl_f068_operating_leverage_oplev_378d_x_closedif_base_v119_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 378)
    result = base * closeadj.diff(94).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_504d_x_closedif base
def f068opl_f068_operating_leverage_oplev_504d_x_closedif_base_v120_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 504)
    result = base * closeadj.diff(126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_5d_ema_x_close base
def f068opl_f068_operating_leverage_revgrow_5d_ema_x_close_base_v121_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 5)
    result = _ema(base, 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_10d_ema_x_close base
def f068opl_f068_operating_leverage_revgrow_10d_ema_x_close_base_v122_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_21d_ema_x_close base
def f068opl_f068_operating_leverage_revgrow_21d_ema_x_close_base_v123_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 21)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_42d_ema_x_close base
def f068opl_f068_operating_leverage_revgrow_42d_ema_x_close_base_v124_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 42)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_63d_ema_x_close base
def f068opl_f068_operating_leverage_revgrow_63d_ema_x_close_base_v125_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 63)
    result = _ema(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_126d_ema_x_close base
def f068opl_f068_operating_leverage_revgrow_126d_ema_x_close_base_v126_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_189d_ema_x_close base
def f068opl_f068_operating_leverage_revgrow_189d_ema_x_close_base_v127_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 189)
    result = _ema(base, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_252d_ema_x_close base
def f068opl_f068_operating_leverage_revgrow_252d_ema_x_close_base_v128_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 252)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_378d_ema_x_close base
def f068opl_f068_operating_leverage_revgrow_378d_ema_x_close_base_v129_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 378)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revgrow_504d_ema_x_close base
def f068opl_f068_operating_leverage_revgrow_504d_ema_x_close_base_v130_signal(revenue, opex, closeadj):
    base = _f068_revenue_growth(revenue, 504)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_5d_ema_x_close base
def f068opl_f068_operating_leverage_opexgrow_5d_ema_x_close_base_v131_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 5)
    result = _ema(base, 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_10d_ema_x_close base
def f068opl_f068_operating_leverage_opexgrow_10d_ema_x_close_base_v132_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_21d_ema_x_close base
def f068opl_f068_operating_leverage_opexgrow_21d_ema_x_close_base_v133_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 21)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_42d_ema_x_close base
def f068opl_f068_operating_leverage_opexgrow_42d_ema_x_close_base_v134_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 42)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_63d_ema_x_close base
def f068opl_f068_operating_leverage_opexgrow_63d_ema_x_close_base_v135_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 63)
    result = _ema(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_126d_ema_x_close base
def f068opl_f068_operating_leverage_opexgrow_126d_ema_x_close_base_v136_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_189d_ema_x_close base
def f068opl_f068_operating_leverage_opexgrow_189d_ema_x_close_base_v137_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 189)
    result = _ema(base, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_252d_ema_x_close base
def f068opl_f068_operating_leverage_opexgrow_252d_ema_x_close_base_v138_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 252)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_378d_ema_x_close base
def f068opl_f068_operating_leverage_opexgrow_378d_ema_x_close_base_v139_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 378)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opexgrow_504d_ema_x_close base
def f068opl_f068_operating_leverage_opexgrow_504d_ema_x_close_base_v140_signal(revenue, opex, closeadj):
    base = _f068_opex_growth(opex, 504)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_5d_ema_x_close base
def f068opl_f068_operating_leverage_oplev_5d_ema_x_close_base_v141_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 5)
    result = _ema(base, 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_10d_ema_x_close base
def f068opl_f068_operating_leverage_oplev_10d_ema_x_close_base_v142_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_21d_ema_x_close base
def f068opl_f068_operating_leverage_oplev_21d_ema_x_close_base_v143_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 21)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_42d_ema_x_close base
def f068opl_f068_operating_leverage_oplev_42d_ema_x_close_base_v144_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 42)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_63d_ema_x_close base
def f068opl_f068_operating_leverage_oplev_63d_ema_x_close_base_v145_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 63)
    result = _ema(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_126d_ema_x_close base
def f068opl_f068_operating_leverage_oplev_126d_ema_x_close_base_v146_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_189d_ema_x_close base
def f068opl_f068_operating_leverage_oplev_189d_ema_x_close_base_v147_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 189)
    result = _ema(base, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_252d_ema_x_close base
def f068opl_f068_operating_leverage_oplev_252d_ema_x_close_base_v148_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 252)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_378d_ema_x_close base
def f068opl_f068_operating_leverage_oplev_378d_ema_x_close_base_v149_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 378)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# oplev_504d_ema_x_close base
def f068opl_f068_operating_leverage_oplev_504d_ema_x_close_base_v150_signal(revenue, opex, closeadj):
    base = _f068_operating_leverage(revenue, opex, 504)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f068opl_f068_operating_leverage_opexgrow_126d_x_meanclose_base_v076_signal,
    f068opl_f068_operating_leverage_opexgrow_189d_x_meanclose_base_v077_signal,
    f068opl_f068_operating_leverage_opexgrow_252d_x_meanclose_base_v078_signal,
    f068opl_f068_operating_leverage_opexgrow_378d_x_meanclose_base_v079_signal,
    f068opl_f068_operating_leverage_opexgrow_504d_x_meanclose_base_v080_signal,
    f068opl_f068_operating_leverage_oplev_5d_x_meanclose_base_v081_signal,
    f068opl_f068_operating_leverage_oplev_10d_x_meanclose_base_v082_signal,
    f068opl_f068_operating_leverage_oplev_21d_x_meanclose_base_v083_signal,
    f068opl_f068_operating_leverage_oplev_42d_x_meanclose_base_v084_signal,
    f068opl_f068_operating_leverage_oplev_63d_x_meanclose_base_v085_signal,
    f068opl_f068_operating_leverage_oplev_126d_x_meanclose_base_v086_signal,
    f068opl_f068_operating_leverage_oplev_189d_x_meanclose_base_v087_signal,
    f068opl_f068_operating_leverage_oplev_252d_x_meanclose_base_v088_signal,
    f068opl_f068_operating_leverage_oplev_378d_x_meanclose_base_v089_signal,
    f068opl_f068_operating_leverage_oplev_504d_x_meanclose_base_v090_signal,
    f068opl_f068_operating_leverage_revgrow_5d_x_closedif_base_v091_signal,
    f068opl_f068_operating_leverage_revgrow_10d_x_closedif_base_v092_signal,
    f068opl_f068_operating_leverage_revgrow_21d_x_closedif_base_v093_signal,
    f068opl_f068_operating_leverage_revgrow_42d_x_closedif_base_v094_signal,
    f068opl_f068_operating_leverage_revgrow_63d_x_closedif_base_v095_signal,
    f068opl_f068_operating_leverage_revgrow_126d_x_closedif_base_v096_signal,
    f068opl_f068_operating_leverage_revgrow_189d_x_closedif_base_v097_signal,
    f068opl_f068_operating_leverage_revgrow_252d_x_closedif_base_v098_signal,
    f068opl_f068_operating_leverage_revgrow_378d_x_closedif_base_v099_signal,
    f068opl_f068_operating_leverage_revgrow_504d_x_closedif_base_v100_signal,
    f068opl_f068_operating_leverage_opexgrow_5d_x_closedif_base_v101_signal,
    f068opl_f068_operating_leverage_opexgrow_10d_x_closedif_base_v102_signal,
    f068opl_f068_operating_leverage_opexgrow_21d_x_closedif_base_v103_signal,
    f068opl_f068_operating_leverage_opexgrow_42d_x_closedif_base_v104_signal,
    f068opl_f068_operating_leverage_opexgrow_63d_x_closedif_base_v105_signal,
    f068opl_f068_operating_leverage_opexgrow_126d_x_closedif_base_v106_signal,
    f068opl_f068_operating_leverage_opexgrow_189d_x_closedif_base_v107_signal,
    f068opl_f068_operating_leverage_opexgrow_252d_x_closedif_base_v108_signal,
    f068opl_f068_operating_leverage_opexgrow_378d_x_closedif_base_v109_signal,
    f068opl_f068_operating_leverage_opexgrow_504d_x_closedif_base_v110_signal,
    f068opl_f068_operating_leverage_oplev_5d_x_closedif_base_v111_signal,
    f068opl_f068_operating_leverage_oplev_10d_x_closedif_base_v112_signal,
    f068opl_f068_operating_leverage_oplev_21d_x_closedif_base_v113_signal,
    f068opl_f068_operating_leverage_oplev_42d_x_closedif_base_v114_signal,
    f068opl_f068_operating_leverage_oplev_63d_x_closedif_base_v115_signal,
    f068opl_f068_operating_leverage_oplev_126d_x_closedif_base_v116_signal,
    f068opl_f068_operating_leverage_oplev_189d_x_closedif_base_v117_signal,
    f068opl_f068_operating_leverage_oplev_252d_x_closedif_base_v118_signal,
    f068opl_f068_operating_leverage_oplev_378d_x_closedif_base_v119_signal,
    f068opl_f068_operating_leverage_oplev_504d_x_closedif_base_v120_signal,
    f068opl_f068_operating_leverage_revgrow_5d_ema_x_close_base_v121_signal,
    f068opl_f068_operating_leverage_revgrow_10d_ema_x_close_base_v122_signal,
    f068opl_f068_operating_leverage_revgrow_21d_ema_x_close_base_v123_signal,
    f068opl_f068_operating_leverage_revgrow_42d_ema_x_close_base_v124_signal,
    f068opl_f068_operating_leverage_revgrow_63d_ema_x_close_base_v125_signal,
    f068opl_f068_operating_leverage_revgrow_126d_ema_x_close_base_v126_signal,
    f068opl_f068_operating_leverage_revgrow_189d_ema_x_close_base_v127_signal,
    f068opl_f068_operating_leverage_revgrow_252d_ema_x_close_base_v128_signal,
    f068opl_f068_operating_leverage_revgrow_378d_ema_x_close_base_v129_signal,
    f068opl_f068_operating_leverage_revgrow_504d_ema_x_close_base_v130_signal,
    f068opl_f068_operating_leverage_opexgrow_5d_ema_x_close_base_v131_signal,
    f068opl_f068_operating_leverage_opexgrow_10d_ema_x_close_base_v132_signal,
    f068opl_f068_operating_leverage_opexgrow_21d_ema_x_close_base_v133_signal,
    f068opl_f068_operating_leverage_opexgrow_42d_ema_x_close_base_v134_signal,
    f068opl_f068_operating_leverage_opexgrow_63d_ema_x_close_base_v135_signal,
    f068opl_f068_operating_leverage_opexgrow_126d_ema_x_close_base_v136_signal,
    f068opl_f068_operating_leverage_opexgrow_189d_ema_x_close_base_v137_signal,
    f068opl_f068_operating_leverage_opexgrow_252d_ema_x_close_base_v138_signal,
    f068opl_f068_operating_leverage_opexgrow_378d_ema_x_close_base_v139_signal,
    f068opl_f068_operating_leverage_opexgrow_504d_ema_x_close_base_v140_signal,
    f068opl_f068_operating_leverage_oplev_5d_ema_x_close_base_v141_signal,
    f068opl_f068_operating_leverage_oplev_10d_ema_x_close_base_v142_signal,
    f068opl_f068_operating_leverage_oplev_21d_ema_x_close_base_v143_signal,
    f068opl_f068_operating_leverage_oplev_42d_ema_x_close_base_v144_signal,
    f068opl_f068_operating_leverage_oplev_63d_ema_x_close_base_v145_signal,
    f068opl_f068_operating_leverage_oplev_126d_ema_x_close_base_v146_signal,
    f068opl_f068_operating_leverage_oplev_189d_ema_x_close_base_v147_signal,
    f068opl_f068_operating_leverage_oplev_252d_ema_x_close_base_v148_signal,
    f068opl_f068_operating_leverage_oplev_378d_ema_x_close_base_v149_signal,
    f068opl_f068_operating_leverage_oplev_504d_ema_x_close_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F068_OPERATING_LEVERAGE_REGISTRY_076_150 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f068_operating_leverage_base_076_150_claude: {n_features} features pass")
