
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_raw_21d_base_v001_signal(ncfo, closeadj):
    result = _mean(ncfo, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_raw_63d_base_v002_signal(ncfo, closeadj):
    result = _mean(ncfo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_raw_126d_base_v003_signal(ncfo, closeadj):
    result = _mean(ncfo, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_raw_252d_base_v004_signal(ncfo, closeadj):
    result = _mean(ncfo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_raw_504d_base_v005_signal(ncfo, closeadj):
    result = _mean(ncfo, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_log_21d_base_v006_signal(ncfo, closeadj):
    result = _mean(_log(ncfo), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_log_63d_base_v007_signal(ncfo, closeadj):
    result = _mean(_log(ncfo), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_log_126d_base_v008_signal(ncfo, closeadj):
    result = _mean(_log(ncfo), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_log_252d_base_v009_signal(ncfo, closeadj):
    result = _mean(_log(ncfo), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_log_504d_base_v010_signal(ncfo, closeadj):
    result = _mean(_log(ncfo), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_z_21d_base_v011_signal(ncfo):
    result = _z(ncfo, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_z_63d_base_v012_signal(ncfo):
    result = _z(ncfo, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_z_126d_base_v013_signal(ncfo):
    result = _z(ncfo, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_z_252d_base_v014_signal(ncfo):
    result = _z(ncfo, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_z_504d_base_v015_signal(ncfo):
    result = _z(ncfo, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_pct_21d_base_v016_signal(ncfo):
    result = _pct_change(ncfo, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_pct_63d_base_v017_signal(ncfo):
    result = _pct_change(ncfo, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_pct_126d_base_v018_signal(ncfo):
    result = _pct_change(ncfo, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_pct_252d_base_v019_signal(ncfo):
    result = _pct_change(ncfo, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_pct_504d_base_v020_signal(ncfo):
    result = _pct_change(ncfo, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_ps_21d_base_v021_signal(ncfo, sharesbas, closeadj):
    ps = _safe_div(ncfo, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_ps_63d_base_v022_signal(ncfo, sharesbas, closeadj):
    ps = _safe_div(ncfo, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_ps_126d_base_v023_signal(ncfo, sharesbas, closeadj):
    ps = _safe_div(ncfo, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_ps_252d_base_v024_signal(ncfo, sharesbas, closeadj):
    ps = _safe_div(ncfo, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_ps_504d_base_v025_signal(ncfo, sharesbas, closeadj):
    ps = _safe_div(ncfo, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of ncfo to revenue
def gm_f14_biotech_f14_burn_to_revenue_ratio_ratio_revenue_21d_base_v026_signal(ncfo, revenue):
    ratio = _safe_div(ncfo, revenue)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of ncfo to revenue
def gm_f14_biotech_f14_burn_to_revenue_ratio_ratio_revenue_63d_base_v027_signal(ncfo, revenue):
    ratio = _safe_div(ncfo, revenue)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of ncfo to revenue
def gm_f14_biotech_f14_burn_to_revenue_ratio_ratio_revenue_126d_base_v028_signal(ncfo, revenue):
    ratio = _safe_div(ncfo, revenue)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of ncfo to revenue
def gm_f14_biotech_f14_burn_to_revenue_ratio_ratio_revenue_252d_base_v029_signal(ncfo, revenue):
    ratio = _safe_div(ncfo, revenue)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of ncfo to revenue
def gm_f14_biotech_f14_burn_to_revenue_ratio_ratio_revenue_504d_base_v030_signal(ncfo, revenue):
    ratio = _safe_div(ncfo, revenue)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ncfo scaled by assets
def gm_f14_biotech_f14_burn_to_revenue_ratio_asset_scaled_21d_base_v031_signal(ncfo, assets):
    scaled = _safe_div(ncfo, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ncfo scaled by assets
def gm_f14_biotech_f14_burn_to_revenue_ratio_asset_scaled_63d_base_v032_signal(ncfo, assets):
    scaled = _safe_div(ncfo, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ncfo scaled by assets
def gm_f14_biotech_f14_burn_to_revenue_ratio_asset_scaled_126d_base_v033_signal(ncfo, assets):
    scaled = _safe_div(ncfo, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ncfo scaled by assets
def gm_f14_biotech_f14_burn_to_revenue_ratio_asset_scaled_252d_base_v034_signal(ncfo, assets):
    scaled = _safe_div(ncfo, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ncfo scaled by assets
def gm_f14_biotech_f14_burn_to_revenue_ratio_asset_scaled_504d_base_v035_signal(ncfo, assets):
    scaled = _safe_div(ncfo, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ncfo scaled by marketcap
def gm_f14_biotech_f14_burn_to_revenue_ratio_mcap_scaled_21d_base_v036_signal(ncfo, marketcap):
    scaled = _safe_div(ncfo, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ncfo scaled by marketcap
def gm_f14_biotech_f14_burn_to_revenue_ratio_mcap_scaled_63d_base_v037_signal(ncfo, marketcap):
    scaled = _safe_div(ncfo, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ncfo scaled by marketcap
def gm_f14_biotech_f14_burn_to_revenue_ratio_mcap_scaled_126d_base_v038_signal(ncfo, marketcap):
    scaled = _safe_div(ncfo, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ncfo scaled by marketcap
def gm_f14_biotech_f14_burn_to_revenue_ratio_mcap_scaled_252d_base_v039_signal(ncfo, marketcap):
    scaled = _safe_div(ncfo, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ncfo scaled by marketcap
def gm_f14_biotech_f14_burn_to_revenue_ratio_mcap_scaled_504d_base_v040_signal(ncfo, marketcap):
    scaled = _safe_div(ncfo, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_dist_low_21d_base_v041_signal(ncfo):
    low = ncfo.rolling(21).min()
    result = _safe_div(ncfo - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_dist_low_63d_base_v042_signal(ncfo):
    low = ncfo.rolling(63).min()
    result = _safe_div(ncfo - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_dist_low_126d_base_v043_signal(ncfo):
    low = ncfo.rolling(126).min()
    result = _safe_div(ncfo - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_dist_low_252d_base_v044_signal(ncfo):
    low = ncfo.rolling(252).min()
    result = _safe_div(ncfo - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_dist_low_504d_base_v045_signal(ncfo):
    low = ncfo.rolling(504).min()
    result = _safe_div(ncfo - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_dist_high_21d_base_v046_signal(ncfo):
    high = ncfo.rolling(21).max()
    result = _safe_div(high - ncfo, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_dist_high_63d_base_v047_signal(ncfo):
    high = ncfo.rolling(63).max()
    result = _safe_div(high - ncfo, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_dist_high_126d_base_v048_signal(ncfo):
    high = ncfo.rolling(126).max()
    result = _safe_div(high - ncfo, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_dist_high_252d_base_v049_signal(ncfo):
    high = ncfo.rolling(252).max()
    result = _safe_div(high - ncfo, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_dist_high_504d_base_v050_signal(ncfo):
    high = ncfo.rolling(504).max()
    result = _safe_div(high - ncfo, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_mom_21d_base_v051_signal(ncfo):
    m1 = _mean(ncfo, 21)
    m2 = _mean(ncfo, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_mom_63d_base_v052_signal(ncfo):
    m1 = _mean(ncfo, 63)
    m2 = _mean(ncfo, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_mom_126d_base_v053_signal(ncfo):
    m1 = _mean(ncfo, 126)
    m2 = _mean(ncfo, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_mom_252d_base_v054_signal(ncfo):
    m1 = _mean(ncfo, 252)
    m2 = _mean(ncfo, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_mom_504d_base_v055_signal(ncfo):
    m1 = _mean(ncfo, 504)
    m2 = _mean(ncfo, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_skew_21d_base_v056_signal(ncfo):
    result = _skew(ncfo, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_skew_63d_base_v057_signal(ncfo):
    result = _skew(ncfo, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_skew_126d_base_v058_signal(ncfo):
    result = _skew(ncfo, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_skew_252d_base_v059_signal(ncfo):
    result = _skew(ncfo, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_skew_504d_base_v060_signal(ncfo):
    result = _skew(ncfo, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_kurt_21d_base_v061_signal(ncfo):
    result = _kurt(ncfo, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_kurt_63d_base_v062_signal(ncfo):
    result = _kurt(ncfo, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_kurt_126d_base_v063_signal(ncfo):
    result = _kurt(ncfo, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_kurt_252d_base_v064_signal(ncfo):
    result = _kurt(ncfo, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_kurt_504d_base_v065_signal(ncfo):
    result = _kurt(ncfo, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_rank_21d_base_v066_signal(ncfo, closeadj):
    result = _rank(ncfo, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_rank_63d_base_v067_signal(ncfo, closeadj):
    result = _rank(ncfo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_rank_126d_base_v068_signal(ncfo, closeadj):
    result = _rank(ncfo, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_rank_252d_base_v069_signal(ncfo, closeadj):
    result = _rank(ncfo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_rank_504d_base_v070_signal(ncfo, closeadj):
    result = _rank(ncfo, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_autocorr_21d_base_v071_signal(ncfo):
    result = _autocorr(ncfo, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_autocorr_63d_base_v072_signal(ncfo):
    result = _autocorr(ncfo, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_autocorr_126d_base_v073_signal(ncfo):
    result = _autocorr(ncfo, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_autocorr_252d_base_v074_signal(ncfo):
    result = _autocorr(ncfo, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of ncfo
def gm_f14_biotech_f14_burn_to_revenue_ratio_autocorr_504d_base_v075_signal(ncfo):
    result = _autocorr(ncfo, 504)
    return result.replace([np.inf, -np.inf], np.nan)

