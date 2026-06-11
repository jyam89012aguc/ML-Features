
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_raw_21d_base_v001_signal(evrev, closeadj):
    result = _mean(evrev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_raw_63d_base_v002_signal(evrev, closeadj):
    result = _mean(evrev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_raw_126d_base_v003_signal(evrev, closeadj):
    result = _mean(evrev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_raw_252d_base_v004_signal(evrev, closeadj):
    result = _mean(evrev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_raw_504d_base_v005_signal(evrev, closeadj):
    result = _mean(evrev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_log_21d_base_v006_signal(evrev, closeadj):
    result = _mean(_log(evrev), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_log_63d_base_v007_signal(evrev, closeadj):
    result = _mean(_log(evrev), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_log_126d_base_v008_signal(evrev, closeadj):
    result = _mean(_log(evrev), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_log_252d_base_v009_signal(evrev, closeadj):
    result = _mean(_log(evrev), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_log_504d_base_v010_signal(evrev, closeadj):
    result = _mean(_log(evrev), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_z_21d_base_v011_signal(evrev):
    result = _z(evrev, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_z_63d_base_v012_signal(evrev):
    result = _z(evrev, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_z_126d_base_v013_signal(evrev):
    result = _z(evrev, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_z_252d_base_v014_signal(evrev):
    result = _z(evrev, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_z_504d_base_v015_signal(evrev):
    result = _z(evrev, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_pct_21d_base_v016_signal(evrev):
    result = _pct_change(evrev, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_pct_63d_base_v017_signal(evrev):
    result = _pct_change(evrev, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_pct_126d_base_v018_signal(evrev):
    result = _pct_change(evrev, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_pct_252d_base_v019_signal(evrev):
    result = _pct_change(evrev, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_pct_504d_base_v020_signal(evrev):
    result = _pct_change(evrev, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_ps_21d_base_v021_signal(evrev, sharesbas, closeadj):
    ps = _safe_div(evrev, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_ps_63d_base_v022_signal(evrev, sharesbas, closeadj):
    ps = _safe_div(evrev, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_ps_126d_base_v023_signal(evrev, sharesbas, closeadj):
    ps = _safe_div(evrev, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_ps_252d_base_v024_signal(evrev, sharesbas, closeadj):
    ps = _safe_div(evrev, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_ps_504d_base_v025_signal(evrev, sharesbas, closeadj):
    ps = _safe_div(evrev, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of evrev to revrevenue
def gm_f81_biotech_f81_enterprise_value_to_revenue_ratio_revrevenue_21d_base_v026_signal(evrev, revrevenue):
    ratio = _safe_div(evrev, revrevenue)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of evrev to revrevenue
def gm_f81_biotech_f81_enterprise_value_to_revenue_ratio_revrevenue_63d_base_v027_signal(evrev, revrevenue):
    ratio = _safe_div(evrev, revrevenue)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of evrev to revrevenue
def gm_f81_biotech_f81_enterprise_value_to_revenue_ratio_revrevenue_126d_base_v028_signal(evrev, revrevenue):
    ratio = _safe_div(evrev, revrevenue)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of evrev to revrevenue
def gm_f81_biotech_f81_enterprise_value_to_revenue_ratio_revrevenue_252d_base_v029_signal(evrev, revrevenue):
    ratio = _safe_div(evrev, revrevenue)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of evrev to revrevenue
def gm_f81_biotech_f81_enterprise_value_to_revenue_ratio_revrevenue_504d_base_v030_signal(evrev, revrevenue):
    ratio = _safe_div(evrev, revrevenue)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d evrev scaled by assets
def gm_f81_biotech_f81_enterprise_value_to_revenue_asset_scaled_21d_base_v031_signal(evrev, assets):
    scaled = _safe_div(evrev, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d evrev scaled by assets
def gm_f81_biotech_f81_enterprise_value_to_revenue_asset_scaled_63d_base_v032_signal(evrev, assets):
    scaled = _safe_div(evrev, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d evrev scaled by assets
def gm_f81_biotech_f81_enterprise_value_to_revenue_asset_scaled_126d_base_v033_signal(evrev, assets):
    scaled = _safe_div(evrev, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d evrev scaled by assets
def gm_f81_biotech_f81_enterprise_value_to_revenue_asset_scaled_252d_base_v034_signal(evrev, assets):
    scaled = _safe_div(evrev, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d evrev scaled by assets
def gm_f81_biotech_f81_enterprise_value_to_revenue_asset_scaled_504d_base_v035_signal(evrev, assets):
    scaled = _safe_div(evrev, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d evrev scaled by marketcap
def gm_f81_biotech_f81_enterprise_value_to_revenue_mcap_scaled_21d_base_v036_signal(evrev, marketcap):
    scaled = _safe_div(evrev, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d evrev scaled by marketcap
def gm_f81_biotech_f81_enterprise_value_to_revenue_mcap_scaled_63d_base_v037_signal(evrev, marketcap):
    scaled = _safe_div(evrev, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d evrev scaled by marketcap
def gm_f81_biotech_f81_enterprise_value_to_revenue_mcap_scaled_126d_base_v038_signal(evrev, marketcap):
    scaled = _safe_div(evrev, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d evrev scaled by marketcap
def gm_f81_biotech_f81_enterprise_value_to_revenue_mcap_scaled_252d_base_v039_signal(evrev, marketcap):
    scaled = _safe_div(evrev, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d evrev scaled by marketcap
def gm_f81_biotech_f81_enterprise_value_to_revenue_mcap_scaled_504d_base_v040_signal(evrev, marketcap):
    scaled = _safe_div(evrev, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_dist_low_21d_base_v041_signal(evrev):
    low = evrev.rolling(21).min()
    result = _safe_div(evrev - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_dist_low_63d_base_v042_signal(evrev):
    low = evrev.rolling(63).min()
    result = _safe_div(evrev - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_dist_low_126d_base_v043_signal(evrev):
    low = evrev.rolling(126).min()
    result = _safe_div(evrev - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_dist_low_252d_base_v044_signal(evrev):
    low = evrev.rolling(252).min()
    result = _safe_div(evrev - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_dist_low_504d_base_v045_signal(evrev):
    low = evrev.rolling(504).min()
    result = _safe_div(evrev - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_dist_high_21d_base_v046_signal(evrev):
    high = evrev.rolling(21).max()
    result = _safe_div(high - evrev, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_dist_high_63d_base_v047_signal(evrev):
    high = evrev.rolling(63).max()
    result = _safe_div(high - evrev, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_dist_high_126d_base_v048_signal(evrev):
    high = evrev.rolling(126).max()
    result = _safe_div(high - evrev, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_dist_high_252d_base_v049_signal(evrev):
    high = evrev.rolling(252).max()
    result = _safe_div(high - evrev, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_dist_high_504d_base_v050_signal(evrev):
    high = evrev.rolling(504).max()
    result = _safe_div(high - evrev, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d levrevel momentum of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_mom_21d_base_v051_signal(evrev):
    m1 = _mean(evrev, 21)
    m2 = _mean(evrev, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d levrevel momentum of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_mom_63d_base_v052_signal(evrev):
    m1 = _mean(evrev, 63)
    m2 = _mean(evrev, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d levrevel momentum of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_mom_126d_base_v053_signal(evrev):
    m1 = _mean(evrev, 126)
    m2 = _mean(evrev, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d levrevel momentum of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_mom_252d_base_v054_signal(evrev):
    m1 = _mean(evrev, 252)
    m2 = _mean(evrev, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d levrevel momentum of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_mom_504d_base_v055_signal(evrev):
    m1 = _mean(evrev, 504)
    m2 = _mean(evrev, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_skew_21d_base_v056_signal(evrev):
    result = _skew(evrev, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_skew_63d_base_v057_signal(evrev):
    result = _skew(evrev, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_skew_126d_base_v058_signal(evrev):
    result = _skew(evrev, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_skew_252d_base_v059_signal(evrev):
    result = _skew(evrev, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_skew_504d_base_v060_signal(evrev):
    result = _skew(evrev, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_kurt_21d_base_v061_signal(evrev):
    result = _kurt(evrev, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_kurt_63d_base_v062_signal(evrev):
    result = _kurt(evrev, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_kurt_126d_base_v063_signal(evrev):
    result = _kurt(evrev, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_kurt_252d_base_v064_signal(evrev):
    result = _kurt(evrev, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_kurt_504d_base_v065_signal(evrev):
    result = _kurt(evrev, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_rank_21d_base_v066_signal(evrev, closeadj):
    result = _rank(evrev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_rank_63d_base_v067_signal(evrev, closeadj):
    result = _rank(evrev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_rank_126d_base_v068_signal(evrev, closeadj):
    result = _rank(evrev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_rank_252d_base_v069_signal(evrev, closeadj):
    result = _rank(evrev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_rank_504d_base_v070_signal(evrev, closeadj):
    result = _rank(evrev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_autocorr_21d_base_v071_signal(evrev):
    result = _autocorr(evrev, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_autocorr_63d_base_v072_signal(evrev):
    result = _autocorr(evrev, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_autocorr_126d_base_v073_signal(evrev):
    result = _autocorr(evrev, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_autocorr_252d_base_v074_signal(evrev):
    result = _autocorr(evrev, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of evrev
def gm_f81_biotech_f81_enterprise_value_to_revenue_autocorr_504d_base_v075_signal(evrev):
    result = _autocorr(evrev, 504)
    return result.replace([np.inf, -np.inf], np.nan)

