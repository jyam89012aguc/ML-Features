
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_raw_21d_base_v001_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_raw_63d_base_v002_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_raw_126d_base_v003_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_raw_252d_base_v004_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_raw_504d_base_v005_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_log_21d_base_v006_signal(assetturnover, closeadj):
    result = _mean(_log(assetturnover), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_log_63d_base_v007_signal(assetturnover, closeadj):
    result = _mean(_log(assetturnover), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_log_126d_base_v008_signal(assetturnover, closeadj):
    result = _mean(_log(assetturnover), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_log_252d_base_v009_signal(assetturnover, closeadj):
    result = _mean(_log(assetturnover), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_log_504d_base_v010_signal(assetturnover, closeadj):
    result = _mean(_log(assetturnover), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_z_21d_base_v011_signal(assetturnover):
    result = _z(assetturnover, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_z_63d_base_v012_signal(assetturnover):
    result = _z(assetturnover, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_z_126d_base_v013_signal(assetturnover):
    result = _z(assetturnover, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_z_252d_base_v014_signal(assetturnover):
    result = _z(assetturnover, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_z_504d_base_v015_signal(assetturnover):
    result = _z(assetturnover, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_pct_21d_base_v016_signal(assetturnover):
    result = _pct_change(assetturnover, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_pct_63d_base_v017_signal(assetturnover):
    result = _pct_change(assetturnover, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_pct_126d_base_v018_signal(assetturnover):
    result = _pct_change(assetturnover, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_pct_252d_base_v019_signal(assetturnover):
    result = _pct_change(assetturnover, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_pct_504d_base_v020_signal(assetturnover):
    result = _pct_change(assetturnover, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_ps_21d_base_v021_signal(assetturnover, sharesbas, closeadj):
    ps = _safe_div(assetturnover, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_ps_63d_base_v022_signal(assetturnover, sharesbas, closeadj):
    ps = _safe_div(assetturnover, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_ps_126d_base_v023_signal(assetturnover, sharesbas, closeadj):
    ps = _safe_div(assetturnover, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_ps_252d_base_v024_signal(assetturnover, sharesbas, closeadj):
    ps = _safe_div(assetturnover, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_ps_504d_base_v025_signal(assetturnover, sharesbas, closeadj):
    ps = _safe_div(assetturnover, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of assetturnover to assets
def gm_f51_biotech_f51_total_asset_turnover_efficiency_ratio_assets_21d_base_v026_signal(assetturnover, assets):
    ratio = _safe_div(assetturnover, assets)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of assetturnover to assets
def gm_f51_biotech_f51_total_asset_turnover_efficiency_ratio_assets_63d_base_v027_signal(assetturnover, assets):
    ratio = _safe_div(assetturnover, assets)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of assetturnover to assets
def gm_f51_biotech_f51_total_asset_turnover_efficiency_ratio_assets_126d_base_v028_signal(assetturnover, assets):
    ratio = _safe_div(assetturnover, assets)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of assetturnover to assets
def gm_f51_biotech_f51_total_asset_turnover_efficiency_ratio_assets_252d_base_v029_signal(assetturnover, assets):
    ratio = _safe_div(assetturnover, assets)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of assetturnover to assets
def gm_f51_biotech_f51_total_asset_turnover_efficiency_ratio_assets_504d_base_v030_signal(assetturnover, assets):
    ratio = _safe_div(assetturnover, assets)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d assetturnover scaled by assets
def gm_f51_biotech_f51_total_asset_turnover_efficiency_asset_scaled_21d_base_v031_signal(assetturnover, assets):
    scaled = _safe_div(assetturnover, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d assetturnover scaled by assets
def gm_f51_biotech_f51_total_asset_turnover_efficiency_asset_scaled_63d_base_v032_signal(assetturnover, assets):
    scaled = _safe_div(assetturnover, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d assetturnover scaled by assets
def gm_f51_biotech_f51_total_asset_turnover_efficiency_asset_scaled_126d_base_v033_signal(assetturnover, assets):
    scaled = _safe_div(assetturnover, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d assetturnover scaled by assets
def gm_f51_biotech_f51_total_asset_turnover_efficiency_asset_scaled_252d_base_v034_signal(assetturnover, assets):
    scaled = _safe_div(assetturnover, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d assetturnover scaled by assets
def gm_f51_biotech_f51_total_asset_turnover_efficiency_asset_scaled_504d_base_v035_signal(assetturnover, assets):
    scaled = _safe_div(assetturnover, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d assetturnover scaled by marketcap
def gm_f51_biotech_f51_total_asset_turnover_efficiency_mcap_scaled_21d_base_v036_signal(assetturnover, marketcap):
    scaled = _safe_div(assetturnover, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d assetturnover scaled by marketcap
def gm_f51_biotech_f51_total_asset_turnover_efficiency_mcap_scaled_63d_base_v037_signal(assetturnover, marketcap):
    scaled = _safe_div(assetturnover, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d assetturnover scaled by marketcap
def gm_f51_biotech_f51_total_asset_turnover_efficiency_mcap_scaled_126d_base_v038_signal(assetturnover, marketcap):
    scaled = _safe_div(assetturnover, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d assetturnover scaled by marketcap
def gm_f51_biotech_f51_total_asset_turnover_efficiency_mcap_scaled_252d_base_v039_signal(assetturnover, marketcap):
    scaled = _safe_div(assetturnover, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d assetturnover scaled by marketcap
def gm_f51_biotech_f51_total_asset_turnover_efficiency_mcap_scaled_504d_base_v040_signal(assetturnover, marketcap):
    scaled = _safe_div(assetturnover, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_dist_low_21d_base_v041_signal(assetturnover):
    low = assetturnover.rolling(21).min()
    result = _safe_div(assetturnover - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_dist_low_63d_base_v042_signal(assetturnover):
    low = assetturnover.rolling(63).min()
    result = _safe_div(assetturnover - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_dist_low_126d_base_v043_signal(assetturnover):
    low = assetturnover.rolling(126).min()
    result = _safe_div(assetturnover - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_dist_low_252d_base_v044_signal(assetturnover):
    low = assetturnover.rolling(252).min()
    result = _safe_div(assetturnover - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_dist_low_504d_base_v045_signal(assetturnover):
    low = assetturnover.rolling(504).min()
    result = _safe_div(assetturnover - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_dist_high_21d_base_v046_signal(assetturnover):
    high = assetturnover.rolling(21).max()
    result = _safe_div(high - assetturnover, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_dist_high_63d_base_v047_signal(assetturnover):
    high = assetturnover.rolling(63).max()
    result = _safe_div(high - assetturnover, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_dist_high_126d_base_v048_signal(assetturnover):
    high = assetturnover.rolling(126).max()
    result = _safe_div(high - assetturnover, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_dist_high_252d_base_v049_signal(assetturnover):
    high = assetturnover.rolling(252).max()
    result = _safe_div(high - assetturnover, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_dist_high_504d_base_v050_signal(assetturnover):
    high = assetturnover.rolling(504).max()
    result = _safe_div(high - assetturnover, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_mom_21d_base_v051_signal(assetturnover):
    m1 = _mean(assetturnover, 21)
    m2 = _mean(assetturnover, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_mom_63d_base_v052_signal(assetturnover):
    m1 = _mean(assetturnover, 63)
    m2 = _mean(assetturnover, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_mom_126d_base_v053_signal(assetturnover):
    m1 = _mean(assetturnover, 126)
    m2 = _mean(assetturnover, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_mom_252d_base_v054_signal(assetturnover):
    m1 = _mean(assetturnover, 252)
    m2 = _mean(assetturnover, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_mom_504d_base_v055_signal(assetturnover):
    m1 = _mean(assetturnover, 504)
    m2 = _mean(assetturnover, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_skew_21d_base_v056_signal(assetturnover):
    result = _skew(assetturnover, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_skew_63d_base_v057_signal(assetturnover):
    result = _skew(assetturnover, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_skew_126d_base_v058_signal(assetturnover):
    result = _skew(assetturnover, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_skew_252d_base_v059_signal(assetturnover):
    result = _skew(assetturnover, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_skew_504d_base_v060_signal(assetturnover):
    result = _skew(assetturnover, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_kurt_21d_base_v061_signal(assetturnover):
    result = _kurt(assetturnover, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_kurt_63d_base_v062_signal(assetturnover):
    result = _kurt(assetturnover, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_kurt_126d_base_v063_signal(assetturnover):
    result = _kurt(assetturnover, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_kurt_252d_base_v064_signal(assetturnover):
    result = _kurt(assetturnover, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_kurt_504d_base_v065_signal(assetturnover):
    result = _kurt(assetturnover, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_rank_21d_base_v066_signal(assetturnover, closeadj):
    result = _rank(assetturnover, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_rank_63d_base_v067_signal(assetturnover, closeadj):
    result = _rank(assetturnover, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_rank_126d_base_v068_signal(assetturnover, closeadj):
    result = _rank(assetturnover, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_rank_252d_base_v069_signal(assetturnover, closeadj):
    result = _rank(assetturnover, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_rank_504d_base_v070_signal(assetturnover, closeadj):
    result = _rank(assetturnover, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_autocorr_21d_base_v071_signal(assetturnover):
    result = _autocorr(assetturnover, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_autocorr_63d_base_v072_signal(assetturnover):
    result = _autocorr(assetturnover, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_autocorr_126d_base_v073_signal(assetturnover):
    result = _autocorr(assetturnover, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_autocorr_252d_base_v074_signal(assetturnover):
    result = _autocorr(assetturnover, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of assetturnover
def gm_f51_biotech_f51_total_asset_turnover_efficiency_autocorr_504d_base_v075_signal(assetturnover):
    result = _autocorr(assetturnover, 504)
    return result.replace([np.inf, -np.inf], np.nan)

