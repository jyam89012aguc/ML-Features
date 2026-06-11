
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr

# Metric implementation
def _get_metric(rnd, assets):
    return _safe_div(rnd, assets)

# 21d smoothed rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_21d_base_v001_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _mean(val, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_63d_base_v002_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _mean(val, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_126d_base_v003_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _mean(val, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_252d_base_v004_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _mean(val, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_504d_base_v005_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _mean(val, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_21d_base_v006_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _mean(_log(val.abs()), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_63d_base_v007_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _mean(_log(val.abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_126d_base_v008_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _mean(_log(val.abs()), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_252d_base_v009_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _mean(_log(val.abs()), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_504d_base_v010_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _mean(_log(val.abs()), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_21d_base_v011_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _z(val, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_63d_base_v012_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _z(val, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_126d_base_v013_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _z(val, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_252d_base_v014_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _z(val, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_504d_base_v015_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _z(val, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_21d_base_v016_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _pct_change(val, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_63d_base_v017_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _pct_change(val, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_126d_base_v018_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _pct_change(val, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_252d_base_v019_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _pct_change(val, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_504d_base_v020_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _pct_change(val, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_21d_base_v021_signal(rnd, assets, sharesbas, closeadj):
    val = _get_metric(rnd, assets)
    ps = _safe_div(val, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_63d_base_v022_signal(rnd, assets, sharesbas, closeadj):
    val = _get_metric(rnd, assets)
    ps = _safe_div(val, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_126d_base_v023_signal(rnd, assets, sharesbas, closeadj):
    val = _get_metric(rnd, assets)
    ps = _safe_div(val, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_252d_base_v024_signal(rnd, assets, sharesbas, closeadj):
    val = _get_metric(rnd, assets)
    ps = _safe_div(val, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_504d_base_v025_signal(rnd, assets, sharesbas, closeadj):
    val = _get_metric(rnd, assets)
    ps = _safe_div(val, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rnd_intensity scaled by assets
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_21d_base_v026_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    scaled = _safe_div(val, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rnd_intensity scaled by assets
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_63d_base_v027_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    scaled = _safe_div(val, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rnd_intensity scaled by assets
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_126d_base_v028_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    scaled = _safe_div(val, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rnd_intensity scaled by assets
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_252d_base_v029_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    scaled = _safe_div(val, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rnd_intensity scaled by assets
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_504d_base_v030_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    scaled = _safe_div(val, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rnd_intensity scaled by marketcap
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_21d_base_v031_signal(rnd, assets, marketcap):
    val = _get_metric(rnd, assets)
    scaled = _safe_div(val, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rnd_intensity scaled by marketcap
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_63d_base_v032_signal(rnd, assets, marketcap):
    val = _get_metric(rnd, assets)
    scaled = _safe_div(val, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rnd_intensity scaled by marketcap
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_126d_base_v033_signal(rnd, assets, marketcap):
    val = _get_metric(rnd, assets)
    scaled = _safe_div(val, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rnd_intensity scaled by marketcap
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_252d_base_v034_signal(rnd, assets, marketcap):
    val = _get_metric(rnd, assets)
    scaled = _safe_div(val, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rnd_intensity scaled by marketcap
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_504d_base_v035_signal(rnd, assets, marketcap):
    val = _get_metric(rnd, assets)
    scaled = _safe_div(val, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_dist_low_21d_base_v036_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    low = val.rolling(21).min()
    result = _safe_div(val - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_dist_low_63d_base_v037_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    low = val.rolling(63).min()
    result = _safe_div(val - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_dist_low_126d_base_v038_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    low = val.rolling(126).min()
    result = _safe_div(val - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_dist_low_252d_base_v039_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    low = val.rolling(252).min()
    result = _safe_div(val - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_dist_low_504d_base_v040_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    low = val.rolling(504).min()
    result = _safe_div(val - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_dist_high_21d_base_v041_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    high = val.rolling(21).max()
    result = _safe_div(high - val, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_dist_high_63d_base_v042_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    high = val.rolling(63).max()
    result = _safe_div(high - val, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_dist_high_126d_base_v043_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    high = val.rolling(126).max()
    result = _safe_div(high - val, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_dist_high_252d_base_v044_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    high = val.rolling(252).max()
    result = _safe_div(high - val, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_dist_high_504d_base_v045_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    high = val.rolling(504).max()
    result = _safe_div(high - val, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mom_21d_base_v046_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    m1 = _mean(val, 21)
    m2 = _mean(val, 21*2)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mom_63d_base_v047_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    m1 = _mean(val, 63)
    m2 = _mean(val, 63*2)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mom_126d_base_v048_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    m1 = _mean(val, 126)
    m2 = _mean(val, 126*2)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mom_252d_base_v049_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    m1 = _mean(val, 252)
    m2 = _mean(val, 252*2)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mom_504d_base_v050_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    m1 = _mean(val, 504)
    m2 = _mean(val, 504*2)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_skew_21d_base_v051_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _skew(val, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_skew_63d_base_v052_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _skew(val, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_skew_126d_base_v053_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _skew(val, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_skew_252d_base_v054_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _skew(val, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_skew_504d_base_v055_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _skew(val, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_kurt_21d_base_v056_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _kurt(val, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_kurt_63d_base_v057_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _kurt(val, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_kurt_126d_base_v058_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _kurt(val, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_kurt_252d_base_v059_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _kurt(val, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_kurt_504d_base_v060_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _kurt(val, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_21d_base_v061_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _rank(val, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_63d_base_v062_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _rank(val, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_126d_base_v063_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _rank(val, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_252d_base_v064_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _rank(val, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_504d_base_v065_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _rank(val, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_autocorr_21d_base_v066_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _autocorr(val, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_autocorr_63d_base_v067_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _autocorr(val, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_autocorr_126d_base_v068_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _autocorr(val, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_autocorr_252d_base_v069_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _autocorr(val, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_autocorr_504d_base_v070_signal(rnd, assets):
    val = _get_metric(rnd, assets)
    result = _autocorr(val, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_std_21d_base_v071_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _std(val, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_std_63d_base_v072_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _std(val, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_std_126d_base_v073_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _std(val, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_std_252d_base_v074_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _std(val, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_std_504d_base_v075_signal(rnd, assets, closeadj):
    val = _get_metric(rnd, assets)
    result = _std(val, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

