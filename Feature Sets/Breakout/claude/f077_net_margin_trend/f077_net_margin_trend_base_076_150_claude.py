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
def _f077_nm_slope(nm, w):
    return (nm - nm.shift(w)) / w

def _f077_nm_smoothed(nm, w):
    return nm.rolling(w, min_periods=max(1, w // 2)).mean()

def _f077_nm_trend_quality(nm, w):
    sm = nm.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = nm.rolling(w, min_periods=max(1, w // 2)).std()
    return (sm - sm.shift(w)) / sd.replace(0, np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v076_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (_z(prim, 21) * _z(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v077_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (_mean(prim, 21) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v078_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).max() - prim.rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v079_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (prim.shift(21) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v080_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (prim.cumsum().diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v081_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (prim.expanding(min_periods=21).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v082_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (prim.expanding(min_periods=21).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v083_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = ((prim - _mean(prim, 21)) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v084_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v085_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v086_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (_mean(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v087_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (_std(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v088_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (prim.ewm(halflife=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v089_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (prim.ewm(halflife=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v090_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).mean() - prim.rolling(21*2, min_periods=max(1, 21 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v091_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (_z(prim, 21*2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v092_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (np.tanh(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v093_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (np.tanh(prim) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v094_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (_mean(prim, 21*2) - _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v095_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (prim.diff(1).rolling(21, min_periods=max(1, 21 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v096_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).var()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v097_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (prim * _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v098_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (prim - prim.rolling(21, min_periods=max(1, 21 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v099_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (_mean(prim, 21).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_base_v100_signal(netmargin, closeadj):
    prim = _f077_nm_slope(netmargin, 21)
    result = (prim.fillna(0).cumsum() - prim.fillna(0).cumsum().shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v101_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (_z(prim, 21) * _z(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v102_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (_mean(prim, 21) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v103_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).max() - prim.rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v104_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (prim.shift(21) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v105_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (prim.cumsum().diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v106_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (prim.expanding(min_periods=21).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v107_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (prim.expanding(min_periods=21).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v108_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = ((prim - _mean(prim, 21)) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v109_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v110_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v111_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (_mean(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v112_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (_std(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v113_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (prim.ewm(halflife=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v114_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (prim.ewm(halflife=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v115_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).mean() - prim.rolling(21*2, min_periods=max(1, 21 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v116_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (_z(prim, 21*2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v117_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (np.tanh(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v118_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (np.tanh(prim) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v119_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (_mean(prim, 21*2) - _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v120_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (prim.diff(1).rolling(21, min_periods=max(1, 21 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v121_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).var()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v122_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (prim * _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v123_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (prim - prim.rolling(21, min_periods=max(1, 21 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v124_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (_mean(prim, 21).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v125_signal(netmargin, closeadj):
    prim = _f077_nm_smoothed(netmargin, 21)
    result = (prim.fillna(0).cumsum() - prim.fillna(0).cumsum().shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v126_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (_z(prim, 21) * _z(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v127_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (_mean(prim, 21) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v128_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).max() - prim.rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v129_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (prim.shift(21) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v130_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (prim.cumsum().diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v131_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (prim.expanding(min_periods=21).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v132_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (prim.expanding(min_periods=21).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v133_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = ((prim - _mean(prim, 21)) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v134_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v135_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v136_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (_mean(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v137_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (_std(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v138_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (prim.ewm(halflife=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v139_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (prim.ewm(halflife=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v140_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).mean() - prim.rolling(21*2, min_periods=max(1, 21 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v141_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (_z(prim, 21*2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v142_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (np.tanh(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v143_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (np.tanh(prim) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v144_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (_mean(prim, 21*2) - _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v145_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (prim.diff(1).rolling(21, min_periods=max(1, 21 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v146_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).var()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v147_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (prim * _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v148_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (prim - prim.rolling(21, min_periods=max(1, 21 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v149_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (_mean(prim, 21).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v150_signal(netmargin, closeadj):
    prim = _f077_nm_trend_quality(netmargin, 21)
    result = (prim.fillna(0).cumsum() - prim.fillna(0).cumsum().shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v076_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v077_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v078_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v079_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v080_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v081_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v082_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v083_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v084_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v085_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v086_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v087_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v088_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v089_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v090_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v091_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v092_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v093_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v094_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v095_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v096_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v097_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v098_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v099_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_base_v100_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v101_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v102_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v103_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v104_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v105_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v106_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v107_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v108_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v109_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v110_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v111_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v112_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v113_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v114_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v115_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v116_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v117_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v118_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v119_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v120_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v121_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v122_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v123_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v124_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_base_v125_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v126_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v127_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v128_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v129_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v130_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v131_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v132_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v133_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v134_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v135_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v136_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v137_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v138_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v139_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v140_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v141_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v142_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v143_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v144_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v145_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v146_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v147_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v148_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v149_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F077_NET_MARGIN_TREND_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    netmargin = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    cols = {"netmargin": netmargin, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f077_nm_slope", "_f077_nm_smoothed", "_f077_nm_trend_quality",)
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
    print(f"OK f077_net_margin_trend_base_076_150_claude: {n_features} features pass")
