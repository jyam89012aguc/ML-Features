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
def _f53rp_rev_opex(rev, opex):
    return rev / opex.replace(0, np.nan)


def _f53rp_rev_ppne(rev, ppne):
    return rev / ppne.replace(0, np.nan)


def _f53rp_rev_assets(rev, assets):
    return rev / assets.replace(0, np.nan)


def _f53rp_align(q, idx):
    return q.reindex(idx).ffill()


# 21d range (max-min) of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_rng_21d_base_v076_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _max(m, 21) - _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range (max-min) of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_rng_21d_base_v077_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _max(m, 21) - _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range (max-min) of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_rng_21d_base_v078_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _max(m, 21) - _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range (max-min) of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_rng_63d_base_v079_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _max(m, 63) - _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range (max-min) of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_rng_63d_base_v080_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _max(m, 63) - _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range (max-min) of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_rng_63d_base_v081_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _max(m, 63) - _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range (max-min) of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_rng_126d_base_v082_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _max(m, 126) - _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range (max-min) of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_rng_126d_base_v083_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _max(m, 126) - _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range (max-min) of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_rng_126d_base_v084_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _max(m, 126) - _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range (max-min) of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_rng_252d_base_v085_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _max(m, 252) - _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range (max-min) of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_rng_252d_base_v086_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _max(m, 252) - _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range (max-min) of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_rng_252d_base_v087_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _max(m, 252) - _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range (max-min) of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_rng_504d_base_v088_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _max(m, 504) - _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range (max-min) of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_rng_504d_base_v089_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _max(m, 504) - _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range (max-min) of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_rng_504d_base_v090_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _max(m, 504) - _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position in rolling range of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_pos_21d_base_v091_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    lo = _min(m, 21)
    hi = _max(m, 21)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position in rolling range of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_pos_21d_base_v092_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    lo = _min(m, 21)
    hi = _max(m, 21)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position in rolling range of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_pos_21d_base_v093_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    lo = _min(m, 21)
    hi = _max(m, 21)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position in rolling range of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_pos_63d_base_v094_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    lo = _min(m, 63)
    hi = _max(m, 63)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position in rolling range of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_pos_63d_base_v095_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    lo = _min(m, 63)
    hi = _max(m, 63)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position in rolling range of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_pos_63d_base_v096_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    lo = _min(m, 63)
    hi = _max(m, 63)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position in rolling range of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_pos_126d_base_v097_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    lo = _min(m, 126)
    hi = _max(m, 126)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position in rolling range of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_pos_126d_base_v098_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    lo = _min(m, 126)
    hi = _max(m, 126)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position in rolling range of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_pos_126d_base_v099_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    lo = _min(m, 126)
    hi = _max(m, 126)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position in rolling range of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_pos_252d_base_v100_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    lo = _min(m, 252)
    hi = _max(m, 252)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position in rolling range of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_pos_252d_base_v101_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    lo = _min(m, 252)
    hi = _max(m, 252)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position in rolling range of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_pos_252d_base_v102_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    lo = _min(m, 252)
    hi = _max(m, 252)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position in rolling range of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_pos_504d_base_v103_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    lo = _min(m, 504)
    hi = _max(m, 504)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position in rolling range of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_pos_504d_base_v104_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    lo = _min(m, 504)
    hi = _max(m, 504)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position in rolling range of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_pos_504d_base_v105_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    lo = _min(m, 504)
    hi = _max(m, 504)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of revopex from rolling peak
