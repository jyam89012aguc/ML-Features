
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed roa
def gm_f52_biotech_f52_return_on_assets_efficiency_raw_21d_base_v001_signal(roa, closeadj):
    result = _mean(roa, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed roa
def gm_f52_biotech_f52_return_on_assets_efficiency_raw_63d_base_v002_signal(roa, closeadj):
    result = _mean(roa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed roa
def gm_f52_biotech_f52_return_on_assets_efficiency_raw_126d_base_v003_signal(roa, closeadj):
    result = _mean(roa, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed roa
def gm_f52_biotech_f52_return_on_assets_efficiency_raw_252d_base_v004_signal(roa, closeadj):
    result = _mean(roa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed roa
def gm_f52_biotech_f52_return_on_assets_efficiency_raw_504d_base_v005_signal(roa, closeadj):
    result = _mean(roa, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed roa
def gm_f52_biotech_f52_return_on_assets_efficiency_log_21d_base_v006_signal(roa, closeadj):
    result = _mean(_log(roa), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed roa
def gm_f52_biotech_f52_return_on_assets_efficiency_log_63d_base_v007_signal(roa, closeadj):
    result = _mean(_log(roa), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed roa
def gm_f52_biotech_f52_return_on_assets_efficiency_log_126d_base_v008_signal(roa, closeadj):
    result = _mean(_log(roa), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed roa
def gm_f52_biotech_f52_return_on_assets_efficiency_log_252d_base_v009_signal(roa, closeadj):
    result = _mean(_log(roa), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed roa
def gm_f52_biotech_f52_return_on_assets_efficiency_log_504d_base_v010_signal(roa, closeadj):
    result = _mean(_log(roa), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_z_21d_base_v011_signal(roa):
    result = _z(roa, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_z_63d_base_v012_signal(roa):
    result = _z(roa, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_z_126d_base_v013_signal(roa):
    result = _z(roa, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_z_252d_base_v014_signal(roa):
    result = _z(roa, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_z_504d_base_v015_signal(roa):
    result = _z(roa, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_pct_21d_base_v016_signal(roa):
    result = _pct_change(roa, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_pct_63d_base_v017_signal(roa):
    result = _pct_change(roa, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_pct_126d_base_v018_signal(roa):
    result = _pct_change(roa, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_pct_252d_base_v019_signal(roa):
    result = _pct_change(roa, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_pct_504d_base_v020_signal(roa):
    result = _pct_change(roa, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share roa
def gm_f52_biotech_f52_return_on_assets_efficiency_ps_21d_base_v021_signal(roa, sharesbas, closeadj):
    ps = _safe_div(roa, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share roa
def gm_f52_biotech_f52_return_on_assets_efficiency_ps_63d_base_v022_signal(roa, sharesbas, closeadj):
    ps = _safe_div(roa, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share roa
def gm_f52_biotech_f52_return_on_assets_efficiency_ps_126d_base_v023_signal(roa, sharesbas, closeadj):
    ps = _safe_div(roa, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share roa
def gm_f52_biotech_f52_return_on_assets_efficiency_ps_252d_base_v024_signal(roa, sharesbas, closeadj):
    ps = _safe_div(roa, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share roa
def gm_f52_biotech_f52_return_on_assets_efficiency_ps_504d_base_v025_signal(roa, sharesbas, closeadj):
    ps = _safe_div(roa, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of roa to assets
def gm_f52_biotech_f52_return_on_assets_efficiency_ratio_assets_21d_base_v026_signal(roa, assets):
    ratio = _safe_div(roa, assets)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of roa to assets
def gm_f52_biotech_f52_return_on_assets_efficiency_ratio_assets_63d_base_v027_signal(roa, assets):
    ratio = _safe_div(roa, assets)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of roa to assets
def gm_f52_biotech_f52_return_on_assets_efficiency_ratio_assets_126d_base_v028_signal(roa, assets):
    ratio = _safe_div(roa, assets)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of roa to assets
def gm_f52_biotech_f52_return_on_assets_efficiency_ratio_assets_252d_base_v029_signal(roa, assets):
    ratio = _safe_div(roa, assets)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of roa to assets
def gm_f52_biotech_f52_return_on_assets_efficiency_ratio_assets_504d_base_v030_signal(roa, assets):
    ratio = _safe_div(roa, assets)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d roa scaled by assets
def gm_f52_biotech_f52_return_on_assets_efficiency_asset_scaled_21d_base_v031_signal(roa, assets):
    scaled = _safe_div(roa, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d roa scaled by assets
def gm_f52_biotech_f52_return_on_assets_efficiency_asset_scaled_63d_base_v032_signal(roa, assets):
    scaled = _safe_div(roa, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d roa scaled by assets
def gm_f52_biotech_f52_return_on_assets_efficiency_asset_scaled_126d_base_v033_signal(roa, assets):
    scaled = _safe_div(roa, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d roa scaled by assets
def gm_f52_biotech_f52_return_on_assets_efficiency_asset_scaled_252d_base_v034_signal(roa, assets):
    scaled = _safe_div(roa, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d roa scaled by assets
def gm_f52_biotech_f52_return_on_assets_efficiency_asset_scaled_504d_base_v035_signal(roa, assets):
    scaled = _safe_div(roa, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d roa scaled by marketcap
def gm_f52_biotech_f52_return_on_assets_efficiency_mcap_scaled_21d_base_v036_signal(roa, marketcap):
    scaled = _safe_div(roa, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d roa scaled by marketcap
def gm_f52_biotech_f52_return_on_assets_efficiency_mcap_scaled_63d_base_v037_signal(roa, marketcap):
    scaled = _safe_div(roa, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d roa scaled by marketcap
def gm_f52_biotech_f52_return_on_assets_efficiency_mcap_scaled_126d_base_v038_signal(roa, marketcap):
    scaled = _safe_div(roa, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d roa scaled by marketcap
def gm_f52_biotech_f52_return_on_assets_efficiency_mcap_scaled_252d_base_v039_signal(roa, marketcap):
    scaled = _safe_div(roa, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d roa scaled by marketcap
def gm_f52_biotech_f52_return_on_assets_efficiency_mcap_scaled_504d_base_v040_signal(roa, marketcap):
    scaled = _safe_div(roa, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low roa
def gm_f52_biotech_f52_return_on_assets_efficiency_dist_low_21d_base_v041_signal(roa):
    low = roa.rolling(21).min()
    result = _safe_div(roa - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low roa
def gm_f52_biotech_f52_return_on_assets_efficiency_dist_low_63d_base_v042_signal(roa):
    low = roa.rolling(63).min()
    result = _safe_div(roa - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low roa
def gm_f52_biotech_f52_return_on_assets_efficiency_dist_low_126d_base_v043_signal(roa):
    low = roa.rolling(126).min()
    result = _safe_div(roa - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low roa
def gm_f52_biotech_f52_return_on_assets_efficiency_dist_low_252d_base_v044_signal(roa):
    low = roa.rolling(252).min()
    result = _safe_div(roa - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low roa
def gm_f52_biotech_f52_return_on_assets_efficiency_dist_low_504d_base_v045_signal(roa):
    low = roa.rolling(504).min()
    result = _safe_div(roa - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high roa
def gm_f52_biotech_f52_return_on_assets_efficiency_dist_high_21d_base_v046_signal(roa):
    high = roa.rolling(21).max()
    result = _safe_div(high - roa, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high roa
def gm_f52_biotech_f52_return_on_assets_efficiency_dist_high_63d_base_v047_signal(roa):
    high = roa.rolling(63).max()
    result = _safe_div(high - roa, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high roa
def gm_f52_biotech_f52_return_on_assets_efficiency_dist_high_126d_base_v048_signal(roa):
    high = roa.rolling(126).max()
    result = _safe_div(high - roa, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high roa
def gm_f52_biotech_f52_return_on_assets_efficiency_dist_high_252d_base_v049_signal(roa):
    high = roa.rolling(252).max()
    result = _safe_div(high - roa, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high roa
def gm_f52_biotech_f52_return_on_assets_efficiency_dist_high_504d_base_v050_signal(roa):
    high = roa.rolling(504).max()
    result = _safe_div(high - roa, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_mom_21d_base_v051_signal(roa):
    m1 = _mean(roa, 21)
    m2 = _mean(roa, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_mom_63d_base_v052_signal(roa):
    m1 = _mean(roa, 63)
    m2 = _mean(roa, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_mom_126d_base_v053_signal(roa):
    m1 = _mean(roa, 126)
    m2 = _mean(roa, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_mom_252d_base_v054_signal(roa):
    m1 = _mean(roa, 252)
    m2 = _mean(roa, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_mom_504d_base_v055_signal(roa):
    m1 = _mean(roa, 504)
    m2 = _mean(roa, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_skew_21d_base_v056_signal(roa):
    result = _skew(roa, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_skew_63d_base_v057_signal(roa):
    result = _skew(roa, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_skew_126d_base_v058_signal(roa):
    result = _skew(roa, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_skew_252d_base_v059_signal(roa):
    result = _skew(roa, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_skew_504d_base_v060_signal(roa):
    result = _skew(roa, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_kurt_21d_base_v061_signal(roa):
    result = _kurt(roa, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_kurt_63d_base_v062_signal(roa):
    result = _kurt(roa, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_kurt_126d_base_v063_signal(roa):
    result = _kurt(roa, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_kurt_252d_base_v064_signal(roa):
    result = _kurt(roa, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_kurt_504d_base_v065_signal(roa):
    result = _kurt(roa, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_rank_21d_base_v066_signal(roa, closeadj):
    result = _rank(roa, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_rank_63d_base_v067_signal(roa, closeadj):
    result = _rank(roa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_rank_126d_base_v068_signal(roa, closeadj):
    result = _rank(roa, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_rank_252d_base_v069_signal(roa, closeadj):
    result = _rank(roa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_rank_504d_base_v070_signal(roa, closeadj):
    result = _rank(roa, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_autocorr_21d_base_v071_signal(roa):
    result = _autocorr(roa, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_autocorr_63d_base_v072_signal(roa):
    result = _autocorr(roa, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_autocorr_126d_base_v073_signal(roa):
    result = _autocorr(roa, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_autocorr_252d_base_v074_signal(roa):
    result = _autocorr(roa, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of roa
def gm_f52_biotech_f52_return_on_assets_efficiency_autocorr_504d_base_v075_signal(roa):
    result = _autocorr(roa, 504)
    return result.replace([np.inf, -np.inf], np.nan)

