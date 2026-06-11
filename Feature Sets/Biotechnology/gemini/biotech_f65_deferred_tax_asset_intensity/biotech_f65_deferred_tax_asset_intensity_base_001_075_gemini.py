
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_21d_base_v001_signal(taxassets, closeadj):
    result = _mean(taxassets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_63d_base_v002_signal(taxassets, closeadj):
    result = _mean(taxassets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_126d_base_v003_signal(taxassets, closeadj):
    result = _mean(taxassets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_252d_base_v004_signal(taxassets, closeadj):
    result = _mean(taxassets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_504d_base_v005_signal(taxassets, closeadj):
    result = _mean(taxassets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_21d_base_v006_signal(taxassets, closeadj):
    result = _mean(_log(taxassets), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_63d_base_v007_signal(taxassets, closeadj):
    result = _mean(_log(taxassets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_126d_base_v008_signal(taxassets, closeadj):
    result = _mean(_log(taxassets), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_252d_base_v009_signal(taxassets, closeadj):
    result = _mean(_log(taxassets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_504d_base_v010_signal(taxassets, closeadj):
    result = _mean(_log(taxassets), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_21d_base_v011_signal(taxassets):
    result = _z(taxassets, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_63d_base_v012_signal(taxassets):
    result = _z(taxassets, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_126d_base_v013_signal(taxassets):
    result = _z(taxassets, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_252d_base_v014_signal(taxassets):
    result = _z(taxassets, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_504d_base_v015_signal(taxassets):
    result = _z(taxassets, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_pct_21d_base_v016_signal(taxassets):
    result = _pct_change(taxassets, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_pct_63d_base_v017_signal(taxassets):
    result = _pct_change(taxassets, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_pct_126d_base_v018_signal(taxassets):
    result = _pct_change(taxassets, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_pct_252d_base_v019_signal(taxassets):
    result = _pct_change(taxassets, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_pct_504d_base_v020_signal(taxassets):
    result = _pct_change(taxassets, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_21d_base_v021_signal(taxassets, sharesbas, closeadj):
    ps = _safe_div(taxassets, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_63d_base_v022_signal(taxassets, sharesbas, closeadj):
    ps = _safe_div(taxassets, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_126d_base_v023_signal(taxassets, sharesbas, closeadj):
    ps = _safe_div(taxassets, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_252d_base_v024_signal(taxassets, sharesbas, closeadj):
    ps = _safe_div(taxassets, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_504d_base_v025_signal(taxassets, sharesbas, closeadj):
    ps = _safe_div(taxassets, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of taxassets to assets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ratio_assets_21d_base_v026_signal(taxassets, assets):
    ratio = _safe_div(taxassets, assets)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of taxassets to assets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ratio_assets_63d_base_v027_signal(taxassets, assets):
    ratio = _safe_div(taxassets, assets)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of taxassets to assets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ratio_assets_126d_base_v028_signal(taxassets, assets):
    ratio = _safe_div(taxassets, assets)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of taxassets to assets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ratio_assets_252d_base_v029_signal(taxassets, assets):
    ratio = _safe_div(taxassets, assets)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of taxassets to assets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ratio_assets_504d_base_v030_signal(taxassets, assets):
    ratio = _safe_div(taxassets, assets)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d taxassets scaled by assets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_21d_base_v031_signal(taxassets, assets):
    scaled = _safe_div(taxassets, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d taxassets scaled by assets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_63d_base_v032_signal(taxassets, assets):
    scaled = _safe_div(taxassets, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d taxassets scaled by assets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_126d_base_v033_signal(taxassets, assets):
    scaled = _safe_div(taxassets, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d taxassets scaled by assets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_252d_base_v034_signal(taxassets, assets):
    scaled = _safe_div(taxassets, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d taxassets scaled by assets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_504d_base_v035_signal(taxassets, assets):
    scaled = _safe_div(taxassets, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d taxassets scaled by marketcap
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_21d_base_v036_signal(taxassets, marketcap):
    scaled = _safe_div(taxassets, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d taxassets scaled by marketcap
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_63d_base_v037_signal(taxassets, marketcap):
    scaled = _safe_div(taxassets, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d taxassets scaled by marketcap
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_126d_base_v038_signal(taxassets, marketcap):
    scaled = _safe_div(taxassets, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d taxassets scaled by marketcap
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_252d_base_v039_signal(taxassets, marketcap):
    scaled = _safe_div(taxassets, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d taxassets scaled by marketcap
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_504d_base_v040_signal(taxassets, marketcap):
    scaled = _safe_div(taxassets, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_21d_base_v041_signal(taxassets):
    low = taxassets.rolling(21).min()
    result = _safe_div(taxassets - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_63d_base_v042_signal(taxassets):
    low = taxassets.rolling(63).min()
    result = _safe_div(taxassets - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_126d_base_v043_signal(taxassets):
    low = taxassets.rolling(126).min()
    result = _safe_div(taxassets - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_252d_base_v044_signal(taxassets):
    low = taxassets.rolling(252).min()
    result = _safe_div(taxassets - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_504d_base_v045_signal(taxassets):
    low = taxassets.rolling(504).min()
    result = _safe_div(taxassets - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_21d_base_v046_signal(taxassets):
    high = taxassets.rolling(21).max()
    result = _safe_div(high - taxassets, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_63d_base_v047_signal(taxassets):
    high = taxassets.rolling(63).max()
    result = _safe_div(high - taxassets, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_126d_base_v048_signal(taxassets):
    high = taxassets.rolling(126).max()
    result = _safe_div(high - taxassets, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_252d_base_v049_signal(taxassets):
    high = taxassets.rolling(252).max()
    result = _safe_div(high - taxassets, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_504d_base_v050_signal(taxassets):
    high = taxassets.rolling(504).max()
    result = _safe_div(high - taxassets, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_21d_base_v051_signal(taxassets):
    m1 = _mean(taxassets, 21)
    m2 = _mean(taxassets, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_63d_base_v052_signal(taxassets):
    m1 = _mean(taxassets, 63)
    m2 = _mean(taxassets, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_126d_base_v053_signal(taxassets):
    m1 = _mean(taxassets, 126)
    m2 = _mean(taxassets, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_252d_base_v054_signal(taxassets):
    m1 = _mean(taxassets, 252)
    m2 = _mean(taxassets, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_504d_base_v055_signal(taxassets):
    m1 = _mean(taxassets, 504)
    m2 = _mean(taxassets, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_skew_21d_base_v056_signal(taxassets):
    result = _skew(taxassets, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_skew_63d_base_v057_signal(taxassets):
    result = _skew(taxassets, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_skew_126d_base_v058_signal(taxassets):
    result = _skew(taxassets, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_skew_252d_base_v059_signal(taxassets):
    result = _skew(taxassets, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_skew_504d_base_v060_signal(taxassets):
    result = _skew(taxassets, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_kurt_21d_base_v061_signal(taxassets):
    result = _kurt(taxassets, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_kurt_63d_base_v062_signal(taxassets):
    result = _kurt(taxassets, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_kurt_126d_base_v063_signal(taxassets):
    result = _kurt(taxassets, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_kurt_252d_base_v064_signal(taxassets):
    result = _kurt(taxassets, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_kurt_504d_base_v065_signal(taxassets):
    result = _kurt(taxassets, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_rank_21d_base_v066_signal(taxassets, closeadj):
    result = _rank(taxassets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_rank_63d_base_v067_signal(taxassets, closeadj):
    result = _rank(taxassets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_rank_126d_base_v068_signal(taxassets, closeadj):
    result = _rank(taxassets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_rank_252d_base_v069_signal(taxassets, closeadj):
    result = _rank(taxassets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_rank_504d_base_v070_signal(taxassets, closeadj):
    result = _rank(taxassets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_autocorr_21d_base_v071_signal(taxassets):
    result = _autocorr(taxassets, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_autocorr_63d_base_v072_signal(taxassets):
    result = _autocorr(taxassets, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_autocorr_126d_base_v073_signal(taxassets):
    result = _autocorr(taxassets, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_autocorr_252d_base_v074_signal(taxassets):
    result = _autocorr(taxassets, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_autocorr_504d_base_v075_signal(taxassets):
    result = _autocorr(taxassets, 504)
    return result.replace([np.inf, -np.inf], np.nan)

