
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed quick_ratio
def gm_f05_biotech_f05_quick_ratio_acid_test_raw_21d_base_v001_signal(quickratio, inventory, liabilitiesc, closeadj):
    qr = _safe_div(quickratio - inventory.fillna(0), liabilitiesc)
    result = _mean(qr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed quick_ratio
def gm_f05_biotech_f05_quick_ratio_acid_test_raw_63d_base_v002_signal(quickratio, inventory, liabilitiesc, closeadj):
    qr = _safe_div(quickratio - inventory.fillna(0), liabilitiesc)
    result = _mean(qr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed quick_ratio
def gm_f05_biotech_f05_quick_ratio_acid_test_raw_126d_base_v003_signal(quickratio, inventory, liabilitiesc, closeadj):
    qr = _safe_div(quickratio - inventory.fillna(0), liabilitiesc)
    result = _mean(qr, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed quick_ratio
def gm_f05_biotech_f05_quick_ratio_acid_test_raw_252d_base_v004_signal(quickratio, inventory, liabilitiesc, closeadj):
    qr = _safe_div(quickratio - inventory.fillna(0), liabilitiesc)
    result = _mean(qr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed quick_ratio
def gm_f05_biotech_f05_quick_ratio_acid_test_raw_504d_base_v005_signal(quickratio, inventory, liabilitiesc, closeadj):
    qr = _safe_div(quickratio - inventory.fillna(0), liabilitiesc)
    result = _mean(qr, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_log_21d_base_v006_signal(quickratio, closeadj):
    result = _mean(_log(quickratio), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_log_63d_base_v007_signal(quickratio, closeadj):
    result = _mean(_log(quickratio), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_log_126d_base_v008_signal(quickratio, closeadj):
    result = _mean(_log(quickratio), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_log_252d_base_v009_signal(quickratio, closeadj):
    result = _mean(_log(quickratio), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_log_504d_base_v010_signal(quickratio, closeadj):
    result = _mean(_log(quickratio), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_z_21d_base_v011_signal(quickratio):
    result = _z(quickratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_z_63d_base_v012_signal(quickratio):
    result = _z(quickratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_z_126d_base_v013_signal(quickratio):
    result = _z(quickratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_z_252d_base_v014_signal(quickratio):
    result = _z(quickratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_z_504d_base_v015_signal(quickratio):
    result = _z(quickratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_pct_21d_base_v016_signal(quickratio):
    result = _pct_change(quickratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_pct_63d_base_v017_signal(quickratio):
    result = _pct_change(quickratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_pct_126d_base_v018_signal(quickratio):
    result = _pct_change(quickratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_pct_252d_base_v019_signal(quickratio):
    result = _pct_change(quickratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_pct_504d_base_v020_signal(quickratio):
    result = _pct_change(quickratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_ps_21d_base_v021_signal(quickratio, sharesbas, closeadj):
    ps = _safe_div(quickratio, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_ps_63d_base_v022_signal(quickratio, sharesbas, closeadj):
    ps = _safe_div(quickratio, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_ps_126d_base_v023_signal(quickratio, sharesbas, closeadj):
    ps = _safe_div(quickratio, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_ps_252d_base_v024_signal(quickratio, sharesbas, closeadj):
    ps = _safe_div(quickratio, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_ps_504d_base_v025_signal(quickratio, sharesbas, closeadj):
    ps = _safe_div(quickratio, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of quickratio to inventory
def gm_f05_biotech_f05_quick_ratio_acid_test_ratio_inventory_21d_base_v026_signal(quickratio, inventory):
    ratio = _safe_div(quickratio, inventory)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of quickratio to inventory
def gm_f05_biotech_f05_quick_ratio_acid_test_ratio_inventory_63d_base_v027_signal(quickratio, inventory):
    ratio = _safe_div(quickratio, inventory)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of quickratio to inventory
def gm_f05_biotech_f05_quick_ratio_acid_test_ratio_inventory_126d_base_v028_signal(quickratio, inventory):
    ratio = _safe_div(quickratio, inventory)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of quickratio to inventory
def gm_f05_biotech_f05_quick_ratio_acid_test_ratio_inventory_252d_base_v029_signal(quickratio, inventory):
    ratio = _safe_div(quickratio, inventory)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of quickratio to inventory
def gm_f05_biotech_f05_quick_ratio_acid_test_ratio_inventory_504d_base_v030_signal(quickratio, inventory):
    ratio = _safe_div(quickratio, inventory)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of quickratio to liabilitiesc
def gm_f05_biotech_f05_quick_ratio_acid_test_ratio_liabilitiesc_21d_base_v031_signal(quickratio, liabilitiesc):
    ratio = _safe_div(quickratio, liabilitiesc)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of quickratio to liabilitiesc
def gm_f05_biotech_f05_quick_ratio_acid_test_ratio_liabilitiesc_63d_base_v032_signal(quickratio, liabilitiesc):
    ratio = _safe_div(quickratio, liabilitiesc)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of quickratio to liabilitiesc
def gm_f05_biotech_f05_quick_ratio_acid_test_ratio_liabilitiesc_126d_base_v033_signal(quickratio, liabilitiesc):
    ratio = _safe_div(quickratio, liabilitiesc)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of quickratio to liabilitiesc
def gm_f05_biotech_f05_quick_ratio_acid_test_ratio_liabilitiesc_252d_base_v034_signal(quickratio, liabilitiesc):
    ratio = _safe_div(quickratio, liabilitiesc)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of quickratio to liabilitiesc
def gm_f05_biotech_f05_quick_ratio_acid_test_ratio_liabilitiesc_504d_base_v035_signal(quickratio, liabilitiesc):
    ratio = _safe_div(quickratio, liabilitiesc)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d quickratio scaled by assets
def gm_f05_biotech_f05_quick_ratio_acid_test_asset_scaled_21d_base_v036_signal(quickratio, assets):
    scaled = _safe_div(quickratio, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d quickratio scaled by assets
def gm_f05_biotech_f05_quick_ratio_acid_test_asset_scaled_63d_base_v037_signal(quickratio, assets):
    scaled = _safe_div(quickratio, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d quickratio scaled by assets
def gm_f05_biotech_f05_quick_ratio_acid_test_asset_scaled_126d_base_v038_signal(quickratio, assets):
    scaled = _safe_div(quickratio, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d quickratio scaled by assets
def gm_f05_biotech_f05_quick_ratio_acid_test_asset_scaled_252d_base_v039_signal(quickratio, assets):
    scaled = _safe_div(quickratio, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d quickratio scaled by assets
def gm_f05_biotech_f05_quick_ratio_acid_test_asset_scaled_504d_base_v040_signal(quickratio, assets):
    scaled = _safe_div(quickratio, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d quickratio scaled by marketcap
def gm_f05_biotech_f05_quick_ratio_acid_test_mcap_scaled_21d_base_v041_signal(quickratio, marketcap):
    scaled = _safe_div(quickratio, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d quickratio scaled by marketcap
def gm_f05_biotech_f05_quick_ratio_acid_test_mcap_scaled_63d_base_v042_signal(quickratio, marketcap):
    scaled = _safe_div(quickratio, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d quickratio scaled by marketcap
def gm_f05_biotech_f05_quick_ratio_acid_test_mcap_scaled_126d_base_v043_signal(quickratio, marketcap):
    scaled = _safe_div(quickratio, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d quickratio scaled by marketcap
def gm_f05_biotech_f05_quick_ratio_acid_test_mcap_scaled_252d_base_v044_signal(quickratio, marketcap):
    scaled = _safe_div(quickratio, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d quickratio scaled by marketcap
def gm_f05_biotech_f05_quick_ratio_acid_test_mcap_scaled_504d_base_v045_signal(quickratio, marketcap):
    scaled = _safe_div(quickratio, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_dist_low_21d_base_v046_signal(quickratio):
    low = quickratio.rolling(21).min()
    result = _safe_div(quickratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_dist_low_63d_base_v047_signal(quickratio):
    low = quickratio.rolling(63).min()
    result = _safe_div(quickratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_dist_low_126d_base_v048_signal(quickratio):
    low = quickratio.rolling(126).min()
    result = _safe_div(quickratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_dist_low_252d_base_v049_signal(quickratio):
    low = quickratio.rolling(252).min()
    result = _safe_div(quickratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_dist_low_504d_base_v050_signal(quickratio):
    low = quickratio.rolling(504).min()
    result = _safe_div(quickratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_dist_high_21d_base_v051_signal(quickratio):
    high = quickratio.rolling(21).max()
    result = _safe_div(high - quickratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_dist_high_63d_base_v052_signal(quickratio):
    high = quickratio.rolling(63).max()
    result = _safe_div(high - quickratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_dist_high_126d_base_v053_signal(quickratio):
    high = quickratio.rolling(126).max()
    result = _safe_div(high - quickratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_dist_high_252d_base_v054_signal(quickratio):
    high = quickratio.rolling(252).max()
    result = _safe_div(high - quickratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_dist_high_504d_base_v055_signal(quickratio):
    high = quickratio.rolling(504).max()
    result = _safe_div(high - quickratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_mom_21d_base_v056_signal(quickratio):
    m1 = _mean(quickratio, 21)
    m2 = _mean(quickratio, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_mom_63d_base_v057_signal(quickratio):
    m1 = _mean(quickratio, 63)
    m2 = _mean(quickratio, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_mom_126d_base_v058_signal(quickratio):
    m1 = _mean(quickratio, 126)
    m2 = _mean(quickratio, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_mom_252d_base_v059_signal(quickratio):
    m1 = _mean(quickratio, 252)
    m2 = _mean(quickratio, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_mom_504d_base_v060_signal(quickratio):
    m1 = _mean(quickratio, 504)
    m2 = _mean(quickratio, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_skew_21d_base_v061_signal(quickratio):
    result = _skew(quickratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_skew_63d_base_v062_signal(quickratio):
    result = _skew(quickratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_skew_126d_base_v063_signal(quickratio):
    result = _skew(quickratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_skew_252d_base_v064_signal(quickratio):
    result = _skew(quickratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_skew_504d_base_v065_signal(quickratio):
    result = _skew(quickratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_kurt_21d_base_v066_signal(quickratio):
    result = _kurt(quickratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_kurt_63d_base_v067_signal(quickratio):
    result = _kurt(quickratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_kurt_126d_base_v068_signal(quickratio):
    result = _kurt(quickratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_kurt_252d_base_v069_signal(quickratio):
    result = _kurt(quickratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_kurt_504d_base_v070_signal(quickratio):
    result = _kurt(quickratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_rank_21d_base_v071_signal(quickratio, closeadj):
    result = _rank(quickratio, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_rank_63d_base_v072_signal(quickratio, closeadj):
    result = _rank(quickratio, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_rank_126d_base_v073_signal(quickratio, closeadj):
    result = _rank(quickratio, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_rank_252d_base_v074_signal(quickratio, closeadj):
    result = _rank(quickratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of quickratio
def gm_f05_biotech_f05_quick_ratio_acid_test_rank_504d_base_v075_signal(quickratio, closeadj):
    result = _rank(quickratio, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

