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
def _f25_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan).abs()


def _f25_capex_cycle(capex, assets, w):
    ratio = capex / assets.replace(0, np.nan).abs()
    m = ratio.rolling(w, min_periods=max(1, w // 2)).mean()
    return ratio - m


def _f25_capex_quality(capex, depamor, w):
    return (capex / depamor.replace(0, np.nan).abs()).rolling(w, min_periods=max(1, w // 2)).mean()


def f25ncc_f25_nuclear_capex_cycle_capintz_252d_base_v076_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_252d_base_v077_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 252) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_252d_base_v078_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 252) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_252d_base_v079_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 252) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_252d_base_v080_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 252) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v081_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v082_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 378) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v083_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v084_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v085_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 378) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v086_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 378) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v087_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 378) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v088_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 378) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v089_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v090_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 504) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v091_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v092_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v093_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 504) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v094_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 504) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v095_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 504) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v096_signal(capex, revenue, closeadj):
    result = _z(_f25_capex_intensity(capex, revenue), 504) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v097_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v098_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v099_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v100_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v101_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 5) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v102_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 5) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v103_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 5) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v104_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 5) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v105_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v106_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 10) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v107_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v108_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v109_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 10) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v110_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 10) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v111_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 10) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v112_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 10) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v113_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v114_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v115_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v116_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v117_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v118_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v119_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v120_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 21) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v121_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v122_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v123_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v124_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v125_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 42) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v126_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 42) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v127_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 42) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v128_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 42) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v129_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v130_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v131_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v132_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v133_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 63) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v134_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 63) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v135_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 63) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v136_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 63) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v137_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v138_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v139_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v140_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v141_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 126) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v142_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 126) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v143_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 126) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v144_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 126) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_189d_base_v145_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_189d_base_v146_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 189) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_189d_base_v147_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_189d_base_v148_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_189d_base_v149_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 189) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f25ncc_f25_nuclear_capex_cycle_capintmean_189d_base_v150_signal(capex, revenue, closeadj):
    result = _mean(_f25_capex_intensity(capex, revenue), 189) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f25ncc_f25_nuclear_capex_cycle_capintz_252d_base_v076_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_252d_base_v077_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_252d_base_v078_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_252d_base_v079_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_252d_base_v080_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v081_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v082_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v083_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v084_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v085_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v086_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v087_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_378d_base_v088_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v089_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v090_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v091_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v092_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v093_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v094_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v095_signal,
    f25ncc_f25_nuclear_capex_cycle_capintz_504d_base_v096_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v097_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v098_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v099_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v100_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v101_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v102_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v103_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_5d_base_v104_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v105_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v106_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v107_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v108_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v109_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v110_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v111_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_10d_base_v112_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v113_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v114_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v115_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v116_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v117_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v118_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v119_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_21d_base_v120_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v121_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v122_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v123_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v124_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v125_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v126_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v127_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_42d_base_v128_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v129_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v130_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v131_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v132_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v133_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v134_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v135_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_63d_base_v136_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v137_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v138_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v139_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v140_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v141_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v142_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v143_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_126d_base_v144_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_189d_base_v145_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_189d_base_v146_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_189d_base_v147_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_189d_base_v148_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_189d_base_v149_signal,
    f25ncc_f25_nuclear_capex_cycle_capintmean_189d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_NUCLEAR_CAPEX_CYCLE_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f25_capex_intensity', '_f25_capex_cycle', '_f25_capex_quality')
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
    print(f"OK f25_nuclear_capex_cycle_base_076_150_claude: {n_features} features pass")
