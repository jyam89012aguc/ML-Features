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
def _f22_small_base_growth(revenue, w):
    base = revenue.rolling(w, min_periods=max(1, w // 2)).min().replace(0, np.nan)
    return (revenue - base) / base.abs()


def _f22_production_acceleration(revenue, w):
    g1 = revenue.pct_change(periods=w)
    g2 = revenue.pct_change(periods=w).shift(w)
    return g1 - g2


def _f22_growth_quality(revenue, assets, w):
    g = revenue.pct_change(periods=w)
    a = assets.pct_change(periods=w)
    return g - a


def f22upg_f22_uranium_production_growth_smbg_504d_base_v076_signal(revenue, closeadj):
    result = _f22_small_base_growth(revenue, 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbg_504d_base_v077_signal(revenue, closeadj):
    result = _f22_small_base_growth(revenue, 504) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbg_504d_base_v078_signal(revenue, closeadj):
    result = _f22_small_base_growth(revenue, 504) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbg_504d_base_v079_signal(revenue, closeadj):
    result = _f22_small_base_growth(revenue, 504) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbg_504d_base_v080_signal(revenue, closeadj):
    result = _f22_small_base_growth(revenue, 504) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_5d_base_v081_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 5).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_5d_base_v082_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 5).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_5d_base_v083_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 5).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_5d_base_v084_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 5).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_5d_base_v085_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 5).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_5d_base_v086_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 5).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_5d_base_v087_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 5).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_5d_base_v088_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 5).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_10d_base_v089_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 10).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_10d_base_v090_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 10).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_10d_base_v091_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 10).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_10d_base_v092_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 10).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_10d_base_v093_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 10).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_10d_base_v094_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 10).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_10d_base_v095_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 10).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_10d_base_v096_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 10).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_21d_base_v097_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 21).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_21d_base_v098_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 21).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_21d_base_v099_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 21).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_21d_base_v100_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 21).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_21d_base_v101_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 21).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_21d_base_v102_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 21).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_21d_base_v103_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 21).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_21d_base_v104_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 21).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_42d_base_v105_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 42).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_42d_base_v106_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 42).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_42d_base_v107_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 42).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_42d_base_v108_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 42).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_42d_base_v109_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 42).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_42d_base_v110_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 42).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_42d_base_v111_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 42).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_42d_base_v112_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 42).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_63d_base_v113_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 63).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_63d_base_v114_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 63).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_63d_base_v115_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 63).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_63d_base_v116_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 63).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_63d_base_v117_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 63).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_63d_base_v118_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 63).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_63d_base_v119_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 63).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_63d_base_v120_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 63).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_126d_base_v121_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 126).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_126d_base_v122_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 126).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_126d_base_v123_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 126).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_126d_base_v124_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 126).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_126d_base_v125_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 126).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_126d_base_v126_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 126).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_126d_base_v127_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 126).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_126d_base_v128_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 126).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_189d_base_v129_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 189).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_189d_base_v130_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 189).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_189d_base_v131_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 189).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_189d_base_v132_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 189).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_189d_base_v133_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 189).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_189d_base_v134_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 189).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_189d_base_v135_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 189).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_189d_base_v136_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 189).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_252d_base_v137_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 252).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_252d_base_v138_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 252).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_252d_base_v139_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 252).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_252d_base_v140_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 252).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_252d_base_v141_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 252).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_252d_base_v142_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 252).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_252d_base_v143_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 252).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_252d_base_v144_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 252).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_378d_base_v145_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 378).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_378d_base_v146_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 378).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_378d_base_v147_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 378).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_378d_base_v148_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 378).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_378d_base_v149_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 378).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f22upg_f22_uranium_production_growth_smbglog_378d_base_v150_signal(revenue, closeadj):
    result = (np.log1p(_f22_small_base_growth(revenue, 378).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f22upg_f22_uranium_production_growth_smbg_504d_base_v076_signal,
    f22upg_f22_uranium_production_growth_smbg_504d_base_v077_signal,
    f22upg_f22_uranium_production_growth_smbg_504d_base_v078_signal,
    f22upg_f22_uranium_production_growth_smbg_504d_base_v079_signal,
    f22upg_f22_uranium_production_growth_smbg_504d_base_v080_signal,
    f22upg_f22_uranium_production_growth_smbglog_5d_base_v081_signal,
    f22upg_f22_uranium_production_growth_smbglog_5d_base_v082_signal,
    f22upg_f22_uranium_production_growth_smbglog_5d_base_v083_signal,
    f22upg_f22_uranium_production_growth_smbglog_5d_base_v084_signal,
    f22upg_f22_uranium_production_growth_smbglog_5d_base_v085_signal,
    f22upg_f22_uranium_production_growth_smbglog_5d_base_v086_signal,
    f22upg_f22_uranium_production_growth_smbglog_5d_base_v087_signal,
    f22upg_f22_uranium_production_growth_smbglog_5d_base_v088_signal,
    f22upg_f22_uranium_production_growth_smbglog_10d_base_v089_signal,
    f22upg_f22_uranium_production_growth_smbglog_10d_base_v090_signal,
    f22upg_f22_uranium_production_growth_smbglog_10d_base_v091_signal,
    f22upg_f22_uranium_production_growth_smbglog_10d_base_v092_signal,
    f22upg_f22_uranium_production_growth_smbglog_10d_base_v093_signal,
    f22upg_f22_uranium_production_growth_smbglog_10d_base_v094_signal,
    f22upg_f22_uranium_production_growth_smbglog_10d_base_v095_signal,
    f22upg_f22_uranium_production_growth_smbglog_10d_base_v096_signal,
    f22upg_f22_uranium_production_growth_smbglog_21d_base_v097_signal,
    f22upg_f22_uranium_production_growth_smbglog_21d_base_v098_signal,
    f22upg_f22_uranium_production_growth_smbglog_21d_base_v099_signal,
    f22upg_f22_uranium_production_growth_smbglog_21d_base_v100_signal,
    f22upg_f22_uranium_production_growth_smbglog_21d_base_v101_signal,
    f22upg_f22_uranium_production_growth_smbglog_21d_base_v102_signal,
    f22upg_f22_uranium_production_growth_smbglog_21d_base_v103_signal,
    f22upg_f22_uranium_production_growth_smbglog_21d_base_v104_signal,
    f22upg_f22_uranium_production_growth_smbglog_42d_base_v105_signal,
    f22upg_f22_uranium_production_growth_smbglog_42d_base_v106_signal,
    f22upg_f22_uranium_production_growth_smbglog_42d_base_v107_signal,
    f22upg_f22_uranium_production_growth_smbglog_42d_base_v108_signal,
    f22upg_f22_uranium_production_growth_smbglog_42d_base_v109_signal,
    f22upg_f22_uranium_production_growth_smbglog_42d_base_v110_signal,
    f22upg_f22_uranium_production_growth_smbglog_42d_base_v111_signal,
    f22upg_f22_uranium_production_growth_smbglog_42d_base_v112_signal,
    f22upg_f22_uranium_production_growth_smbglog_63d_base_v113_signal,
    f22upg_f22_uranium_production_growth_smbglog_63d_base_v114_signal,
    f22upg_f22_uranium_production_growth_smbglog_63d_base_v115_signal,
    f22upg_f22_uranium_production_growth_smbglog_63d_base_v116_signal,
    f22upg_f22_uranium_production_growth_smbglog_63d_base_v117_signal,
    f22upg_f22_uranium_production_growth_smbglog_63d_base_v118_signal,
    f22upg_f22_uranium_production_growth_smbglog_63d_base_v119_signal,
    f22upg_f22_uranium_production_growth_smbglog_63d_base_v120_signal,
    f22upg_f22_uranium_production_growth_smbglog_126d_base_v121_signal,
    f22upg_f22_uranium_production_growth_smbglog_126d_base_v122_signal,
    f22upg_f22_uranium_production_growth_smbglog_126d_base_v123_signal,
    f22upg_f22_uranium_production_growth_smbglog_126d_base_v124_signal,
    f22upg_f22_uranium_production_growth_smbglog_126d_base_v125_signal,
    f22upg_f22_uranium_production_growth_smbglog_126d_base_v126_signal,
    f22upg_f22_uranium_production_growth_smbglog_126d_base_v127_signal,
    f22upg_f22_uranium_production_growth_smbglog_126d_base_v128_signal,
    f22upg_f22_uranium_production_growth_smbglog_189d_base_v129_signal,
    f22upg_f22_uranium_production_growth_smbglog_189d_base_v130_signal,
    f22upg_f22_uranium_production_growth_smbglog_189d_base_v131_signal,
    f22upg_f22_uranium_production_growth_smbglog_189d_base_v132_signal,
    f22upg_f22_uranium_production_growth_smbglog_189d_base_v133_signal,
    f22upg_f22_uranium_production_growth_smbglog_189d_base_v134_signal,
    f22upg_f22_uranium_production_growth_smbglog_189d_base_v135_signal,
    f22upg_f22_uranium_production_growth_smbglog_189d_base_v136_signal,
    f22upg_f22_uranium_production_growth_smbglog_252d_base_v137_signal,
    f22upg_f22_uranium_production_growth_smbglog_252d_base_v138_signal,
    f22upg_f22_uranium_production_growth_smbglog_252d_base_v139_signal,
    f22upg_f22_uranium_production_growth_smbglog_252d_base_v140_signal,
    f22upg_f22_uranium_production_growth_smbglog_252d_base_v141_signal,
    f22upg_f22_uranium_production_growth_smbglog_252d_base_v142_signal,
    f22upg_f22_uranium_production_growth_smbglog_252d_base_v143_signal,
    f22upg_f22_uranium_production_growth_smbglog_252d_base_v144_signal,
    f22upg_f22_uranium_production_growth_smbglog_378d_base_v145_signal,
    f22upg_f22_uranium_production_growth_smbglog_378d_base_v146_signal,
    f22upg_f22_uranium_production_growth_smbglog_378d_base_v147_signal,
    f22upg_f22_uranium_production_growth_smbglog_378d_base_v148_signal,
    f22upg_f22_uranium_production_growth_smbglog_378d_base_v149_signal,
    f22upg_f22_uranium_production_growth_smbglog_378d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_URANIUM_PRODUCTION_GROWTH_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f22_small_base_growth', '_f22_production_acceleration', '_f22_growth_quality')
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
    print(f"OK f22_uranium_production_growth_base_076_150_claude: {n_features} features pass")
