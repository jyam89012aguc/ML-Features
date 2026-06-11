
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_21d_base_v001_signal(deferredrev, closeadj):
    result = _mean(deferredrev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_63d_base_v002_signal(deferredrev, closeadj):
    result = _mean(deferredrev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_126d_base_v003_signal(deferredrev, closeadj):
    result = _mean(deferredrev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_252d_base_v004_signal(deferredrev, closeadj):
    result = _mean(deferredrev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_504d_base_v005_signal(deferredrev, closeadj):
    result = _mean(deferredrev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_21d_base_v006_signal(deferredrev, closeadj):
    result = _mean(_log(deferredrev), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_63d_base_v007_signal(deferredrev, closeadj):
    result = _mean(_log(deferredrev), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_126d_base_v008_signal(deferredrev, closeadj):
    result = _mean(_log(deferredrev), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_252d_base_v009_signal(deferredrev, closeadj):
    result = _mean(_log(deferredrev), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_504d_base_v010_signal(deferredrev, closeadj):
    result = _mean(_log(deferredrev), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_21d_base_v011_signal(deferredrev):
    result = _z(deferredrev, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_63d_base_v012_signal(deferredrev):
    result = _z(deferredrev, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_126d_base_v013_signal(deferredrev):
    result = _z(deferredrev, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_252d_base_v014_signal(deferredrev):
    result = _z(deferredrev, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_504d_base_v015_signal(deferredrev):
    result = _z(deferredrev, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_pct_21d_base_v016_signal(deferredrev):
    result = _pct_change(deferredrev, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_pct_63d_base_v017_signal(deferredrev):
    result = _pct_change(deferredrev, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_pct_126d_base_v018_signal(deferredrev):
    result = _pct_change(deferredrev, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_pct_252d_base_v019_signal(deferredrev):
    result = _pct_change(deferredrev, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_pct_504d_base_v020_signal(deferredrev):
    result = _pct_change(deferredrev, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_21d_base_v021_signal(deferredrev, sharesbas, closeadj):
    ps = _safe_div(deferredrev, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_63d_base_v022_signal(deferredrev, sharesbas, closeadj):
    ps = _safe_div(deferredrev, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_126d_base_v023_signal(deferredrev, sharesbas, closeadj):
    ps = _safe_div(deferredrev, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_252d_base_v024_signal(deferredrev, sharesbas, closeadj):
    ps = _safe_div(deferredrev, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_504d_base_v025_signal(deferredrev, sharesbas, closeadj):
    ps = _safe_div(deferredrev, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d deferredrev scaled by assets
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_21d_base_v026_signal(deferredrev, assets):
    scaled = _safe_div(deferredrev, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d deferredrev scaled by assets
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_63d_base_v027_signal(deferredrev, assets):
    scaled = _safe_div(deferredrev, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d deferredrev scaled by assets
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_126d_base_v028_signal(deferredrev, assets):
    scaled = _safe_div(deferredrev, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d deferredrev scaled by assets
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_252d_base_v029_signal(deferredrev, assets):
    scaled = _safe_div(deferredrev, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d deferredrev scaled by assets
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_504d_base_v030_signal(deferredrev, assets):
    scaled = _safe_div(deferredrev, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d deferredrev scaled by marketcap
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_21d_base_v031_signal(deferredrev, marketcap):
    scaled = _safe_div(deferredrev, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d deferredrev scaled by marketcap
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_63d_base_v032_signal(deferredrev, marketcap):
    scaled = _safe_div(deferredrev, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d deferredrev scaled by marketcap
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_126d_base_v033_signal(deferredrev, marketcap):
    scaled = _safe_div(deferredrev, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d deferredrev scaled by marketcap
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_252d_base_v034_signal(deferredrev, marketcap):
    scaled = _safe_div(deferredrev, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d deferredrev scaled by marketcap
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_504d_base_v035_signal(deferredrev, marketcap):
    scaled = _safe_div(deferredrev, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_21d_base_v036_signal(deferredrev):
    low = deferredrev.rolling(21).min()
    result = _safe_div(deferredrev - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_63d_base_v037_signal(deferredrev):
    low = deferredrev.rolling(63).min()
    result = _safe_div(deferredrev - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_126d_base_v038_signal(deferredrev):
    low = deferredrev.rolling(126).min()
    result = _safe_div(deferredrev - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_252d_base_v039_signal(deferredrev):
    low = deferredrev.rolling(252).min()
    result = _safe_div(deferredrev - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_504d_base_v040_signal(deferredrev):
    low = deferredrev.rolling(504).min()
    result = _safe_div(deferredrev - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_21d_base_v041_signal(deferredrev):
    high = deferredrev.rolling(21).max()
    result = _safe_div(high - deferredrev, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_63d_base_v042_signal(deferredrev):
    high = deferredrev.rolling(63).max()
    result = _safe_div(high - deferredrev, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_126d_base_v043_signal(deferredrev):
    high = deferredrev.rolling(126).max()
    result = _safe_div(high - deferredrev, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_252d_base_v044_signal(deferredrev):
    high = deferredrev.rolling(252).max()
    result = _safe_div(high - deferredrev, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_504d_base_v045_signal(deferredrev):
    high = deferredrev.rolling(504).max()
    result = _safe_div(high - deferredrev, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_21d_base_v046_signal(deferredrev):
    m1 = _mean(deferredrev, 21)
    m2 = _mean(deferredrev, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_63d_base_v047_signal(deferredrev):
    m1 = _mean(deferredrev, 63)
    m2 = _mean(deferredrev, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_126d_base_v048_signal(deferredrev):
    m1 = _mean(deferredrev, 126)
    m2 = _mean(deferredrev, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_252d_base_v049_signal(deferredrev):
    m1 = _mean(deferredrev, 252)
    m2 = _mean(deferredrev, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_504d_base_v050_signal(deferredrev):
    m1 = _mean(deferredrev, 504)
    m2 = _mean(deferredrev, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_skew_21d_base_v051_signal(deferredrev):
    result = _skew(deferredrev, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_skew_63d_base_v052_signal(deferredrev):
    result = _skew(deferredrev, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_skew_126d_base_v053_signal(deferredrev):
    result = _skew(deferredrev, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_skew_252d_base_v054_signal(deferredrev):
    result = _skew(deferredrev, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_skew_504d_base_v055_signal(deferredrev):
    result = _skew(deferredrev, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_kurt_21d_base_v056_signal(deferredrev):
    result = _kurt(deferredrev, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_kurt_63d_base_v057_signal(deferredrev):
    result = _kurt(deferredrev, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_kurt_126d_base_v058_signal(deferredrev):
    result = _kurt(deferredrev, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_kurt_252d_base_v059_signal(deferredrev):
    result = _kurt(deferredrev, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_kurt_504d_base_v060_signal(deferredrev):
    result = _kurt(deferredrev, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_rank_21d_base_v061_signal(deferredrev, closeadj):
    result = _rank(deferredrev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_rank_63d_base_v062_signal(deferredrev, closeadj):
    result = _rank(deferredrev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_rank_126d_base_v063_signal(deferredrev, closeadj):
    result = _rank(deferredrev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_rank_252d_base_v064_signal(deferredrev, closeadj):
    result = _rank(deferredrev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_rank_504d_base_v065_signal(deferredrev, closeadj):
    result = _rank(deferredrev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_autocorr_21d_base_v066_signal(deferredrev):
    result = _autocorr(deferredrev, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_autocorr_63d_base_v067_signal(deferredrev):
    result = _autocorr(deferredrev, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_autocorr_126d_base_v068_signal(deferredrev):
    result = _autocorr(deferredrev, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_autocorr_252d_base_v069_signal(deferredrev):
    result = _autocorr(deferredrev, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_autocorr_504d_base_v070_signal(deferredrev):
    result = _autocorr(deferredrev, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_std_21d_base_v071_signal(deferredrev, closeadj):
    result = _std(deferredrev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_std_63d_base_v072_signal(deferredrev, closeadj):
    result = _std(deferredrev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_std_126d_base_v073_signal(deferredrev, closeadj):
    result = _std(deferredrev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_std_252d_base_v074_signal(deferredrev, closeadj):
    result = _std(deferredrev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_std_504d_base_v075_signal(deferredrev, closeadj):
    result = _std(deferredrev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

