
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed equityratio
def gm_f10_f10_equityratio_ratio_raw_21d_base_v001_signal(equityratio, closeadj):
    result = _mean(equityratio, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed equityratio
def gm_f10_f10_equityratio_ratio_raw_63d_base_v002_signal(equityratio, closeadj):
    result = _mean(equityratio, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed equityratio
def gm_f10_f10_equityratio_ratio_raw_126d_base_v003_signal(equityratio, closeadj):
    result = _mean(equityratio, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed equityratio
def gm_f10_f10_equityratio_ratio_raw_252d_base_v004_signal(equityratio, closeadj):
    result = _mean(equityratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed equityratio
def gm_f10_f10_equityratio_ratio_raw_504d_base_v005_signal(equityratio, closeadj):
    result = _mean(equityratio, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed equityratio
def gm_f10_f10_equityratio_ratio_log_21d_base_v006_signal(equityratio, closeadj):
    result = _mean(_log(equityratio), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed equityratio
def gm_f10_f10_equityratio_ratio_log_63d_base_v007_signal(equityratio, closeadj):
    result = _mean(_log(equityratio), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed equityratio
def gm_f10_f10_equityratio_ratio_log_126d_base_v008_signal(equityratio, closeadj):
    result = _mean(_log(equityratio), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed equityratio
def gm_f10_f10_equityratio_ratio_log_252d_base_v009_signal(equityratio, closeadj):
    result = _mean(_log(equityratio), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed equityratio
def gm_f10_f10_equityratio_ratio_log_504d_base_v010_signal(equityratio, closeadj):
    result = _mean(_log(equityratio), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of equityratio
def gm_f10_f10_equityratio_ratio_z_21d_base_v011_signal(equityratio):
    result = _z(equityratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of equityratio
def gm_f10_f10_equityratio_ratio_z_63d_base_v012_signal(equityratio):
    result = _z(equityratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of equityratio
def gm_f10_f10_equityratio_ratio_z_126d_base_v013_signal(equityratio):
    result = _z(equityratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of equityratio
def gm_f10_f10_equityratio_ratio_z_252d_base_v014_signal(equityratio):
    result = _z(equityratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of equityratio
def gm_f10_f10_equityratio_ratio_z_504d_base_v015_signal(equityratio):
    result = _z(equityratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of equityratio
def gm_f10_f10_equityratio_ratio_pct_21d_base_v016_signal(equityratio):
    result = _pct_change(equityratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of equityratio
def gm_f10_f10_equityratio_ratio_pct_63d_base_v017_signal(equityratio):
    result = _pct_change(equityratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of equityratio
def gm_f10_f10_equityratio_ratio_pct_126d_base_v018_signal(equityratio):
    result = _pct_change(equityratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of equityratio
def gm_f10_f10_equityratio_ratio_pct_252d_base_v019_signal(equityratio):
    result = _pct_change(equityratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of equityratio
def gm_f10_f10_equityratio_ratio_pct_504d_base_v020_signal(equityratio):
    result = _pct_change(equityratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share equityratio
def gm_f10_f10_equityratio_ratio_ps_21d_base_v021_signal(equityratio, sharesbas, closeadj):
    ps = _safe_div(equityratio, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share equityratio
def gm_f10_f10_equityratio_ratio_ps_63d_base_v022_signal(equityratio, sharesbas, closeadj):
    ps = _safe_div(equityratio, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share equityratio
def gm_f10_f10_equityratio_ratio_ps_126d_base_v023_signal(equityratio, sharesbas, closeadj):
    ps = _safe_div(equityratio, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share equityratio
def gm_f10_f10_equityratio_ratio_ps_252d_base_v024_signal(equityratio, sharesbas, closeadj):
    ps = _safe_div(equityratio, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share equityratio
def gm_f10_f10_equityratio_ratio_ps_504d_base_v025_signal(equityratio, sharesbas, closeadj):
    ps = _safe_div(equityratio, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of equityratio to assets
def gm_f10_f10_equityratio_ratio_ratio_assets_21d_base_v026_signal(equityratio, assets):
    ratio = _safe_div(equityratio, assets)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of equityratio to assets
def gm_f10_f10_equityratio_ratio_ratio_assets_63d_base_v027_signal(equityratio, assets):
    ratio = _safe_div(equityratio, assets)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of equityratio to assets
def gm_f10_f10_equityratio_ratio_ratio_assets_126d_base_v028_signal(equityratio, assets):
    ratio = _safe_div(equityratio, assets)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of equityratio to assets
def gm_f10_f10_equityratio_ratio_ratio_assets_252d_base_v029_signal(equityratio, assets):
    ratio = _safe_div(equityratio, assets)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of equityratio to assets
def gm_f10_f10_equityratio_ratio_ratio_assets_504d_base_v030_signal(equityratio, assets):
    ratio = _safe_div(equityratio, assets)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d equityratio scaled by assets
def gm_f10_f10_equityratio_ratio_asset_scaled_21d_base_v031_signal(equityratio, assets):
    scaled = _safe_div(equityratio, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d equityratio scaled by assets
def gm_f10_f10_equityratio_ratio_asset_scaled_63d_base_v032_signal(equityratio, assets):
    scaled = _safe_div(equityratio, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d equityratio scaled by assets
def gm_f10_f10_equityratio_ratio_asset_scaled_126d_base_v033_signal(equityratio, assets):
    scaled = _safe_div(equityratio, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d equityratio scaled by assets
def gm_f10_f10_equityratio_ratio_asset_scaled_252d_base_v034_signal(equityratio, assets):
    scaled = _safe_div(equityratio, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d equityratio scaled by assets
def gm_f10_f10_equityratio_ratio_asset_scaled_504d_base_v035_signal(equityratio, assets):
    scaled = _safe_div(equityratio, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d equityratio scaled by marketcap
def gm_f10_f10_equityratio_ratio_mcap_scaled_21d_base_v036_signal(equityratio, marketcap):
    scaled = _safe_div(equityratio, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d equityratio scaled by marketcap
def gm_f10_f10_equityratio_ratio_mcap_scaled_63d_base_v037_signal(equityratio, marketcap):
    scaled = _safe_div(equityratio, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d equityratio scaled by marketcap
def gm_f10_f10_equityratio_ratio_mcap_scaled_126d_base_v038_signal(equityratio, marketcap):
    scaled = _safe_div(equityratio, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d equityratio scaled by marketcap
def gm_f10_f10_equityratio_ratio_mcap_scaled_252d_base_v039_signal(equityratio, marketcap):
    scaled = _safe_div(equityratio, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d equityratio scaled by marketcap
def gm_f10_f10_equityratio_ratio_mcap_scaled_504d_base_v040_signal(equityratio, marketcap):
    scaled = _safe_div(equityratio, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low equityratio
def gm_f10_f10_equityratio_ratio_dist_low_21d_base_v041_signal(equityratio):
    low = equityratio.rolling(21).min()
    result = _safe_div(equityratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low equityratio
def gm_f10_f10_equityratio_ratio_dist_low_63d_base_v042_signal(equityratio):
    low = equityratio.rolling(63).min()
    result = _safe_div(equityratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low equityratio
def gm_f10_f10_equityratio_ratio_dist_low_126d_base_v043_signal(equityratio):
    low = equityratio.rolling(126).min()
    result = _safe_div(equityratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low equityratio
def gm_f10_f10_equityratio_ratio_dist_low_252d_base_v044_signal(equityratio):
    low = equityratio.rolling(252).min()
    result = _safe_div(equityratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low equityratio
def gm_f10_f10_equityratio_ratio_dist_low_504d_base_v045_signal(equityratio):
    low = equityratio.rolling(504).min()
    result = _safe_div(equityratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high equityratio
def gm_f10_f10_equityratio_ratio_dist_high_21d_base_v046_signal(equityratio):
    high = equityratio.rolling(21).max()
    result = _safe_div(high - equityratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high equityratio
def gm_f10_f10_equityratio_ratio_dist_high_63d_base_v047_signal(equityratio):
    high = equityratio.rolling(63).max()
    result = _safe_div(high - equityratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high equityratio
def gm_f10_f10_equityratio_ratio_dist_high_126d_base_v048_signal(equityratio):
    high = equityratio.rolling(126).max()
    result = _safe_div(high - equityratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high equityratio
def gm_f10_f10_equityratio_ratio_dist_high_252d_base_v049_signal(equityratio):
    high = equityratio.rolling(252).max()
    result = _safe_div(high - equityratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high equityratio
def gm_f10_f10_equityratio_ratio_dist_high_504d_base_v050_signal(equityratio):
    high = equityratio.rolling(504).max()
    result = _safe_div(high - equityratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of equityratio
def gm_f10_f10_equityratio_ratio_mom_21d_base_v051_signal(equityratio):
    m1 = _mean(equityratio, 21)
    m2 = _mean(equityratio, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of equityratio
def gm_f10_f10_equityratio_ratio_mom_63d_base_v052_signal(equityratio):
    m1 = _mean(equityratio, 63)
    m2 = _mean(equityratio, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of equityratio
def gm_f10_f10_equityratio_ratio_mom_126d_base_v053_signal(equityratio):
    m1 = _mean(equityratio, 126)
    m2 = _mean(equityratio, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of equityratio
def gm_f10_f10_equityratio_ratio_mom_252d_base_v054_signal(equityratio):
    m1 = _mean(equityratio, 252)
    m2 = _mean(equityratio, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of equityratio
def gm_f10_f10_equityratio_ratio_mom_504d_base_v055_signal(equityratio):
    m1 = _mean(equityratio, 504)
    m2 = _mean(equityratio, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of equityratio
def gm_f10_f10_equityratio_ratio_skew_21d_base_v056_signal(equityratio):
    result = _skew(equityratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of equityratio
def gm_f10_f10_equityratio_ratio_skew_63d_base_v057_signal(equityratio):
    result = _skew(equityratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of equityratio
def gm_f10_f10_equityratio_ratio_skew_126d_base_v058_signal(equityratio):
    result = _skew(equityratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of equityratio
def gm_f10_f10_equityratio_ratio_skew_252d_base_v059_signal(equityratio):
    result = _skew(equityratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of equityratio
def gm_f10_f10_equityratio_ratio_skew_504d_base_v060_signal(equityratio):
    result = _skew(equityratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of equityratio
def gm_f10_f10_equityratio_ratio_kurt_21d_base_v061_signal(equityratio):
    result = _kurt(equityratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of equityratio
def gm_f10_f10_equityratio_ratio_kurt_63d_base_v062_signal(equityratio):
    result = _kurt(equityratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of equityratio
def gm_f10_f10_equityratio_ratio_kurt_126d_base_v063_signal(equityratio):
    result = _kurt(equityratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of equityratio
def gm_f10_f10_equityratio_ratio_kurt_252d_base_v064_signal(equityratio):
    result = _kurt(equityratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of equityratio
def gm_f10_f10_equityratio_ratio_kurt_504d_base_v065_signal(equityratio):
    result = _kurt(equityratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of equityratio
def gm_f10_f10_equityratio_ratio_rank_21d_base_v066_signal(equityratio, closeadj):
    result = _rank(equityratio, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of equityratio
def gm_f10_f10_equityratio_ratio_rank_63d_base_v067_signal(equityratio, closeadj):
    result = _rank(equityratio, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of equityratio
def gm_f10_f10_equityratio_ratio_rank_126d_base_v068_signal(equityratio, closeadj):
    result = _rank(equityratio, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of equityratio
def gm_f10_f10_equityratio_ratio_rank_252d_base_v069_signal(equityratio, closeadj):
    result = _rank(equityratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of equityratio
def gm_f10_f10_equityratio_ratio_rank_504d_base_v070_signal(equityratio, closeadj):
    result = _rank(equityratio, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of equityratio
def gm_f10_f10_equityratio_ratio_autocorr_21d_base_v071_signal(equityratio):
    result = _autocorr(equityratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of equityratio
def gm_f10_f10_equityratio_ratio_autocorr_63d_base_v072_signal(equityratio):
    result = _autocorr(equityratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of equityratio
def gm_f10_f10_equityratio_ratio_autocorr_126d_base_v073_signal(equityratio):
    result = _autocorr(equityratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of equityratio
def gm_f10_f10_equityratio_ratio_autocorr_252d_base_v074_signal(equityratio):
    result = _autocorr(equityratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of equityratio
def gm_f10_f10_equityratio_ratio_autocorr_504d_base_v075_signal(equityratio):
    result = _autocorr(equityratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

