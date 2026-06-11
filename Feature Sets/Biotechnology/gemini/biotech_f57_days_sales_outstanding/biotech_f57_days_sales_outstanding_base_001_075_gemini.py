
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed dso
def gm_f57_biotech_f57_days_sales_outstanding_raw_21d_base_v001_signal(dso, closeadj):
    result = _mean(dso, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed dso
def gm_f57_biotech_f57_days_sales_outstanding_raw_63d_base_v002_signal(dso, closeadj):
    result = _mean(dso, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed dso
def gm_f57_biotech_f57_days_sales_outstanding_raw_126d_base_v003_signal(dso, closeadj):
    result = _mean(dso, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed dso
def gm_f57_biotech_f57_days_sales_outstanding_raw_252d_base_v004_signal(dso, closeadj):
    result = _mean(dso, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed dso
def gm_f57_biotech_f57_days_sales_outstanding_raw_504d_base_v005_signal(dso, closeadj):
    result = _mean(dso, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed dso
def gm_f57_biotech_f57_days_sales_outstanding_log_21d_base_v006_signal(dso, closeadj):
    result = _mean(_log(dso), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed dso
def gm_f57_biotech_f57_days_sales_outstanding_log_63d_base_v007_signal(dso, closeadj):
    result = _mean(_log(dso), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed dso
def gm_f57_biotech_f57_days_sales_outstanding_log_126d_base_v008_signal(dso, closeadj):
    result = _mean(_log(dso), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed dso
def gm_f57_biotech_f57_days_sales_outstanding_log_252d_base_v009_signal(dso, closeadj):
    result = _mean(_log(dso), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed dso
def gm_f57_biotech_f57_days_sales_outstanding_log_504d_base_v010_signal(dso, closeadj):
    result = _mean(_log(dso), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of dso
def gm_f57_biotech_f57_days_sales_outstanding_z_21d_base_v011_signal(dso):
    result = _z(dso, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dso
def gm_f57_biotech_f57_days_sales_outstanding_z_63d_base_v012_signal(dso):
    result = _z(dso, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dso
def gm_f57_biotech_f57_days_sales_outstanding_z_126d_base_v013_signal(dso):
    result = _z(dso, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dso
def gm_f57_biotech_f57_days_sales_outstanding_z_252d_base_v014_signal(dso):
    result = _z(dso, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dso
def gm_f57_biotech_f57_days_sales_outstanding_z_504d_base_v015_signal(dso):
    result = _z(dso, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of dso
def gm_f57_biotech_f57_days_sales_outstanding_pct_21d_base_v016_signal(dso):
    result = _pct_change(dso, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of dso
def gm_f57_biotech_f57_days_sales_outstanding_pct_63d_base_v017_signal(dso):
    result = _pct_change(dso, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of dso
def gm_f57_biotech_f57_days_sales_outstanding_pct_126d_base_v018_signal(dso):
    result = _pct_change(dso, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of dso
def gm_f57_biotech_f57_days_sales_outstanding_pct_252d_base_v019_signal(dso):
    result = _pct_change(dso, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of dso
def gm_f57_biotech_f57_days_sales_outstanding_pct_504d_base_v020_signal(dso):
    result = _pct_change(dso, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share dso
def gm_f57_biotech_f57_days_sales_outstanding_ps_21d_base_v021_signal(dso, sharesbas, closeadj):
    ps = _safe_div(dso, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share dso
def gm_f57_biotech_f57_days_sales_outstanding_ps_63d_base_v022_signal(dso, sharesbas, closeadj):
    ps = _safe_div(dso, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share dso
def gm_f57_biotech_f57_days_sales_outstanding_ps_126d_base_v023_signal(dso, sharesbas, closeadj):
    ps = _safe_div(dso, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share dso
def gm_f57_biotech_f57_days_sales_outstanding_ps_252d_base_v024_signal(dso, sharesbas, closeadj):
    ps = _safe_div(dso, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share dso
def gm_f57_biotech_f57_days_sales_outstanding_ps_504d_base_v025_signal(dso, sharesbas, closeadj):
    ps = _safe_div(dso, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of dso to revenue
def gm_f57_biotech_f57_days_sales_outstanding_ratio_revenue_21d_base_v026_signal(dso, revenue):
    ratio = _safe_div(dso, revenue)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of dso to revenue
def gm_f57_biotech_f57_days_sales_outstanding_ratio_revenue_63d_base_v027_signal(dso, revenue):
    ratio = _safe_div(dso, revenue)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of dso to revenue
def gm_f57_biotech_f57_days_sales_outstanding_ratio_revenue_126d_base_v028_signal(dso, revenue):
    ratio = _safe_div(dso, revenue)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of dso to revenue
def gm_f57_biotech_f57_days_sales_outstanding_ratio_revenue_252d_base_v029_signal(dso, revenue):
    ratio = _safe_div(dso, revenue)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of dso to revenue
def gm_f57_biotech_f57_days_sales_outstanding_ratio_revenue_504d_base_v030_signal(dso, revenue):
    ratio = _safe_div(dso, revenue)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d dso scaled by assets
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_21d_base_v031_signal(dso, assets):
    scaled = _safe_div(dso, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d dso scaled by assets
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_63d_base_v032_signal(dso, assets):
    scaled = _safe_div(dso, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d dso scaled by assets
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_126d_base_v033_signal(dso, assets):
    scaled = _safe_div(dso, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d dso scaled by assets
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_252d_base_v034_signal(dso, assets):
    scaled = _safe_div(dso, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d dso scaled by assets
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_504d_base_v035_signal(dso, assets):
    scaled = _safe_div(dso, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d dso scaled by marketcap
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_21d_base_v036_signal(dso, marketcap):
    scaled = _safe_div(dso, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d dso scaled by marketcap
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_63d_base_v037_signal(dso, marketcap):
    scaled = _safe_div(dso, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d dso scaled by marketcap
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_126d_base_v038_signal(dso, marketcap):
    scaled = _safe_div(dso, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d dso scaled by marketcap
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_252d_base_v039_signal(dso, marketcap):
    scaled = _safe_div(dso, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d dso scaled by marketcap
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_504d_base_v040_signal(dso, marketcap):
    scaled = _safe_div(dso, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low dso
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_21d_base_v041_signal(dso):
    low = dso.rolling(21).min()
    result = _safe_div(dso - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low dso
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_63d_base_v042_signal(dso):
    low = dso.rolling(63).min()
    result = _safe_div(dso - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low dso
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_126d_base_v043_signal(dso):
    low = dso.rolling(126).min()
    result = _safe_div(dso - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low dso
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_252d_base_v044_signal(dso):
    low = dso.rolling(252).min()
    result = _safe_div(dso - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low dso
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_504d_base_v045_signal(dso):
    low = dso.rolling(504).min()
    result = _safe_div(dso - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high dso
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_21d_base_v046_signal(dso):
    high = dso.rolling(21).max()
    result = _safe_div(high - dso, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high dso
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_63d_base_v047_signal(dso):
    high = dso.rolling(63).max()
    result = _safe_div(high - dso, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high dso
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_126d_base_v048_signal(dso):
    high = dso.rolling(126).max()
    result = _safe_div(high - dso, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high dso
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_252d_base_v049_signal(dso):
    high = dso.rolling(252).max()
    result = _safe_div(high - dso, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high dso
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_504d_base_v050_signal(dso):
    high = dso.rolling(504).max()
    result = _safe_div(high - dso, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of dso
def gm_f57_biotech_f57_days_sales_outstanding_mom_21d_base_v051_signal(dso):
    m1 = _mean(dso, 21)
    m2 = _mean(dso, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of dso
def gm_f57_biotech_f57_days_sales_outstanding_mom_63d_base_v052_signal(dso):
    m1 = _mean(dso, 63)
    m2 = _mean(dso, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of dso
def gm_f57_biotech_f57_days_sales_outstanding_mom_126d_base_v053_signal(dso):
    m1 = _mean(dso, 126)
    m2 = _mean(dso, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of dso
def gm_f57_biotech_f57_days_sales_outstanding_mom_252d_base_v054_signal(dso):
    m1 = _mean(dso, 252)
    m2 = _mean(dso, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of dso
def gm_f57_biotech_f57_days_sales_outstanding_mom_504d_base_v055_signal(dso):
    m1 = _mean(dso, 504)
    m2 = _mean(dso, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of dso
def gm_f57_biotech_f57_days_sales_outstanding_skew_21d_base_v056_signal(dso):
    result = _skew(dso, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of dso
def gm_f57_biotech_f57_days_sales_outstanding_skew_63d_base_v057_signal(dso):
    result = _skew(dso, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of dso
def gm_f57_biotech_f57_days_sales_outstanding_skew_126d_base_v058_signal(dso):
    result = _skew(dso, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of dso
def gm_f57_biotech_f57_days_sales_outstanding_skew_252d_base_v059_signal(dso):
    result = _skew(dso, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of dso
def gm_f57_biotech_f57_days_sales_outstanding_skew_504d_base_v060_signal(dso):
    result = _skew(dso, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of dso
def gm_f57_biotech_f57_days_sales_outstanding_kurt_21d_base_v061_signal(dso):
    result = _kurt(dso, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of dso
def gm_f57_biotech_f57_days_sales_outstanding_kurt_63d_base_v062_signal(dso):
    result = _kurt(dso, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of dso
def gm_f57_biotech_f57_days_sales_outstanding_kurt_126d_base_v063_signal(dso):
    result = _kurt(dso, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of dso
def gm_f57_biotech_f57_days_sales_outstanding_kurt_252d_base_v064_signal(dso):
    result = _kurt(dso, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of dso
def gm_f57_biotech_f57_days_sales_outstanding_kurt_504d_base_v065_signal(dso):
    result = _kurt(dso, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of dso
def gm_f57_biotech_f57_days_sales_outstanding_rank_21d_base_v066_signal(dso, closeadj):
    result = _rank(dso, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of dso
def gm_f57_biotech_f57_days_sales_outstanding_rank_63d_base_v067_signal(dso, closeadj):
    result = _rank(dso, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of dso
def gm_f57_biotech_f57_days_sales_outstanding_rank_126d_base_v068_signal(dso, closeadj):
    result = _rank(dso, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of dso
def gm_f57_biotech_f57_days_sales_outstanding_rank_252d_base_v069_signal(dso, closeadj):
    result = _rank(dso, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of dso
def gm_f57_biotech_f57_days_sales_outstanding_rank_504d_base_v070_signal(dso, closeadj):
    result = _rank(dso, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of dso
def gm_f57_biotech_f57_days_sales_outstanding_autocorr_21d_base_v071_signal(dso):
    result = _autocorr(dso, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of dso
def gm_f57_biotech_f57_days_sales_outstanding_autocorr_63d_base_v072_signal(dso):
    result = _autocorr(dso, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of dso
def gm_f57_biotech_f57_days_sales_outstanding_autocorr_126d_base_v073_signal(dso):
    result = _autocorr(dso, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of dso
def gm_f57_biotech_f57_days_sales_outstanding_autocorr_252d_base_v074_signal(dso):
    result = _autocorr(dso, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of dso
def gm_f57_biotech_f57_days_sales_outstanding_autocorr_504d_base_v075_signal(dso):
    result = _autocorr(dso, 504)
    return result.replace([np.inf, -np.inf], np.nan)

