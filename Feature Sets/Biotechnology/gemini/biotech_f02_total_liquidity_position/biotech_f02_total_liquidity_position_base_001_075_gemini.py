
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed cashneq
def gm_f02_biotech_f02_total_liquidity_position_raw_21d_base_v001_signal(cashneq, closeadj):
    result = _mean(cashneq, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed cashneq
def gm_f02_biotech_f02_total_liquidity_position_raw_63d_base_v002_signal(cashneq, closeadj):
    result = _mean(cashneq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed cashneq
def gm_f02_biotech_f02_total_liquidity_position_raw_126d_base_v003_signal(cashneq, closeadj):
    result = _mean(cashneq, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed cashneq
def gm_f02_biotech_f02_total_liquidity_position_raw_252d_base_v004_signal(cashneq, closeadj):
    result = _mean(cashneq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed cashneq
def gm_f02_biotech_f02_total_liquidity_position_raw_504d_base_v005_signal(cashneq, closeadj):
    result = _mean(cashneq, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed cashneq
def gm_f02_biotech_f02_total_liquidity_position_log_21d_base_v006_signal(cashneq, closeadj):
    result = _mean(_log(cashneq), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed cashneq
def gm_f02_biotech_f02_total_liquidity_position_log_63d_base_v007_signal(cashneq, closeadj):
    result = _mean(_log(cashneq), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed cashneq
def gm_f02_biotech_f02_total_liquidity_position_log_126d_base_v008_signal(cashneq, closeadj):
    result = _mean(_log(cashneq), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed cashneq
def gm_f02_biotech_f02_total_liquidity_position_log_252d_base_v009_signal(cashneq, closeadj):
    result = _mean(_log(cashneq), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed cashneq
def gm_f02_biotech_f02_total_liquidity_position_log_504d_base_v010_signal(cashneq, closeadj):
    result = _mean(_log(cashneq), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of cashneq
def gm_f02_biotech_f02_total_liquidity_position_z_21d_base_v011_signal(cashneq):
    result = _z(cashneq, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of cashneq
def gm_f02_biotech_f02_total_liquidity_position_z_63d_base_v012_signal(cashneq):
    result = _z(cashneq, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of cashneq
def gm_f02_biotech_f02_total_liquidity_position_z_126d_base_v013_signal(cashneq):
    result = _z(cashneq, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of cashneq
def gm_f02_biotech_f02_total_liquidity_position_z_252d_base_v014_signal(cashneq):
    result = _z(cashneq, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of cashneq
def gm_f02_biotech_f02_total_liquidity_position_z_504d_base_v015_signal(cashneq):
    result = _z(cashneq, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of cashneq
def gm_f02_biotech_f02_total_liquidity_position_pct_21d_base_v016_signal(cashneq):
    result = _pct_change(cashneq, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of cashneq
def gm_f02_biotech_f02_total_liquidity_position_pct_63d_base_v017_signal(cashneq):
    result = _pct_change(cashneq, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of cashneq
def gm_f02_biotech_f02_total_liquidity_position_pct_126d_base_v018_signal(cashneq):
    result = _pct_change(cashneq, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of cashneq
def gm_f02_biotech_f02_total_liquidity_position_pct_252d_base_v019_signal(cashneq):
    result = _pct_change(cashneq, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of cashneq
def gm_f02_biotech_f02_total_liquidity_position_pct_504d_base_v020_signal(cashneq):
    result = _pct_change(cashneq, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share cashneq
def gm_f02_biotech_f02_total_liquidity_position_ps_21d_base_v021_signal(cashneq, sharesbas, closeadj):
    ps = _safe_div(cashneq, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share cashneq
def gm_f02_biotech_f02_total_liquidity_position_ps_63d_base_v022_signal(cashneq, sharesbas, closeadj):
    ps = _safe_div(cashneq, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share cashneq
def gm_f02_biotech_f02_total_liquidity_position_ps_126d_base_v023_signal(cashneq, sharesbas, closeadj):
    ps = _safe_div(cashneq, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share cashneq
def gm_f02_biotech_f02_total_liquidity_position_ps_252d_base_v024_signal(cashneq, sharesbas, closeadj):
    ps = _safe_div(cashneq, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share cashneq
def gm_f02_biotech_f02_total_liquidity_position_ps_504d_base_v025_signal(cashneq, sharesbas, closeadj):
    ps = _safe_div(cashneq, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of cashneq to investments
def gm_f02_biotech_f02_total_liquidity_position_ratio_investments_21d_base_v026_signal(cashneq, investments):
    ratio = _safe_div(cashneq, investments)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of cashneq to investments
def gm_f02_biotech_f02_total_liquidity_position_ratio_investments_63d_base_v027_signal(cashneq, investments):
    ratio = _safe_div(cashneq, investments)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of cashneq to investments
def gm_f02_biotech_f02_total_liquidity_position_ratio_investments_126d_base_v028_signal(cashneq, investments):
    ratio = _safe_div(cashneq, investments)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of cashneq to investments
def gm_f02_biotech_f02_total_liquidity_position_ratio_investments_252d_base_v029_signal(cashneq, investments):
    ratio = _safe_div(cashneq, investments)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of cashneq to investments
def gm_f02_biotech_f02_total_liquidity_position_ratio_investments_504d_base_v030_signal(cashneq, investments):
    ratio = _safe_div(cashneq, investments)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cashneq scaled by assets
def gm_f02_biotech_f02_total_liquidity_position_asset_scaled_21d_base_v031_signal(cashneq, assets):
    scaled = _safe_div(cashneq, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cashneq scaled by assets
def gm_f02_biotech_f02_total_liquidity_position_asset_scaled_63d_base_v032_signal(cashneq, assets):
    scaled = _safe_div(cashneq, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d cashneq scaled by assets
def gm_f02_biotech_f02_total_liquidity_position_asset_scaled_126d_base_v033_signal(cashneq, assets):
    scaled = _safe_div(cashneq, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cashneq scaled by assets
def gm_f02_biotech_f02_total_liquidity_position_asset_scaled_252d_base_v034_signal(cashneq, assets):
    scaled = _safe_div(cashneq, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d cashneq scaled by assets
def gm_f02_biotech_f02_total_liquidity_position_asset_scaled_504d_base_v035_signal(cashneq, assets):
    scaled = _safe_div(cashneq, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cashneq scaled by marketcap
def gm_f02_biotech_f02_total_liquidity_position_mcap_scaled_21d_base_v036_signal(cashneq, marketcap):
    scaled = _safe_div(cashneq, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cashneq scaled by marketcap
def gm_f02_biotech_f02_total_liquidity_position_mcap_scaled_63d_base_v037_signal(cashneq, marketcap):
    scaled = _safe_div(cashneq, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d cashneq scaled by marketcap
def gm_f02_biotech_f02_total_liquidity_position_mcap_scaled_126d_base_v038_signal(cashneq, marketcap):
    scaled = _safe_div(cashneq, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cashneq scaled by marketcap
def gm_f02_biotech_f02_total_liquidity_position_mcap_scaled_252d_base_v039_signal(cashneq, marketcap):
    scaled = _safe_div(cashneq, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d cashneq scaled by marketcap
def gm_f02_biotech_f02_total_liquidity_position_mcap_scaled_504d_base_v040_signal(cashneq, marketcap):
    scaled = _safe_div(cashneq, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low cashneq
def gm_f02_biotech_f02_total_liquidity_position_dist_low_21d_base_v041_signal(cashneq):
    low = cashneq.rolling(21).min()
    result = _safe_div(cashneq - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low cashneq
def gm_f02_biotech_f02_total_liquidity_position_dist_low_63d_base_v042_signal(cashneq):
    low = cashneq.rolling(63).min()
    result = _safe_div(cashneq - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low cashneq
def gm_f02_biotech_f02_total_liquidity_position_dist_low_126d_base_v043_signal(cashneq):
    low = cashneq.rolling(126).min()
    result = _safe_div(cashneq - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low cashneq
def gm_f02_biotech_f02_total_liquidity_position_dist_low_252d_base_v044_signal(cashneq):
    low = cashneq.rolling(252).min()
    result = _safe_div(cashneq - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low cashneq
def gm_f02_biotech_f02_total_liquidity_position_dist_low_504d_base_v045_signal(cashneq):
    low = cashneq.rolling(504).min()
    result = _safe_div(cashneq - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high cashneq
def gm_f02_biotech_f02_total_liquidity_position_dist_high_21d_base_v046_signal(cashneq):
    high = cashneq.rolling(21).max()
    result = _safe_div(high - cashneq, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high cashneq
def gm_f02_biotech_f02_total_liquidity_position_dist_high_63d_base_v047_signal(cashneq):
    high = cashneq.rolling(63).max()
    result = _safe_div(high - cashneq, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high cashneq
def gm_f02_biotech_f02_total_liquidity_position_dist_high_126d_base_v048_signal(cashneq):
    high = cashneq.rolling(126).max()
    result = _safe_div(high - cashneq, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high cashneq
def gm_f02_biotech_f02_total_liquidity_position_dist_high_252d_base_v049_signal(cashneq):
    high = cashneq.rolling(252).max()
    result = _safe_div(high - cashneq, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high cashneq
def gm_f02_biotech_f02_total_liquidity_position_dist_high_504d_base_v050_signal(cashneq):
    high = cashneq.rolling(504).max()
    result = _safe_div(high - cashneq, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of cashneq
def gm_f02_biotech_f02_total_liquidity_position_mom_21d_base_v051_signal(cashneq):
    m1 = _mean(cashneq, 21)
    m2 = _mean(cashneq, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of cashneq
def gm_f02_biotech_f02_total_liquidity_position_mom_63d_base_v052_signal(cashneq):
    m1 = _mean(cashneq, 63)
    m2 = _mean(cashneq, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of cashneq
def gm_f02_biotech_f02_total_liquidity_position_mom_126d_base_v053_signal(cashneq):
    m1 = _mean(cashneq, 126)
    m2 = _mean(cashneq, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of cashneq
def gm_f02_biotech_f02_total_liquidity_position_mom_252d_base_v054_signal(cashneq):
    m1 = _mean(cashneq, 252)
    m2 = _mean(cashneq, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of cashneq
def gm_f02_biotech_f02_total_liquidity_position_mom_504d_base_v055_signal(cashneq):
    m1 = _mean(cashneq, 504)
    m2 = _mean(cashneq, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of cashneq
def gm_f02_biotech_f02_total_liquidity_position_skew_21d_base_v056_signal(cashneq):
    result = _skew(cashneq, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of cashneq
def gm_f02_biotech_f02_total_liquidity_position_skew_63d_base_v057_signal(cashneq):
    result = _skew(cashneq, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of cashneq
def gm_f02_biotech_f02_total_liquidity_position_skew_126d_base_v058_signal(cashneq):
    result = _skew(cashneq, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of cashneq
def gm_f02_biotech_f02_total_liquidity_position_skew_252d_base_v059_signal(cashneq):
    result = _skew(cashneq, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of cashneq
def gm_f02_biotech_f02_total_liquidity_position_skew_504d_base_v060_signal(cashneq):
    result = _skew(cashneq, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of cashneq
def gm_f02_biotech_f02_total_liquidity_position_kurt_21d_base_v061_signal(cashneq):
    result = _kurt(cashneq, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of cashneq
def gm_f02_biotech_f02_total_liquidity_position_kurt_63d_base_v062_signal(cashneq):
    result = _kurt(cashneq, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of cashneq
def gm_f02_biotech_f02_total_liquidity_position_kurt_126d_base_v063_signal(cashneq):
    result = _kurt(cashneq, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of cashneq
def gm_f02_biotech_f02_total_liquidity_position_kurt_252d_base_v064_signal(cashneq):
    result = _kurt(cashneq, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of cashneq
def gm_f02_biotech_f02_total_liquidity_position_kurt_504d_base_v065_signal(cashneq):
    result = _kurt(cashneq, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of cashneq
def gm_f02_biotech_f02_total_liquidity_position_rank_21d_base_v066_signal(cashneq, closeadj):
    result = _rank(cashneq, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of cashneq
def gm_f02_biotech_f02_total_liquidity_position_rank_63d_base_v067_signal(cashneq, closeadj):
    result = _rank(cashneq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of cashneq
def gm_f02_biotech_f02_total_liquidity_position_rank_126d_base_v068_signal(cashneq, closeadj):
    result = _rank(cashneq, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of cashneq
def gm_f02_biotech_f02_total_liquidity_position_rank_252d_base_v069_signal(cashneq, closeadj):
    result = _rank(cashneq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of cashneq
def gm_f02_biotech_f02_total_liquidity_position_rank_504d_base_v070_signal(cashneq, closeadj):
    result = _rank(cashneq, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of cashneq
def gm_f02_biotech_f02_total_liquidity_position_autocorr_21d_base_v071_signal(cashneq):
    result = _autocorr(cashneq, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of cashneq
def gm_f02_biotech_f02_total_liquidity_position_autocorr_63d_base_v072_signal(cashneq):
    result = _autocorr(cashneq, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of cashneq
def gm_f02_biotech_f02_total_liquidity_position_autocorr_126d_base_v073_signal(cashneq):
    result = _autocorr(cashneq, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of cashneq
def gm_f02_biotech_f02_total_liquidity_position_autocorr_252d_base_v074_signal(cashneq):
    result = _autocorr(cashneq, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of cashneq
def gm_f02_biotech_f02_total_liquidity_position_autocorr_504d_base_v075_signal(cashneq):
    result = _autocorr(cashneq, 504)
    return result.replace([np.inf, -np.inf], np.nan)

