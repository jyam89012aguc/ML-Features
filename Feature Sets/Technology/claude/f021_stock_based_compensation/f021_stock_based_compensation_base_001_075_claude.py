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


# 21d mean of sbc_lvl scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_lvl_mean_21d_base_v001_signal(sbcomp, closeadj):
    base = sbcomp
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_lvl scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_lvl_mean_63d_base_v002_signal(sbcomp, closeadj):
    base = sbcomp
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_lvl scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_lvl_mean_126d_base_v003_signal(sbcomp, closeadj):
    base = sbcomp
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_lvl scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_lvl_mean_252d_base_v004_signal(sbcomp, closeadj):
    base = sbcomp
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_lvl scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_lvl_mean_504d_base_v005_signal(sbcomp, closeadj):
    base = sbcomp
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbc_to_rev scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_rev_mean_21d_base_v006_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_to_rev scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_rev_mean_63d_base_v007_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_to_rev scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_rev_mean_126d_base_v008_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_to_rev scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_rev_mean_252d_base_v009_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_to_rev scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_rev_mean_504d_base_v010_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbc_to_mcap scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_mean_21d_base_v011_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_to_mcap scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_mean_63d_base_v012_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_to_mcap scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_mean_126d_base_v013_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_to_mcap scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_mean_252d_base_v014_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_to_mcap scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_mean_504d_base_v015_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbc_to_opex scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_opex_mean_21d_base_v016_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_to_opex scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_opex_mean_63d_base_v017_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_to_opex scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_opex_mean_126d_base_v018_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_to_opex scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_opex_mean_252d_base_v019_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_to_opex scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_opex_mean_504d_base_v020_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbc_to_rnd scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_mean_21d_base_v021_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_to_rnd scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_mean_63d_base_v022_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_to_rnd scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_mean_126d_base_v023_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_to_rnd scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_mean_252d_base_v024_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_to_rnd scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_mean_504d_base_v025_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbc_per_share scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_per_share_mean_21d_base_v026_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_per_share scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_per_share_mean_63d_base_v027_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_per_share scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_per_share_mean_126d_base_v028_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_per_share scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_per_share_mean_252d_base_v029_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_per_share scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_per_share_mean_504d_base_v030_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbc_to_equity scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_equity_mean_21d_base_v031_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_to_equity scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_equity_mean_63d_base_v032_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_to_equity scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_equity_mean_126d_base_v033_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_to_equity scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_equity_mean_252d_base_v034_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_to_equity scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbc_to_equity_mean_504d_base_v035_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbcrev_peer_sector_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_mean_21d_base_v036_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbcrev_peer_sector_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_mean_63d_base_v037_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbcrev_peer_sector_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_mean_126d_base_v038_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbcrev_peer_sector_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_mean_252d_base_v039_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbcrev_peer_sector_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_mean_504d_base_v040_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbcrev_peer_sector_z scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_mean_21d_base_v041_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbcrev_peer_sector_z scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_mean_63d_base_v042_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbcrev_peer_sector_z scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_mean_126d_base_v043_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbcrev_peer_sector_z scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_mean_252d_base_v044_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbcrev_peer_sector_z scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_mean_504d_base_v045_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbcrev_peer_industry_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_mean_21d_base_v046_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbcrev_peer_industry_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_mean_63d_base_v047_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbcrev_peer_industry_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_mean_126d_base_v048_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbcrev_peer_industry_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_mean_252d_base_v049_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbcrev_peer_industry_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_mean_504d_base_v050_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbcrev_peer_mcap_bucket_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_mean_21d_base_v051_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbcrev_peer_mcap_bucket_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_mean_63d_base_v052_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbcrev_peer_mcap_bucket_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_mean_126d_base_v053_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbcrev_peer_mcap_bucket_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_mean_252d_base_v054_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbcrev_peer_mcap_bucket_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_mean_504d_base_v055_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbcrev_peer_sector_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_mean_21d_base_v056_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbcrev_peer_sector_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_mean_63d_base_v057_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbcrev_peer_sector_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_mean_126d_base_v058_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbcrev_peer_sector_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_mean_252d_base_v059_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbcrev_peer_sector_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_mean_504d_base_v060_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbcrev_peer_industry_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_mean_21d_base_v061_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbcrev_peer_industry_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_mean_63d_base_v062_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbcrev_peer_industry_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_mean_126d_base_v063_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbcrev_peer_industry_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_mean_252d_base_v064_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbcrev_peer_industry_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_mean_504d_base_v065_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbcmc_peer_sector_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_mean_21d_base_v066_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbcmc_peer_sector_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_mean_63d_base_v067_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbcmc_peer_sector_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_mean_126d_base_v068_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbcmc_peer_sector_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_mean_252d_base_v069_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbcmc_peer_sector_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_mean_504d_base_v070_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbcmc_peer_sector_z scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_mean_21d_base_v071_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbcmc_peer_sector_z scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_mean_63d_base_v072_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbcmc_peer_sector_z scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_mean_126d_base_v073_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbcmc_peer_sector_z scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_mean_252d_base_v074_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbcmc_peer_sector_z scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_mean_504d_base_v075_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbcmc_peer_industry_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_mean_21d_base_v076_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbcmc_peer_industry_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_mean_63d_base_v077_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbcmc_peer_industry_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_mean_126d_base_v078_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbcmc_peer_industry_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_mean_252d_base_v079_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbcmc_peer_industry_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_mean_504d_base_v080_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbcmc_peer_mcap_bucket_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_mean_21d_base_v081_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbcmc_peer_mcap_bucket_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_mean_63d_base_v082_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbcmc_peer_mcap_bucket_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_mean_126d_base_v083_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbcmc_peer_mcap_bucket_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_mean_252d_base_v084_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbcmc_peer_mcap_bucket_dist scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_mean_504d_base_v085_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbcmc_peer_sector_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_mean_21d_base_v086_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbcmc_peer_sector_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_mean_63d_base_v087_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbcmc_peer_sector_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_mean_126d_base_v088_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbcmc_peer_sector_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_mean_252d_base_v089_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbcmc_peer_sector_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_mean_504d_base_v090_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbcmc_peer_industry_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_mean_21d_base_v091_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbcmc_peer_industry_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_mean_63d_base_v092_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbcmc_peer_industry_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_mean_126d_base_v093_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbcmc_peer_industry_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_mean_252d_base_v094_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbcmc_peer_industry_pctile scaled by closeadj
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_mean_504d_base_v095_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_median_63d_base_v096_signal(sbcomp, closeadj):
    base = sbcomp
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_median_252d_base_v097_signal(sbcomp, closeadj):
    base = sbcomp
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_median_504d_base_v098_signal(sbcomp, closeadj):
    base = sbcomp
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_median_63d_base_v099_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_median_252d_base_v100_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

