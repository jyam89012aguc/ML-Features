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
def _f080_delta_revenue(rv, w):
    return rv - rv.shift(w)

def _f080_delta_op_inc(eb, w):
    return eb - eb.shift(w)

def _f080_incremental_margin(eb, rv, w):
    deb = eb - eb.shift(w)
    drv = rv - rv.shift(w)
    return deb / drv.replace(0, np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v076_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (_z(prim, 21) * _z(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v077_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (_mean(prim, 21) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v078_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).max() - prim.rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v079_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (prim.shift(21) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v080_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (prim.cumsum().diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v081_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (prim.expanding(min_periods=21).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v082_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (prim.expanding(min_periods=21).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v083_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = ((prim - _mean(prim, 21)) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v084_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v085_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v086_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (_mean(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v087_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (_std(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v088_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (prim.ewm(halflife=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v089_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (prim.ewm(halflife=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v090_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).mean() - prim.rolling(21*2, min_periods=max(1, 21 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v091_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (_z(prim, 21*2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v092_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (np.tanh(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v093_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (np.tanh(prim) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v094_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (_mean(prim, 21*2) - _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v095_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (prim.diff(1).rolling(21, min_periods=max(1, 21 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v096_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).var()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v097_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (prim * _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v098_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (prim - prim.rolling(21, min_periods=max(1, 21 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v099_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (_mean(prim, 21).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_base_v100_signal(ebit, revenue, closeadj):
    prim = _f080_delta_revenue(revenue, 21)
    result = (prim.fillna(0).cumsum() - prim.fillna(0).cumsum().shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v101_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (_z(prim, 21) * _z(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v102_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (_mean(prim, 21) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v103_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).max() - prim.rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v104_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (prim.shift(21) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v105_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (prim.cumsum().diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v106_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (prim.expanding(min_periods=21).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v107_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (prim.expanding(min_periods=21).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v108_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = ((prim - _mean(prim, 21)) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v109_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v110_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v111_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (_mean(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v112_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (_std(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v113_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (prim.ewm(halflife=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v114_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (prim.ewm(halflife=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v115_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).mean() - prim.rolling(21*2, min_periods=max(1, 21 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v116_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (_z(prim, 21*2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v117_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (np.tanh(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v118_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (np.tanh(prim) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v119_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (_mean(prim, 21*2) - _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v120_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (prim.diff(1).rolling(21, min_periods=max(1, 21 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v121_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).var()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v122_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (prim * _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v123_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (prim - prim.rolling(21, min_periods=max(1, 21 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v124_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (_mean(prim, 21).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_base_v125_signal(ebit, revenue, closeadj):
    prim = _f080_delta_op_inc(ebit, 21)
    result = (prim.fillna(0).cumsum() - prim.fillna(0).cumsum().shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v126_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (_z(prim, 21) * _z(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v127_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (_mean(prim, 21) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v128_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).max() - prim.rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v129_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (prim.shift(21) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v130_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (prim.cumsum().diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v131_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (prim.expanding(min_periods=21).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v132_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (prim.expanding(min_periods=21).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v133_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = ((prim - _mean(prim, 21)) * _std(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v134_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v135_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v136_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (_mean(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v137_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (_std(prim.abs(), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v138_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (prim.ewm(halflife=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v139_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (prim.ewm(halflife=21, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v140_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).mean() - prim.rolling(21*2, min_periods=max(1, 21 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v141_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (_z(prim, 21*2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v142_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (np.tanh(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v143_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (np.tanh(prim) * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v144_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (_mean(prim, 21*2) - _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v145_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (prim.diff(1).rolling(21, min_periods=max(1, 21 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v146_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (prim.rolling(21, min_periods=max(1, 21 // 2)).var()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v147_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (prim * _mean(prim, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v148_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (prim - prim.rolling(21, min_periods=max(1, 21 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v149_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (_mean(prim, 21).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_base_v150_signal(ebit, revenue, closeadj):
    prim = _f080_incremental_margin(ebit, revenue, 21)
    result = (prim.fillna(0).cumsum() - prim.fillna(0).cumsum().shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v076_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v077_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v078_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v079_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v080_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v081_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v082_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v083_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v084_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v085_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v086_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v087_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v088_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v089_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v090_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v091_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v092_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v093_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v094_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v095_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v096_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v097_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v098_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v099_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_base_v100_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v101_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v102_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v103_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v104_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v105_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v106_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v107_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v108_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v109_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v110_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v111_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v112_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v113_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v114_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v115_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v116_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v117_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v118_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v119_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v120_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v121_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v122_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v123_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v124_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_base_v125_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v126_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v127_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v128_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v129_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v130_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v131_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v132_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v133_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v134_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v135_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v136_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v137_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v138_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v139_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v140_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v141_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v142_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v143_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v144_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v145_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v146_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v147_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v148_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v149_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F080_INCREMENTAL_MARGIN_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    cols = {"ebit": ebit, "revenue": revenue, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f080_delta_revenue", "_f080_delta_op_inc", "_f080_incremental_margin",)
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
    print(f"OK f080_incremental_margin_base_076_150_claude: {n_features} features pass")
