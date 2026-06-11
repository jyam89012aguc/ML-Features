
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed invcapgrowth
def gm_f55_f55_invcapgrowth_growth_raw_21d_base_v001_signal(invcapgrowth, closeadj):
    result = _mean(invcapgrowth, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed invcapgrowth
def gm_f55_f55_invcapgrowth_growth_raw_63d_base_v002_signal(invcapgrowth, closeadj):
    result = _mean(invcapgrowth, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed invcapgrowth
def gm_f55_f55_invcapgrowth_growth_raw_126d_base_v003_signal(invcapgrowth, closeadj):
    result = _mean(invcapgrowth, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed invcapgrowth
def gm_f55_f55_invcapgrowth_growth_raw_252d_base_v004_signal(invcapgrowth, closeadj):
    result = _mean(invcapgrowth, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed invcapgrowth
def gm_f55_f55_invcapgrowth_growth_raw_504d_base_v005_signal(invcapgrowth, closeadj):
    result = _mean(invcapgrowth, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed invcapgrowth
def gm_f55_f55_invcapgrowth_growth_log_21d_base_v006_signal(invcapgrowth, closeadj):
    result = _mean(_log(invcapgrowth), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed invcapgrowth
def gm_f55_f55_invcapgrowth_growth_log_63d_base_v007_signal(invcapgrowth, closeadj):
    result = _mean(_log(invcapgrowth), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed invcapgrowth
def gm_f55_f55_invcapgrowth_growth_log_126d_base_v008_signal(invcapgrowth, closeadj):
    result = _mean(_log(invcapgrowth), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed invcapgrowth
def gm_f55_f55_invcapgrowth_growth_log_252d_base_v009_signal(invcapgrowth, closeadj):
    result = _mean(_log(invcapgrowth), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed invcapgrowth
def gm_f55_f55_invcapgrowth_growth_log_504d_base_v010_signal(invcapgrowth, closeadj):
    result = _mean(_log(invcapgrowth), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_z_21d_base_v011_signal(invcapgrowth):
    result = _z(invcapgrowth, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_z_63d_base_v012_signal(invcapgrowth):
    result = _z(invcapgrowth, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_z_126d_base_v013_signal(invcapgrowth):
    result = _z(invcapgrowth, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_z_252d_base_v014_signal(invcapgrowth):
    result = _z(invcapgrowth, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_z_504d_base_v015_signal(invcapgrowth):
    result = _z(invcapgrowth, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_pct_21d_base_v016_signal(invcapgrowth):
    result = _pct_change(invcapgrowth, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_pct_63d_base_v017_signal(invcapgrowth):
    result = _pct_change(invcapgrowth, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_pct_126d_base_v018_signal(invcapgrowth):
    result = _pct_change(invcapgrowth, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_pct_252d_base_v019_signal(invcapgrowth):
    result = _pct_change(invcapgrowth, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_pct_504d_base_v020_signal(invcapgrowth):
    result = _pct_change(invcapgrowth, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share invcapgrowth
def gm_f55_f55_invcapgrowth_growth_ps_21d_base_v021_signal(invcapgrowth, sharesbas, closeadj):
    ps = _safe_div(invcapgrowth, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share invcapgrowth
def gm_f55_f55_invcapgrowth_growth_ps_63d_base_v022_signal(invcapgrowth, sharesbas, closeadj):
    ps = _safe_div(invcapgrowth, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share invcapgrowth
def gm_f55_f55_invcapgrowth_growth_ps_126d_base_v023_signal(invcapgrowth, sharesbas, closeadj):
    ps = _safe_div(invcapgrowth, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share invcapgrowth
def gm_f55_f55_invcapgrowth_growth_ps_252d_base_v024_signal(invcapgrowth, sharesbas, closeadj):
    ps = _safe_div(invcapgrowth, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share invcapgrowth
def gm_f55_f55_invcapgrowth_growth_ps_504d_base_v025_signal(invcapgrowth, sharesbas, closeadj):
    ps = _safe_div(invcapgrowth, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d invcapgrowth scaled by assets
def gm_f55_f55_invcapgrowth_growth_asset_scaled_21d_base_v026_signal(invcapgrowth, assets):
    scaled = _safe_div(invcapgrowth, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d invcapgrowth scaled by assets
def gm_f55_f55_invcapgrowth_growth_asset_scaled_63d_base_v027_signal(invcapgrowth, assets):
    scaled = _safe_div(invcapgrowth, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d invcapgrowth scaled by assets
def gm_f55_f55_invcapgrowth_growth_asset_scaled_126d_base_v028_signal(invcapgrowth, assets):
    scaled = _safe_div(invcapgrowth, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d invcapgrowth scaled by assets
def gm_f55_f55_invcapgrowth_growth_asset_scaled_252d_base_v029_signal(invcapgrowth, assets):
    scaled = _safe_div(invcapgrowth, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d invcapgrowth scaled by assets
def gm_f55_f55_invcapgrowth_growth_asset_scaled_504d_base_v030_signal(invcapgrowth, assets):
    scaled = _safe_div(invcapgrowth, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d invcapgrowth scaled by marketcap
def gm_f55_f55_invcapgrowth_growth_mcap_scaled_21d_base_v031_signal(invcapgrowth, marketcap):
    scaled = _safe_div(invcapgrowth, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d invcapgrowth scaled by marketcap
def gm_f55_f55_invcapgrowth_growth_mcap_scaled_63d_base_v032_signal(invcapgrowth, marketcap):
    scaled = _safe_div(invcapgrowth, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d invcapgrowth scaled by marketcap
def gm_f55_f55_invcapgrowth_growth_mcap_scaled_126d_base_v033_signal(invcapgrowth, marketcap):
    scaled = _safe_div(invcapgrowth, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d invcapgrowth scaled by marketcap
def gm_f55_f55_invcapgrowth_growth_mcap_scaled_252d_base_v034_signal(invcapgrowth, marketcap):
    scaled = _safe_div(invcapgrowth, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d invcapgrowth scaled by marketcap
def gm_f55_f55_invcapgrowth_growth_mcap_scaled_504d_base_v035_signal(invcapgrowth, marketcap):
    scaled = _safe_div(invcapgrowth, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low invcapgrowth
def gm_f55_f55_invcapgrowth_growth_dist_low_21d_base_v036_signal(invcapgrowth):
    low = invcapgrowth.rolling(21).min()
    result = _safe_div(invcapgrowth - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low invcapgrowth
def gm_f55_f55_invcapgrowth_growth_dist_low_63d_base_v037_signal(invcapgrowth):
    low = invcapgrowth.rolling(63).min()
    result = _safe_div(invcapgrowth - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low invcapgrowth
def gm_f55_f55_invcapgrowth_growth_dist_low_126d_base_v038_signal(invcapgrowth):
    low = invcapgrowth.rolling(126).min()
    result = _safe_div(invcapgrowth - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low invcapgrowth
def gm_f55_f55_invcapgrowth_growth_dist_low_252d_base_v039_signal(invcapgrowth):
    low = invcapgrowth.rolling(252).min()
    result = _safe_div(invcapgrowth - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low invcapgrowth
def gm_f55_f55_invcapgrowth_growth_dist_low_504d_base_v040_signal(invcapgrowth):
    low = invcapgrowth.rolling(504).min()
    result = _safe_div(invcapgrowth - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high invcapgrowth
def gm_f55_f55_invcapgrowth_growth_dist_high_21d_base_v041_signal(invcapgrowth):
    high = invcapgrowth.rolling(21).max()
    result = _safe_div(high - invcapgrowth, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high invcapgrowth
def gm_f55_f55_invcapgrowth_growth_dist_high_63d_base_v042_signal(invcapgrowth):
    high = invcapgrowth.rolling(63).max()
    result = _safe_div(high - invcapgrowth, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high invcapgrowth
def gm_f55_f55_invcapgrowth_growth_dist_high_126d_base_v043_signal(invcapgrowth):
    high = invcapgrowth.rolling(126).max()
    result = _safe_div(high - invcapgrowth, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high invcapgrowth
def gm_f55_f55_invcapgrowth_growth_dist_high_252d_base_v044_signal(invcapgrowth):
    high = invcapgrowth.rolling(252).max()
    result = _safe_div(high - invcapgrowth, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high invcapgrowth
def gm_f55_f55_invcapgrowth_growth_dist_high_504d_base_v045_signal(invcapgrowth):
    high = invcapgrowth.rolling(504).max()
    result = _safe_div(high - invcapgrowth, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_mom_21d_base_v046_signal(invcapgrowth):
    m1 = _mean(invcapgrowth, 21)
    m2 = _mean(invcapgrowth, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_mom_63d_base_v047_signal(invcapgrowth):
    m1 = _mean(invcapgrowth, 63)
    m2 = _mean(invcapgrowth, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_mom_126d_base_v048_signal(invcapgrowth):
    m1 = _mean(invcapgrowth, 126)
    m2 = _mean(invcapgrowth, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_mom_252d_base_v049_signal(invcapgrowth):
    m1 = _mean(invcapgrowth, 252)
    m2 = _mean(invcapgrowth, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_mom_504d_base_v050_signal(invcapgrowth):
    m1 = _mean(invcapgrowth, 504)
    m2 = _mean(invcapgrowth, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_skew_21d_base_v051_signal(invcapgrowth):
    result = _skew(invcapgrowth, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_skew_63d_base_v052_signal(invcapgrowth):
    result = _skew(invcapgrowth, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_skew_126d_base_v053_signal(invcapgrowth):
    result = _skew(invcapgrowth, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_skew_252d_base_v054_signal(invcapgrowth):
    result = _skew(invcapgrowth, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_skew_504d_base_v055_signal(invcapgrowth):
    result = _skew(invcapgrowth, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_kurt_21d_base_v056_signal(invcapgrowth):
    result = _kurt(invcapgrowth, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_kurt_63d_base_v057_signal(invcapgrowth):
    result = _kurt(invcapgrowth, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_kurt_126d_base_v058_signal(invcapgrowth):
    result = _kurt(invcapgrowth, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_kurt_252d_base_v059_signal(invcapgrowth):
    result = _kurt(invcapgrowth, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_kurt_504d_base_v060_signal(invcapgrowth):
    result = _kurt(invcapgrowth, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_rank_21d_base_v061_signal(invcapgrowth, closeadj):
    result = _rank(invcapgrowth, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_rank_63d_base_v062_signal(invcapgrowth, closeadj):
    result = _rank(invcapgrowth, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_rank_126d_base_v063_signal(invcapgrowth, closeadj):
    result = _rank(invcapgrowth, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_rank_252d_base_v064_signal(invcapgrowth, closeadj):
    result = _rank(invcapgrowth, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_rank_504d_base_v065_signal(invcapgrowth, closeadj):
    result = _rank(invcapgrowth, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_autocorr_21d_base_v066_signal(invcapgrowth):
    result = _autocorr(invcapgrowth, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_autocorr_63d_base_v067_signal(invcapgrowth):
    result = _autocorr(invcapgrowth, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_autocorr_126d_base_v068_signal(invcapgrowth):
    result = _autocorr(invcapgrowth, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_autocorr_252d_base_v069_signal(invcapgrowth):
    result = _autocorr(invcapgrowth, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_autocorr_504d_base_v070_signal(invcapgrowth):
    result = _autocorr(invcapgrowth, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_std_21d_base_v071_signal(invcapgrowth, closeadj):
    result = _std(invcapgrowth, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_std_63d_base_v072_signal(invcapgrowth, closeadj):
    result = _std(invcapgrowth, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_std_126d_base_v073_signal(invcapgrowth, closeadj):
    result = _std(invcapgrowth, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_std_252d_base_v074_signal(invcapgrowth, closeadj):
    result = _std(invcapgrowth, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of invcapgrowth
def gm_f55_f55_invcapgrowth_growth_std_504d_base_v075_signal(invcapgrowth, closeadj):
    result = _std(invcapgrowth, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

