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
def _f018_rnd_to_rev(rnd, revenue):
    return rnd / revenue.abs().replace(0, np.nan)


def _f018_rnd_to_opex(rnd, opex):
    return rnd / opex.abs().replace(0, np.nan)


# 21d slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_slope_21d_2d_v001_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_slope_63d_2d_v002_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_slope_126d_2d_v003_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_slope_252d_2d_v004_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_slope_504d_2d_v005_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_slope_21d_2d_v006_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_slope_63d_2d_v007_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_slope_126d_2d_v008_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_slope_252d_2d_v009_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_slope_504d_2d_v010_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_slope_21d_2d_v011_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_slope_63d_2d_v012_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_slope_126d_2d_v013_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_slope_252d_2d_v014_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_slope_504d_2d_v015_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_slope_21d_2d_v016_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_slope_63d_2d_v017_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_slope_126d_2d_v018_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_slope_252d_2d_v019_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_slope_504d_2d_v020_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_slope_21d_2d_v021_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_slope_63d_2d_v022_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_slope_126d_2d_v023_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_slope_252d_2d_v024_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_slope_504d_2d_v025_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_slope_21d_2d_v026_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_slope_63d_2d_v027_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_slope_126d_2d_v028_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_slope_252d_2d_v029_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_slope_504d_2d_v030_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_slope_21d_2d_v031_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_slope_63d_2d_v032_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_slope_126d_2d_v033_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_slope_252d_2d_v034_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_slope_504d_2d_v035_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_slope_21d_2d_v036_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_slope_63d_2d_v037_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_slope_126d_2d_v038_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_slope_252d_2d_v039_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_slope_504d_2d_v040_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_slope_21d_2d_v041_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_slope_63d_2d_v042_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_slope_126d_2d_v043_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_slope_252d_2d_v044_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_slope_504d_2d_v045_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_slope_21d_2d_v046_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_slope_63d_2d_v047_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_slope_126d_2d_v048_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_slope_252d_2d_v049_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_slope_504d_2d_v050_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_slope_21d_2d_v051_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_slope_63d_2d_v052_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_slope_126d_2d_v053_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_slope_252d_2d_v054_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_slope_504d_2d_v055_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_slope_21d_2d_v056_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_slope_63d_2d_v057_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_slope_126d_2d_v058_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_slope_252d_2d_v059_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_slope_504d_2d_v060_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_slope_21d_2d_v061_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_slope_63d_2d_v062_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_slope_126d_2d_v063_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_slope_252d_2d_v064_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_slope_504d_2d_v065_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_sm21_sl21_2d_v066_signal(rnd, revenue, closeadj):
    base = _mean(_f018_rnd_to_rev(rnd, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_sm63_sl21_2d_v067_signal(rnd, revenue, closeadj):
    base = _mean(_f018_rnd_to_rev(rnd, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_sm63_sl63_2d_v068_signal(rnd, revenue, closeadj):
    base = _mean(_f018_rnd_to_rev(rnd, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_sm252_sl63_2d_v069_signal(rnd, revenue, closeadj):
    base = _mean(_f018_rnd_to_rev(rnd, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_sm252_sl126_2d_v070_signal(rnd, revenue, closeadj):
    base = _mean(_f018_rnd_to_rev(rnd, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_sm21_sl21_2d_v071_signal(rnd, opex, closeadj):
    base = _mean(_f018_rnd_to_opex(rnd, opex), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_sm63_sl21_2d_v072_signal(rnd, opex, closeadj):
    base = _mean(_f018_rnd_to_opex(rnd, opex), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_sm63_sl63_2d_v073_signal(rnd, opex, closeadj):
    base = _mean(_f018_rnd_to_opex(rnd, opex), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_sm252_sl63_2d_v074_signal(rnd, opex, closeadj):
    base = _mean(_f018_rnd_to_opex(rnd, opex), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_sm252_sl126_2d_v075_signal(rnd, opex, closeadj):
    base = _mean(_f018_rnd_to_opex(rnd, opex), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_sm21_sl21_2d_v076_signal(rnd, gp, closeadj):
    base = _mean(rnd / gp.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_sm63_sl21_2d_v077_signal(rnd, gp, closeadj):
    base = _mean(rnd / gp.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_sm63_sl63_2d_v078_signal(rnd, gp, closeadj):
    base = _mean(rnd / gp.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_sm252_sl63_2d_v079_signal(rnd, gp, closeadj):
    base = _mean(rnd / gp.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_sm252_sl126_2d_v080_signal(rnd, gp, closeadj):
    base = _mean(rnd / gp.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_sm21_sl21_2d_v081_signal(rnd, cashneq, closeadj):
    base = _mean(rnd / cashneq.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_sm63_sl21_2d_v082_signal(rnd, cashneq, closeadj):
    base = _mean(rnd / cashneq.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_sm63_sl63_2d_v083_signal(rnd, cashneq, closeadj):
    base = _mean(rnd / cashneq.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_sm252_sl63_2d_v084_signal(rnd, cashneq, closeadj):
    base = _mean(rnd / cashneq.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_sm252_sl126_2d_v085_signal(rnd, cashneq, closeadj):
    base = _mean(rnd / cashneq.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_sm21_sl21_2d_v086_signal(rnd, assets, closeadj):
    base = _mean(rnd / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_sm63_sl21_2d_v087_signal(rnd, assets, closeadj):
    base = _mean(rnd / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_sm63_sl63_2d_v088_signal(rnd, assets, closeadj):
    base = _mean(rnd / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_sm252_sl63_2d_v089_signal(rnd, assets, closeadj):
    base = _mean(rnd / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_sm252_sl126_2d_v090_signal(rnd, assets, closeadj):
    base = _mean(rnd / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_sm21_sl21_2d_v091_signal(rnd, ebit, closeadj):
    base = _mean(rnd / ebit.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_sm63_sl21_2d_v092_signal(rnd, ebit, closeadj):
    base = _mean(rnd / ebit.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_sm63_sl63_2d_v093_signal(rnd, ebit, closeadj):
    base = _mean(rnd / ebit.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_sm252_sl63_2d_v094_signal(rnd, ebit, closeadj):
    base = _mean(rnd / ebit.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_sm252_sl126_2d_v095_signal(rnd, ebit, closeadj):
    base = _mean(rnd / ebit.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_sm21_sl21_2d_v096_signal(rnd, netinc, closeadj):
    base = _mean(rnd / (-netinc).clip(lower=0).replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_sm63_sl21_2d_v097_signal(rnd, netinc, closeadj):
    base = _mean(rnd / (-netinc).clip(lower=0).replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_sm63_sl63_2d_v098_signal(rnd, netinc, closeadj):
    base = _mean(rnd / (-netinc).clip(lower=0).replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_sm252_sl63_2d_v099_signal(rnd, netinc, closeadj):
    base = _mean(rnd / (-netinc).clip(lower=0).replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_sm252_sl126_2d_v100_signal(rnd, netinc, closeadj):
    base = _mean(rnd / (-netinc).clip(lower=0).replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_sm21_sl21_2d_v101_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_sm63_sl21_2d_v102_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_sm63_sl63_2d_v103_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_sm252_sl63_2d_v104_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_sm252_sl126_2d_v105_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_sm21_sl21_2d_v106_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_sm63_sl21_2d_v107_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_sm63_sl63_2d_v108_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_sm252_sl63_2d_v109_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_sm252_sl126_2d_v110_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_sm21_sl21_2d_v111_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_sm63_sl21_2d_v112_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_sm63_sl63_2d_v113_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_sm252_sl63_2d_v114_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_sm252_sl126_2d_v115_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_sm21_sl21_2d_v116_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_sm63_sl21_2d_v117_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_sm63_sl63_2d_v118_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_sm252_sl63_2d_v119_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_sm252_sl126_2d_v120_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = _mean((_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_sm21_sl21_2d_v121_signal(rnd_to_rev_sector_pctile, closeadj):
    base = _mean(rnd_to_rev_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_sm63_sl21_2d_v122_signal(rnd_to_rev_sector_pctile, closeadj):
    base = _mean(rnd_to_rev_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_sm63_sl63_2d_v123_signal(rnd_to_rev_sector_pctile, closeadj):
    base = _mean(rnd_to_rev_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_sm252_sl63_2d_v124_signal(rnd_to_rev_sector_pctile, closeadj):
    base = _mean(rnd_to_rev_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_sm252_sl126_2d_v125_signal(rnd_to_rev_sector_pctile, closeadj):
    base = _mean(rnd_to_rev_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_sm21_sl21_2d_v126_signal(rnd_to_rev_industry_pctile, closeadj):
    base = _mean(rnd_to_rev_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_sm63_sl21_2d_v127_signal(rnd_to_rev_industry_pctile, closeadj):
    base = _mean(rnd_to_rev_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_sm63_sl63_2d_v128_signal(rnd_to_rev_industry_pctile, closeadj):
    base = _mean(rnd_to_rev_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_sm252_sl63_2d_v129_signal(rnd_to_rev_industry_pctile, closeadj):
    base = _mean(rnd_to_rev_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_sm252_sl126_2d_v130_signal(rnd_to_rev_industry_pctile, closeadj):
    base = _mean(rnd_to_rev_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_pctslope_21d_2d_v131_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_pctslope_63d_2d_v132_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_pctslope_252d_2d_v133_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_pctslope_21d_2d_v134_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_pctslope_63d_2d_v135_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_pctslope_252d_2d_v136_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_pctslope_21d_2d_v137_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_pctslope_63d_2d_v138_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_pctslope_252d_2d_v139_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_pctslope_21d_2d_v140_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_pctslope_63d_2d_v141_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_pctslope_252d_2d_v142_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_pctslope_21d_2d_v143_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_pctslope_63d_2d_v144_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_pctslope_252d_2d_v145_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_pctslope_21d_2d_v146_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_pctslope_63d_2d_v147_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_pctslope_252d_2d_v148_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_pctslope_21d_2d_v149_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_pctslope_63d_2d_v150_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_pctslope_252d_2d_v151_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_pctslope_21d_2d_v152_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_pctslope_63d_2d_v153_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_pctslope_252d_2d_v154_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_pctslope_21d_2d_v155_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_pctslope_63d_2d_v156_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_pctslope_252d_2d_v157_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_pctslope_21d_2d_v158_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_pctslope_63d_2d_v159_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_pctslope_252d_2d_v160_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_pctslope_21d_2d_v161_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_pctslope_63d_2d_v162_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_pctslope_252d_2d_v163_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_pctslope_21d_2d_v164_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_pctslope_63d_2d_v165_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_pctslope_252d_2d_v166_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_pctslope_21d_2d_v167_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_pctslope_63d_2d_v168_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_pctslope_252d_2d_v169_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_sgnslope_21d_2d_v170_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_sgnslope_63d_2d_v171_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_sgnslope_252d_2d_v172_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_sgnslope_21d_2d_v173_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_sgnslope_63d_2d_v174_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_sgnslope_252d_2d_v175_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_sgnslope_21d_2d_v176_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_sgnslope_63d_2d_v177_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_sgnslope_252d_2d_v178_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_sgnslope_21d_2d_v179_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_sgnslope_63d_2d_v180_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_sgnslope_252d_2d_v181_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_sgnslope_21d_2d_v182_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_sgnslope_63d_2d_v183_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_sgnslope_252d_2d_v184_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_sgnslope_21d_2d_v185_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_sgnslope_63d_2d_v186_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_sgnslope_252d_2d_v187_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_sgnslope_21d_2d_v188_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_sgnslope_63d_2d_v189_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_sgnslope_252d_2d_v190_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_sgnslope_21d_2d_v191_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_sgnslope_63d_2d_v192_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_sgnslope_252d_2d_v193_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_sgnslope_21d_2d_v194_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_sgnslope_63d_2d_v195_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_sgnslope_252d_2d_v196_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_sgnslope_21d_2d_v197_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_sgnslope_63d_2d_v198_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_sgnslope_252d_2d_v199_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_sgnslope_21d_2d_v200_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

