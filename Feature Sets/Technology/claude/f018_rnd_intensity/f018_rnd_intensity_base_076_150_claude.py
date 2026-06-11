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
def _f018_rnd_to_rev(rnd, revenue):
    return rnd / revenue.abs().replace(0, np.nan)


def _f018_rnd_to_opex(rnd, opex):
    return rnd / opex.abs().replace(0, np.nan)


# 63d z-score of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_z_63d_base_v076_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_z_126d_base_v077_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_z_252d_base_v078_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_z_504d_base_v079_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_z_63d_base_v080_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_z_126d_base_v081_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_z_252d_base_v082_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_z_504d_base_v083_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_z_63d_base_v084_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_z_126d_base_v085_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_z_252d_base_v086_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_z_504d_base_v087_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_z_63d_base_v088_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_z_126d_base_v089_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_z_252d_base_v090_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_z_504d_base_v091_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_z_63d_base_v092_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_z_126d_base_v093_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_z_252d_base_v094_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_z_504d_base_v095_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_z_63d_base_v096_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_z_126d_base_v097_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_z_252d_base_v098_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_z_504d_base_v099_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_z_63d_base_v100_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_z_126d_base_v101_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_z_252d_base_v102_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_z_504d_base_v103_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_z_63d_base_v104_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_z_126d_base_v105_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_z_252d_base_v106_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_z_504d_base_v107_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_z_63d_base_v108_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_z_126d_base_v109_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_z_252d_base_v110_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_z_504d_base_v111_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_z_63d_base_v112_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_z_126d_base_v113_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_z_252d_base_v114_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_z_504d_base_v115_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_z_63d_base_v116_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_z_126d_base_v117_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_z_252d_base_v118_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_z_504d_base_v119_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_z_63d_base_v120_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_z_126d_base_v121_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_z_252d_base_v122_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_z_504d_base_v123_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_z_63d_base_v124_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_z_126d_base_v125_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_z_252d_base_v126_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_z_504d_base_v127_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_distmax_252d_base_v128_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_distmax_504d_base_v129_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_distmax_252d_base_v130_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_distmax_504d_base_v131_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_distmax_252d_base_v132_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_distmax_504d_base_v133_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_distmax_252d_base_v134_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_distmax_504d_base_v135_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_distmax_252d_base_v136_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_distmax_504d_base_v137_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_distmax_252d_base_v138_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_distmax_504d_base_v139_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_distmax_252d_base_v140_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_distmax_504d_base_v141_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_distmax_252d_base_v142_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_distmax_504d_base_v143_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_distmax_252d_base_v144_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rnd_to_rev_peer_sector_z
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_z_distmax_504d_base_v145_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_distmax_252d_base_v146_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rnd_to_rev_peer_industry_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_distmax_504d_base_v147_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_distmax_252d_base_v148_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rnd_to_rev_peer_mcap_bucket_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_distmax_504d_base_v149_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_distmax_252d_base_v150_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rnd_to_rev_peer_sector_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_distmax_504d_base_v151_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_distmax_252d_base_v152_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rnd_to_rev_peer_industry_pctile
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_distmax_504d_base_v153_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_distmed_126d_base_v154_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_distmed_252d_base_v155_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rnd_to_rev
def f018rdi_f018_rnd_intensity_rnd_to_rev_distmed_504d_base_v156_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_distmed_126d_base_v157_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_distmed_252d_base_v158_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rnd_to_opex
def f018rdi_f018_rnd_intensity_rnd_to_opex_distmed_504d_base_v159_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_distmed_126d_base_v160_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_distmed_252d_base_v161_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rnd_to_gp
def f018rdi_f018_rnd_intensity_rnd_to_gp_distmed_504d_base_v162_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_distmed_126d_base_v163_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_distmed_252d_base_v164_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rnd_to_cash_balance
def f018rdi_f018_rnd_intensity_rnd_to_cash_balance_distmed_504d_base_v165_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_distmed_126d_base_v166_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_distmed_252d_base_v167_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rnd_to_asset
def f018rdi_f018_rnd_intensity_rnd_to_asset_distmed_504d_base_v168_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_distmed_126d_base_v169_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_distmed_252d_base_v170_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rnd_to_ebit
def f018rdi_f018_rnd_intensity_rnd_to_ebit_distmed_504d_base_v171_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_distmed_126d_base_v172_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_distmed_252d_base_v173_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rnd_share_of_loss
def f018rdi_f018_rnd_intensity_rnd_share_of_loss_distmed_504d_base_v174_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rnd_to_rev_peer_sector_dist
def f018rdi_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_distmed_126d_base_v175_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

