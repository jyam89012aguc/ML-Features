
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_raw_21d_base_v001_signal(rnd, closeadj):
    result = _mean(rnd, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_raw_63d_base_v002_signal(rnd, closeadj):
    result = _mean(rnd, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_raw_126d_base_v003_signal(rnd, closeadj):
    result = _mean(rnd, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_raw_252d_base_v004_signal(rnd, closeadj):
    result = _mean(rnd, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_raw_504d_base_v005_signal(rnd, closeadj):
    result = _mean(rnd, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_log_21d_base_v006_signal(rnd, closeadj):
    result = _mean(_log(rnd), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_log_63d_base_v007_signal(rnd, closeadj):
    result = _mean(_log(rnd), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_log_126d_base_v008_signal(rnd, closeadj):
    result = _mean(_log(rnd), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_log_252d_base_v009_signal(rnd, closeadj):
    result = _mean(_log(rnd), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_log_504d_base_v010_signal(rnd, closeadj):
    result = _mean(_log(rnd), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_z_21d_base_v011_signal(rnd):
    result = _z(rnd, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_z_63d_base_v012_signal(rnd):
    result = _z(rnd, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_z_126d_base_v013_signal(rnd):
    result = _z(rnd, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_z_252d_base_v014_signal(rnd):
    result = _z(rnd, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_z_504d_base_v015_signal(rnd):
    result = _z(rnd, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_pct_21d_base_v016_signal(rnd):
    result = _pct_change(rnd, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_pct_63d_base_v017_signal(rnd):
    result = _pct_change(rnd, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_pct_126d_base_v018_signal(rnd):
    result = _pct_change(rnd, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_pct_252d_base_v019_signal(rnd):
    result = _pct_change(rnd, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_pct_504d_base_v020_signal(rnd):
    result = _pct_change(rnd, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_ps_21d_base_v021_signal(rnd, sharesbas, closeadj):
    ps = _safe_div(rnd, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_ps_63d_base_v022_signal(rnd, sharesbas, closeadj):
    ps = _safe_div(rnd, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_ps_126d_base_v023_signal(rnd, sharesbas, closeadj):
    ps = _safe_div(rnd, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_ps_252d_base_v024_signal(rnd, sharesbas, closeadj):
    ps = _safe_div(rnd, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_ps_504d_base_v025_signal(rnd, sharesbas, closeadj):
    ps = _safe_div(rnd, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of rnd to ncfo
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_ratio_ncfo_21d_base_v026_signal(rnd, ncfo):
    ratio = _safe_div(rnd, ncfo)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of rnd to ncfo
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_ratio_ncfo_63d_base_v027_signal(rnd, ncfo):
    ratio = _safe_div(rnd, ncfo)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of rnd to ncfo
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_ratio_ncfo_126d_base_v028_signal(rnd, ncfo):
    ratio = _safe_div(rnd, ncfo)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of rnd to ncfo
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_ratio_ncfo_252d_base_v029_signal(rnd, ncfo):
    ratio = _safe_div(rnd, ncfo)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of rnd to ncfo
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_ratio_ncfo_504d_base_v030_signal(rnd, ncfo):
    ratio = _safe_div(rnd, ncfo)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rnd scaled by assets
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_asset_scaled_21d_base_v031_signal(rnd, assets):
    scaled = _safe_div(rnd, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rnd scaled by assets
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_asset_scaled_63d_base_v032_signal(rnd, assets):
    scaled = _safe_div(rnd, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rnd scaled by assets
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_asset_scaled_126d_base_v033_signal(rnd, assets):
    scaled = _safe_div(rnd, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rnd scaled by assets
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_asset_scaled_252d_base_v034_signal(rnd, assets):
    scaled = _safe_div(rnd, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rnd scaled by assets
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_asset_scaled_504d_base_v035_signal(rnd, assets):
    scaled = _safe_div(rnd, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rnd scaled by marketcap
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_mcap_scaled_21d_base_v036_signal(rnd, marketcap):
    scaled = _safe_div(rnd, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rnd scaled by marketcap
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_mcap_scaled_63d_base_v037_signal(rnd, marketcap):
    scaled = _safe_div(rnd, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rnd scaled by marketcap
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_mcap_scaled_126d_base_v038_signal(rnd, marketcap):
    scaled = _safe_div(rnd, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rnd scaled by marketcap
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_mcap_scaled_252d_base_v039_signal(rnd, marketcap):
    scaled = _safe_div(rnd, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rnd scaled by marketcap
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_mcap_scaled_504d_base_v040_signal(rnd, marketcap):
    scaled = _safe_div(rnd, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_dist_low_21d_base_v041_signal(rnd):
    low = rnd.rolling(21).min()
    result = _safe_div(rnd - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_dist_low_63d_base_v042_signal(rnd):
    low = rnd.rolling(63).min()
    result = _safe_div(rnd - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_dist_low_126d_base_v043_signal(rnd):
    low = rnd.rolling(126).min()
    result = _safe_div(rnd - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_dist_low_252d_base_v044_signal(rnd):
    low = rnd.rolling(252).min()
    result = _safe_div(rnd - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_dist_low_504d_base_v045_signal(rnd):
    low = rnd.rolling(504).min()
    result = _safe_div(rnd - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_dist_high_21d_base_v046_signal(rnd):
    high = rnd.rolling(21).max()
    result = _safe_div(high - rnd, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_dist_high_63d_base_v047_signal(rnd):
    high = rnd.rolling(63).max()
    result = _safe_div(high - rnd, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_dist_high_126d_base_v048_signal(rnd):
    high = rnd.rolling(126).max()
    result = _safe_div(high - rnd, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_dist_high_252d_base_v049_signal(rnd):
    high = rnd.rolling(252).max()
    result = _safe_div(high - rnd, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_dist_high_504d_base_v050_signal(rnd):
    high = rnd.rolling(504).max()
    result = _safe_div(high - rnd, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_mom_21d_base_v051_signal(rnd):
    m1 = _mean(rnd, 21)
    m2 = _mean(rnd, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_mom_63d_base_v052_signal(rnd):
    m1 = _mean(rnd, 63)
    m2 = _mean(rnd, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_mom_126d_base_v053_signal(rnd):
    m1 = _mean(rnd, 126)
    m2 = _mean(rnd, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_mom_252d_base_v054_signal(rnd):
    m1 = _mean(rnd, 252)
    m2 = _mean(rnd, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_mom_504d_base_v055_signal(rnd):
    m1 = _mean(rnd, 504)
    m2 = _mean(rnd, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_skew_21d_base_v056_signal(rnd):
    result = _skew(rnd, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_skew_63d_base_v057_signal(rnd):
    result = _skew(rnd, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_skew_126d_base_v058_signal(rnd):
    result = _skew(rnd, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_skew_252d_base_v059_signal(rnd):
    result = _skew(rnd, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_skew_504d_base_v060_signal(rnd):
    result = _skew(rnd, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_kurt_21d_base_v061_signal(rnd):
    result = _kurt(rnd, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_kurt_63d_base_v062_signal(rnd):
    result = _kurt(rnd, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_kurt_126d_base_v063_signal(rnd):
    result = _kurt(rnd, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_kurt_252d_base_v064_signal(rnd):
    result = _kurt(rnd, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_kurt_504d_base_v065_signal(rnd):
    result = _kurt(rnd, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_rank_21d_base_v066_signal(rnd, closeadj):
    result = _rank(rnd, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_rank_63d_base_v067_signal(rnd, closeadj):
    result = _rank(rnd, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_rank_126d_base_v068_signal(rnd, closeadj):
    result = _rank(rnd, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_rank_252d_base_v069_signal(rnd, closeadj):
    result = _rank(rnd, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_rank_504d_base_v070_signal(rnd, closeadj):
    result = _rank(rnd, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_autocorr_21d_base_v071_signal(rnd):
    result = _autocorr(rnd, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_autocorr_63d_base_v072_signal(rnd):
    result = _autocorr(rnd, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_autocorr_126d_base_v073_signal(rnd):
    result = _autocorr(rnd, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_autocorr_252d_base_v074_signal(rnd):
    result = _autocorr(rnd, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of rnd
def gm_f26_biotech_f26_rnd_to_total_burn_ratio_autocorr_504d_base_v075_signal(rnd):
    result = _autocorr(rnd, 504)
    return result.replace([np.inf, -np.inf], np.nan)

