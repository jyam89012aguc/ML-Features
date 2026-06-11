
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_21d_base_v001_signal(intangibles, closeadj):
    result = _mean(intangibles, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_63d_base_v002_signal(intangibles, closeadj):
    result = _mean(intangibles, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_126d_base_v003_signal(intangibles, closeadj):
    result = _mean(intangibles, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_252d_base_v004_signal(intangibles, closeadj):
    result = _mean(intangibles, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_504d_base_v005_signal(intangibles, closeadj):
    result = _mean(intangibles, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_21d_base_v006_signal(intangibles, closeadj):
    result = _mean(_log(intangibles), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_63d_base_v007_signal(intangibles, closeadj):
    result = _mean(_log(intangibles), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_126d_base_v008_signal(intangibles, closeadj):
    result = _mean(_log(intangibles), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_252d_base_v009_signal(intangibles, closeadj):
    result = _mean(_log(intangibles), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_504d_base_v010_signal(intangibles, closeadj):
    result = _mean(_log(intangibles), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_21d_base_v011_signal(intangibles):
    result = _z(intangibles, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_63d_base_v012_signal(intangibles):
    result = _z(intangibles, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_126d_base_v013_signal(intangibles):
    result = _z(intangibles, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_252d_base_v014_signal(intangibles):
    result = _z(intangibles, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_504d_base_v015_signal(intangibles):
    result = _z(intangibles, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_pct_21d_base_v016_signal(intangibles):
    result = _pct_change(intangibles, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_pct_63d_base_v017_signal(intangibles):
    result = _pct_change(intangibles, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_pct_126d_base_v018_signal(intangibles):
    result = _pct_change(intangibles, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_pct_252d_base_v019_signal(intangibles):
    result = _pct_change(intangibles, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_pct_504d_base_v020_signal(intangibles):
    result = _pct_change(intangibles, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_21d_base_v021_signal(intangibles, sharesbas, closeadj):
    ps = _safe_div(intangibles, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_63d_base_v022_signal(intangibles, sharesbas, closeadj):
    ps = _safe_div(intangibles, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_126d_base_v023_signal(intangibles, sharesbas, closeadj):
    ps = _safe_div(intangibles, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_252d_base_v024_signal(intangibles, sharesbas, closeadj):
    ps = _safe_div(intangibles, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_504d_base_v025_signal(intangibles, sharesbas, closeadj):
    ps = _safe_div(intangibles, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of intangibles to assets
def gm_f09_biotech_f09_intangible_asset_intensity_ratio_assets_21d_base_v026_signal(intangibles, assets):
    ratio = _safe_div(intangibles, assets)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of intangibles to assets
def gm_f09_biotech_f09_intangible_asset_intensity_ratio_assets_63d_base_v027_signal(intangibles, assets):
    ratio = _safe_div(intangibles, assets)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of intangibles to assets
def gm_f09_biotech_f09_intangible_asset_intensity_ratio_assets_126d_base_v028_signal(intangibles, assets):
    ratio = _safe_div(intangibles, assets)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of intangibles to assets
def gm_f09_biotech_f09_intangible_asset_intensity_ratio_assets_252d_base_v029_signal(intangibles, assets):
    ratio = _safe_div(intangibles, assets)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of intangibles to assets
def gm_f09_biotech_f09_intangible_asset_intensity_ratio_assets_504d_base_v030_signal(intangibles, assets):
    ratio = _safe_div(intangibles, assets)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d intangibles scaled by assets
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_21d_base_v031_signal(intangibles, assets):
    scaled = _safe_div(intangibles, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d intangibles scaled by assets
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_63d_base_v032_signal(intangibles, assets):
    scaled = _safe_div(intangibles, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d intangibles scaled by assets
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_126d_base_v033_signal(intangibles, assets):
    scaled = _safe_div(intangibles, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d intangibles scaled by assets
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_252d_base_v034_signal(intangibles, assets):
    scaled = _safe_div(intangibles, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d intangibles scaled by assets
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_504d_base_v035_signal(intangibles, assets):
    scaled = _safe_div(intangibles, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d intangibles scaled by marketcap
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_21d_base_v036_signal(intangibles, marketcap):
    scaled = _safe_div(intangibles, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d intangibles scaled by marketcap
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_63d_base_v037_signal(intangibles, marketcap):
    scaled = _safe_div(intangibles, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d intangibles scaled by marketcap
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_126d_base_v038_signal(intangibles, marketcap):
    scaled = _safe_div(intangibles, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d intangibles scaled by marketcap
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_252d_base_v039_signal(intangibles, marketcap):
    scaled = _safe_div(intangibles, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d intangibles scaled by marketcap
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_504d_base_v040_signal(intangibles, marketcap):
    scaled = _safe_div(intangibles, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_21d_base_v041_signal(intangibles):
    low = intangibles.rolling(21).min()
    result = _safe_div(intangibles - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_63d_base_v042_signal(intangibles):
    low = intangibles.rolling(63).min()
    result = _safe_div(intangibles - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_126d_base_v043_signal(intangibles):
    low = intangibles.rolling(126).min()
    result = _safe_div(intangibles - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_252d_base_v044_signal(intangibles):
    low = intangibles.rolling(252).min()
    result = _safe_div(intangibles - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_504d_base_v045_signal(intangibles):
    low = intangibles.rolling(504).min()
    result = _safe_div(intangibles - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_21d_base_v046_signal(intangibles):
    high = intangibles.rolling(21).max()
    result = _safe_div(high - intangibles, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_63d_base_v047_signal(intangibles):
    high = intangibles.rolling(63).max()
    result = _safe_div(high - intangibles, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_126d_base_v048_signal(intangibles):
    high = intangibles.rolling(126).max()
    result = _safe_div(high - intangibles, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_252d_base_v049_signal(intangibles):
    high = intangibles.rolling(252).max()
    result = _safe_div(high - intangibles, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_504d_base_v050_signal(intangibles):
    high = intangibles.rolling(504).max()
    result = _safe_div(high - intangibles, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_21d_base_v051_signal(intangibles):
    m1 = _mean(intangibles, 21)
    m2 = _mean(intangibles, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_63d_base_v052_signal(intangibles):
    m1 = _mean(intangibles, 63)
    m2 = _mean(intangibles, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_126d_base_v053_signal(intangibles):
    m1 = _mean(intangibles, 126)
    m2 = _mean(intangibles, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_252d_base_v054_signal(intangibles):
    m1 = _mean(intangibles, 252)
    m2 = _mean(intangibles, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_504d_base_v055_signal(intangibles):
    m1 = _mean(intangibles, 504)
    m2 = _mean(intangibles, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_skew_21d_base_v056_signal(intangibles):
    result = _skew(intangibles, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_skew_63d_base_v057_signal(intangibles):
    result = _skew(intangibles, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_skew_126d_base_v058_signal(intangibles):
    result = _skew(intangibles, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_skew_252d_base_v059_signal(intangibles):
    result = _skew(intangibles, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_skew_504d_base_v060_signal(intangibles):
    result = _skew(intangibles, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_kurt_21d_base_v061_signal(intangibles):
    result = _kurt(intangibles, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_kurt_63d_base_v062_signal(intangibles):
    result = _kurt(intangibles, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_kurt_126d_base_v063_signal(intangibles):
    result = _kurt(intangibles, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_kurt_252d_base_v064_signal(intangibles):
    result = _kurt(intangibles, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_kurt_504d_base_v065_signal(intangibles):
    result = _kurt(intangibles, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_rank_21d_base_v066_signal(intangibles, closeadj):
    result = _rank(intangibles, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_rank_63d_base_v067_signal(intangibles, closeadj):
    result = _rank(intangibles, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_rank_126d_base_v068_signal(intangibles, closeadj):
    result = _rank(intangibles, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_rank_252d_base_v069_signal(intangibles, closeadj):
    result = _rank(intangibles, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_rank_504d_base_v070_signal(intangibles, closeadj):
    result = _rank(intangibles, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_autocorr_21d_base_v071_signal(intangibles):
    result = _autocorr(intangibles, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_autocorr_63d_base_v072_signal(intangibles):
    result = _autocorr(intangibles, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_autocorr_126d_base_v073_signal(intangibles):
    result = _autocorr(intangibles, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_autocorr_252d_base_v074_signal(intangibles):
    result = _autocorr(intangibles, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_autocorr_504d_base_v075_signal(intangibles):
    result = _autocorr(intangibles, 504)
    return result.replace([np.inf, -np.inf], np.nan)

