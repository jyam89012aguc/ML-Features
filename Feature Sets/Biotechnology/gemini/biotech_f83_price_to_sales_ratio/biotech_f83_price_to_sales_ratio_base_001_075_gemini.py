
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed ps
def gm_f83_biotech_f83_price_to_sales_ratio_raw_21d_base_v001_signal(ps, closeadj):
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed ps
def gm_f83_biotech_f83_price_to_sales_ratio_raw_63d_base_v002_signal(ps, closeadj):
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed ps
def gm_f83_biotech_f83_price_to_sales_ratio_raw_126d_base_v003_signal(ps, closeadj):
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed ps
def gm_f83_biotech_f83_price_to_sales_ratio_raw_252d_base_v004_signal(ps, closeadj):
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed ps
def gm_f83_biotech_f83_price_to_sales_ratio_raw_504d_base_v005_signal(ps, closeadj):
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed ps
def gm_f83_biotech_f83_price_to_sales_ratio_log_21d_base_v006_signal(ps, closeadj):
    result = _mean(_log(ps), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed ps
def gm_f83_biotech_f83_price_to_sales_ratio_log_63d_base_v007_signal(ps, closeadj):
    result = _mean(_log(ps), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed ps
def gm_f83_biotech_f83_price_to_sales_ratio_log_126d_base_v008_signal(ps, closeadj):
    result = _mean(_log(ps), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed ps
def gm_f83_biotech_f83_price_to_sales_ratio_log_252d_base_v009_signal(ps, closeadj):
    result = _mean(_log(ps), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed ps
def gm_f83_biotech_f83_price_to_sales_ratio_log_504d_base_v010_signal(ps, closeadj):
    result = _mean(_log(ps), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of ps
def gm_f83_biotech_f83_price_to_sales_ratio_z_21d_base_v011_signal(ps):
    result = _z(ps, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ps
def gm_f83_biotech_f83_price_to_sales_ratio_z_63d_base_v012_signal(ps):
    result = _z(ps, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ps
def gm_f83_biotech_f83_price_to_sales_ratio_z_126d_base_v013_signal(ps):
    result = _z(ps, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ps
def gm_f83_biotech_f83_price_to_sales_ratio_z_252d_base_v014_signal(ps):
    result = _z(ps, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ps
def gm_f83_biotech_f83_price_to_sales_ratio_z_504d_base_v015_signal(ps):
    result = _z(ps, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of ps
def gm_f83_biotech_f83_price_to_sales_ratio_pct_21d_base_v016_signal(ps):
    result = _pct_change(ps, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of ps
def gm_f83_biotech_f83_price_to_sales_ratio_pct_63d_base_v017_signal(ps):
    result = _pct_change(ps, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of ps
def gm_f83_biotech_f83_price_to_sales_ratio_pct_126d_base_v018_signal(ps):
    result = _pct_change(ps, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of ps
def gm_f83_biotech_f83_price_to_sales_ratio_pct_252d_base_v019_signal(ps):
    result = _pct_change(ps, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of ps
def gm_f83_biotech_f83_price_to_sales_ratio_pct_504d_base_v020_signal(ps):
    result = _pct_change(ps, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share ps
def gm_f83_biotech_f83_price_to_sales_ratio_ps_21d_base_v021_signal(ps, sharesbas, closeadj):
    ps = _safe_div(ps, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share ps
def gm_f83_biotech_f83_price_to_sales_ratio_ps_63d_base_v022_signal(ps, sharesbas, closeadj):
    ps = _safe_div(ps, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share ps
def gm_f83_biotech_f83_price_to_sales_ratio_ps_126d_base_v023_signal(ps, sharesbas, closeadj):
    ps = _safe_div(ps, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share ps
def gm_f83_biotech_f83_price_to_sales_ratio_ps_252d_base_v024_signal(ps, sharesbas, closeadj):
    ps = _safe_div(ps, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share ps
def gm_f83_biotech_f83_price_to_sales_ratio_ps_504d_base_v025_signal(ps, sharesbas, closeadj):
    ps = _safe_div(ps, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of ps to revenue
def gm_f83_biotech_f83_price_to_sales_ratio_ratio_revenue_21d_base_v026_signal(ps, revenue):
    ratio = _safe_div(ps, revenue)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of ps to revenue
def gm_f83_biotech_f83_price_to_sales_ratio_ratio_revenue_63d_base_v027_signal(ps, revenue):
    ratio = _safe_div(ps, revenue)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of ps to revenue
def gm_f83_biotech_f83_price_to_sales_ratio_ratio_revenue_126d_base_v028_signal(ps, revenue):
    ratio = _safe_div(ps, revenue)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of ps to revenue
def gm_f83_biotech_f83_price_to_sales_ratio_ratio_revenue_252d_base_v029_signal(ps, revenue):
    ratio = _safe_div(ps, revenue)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of ps to revenue
def gm_f83_biotech_f83_price_to_sales_ratio_ratio_revenue_504d_base_v030_signal(ps, revenue):
    ratio = _safe_div(ps, revenue)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ps scaled by assets
def gm_f83_biotech_f83_price_to_sales_ratio_asset_scaled_21d_base_v031_signal(ps, assets):
    scaled = _safe_div(ps, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ps scaled by assets
def gm_f83_biotech_f83_price_to_sales_ratio_asset_scaled_63d_base_v032_signal(ps, assets):
    scaled = _safe_div(ps, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ps scaled by assets
def gm_f83_biotech_f83_price_to_sales_ratio_asset_scaled_126d_base_v033_signal(ps, assets):
    scaled = _safe_div(ps, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ps scaled by assets
def gm_f83_biotech_f83_price_to_sales_ratio_asset_scaled_252d_base_v034_signal(ps, assets):
    scaled = _safe_div(ps, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ps scaled by assets
def gm_f83_biotech_f83_price_to_sales_ratio_asset_scaled_504d_base_v035_signal(ps, assets):
    scaled = _safe_div(ps, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ps scaled by ps
def gm_f83_biotech_f83_price_to_sales_ratio_mcap_scaled_21d_base_v036_signal(ps):
    scaled = _safe_div(ps, ps)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ps scaled by ps
def gm_f83_biotech_f83_price_to_sales_ratio_mcap_scaled_63d_base_v037_signal(ps):
    scaled = _safe_div(ps, ps)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ps scaled by ps
def gm_f83_biotech_f83_price_to_sales_ratio_mcap_scaled_126d_base_v038_signal(ps):
    scaled = _safe_div(ps, ps)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ps scaled by ps
def gm_f83_biotech_f83_price_to_sales_ratio_mcap_scaled_252d_base_v039_signal(ps):
    scaled = _safe_div(ps, ps)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ps scaled by ps
def gm_f83_biotech_f83_price_to_sales_ratio_mcap_scaled_504d_base_v040_signal(ps):
    scaled = _safe_div(ps, ps)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low ps
def gm_f83_biotech_f83_price_to_sales_ratio_dist_low_21d_base_v041_signal(ps):
    low = ps.rolling(21).min()
    result = _safe_div(ps - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low ps
def gm_f83_biotech_f83_price_to_sales_ratio_dist_low_63d_base_v042_signal(ps):
    low = ps.rolling(63).min()
    result = _safe_div(ps - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low ps
def gm_f83_biotech_f83_price_to_sales_ratio_dist_low_126d_base_v043_signal(ps):
    low = ps.rolling(126).min()
    result = _safe_div(ps - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low ps
def gm_f83_biotech_f83_price_to_sales_ratio_dist_low_252d_base_v044_signal(ps):
    low = ps.rolling(252).min()
    result = _safe_div(ps - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low ps
def gm_f83_biotech_f83_price_to_sales_ratio_dist_low_504d_base_v045_signal(ps):
    low = ps.rolling(504).min()
    result = _safe_div(ps - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high ps
def gm_f83_biotech_f83_price_to_sales_ratio_dist_high_21d_base_v046_signal(ps):
    high = ps.rolling(21).max()
    result = _safe_div(high - ps, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high ps
def gm_f83_biotech_f83_price_to_sales_ratio_dist_high_63d_base_v047_signal(ps):
    high = ps.rolling(63).max()
    result = _safe_div(high - ps, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high ps
def gm_f83_biotech_f83_price_to_sales_ratio_dist_high_126d_base_v048_signal(ps):
    high = ps.rolling(126).max()
    result = _safe_div(high - ps, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high ps
def gm_f83_biotech_f83_price_to_sales_ratio_dist_high_252d_base_v049_signal(ps):
    high = ps.rolling(252).max()
    result = _safe_div(high - ps, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high ps
def gm_f83_biotech_f83_price_to_sales_ratio_dist_high_504d_base_v050_signal(ps):
    high = ps.rolling(504).max()
    result = _safe_div(high - ps, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of ps
def gm_f83_biotech_f83_price_to_sales_ratio_mom_21d_base_v051_signal(ps):
    m1 = _mean(ps, 21)
    m2 = _mean(ps, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of ps
def gm_f83_biotech_f83_price_to_sales_ratio_mom_63d_base_v052_signal(ps):
    m1 = _mean(ps, 63)
    m2 = _mean(ps, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of ps
def gm_f83_biotech_f83_price_to_sales_ratio_mom_126d_base_v053_signal(ps):
    m1 = _mean(ps, 126)
    m2 = _mean(ps, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of ps
def gm_f83_biotech_f83_price_to_sales_ratio_mom_252d_base_v054_signal(ps):
    m1 = _mean(ps, 252)
    m2 = _mean(ps, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of ps
def gm_f83_biotech_f83_price_to_sales_ratio_mom_504d_base_v055_signal(ps):
    m1 = _mean(ps, 504)
    m2 = _mean(ps, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of ps
def gm_f83_biotech_f83_price_to_sales_ratio_skew_21d_base_v056_signal(ps):
    result = _skew(ps, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of ps
def gm_f83_biotech_f83_price_to_sales_ratio_skew_63d_base_v057_signal(ps):
    result = _skew(ps, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of ps
def gm_f83_biotech_f83_price_to_sales_ratio_skew_126d_base_v058_signal(ps):
    result = _skew(ps, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of ps
def gm_f83_biotech_f83_price_to_sales_ratio_skew_252d_base_v059_signal(ps):
    result = _skew(ps, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of ps
def gm_f83_biotech_f83_price_to_sales_ratio_skew_504d_base_v060_signal(ps):
    result = _skew(ps, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of ps
def gm_f83_biotech_f83_price_to_sales_ratio_kurt_21d_base_v061_signal(ps):
    result = _kurt(ps, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of ps
def gm_f83_biotech_f83_price_to_sales_ratio_kurt_63d_base_v062_signal(ps):
    result = _kurt(ps, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of ps
def gm_f83_biotech_f83_price_to_sales_ratio_kurt_126d_base_v063_signal(ps):
    result = _kurt(ps, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of ps
def gm_f83_biotech_f83_price_to_sales_ratio_kurt_252d_base_v064_signal(ps):
    result = _kurt(ps, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of ps
def gm_f83_biotech_f83_price_to_sales_ratio_kurt_504d_base_v065_signal(ps):
    result = _kurt(ps, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of ps
def gm_f83_biotech_f83_price_to_sales_ratio_rank_21d_base_v066_signal(ps, closeadj):
    result = _rank(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of ps
def gm_f83_biotech_f83_price_to_sales_ratio_rank_63d_base_v067_signal(ps, closeadj):
    result = _rank(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of ps
def gm_f83_biotech_f83_price_to_sales_ratio_rank_126d_base_v068_signal(ps, closeadj):
    result = _rank(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of ps
def gm_f83_biotech_f83_price_to_sales_ratio_rank_252d_base_v069_signal(ps, closeadj):
    result = _rank(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of ps
def gm_f83_biotech_f83_price_to_sales_ratio_rank_504d_base_v070_signal(ps, closeadj):
    result = _rank(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of ps
def gm_f83_biotech_f83_price_to_sales_ratio_autocorr_21d_base_v071_signal(ps):
    result = _autocorr(ps, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of ps
def gm_f83_biotech_f83_price_to_sales_ratio_autocorr_63d_base_v072_signal(ps):
    result = _autocorr(ps, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of ps
def gm_f83_biotech_f83_price_to_sales_ratio_autocorr_126d_base_v073_signal(ps):
    result = _autocorr(ps, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of ps
def gm_f83_biotech_f83_price_to_sales_ratio_autocorr_252d_base_v074_signal(ps):
    result = _autocorr(ps, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of ps
def gm_f83_biotech_f83_price_to_sales_ratio_autocorr_504d_base_v075_signal(ps):
    result = _autocorr(ps, 504)
    return result.replace([np.inf, -np.inf], np.nan)

