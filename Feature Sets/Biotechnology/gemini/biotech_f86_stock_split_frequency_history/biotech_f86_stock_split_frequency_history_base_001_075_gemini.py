
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed action
def gm_f86_biotech_f86_stock_split_frequency_history_raw_21d_base_v001_signal(action, closeadj):
    result = _mean(action, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed action
def gm_f86_biotech_f86_stock_split_frequency_history_raw_63d_base_v002_signal(action, closeadj):
    result = _mean(action, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed action
def gm_f86_biotech_f86_stock_split_frequency_history_raw_126d_base_v003_signal(action, closeadj):
    result = _mean(action, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed action
def gm_f86_biotech_f86_stock_split_frequency_history_raw_252d_base_v004_signal(action, closeadj):
    result = _mean(action, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed action
def gm_f86_biotech_f86_stock_split_frequency_history_raw_504d_base_v005_signal(action, closeadj):
    result = _mean(action, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed action
def gm_f86_biotech_f86_stock_split_frequency_history_log_21d_base_v006_signal(action, closeadj):
    result = _mean(_log(action), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed action
def gm_f86_biotech_f86_stock_split_frequency_history_log_63d_base_v007_signal(action, closeadj):
    result = _mean(_log(action), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed action
def gm_f86_biotech_f86_stock_split_frequency_history_log_126d_base_v008_signal(action, closeadj):
    result = _mean(_log(action), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed action
def gm_f86_biotech_f86_stock_split_frequency_history_log_252d_base_v009_signal(action, closeadj):
    result = _mean(_log(action), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed action
def gm_f86_biotech_f86_stock_split_frequency_history_log_504d_base_v010_signal(action, closeadj):
    result = _mean(_log(action), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of action
def gm_f86_biotech_f86_stock_split_frequency_history_z_21d_base_v011_signal(action):
    result = _z(action, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of action
def gm_f86_biotech_f86_stock_split_frequency_history_z_63d_base_v012_signal(action):
    result = _z(action, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of action
def gm_f86_biotech_f86_stock_split_frequency_history_z_126d_base_v013_signal(action):
    result = _z(action, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of action
def gm_f86_biotech_f86_stock_split_frequency_history_z_252d_base_v014_signal(action):
    result = _z(action, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of action
def gm_f86_biotech_f86_stock_split_frequency_history_z_504d_base_v015_signal(action):
    result = _z(action, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of action
def gm_f86_biotech_f86_stock_split_frequency_history_pct_21d_base_v016_signal(action):
    result = _pct_change(action, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of action
def gm_f86_biotech_f86_stock_split_frequency_history_pct_63d_base_v017_signal(action):
    result = _pct_change(action, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of action
def gm_f86_biotech_f86_stock_split_frequency_history_pct_126d_base_v018_signal(action):
    result = _pct_change(action, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of action
def gm_f86_biotech_f86_stock_split_frequency_history_pct_252d_base_v019_signal(action):
    result = _pct_change(action, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of action
def gm_f86_biotech_f86_stock_split_frequency_history_pct_504d_base_v020_signal(action):
    result = _pct_change(action, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share action
def gm_f86_biotech_f86_stock_split_frequency_history_ps_21d_base_v021_signal(action, sharesbas, closeadj):
    ps = _safe_div(action, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share action
def gm_f86_biotech_f86_stock_split_frequency_history_ps_63d_base_v022_signal(action, sharesbas, closeadj):
    ps = _safe_div(action, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share action
def gm_f86_biotech_f86_stock_split_frequency_history_ps_126d_base_v023_signal(action, sharesbas, closeadj):
    ps = _safe_div(action, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share action
def gm_f86_biotech_f86_stock_split_frequency_history_ps_252d_base_v024_signal(action, sharesbas, closeadj):
    ps = _safe_div(action, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share action
def gm_f86_biotech_f86_stock_split_frequency_history_ps_504d_base_v025_signal(action, sharesbas, closeadj):
    ps = _safe_div(action, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d action scaled by assets
def gm_f86_biotech_f86_stock_split_frequency_history_asset_scaled_21d_base_v026_signal(action, assets):
    scaled = _safe_div(action, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d action scaled by assets
def gm_f86_biotech_f86_stock_split_frequency_history_asset_scaled_63d_base_v027_signal(action, assets):
    scaled = _safe_div(action, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d action scaled by assets
def gm_f86_biotech_f86_stock_split_frequency_history_asset_scaled_126d_base_v028_signal(action, assets):
    scaled = _safe_div(action, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d action scaled by assets
def gm_f86_biotech_f86_stock_split_frequency_history_asset_scaled_252d_base_v029_signal(action, assets):
    scaled = _safe_div(action, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d action scaled by assets
def gm_f86_biotech_f86_stock_split_frequency_history_asset_scaled_504d_base_v030_signal(action, assets):
    scaled = _safe_div(action, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d action scaled by marketcap
def gm_f86_biotech_f86_stock_split_frequency_history_mcap_scaled_21d_base_v031_signal(action, marketcap):
    scaled = _safe_div(action, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d action scaled by marketcap
def gm_f86_biotech_f86_stock_split_frequency_history_mcap_scaled_63d_base_v032_signal(action, marketcap):
    scaled = _safe_div(action, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d action scaled by marketcap
def gm_f86_biotech_f86_stock_split_frequency_history_mcap_scaled_126d_base_v033_signal(action, marketcap):
    scaled = _safe_div(action, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d action scaled by marketcap
def gm_f86_biotech_f86_stock_split_frequency_history_mcap_scaled_252d_base_v034_signal(action, marketcap):
    scaled = _safe_div(action, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d action scaled by marketcap
def gm_f86_biotech_f86_stock_split_frequency_history_mcap_scaled_504d_base_v035_signal(action, marketcap):
    scaled = _safe_div(action, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low action
def gm_f86_biotech_f86_stock_split_frequency_history_dist_low_21d_base_v036_signal(action):
    low = action.rolling(21).min()
    result = _safe_div(action - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low action
def gm_f86_biotech_f86_stock_split_frequency_history_dist_low_63d_base_v037_signal(action):
    low = action.rolling(63).min()
    result = _safe_div(action - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low action
def gm_f86_biotech_f86_stock_split_frequency_history_dist_low_126d_base_v038_signal(action):
    low = action.rolling(126).min()
    result = _safe_div(action - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low action
def gm_f86_biotech_f86_stock_split_frequency_history_dist_low_252d_base_v039_signal(action):
    low = action.rolling(252).min()
    result = _safe_div(action - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low action
def gm_f86_biotech_f86_stock_split_frequency_history_dist_low_504d_base_v040_signal(action):
    low = action.rolling(504).min()
    result = _safe_div(action - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high action
def gm_f86_biotech_f86_stock_split_frequency_history_dist_high_21d_base_v041_signal(action):
    high = action.rolling(21).max()
    result = _safe_div(high - action, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high action
def gm_f86_biotech_f86_stock_split_frequency_history_dist_high_63d_base_v042_signal(action):
    high = action.rolling(63).max()
    result = _safe_div(high - action, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high action
def gm_f86_biotech_f86_stock_split_frequency_history_dist_high_126d_base_v043_signal(action):
    high = action.rolling(126).max()
    result = _safe_div(high - action, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high action
def gm_f86_biotech_f86_stock_split_frequency_history_dist_high_252d_base_v044_signal(action):
    high = action.rolling(252).max()
    result = _safe_div(high - action, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high action
def gm_f86_biotech_f86_stock_split_frequency_history_dist_high_504d_base_v045_signal(action):
    high = action.rolling(504).max()
    result = _safe_div(high - action, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of action
def gm_f86_biotech_f86_stock_split_frequency_history_mom_21d_base_v046_signal(action):
    m1 = _mean(action, 21)
    m2 = _mean(action, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of action
def gm_f86_biotech_f86_stock_split_frequency_history_mom_63d_base_v047_signal(action):
    m1 = _mean(action, 63)
    m2 = _mean(action, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of action
def gm_f86_biotech_f86_stock_split_frequency_history_mom_126d_base_v048_signal(action):
    m1 = _mean(action, 126)
    m2 = _mean(action, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of action
def gm_f86_biotech_f86_stock_split_frequency_history_mom_252d_base_v049_signal(action):
    m1 = _mean(action, 252)
    m2 = _mean(action, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of action
def gm_f86_biotech_f86_stock_split_frequency_history_mom_504d_base_v050_signal(action):
    m1 = _mean(action, 504)
    m2 = _mean(action, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of action
def gm_f86_biotech_f86_stock_split_frequency_history_skew_21d_base_v051_signal(action):
    result = _skew(action, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of action
def gm_f86_biotech_f86_stock_split_frequency_history_skew_63d_base_v052_signal(action):
    result = _skew(action, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of action
def gm_f86_biotech_f86_stock_split_frequency_history_skew_126d_base_v053_signal(action):
    result = _skew(action, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of action
def gm_f86_biotech_f86_stock_split_frequency_history_skew_252d_base_v054_signal(action):
    result = _skew(action, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of action
def gm_f86_biotech_f86_stock_split_frequency_history_skew_504d_base_v055_signal(action):
    result = _skew(action, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of action
def gm_f86_biotech_f86_stock_split_frequency_history_kurt_21d_base_v056_signal(action):
    result = _kurt(action, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of action
def gm_f86_biotech_f86_stock_split_frequency_history_kurt_63d_base_v057_signal(action):
    result = _kurt(action, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of action
def gm_f86_biotech_f86_stock_split_frequency_history_kurt_126d_base_v058_signal(action):
    result = _kurt(action, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of action
def gm_f86_biotech_f86_stock_split_frequency_history_kurt_252d_base_v059_signal(action):
    result = _kurt(action, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of action
def gm_f86_biotech_f86_stock_split_frequency_history_kurt_504d_base_v060_signal(action):
    result = _kurt(action, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of action
def gm_f86_biotech_f86_stock_split_frequency_history_rank_21d_base_v061_signal(action, closeadj):
    result = _rank(action, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of action
def gm_f86_biotech_f86_stock_split_frequency_history_rank_63d_base_v062_signal(action, closeadj):
    result = _rank(action, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of action
def gm_f86_biotech_f86_stock_split_frequency_history_rank_126d_base_v063_signal(action, closeadj):
    result = _rank(action, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of action
def gm_f86_biotech_f86_stock_split_frequency_history_rank_252d_base_v064_signal(action, closeadj):
    result = _rank(action, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of action
def gm_f86_biotech_f86_stock_split_frequency_history_rank_504d_base_v065_signal(action, closeadj):
    result = _rank(action, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of action
def gm_f86_biotech_f86_stock_split_frequency_history_autocorr_21d_base_v066_signal(action):
    result = _autocorr(action, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of action
def gm_f86_biotech_f86_stock_split_frequency_history_autocorr_63d_base_v067_signal(action):
    result = _autocorr(action, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of action
def gm_f86_biotech_f86_stock_split_frequency_history_autocorr_126d_base_v068_signal(action):
    result = _autocorr(action, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of action
def gm_f86_biotech_f86_stock_split_frequency_history_autocorr_252d_base_v069_signal(action):
    result = _autocorr(action, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of action
def gm_f86_biotech_f86_stock_split_frequency_history_autocorr_504d_base_v070_signal(action):
    result = _autocorr(action, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of action
def gm_f86_biotech_f86_stock_split_frequency_history_std_21d_base_v071_signal(action, closeadj):
    result = _std(action, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of action
def gm_f86_biotech_f86_stock_split_frequency_history_std_63d_base_v072_signal(action, closeadj):
    result = _std(action, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of action
def gm_f86_biotech_f86_stock_split_frequency_history_std_126d_base_v073_signal(action, closeadj):
    result = _std(action, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of action
def gm_f86_biotech_f86_stock_split_frequency_history_std_252d_base_v074_signal(action, closeadj):
    result = _std(action, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of action
def gm_f86_biotech_f86_stock_split_frequency_history_std_504d_base_v075_signal(action, closeadj):
    result = _std(action, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

