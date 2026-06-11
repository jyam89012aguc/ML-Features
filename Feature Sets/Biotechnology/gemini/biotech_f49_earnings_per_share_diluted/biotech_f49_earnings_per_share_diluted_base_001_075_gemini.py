
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_21d_base_v001_signal(epsdil, closeadj):
    result = _mean(epsdil, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_63d_base_v002_signal(epsdil, closeadj):
    result = _mean(epsdil, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_126d_base_v003_signal(epsdil, closeadj):
    result = _mean(epsdil, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_252d_base_v004_signal(epsdil, closeadj):
    result = _mean(epsdil, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_504d_base_v005_signal(epsdil, closeadj):
    result = _mean(epsdil, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_21d_base_v006_signal(epsdil, closeadj):
    result = _mean(_log(epsdil), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_63d_base_v007_signal(epsdil, closeadj):
    result = _mean(_log(epsdil), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_126d_base_v008_signal(epsdil, closeadj):
    result = _mean(_log(epsdil), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_252d_base_v009_signal(epsdil, closeadj):
    result = _mean(_log(epsdil), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_504d_base_v010_signal(epsdil, closeadj):
    result = _mean(_log(epsdil), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_21d_base_v011_signal(epsdil):
    result = _z(epsdil, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_63d_base_v012_signal(epsdil):
    result = _z(epsdil, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_126d_base_v013_signal(epsdil):
    result = _z(epsdil, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_252d_base_v014_signal(epsdil):
    result = _z(epsdil, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_504d_base_v015_signal(epsdil):
    result = _z(epsdil, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_pct_21d_base_v016_signal(epsdil):
    result = _pct_change(epsdil, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_pct_63d_base_v017_signal(epsdil):
    result = _pct_change(epsdil, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_pct_126d_base_v018_signal(epsdil):
    result = _pct_change(epsdil, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_pct_252d_base_v019_signal(epsdil):
    result = _pct_change(epsdil, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_pct_504d_base_v020_signal(epsdil):
    result = _pct_change(epsdil, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_21d_base_v021_signal(epsdil, sharesbas, closeadj):
    ps = _safe_div(epsdil, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_63d_base_v022_signal(epsdil, sharesbas, closeadj):
    ps = _safe_div(epsdil, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_126d_base_v023_signal(epsdil, sharesbas, closeadj):
    ps = _safe_div(epsdil, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_252d_base_v024_signal(epsdil, sharesbas, closeadj):
    ps = _safe_div(epsdil, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_504d_base_v025_signal(epsdil, sharesbas, closeadj):
    ps = _safe_div(epsdil, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d epsdil scaled by assets
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_21d_base_v026_signal(epsdil, assets):
    scaled = _safe_div(epsdil, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d epsdil scaled by assets
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_63d_base_v027_signal(epsdil, assets):
    scaled = _safe_div(epsdil, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d epsdil scaled by assets
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_126d_base_v028_signal(epsdil, assets):
    scaled = _safe_div(epsdil, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d epsdil scaled by assets
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_252d_base_v029_signal(epsdil, assets):
    scaled = _safe_div(epsdil, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d epsdil scaled by assets
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_504d_base_v030_signal(epsdil, assets):
    scaled = _safe_div(epsdil, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d epsdil scaled by marketcap
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_21d_base_v031_signal(epsdil, marketcap):
    scaled = _safe_div(epsdil, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d epsdil scaled by marketcap
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_63d_base_v032_signal(epsdil, marketcap):
    scaled = _safe_div(epsdil, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d epsdil scaled by marketcap
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_126d_base_v033_signal(epsdil, marketcap):
    scaled = _safe_div(epsdil, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d epsdil scaled by marketcap
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_252d_base_v034_signal(epsdil, marketcap):
    scaled = _safe_div(epsdil, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d epsdil scaled by marketcap
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_504d_base_v035_signal(epsdil, marketcap):
    scaled = _safe_div(epsdil, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_21d_base_v036_signal(epsdil):
    low = epsdil.rolling(21).min()
    result = _safe_div(epsdil - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_63d_base_v037_signal(epsdil):
    low = epsdil.rolling(63).min()
    result = _safe_div(epsdil - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_126d_base_v038_signal(epsdil):
    low = epsdil.rolling(126).min()
    result = _safe_div(epsdil - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_252d_base_v039_signal(epsdil):
    low = epsdil.rolling(252).min()
    result = _safe_div(epsdil - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_504d_base_v040_signal(epsdil):
    low = epsdil.rolling(504).min()
    result = _safe_div(epsdil - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_21d_base_v041_signal(epsdil):
    high = epsdil.rolling(21).max()
    result = _safe_div(high - epsdil, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_63d_base_v042_signal(epsdil):
    high = epsdil.rolling(63).max()
    result = _safe_div(high - epsdil, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_126d_base_v043_signal(epsdil):
    high = epsdil.rolling(126).max()
    result = _safe_div(high - epsdil, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_252d_base_v044_signal(epsdil):
    high = epsdil.rolling(252).max()
    result = _safe_div(high - epsdil, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_504d_base_v045_signal(epsdil):
    high = epsdil.rolling(504).max()
    result = _safe_div(high - epsdil, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_21d_base_v046_signal(epsdil):
    m1 = _mean(epsdil, 21)
    m2 = _mean(epsdil, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_63d_base_v047_signal(epsdil):
    m1 = _mean(epsdil, 63)
    m2 = _mean(epsdil, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_126d_base_v048_signal(epsdil):
    m1 = _mean(epsdil, 126)
    m2 = _mean(epsdil, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_252d_base_v049_signal(epsdil):
    m1 = _mean(epsdil, 252)
    m2 = _mean(epsdil, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_504d_base_v050_signal(epsdil):
    m1 = _mean(epsdil, 504)
    m2 = _mean(epsdil, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_skew_21d_base_v051_signal(epsdil):
    result = _skew(epsdil, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_skew_63d_base_v052_signal(epsdil):
    result = _skew(epsdil, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_skew_126d_base_v053_signal(epsdil):
    result = _skew(epsdil, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_skew_252d_base_v054_signal(epsdil):
    result = _skew(epsdil, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_skew_504d_base_v055_signal(epsdil):
    result = _skew(epsdil, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_kurt_21d_base_v056_signal(epsdil):
    result = _kurt(epsdil, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_kurt_63d_base_v057_signal(epsdil):
    result = _kurt(epsdil, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_kurt_126d_base_v058_signal(epsdil):
    result = _kurt(epsdil, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_kurt_252d_base_v059_signal(epsdil):
    result = _kurt(epsdil, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_kurt_504d_base_v060_signal(epsdil):
    result = _kurt(epsdil, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_rank_21d_base_v061_signal(epsdil, closeadj):
    result = _rank(epsdil, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_rank_63d_base_v062_signal(epsdil, closeadj):
    result = _rank(epsdil, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_rank_126d_base_v063_signal(epsdil, closeadj):
    result = _rank(epsdil, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_rank_252d_base_v064_signal(epsdil, closeadj):
    result = _rank(epsdil, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_rank_504d_base_v065_signal(epsdil, closeadj):
    result = _rank(epsdil, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_autocorr_21d_base_v066_signal(epsdil):
    result = _autocorr(epsdil, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_autocorr_63d_base_v067_signal(epsdil):
    result = _autocorr(epsdil, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_autocorr_126d_base_v068_signal(epsdil):
    result = _autocorr(epsdil, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_autocorr_252d_base_v069_signal(epsdil):
    result = _autocorr(epsdil, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_autocorr_504d_base_v070_signal(epsdil):
    result = _autocorr(epsdil, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_std_21d_base_v071_signal(epsdil, closeadj):
    result = _std(epsdil, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_std_63d_base_v072_signal(epsdil, closeadj):
    result = _std(epsdil, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_std_126d_base_v073_signal(epsdil, closeadj):
    result = _std(epsdil, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_std_252d_base_v074_signal(epsdil, closeadj):
    result = _std(epsdil, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_std_504d_base_v075_signal(epsdil, closeadj):
    result = _std(epsdil, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

