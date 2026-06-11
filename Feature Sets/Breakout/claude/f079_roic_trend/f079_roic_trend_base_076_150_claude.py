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
def _f079_roic_slope(r, w):
    return (r - r.shift(w)) / w

def _f079_roic_improvement(r, w):
    sm = r.rolling(w, min_periods=max(1, w // 2)).mean()
    return sm - sm.shift(w)

def _f079_value_creation(r, w):
    sm = r.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = r.rolling(w, min_periods=max(1, w // 2)).std()
    return (r - sm) / sd.replace(0, np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v076_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (_z(prim, 21) * _z(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v077_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (_mean(prim, 21) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v078_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).max() - prim.rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v079_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (prim.shift(21) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v080_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (prim.cumsum().diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v081_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (prim.expanding(min_periods=21).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v082_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (prim.expanding(min_periods=21).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v083_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = ((prim - _mean(prim, 21)) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v084_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v085_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v086_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (_mean(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v087_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (_std(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v088_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (prim.ewm(halflife=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v089_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (prim.ewm(halflife=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v090_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).mean() - prim.rolling(21*2, min_periods=max(1, 21 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v091_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (_z(prim, 21*2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v092_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (np.tanh(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v093_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (np.tanh(prim) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v094_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (_mean(prim, 21*2) - _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v095_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (prim.diff(1).rolling(21, min_periods=max(1, 21 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v096_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).var()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v097_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (prim * _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v098_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (prim - prim.rolling(21, min_periods=max(1, 21 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v099_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (_mean(prim, 21).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_base_v100_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 21)
    result = (prim.fillna(0).cumsum() - prim.fillna(0).cumsum().shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v101_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (_z(prim, 21) * _z(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v102_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (_mean(prim, 21) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v103_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).max() - prim.rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v104_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (prim.shift(21) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v105_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (prim.cumsum().diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v106_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (prim.expanding(min_periods=21).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v107_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (prim.expanding(min_periods=21).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v108_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = ((prim - _mean(prim, 21)) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v109_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v110_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v111_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (_mean(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v112_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (_std(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v113_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (prim.ewm(halflife=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v114_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (prim.ewm(halflife=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v115_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).mean() - prim.rolling(21*2, min_periods=max(1, 21 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v116_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (_z(prim, 21*2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v117_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (np.tanh(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v118_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (np.tanh(prim) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v119_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (_mean(prim, 21*2) - _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v120_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (prim.diff(1).rolling(21, min_periods=max(1, 21 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v121_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).var()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v122_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (prim * _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v123_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (prim - prim.rolling(21, min_periods=max(1, 21 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v124_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (_mean(prim, 21).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_base_v125_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 21)
    result = (prim.fillna(0).cumsum() - prim.fillna(0).cumsum().shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v126_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (_z(prim, 21) * _z(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v127_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (_mean(prim, 21) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v128_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).max() - prim.rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v129_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (prim.shift(21) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v130_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (prim.cumsum().diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v131_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (prim.expanding(min_periods=21).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v132_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (prim.expanding(min_periods=21).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v133_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = ((prim - _mean(prim, 21)) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v134_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v135_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v136_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (_mean(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v137_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (_std(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v138_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (prim.ewm(halflife=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v139_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (prim.ewm(halflife=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v140_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).mean() - prim.rolling(21*2, min_periods=max(1, 21 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v141_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (_z(prim, 21*2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v142_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (np.tanh(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v143_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (np.tanh(prim) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v144_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (_mean(prim, 21*2) - _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v145_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (prim.diff(1).rolling(21, min_periods=max(1, 21 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v146_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).var()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v147_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (prim * _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v148_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (prim - prim.rolling(21, min_periods=max(1, 21 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v149_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (_mean(prim, 21).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_base_v150_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 21)
    result = (prim.fillna(0).cumsum() - prim.fillna(0).cumsum().shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f079rct_f079_roic_trend_roic_slope_21d_base_v076_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v077_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v078_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v079_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v080_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v081_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v082_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v083_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v084_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v085_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v086_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v087_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v088_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v089_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v090_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v091_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v092_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v093_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v094_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v095_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v096_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v097_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v098_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v099_signal,
    f079rct_f079_roic_trend_roic_slope_21d_base_v100_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v101_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v102_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v103_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v104_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v105_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v106_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v107_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v108_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v109_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v110_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v111_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v112_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v113_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v114_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v115_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v116_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v117_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v118_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v119_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v120_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v121_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v122_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v123_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v124_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_base_v125_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v126_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v127_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v128_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v129_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v130_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v131_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v132_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v133_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v134_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v135_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v136_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v137_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v138_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v139_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v140_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v141_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v142_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v143_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v144_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v145_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v146_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v147_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v148_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v149_signal,
    f079rct_f079_roic_trend_value_creation_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F079_ROIC_TREND_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    cols = {"roic": roic, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f079_roic_slope", "_f079_roic_improvement", "_f079_value_creation",)
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
    print(f"OK f079_roic_trend_base_076_150_claude: {n_features} features pass")
