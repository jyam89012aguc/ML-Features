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


# gpaccel_126d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpaccel_126d_x_meanclose_base_v076_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 126)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_189d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpaccel_189d_x_meanclose_base_v077_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 189)
    result = base * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_252d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpaccel_252d_x_meanclose_base_v078_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_378d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpaccel_378d_x_meanclose_base_v079_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 378)
    result = base * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_504d_x_meanclose base
def f070gpg_f070_gross_profit_growth_gpaccel_504d_x_meanclose_base_v080_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 504)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_5d_x_meanclose base
def f070gpg_f070_gross_profit_growth_qualgrow_5d_x_meanclose_base_v081_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 5)
    result = base * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_10d_x_meanclose base
def f070gpg_f070_gross_profit_growth_qualgrow_10d_x_meanclose_base_v082_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 10)
    result = base * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_21d_x_meanclose base
def f070gpg_f070_gross_profit_growth_qualgrow_21d_x_meanclose_base_v083_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_42d_x_meanclose base
def f070gpg_f070_gross_profit_growth_qualgrow_42d_x_meanclose_base_v084_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 42)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_63d_x_meanclose base
def f070gpg_f070_gross_profit_growth_qualgrow_63d_x_meanclose_base_v085_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_126d_x_meanclose base
def f070gpg_f070_gross_profit_growth_qualgrow_126d_x_meanclose_base_v086_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 126)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_189d_x_meanclose base
def f070gpg_f070_gross_profit_growth_qualgrow_189d_x_meanclose_base_v087_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 189)
    result = base * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_252d_x_meanclose base
def f070gpg_f070_gross_profit_growth_qualgrow_252d_x_meanclose_base_v088_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_378d_x_meanclose base
def f070gpg_f070_gross_profit_growth_qualgrow_378d_x_meanclose_base_v089_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 378)
    result = base * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_504d_x_meanclose base
def f070gpg_f070_gross_profit_growth_qualgrow_504d_x_meanclose_base_v090_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 504)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_5d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpyoy_5d_x_closedif_base_v091_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 5)
    result = base * closeadj.diff(1).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_10d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpyoy_10d_x_closedif_base_v092_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 10)
    result = base * closeadj.diff(2).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_21d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpyoy_21d_x_closedif_base_v093_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 21)
    result = base * closeadj.diff(5).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_42d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpyoy_42d_x_closedif_base_v094_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 42)
    result = base * closeadj.diff(10).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_63d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpyoy_63d_x_closedif_base_v095_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 63)
    result = base * closeadj.diff(15).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_126d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpyoy_126d_x_closedif_base_v096_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 126)
    result = base * closeadj.diff(31).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_189d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpyoy_189d_x_closedif_base_v097_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 189)
    result = base * closeadj.diff(47).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_252d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpyoy_252d_x_closedif_base_v098_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 252)
    result = base * closeadj.diff(63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_378d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpyoy_378d_x_closedif_base_v099_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 378)
    result = base * closeadj.diff(94).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_504d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpyoy_504d_x_closedif_base_v100_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 504)
    result = base * closeadj.diff(126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_5d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpaccel_5d_x_closedif_base_v101_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 5)
    result = base * closeadj.diff(1).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_10d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpaccel_10d_x_closedif_base_v102_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 10)
    result = base * closeadj.diff(2).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_21d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpaccel_21d_x_closedif_base_v103_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 21)
    result = base * closeadj.diff(5).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_42d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpaccel_42d_x_closedif_base_v104_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 42)
    result = base * closeadj.diff(10).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_63d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpaccel_63d_x_closedif_base_v105_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 63)
    result = base * closeadj.diff(15).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_126d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpaccel_126d_x_closedif_base_v106_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 126)
    result = base * closeadj.diff(31).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_189d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpaccel_189d_x_closedif_base_v107_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 189)
    result = base * closeadj.diff(47).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_252d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpaccel_252d_x_closedif_base_v108_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 252)
    result = base * closeadj.diff(63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_378d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpaccel_378d_x_closedif_base_v109_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 378)
    result = base * closeadj.diff(94).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_504d_x_closedif base
