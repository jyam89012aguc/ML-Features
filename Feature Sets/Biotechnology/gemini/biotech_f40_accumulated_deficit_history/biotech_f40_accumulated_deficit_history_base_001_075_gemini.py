
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_21d_base_v001_signal(retearn, closeadj):
    result = _mean(retearn, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_63d_base_v002_signal(retearn, closeadj):
    result = _mean(retearn, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_126d_base_v003_signal(retearn, closeadj):
    result = _mean(retearn, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_252d_base_v004_signal(retearn, closeadj):
    result = _mean(retearn, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_504d_base_v005_signal(retearn, closeadj):
    result = _mean(retearn, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_21d_base_v006_signal(retearn, closeadj):
    result = _mean(_log(retearn), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_63d_base_v007_signal(retearn, closeadj):
    result = _mean(_log(retearn), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_126d_base_v008_signal(retearn, closeadj):
    result = _mean(_log(retearn), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_252d_base_v009_signal(retearn, closeadj):
    result = _mean(_log(retearn), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_504d_base_v010_signal(retearn, closeadj):
    result = _mean(_log(retearn), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_21d_base_v011_signal(retearn):
    result = _z(retearn, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_63d_base_v012_signal(retearn):
    result = _z(retearn, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_126d_base_v013_signal(retearn):
    result = _z(retearn, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_252d_base_v014_signal(retearn):
    result = _z(retearn, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_504d_base_v015_signal(retearn):
    result = _z(retearn, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_pct_21d_base_v016_signal(retearn):
    result = _pct_change(retearn, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_pct_63d_base_v017_signal(retearn):
    result = _pct_change(retearn, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_pct_126d_base_v018_signal(retearn):
    result = _pct_change(retearn, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_pct_252d_base_v019_signal(retearn):
    result = _pct_change(retearn, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_pct_504d_base_v020_signal(retearn):
    result = _pct_change(retearn, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_21d_base_v021_signal(retearn, sharesbas, closeadj):
    ps = _safe_div(retearn, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_63d_base_v022_signal(retearn, sharesbas, closeadj):
    ps = _safe_div(retearn, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_126d_base_v023_signal(retearn, sharesbas, closeadj):
    ps = _safe_div(retearn, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_252d_base_v024_signal(retearn, sharesbas, closeadj):
    ps = _safe_div(retearn, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_504d_base_v025_signal(retearn, sharesbas, closeadj):
    ps = _safe_div(retearn, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d retearn scaled by assets
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_21d_base_v026_signal(retearn, assets):
    scaled = _safe_div(retearn, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d retearn scaled by assets
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_63d_base_v027_signal(retearn, assets):
    scaled = _safe_div(retearn, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d retearn scaled by assets
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_126d_base_v028_signal(retearn, assets):
    scaled = _safe_div(retearn, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d retearn scaled by assets
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_252d_base_v029_signal(retearn, assets):
    scaled = _safe_div(retearn, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d retearn scaled by assets
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_504d_base_v030_signal(retearn, assets):
    scaled = _safe_div(retearn, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d retearn scaled by marketcap
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_21d_base_v031_signal(retearn, marketcap):
    scaled = _safe_div(retearn, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d retearn scaled by marketcap
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_63d_base_v032_signal(retearn, marketcap):
    scaled = _safe_div(retearn, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d retearn scaled by marketcap
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_126d_base_v033_signal(retearn, marketcap):
    scaled = _safe_div(retearn, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d retearn scaled by marketcap
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_252d_base_v034_signal(retearn, marketcap):
    scaled = _safe_div(retearn, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d retearn scaled by marketcap
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_504d_base_v035_signal(retearn, marketcap):
    scaled = _safe_div(retearn, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_21d_base_v036_signal(retearn):
    low = retearn.rolling(21).min()
    result = _safe_div(retearn - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_63d_base_v037_signal(retearn):
    low = retearn.rolling(63).min()
    result = _safe_div(retearn - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_126d_base_v038_signal(retearn):
    low = retearn.rolling(126).min()
    result = _safe_div(retearn - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_252d_base_v039_signal(retearn):
    low = retearn.rolling(252).min()
    result = _safe_div(retearn - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_504d_base_v040_signal(retearn):
    low = retearn.rolling(504).min()
    result = _safe_div(retearn - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_21d_base_v041_signal(retearn):
    high = retearn.rolling(21).max()
    result = _safe_div(high - retearn, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_63d_base_v042_signal(retearn):
    high = retearn.rolling(63).max()
    result = _safe_div(high - retearn, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_126d_base_v043_signal(retearn):
    high = retearn.rolling(126).max()
    result = _safe_div(high - retearn, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_252d_base_v044_signal(retearn):
    high = retearn.rolling(252).max()
    result = _safe_div(high - retearn, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_504d_base_v045_signal(retearn):
    high = retearn.rolling(504).max()
    result = _safe_div(high - retearn, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_21d_base_v046_signal(retearn):
    m1 = _mean(retearn, 21)
    m2 = _mean(retearn, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_63d_base_v047_signal(retearn):
    m1 = _mean(retearn, 63)
    m2 = _mean(retearn, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_126d_base_v048_signal(retearn):
    m1 = _mean(retearn, 126)
    m2 = _mean(retearn, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_252d_base_v049_signal(retearn):
    m1 = _mean(retearn, 252)
    m2 = _mean(retearn, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_504d_base_v050_signal(retearn):
    m1 = _mean(retearn, 504)
    m2 = _mean(retearn, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_skew_21d_base_v051_signal(retearn):
    result = _skew(retearn, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_skew_63d_base_v052_signal(retearn):
    result = _skew(retearn, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_skew_126d_base_v053_signal(retearn):
    result = _skew(retearn, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_skew_252d_base_v054_signal(retearn):
    result = _skew(retearn, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_skew_504d_base_v055_signal(retearn):
    result = _skew(retearn, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_kurt_21d_base_v056_signal(retearn):
    result = _kurt(retearn, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_kurt_63d_base_v057_signal(retearn):
    result = _kurt(retearn, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_kurt_126d_base_v058_signal(retearn):
    result = _kurt(retearn, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_kurt_252d_base_v059_signal(retearn):
    result = _kurt(retearn, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_kurt_504d_base_v060_signal(retearn):
    result = _kurt(retearn, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_rank_21d_base_v061_signal(retearn, closeadj):
    result = _rank(retearn, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_rank_63d_base_v062_signal(retearn, closeadj):
    result = _rank(retearn, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_rank_126d_base_v063_signal(retearn, closeadj):
    result = _rank(retearn, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_rank_252d_base_v064_signal(retearn, closeadj):
    result = _rank(retearn, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_rank_504d_base_v065_signal(retearn, closeadj):
    result = _rank(retearn, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_autocorr_21d_base_v066_signal(retearn):
    result = _autocorr(retearn, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_autocorr_63d_base_v067_signal(retearn):
    result = _autocorr(retearn, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_autocorr_126d_base_v068_signal(retearn):
    result = _autocorr(retearn, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_autocorr_252d_base_v069_signal(retearn):
    result = _autocorr(retearn, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_autocorr_504d_base_v070_signal(retearn):
    result = _autocorr(retearn, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_std_21d_base_v071_signal(retearn, closeadj):
    result = _std(retearn, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_std_63d_base_v072_signal(retearn, closeadj):
    result = _std(retearn, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_std_126d_base_v073_signal(retearn, closeadj):
    result = _std(retearn, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_std_252d_base_v074_signal(retearn, closeadj):
    result = _std(retearn, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of retearn
def gm_f40_biotech_f40_accumulated_deficit_history_std_504d_base_v075_signal(retearn, closeadj):
    result = _std(retearn, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

