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


# recent_126d_x_meanclose base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_x_meanclose_base_v076_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 126)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_189d_x_meanclose base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_x_meanclose_base_v077_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 189)
    result = base * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_252d_x_meanclose base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_x_meanclose_base_v078_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_378d_x_meanclose base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_x_meanclose_base_v079_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 378)
    result = base * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# recent_504d_x_meanclose base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_x_meanclose_base_v080_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 504)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_5d_x_meanclose base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_x_meanclose_base_v081_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 5)
    result = base * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_10d_x_meanclose base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_x_meanclose_base_v082_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 10)
    result = base * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_21d_x_meanclose base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_x_meanclose_base_v083_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_42d_x_meanclose base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_x_meanclose_base_v084_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 42)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_63d_x_meanclose base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_x_meanclose_base_v085_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_126d_x_meanclose base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_x_meanclose_base_v086_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 126)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_189d_x_meanclose base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_x_meanclose_base_v087_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 189)
    result = base * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_252d_x_meanclose base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_x_meanclose_base_v088_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_378d_x_meanclose base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_x_meanclose_base_v089_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 378)
    result = base * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_504d_x_meanclose base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_x_meanclose_base_v090_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 504)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_5d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_5d_x_closedif_base_v091_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 5)
    result = base * closeadj.diff(1).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_10d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_10d_x_closedif_base_v092_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 10)
    result = base * closeadj.diff(2).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_21d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_21d_x_closedif_base_v093_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 21)
    result = base * closeadj.diff(5).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_42d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_42d_x_closedif_base_v094_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 42)
    result = base * closeadj.diff(10).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_63d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_63d_x_closedif_base_v095_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 63)
    result = base * closeadj.diff(15).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_126d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_126d_x_closedif_base_v096_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 126)
    result = base * closeadj.diff(31).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_189d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_189d_x_closedif_base_v097_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 189)
    result = base * closeadj.diff(47).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_252d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_252d_x_closedif_base_v098_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 252)
    result = base * closeadj.diff(63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_378d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_378d_x_closedif_base_v099_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 378)
    result = base * closeadj.diff(94).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_504d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_504d_x_closedif_base_v100_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 504)
    result = base * closeadj.diff(126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# recent_5d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_5d_x_closedif_base_v101_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 5)
    result = base * closeadj.diff(1).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# recent_10d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_10d_x_closedif_base_v102_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 10)
    result = base * closeadj.diff(2).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# recent_21d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_21d_x_closedif_base_v103_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 21)
    result = base * closeadj.diff(5).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# recent_42d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_42d_x_closedif_base_v104_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 42)
    result = base * closeadj.diff(10).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# recent_63d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_63d_x_closedif_base_v105_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 63)
    result = base * closeadj.diff(15).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# recent_126d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_x_closedif_base_v106_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 126)
    result = base * closeadj.diff(31).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# recent_189d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_x_closedif_base_v107_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 189)
    result = base * closeadj.diff(47).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# recent_252d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_x_closedif_base_v108_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 252)
    result = base * closeadj.diff(63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# recent_378d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_x_closedif_base_v109_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 378)
    result = base * closeadj.diff(94).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# recent_504d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_x_closedif_base_v110_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 504)
    result = base * closeadj.diff(126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_5d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_x_closedif_base_v111_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 5)
    result = base * closeadj.diff(1).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_10d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_x_closedif_base_v112_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 10)
    result = base * closeadj.diff(2).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_21d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_x_closedif_base_v113_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 21)
    result = base * closeadj.diff(5).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_42d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_x_closedif_base_v114_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 42)
    result = base * closeadj.diff(10).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_63d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_x_closedif_base_v115_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 63)
    result = base * closeadj.diff(15).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_126d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_x_closedif_base_v116_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 126)
    result = base * closeadj.diff(31).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_189d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_x_closedif_base_v117_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 189)
    result = base * closeadj.diff(47).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_252d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_x_closedif_base_v118_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 252)
    result = base * closeadj.diff(63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_378d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_x_closedif_base_v119_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 378)
    result = base * closeadj.diff(94).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_504d_x_closedif base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_x_closedif_base_v120_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 504)
    result = base * closeadj.diff(126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_5d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_5d_ema_x_close_base_v121_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 5)
    result = _ema(base, 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_10d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_10d_ema_x_close_base_v122_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_21d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_21d_ema_x_close_base_v123_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 21)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_42d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_42d_ema_x_close_base_v124_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 42)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_63d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_63d_ema_x_close_base_v125_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 63)
    result = _ema(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_126d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_126d_ema_x_close_base_v126_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_189d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_189d_ema_x_close_base_v127_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 189)
    result = _ema(base, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_252d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_252d_ema_x_close_base_v128_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 252)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_378d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_378d_ema_x_close_base_v129_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 378)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# trailing_504d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_trailing_504d_ema_x_close_base_v130_signal(revenue, closeadj):
    base = _f066_trailing_growth(revenue, 504)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# recent_5d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_5d_ema_x_close_base_v131_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 5)
    result = _ema(base, 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# recent_10d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_10d_ema_x_close_base_v132_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# recent_21d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_21d_ema_x_close_base_v133_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 21)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# recent_42d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_42d_ema_x_close_base_v134_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 42)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# recent_63d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_63d_ema_x_close_base_v135_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 63)
    result = _ema(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# recent_126d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_ema_x_close_base_v136_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# recent_189d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_ema_x_close_base_v137_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 189)
    result = _ema(base, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# recent_252d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_ema_x_close_base_v138_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 252)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# recent_378d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_ema_x_close_base_v139_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 378)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# recent_504d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_ema_x_close_base_v140_signal(revenue, closeadj):
    base = _f066_recent_growth(revenue, 504)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_5d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_ema_x_close_base_v141_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 5)
    result = _ema(base, 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_10d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_ema_x_close_base_v142_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_21d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_ema_x_close_base_v143_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 21)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_42d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_ema_x_close_base_v144_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 42)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_63d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_ema_x_close_base_v145_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 63)
    result = _ema(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_126d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_ema_x_close_base_v146_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_189d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_ema_x_close_base_v147_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 189)
    result = _ema(base, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_252d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_ema_x_close_base_v148_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 252)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_378d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_ema_x_close_base_v149_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 378)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# surprise_504d_ema_x_close base
