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


# 21d acceleration of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_accel_21d_3d_v001_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_accel_63d_3d_v002_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_accel_126d_3d_v003_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_accel_252d_3d_v004_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_accel_21d_3d_v005_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_accel_63d_3d_v006_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_accel_126d_3d_v007_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_accel_252d_3d_v008_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_accel_21d_3d_v009_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_accel_63d_3d_v010_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_accel_126d_3d_v011_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_accel_252d_3d_v012_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_accel_21d_3d_v013_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_accel_63d_3d_v014_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_accel_126d_3d_v015_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_accel_252d_3d_v016_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_accel_21d_3d_v017_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_accel_63d_3d_v018_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_accel_126d_3d_v019_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_accel_252d_3d_v020_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_accel_21d_3d_v021_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_accel_63d_3d_v022_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_accel_126d_3d_v023_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_accel_252d_3d_v024_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_accel_21d_3d_v025_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_accel_63d_3d_v026_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_accel_126d_3d_v027_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_accel_252d_3d_v028_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_accel_21d_3d_v029_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_accel_63d_3d_v030_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_accel_126d_3d_v031_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_accel_252d_3d_v032_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_accel_21d_3d_v033_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_accel_63d_3d_v034_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_accel_126d_3d_v035_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_accel_252d_3d_v036_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_accel_21d_3d_v037_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_accel_63d_3d_v038_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_accel_126d_3d_v039_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_accel_252d_3d_v040_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_accel_21d_3d_v041_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_accel_63d_3d_v042_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_accel_126d_3d_v043_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_accel_252d_3d_v044_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_accel_21d_3d_v045_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_accel_63d_3d_v046_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_accel_126d_3d_v047_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_accel_252d_3d_v048_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_accel_21d_3d_v049_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_accel_63d_3d_v050_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_accel_126d_3d_v051_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_accel_252d_3d_v052_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_slopez_21d_z126_3d_v053_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_slopez_63d_z252_3d_v054_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_slopez_126d_z252_3d_v055_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_slopez_252d_z504_3d_v056_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_slopez_21d_z126_3d_v057_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_slopez_63d_z252_3d_v058_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_slopez_126d_z252_3d_v059_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_slopez_252d_z504_3d_v060_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_slopez_21d_z126_3d_v061_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_slopez_63d_z252_3d_v062_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_slopez_126d_z252_3d_v063_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_slopez_252d_z504_3d_v064_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_slopez_21d_z126_3d_v065_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_slopez_63d_z252_3d_v066_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_slopez_126d_z252_3d_v067_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_slopez_252d_z504_3d_v068_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_slopez_21d_z126_3d_v069_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_slopez_63d_z252_3d_v070_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_slopez_126d_z252_3d_v071_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_slopez_252d_z504_3d_v072_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_slopez_21d_z126_3d_v073_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_slopez_63d_z252_3d_v074_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_slopez_126d_z252_3d_v075_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_slopez_252d_z504_3d_v076_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_slopez_21d_z126_3d_v077_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_slopez_63d_z252_3d_v078_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_slopez_126d_z252_3d_v079_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_slopez_252d_z504_3d_v080_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_slopez_21d_z126_3d_v081_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_slopez_63d_z252_3d_v082_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_slopez_126d_z252_3d_v083_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_slopez_252d_z504_3d_v084_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_slopez_21d_z126_3d_v085_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_slopez_63d_z252_3d_v086_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_slopez_126d_z252_3d_v087_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_slopez_252d_z504_3d_v088_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_slopez_21d_z126_3d_v089_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_slopez_63d_z252_3d_v090_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_slopez_126d_z252_3d_v091_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_slopez_252d_z504_3d_v092_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_slopez_21d_z126_3d_v093_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_slopez_63d_z252_3d_v094_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_slopez_126d_z252_3d_v095_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_slopez_252d_z504_3d_v096_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_slopez_21d_z126_3d_v097_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_slopez_63d_z252_3d_v098_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_slopez_126d_z252_3d_v099_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_slopez_252d_z504_3d_v100_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_slopez_21d_z126_3d_v101_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_slopez_63d_z252_3d_v102_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_slopez_126d_z252_3d_v103_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_slopez_252d_z504_3d_v104_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_jerk_21d_3d_v105_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_jerk_63d_3d_v106_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_jerk_126d_3d_v107_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_jerk_21d_3d_v108_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_jerk_63d_3d_v109_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_jerk_126d_3d_v110_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_jerk_21d_3d_v111_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_jerk_63d_3d_v112_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_jerk_126d_3d_v113_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_jerk_21d_3d_v114_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_jerk_63d_3d_v115_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_jerk_126d_3d_v116_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_jerk_21d_3d_v117_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_jerk_63d_3d_v118_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_jerk_126d_3d_v119_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_jerk_21d_3d_v120_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_jerk_63d_3d_v121_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_jerk_126d_3d_v122_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_jerk_21d_3d_v123_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_jerk_63d_3d_v124_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_jerk_126d_3d_v125_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_jerk_21d_3d_v126_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_jerk_63d_3d_v127_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_jerk_126d_3d_v128_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_jerk_21d_3d_v129_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_jerk_63d_3d_v130_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_jerk_126d_3d_v131_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_jerk_21d_3d_v132_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_jerk_63d_3d_v133_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_jerk_126d_3d_v134_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_jerk_21d_3d_v135_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_jerk_63d_3d_v136_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_jerk_126d_3d_v137_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_jerk_21d_3d_v138_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_jerk_63d_3d_v139_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_jerk_126d_3d_v140_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_jerk_21d_3d_v141_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_jerk_63d_3d_v142_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_jerk_126d_3d_v143_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_to_rev smoothed over 252d
def f018rdi_f018_rnd_intensity_rnd_to_rev_smoothaccel_63d_sm252_3d_v144_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_to_rev smoothed over 504d
def f018rdi_f018_rnd_intensity_rnd_to_rev_smoothaccel_252d_sm504_3d_v145_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_to_opex smoothed over 252d
def f018rdi_f018_rnd_intensity_rnd_to_opex_smoothaccel_63d_sm252_3d_v146_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_to_opex smoothed over 504d
def f018rdi_f018_rnd_intensity_rnd_to_opex_smoothaccel_252d_sm504_3d_v147_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_to_gp smoothed over 252d
def f018rdi_f018_rnd_intensity_rnd_to_gp_smoothaccel_63d_sm252_3d_v148_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_to_gp smoothed over 504d
def f018rdi_f018_rnd_intensity_rnd_to_gp_smoothaccel_252d_sm504_3d_v149_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_to_cash_balance smoothed over 252d
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_smoothaccel_63d_sm252_3d_v150_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_to_cash_balance smoothed over 504d
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_smoothaccel_252d_sm504_3d_v151_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_to_asset smoothed over 252d
def f018rdi_f018_rnd_intensity_rnd_to_asset_smoothaccel_63d_sm252_3d_v152_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_to_asset smoothed over 504d
def f018rdi_f018_rnd_intensity_rnd_to_asset_smoothaccel_252d_sm504_3d_v153_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_to_ebit smoothed over 252d
def f018rdi_f018_rnd_intensity_rnd_to_ebit_smoothaccel_63d_sm252_3d_v154_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_to_ebit smoothed over 504d
def f018rdi_f018_rnd_intensity_rnd_to_ebit_smoothaccel_252d_sm504_3d_v155_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_share_of_loss smoothed over 252d
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_smoothaccel_63d_sm252_3d_v156_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_share_of_loss smoothed over 504d
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_smoothaccel_252d_sm504_3d_v157_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_to_rev_peer_sector_dist smoothed over 252d
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_smoothaccel_63d_sm252_3d_v158_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_to_rev_peer_sector_dist smoothed over 504d
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_smoothaccel_252d_sm504_3d_v159_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_to_rev_peer_sector_z smoothed over 252d
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_smoothaccel_63d_sm252_3d_v160_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_to_rev_peer_sector_z smoothed over 504d
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_smoothaccel_252d_sm504_3d_v161_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_to_rev_peer_industry_dist smoothed over 252d
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_smoothaccel_63d_sm252_3d_v162_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_to_rev_peer_industry_dist smoothed over 504d
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_smoothaccel_252d_sm504_3d_v163_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_to_rev_peer_mcap_bucket_dist smoothed over 252d
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_smoothaccel_63d_sm252_3d_v164_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_to_rev_peer_mcap_bucket_dist smoothed over 504d
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_smoothaccel_252d_sm504_3d_v165_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_to_rev_peer_sector_pctile smoothed over 252d
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_smoothaccel_63d_sm252_3d_v166_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_to_rev_peer_sector_pctile smoothed over 504d
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_smoothaccel_252d_sm504_3d_v167_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_to_rev_peer_industry_pctile smoothed over 252d
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_smoothaccel_63d_sm252_3d_v168_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_to_rev_peer_industry_pctile smoothed over 504d
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_smoothaccel_252d_sm504_3d_v169_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_accelz_21d_z252_3d_v170_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_accelz_63d_z504_3d_v171_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_accelz_21d_z252_3d_v172_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_accelz_63d_z504_3d_v173_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_accelz_21d_z252_3d_v174_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_accelz_63d_z504_3d_v175_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_accelz_21d_z252_3d_v176_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_accelz_63d_z504_3d_v177_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_accelz_21d_z252_3d_v178_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_accelz_63d_z504_3d_v179_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_accelz_21d_z252_3d_v180_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_accelz_63d_z504_3d_v181_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_accelz_21d_z252_3d_v182_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_accelz_63d_z504_3d_v183_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_accelz_21d_z252_3d_v184_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_accelz_63d_z504_3d_v185_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_accelz_21d_z252_3d_v186_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_accelz_63d_z504_3d_v187_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_accelz_21d_z252_3d_v188_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_accelz_63d_z504_3d_v189_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_accelz_21d_z252_3d_v190_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_accelz_63d_z504_3d_v191_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_accelz_21d_z252_3d_v192_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_accelz_63d_z504_3d_v193_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_accelz_21d_z252_3d_v194_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_accelz_63d_z504_3d_v195_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rnd_to_rev (raw count, no price scaling)
def f018rdi_f018_rnd_intensity_rnd_to_rev_signflip_63d_3d_v196_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rnd_to_rev (raw count, no price scaling)
def f018rdi_f018_rnd_intensity_rnd_to_rev_signflip_252d_3d_v197_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rnd_to_opex (raw count, no price scaling)
def f018rdi_f018_rnd_intensity_rnd_to_opex_signflip_63d_3d_v198_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rnd_to_opex (raw count, no price scaling)
def f018rdi_f018_rnd_intensity_rnd_to_opex_signflip_252d_3d_v199_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rnd_to_gp (raw count, no price scaling)
def f018rdi_f018_rnd_intensity_rnd_to_gp_signflip_63d_3d_v200_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

