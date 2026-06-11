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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f73gs_int_assets(intang, assets):
    return intang / assets.replace(0, np.nan)


def _f73gs_int_equity(intang, equity):
    return intang / equity.replace(0, np.nan)


def _f73gs_int_tangibles(intang, tangibles):
    return intang / tangibles.replace(0, np.nan)


def _f73gs_int_revenue(intang, revenue):
    return intang / revenue.replace(0, np.nan)


def _f73gs_align(q, idx):
    return q.reindex(idx).ffill()


# 252d max of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_max_252d_base_v076_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _max(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of intassets
def f73gs_f73_semi_goodwill_share_intassets_max_504d_base_v077_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _max(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of intequity
def f73gs_f73_semi_goodwill_share_intequity_max_504d_base_v078_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _max(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_max_504d_base_v079_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _max(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_max_504d_base_v080_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _max(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of intassets
def f73gs_f73_semi_goodwill_share_intassets_min_21d_base_v081_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of intequity
def f73gs_f73_semi_goodwill_share_intequity_min_21d_base_v082_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_min_21d_base_v083_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_min_21d_base_v084_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of intassets
def f73gs_f73_semi_goodwill_share_intassets_min_63d_base_v085_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of intequity
def f73gs_f73_semi_goodwill_share_intequity_min_63d_base_v086_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_min_63d_base_v087_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_min_63d_base_v088_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of intassets
def f73gs_f73_semi_goodwill_share_intassets_min_126d_base_v089_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of intequity
def f73gs_f73_semi_goodwill_share_intequity_min_126d_base_v090_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_min_126d_base_v091_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_min_126d_base_v092_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of intassets
def f73gs_f73_semi_goodwill_share_intassets_min_252d_base_v093_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of intequity
def f73gs_f73_semi_goodwill_share_intequity_min_252d_base_v094_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_min_252d_base_v095_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_min_252d_base_v096_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of intassets
def f73gs_f73_semi_goodwill_share_intassets_min_504d_base_v097_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of intequity
def f73gs_f73_semi_goodwill_share_intequity_min_504d_base_v098_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_min_504d_base_v099_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_min_504d_base_v100_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range (max-min) of intassets
def f73gs_f73_semi_goodwill_share_intassets_rng_21d_base_v101_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _max(m, 21) - _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range (max-min) of intequity
def f73gs_f73_semi_goodwill_share_intequity_rng_21d_base_v102_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _max(m, 21) - _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range (max-min) of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_rng_21d_base_v103_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _max(m, 21) - _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range (max-min) of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_rng_21d_base_v104_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _max(m, 21) - _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range (max-min) of intassets
def f73gs_f73_semi_goodwill_share_intassets_rng_63d_base_v105_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _max(m, 63) - _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range (max-min) of intequity
def f73gs_f73_semi_goodwill_share_intequity_rng_63d_base_v106_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _max(m, 63) - _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range (max-min) of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_rng_63d_base_v107_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _max(m, 63) - _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range (max-min) of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_rng_63d_base_v108_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _max(m, 63) - _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range (max-min) of intassets
def f73gs_f73_semi_goodwill_share_intassets_rng_126d_base_v109_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _max(m, 126) - _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range (max-min) of intequity
def f73gs_f73_semi_goodwill_share_intequity_rng_126d_base_v110_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _max(m, 126) - _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range (max-min) of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_rng_126d_base_v111_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _max(m, 126) - _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range (max-min) of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_rng_126d_base_v112_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _max(m, 126) - _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range (max-min) of intassets
def f73gs_f73_semi_goodwill_share_intassets_rng_252d_base_v113_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _max(m, 252) - _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range (max-min) of intequity
def f73gs_f73_semi_goodwill_share_intequity_rng_252d_base_v114_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _max(m, 252) - _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range (max-min) of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_rng_252d_base_v115_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _max(m, 252) - _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range (max-min) of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_rng_252d_base_v116_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _max(m, 252) - _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range (max-min) of intassets
def f73gs_f73_semi_goodwill_share_intassets_rng_504d_base_v117_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _max(m, 504) - _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range (max-min) of intequity
def f73gs_f73_semi_goodwill_share_intequity_rng_504d_base_v118_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _max(m, 504) - _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range (max-min) of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_rng_504d_base_v119_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _max(m, 504) - _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range (max-min) of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_rng_504d_base_v120_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _max(m, 504) - _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position in rolling range of intassets
def f73gs_f73_semi_goodwill_share_intassets_pos_21d_base_v121_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    lo = _min(m, 21)
    hi = _max(m, 21)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position in rolling range of intequity
def f73gs_f73_semi_goodwill_share_intequity_pos_21d_base_v122_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    lo = _min(m, 21)
    hi = _max(m, 21)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position in rolling range of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_pos_21d_base_v123_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    lo = _min(m, 21)
    hi = _max(m, 21)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position in rolling range of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_pos_21d_base_v124_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    lo = _min(m, 21)
    hi = _max(m, 21)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position in rolling range of intassets
def f73gs_f73_semi_goodwill_share_intassets_pos_63d_base_v125_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    lo = _min(m, 63)
    hi = _max(m, 63)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position in rolling range of intequity
def f73gs_f73_semi_goodwill_share_intequity_pos_63d_base_v126_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    lo = _min(m, 63)
    hi = _max(m, 63)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position in rolling range of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_pos_63d_base_v127_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    lo = _min(m, 63)
    hi = _max(m, 63)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position in rolling range of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_pos_63d_base_v128_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    lo = _min(m, 63)
    hi = _max(m, 63)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position in rolling range of intassets
def f73gs_f73_semi_goodwill_share_intassets_pos_126d_base_v129_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    lo = _min(m, 126)
    hi = _max(m, 126)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position in rolling range of intequity
def f73gs_f73_semi_goodwill_share_intequity_pos_126d_base_v130_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    lo = _min(m, 126)
    hi = _max(m, 126)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position in rolling range of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_pos_126d_base_v131_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    lo = _min(m, 126)
    hi = _max(m, 126)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position in rolling range of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_pos_126d_base_v132_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    lo = _min(m, 126)
    hi = _max(m, 126)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position in rolling range of intassets
def f73gs_f73_semi_goodwill_share_intassets_pos_252d_base_v133_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    lo = _min(m, 252)
    hi = _max(m, 252)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position in rolling range of intequity
def f73gs_f73_semi_goodwill_share_intequity_pos_252d_base_v134_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    lo = _min(m, 252)
    hi = _max(m, 252)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position in rolling range of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_pos_252d_base_v135_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    lo = _min(m, 252)
    hi = _max(m, 252)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position in rolling range of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_pos_252d_base_v136_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    lo = _min(m, 252)
    hi = _max(m, 252)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position in rolling range of intassets
def f73gs_f73_semi_goodwill_share_intassets_pos_504d_base_v137_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    lo = _min(m, 504)
    hi = _max(m, 504)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position in rolling range of intequity
def f73gs_f73_semi_goodwill_share_intequity_pos_504d_base_v138_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    lo = _min(m, 504)
    hi = _max(m, 504)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position in rolling range of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_pos_504d_base_v139_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    lo = _min(m, 504)
    hi = _max(m, 504)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position in rolling range of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_pos_504d_base_v140_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    lo = _min(m, 504)
    hi = _max(m, 504)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of intassets from rolling peak
def f73gs_f73_semi_goodwill_share_intassets_dd_21d_base_v141_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    peak = _max(m, 21)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of intequity from rolling peak
def f73gs_f73_semi_goodwill_share_intequity_dd_21d_base_v142_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    peak = _max(m, 21)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of inttangibles from rolling peak
def f73gs_f73_semi_goodwill_share_inttangibles_dd_21d_base_v143_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    peak = _max(m, 21)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of intrevenue from rolling peak
def f73gs_f73_semi_goodwill_share_intrevenue_dd_21d_base_v144_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    peak = _max(m, 21)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of intassets from rolling peak
def f73gs_f73_semi_goodwill_share_intassets_dd_63d_base_v145_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    peak = _max(m, 63)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of intequity from rolling peak
def f73gs_f73_semi_goodwill_share_intequity_dd_63d_base_v146_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    peak = _max(m, 63)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of inttangibles from rolling peak
def f73gs_f73_semi_goodwill_share_inttangibles_dd_63d_base_v147_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    peak = _max(m, 63)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of intrevenue from rolling peak
def f73gs_f73_semi_goodwill_share_intrevenue_dd_63d_base_v148_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    peak = _max(m, 63)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of intassets from rolling peak
def f73gs_f73_semi_goodwill_share_intassets_dd_126d_base_v149_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    peak = _max(m, 126)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of intequity from rolling peak
def f73gs_f73_semi_goodwill_share_intequity_dd_126d_base_v150_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    peak = _max(m, 126)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)

