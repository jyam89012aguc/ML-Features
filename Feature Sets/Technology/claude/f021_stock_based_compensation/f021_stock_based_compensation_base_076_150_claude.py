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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f021_sbc_to_rev(sbcomp, revenue):
    return sbcomp / revenue.abs().replace(0, np.nan)


def _f021_sbc_to_mcap(sbcomp, marketcap):
    return sbcomp / marketcap.replace(0, np.nan).abs()


# 63d z-score of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_z_63d_base_v076_signal(sbcomp, closeadj):
    base = sbcomp
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_z_126d_base_v077_signal(sbcomp, closeadj):
    base = sbcomp
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_z_252d_base_v078_signal(sbcomp, closeadj):
    base = sbcomp
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_z_504d_base_v079_signal(sbcomp, closeadj):
    base = sbcomp
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_z_63d_base_v080_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_z_126d_base_v081_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_z_252d_base_v082_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_z_504d_base_v083_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_z_63d_base_v084_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_z_126d_base_v085_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_z_252d_base_v086_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_z_504d_base_v087_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_z_63d_base_v088_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_z_126d_base_v089_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_z_252d_base_v090_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_z_504d_base_v091_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_z_63d_base_v092_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_z_126d_base_v093_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_z_252d_base_v094_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_z_504d_base_v095_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_z_63d_base_v096_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_z_126d_base_v097_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_z_252d_base_v098_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_z_504d_base_v099_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_z_63d_base_v100_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_z_126d_base_v101_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_z_252d_base_v102_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_z_504d_base_v103_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_z_63d_base_v104_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_z_126d_base_v105_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_z_252d_base_v106_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_z_504d_base_v107_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_z_63d_base_v108_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_z_126d_base_v109_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_z_252d_base_v110_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_z_504d_base_v111_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_z_63d_base_v112_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_z_126d_base_v113_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_z_252d_base_v114_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_z_504d_base_v115_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_z_63d_base_v116_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_z_126d_base_v117_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_z_252d_base_v118_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_z_504d_base_v119_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_z_63d_base_v120_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_z_126d_base_v121_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_z_252d_base_v122_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_z_504d_base_v123_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_z_63d_base_v124_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_z_126d_base_v125_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_z_252d_base_v126_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_z_504d_base_v127_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_z_63d_base_v128_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_z_126d_base_v129_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_z_252d_base_v130_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_z_504d_base_v131_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_z_63d_base_v132_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_z_126d_base_v133_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_z_252d_base_v134_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_z_504d_base_v135_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_z_63d_base_v136_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_z_126d_base_v137_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_z_252d_base_v138_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_z_504d_base_v139_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_z_63d_base_v140_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_z_126d_base_v141_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_z_252d_base_v142_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_z_504d_base_v143_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_z_63d_base_v144_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_z_126d_base_v145_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_z_252d_base_v146_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_z_504d_base_v147_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_z_63d_base_v148_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_z_126d_base_v149_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_z_252d_base_v150_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_z_504d_base_v151_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_distmax_252d_base_v152_signal(sbcomp, closeadj):
    base = sbcomp
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_distmax_504d_base_v153_signal(sbcomp, closeadj):
    base = sbcomp
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_distmax_252d_base_v154_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_distmax_504d_base_v155_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_distmax_252d_base_v156_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_distmax_504d_base_v157_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_distmax_252d_base_v158_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_distmax_504d_base_v159_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_distmax_252d_base_v160_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_distmax_504d_base_v161_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_distmax_252d_base_v162_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_distmax_504d_base_v163_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_distmax_252d_base_v164_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_distmax_504d_base_v165_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_distmax_252d_base_v166_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_distmax_504d_base_v167_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_distmax_252d_base_v168_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_distmax_504d_base_v169_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_distmax_252d_base_v170_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_distmax_504d_base_v171_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_distmax_252d_base_v172_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_distmax_504d_base_v173_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_distmax_252d_base_v174_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_distmax_504d_base_v175_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