def f070gpg_f070_gross_profit_growth_gpaccel_504d_x_closedif_base_v110_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 504)
    result = base * closeadj.diff(126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_5d_x_closedif base
def f070gpg_f070_gross_profit_growth_qualgrow_5d_x_closedif_base_v111_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 5)
    result = base * closeadj.diff(1).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_10d_x_closedif base
def f070gpg_f070_gross_profit_growth_qualgrow_10d_x_closedif_base_v112_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 10)
    result = base * closeadj.diff(2).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_21d_x_closedif base
def f070gpg_f070_gross_profit_growth_qualgrow_21d_x_closedif_base_v113_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 21)
    result = base * closeadj.diff(5).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_42d_x_closedif base
def f070gpg_f070_gross_profit_growth_qualgrow_42d_x_closedif_base_v114_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 42)
    result = base * closeadj.diff(10).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_63d_x_closedif base
def f070gpg_f070_gross_profit_growth_qualgrow_63d_x_closedif_base_v115_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 63)
    result = base * closeadj.diff(15).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_126d_x_closedif base
def f070gpg_f070_gross_profit_growth_qualgrow_126d_x_closedif_base_v116_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 126)
    result = base * closeadj.diff(31).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_189d_x_closedif base
def f070gpg_f070_gross_profit_growth_qualgrow_189d_x_closedif_base_v117_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 189)
    result = base * closeadj.diff(47).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_252d_x_closedif base
def f070gpg_f070_gross_profit_growth_qualgrow_252d_x_closedif_base_v118_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 252)
    result = base * closeadj.diff(63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_378d_x_closedif base
def f070gpg_f070_gross_profit_growth_qualgrow_378d_x_closedif_base_v119_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 378)
    result = base * closeadj.diff(94).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_504d_x_closedif base
def f070gpg_f070_gross_profit_growth_qualgrow_504d_x_closedif_base_v120_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 504)
    result = base * closeadj.diff(126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_5d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_5d_ema_x_close_base_v121_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 5)
    result = _ema(base, 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_10d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_10d_ema_x_close_base_v122_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_21d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_21d_ema_x_close_base_v123_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 21)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_42d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_42d_ema_x_close_base_v124_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 42)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_63d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_63d_ema_x_close_base_v125_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 63)
    result = _ema(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_126d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_126d_ema_x_close_base_v126_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_189d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_189d_ema_x_close_base_v127_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 189)
    result = _ema(base, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_252d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_252d_ema_x_close_base_v128_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 252)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_378d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_378d_ema_x_close_base_v129_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 378)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpyoy_504d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpyoy_504d_ema_x_close_base_v130_signal(gp, revenue, closeadj):
    base = _f070_gp_yoy(gp, 504)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_5d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_5d_ema_x_close_base_v131_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 5)
    result = _ema(base, 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_10d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_10d_ema_x_close_base_v132_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_21d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_21d_ema_x_close_base_v133_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 21)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_42d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_42d_ema_x_close_base_v134_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 42)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_63d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_63d_ema_x_close_base_v135_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 63)
    result = _ema(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_126d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_126d_ema_x_close_base_v136_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_189d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_189d_ema_x_close_base_v137_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 189)
    result = _ema(base, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_252d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_252d_ema_x_close_base_v138_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 252)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_378d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_378d_ema_x_close_base_v139_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 378)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gpaccel_504d_ema_x_close base
def f070gpg_f070_gross_profit_growth_gpaccel_504d_ema_x_close_base_v140_signal(gp, revenue, closeadj):
    base = _f070_gp_acceleration(gp, 504)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_5d_ema_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_5d_ema_x_close_base_v141_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 5)
    result = _ema(base, 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_10d_ema_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_10d_ema_x_close_base_v142_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_21d_ema_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_21d_ema_x_close_base_v143_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 21)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_42d_ema_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_42d_ema_x_close_base_v144_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 42)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_63d_ema_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_63d_ema_x_close_base_v145_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 63)
    result = _ema(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_126d_ema_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_126d_ema_x_close_base_v146_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_189d_ema_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_189d_ema_x_close_base_v147_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 189)
    result = _ema(base, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_252d_ema_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_252d_ema_x_close_base_v148_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 252)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_378d_ema_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_378d_ema_x_close_base_v149_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 378)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# qualgrow_504d_ema_x_close base
