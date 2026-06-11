
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed units
def gm_f71_biotech_f71_institutional_ownership_pct_raw_21d_base_v001_signal(units, closeadj):
    result = _mean(units, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed units
def gm_f71_biotech_f71_institutional_ownership_pct_raw_63d_base_v002_signal(units, closeadj):
    result = _mean(units, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed units
def gm_f71_biotech_f71_institutional_ownership_pct_raw_126d_base_v003_signal(units, closeadj):
    result = _mean(units, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed units
def gm_f71_biotech_f71_institutional_ownership_pct_raw_252d_base_v004_signal(units, closeadj):
    result = _mean(units, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed units
def gm_f71_biotech_f71_institutional_ownership_pct_raw_504d_base_v005_signal(units, closeadj):
    result = _mean(units, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed units
def gm_f71_biotech_f71_institutional_ownership_pct_log_21d_base_v006_signal(units, closeadj):
    result = _mean(_log(units), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed units
def gm_f71_biotech_f71_institutional_ownership_pct_log_63d_base_v007_signal(units, closeadj):
    result = _mean(_log(units), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed units
def gm_f71_biotech_f71_institutional_ownership_pct_log_126d_base_v008_signal(units, closeadj):
    result = _mean(_log(units), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed units
def gm_f71_biotech_f71_institutional_ownership_pct_log_252d_base_v009_signal(units, closeadj):
    result = _mean(_log(units), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed units
def gm_f71_biotech_f71_institutional_ownership_pct_log_504d_base_v010_signal(units, closeadj):
    result = _mean(_log(units), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of units
def gm_f71_biotech_f71_institutional_ownership_pct_z_21d_base_v011_signal(units):
    result = _z(units, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of units
def gm_f71_biotech_f71_institutional_ownership_pct_z_63d_base_v012_signal(units):
    result = _z(units, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of units
def gm_f71_biotech_f71_institutional_ownership_pct_z_126d_base_v013_signal(units):
    result = _z(units, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of units
def gm_f71_biotech_f71_institutional_ownership_pct_z_252d_base_v014_signal(units):
    result = _z(units, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of units
def gm_f71_biotech_f71_institutional_ownership_pct_z_504d_base_v015_signal(units):
    result = _z(units, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of units
def gm_f71_biotech_f71_institutional_ownership_pct_pct_21d_base_v016_signal(units):
    result = _pct_change(units, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of units
def gm_f71_biotech_f71_institutional_ownership_pct_pct_63d_base_v017_signal(units):
    result = _pct_change(units, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of units
def gm_f71_biotech_f71_institutional_ownership_pct_pct_126d_base_v018_signal(units):
    result = _pct_change(units, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of units
def gm_f71_biotech_f71_institutional_ownership_pct_pct_252d_base_v019_signal(units):
    result = _pct_change(units, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of units
def gm_f71_biotech_f71_institutional_ownership_pct_pct_504d_base_v020_signal(units):
    result = _pct_change(units, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share units
def gm_f71_biotech_f71_institutional_ownership_pct_ps_21d_base_v021_signal(units, sharesbas, closeadj):
    ps = _safe_div(units, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share units
def gm_f71_biotech_f71_institutional_ownership_pct_ps_63d_base_v022_signal(units, sharesbas, closeadj):
    ps = _safe_div(units, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share units
def gm_f71_biotech_f71_institutional_ownership_pct_ps_126d_base_v023_signal(units, sharesbas, closeadj):
    ps = _safe_div(units, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share units
def gm_f71_biotech_f71_institutional_ownership_pct_ps_252d_base_v024_signal(units, sharesbas, closeadj):
    ps = _safe_div(units, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share units
def gm_f71_biotech_f71_institutional_ownership_pct_ps_504d_base_v025_signal(units, sharesbas, closeadj):
    ps = _safe_div(units, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of units to sharesbas
def gm_f71_biotech_f71_institutional_ownership_pct_ratio_sharesbas_21d_base_v026_signal(units, sharesbas):
    ratio = _safe_div(units, sharesbas)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of units to sharesbas
def gm_f71_biotech_f71_institutional_ownership_pct_ratio_sharesbas_63d_base_v027_signal(units, sharesbas):
    ratio = _safe_div(units, sharesbas)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of units to sharesbas
def gm_f71_biotech_f71_institutional_ownership_pct_ratio_sharesbas_126d_base_v028_signal(units, sharesbas):
    ratio = _safe_div(units, sharesbas)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of units to sharesbas
def gm_f71_biotech_f71_institutional_ownership_pct_ratio_sharesbas_252d_base_v029_signal(units, sharesbas):
    ratio = _safe_div(units, sharesbas)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of units to sharesbas
def gm_f71_biotech_f71_institutional_ownership_pct_ratio_sharesbas_504d_base_v030_signal(units, sharesbas):
    ratio = _safe_div(units, sharesbas)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d units scaled by assets
def gm_f71_biotech_f71_institutional_ownership_pct_asset_scaled_21d_base_v031_signal(units, assets):
    scaled = _safe_div(units, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d units scaled by assets
def gm_f71_biotech_f71_institutional_ownership_pct_asset_scaled_63d_base_v032_signal(units, assets):
    scaled = _safe_div(units, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d units scaled by assets
def gm_f71_biotech_f71_institutional_ownership_pct_asset_scaled_126d_base_v033_signal(units, assets):
    scaled = _safe_div(units, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d units scaled by assets
def gm_f71_biotech_f71_institutional_ownership_pct_asset_scaled_252d_base_v034_signal(units, assets):
    scaled = _safe_div(units, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d units scaled by assets
def gm_f71_biotech_f71_institutional_ownership_pct_asset_scaled_504d_base_v035_signal(units, assets):
    scaled = _safe_div(units, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d units scaled by marketcap
def gm_f71_biotech_f71_institutional_ownership_pct_mcap_scaled_21d_base_v036_signal(units, marketcap):
    scaled = _safe_div(units, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d units scaled by marketcap
def gm_f71_biotech_f71_institutional_ownership_pct_mcap_scaled_63d_base_v037_signal(units, marketcap):
    scaled = _safe_div(units, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d units scaled by marketcap
def gm_f71_biotech_f71_institutional_ownership_pct_mcap_scaled_126d_base_v038_signal(units, marketcap):
    scaled = _safe_div(units, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d units scaled by marketcap
def gm_f71_biotech_f71_institutional_ownership_pct_mcap_scaled_252d_base_v039_signal(units, marketcap):
    scaled = _safe_div(units, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d units scaled by marketcap
def gm_f71_biotech_f71_institutional_ownership_pct_mcap_scaled_504d_base_v040_signal(units, marketcap):
    scaled = _safe_div(units, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low units
def gm_f71_biotech_f71_institutional_ownership_pct_dist_low_21d_base_v041_signal(units):
    low = units.rolling(21).min()
    result = _safe_div(units - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low units
def gm_f71_biotech_f71_institutional_ownership_pct_dist_low_63d_base_v042_signal(units):
    low = units.rolling(63).min()
    result = _safe_div(units - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low units
def gm_f71_biotech_f71_institutional_ownership_pct_dist_low_126d_base_v043_signal(units):
    low = units.rolling(126).min()
    result = _safe_div(units - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low units
def gm_f71_biotech_f71_institutional_ownership_pct_dist_low_252d_base_v044_signal(units):
    low = units.rolling(252).min()
    result = _safe_div(units - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low units
def gm_f71_biotech_f71_institutional_ownership_pct_dist_low_504d_base_v045_signal(units):
    low = units.rolling(504).min()
    result = _safe_div(units - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high units
def gm_f71_biotech_f71_institutional_ownership_pct_dist_high_21d_base_v046_signal(units):
    high = units.rolling(21).max()
    result = _safe_div(high - units, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high units
def gm_f71_biotech_f71_institutional_ownership_pct_dist_high_63d_base_v047_signal(units):
    high = units.rolling(63).max()
    result = _safe_div(high - units, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high units
def gm_f71_biotech_f71_institutional_ownership_pct_dist_high_126d_base_v048_signal(units):
    high = units.rolling(126).max()
    result = _safe_div(high - units, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high units
def gm_f71_biotech_f71_institutional_ownership_pct_dist_high_252d_base_v049_signal(units):
    high = units.rolling(252).max()
    result = _safe_div(high - units, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high units
def gm_f71_biotech_f71_institutional_ownership_pct_dist_high_504d_base_v050_signal(units):
    high = units.rolling(504).max()
    result = _safe_div(high - units, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of units
def gm_f71_biotech_f71_institutional_ownership_pct_mom_21d_base_v051_signal(units):
    m1 = _mean(units, 21)
    m2 = _mean(units, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of units
def gm_f71_biotech_f71_institutional_ownership_pct_mom_63d_base_v052_signal(units):
    m1 = _mean(units, 63)
    m2 = _mean(units, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of units
def gm_f71_biotech_f71_institutional_ownership_pct_mom_126d_base_v053_signal(units):
    m1 = _mean(units, 126)
    m2 = _mean(units, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of units
def gm_f71_biotech_f71_institutional_ownership_pct_mom_252d_base_v054_signal(units):
    m1 = _mean(units, 252)
    m2 = _mean(units, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of units
def gm_f71_biotech_f71_institutional_ownership_pct_mom_504d_base_v055_signal(units):
    m1 = _mean(units, 504)
    m2 = _mean(units, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of units
def gm_f71_biotech_f71_institutional_ownership_pct_skew_21d_base_v056_signal(units):
    result = _skew(units, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of units
def gm_f71_biotech_f71_institutional_ownership_pct_skew_63d_base_v057_signal(units):
    result = _skew(units, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of units
def gm_f71_biotech_f71_institutional_ownership_pct_skew_126d_base_v058_signal(units):
    result = _skew(units, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of units
def gm_f71_biotech_f71_institutional_ownership_pct_skew_252d_base_v059_signal(units):
    result = _skew(units, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of units
def gm_f71_biotech_f71_institutional_ownership_pct_skew_504d_base_v060_signal(units):
    result = _skew(units, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of units
def gm_f71_biotech_f71_institutional_ownership_pct_kurt_21d_base_v061_signal(units):
    result = _kurt(units, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of units
def gm_f71_biotech_f71_institutional_ownership_pct_kurt_63d_base_v062_signal(units):
    result = _kurt(units, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of units
def gm_f71_biotech_f71_institutional_ownership_pct_kurt_126d_base_v063_signal(units):
    result = _kurt(units, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of units
def gm_f71_biotech_f71_institutional_ownership_pct_kurt_252d_base_v064_signal(units):
    result = _kurt(units, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of units
def gm_f71_biotech_f71_institutional_ownership_pct_kurt_504d_base_v065_signal(units):
    result = _kurt(units, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of units
def gm_f71_biotech_f71_institutional_ownership_pct_rank_21d_base_v066_signal(units, closeadj):
    result = _rank(units, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of units
def gm_f71_biotech_f71_institutional_ownership_pct_rank_63d_base_v067_signal(units, closeadj):
    result = _rank(units, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of units
def gm_f71_biotech_f71_institutional_ownership_pct_rank_126d_base_v068_signal(units, closeadj):
    result = _rank(units, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of units
def gm_f71_biotech_f71_institutional_ownership_pct_rank_252d_base_v069_signal(units, closeadj):
    result = _rank(units, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of units
def gm_f71_biotech_f71_institutional_ownership_pct_rank_504d_base_v070_signal(units, closeadj):
    result = _rank(units, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of units
def gm_f71_biotech_f71_institutional_ownership_pct_autocorr_21d_base_v071_signal(units):
    result = _autocorr(units, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of units
def gm_f71_biotech_f71_institutional_ownership_pct_autocorr_63d_base_v072_signal(units):
    result = _autocorr(units, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of units
def gm_f71_biotech_f71_institutional_ownership_pct_autocorr_126d_base_v073_signal(units):
    result = _autocorr(units, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of units
def gm_f71_biotech_f71_institutional_ownership_pct_autocorr_252d_base_v074_signal(units):
    result = _autocorr(units, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of units
def gm_f71_biotech_f71_institutional_ownership_pct_autocorr_504d_base_v075_signal(units):
    result = _autocorr(units, 504)
    return result.replace([np.inf, -np.inf], np.nan)