def f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_ema_x_close_base_v150_signal(revenue, closeadj):
    base = _f066_growth_surprise(revenue, 504)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_x_meanclose_base_v076_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_x_meanclose_base_v077_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_x_meanclose_base_v078_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_x_meanclose_base_v079_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_x_meanclose_base_v080_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_x_meanclose_base_v081_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_x_meanclose_base_v082_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_x_meanclose_base_v083_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_x_meanclose_base_v084_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_x_meanclose_base_v085_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_x_meanclose_base_v086_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_x_meanclose_base_v087_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_x_meanclose_base_v088_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_x_meanclose_base_v089_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_x_meanclose_base_v090_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_5d_x_closedif_base_v091_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_10d_x_closedif_base_v092_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_21d_x_closedif_base_v093_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_42d_x_closedif_base_v094_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_63d_x_closedif_base_v095_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_126d_x_closedif_base_v096_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_189d_x_closedif_base_v097_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_252d_x_closedif_base_v098_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_378d_x_closedif_base_v099_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_504d_x_closedif_base_v100_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_5d_x_closedif_base_v101_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_10d_x_closedif_base_v102_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_21d_x_closedif_base_v103_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_42d_x_closedif_base_v104_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_63d_x_closedif_base_v105_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_x_closedif_base_v106_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_x_closedif_base_v107_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_x_closedif_base_v108_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_x_closedif_base_v109_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_x_closedif_base_v110_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_x_closedif_base_v111_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_x_closedif_base_v112_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_x_closedif_base_v113_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_x_closedif_base_v114_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_x_closedif_base_v115_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_x_closedif_base_v116_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_x_closedif_base_v117_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_x_closedif_base_v118_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_x_closedif_base_v119_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_x_closedif_base_v120_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_5d_ema_x_close_base_v121_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_10d_ema_x_close_base_v122_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_21d_ema_x_close_base_v123_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_42d_ema_x_close_base_v124_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_63d_ema_x_close_base_v125_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_126d_ema_x_close_base_v126_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_189d_ema_x_close_base_v127_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_252d_ema_x_close_base_v128_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_378d_ema_x_close_base_v129_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_trailing_504d_ema_x_close_base_v130_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_5d_ema_x_close_base_v131_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_10d_ema_x_close_base_v132_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_21d_ema_x_close_base_v133_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_42d_ema_x_close_base_v134_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_63d_ema_x_close_base_v135_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_126d_ema_x_close_base_v136_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_189d_ema_x_close_base_v137_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_252d_ema_x_close_base_v138_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_378d_ema_x_close_base_v139_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_recent_504d_ema_x_close_base_v140_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_5d_ema_x_close_base_v141_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_10d_ema_x_close_base_v142_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_21d_ema_x_close_base_v143_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_42d_ema_x_close_base_v144_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_63d_ema_x_close_base_v145_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_126d_ema_x_close_base_v146_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_189d_ema_x_close_base_v147_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_252d_ema_x_close_base_v148_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_378d_ema_x_close_base_v149_signal,
    f066sgs_f066_sales_growth_surprise_vs_trend_surprise_504d_ema_x_close_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F066_SALES_GROWTH_SURPRISE_VS_TREND_REGISTRY_076_150 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f066_sales_growth_surprise_vs_trend_base_076_150_claude: {n_features} features pass")
