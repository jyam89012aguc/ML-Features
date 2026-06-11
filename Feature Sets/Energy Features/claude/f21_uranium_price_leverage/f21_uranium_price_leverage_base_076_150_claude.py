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

# ===== folder domain primitives =====
def _f21_revenue_sensitivity(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / m.replace(0, np.nan)


def _f21_commodity_leverage(revenue, ebitdamargin, w):
    rev_chg = revenue.pct_change(periods=w)
    mar_chg = ebitdamargin.diff(periods=w)
    return rev_chg * (1.0 + mar_chg)


def _f21_price_leverage_score(revenue, w):
    z = (revenue - revenue.rolling(w, min_periods=max(1, w // 2)).mean()) /         revenue.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return z * revenue.pct_change(periods=max(1, w // 4))


def f21upl_f21_uranium_price_leverage_revsens_504d_base_v076_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_504d_base_v077_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 504) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_504d_base_v078_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 504) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_504d_base_v079_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 504) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsens_504d_base_v080_signal(revenue, closeadj):
    result = _f21_revenue_sensitivity(revenue, 504) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v081_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 5).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v082_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 5).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v083_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 5).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v084_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 5).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v085_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 5).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v086_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 5).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v087_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 5).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v088_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 5).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v089_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 10).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v090_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 10).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v091_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 10).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v092_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 10).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v093_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 10).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v094_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 10).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v095_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 10).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v096_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 10).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v097_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 21).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v098_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 21).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v099_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 21).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v100_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 21).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v101_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 21).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v102_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 21).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v103_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 21).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v104_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 21).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v105_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 42).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v106_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 42).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v107_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 42).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v108_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 42).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v109_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 42).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v110_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 42).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v111_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 42).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v112_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 42).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v113_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 63).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v114_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 63).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v115_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 63).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v116_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 63).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v117_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 63).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v118_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 63).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v119_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 63).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v120_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 63).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v121_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 126).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v122_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 126).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v123_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 126).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v124_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 126).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v125_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 126).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v126_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 126).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v127_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 126).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v128_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 126).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v129_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 189).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v130_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 189).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v131_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 189).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v132_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 189).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v133_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 189).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v134_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 189).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v135_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 189).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v136_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 189).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v137_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 252).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v138_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 252).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v139_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 252).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v140_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 252).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v141_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 252).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v142_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 252).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v143_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 252).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v144_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 252).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_378d_base_v145_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 378).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_378d_base_v146_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 378).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_378d_base_v147_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 378).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_378d_base_v148_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 378).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_378d_base_v149_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 378).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f21upl_f21_uranium_price_leverage_revsenslog_378d_base_v150_signal(revenue, closeadj):
    result = (np.log1p(_f21_revenue_sensitivity(revenue, 378).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f21upl_f21_uranium_price_leverage_revsens_504d_base_v076_signal,
    f21upl_f21_uranium_price_leverage_revsens_504d_base_v077_signal,
    f21upl_f21_uranium_price_leverage_revsens_504d_base_v078_signal,
    f21upl_f21_uranium_price_leverage_revsens_504d_base_v079_signal,
    f21upl_f21_uranium_price_leverage_revsens_504d_base_v080_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v081_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v082_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v083_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v084_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v085_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v086_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v087_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_5d_base_v088_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v089_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v090_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v091_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v092_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v093_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v094_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v095_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_10d_base_v096_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v097_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v098_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v099_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v100_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v101_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v102_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v103_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_21d_base_v104_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v105_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v106_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v107_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v108_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v109_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v110_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v111_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_42d_base_v112_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v113_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v114_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v115_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v116_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v117_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v118_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v119_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_63d_base_v120_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v121_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v122_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v123_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v124_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v125_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v126_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v127_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_126d_base_v128_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v129_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v130_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v131_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v132_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v133_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v134_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v135_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_189d_base_v136_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v137_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v138_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v139_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v140_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v141_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v142_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v143_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_252d_base_v144_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_378d_base_v145_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_378d_base_v146_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_378d_base_v147_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_378d_base_v148_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_378d_base_v149_signal,
    f21upl_f21_uranium_price_leverage_revsenslog_378d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_URANIUM_PRICE_LEVERAGE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    inventory = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "ebitda": ebitda,
        "capex": capex,
        "depamor": depamor,
        "cor": cor,
        "assets": assets,
        "inventory": inventory,
        "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f21_revenue_sensitivity', '_f21_commodity_leverage', '_f21_price_leverage_score')
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
    print(f"OK f21_uranium_price_leverage_base_076_150_claude: {n_features} features pass")
