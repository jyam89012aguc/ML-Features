
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_21d_base_v001_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_63d_base_v002_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_126d_base_v003_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_252d_base_v004_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_504d_base_v005_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_21d_base_v006_signal(sharesbas, closeadj):
    result = _mean(_log(sharesbas), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_63d_base_v007_signal(sharesbas, closeadj):
    result = _mean(_log(sharesbas), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_126d_base_v008_signal(sharesbas, closeadj):
    result = _mean(_log(sharesbas), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_252d_base_v009_signal(sharesbas, closeadj):
    result = _mean(_log(sharesbas), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_504d_base_v010_signal(sharesbas, closeadj):
    result = _mean(_log(sharesbas), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_21d_base_v011_signal(sharesbas):
    result = _z(sharesbas, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_63d_base_v012_signal(sharesbas):
    result = _z(sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_126d_base_v013_signal(sharesbas):
    result = _z(sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_252d_base_v014_signal(sharesbas):
    result = _z(sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_504d_base_v015_signal(sharesbas):
    result = _z(sharesbas, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of sharesbas
def gm_f28_biotech_f28_share_count_velocity_pct_21d_base_v016_signal(sharesbas):
    result = _pct_change(sharesbas, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of sharesbas
def gm_f28_biotech_f28_share_count_velocity_pct_63d_base_v017_signal(sharesbas):
    result = _pct_change(sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of sharesbas
def gm_f28_biotech_f28_share_count_velocity_pct_126d_base_v018_signal(sharesbas):
    result = _pct_change(sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of sharesbas
def gm_f28_biotech_f28_share_count_velocity_pct_252d_base_v019_signal(sharesbas):
    result = _pct_change(sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of sharesbas
def gm_f28_biotech_f28_share_count_velocity_pct_504d_base_v020_signal(sharesbas):
    result = _pct_change(sharesbas, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_21d_base_v021_signal(sharesbas, closeadj):
    ps = _safe_div(sharesbas, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_63d_base_v022_signal(sharesbas, closeadj):
    ps = _safe_div(sharesbas, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_126d_base_v023_signal(sharesbas, closeadj):
    ps = _safe_div(sharesbas, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_252d_base_v024_signal(sharesbas, closeadj):
    ps = _safe_div(sharesbas, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_504d_base_v025_signal(sharesbas, closeadj):
    ps = _safe_div(sharesbas, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sharesbas scaled by assets
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_21d_base_v026_signal(sharesbas, assets):
    scaled = _safe_div(sharesbas, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sharesbas scaled by assets
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_63d_base_v027_signal(sharesbas, assets):
    scaled = _safe_div(sharesbas, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sharesbas scaled by assets
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_126d_base_v028_signal(sharesbas, assets):
    scaled = _safe_div(sharesbas, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sharesbas scaled by assets
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_252d_base_v029_signal(sharesbas, assets):
    scaled = _safe_div(sharesbas, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sharesbas scaled by assets
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_504d_base_v030_signal(sharesbas, assets):
    scaled = _safe_div(sharesbas, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sharesbas scaled by marketcap
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_21d_base_v031_signal(sharesbas, marketcap):
    scaled = _safe_div(sharesbas, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sharesbas scaled by marketcap
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_63d_base_v032_signal(sharesbas, marketcap):
    scaled = _safe_div(sharesbas, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sharesbas scaled by marketcap
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_126d_base_v033_signal(sharesbas, marketcap):
    scaled = _safe_div(sharesbas, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sharesbas scaled by marketcap
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_252d_base_v034_signal(sharesbas, marketcap):
    scaled = _safe_div(sharesbas, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sharesbas scaled by marketcap
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_504d_base_v035_signal(sharesbas, marketcap):
    scaled = _safe_div(sharesbas, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_21d_base_v036_signal(sharesbas):
    low = sharesbas.rolling(21).min()
    result = _safe_div(sharesbas - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_63d_base_v037_signal(sharesbas):
    low = sharesbas.rolling(63).min()
    result = _safe_div(sharesbas - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_126d_base_v038_signal(sharesbas):
    low = sharesbas.rolling(126).min()
    result = _safe_div(sharesbas - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_252d_base_v039_signal(sharesbas):
    low = sharesbas.rolling(252).min()
    result = _safe_div(sharesbas - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_504d_base_v040_signal(sharesbas):
    low = sharesbas.rolling(504).min()
    result = _safe_div(sharesbas - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_21d_base_v041_signal(sharesbas):
    high = sharesbas.rolling(21).max()
    result = _safe_div(high - sharesbas, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_63d_base_v042_signal(sharesbas):
    high = sharesbas.rolling(63).max()
    result = _safe_div(high - sharesbas, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_126d_base_v043_signal(sharesbas):
    high = sharesbas.rolling(126).max()
    result = _safe_div(high - sharesbas, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_252d_base_v044_signal(sharesbas):
    high = sharesbas.rolling(252).max()
    result = _safe_div(high - sharesbas, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_504d_base_v045_signal(sharesbas):
    high = sharesbas.rolling(504).max()
    result = _safe_div(high - sharesbas, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_21d_base_v046_signal(sharesbas):
    m1 = _mean(sharesbas, 21)
    m2 = _mean(sharesbas, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_63d_base_v047_signal(sharesbas):
    m1 = _mean(sharesbas, 63)
    m2 = _mean(sharesbas, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_126d_base_v048_signal(sharesbas):
    m1 = _mean(sharesbas, 126)
    m2 = _mean(sharesbas, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_252d_base_v049_signal(sharesbas):
    m1 = _mean(sharesbas, 252)
    m2 = _mean(sharesbas, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_504d_base_v050_signal(sharesbas):
    m1 = _mean(sharesbas, 504)
    m2 = _mean(sharesbas, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of sharesbas
def gm_f28_biotech_f28_share_count_velocity_skew_21d_base_v051_signal(sharesbas):
    result = _skew(sharesbas, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of sharesbas
def gm_f28_biotech_f28_share_count_velocity_skew_63d_base_v052_signal(sharesbas):
    result = _skew(sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of sharesbas
def gm_f28_biotech_f28_share_count_velocity_skew_126d_base_v053_signal(sharesbas):
    result = _skew(sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of sharesbas
def gm_f28_biotech_f28_share_count_velocity_skew_252d_base_v054_signal(sharesbas):
    result = _skew(sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of sharesbas
def gm_f28_biotech_f28_share_count_velocity_skew_504d_base_v055_signal(sharesbas):
    result = _skew(sharesbas, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of sharesbas
def gm_f28_biotech_f28_share_count_velocity_kurt_21d_base_v056_signal(sharesbas):
    result = _kurt(sharesbas, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of sharesbas
def gm_f28_biotech_f28_share_count_velocity_kurt_63d_base_v057_signal(sharesbas):
    result = _kurt(sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of sharesbas
def gm_f28_biotech_f28_share_count_velocity_kurt_126d_base_v058_signal(sharesbas):
    result = _kurt(sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of sharesbas
def gm_f28_biotech_f28_share_count_velocity_kurt_252d_base_v059_signal(sharesbas):
    result = _kurt(sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of sharesbas
def gm_f28_biotech_f28_share_count_velocity_kurt_504d_base_v060_signal(sharesbas):
    result = _kurt(sharesbas, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of sharesbas
def gm_f28_biotech_f28_share_count_velocity_rank_21d_base_v061_signal(sharesbas, closeadj):
    result = _rank(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of sharesbas
def gm_f28_biotech_f28_share_count_velocity_rank_63d_base_v062_signal(sharesbas, closeadj):
    result = _rank(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of sharesbas
def gm_f28_biotech_f28_share_count_velocity_rank_126d_base_v063_signal(sharesbas, closeadj):
    result = _rank(sharesbas, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of sharesbas
def gm_f28_biotech_f28_share_count_velocity_rank_252d_base_v064_signal(sharesbas, closeadj):
    result = _rank(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of sharesbas
def gm_f28_biotech_f28_share_count_velocity_rank_504d_base_v065_signal(sharesbas, closeadj):
    result = _rank(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of sharesbas
def gm_f28_biotech_f28_share_count_velocity_autocorr_21d_base_v066_signal(sharesbas):
    result = _autocorr(sharesbas, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of sharesbas
def gm_f28_biotech_f28_share_count_velocity_autocorr_63d_base_v067_signal(sharesbas):
    result = _autocorr(sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of sharesbas
def gm_f28_biotech_f28_share_count_velocity_autocorr_126d_base_v068_signal(sharesbas):
    result = _autocorr(sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of sharesbas
def gm_f28_biotech_f28_share_count_velocity_autocorr_252d_base_v069_signal(sharesbas):
    result = _autocorr(sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of sharesbas
def gm_f28_biotech_f28_share_count_velocity_autocorr_504d_base_v070_signal(sharesbas):
    result = _autocorr(sharesbas, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of sharesbas
def gm_f28_biotech_f28_share_count_velocity_std_21d_base_v071_signal(sharesbas, closeadj):
    result = _std(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of sharesbas
def gm_f28_biotech_f28_share_count_velocity_std_63d_base_v072_signal(sharesbas, closeadj):
    result = _std(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of sharesbas
def gm_f28_biotech_f28_share_count_velocity_std_126d_base_v073_signal(sharesbas, closeadj):
    result = _std(sharesbas, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of sharesbas
def gm_f28_biotech_f28_share_count_velocity_std_252d_base_v074_signal(sharesbas, closeadj):
    result = _std(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of sharesbas
def gm_f28_biotech_f28_share_count_velocity_std_504d_base_v075_signal(sharesbas, closeadj):
    result = _std(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

