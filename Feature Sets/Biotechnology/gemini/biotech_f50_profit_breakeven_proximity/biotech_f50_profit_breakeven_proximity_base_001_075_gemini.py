
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_raw_21d_base_v001_signal(breakeven, closeadj):
    result = _mean(breakeven, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_raw_63d_base_v002_signal(breakeven, closeadj):
    result = _mean(breakeven, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_raw_126d_base_v003_signal(breakeven, closeadj):
    result = _mean(breakeven, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_raw_252d_base_v004_signal(breakeven, closeadj):
    result = _mean(breakeven, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_raw_504d_base_v005_signal(breakeven, closeadj):
    result = _mean(breakeven, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_log_21d_base_v006_signal(breakeven, closeadj):
    result = _mean(_log(breakeven), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_log_63d_base_v007_signal(breakeven, closeadj):
    result = _mean(_log(breakeven), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_log_126d_base_v008_signal(breakeven, closeadj):
    result = _mean(_log(breakeven), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_log_252d_base_v009_signal(breakeven, closeadj):
    result = _mean(_log(breakeven), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_log_504d_base_v010_signal(breakeven, closeadj):
    result = _mean(_log(breakeven), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_z_21d_base_v011_signal(breakeven):
    result = _z(breakeven, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_z_63d_base_v012_signal(breakeven):
    result = _z(breakeven, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_z_126d_base_v013_signal(breakeven):
    result = _z(breakeven, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_z_252d_base_v014_signal(breakeven):
    result = _z(breakeven, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_z_504d_base_v015_signal(breakeven):
    result = _z(breakeven, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_pct_21d_base_v016_signal(breakeven):
    result = _pct_change(breakeven, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_pct_63d_base_v017_signal(breakeven):
    result = _pct_change(breakeven, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_pct_126d_base_v018_signal(breakeven):
    result = _pct_change(breakeven, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_pct_252d_base_v019_signal(breakeven):
    result = _pct_change(breakeven, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_pct_504d_base_v020_signal(breakeven):
    result = _pct_change(breakeven, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_ps_21d_base_v021_signal(breakeven, sharesbas, closeadj):
    ps = _safe_div(breakeven, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_ps_63d_base_v022_signal(breakeven, sharesbas, closeadj):
    ps = _safe_div(breakeven, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_ps_126d_base_v023_signal(breakeven, sharesbas, closeadj):
    ps = _safe_div(breakeven, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_ps_252d_base_v024_signal(breakeven, sharesbas, closeadj):
    ps = _safe_div(breakeven, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_ps_504d_base_v025_signal(breakeven, sharesbas, closeadj):
    ps = _safe_div(breakeven, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of breakeven to opex
def gm_f50_biotech_f50_profit_breakeven_proximity_ratio_opex_21d_base_v026_signal(breakeven, opex):
    ratio = _safe_div(breakeven, opex)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of breakeven to opex
def gm_f50_biotech_f50_profit_breakeven_proximity_ratio_opex_63d_base_v027_signal(breakeven, opex):
    ratio = _safe_div(breakeven, opex)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of breakeven to opex
def gm_f50_biotech_f50_profit_breakeven_proximity_ratio_opex_126d_base_v028_signal(breakeven, opex):
    ratio = _safe_div(breakeven, opex)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of breakeven to opex
def gm_f50_biotech_f50_profit_breakeven_proximity_ratio_opex_252d_base_v029_signal(breakeven, opex):
    ratio = _safe_div(breakeven, opex)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of breakeven to opex
def gm_f50_biotech_f50_profit_breakeven_proximity_ratio_opex_504d_base_v030_signal(breakeven, opex):
    ratio = _safe_div(breakeven, opex)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d breakeven scaled by assets
def gm_f50_biotech_f50_profit_breakeven_proximity_asset_scaled_21d_base_v031_signal(breakeven, assets):
    scaled = _safe_div(breakeven, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d breakeven scaled by assets
def gm_f50_biotech_f50_profit_breakeven_proximity_asset_scaled_63d_base_v032_signal(breakeven, assets):
    scaled = _safe_div(breakeven, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d breakeven scaled by assets
def gm_f50_biotech_f50_profit_breakeven_proximity_asset_scaled_126d_base_v033_signal(breakeven, assets):
    scaled = _safe_div(breakeven, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d breakeven scaled by assets
def gm_f50_biotech_f50_profit_breakeven_proximity_asset_scaled_252d_base_v034_signal(breakeven, assets):
    scaled = _safe_div(breakeven, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d breakeven scaled by assets
def gm_f50_biotech_f50_profit_breakeven_proximity_asset_scaled_504d_base_v035_signal(breakeven, assets):
    scaled = _safe_div(breakeven, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d breakeven scaled by marketcap
def gm_f50_biotech_f50_profit_breakeven_proximity_mcap_scaled_21d_base_v036_signal(breakeven, marketcap):
    scaled = _safe_div(breakeven, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d breakeven scaled by marketcap
def gm_f50_biotech_f50_profit_breakeven_proximity_mcap_scaled_63d_base_v037_signal(breakeven, marketcap):
    scaled = _safe_div(breakeven, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d breakeven scaled by marketcap
def gm_f50_biotech_f50_profit_breakeven_proximity_mcap_scaled_126d_base_v038_signal(breakeven, marketcap):
    scaled = _safe_div(breakeven, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d breakeven scaled by marketcap
def gm_f50_biotech_f50_profit_breakeven_proximity_mcap_scaled_252d_base_v039_signal(breakeven, marketcap):
    scaled = _safe_div(breakeven, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d breakeven scaled by marketcap
def gm_f50_biotech_f50_profit_breakeven_proximity_mcap_scaled_504d_base_v040_signal(breakeven, marketcap):
    scaled = _safe_div(breakeven, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_dist_low_21d_base_v041_signal(breakeven):
    low = breakeven.rolling(21).min()
    result = _safe_div(breakeven - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_dist_low_63d_base_v042_signal(breakeven):
    low = breakeven.rolling(63).min()
    result = _safe_div(breakeven - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_dist_low_126d_base_v043_signal(breakeven):
    low = breakeven.rolling(126).min()
    result = _safe_div(breakeven - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_dist_low_252d_base_v044_signal(breakeven):
    low = breakeven.rolling(252).min()
    result = _safe_div(breakeven - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_dist_low_504d_base_v045_signal(breakeven):
    low = breakeven.rolling(504).min()
    result = _safe_div(breakeven - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_dist_high_21d_base_v046_signal(breakeven):
    high = breakeven.rolling(21).max()
    result = _safe_div(high - breakeven, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_dist_high_63d_base_v047_signal(breakeven):
    high = breakeven.rolling(63).max()
    result = _safe_div(high - breakeven, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_dist_high_126d_base_v048_signal(breakeven):
    high = breakeven.rolling(126).max()
    result = _safe_div(high - breakeven, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_dist_high_252d_base_v049_signal(breakeven):
    high = breakeven.rolling(252).max()
    result = _safe_div(high - breakeven, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_dist_high_504d_base_v050_signal(breakeven):
    high = breakeven.rolling(504).max()
    result = _safe_div(high - breakeven, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_mom_21d_base_v051_signal(breakeven):
    m1 = _mean(breakeven, 21)
    m2 = _mean(breakeven, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_mom_63d_base_v052_signal(breakeven):
    m1 = _mean(breakeven, 63)
    m2 = _mean(breakeven, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_mom_126d_base_v053_signal(breakeven):
    m1 = _mean(breakeven, 126)
    m2 = _mean(breakeven, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_mom_252d_base_v054_signal(breakeven):
    m1 = _mean(breakeven, 252)
    m2 = _mean(breakeven, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_mom_504d_base_v055_signal(breakeven):
    m1 = _mean(breakeven, 504)
    m2 = _mean(breakeven, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_skew_21d_base_v056_signal(breakeven):
    result = _skew(breakeven, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_skew_63d_base_v057_signal(breakeven):
    result = _skew(breakeven, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_skew_126d_base_v058_signal(breakeven):
    result = _skew(breakeven, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_skew_252d_base_v059_signal(breakeven):
    result = _skew(breakeven, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_skew_504d_base_v060_signal(breakeven):
    result = _skew(breakeven, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_kurt_21d_base_v061_signal(breakeven):
    result = _kurt(breakeven, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_kurt_63d_base_v062_signal(breakeven):
    result = _kurt(breakeven, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_kurt_126d_base_v063_signal(breakeven):
    result = _kurt(breakeven, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_kurt_252d_base_v064_signal(breakeven):
    result = _kurt(breakeven, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_kurt_504d_base_v065_signal(breakeven):
    result = _kurt(breakeven, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_rank_21d_base_v066_signal(breakeven, closeadj):
    result = _rank(breakeven, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_rank_63d_base_v067_signal(breakeven, closeadj):
    result = _rank(breakeven, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_rank_126d_base_v068_signal(breakeven, closeadj):
    result = _rank(breakeven, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_rank_252d_base_v069_signal(breakeven, closeadj):
    result = _rank(breakeven, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_rank_504d_base_v070_signal(breakeven, closeadj):
    result = _rank(breakeven, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_autocorr_21d_base_v071_signal(breakeven):
    result = _autocorr(breakeven, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_autocorr_63d_base_v072_signal(breakeven):
    result = _autocorr(breakeven, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_autocorr_126d_base_v073_signal(breakeven):
    result = _autocorr(breakeven, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_autocorr_252d_base_v074_signal(breakeven):
    result = _autocorr(breakeven, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of breakeven
def gm_f50_biotech_f50_profit_breakeven_proximity_autocorr_504d_base_v075_signal(breakeven):
    result = _autocorr(breakeven, 504)
    return result.replace([np.inf, -np.inf], np.nan)