def f070gpg_f070_gross_profit_growth_qualgrow_504d_ema_x_close_base_v150_signal(gp, revenue, closeadj):
    base = _f070_quality_growth(gp, revenue, 504)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f070gpg_f070_gross_profit_growth_gpaccel_126d_x_meanclose_base_v076_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_189d_x_meanclose_base_v077_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_252d_x_meanclose_base_v078_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_378d_x_meanclose_base_v079_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_504d_x_meanclose_base_v080_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_5d_x_meanclose_base_v081_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_10d_x_meanclose_base_v082_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_21d_x_meanclose_base_v083_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_42d_x_meanclose_base_v084_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_63d_x_meanclose_base_v085_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_126d_x_meanclose_base_v086_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_189d_x_meanclose_base_v087_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_252d_x_meanclose_base_v088_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_378d_x_meanclose_base_v089_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_504d_x_meanclose_base_v090_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_5d_x_closedif_base_v091_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_10d_x_closedif_base_v092_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_21d_x_closedif_base_v093_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_42d_x_closedif_base_v094_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_63d_x_closedif_base_v095_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_126d_x_closedif_base_v096_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_189d_x_closedif_base_v097_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_252d_x_closedif_base_v098_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_378d_x_closedif_base_v099_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_504d_x_closedif_base_v100_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_5d_x_closedif_base_v101_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_10d_x_closedif_base_v102_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_21d_x_closedif_base_v103_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_42d_x_closedif_base_v104_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_63d_x_closedif_base_v105_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_126d_x_closedif_base_v106_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_189d_x_closedif_base_v107_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_252d_x_closedif_base_v108_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_378d_x_closedif_base_v109_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_504d_x_closedif_base_v110_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_5d_x_closedif_base_v111_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_10d_x_closedif_base_v112_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_21d_x_closedif_base_v113_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_42d_x_closedif_base_v114_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_63d_x_closedif_base_v115_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_126d_x_closedif_base_v116_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_189d_x_closedif_base_v117_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_252d_x_closedif_base_v118_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_378d_x_closedif_base_v119_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_504d_x_closedif_base_v120_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_5d_ema_x_close_base_v121_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_10d_ema_x_close_base_v122_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_21d_ema_x_close_base_v123_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_42d_ema_x_close_base_v124_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_63d_ema_x_close_base_v125_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_126d_ema_x_close_base_v126_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_189d_ema_x_close_base_v127_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_252d_ema_x_close_base_v128_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_378d_ema_x_close_base_v129_signal,
    f070gpg_f070_gross_profit_growth_gpyoy_504d_ema_x_close_base_v130_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_5d_ema_x_close_base_v131_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_10d_ema_x_close_base_v132_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_21d_ema_x_close_base_v133_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_42d_ema_x_close_base_v134_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_63d_ema_x_close_base_v135_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_126d_ema_x_close_base_v136_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_189d_ema_x_close_base_v137_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_252d_ema_x_close_base_v138_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_378d_ema_x_close_base_v139_signal,
    f070gpg_f070_gross_profit_growth_gpaccel_504d_ema_x_close_base_v140_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_5d_ema_x_close_base_v141_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_10d_ema_x_close_base_v142_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_21d_ema_x_close_base_v143_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_42d_ema_x_close_base_v144_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_63d_ema_x_close_base_v145_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_126d_ema_x_close_base_v146_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_189d_ema_x_close_base_v147_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_252d_ema_x_close_base_v148_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_378d_ema_x_close_base_v149_signal,
    f070gpg_f070_gross_profit_growth_qualgrow_504d_ema_x_close_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F070_GROSS_PROFIT_GROWTH_REGISTRY_076_150 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f070_gross_profit_growth_base_076_150_claude: {n_features} features pass")
