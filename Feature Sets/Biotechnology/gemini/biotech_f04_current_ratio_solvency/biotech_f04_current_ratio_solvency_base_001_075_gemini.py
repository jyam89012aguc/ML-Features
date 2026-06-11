
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_21d_base_v001_signal(currentratio, closeadj):
    result = _mean(currentratio, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_63d_base_v002_signal(currentratio, closeadj):
    result = _mean(currentratio, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_126d_base_v003_signal(currentratio, closeadj):
    result = _mean(currentratio, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_252d_base_v004_signal(currentratio, closeadj):
    result = _mean(currentratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_504d_base_v005_signal(currentratio, closeadj):
    result = _mean(currentratio, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_21d_base_v006_signal(currentratio, closeadj):
    result = _mean(_log(currentratio), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_63d_base_v007_signal(currentratio, closeadj):
    result = _mean(_log(currentratio), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_126d_base_v008_signal(currentratio, closeadj):
    result = _mean(_log(currentratio), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_252d_base_v009_signal(currentratio, closeadj):
    result = _mean(_log(currentratio), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_504d_base_v010_signal(currentratio, closeadj):
    result = _mean(_log(currentratio), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_21d_base_v011_signal(currentratio):
    result = _z(currentratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_63d_base_v012_signal(currentratio):
    result = _z(currentratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_126d_base_v013_signal(currentratio):
    result = _z(currentratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_252d_base_v014_signal(currentratio):
    result = _z(currentratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_504d_base_v015_signal(currentratio):
    result = _z(currentratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_pct_21d_base_v016_signal(currentratio):
    result = _pct_change(currentratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_pct_63d_base_v017_signal(currentratio):
    result = _pct_change(currentratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_pct_126d_base_v018_signal(currentratio):
    result = _pct_change(currentratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_pct_252d_base_v019_signal(currentratio):
    result = _pct_change(currentratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_pct_504d_base_v020_signal(currentratio):
    result = _pct_change(currentratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_21d_base_v021_signal(currentratio, sharesbas, closeadj):
    ps = _safe_div(currentratio, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_63d_base_v022_signal(currentratio, sharesbas, closeadj):
    ps = _safe_div(currentratio, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_126d_base_v023_signal(currentratio, sharesbas, closeadj):
    ps = _safe_div(currentratio, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_252d_base_v024_signal(currentratio, sharesbas, closeadj):
    ps = _safe_div(currentratio, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_504d_base_v025_signal(currentratio, sharesbas, closeadj):
    ps = _safe_div(currentratio, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d currentratio scaled by assets
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_21d_base_v026_signal(currentratio, assets):
    scaled = _safe_div(currentratio, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d currentratio scaled by assets
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_63d_base_v027_signal(currentratio, assets):
    scaled = _safe_div(currentratio, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d currentratio scaled by assets
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_126d_base_v028_signal(currentratio, assets):
    scaled = _safe_div(currentratio, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d currentratio scaled by assets
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_252d_base_v029_signal(currentratio, assets):
    scaled = _safe_div(currentratio, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d currentratio scaled by assets
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_504d_base_v030_signal(currentratio, assets):
    scaled = _safe_div(currentratio, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d currentratio scaled by marketcap
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_21d_base_v031_signal(currentratio, marketcap):
    scaled = _safe_div(currentratio, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d currentratio scaled by marketcap
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_63d_base_v032_signal(currentratio, marketcap):
    scaled = _safe_div(currentratio, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d currentratio scaled by marketcap
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_126d_base_v033_signal(currentratio, marketcap):
    scaled = _safe_div(currentratio, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d currentratio scaled by marketcap
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_252d_base_v034_signal(currentratio, marketcap):
    scaled = _safe_div(currentratio, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d currentratio scaled by marketcap
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_504d_base_v035_signal(currentratio, marketcap):
    scaled = _safe_div(currentratio, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_21d_base_v036_signal(currentratio):
    low = currentratio.rolling(21).min()
    result = _safe_div(currentratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_63d_base_v037_signal(currentratio):
    low = currentratio.rolling(63).min()
    result = _safe_div(currentratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_126d_base_v038_signal(currentratio):
    low = currentratio.rolling(126).min()
    result = _safe_div(currentratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_252d_base_v039_signal(currentratio):
    low = currentratio.rolling(252).min()
    result = _safe_div(currentratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_504d_base_v040_signal(currentratio):
    low = currentratio.rolling(504).min()
    result = _safe_div(currentratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_21d_base_v041_signal(currentratio):
    high = currentratio.rolling(21).max()
    result = _safe_div(high - currentratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_63d_base_v042_signal(currentratio):
    high = currentratio.rolling(63).max()
    result = _safe_div(high - currentratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_126d_base_v043_signal(currentratio):
    high = currentratio.rolling(126).max()
    result = _safe_div(high - currentratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_252d_base_v044_signal(currentratio):
    high = currentratio.rolling(252).max()
    result = _safe_div(high - currentratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_504d_base_v045_signal(currentratio):
    high = currentratio.rolling(504).max()
    result = _safe_div(high - currentratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_21d_base_v046_signal(currentratio):
    m1 = _mean(currentratio, 21)
    m2 = _mean(currentratio, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_63d_base_v047_signal(currentratio):
    m1 = _mean(currentratio, 63)
    m2 = _mean(currentratio, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_126d_base_v048_signal(currentratio):
    m1 = _mean(currentratio, 126)
    m2 = _mean(currentratio, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_252d_base_v049_signal(currentratio):
    m1 = _mean(currentratio, 252)
    m2 = _mean(currentratio, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_504d_base_v050_signal(currentratio):
    m1 = _mean(currentratio, 504)
    m2 = _mean(currentratio, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_skew_21d_base_v051_signal(currentratio):
    result = _skew(currentratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_skew_63d_base_v052_signal(currentratio):
    result = _skew(currentratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_skew_126d_base_v053_signal(currentratio):
    result = _skew(currentratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_skew_252d_base_v054_signal(currentratio):
    result = _skew(currentratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_skew_504d_base_v055_signal(currentratio):
    result = _skew(currentratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_kurt_21d_base_v056_signal(currentratio):
    result = _kurt(currentratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_kurt_63d_base_v057_signal(currentratio):
    result = _kurt(currentratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_kurt_126d_base_v058_signal(currentratio):
    result = _kurt(currentratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_kurt_252d_base_v059_signal(currentratio):
    result = _kurt(currentratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_kurt_504d_base_v060_signal(currentratio):
    result = _kurt(currentratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_rank_21d_base_v061_signal(currentratio, closeadj):
    result = _rank(currentratio, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_rank_63d_base_v062_signal(currentratio, closeadj):
    result = _rank(currentratio, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_rank_126d_base_v063_signal(currentratio, closeadj):
    result = _rank(currentratio, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_rank_252d_base_v064_signal(currentratio, closeadj):
    result = _rank(currentratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_rank_504d_base_v065_signal(currentratio, closeadj):
    result = _rank(currentratio, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_autocorr_21d_base_v066_signal(currentratio):
    result = _autocorr(currentratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_autocorr_63d_base_v067_signal(currentratio):
    result = _autocorr(currentratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_autocorr_126d_base_v068_signal(currentratio):
    result = _autocorr(currentratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_autocorr_252d_base_v069_signal(currentratio):
    result = _autocorr(currentratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_autocorr_504d_base_v070_signal(currentratio):
    result = _autocorr(currentratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_std_21d_base_v071_signal(currentratio, closeadj):
    result = _std(currentratio, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_std_63d_base_v072_signal(currentratio, closeadj):
    result = _std(currentratio, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_std_126d_base_v073_signal(currentratio, closeadj):
    result = _std(currentratio, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_std_252d_base_v074_signal(currentratio, closeadj):
    result = _std(currentratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of currentratio
def gm_f04_biotech_f04_current_ratio_solvency_std_504d_base_v075_signal(currentratio, closeadj):
    result = _std(currentratio, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

