
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_21d_base_v001_signal(invturn, closeadj):
    result = _mean(invturn, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_63d_base_v002_signal(invturn, closeadj):
    result = _mean(invturn, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_126d_base_v003_signal(invturn, closeadj):
    result = _mean(invturn, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_252d_base_v004_signal(invturn, closeadj):
    result = _mean(invturn, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_504d_base_v005_signal(invturn, closeadj):
    result = _mean(invturn, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_log_21d_base_v006_signal(invturn, closeadj):
    result = _mean(_log(invturn), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_log_63d_base_v007_signal(invturn, closeadj):
    result = _mean(_log(invturn), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_log_126d_base_v008_signal(invturn, closeadj):
    result = _mean(_log(invturn), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_log_252d_base_v009_signal(invturn, closeadj):
    result = _mean(_log(invturn), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_log_504d_base_v010_signal(invturn, closeadj):
    result = _mean(_log(invturn), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_z_21d_base_v011_signal(invturn):
    result = _z(invturn, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_z_63d_base_v012_signal(invturn):
    result = _z(invturn, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_z_126d_base_v013_signal(invturn):
    result = _z(invturn, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_z_252d_base_v014_signal(invturn):
    result = _z(invturn, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_z_504d_base_v015_signal(invturn):
    result = _z(invturn, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_pct_21d_base_v016_signal(invturn):
    result = _pct_change(invturn, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_pct_63d_base_v017_signal(invturn):
    result = _pct_change(invturn, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_pct_126d_base_v018_signal(invturn):
    result = _pct_change(invturn, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_pct_252d_base_v019_signal(invturn):
    result = _pct_change(invturn, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_pct_504d_base_v020_signal(invturn):
    result = _pct_change(invturn, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_21d_base_v021_signal(invturn, sharesbas, closeadj):
    ps = _safe_div(invturn, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_63d_base_v022_signal(invturn, sharesbas, closeadj):
    ps = _safe_div(invturn, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_126d_base_v023_signal(invturn, sharesbas, closeadj):
    ps = _safe_div(invturn, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_252d_base_v024_signal(invturn, sharesbas, closeadj):
    ps = _safe_div(invturn, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_504d_base_v025_signal(invturn, sharesbas, closeadj):
    ps = _safe_div(invturn, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of invturn to inventory
def gm_f59_biotech_f59_inventory_turnover_ratio_ratio_inventory_21d_base_v026_signal(invturn, inventory):
    ratio = _safe_div(invturn, inventory)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of invturn to inventory
def gm_f59_biotech_f59_inventory_turnover_ratio_ratio_inventory_63d_base_v027_signal(invturn, inventory):
    ratio = _safe_div(invturn, inventory)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of invturn to inventory
def gm_f59_biotech_f59_inventory_turnover_ratio_ratio_inventory_126d_base_v028_signal(invturn, inventory):
    ratio = _safe_div(invturn, inventory)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of invturn to inventory
def gm_f59_biotech_f59_inventory_turnover_ratio_ratio_inventory_252d_base_v029_signal(invturn, inventory):
    ratio = _safe_div(invturn, inventory)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of invturn to inventory
def gm_f59_biotech_f59_inventory_turnover_ratio_ratio_inventory_504d_base_v030_signal(invturn, inventory):
    ratio = _safe_div(invturn, inventory)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d invturn scaled by assets
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_21d_base_v031_signal(invturn, assets):
    scaled = _safe_div(invturn, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d invturn scaled by assets
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_63d_base_v032_signal(invturn, assets):
    scaled = _safe_div(invturn, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d invturn scaled by assets
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_126d_base_v033_signal(invturn, assets):
    scaled = _safe_div(invturn, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d invturn scaled by assets
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_252d_base_v034_signal(invturn, assets):
    scaled = _safe_div(invturn, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d invturn scaled by assets
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_504d_base_v035_signal(invturn, assets):
    scaled = _safe_div(invturn, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d invturn scaled by marketcap
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_21d_base_v036_signal(invturn, marketcap):
    scaled = _safe_div(invturn, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d invturn scaled by marketcap
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_63d_base_v037_signal(invturn, marketcap):
    scaled = _safe_div(invturn, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d invturn scaled by marketcap
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_126d_base_v038_signal(invturn, marketcap):
    scaled = _safe_div(invturn, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d invturn scaled by marketcap
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_252d_base_v039_signal(invturn, marketcap):
    scaled = _safe_div(invturn, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d invturn scaled by marketcap
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_504d_base_v040_signal(invturn, marketcap):
    scaled = _safe_div(invturn, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_21d_base_v041_signal(invturn):
    low = invturn.rolling(21).min()
    result = _safe_div(invturn - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_63d_base_v042_signal(invturn):
    low = invturn.rolling(63).min()
    result = _safe_div(invturn - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_126d_base_v043_signal(invturn):
    low = invturn.rolling(126).min()
    result = _safe_div(invturn - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_252d_base_v044_signal(invturn):
    low = invturn.rolling(252).min()
    result = _safe_div(invturn - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_504d_base_v045_signal(invturn):
    low = invturn.rolling(504).min()
    result = _safe_div(invturn - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_21d_base_v046_signal(invturn):
    high = invturn.rolling(21).max()
    result = _safe_div(high - invturn, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_63d_base_v047_signal(invturn):
    high = invturn.rolling(63).max()
    result = _safe_div(high - invturn, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_126d_base_v048_signal(invturn):
    high = invturn.rolling(126).max()
    result = _safe_div(high - invturn, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_252d_base_v049_signal(invturn):
    high = invturn.rolling(252).max()
    result = _safe_div(high - invturn, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_504d_base_v050_signal(invturn):
    high = invturn.rolling(504).max()
    result = _safe_div(high - invturn, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_21d_base_v051_signal(invturn):
    m1 = _mean(invturn, 21)
    m2 = _mean(invturn, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_63d_base_v052_signal(invturn):
    m1 = _mean(invturn, 63)
    m2 = _mean(invturn, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_126d_base_v053_signal(invturn):
    m1 = _mean(invturn, 126)
    m2 = _mean(invturn, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_252d_base_v054_signal(invturn):
    m1 = _mean(invturn, 252)
    m2 = _mean(invturn, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_504d_base_v055_signal(invturn):
    m1 = _mean(invturn, 504)
    m2 = _mean(invturn, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_skew_21d_base_v056_signal(invturn):
    result = _skew(invturn, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_skew_63d_base_v057_signal(invturn):
    result = _skew(invturn, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_skew_126d_base_v058_signal(invturn):
    result = _skew(invturn, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_skew_252d_base_v059_signal(invturn):
    result = _skew(invturn, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_skew_504d_base_v060_signal(invturn):
    result = _skew(invturn, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_kurt_21d_base_v061_signal(invturn):
    result = _kurt(invturn, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_kurt_63d_base_v062_signal(invturn):
    result = _kurt(invturn, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_kurt_126d_base_v063_signal(invturn):
    result = _kurt(invturn, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_kurt_252d_base_v064_signal(invturn):
    result = _kurt(invturn, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_kurt_504d_base_v065_signal(invturn):
    result = _kurt(invturn, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_rank_21d_base_v066_signal(invturn, closeadj):
    result = _rank(invturn, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_rank_63d_base_v067_signal(invturn, closeadj):
    result = _rank(invturn, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_rank_126d_base_v068_signal(invturn, closeadj):
    result = _rank(invturn, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_rank_252d_base_v069_signal(invturn, closeadj):
    result = _rank(invturn, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_rank_504d_base_v070_signal(invturn, closeadj):
    result = _rank(invturn, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autoinvturnr of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_autocorr_21d_base_v071_signal(invturn):
    result = _autocorr(invturn, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autoinvturnr of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_autocorr_63d_base_v072_signal(invturn):
    result = _autocorr(invturn, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autoinvturnr of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_autocorr_126d_base_v073_signal(invturn):
    result = _autocorr(invturn, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autoinvturnr of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_autocorr_252d_base_v074_signal(invturn):
    result = _autocorr(invturn, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autoinvturnr of invturn
def gm_f59_biotech_f59_inventory_turnover_ratio_autocorr_504d_base_v075_signal(invturn):
    result = _autocorr(invturn, 504)
    return result.replace([np.inf, -np.inf], np.nan)

