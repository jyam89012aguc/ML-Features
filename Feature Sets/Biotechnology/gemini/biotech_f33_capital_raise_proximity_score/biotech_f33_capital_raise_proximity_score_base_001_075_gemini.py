
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_raw_21d_base_v001_signal(ncfcommon, closeadj):
    result = _mean(ncfcommon, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_raw_63d_base_v002_signal(ncfcommon, closeadj):
    result = _mean(ncfcommon, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_raw_126d_base_v003_signal(ncfcommon, closeadj):
    result = _mean(ncfcommon, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_raw_252d_base_v004_signal(ncfcommon, closeadj):
    result = _mean(ncfcommon, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_raw_504d_base_v005_signal(ncfcommon, closeadj):
    result = _mean(ncfcommon, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_log_21d_base_v006_signal(ncfcommon, closeadj):
    result = _mean(_log(ncfcommon), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_log_63d_base_v007_signal(ncfcommon, closeadj):
    result = _mean(_log(ncfcommon), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_log_126d_base_v008_signal(ncfcommon, closeadj):
    result = _mean(_log(ncfcommon), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_log_252d_base_v009_signal(ncfcommon, closeadj):
    result = _mean(_log(ncfcommon), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_log_504d_base_v010_signal(ncfcommon, closeadj):
    result = _mean(_log(ncfcommon), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_z_21d_base_v011_signal(ncfcommon):
    result = _z(ncfcommon, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_z_63d_base_v012_signal(ncfcommon):
    result = _z(ncfcommon, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_z_126d_base_v013_signal(ncfcommon):
    result = _z(ncfcommon, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_z_252d_base_v014_signal(ncfcommon):
    result = _z(ncfcommon, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_z_504d_base_v015_signal(ncfcommon):
    result = _z(ncfcommon, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_pct_21d_base_v016_signal(ncfcommon):
    result = _pct_change(ncfcommon, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_pct_63d_base_v017_signal(ncfcommon):
    result = _pct_change(ncfcommon, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_pct_126d_base_v018_signal(ncfcommon):
    result = _pct_change(ncfcommon, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_pct_252d_base_v019_signal(ncfcommon):
    result = _pct_change(ncfcommon, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_pct_504d_base_v020_signal(ncfcommon):
    result = _pct_change(ncfcommon, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_ps_21d_base_v021_signal(ncfcommon, sharesbas, closeadj):
    ps = _safe_div(ncfcommon, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_ps_63d_base_v022_signal(ncfcommon, sharesbas, closeadj):
    ps = _safe_div(ncfcommon, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_ps_126d_base_v023_signal(ncfcommon, sharesbas, closeadj):
    ps = _safe_div(ncfcommon, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_ps_252d_base_v024_signal(ncfcommon, sharesbas, closeadj):
    ps = _safe_div(ncfcommon, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_ps_504d_base_v025_signal(ncfcommon, sharesbas, closeadj):
    ps = _safe_div(ncfcommon, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ncfcommon scaled by assets
def gm_f33_biotech_f33_capital_raise_proximity_score_asset_scaled_21d_base_v026_signal(ncfcommon, assets):
    scaled = _safe_div(ncfcommon, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ncfcommon scaled by assets
def gm_f33_biotech_f33_capital_raise_proximity_score_asset_scaled_63d_base_v027_signal(ncfcommon, assets):
    scaled = _safe_div(ncfcommon, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ncfcommon scaled by assets
def gm_f33_biotech_f33_capital_raise_proximity_score_asset_scaled_126d_base_v028_signal(ncfcommon, assets):
    scaled = _safe_div(ncfcommon, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ncfcommon scaled by assets
def gm_f33_biotech_f33_capital_raise_proximity_score_asset_scaled_252d_base_v029_signal(ncfcommon, assets):
    scaled = _safe_div(ncfcommon, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ncfcommon scaled by assets
def gm_f33_biotech_f33_capital_raise_proximity_score_asset_scaled_504d_base_v030_signal(ncfcommon, assets):
    scaled = _safe_div(ncfcommon, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ncfcommon scaled by marketcap
def gm_f33_biotech_f33_capital_raise_proximity_score_mcap_scaled_21d_base_v031_signal(ncfcommon, marketcap):
    scaled = _safe_div(ncfcommon, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ncfcommon scaled by marketcap
def gm_f33_biotech_f33_capital_raise_proximity_score_mcap_scaled_63d_base_v032_signal(ncfcommon, marketcap):
    scaled = _safe_div(ncfcommon, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ncfcommon scaled by marketcap
def gm_f33_biotech_f33_capital_raise_proximity_score_mcap_scaled_126d_base_v033_signal(ncfcommon, marketcap):
    scaled = _safe_div(ncfcommon, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ncfcommon scaled by marketcap
def gm_f33_biotech_f33_capital_raise_proximity_score_mcap_scaled_252d_base_v034_signal(ncfcommon, marketcap):
    scaled = _safe_div(ncfcommon, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ncfcommon scaled by marketcap
def gm_f33_biotech_f33_capital_raise_proximity_score_mcap_scaled_504d_base_v035_signal(ncfcommon, marketcap):
    scaled = _safe_div(ncfcommon, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_dist_low_21d_base_v036_signal(ncfcommon):
    low = ncfcommon.rolling(21).min()
    result = _safe_div(ncfcommon - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_dist_low_63d_base_v037_signal(ncfcommon):
    low = ncfcommon.rolling(63).min()
    result = _safe_div(ncfcommon - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_dist_low_126d_base_v038_signal(ncfcommon):
    low = ncfcommon.rolling(126).min()
    result = _safe_div(ncfcommon - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_dist_low_252d_base_v039_signal(ncfcommon):
    low = ncfcommon.rolling(252).min()
    result = _safe_div(ncfcommon - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_dist_low_504d_base_v040_signal(ncfcommon):
    low = ncfcommon.rolling(504).min()
    result = _safe_div(ncfcommon - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_dist_high_21d_base_v041_signal(ncfcommon):
    high = ncfcommon.rolling(21).max()
    result = _safe_div(high - ncfcommon, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_dist_high_63d_base_v042_signal(ncfcommon):
    high = ncfcommon.rolling(63).max()
    result = _safe_div(high - ncfcommon, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_dist_high_126d_base_v043_signal(ncfcommon):
    high = ncfcommon.rolling(126).max()
    result = _safe_div(high - ncfcommon, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_dist_high_252d_base_v044_signal(ncfcommon):
    high = ncfcommon.rolling(252).max()
    result = _safe_div(high - ncfcommon, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_dist_high_504d_base_v045_signal(ncfcommon):
    high = ncfcommon.rolling(504).max()
    result = _safe_div(high - ncfcommon, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_mom_21d_base_v046_signal(ncfcommon):
    m1 = _mean(ncfcommon, 21)
    m2 = _mean(ncfcommon, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_mom_63d_base_v047_signal(ncfcommon):
    m1 = _mean(ncfcommon, 63)
    m2 = _mean(ncfcommon, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_mom_126d_base_v048_signal(ncfcommon):
    m1 = _mean(ncfcommon, 126)
    m2 = _mean(ncfcommon, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_mom_252d_base_v049_signal(ncfcommon):
    m1 = _mean(ncfcommon, 252)
    m2 = _mean(ncfcommon, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_mom_504d_base_v050_signal(ncfcommon):
    m1 = _mean(ncfcommon, 504)
    m2 = _mean(ncfcommon, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_skew_21d_base_v051_signal(ncfcommon):
    result = _skew(ncfcommon, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_skew_63d_base_v052_signal(ncfcommon):
    result = _skew(ncfcommon, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_skew_126d_base_v053_signal(ncfcommon):
    result = _skew(ncfcommon, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_skew_252d_base_v054_signal(ncfcommon):
    result = _skew(ncfcommon, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_skew_504d_base_v055_signal(ncfcommon):
    result = _skew(ncfcommon, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_kurt_21d_base_v056_signal(ncfcommon):
    result = _kurt(ncfcommon, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_kurt_63d_base_v057_signal(ncfcommon):
    result = _kurt(ncfcommon, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_kurt_126d_base_v058_signal(ncfcommon):
    result = _kurt(ncfcommon, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_kurt_252d_base_v059_signal(ncfcommon):
    result = _kurt(ncfcommon, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_kurt_504d_base_v060_signal(ncfcommon):
    result = _kurt(ncfcommon, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_rank_21d_base_v061_signal(ncfcommon, closeadj):
    result = _rank(ncfcommon, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_rank_63d_base_v062_signal(ncfcommon, closeadj):
    result = _rank(ncfcommon, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_rank_126d_base_v063_signal(ncfcommon, closeadj):
    result = _rank(ncfcommon, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_rank_252d_base_v064_signal(ncfcommon, closeadj):
    result = _rank(ncfcommon, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_rank_504d_base_v065_signal(ncfcommon, closeadj):
    result = _rank(ncfcommon, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_autocorr_21d_base_v066_signal(ncfcommon):
    result = _autocorr(ncfcommon, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_autocorr_63d_base_v067_signal(ncfcommon):
    result = _autocorr(ncfcommon, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_autocorr_126d_base_v068_signal(ncfcommon):
    result = _autocorr(ncfcommon, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_autocorr_252d_base_v069_signal(ncfcommon):
    result = _autocorr(ncfcommon, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_autocorr_504d_base_v070_signal(ncfcommon):
    result = _autocorr(ncfcommon, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_std_21d_base_v071_signal(ncfcommon, closeadj):
    result = _std(ncfcommon, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_std_63d_base_v072_signal(ncfcommon, closeadj):
    result = _std(ncfcommon, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_std_126d_base_v073_signal(ncfcommon, closeadj):
    result = _std(ncfcommon, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_std_252d_base_v074_signal(ncfcommon, closeadj):
    result = _std(ncfcommon, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of ncfcommon
def gm_f33_biotech_f33_capital_raise_proximity_score_std_504d_base_v075_signal(ncfcommon, closeadj):
    result = _std(ncfcommon, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

