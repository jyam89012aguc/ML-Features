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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f021_sbc_to_rev(sbcomp, revenue):
    return sbcomp / revenue.abs().replace(0, np.nan)


def _f021_sbc_to_mcap(sbcomp, marketcap):
    return sbcomp / marketcap.replace(0, np.nan).abs()


# 21d slope of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_slope_21d_2d_v001_signal(sbcomp, closeadj):
    base = sbcomp
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_slope_63d_2d_v002_signal(sbcomp, closeadj):
    base = sbcomp
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_slope_126d_2d_v003_signal(sbcomp, closeadj):
    base = sbcomp
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_slope_252d_2d_v004_signal(sbcomp, closeadj):
    base = sbcomp
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_slope_504d_2d_v005_signal(sbcomp, closeadj):
    base = sbcomp
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_slope_21d_2d_v006_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_slope_63d_2d_v007_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_slope_126d_2d_v008_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_slope_252d_2d_v009_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_slope_504d_2d_v010_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_slope_21d_2d_v011_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_slope_63d_2d_v012_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_slope_126d_2d_v013_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_slope_252d_2d_v014_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_slope_504d_2d_v015_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_slope_21d_2d_v016_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_slope_63d_2d_v017_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_slope_126d_2d_v018_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_slope_252d_2d_v019_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_slope_504d_2d_v020_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_slope_21d_2d_v021_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_slope_63d_2d_v022_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_slope_126d_2d_v023_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_slope_252d_2d_v024_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_slope_504d_2d_v025_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_slope_21d_2d_v026_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_slope_63d_2d_v027_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_slope_126d_2d_v028_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_slope_252d_2d_v029_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_slope_504d_2d_v030_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_slope_21d_2d_v031_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_slope_63d_2d_v032_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_slope_126d_2d_v033_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_slope_252d_2d_v034_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_slope_504d_2d_v035_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_slope_21d_2d_v036_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_slope_63d_2d_v037_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_slope_126d_2d_v038_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_slope_252d_2d_v039_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_slope_504d_2d_v040_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_slope_21d_2d_v041_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_slope_63d_2d_v042_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_slope_126d_2d_v043_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_slope_252d_2d_v044_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_slope_504d_2d_v045_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_slope_21d_2d_v046_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_slope_63d_2d_v047_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_slope_126d_2d_v048_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_slope_252d_2d_v049_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_slope_504d_2d_v050_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_slope_21d_2d_v051_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_slope_63d_2d_v052_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_slope_126d_2d_v053_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_slope_252d_2d_v054_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_slope_504d_2d_v055_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_slope_21d_2d_v056_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_slope_63d_2d_v057_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_slope_126d_2d_v058_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_slope_252d_2d_v059_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_slope_504d_2d_v060_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_slope_21d_2d_v061_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_slope_63d_2d_v062_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_slope_126d_2d_v063_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_slope_252d_2d_v064_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_slope_504d_2d_v065_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_slope_21d_2d_v066_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_slope_63d_2d_v067_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_slope_126d_2d_v068_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_slope_252d_2d_v069_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_slope_504d_2d_v070_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_slope_21d_2d_v071_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_slope_63d_2d_v072_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_slope_126d_2d_v073_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_slope_252d_2d_v074_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_slope_504d_2d_v075_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_slope_21d_2d_v076_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_slope_63d_2d_v077_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_slope_126d_2d_v078_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_slope_252d_2d_v079_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_slope_504d_2d_v080_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_slope_21d_2d_v081_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_slope_63d_2d_v082_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_slope_126d_2d_v083_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_slope_252d_2d_v084_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_slope_504d_2d_v085_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_slope_21d_2d_v086_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_slope_63d_2d_v087_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_slope_126d_2d_v088_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_slope_252d_2d_v089_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_slope_504d_2d_v090_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_slope_21d_2d_v091_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_slope_63d_2d_v092_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_slope_126d_2d_v093_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_slope_252d_2d_v094_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_slope_504d_2d_v095_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_sm21_sl21_2d_v096_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_sm63_sl21_2d_v097_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_sm63_sl63_2d_v098_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_sm252_sl63_2d_v099_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_sm252_sl126_2d_v100_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_sm21_sl21_2d_v101_signal(sbcomp, revenue, closeadj):
    base = _mean(_f021_sbc_to_rev(sbcomp, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_sm63_sl21_2d_v102_signal(sbcomp, revenue, closeadj):
    base = _mean(_f021_sbc_to_rev(sbcomp, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_sm63_sl63_2d_v103_signal(sbcomp, revenue, closeadj):
    base = _mean(_f021_sbc_to_rev(sbcomp, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_sm252_sl63_2d_v104_signal(sbcomp, revenue, closeadj):
    base = _mean(_f021_sbc_to_rev(sbcomp, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_sm252_sl126_2d_v105_signal(sbcomp, revenue, closeadj):
    base = _mean(_f021_sbc_to_rev(sbcomp, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_sm21_sl21_2d_v106_signal(sbcomp, marketcap, closeadj):
    base = _mean(_f021_sbc_to_mcap(sbcomp, marketcap), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_sm63_sl21_2d_v107_signal(sbcomp, marketcap, closeadj):
    base = _mean(_f021_sbc_to_mcap(sbcomp, marketcap), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_sm63_sl63_2d_v108_signal(sbcomp, marketcap, closeadj):
    base = _mean(_f021_sbc_to_mcap(sbcomp, marketcap), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_sm252_sl63_2d_v109_signal(sbcomp, marketcap, closeadj):
    base = _mean(_f021_sbc_to_mcap(sbcomp, marketcap), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_sm252_sl126_2d_v110_signal(sbcomp, marketcap, closeadj):
    base = _mean(_f021_sbc_to_mcap(sbcomp, marketcap), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_sm21_sl21_2d_v111_signal(sbcomp, opex, closeadj):
    base = _mean(sbcomp / opex.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_sm63_sl21_2d_v112_signal(sbcomp, opex, closeadj):
    base = _mean(sbcomp / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_sm63_sl63_2d_v113_signal(sbcomp, opex, closeadj):
    base = _mean(sbcomp / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_sm252_sl63_2d_v114_signal(sbcomp, opex, closeadj):
    base = _mean(sbcomp / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_sm252_sl126_2d_v115_signal(sbcomp, opex, closeadj):
    base = _mean(sbcomp / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_sm21_sl21_2d_v116_signal(sbcomp, rnd, closeadj):
    base = _mean(sbcomp / rnd.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_sm63_sl21_2d_v117_signal(sbcomp, rnd, closeadj):
    base = _mean(sbcomp / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_sm63_sl63_2d_v118_signal(sbcomp, rnd, closeadj):
    base = _mean(sbcomp / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_sm252_sl63_2d_v119_signal(sbcomp, rnd, closeadj):
    base = _mean(sbcomp / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_sm252_sl126_2d_v120_signal(sbcomp, rnd, closeadj):
    base = _mean(sbcomp / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_sm21_sl21_2d_v121_signal(sbcomp, sharesbas, closeadj):
    base = _mean(sbcomp / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_sm63_sl21_2d_v122_signal(sbcomp, sharesbas, closeadj):
    base = _mean(sbcomp / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_sm63_sl63_2d_v123_signal(sbcomp, sharesbas, closeadj):
    base = _mean(sbcomp / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_sm252_sl63_2d_v124_signal(sbcomp, sharesbas, closeadj):
    base = _mean(sbcomp / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_sm252_sl126_2d_v125_signal(sbcomp, sharesbas, closeadj):
    base = _mean(sbcomp / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_sm21_sl21_2d_v126_signal(sbcomp, equity, closeadj):
    base = _mean(sbcomp / equity.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_sm63_sl21_2d_v127_signal(sbcomp, equity, closeadj):
    base = _mean(sbcomp / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_sm63_sl63_2d_v128_signal(sbcomp, equity, closeadj):
    base = _mean(sbcomp / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_sm252_sl63_2d_v129_signal(sbcomp, equity, closeadj):
    base = _mean(sbcomp / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_sm252_sl126_2d_v130_signal(sbcomp, equity, closeadj):
    base = _mean(sbcomp / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_sm21_sl21_2d_v131_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_sm63_sl21_2d_v132_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_sm63_sl63_2d_v133_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_sm252_sl63_2d_v134_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_sm252_sl126_2d_v135_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_sm21_sl21_2d_v136_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_sm63_sl21_2d_v137_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_sm63_sl63_2d_v138_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_sm252_sl63_2d_v139_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_sm252_sl126_2d_v140_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_sm21_sl21_2d_v141_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_sm63_sl21_2d_v142_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_sm63_sl63_2d_v143_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_sm252_sl63_2d_v144_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_sm252_sl126_2d_v145_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_sm21_sl21_2d_v146_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_sm63_sl21_2d_v147_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_sm63_sl63_2d_v148_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_sm252_sl63_2d_v149_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_sm252_sl126_2d_v150_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = _mean((_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_sm21_sl21_2d_v151_signal(sbcrev_sector_pctile, closeadj):
    base = _mean(sbcrev_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_sm63_sl21_2d_v152_signal(sbcrev_sector_pctile, closeadj):
    base = _mean(sbcrev_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_sm63_sl63_2d_v153_signal(sbcrev_sector_pctile, closeadj):
    base = _mean(sbcrev_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_sm252_sl63_2d_v154_signal(sbcrev_sector_pctile, closeadj):
    base = _mean(sbcrev_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_sm252_sl126_2d_v155_signal(sbcrev_sector_pctile, closeadj):
    base = _mean(sbcrev_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_sm21_sl21_2d_v156_signal(sbcrev_industry_pctile, closeadj):
    base = _mean(sbcrev_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_sm63_sl21_2d_v157_signal(sbcrev_industry_pctile, closeadj):
    base = _mean(sbcrev_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_sm63_sl63_2d_v158_signal(sbcrev_industry_pctile, closeadj):
    base = _mean(sbcrev_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_sm252_sl63_2d_v159_signal(sbcrev_industry_pctile, closeadj):
    base = _mean(sbcrev_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_sm252_sl126_2d_v160_signal(sbcrev_industry_pctile, closeadj):
    base = _mean(sbcrev_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_sm21_sl21_2d_v161_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_sm63_sl21_2d_v162_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_sm63_sl63_2d_v163_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_sm252_sl63_2d_v164_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_sm252_sl126_2d_v165_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_sm21_sl21_2d_v166_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_sm63_sl21_2d_v167_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_sm63_sl63_2d_v168_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_sm252_sl63_2d_v169_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_sm252_sl126_2d_v170_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_sm21_sl21_2d_v171_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_sm63_sl21_2d_v172_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_sm63_sl63_2d_v173_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_sm252_sl63_2d_v174_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_sm252_sl126_2d_v175_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_sm21_sl21_2d_v176_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_sm63_sl21_2d_v177_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_sm63_sl63_2d_v178_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_sm252_sl63_2d_v179_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_sm252_sl126_2d_v180_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = _mean((_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_sm21_sl21_2d_v181_signal(sbcmc_sector_pctile, closeadj):
    base = _mean(sbcmc_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_sm63_sl21_2d_v182_signal(sbcmc_sector_pctile, closeadj):
    base = _mean(sbcmc_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_sm63_sl63_2d_v183_signal(sbcmc_sector_pctile, closeadj):
    base = _mean(sbcmc_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_sm252_sl63_2d_v184_signal(sbcmc_sector_pctile, closeadj):
    base = _mean(sbcmc_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_sm252_sl126_2d_v185_signal(sbcmc_sector_pctile, closeadj):
    base = _mean(sbcmc_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_sm21_sl21_2d_v186_signal(sbcmc_industry_pctile, closeadj):
    base = _mean(sbcmc_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_sm63_sl21_2d_v187_signal(sbcmc_industry_pctile, closeadj):
    base = _mean(sbcmc_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_sm63_sl63_2d_v188_signal(sbcmc_industry_pctile, closeadj):
    base = _mean(sbcmc_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_sm252_sl63_2d_v189_signal(sbcmc_industry_pctile, closeadj):
    base = _mean(sbcmc_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_sm252_sl126_2d_v190_signal(sbcmc_industry_pctile, closeadj):
    base = _mean(sbcmc_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_pctslope_21d_2d_v191_signal(sbcomp, closeadj):
    base = sbcomp
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_pctslope_63d_2d_v192_signal(sbcomp, closeadj):
    base = sbcomp
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_pctslope_252d_2d_v193_signal(sbcomp, closeadj):
    base = sbcomp
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_pctslope_21d_2d_v194_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_pctslope_63d_2d_v195_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_pctslope_252d_2d_v196_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_pctslope_21d_2d_v197_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_pctslope_63d_2d_v198_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_pctslope_252d_2d_v199_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_pctslope_21d_2d_v200_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

