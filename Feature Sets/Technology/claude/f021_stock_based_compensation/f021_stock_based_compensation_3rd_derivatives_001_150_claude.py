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


# 21d acceleration of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_accel_21d_3d_v001_signal(sbcomp, closeadj):
    base = sbcomp
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_accel_63d_3d_v002_signal(sbcomp, closeadj):
    base = sbcomp
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_accel_126d_3d_v003_signal(sbcomp, closeadj):
    base = sbcomp
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_accel_252d_3d_v004_signal(sbcomp, closeadj):
    base = sbcomp
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_accel_21d_3d_v005_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_accel_63d_3d_v006_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_accel_126d_3d_v007_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_accel_252d_3d_v008_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_accel_21d_3d_v009_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_accel_63d_3d_v010_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_accel_126d_3d_v011_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_accel_252d_3d_v012_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_accel_21d_3d_v013_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_accel_63d_3d_v014_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_accel_126d_3d_v015_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_accel_252d_3d_v016_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_accel_21d_3d_v017_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_accel_63d_3d_v018_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_accel_126d_3d_v019_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_accel_252d_3d_v020_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_accel_21d_3d_v021_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_accel_63d_3d_v022_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_accel_126d_3d_v023_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_accel_252d_3d_v024_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_accel_21d_3d_v025_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_accel_63d_3d_v026_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_accel_126d_3d_v027_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_accel_252d_3d_v028_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_accel_21d_3d_v029_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_accel_63d_3d_v030_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_accel_126d_3d_v031_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_accel_252d_3d_v032_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_accel_21d_3d_v033_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_accel_63d_3d_v034_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_accel_126d_3d_v035_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_accel_252d_3d_v036_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_accel_21d_3d_v037_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_accel_63d_3d_v038_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_accel_126d_3d_v039_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_accel_252d_3d_v040_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_accel_21d_3d_v041_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_accel_63d_3d_v042_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_accel_126d_3d_v043_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_accel_252d_3d_v044_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_accel_21d_3d_v045_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_accel_63d_3d_v046_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_accel_126d_3d_v047_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_accel_252d_3d_v048_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_accel_21d_3d_v049_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_accel_63d_3d_v050_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_accel_126d_3d_v051_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_accel_252d_3d_v052_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_accel_21d_3d_v053_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_accel_63d_3d_v054_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_accel_126d_3d_v055_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_accel_252d_3d_v056_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_accel_21d_3d_v057_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_accel_63d_3d_v058_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_accel_126d_3d_v059_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_accel_252d_3d_v060_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_accel_21d_3d_v061_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_accel_63d_3d_v062_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_accel_126d_3d_v063_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_accel_252d_3d_v064_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_accel_21d_3d_v065_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_accel_63d_3d_v066_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_accel_126d_3d_v067_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_accel_252d_3d_v068_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_accel_21d_3d_v069_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_accel_63d_3d_v070_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_accel_126d_3d_v071_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_accel_252d_3d_v072_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_accel_21d_3d_v073_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_accel_63d_3d_v074_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_accel_126d_3d_v075_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_accel_252d_3d_v076_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_slopez_21d_z126_3d_v077_signal(sbcomp, closeadj):
    base = sbcomp
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_slopez_63d_z252_3d_v078_signal(sbcomp, closeadj):
    base = sbcomp
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_slopez_126d_z252_3d_v079_signal(sbcomp, closeadj):
    base = sbcomp
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_slopez_252d_z504_3d_v080_signal(sbcomp, closeadj):
    base = sbcomp
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_slopez_21d_z126_3d_v081_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_slopez_63d_z252_3d_v082_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_slopez_126d_z252_3d_v083_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_slopez_252d_z504_3d_v084_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_slopez_21d_z126_3d_v085_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_slopez_63d_z252_3d_v086_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_slopez_126d_z252_3d_v087_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_slopez_252d_z504_3d_v088_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_slopez_21d_z126_3d_v089_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_slopez_63d_z252_3d_v090_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_slopez_126d_z252_3d_v091_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_slopez_252d_z504_3d_v092_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_slopez_21d_z126_3d_v093_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_slopez_63d_z252_3d_v094_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_slopez_126d_z252_3d_v095_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_slopez_252d_z504_3d_v096_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_slopez_21d_z126_3d_v097_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_slopez_63d_z252_3d_v098_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_slopez_126d_z252_3d_v099_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_slopez_252d_z504_3d_v100_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_slopez_21d_z126_3d_v101_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_slopez_63d_z252_3d_v102_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_slopez_126d_z252_3d_v103_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_slopez_252d_z504_3d_v104_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_slopez_21d_z126_3d_v105_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_slopez_63d_z252_3d_v106_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_slopez_126d_z252_3d_v107_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_slopez_252d_z504_3d_v108_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_slopez_21d_z126_3d_v109_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_slopez_63d_z252_3d_v110_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_slopez_126d_z252_3d_v111_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_slopez_252d_z504_3d_v112_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_slopez_21d_z126_3d_v113_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_slopez_63d_z252_3d_v114_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_slopez_126d_z252_3d_v115_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_slopez_252d_z504_3d_v116_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_slopez_21d_z126_3d_v117_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_slopez_63d_z252_3d_v118_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_slopez_126d_z252_3d_v119_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_slopez_252d_z504_3d_v120_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_slopez_21d_z126_3d_v121_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_slopez_63d_z252_3d_v122_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_slopez_126d_z252_3d_v123_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_slopez_252d_z504_3d_v124_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_slopez_21d_z126_3d_v125_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_slopez_63d_z252_3d_v126_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_slopez_126d_z252_3d_v127_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_slopez_252d_z504_3d_v128_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_slopez_21d_z126_3d_v129_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_slopez_63d_z252_3d_v130_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_slopez_126d_z252_3d_v131_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_slopez_252d_z504_3d_v132_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_slopez_21d_z126_3d_v133_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_slopez_63d_z252_3d_v134_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_slopez_126d_z252_3d_v135_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_slopez_252d_z504_3d_v136_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_slopez_21d_z126_3d_v137_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_slopez_63d_z252_3d_v138_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_slopez_126d_z252_3d_v139_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_slopez_252d_z504_3d_v140_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_slopez_21d_z126_3d_v141_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_slopez_63d_z252_3d_v142_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_slopez_126d_z252_3d_v143_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbcmc_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_mcap_bucket_dist_slopez_252d_z504_3d_v144_signal(sbcomp, marketcap, sbcmc_mcap_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_mcap_med) / sbcmc_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_slopez_21d_z126_3d_v145_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_slopez_63d_z252_3d_v146_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_slopez_126d_z252_3d_v147_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbcmc_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_pctile_slopez_252d_z504_3d_v148_signal(sbcmc_sector_pctile, closeadj):
    base = sbcmc_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_slopez_21d_z126_3d_v149_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_slopez_63d_z252_3d_v150_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_slopez_126d_z252_3d_v151_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbcmc_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_pctile_slopez_252d_z504_3d_v152_signal(sbcmc_industry_pctile, closeadj):
    base = sbcmc_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_jerk_21d_3d_v153_signal(sbcomp, closeadj):
    base = sbcomp
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_jerk_63d_3d_v154_signal(sbcomp, closeadj):
    base = sbcomp
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_lvl
def f021sbc_f021_stock_based_compensation_sbc_lvl_jerk_126d_3d_v155_signal(sbcomp, closeadj):
    base = sbcomp
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_jerk_21d_3d_v156_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_jerk_63d_3d_v157_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_to_rev
def f021sbc_f021_stock_based_compensation_sbc_to_rev_jerk_126d_3d_v158_signal(sbcomp, revenue, closeadj):
    base = _f021_sbc_to_rev(sbcomp, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_jerk_21d_3d_v159_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_jerk_63d_3d_v160_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_to_mcap
def f021sbc_f021_stock_based_compensation_sbc_to_mcap_jerk_126d_3d_v161_signal(sbcomp, marketcap, closeadj):
    base = _f021_sbc_to_mcap(sbcomp, marketcap)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_jerk_21d_3d_v162_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_jerk_63d_3d_v163_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_to_opex
def f021sbc_f021_stock_based_compensation_sbc_to_opex_jerk_126d_3d_v164_signal(sbcomp, opex, closeadj):
    base = sbcomp / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_jerk_21d_3d_v165_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_jerk_63d_3d_v166_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_to_rnd
def f021sbc_f021_stock_based_compensation_sbc_to_rnd_jerk_126d_3d_v167_signal(sbcomp, rnd, closeadj):
    base = sbcomp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_jerk_21d_3d_v168_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_jerk_63d_3d_v169_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_per_share
def f021sbc_f021_stock_based_compensation_sbc_per_share_jerk_126d_3d_v170_signal(sbcomp, sharesbas, closeadj):
    base = sbcomp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_jerk_21d_3d_v171_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_jerk_63d_3d_v172_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_to_equity
def f021sbc_f021_stock_based_compensation_sbc_to_equity_jerk_126d_3d_v173_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_jerk_21d_3d_v174_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_jerk_63d_3d_v175_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbcrev_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_dist_jerk_126d_3d_v176_signal(sbcomp, revenue, sbcrev_sector_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_jerk_21d_3d_v177_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_jerk_63d_3d_v178_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbcrev_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_z_jerk_126d_3d_v179_signal(sbcomp, revenue, sbcrev_sector_med, sbcrev_sector_std, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_sector_med) / sbcrev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_jerk_21d_3d_v180_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_jerk_63d_3d_v181_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbcrev_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_dist_jerk_126d_3d_v182_signal(sbcomp, revenue, sbcrev_industry_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_industry_med) / sbcrev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_jerk_21d_3d_v183_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_jerk_63d_3d_v184_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbcrev_peer_mcap_bucket_dist
def f021sbc_f021_stock_based_compensation_sbcrev_peer_mcap_bucket_dist_jerk_126d_3d_v185_signal(sbcomp, revenue, sbcrev_mcap_med, closeadj):
    base = (_f021_sbc_to_rev(sbcomp, revenue) - sbcrev_mcap_med) / sbcrev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_jerk_21d_3d_v186_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_jerk_63d_3d_v187_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbcrev_peer_sector_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_sector_pctile_jerk_126d_3d_v188_signal(sbcrev_sector_pctile, closeadj):
    base = sbcrev_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_jerk_21d_3d_v189_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_jerk_63d_3d_v190_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbcrev_peer_industry_pctile
def f021sbc_f021_stock_based_compensation_sbcrev_peer_industry_pctile_jerk_126d_3d_v191_signal(sbcrev_industry_pctile, closeadj):
    base = sbcrev_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_jerk_21d_3d_v192_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_jerk_63d_3d_v193_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbcmc_peer_sector_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_dist_jerk_126d_3d_v194_signal(sbcomp, marketcap, sbcmc_sector_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_jerk_21d_3d_v195_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_jerk_63d_3d_v196_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbcmc_peer_sector_z
def f021sbc_f021_stock_based_compensation_sbcmc_peer_sector_z_jerk_126d_3d_v197_signal(sbcomp, marketcap, sbcmc_sector_med, sbcmc_sector_std, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_sector_med) / sbcmc_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_jerk_21d_3d_v198_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_jerk_63d_3d_v199_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbcmc_peer_industry_dist
def f021sbc_f021_stock_based_compensation_sbcmc_peer_industry_dist_jerk_126d_3d_v200_signal(sbcomp, marketcap, sbcmc_industry_med, closeadj):
    base = (_f021_sbc_to_mcap(sbcomp, marketcap) - sbcmc_industry_med) / sbcmc_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

