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
def _f076_op_margin_change(em, w):
    return em - em.shift(w)

def _f076_op_inflection(em, w):
    d1 = em - em.shift(w)
    d2 = d1 - d1.shift(w)
    return d2

def _f076_profitability_turn(em, nm, w):
    em_ch = em - em.shift(w)
    nm_ch = nm - nm.shift(w)
    return em_ch + nm_ch


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v076_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (_z(prim, 21) * _z(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v077_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (_mean(prim, 21) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v078_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).max() - prim.rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v079_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (prim.shift(21) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v080_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (prim.cumsum().diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v081_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (prim.expanding(min_periods=21).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v082_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (prim.expanding(min_periods=21).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v083_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = ((prim - _mean(prim, 21)) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v084_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v085_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v086_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (_mean(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v087_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (_std(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v088_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (prim.ewm(halflife=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v089_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (prim.ewm(halflife=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v090_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).mean() - prim.rolling(21*2, min_periods=max(1, 21 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v091_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (_z(prim, 21*2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v092_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (np.tanh(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v093_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (np.tanh(prim) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v094_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (_mean(prim, 21*2) - _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v095_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (prim.diff(1).rolling(21, min_periods=max(1, 21 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v096_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).var()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v097_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (prim * _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v098_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (prim - prim.rolling(21, min_periods=max(1, 21 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v099_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (_mean(prim, 21).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v100_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_margin_change(ebitdamargin, 21)
    result = (prim.fillna(0).cumsum() - prim.fillna(0).cumsum().shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v101_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (_z(prim, 21) * _z(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v102_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (_mean(prim, 21) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v103_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).max() - prim.rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v104_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (prim.shift(21) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v105_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (prim.cumsum().diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v106_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (prim.expanding(min_periods=21).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v107_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (prim.expanding(min_periods=21).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v108_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = ((prim - _mean(prim, 21)) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v109_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v110_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v111_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (_mean(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v112_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (_std(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v113_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (prim.ewm(halflife=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v114_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (prim.ewm(halflife=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v115_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).mean() - prim.rolling(21*2, min_periods=max(1, 21 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v116_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (_z(prim, 21*2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v117_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (np.tanh(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v118_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (np.tanh(prim) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v119_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (_mean(prim, 21*2) - _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v120_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (prim.diff(1).rolling(21, min_periods=max(1, 21 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v121_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).var()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v122_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (prim * _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v123_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (prim - prim.rolling(21, min_periods=max(1, 21 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v124_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (_mean(prim, 21).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v125_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_op_inflection(ebitdamargin, 21)
    result = (prim.fillna(0).cumsum() - prim.fillna(0).cumsum().shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v126_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (_z(prim, 21) * _z(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v127_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (_mean(prim, 21) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v128_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).max() - prim.rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v129_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (prim.shift(21) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v130_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (prim.cumsum().diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v131_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (prim.expanding(min_periods=21).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v132_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (prim.expanding(min_periods=21).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v133_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = ((prim - _mean(prim, 21)) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v134_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v135_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v136_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (_mean(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v137_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (_std(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v138_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (prim.ewm(halflife=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v139_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (prim.ewm(halflife=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v140_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).mean() - prim.rolling(21*2, min_periods=max(1, 21 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v141_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (_z(prim, 21*2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v142_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (np.tanh(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v143_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (np.tanh(prim) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v144_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (_mean(prim, 21*2) - _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v145_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (prim.diff(1).rolling(21, min_periods=max(1, 21 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v146_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).var()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v147_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (prim * _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v148_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (prim - prim.rolling(21, min_periods=max(1, 21 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v149_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (_mean(prim, 21).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v150_signal(ebitdamargin, netmargin, closeadj):
    prim = _f076_profitability_turn(ebitdamargin, netmargin, 21)
    result = (prim.fillna(0).cumsum() - prim.fillna(0).cumsum().shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v076_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v077_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v078_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v079_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v080_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v081_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v082_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v083_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v084_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v085_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v086_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v087_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v088_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v089_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v090_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v091_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v092_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v093_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v094_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v095_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v096_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v097_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v098_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v099_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_base_v100_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v101_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v102_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v103_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v104_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v105_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v106_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v107_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v108_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v109_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v110_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v111_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v112_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v113_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v114_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v115_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v116_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v117_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v118_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v119_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v120_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v121_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v122_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v123_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v124_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_base_v125_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v126_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v127_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v128_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v129_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v130_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v131_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v132_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v133_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v134_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v135_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v136_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v137_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v138_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v139_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v140_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v141_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v142_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v143_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v144_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v145_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v146_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v147_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v148_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v149_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F076_OPERATING_MARGIN_INFLECTION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    cols = {"ebitdamargin": ebitdamargin, "netmargin": netmargin, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f076_op_margin_change", "_f076_op_inflection", "_f076_profitability_turn",)
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
    print(f"OK f076_operating_margin_inflection_base_076_150_claude: {n_features} features pass")
