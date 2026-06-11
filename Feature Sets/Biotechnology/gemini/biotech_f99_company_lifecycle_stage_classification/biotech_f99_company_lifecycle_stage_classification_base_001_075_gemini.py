
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_21d_base_v001_signal(revenue, closeadj):
    result = _mean(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_63d_base_v002_signal(revenue, closeadj):
    result = _mean(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_126d_base_v003_signal(revenue, closeadj):
    result = _mean(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_252d_base_v004_signal(revenue, closeadj):
    result = _mean(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_504d_base_v005_signal(revenue, closeadj):
    result = _mean(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_21d_base_v006_signal(revenue, closeadj):
    result = _mean(_log(revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_63d_base_v007_signal(revenue, closeadj):
    result = _mean(_log(revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_126d_base_v008_signal(revenue, closeadj):
    result = _mean(_log(revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_252d_base_v009_signal(revenue, closeadj):
    result = _mean(_log(revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_504d_base_v010_signal(revenue, closeadj):
    result = _mean(_log(revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_21d_base_v011_signal(revenue):
    result = _z(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_63d_base_v012_signal(revenue):
    result = _z(revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_126d_base_v013_signal(revenue):
    result = _z(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_252d_base_v014_signal(revenue):
    result = _z(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_504d_base_v015_signal(revenue):
    result = _z(revenue, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_pct_21d_base_v016_signal(revenue):
    result = _pct_change(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_pct_63d_base_v017_signal(revenue):
    result = _pct_change(revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_pct_126d_base_v018_signal(revenue):
    result = _pct_change(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_pct_252d_base_v019_signal(revenue):
    result = _pct_change(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_pct_504d_base_v020_signal(revenue):
    result = _pct_change(revenue, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_21d_base_v021_signal(revenue, sharesbas, closeadj):
    ps = _safe_div(revenue, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_63d_base_v022_signal(revenue, sharesbas, closeadj):
    ps = _safe_div(revenue, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_126d_base_v023_signal(revenue, sharesbas, closeadj):
    ps = _safe_div(revenue, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_252d_base_v024_signal(revenue, sharesbas, closeadj):
    ps = _safe_div(revenue, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_504d_base_v025_signal(revenue, sharesbas, closeadj):
    ps = _safe_div(revenue, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of revenue to rnd
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ratio_rnd_21d_base_v026_signal(revenue, rnd):
    ratio = _safe_div(revenue, rnd)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of revenue to rnd
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ratio_rnd_63d_base_v027_signal(revenue, rnd):
    ratio = _safe_div(revenue, rnd)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of revenue to rnd
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ratio_rnd_126d_base_v028_signal(revenue, rnd):
    ratio = _safe_div(revenue, rnd)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of revenue to rnd
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ratio_rnd_252d_base_v029_signal(revenue, rnd):
    ratio = _safe_div(revenue, rnd)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of revenue to rnd
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ratio_rnd_504d_base_v030_signal(revenue, rnd):
    ratio = _safe_div(revenue, rnd)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of revenue to marketcap
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ratio_marketcap_21d_base_v031_signal(revenue, marketcap):
    ratio = _safe_div(revenue, marketcap)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of revenue to marketcap
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ratio_marketcap_63d_base_v032_signal(revenue, marketcap):
    ratio = _safe_div(revenue, marketcap)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of revenue to marketcap
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ratio_marketcap_126d_base_v033_signal(revenue, marketcap):
    ratio = _safe_div(revenue, marketcap)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of revenue to marketcap
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ratio_marketcap_252d_base_v034_signal(revenue, marketcap):
    ratio = _safe_div(revenue, marketcap)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of revenue to marketcap
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ratio_marketcap_504d_base_v035_signal(revenue, marketcap):
    ratio = _safe_div(revenue, marketcap)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d revenue scaled by assets
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_21d_base_v036_signal(revenue, assets):
    scaled = _safe_div(revenue, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d revenue scaled by assets
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_63d_base_v037_signal(revenue, assets):
    scaled = _safe_div(revenue, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d revenue scaled by assets
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_126d_base_v038_signal(revenue, assets):
    scaled = _safe_div(revenue, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d revenue scaled by assets
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_252d_base_v039_signal(revenue, assets):
    scaled = _safe_div(revenue, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d revenue scaled by assets
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_504d_base_v040_signal(revenue, assets):
    scaled = _safe_div(revenue, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d revenue scaled by marketcap
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_21d_base_v041_signal(revenue, marketcap):
    scaled = _safe_div(revenue, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d revenue scaled by marketcap
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_63d_base_v042_signal(revenue, marketcap):
    scaled = _safe_div(revenue, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d revenue scaled by marketcap
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_126d_base_v043_signal(revenue, marketcap):
    scaled = _safe_div(revenue, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d revenue scaled by marketcap
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_252d_base_v044_signal(revenue, marketcap):
    scaled = _safe_div(revenue, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d revenue scaled by marketcap
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_504d_base_v045_signal(revenue, marketcap):
    scaled = _safe_div(revenue, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_21d_base_v046_signal(revenue):
    low = revenue.rolling(21).min()
    result = _safe_div(revenue - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_63d_base_v047_signal(revenue):
    low = revenue.rolling(63).min()
    result = _safe_div(revenue - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_126d_base_v048_signal(revenue):
    low = revenue.rolling(126).min()
    result = _safe_div(revenue - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_252d_base_v049_signal(revenue):
    low = revenue.rolling(252).min()
    result = _safe_div(revenue - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_504d_base_v050_signal(revenue):
    low = revenue.rolling(504).min()
    result = _safe_div(revenue - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_21d_base_v051_signal(revenue):
    high = revenue.rolling(21).max()
    result = _safe_div(high - revenue, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_63d_base_v052_signal(revenue):
    high = revenue.rolling(63).max()
    result = _safe_div(high - revenue, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_126d_base_v053_signal(revenue):
    high = revenue.rolling(126).max()
    result = _safe_div(high - revenue, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_252d_base_v054_signal(revenue):
    high = revenue.rolling(252).max()
    result = _safe_div(high - revenue, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_504d_base_v055_signal(revenue):
    high = revenue.rolling(504).max()
    result = _safe_div(high - revenue, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_21d_base_v056_signal(revenue):
    m1 = _mean(revenue, 21)
    m2 = _mean(revenue, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_63d_base_v057_signal(revenue):
    m1 = _mean(revenue, 63)
    m2 = _mean(revenue, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_126d_base_v058_signal(revenue):
    m1 = _mean(revenue, 126)
    m2 = _mean(revenue, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_252d_base_v059_signal(revenue):
    m1 = _mean(revenue, 252)
    m2 = _mean(revenue, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_504d_base_v060_signal(revenue):
    m1 = _mean(revenue, 504)
    m2 = _mean(revenue, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_skew_21d_base_v061_signal(revenue):
    result = _skew(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_skew_63d_base_v062_signal(revenue):
    result = _skew(revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_skew_126d_base_v063_signal(revenue):
    result = _skew(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_skew_252d_base_v064_signal(revenue):
    result = _skew(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_skew_504d_base_v065_signal(revenue):
    result = _skew(revenue, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_kurt_21d_base_v066_signal(revenue):
    result = _kurt(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_kurt_63d_base_v067_signal(revenue):
    result = _kurt(revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_kurt_126d_base_v068_signal(revenue):
    result = _kurt(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_kurt_252d_base_v069_signal(revenue):
    result = _kurt(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_kurt_504d_base_v070_signal(revenue):
    result = _kurt(revenue, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_rank_21d_base_v071_signal(revenue, closeadj):
    result = _rank(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_rank_63d_base_v072_signal(revenue, closeadj):
    result = _rank(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_rank_126d_base_v073_signal(revenue, closeadj):
    result = _rank(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_rank_252d_base_v074_signal(revenue, closeadj):
    result = _rank(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_rank_504d_base_v075_signal(revenue, closeadj):
    result = _rank(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