def f53rp_f53_semi_revenue_per_employee_revopex_dd_21d_base_v106_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    peak = _max(m, 21)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of revppne from rolling peak
def f53rp_f53_semi_revenue_per_employee_revppne_dd_21d_base_v107_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    peak = _max(m, 21)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of revassets from rolling peak
def f53rp_f53_semi_revenue_per_employee_revassets_dd_21d_base_v108_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    peak = _max(m, 21)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of revopex from rolling peak
def f53rp_f53_semi_revenue_per_employee_revopex_dd_63d_base_v109_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    peak = _max(m, 63)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of revppne from rolling peak
def f53rp_f53_semi_revenue_per_employee_revppne_dd_63d_base_v110_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    peak = _max(m, 63)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of revassets from rolling peak
def f53rp_f53_semi_revenue_per_employee_revassets_dd_63d_base_v111_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    peak = _max(m, 63)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of revopex from rolling peak
def f53rp_f53_semi_revenue_per_employee_revopex_dd_126d_base_v112_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    peak = _max(m, 126)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of revppne from rolling peak
def f53rp_f53_semi_revenue_per_employee_revppne_dd_126d_base_v113_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    peak = _max(m, 126)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of revassets from rolling peak
def f53rp_f53_semi_revenue_per_employee_revassets_dd_126d_base_v114_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    peak = _max(m, 126)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of revopex from rolling peak
def f53rp_f53_semi_revenue_per_employee_revopex_dd_252d_base_v115_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    peak = _max(m, 252)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of revppne from rolling peak
def f53rp_f53_semi_revenue_per_employee_revppne_dd_252d_base_v116_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    peak = _max(m, 252)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of revassets from rolling peak
def f53rp_f53_semi_revenue_per_employee_revassets_dd_252d_base_v117_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    peak = _max(m, 252)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of revopex from rolling peak
def f53rp_f53_semi_revenue_per_employee_revopex_dd_504d_base_v118_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    peak = _max(m, 504)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of revppne from rolling peak
def f53rp_f53_semi_revenue_per_employee_revppne_dd_504d_base_v119_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    peak = _max(m, 504)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of revassets from rolling peak
def f53rp_f53_semi_revenue_per_employee_revassets_dd_504d_base_v120_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    peak = _max(m, 504)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of revopex above rolling trough
def f53rp_f53_semi_revenue_per_employee_revopex_up_21d_base_v121_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    trough = _min(m, 21)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of revppne above rolling trough
def f53rp_f53_semi_revenue_per_employee_revppne_up_21d_base_v122_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    trough = _min(m, 21)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of revassets above rolling trough
def f53rp_f53_semi_revenue_per_employee_revassets_up_21d_base_v123_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    trough = _min(m, 21)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of revopex above rolling trough
def f53rp_f53_semi_revenue_per_employee_revopex_up_63d_base_v124_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    trough = _min(m, 63)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of revppne above rolling trough
def f53rp_f53_semi_revenue_per_employee_revppne_up_63d_base_v125_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    trough = _min(m, 63)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of revassets above rolling trough
def f53rp_f53_semi_revenue_per_employee_revassets_up_63d_base_v126_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    trough = _min(m, 63)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of revopex above rolling trough
def f53rp_f53_semi_revenue_per_employee_revopex_up_126d_base_v127_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    trough = _min(m, 126)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of revppne above rolling trough
def f53rp_f53_semi_revenue_per_employee_revppne_up_126d_base_v128_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    trough = _min(m, 126)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of revassets above rolling trough
def f53rp_f53_semi_revenue_per_employee_revassets_up_126d_base_v129_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    trough = _min(m, 126)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of revopex above rolling trough
def f53rp_f53_semi_revenue_per_employee_revopex_up_252d_base_v130_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    trough = _min(m, 252)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of revppne above rolling trough
def f53rp_f53_semi_revenue_per_employee_revppne_up_252d_base_v131_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    trough = _min(m, 252)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of revassets above rolling trough
def f53rp_f53_semi_revenue_per_employee_revassets_up_252d_base_v132_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    trough = _min(m, 252)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of revopex above rolling trough
def f53rp_f53_semi_revenue_per_employee_revopex_up_504d_base_v133_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    trough = _min(m, 504)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of revppne above rolling trough
def f53rp_f53_semi_revenue_per_employee_revppne_up_504d_base_v134_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    trough = _min(m, 504)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of revassets above rolling trough
def f53rp_f53_semi_revenue_per_employee_revassets_up_504d_base_v135_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    trough = _min(m, 504)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_std_21d_base_v136_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _std(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_std_21d_base_v137_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _std(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_std_21d_base_v138_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _std(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_std_63d_base_v139_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _std(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_std_63d_base_v140_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _std(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_std_63d_base_v141_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _std(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_std_126d_base_v142_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _std(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_std_126d_base_v143_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _std(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_std_126d_base_v144_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _std(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_std_252d_base_v145_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _std(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_std_252d_base_v146_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _std(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_std_252d_base_v147_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _std(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of revopex
def f53rp_f53_semi_revenue_per_employee_revopex_std_504d_base_v148_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_opex(revenue, opex), closeadj.index)
    result = _std(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of revppne
def f53rp_f53_semi_revenue_per_employee_revppne_std_504d_base_v149_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_ppne(revenue, ppnenet), closeadj.index)
    result = _std(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of revassets
def f53rp_f53_semi_revenue_per_employee_revassets_std_504d_base_v150_signal(revenue, opex, ppnenet, assets, closeadj):
    m = _f53rp_align(_f53rp_rev_assets(revenue, assets), closeadj.index)
    result = _std(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)

