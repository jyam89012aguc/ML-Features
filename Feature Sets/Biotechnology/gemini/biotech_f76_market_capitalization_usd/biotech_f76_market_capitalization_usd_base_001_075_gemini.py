
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_21d_base_v001_signal(marketcap, closeadj):
    result = _mean(marketcap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_63d_base_v002_signal(marketcap, closeadj):
    result = _mean(marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_126d_base_v003_signal(marketcap, closeadj):
    result = _mean(marketcap, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_252d_base_v004_signal(marketcap, closeadj):
    result = _mean(marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_504d_base_v005_signal(marketcap, closeadj):
    result = _mean(marketcap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_21d_base_v006_signal(marketcap, closeadj):
    result = _mean(_log(marketcap), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_63d_base_v007_signal(marketcap, closeadj):
    result = _mean(_log(marketcap), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_126d_base_v008_signal(marketcap, closeadj):
    result = _mean(_log(marketcap), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_252d_base_v009_signal(marketcap, closeadj):
    result = _mean(_log(marketcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_504d_base_v010_signal(marketcap, closeadj):
    result = _mean(_log(marketcap), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_21d_base_v011_signal(marketcap):
    result = _z(marketcap, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_63d_base_v012_signal(marketcap):
    result = _z(marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_126d_base_v013_signal(marketcap):
    result = _z(marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_252d_base_v014_signal(marketcap):
    result = _z(marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_504d_base_v015_signal(marketcap):
    result = _z(marketcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_pct_21d_base_v016_signal(marketcap):
    result = _pct_change(marketcap, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_pct_63d_base_v017_signal(marketcap):
    result = _pct_change(marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_pct_126d_base_v018_signal(marketcap):
    result = _pct_change(marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_pct_252d_base_v019_signal(marketcap):
    result = _pct_change(marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_pct_504d_base_v020_signal(marketcap):
    result = _pct_change(marketcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_21d_base_v021_signal(marketcap, sharesbas, closeadj):
    ps = _safe_div(marketcap, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_63d_base_v022_signal(marketcap, sharesbas, closeadj):
    ps = _safe_div(marketcap, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_126d_base_v023_signal(marketcap, sharesbas, closeadj):
    ps = _safe_div(marketcap, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_252d_base_v024_signal(marketcap, sharesbas, closeadj):
    ps = _safe_div(marketcap, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_504d_base_v025_signal(marketcap, sharesbas, closeadj):
    ps = _safe_div(marketcap, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d marketcap scaled by assets
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_21d_base_v026_signal(marketcap, assets):
    scaled = _safe_div(marketcap, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d marketcap scaled by assets
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_63d_base_v027_signal(marketcap, assets):
    scaled = _safe_div(marketcap, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d marketcap scaled by assets
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_126d_base_v028_signal(marketcap, assets):
    scaled = _safe_div(marketcap, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d marketcap scaled by assets
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_252d_base_v029_signal(marketcap, assets):
    scaled = _safe_div(marketcap, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d marketcap scaled by assets
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_504d_base_v030_signal(marketcap, assets):
    scaled = _safe_div(marketcap, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d marketcap scaled by marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_21d_base_v031_signal(marketcap):
    scaled = _safe_div(marketcap, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d marketcap scaled by marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_63d_base_v032_signal(marketcap):
    scaled = _safe_div(marketcap, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d marketcap scaled by marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_126d_base_v033_signal(marketcap):
    scaled = _safe_div(marketcap, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d marketcap scaled by marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_252d_base_v034_signal(marketcap):
    scaled = _safe_div(marketcap, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d marketcap scaled by marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_504d_base_v035_signal(marketcap):
    scaled = _safe_div(marketcap, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_21d_base_v036_signal(marketcap):
    low = marketcap.rolling(21).min()
    result = _safe_div(marketcap - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_63d_base_v037_signal(marketcap):
    low = marketcap.rolling(63).min()
    result = _safe_div(marketcap - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_126d_base_v038_signal(marketcap):
    low = marketcap.rolling(126).min()
    result = _safe_div(marketcap - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_252d_base_v039_signal(marketcap):
    low = marketcap.rolling(252).min()
    result = _safe_div(marketcap - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_504d_base_v040_signal(marketcap):
    low = marketcap.rolling(504).min()
    result = _safe_div(marketcap - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_21d_base_v041_signal(marketcap):
    high = marketcap.rolling(21).max()
    result = _safe_div(high - marketcap, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_63d_base_v042_signal(marketcap):
    high = marketcap.rolling(63).max()
    result = _safe_div(high - marketcap, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_126d_base_v043_signal(marketcap):
    high = marketcap.rolling(126).max()
    result = _safe_div(high - marketcap, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_252d_base_v044_signal(marketcap):
    high = marketcap.rolling(252).max()
    result = _safe_div(high - marketcap, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_504d_base_v045_signal(marketcap):
    high = marketcap.rolling(504).max()
    result = _safe_div(high - marketcap, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_21d_base_v046_signal(marketcap):
    m1 = _mean(marketcap, 21)
    m2 = _mean(marketcap, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_63d_base_v047_signal(marketcap):
    m1 = _mean(marketcap, 63)
    m2 = _mean(marketcap, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_126d_base_v048_signal(marketcap):
    m1 = _mean(marketcap, 126)
    m2 = _mean(marketcap, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_252d_base_v049_signal(marketcap):
    m1 = _mean(marketcap, 252)
    m2 = _mean(marketcap, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_504d_base_v050_signal(marketcap):
    m1 = _mean(marketcap, 504)
    m2 = _mean(marketcap, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_skew_21d_base_v051_signal(marketcap):
    result = _skew(marketcap, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_skew_63d_base_v052_signal(marketcap):
    result = _skew(marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_skew_126d_base_v053_signal(marketcap):
    result = _skew(marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_skew_252d_base_v054_signal(marketcap):
    result = _skew(marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_skew_504d_base_v055_signal(marketcap):
    result = _skew(marketcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_kurt_21d_base_v056_signal(marketcap):
    result = _kurt(marketcap, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_kurt_63d_base_v057_signal(marketcap):
    result = _kurt(marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_kurt_126d_base_v058_signal(marketcap):
    result = _kurt(marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_kurt_252d_base_v059_signal(marketcap):
    result = _kurt(marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_kurt_504d_base_v060_signal(marketcap):
    result = _kurt(marketcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_rank_21d_base_v061_signal(marketcap, closeadj):
    result = _rank(marketcap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_rank_63d_base_v062_signal(marketcap, closeadj):
    result = _rank(marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_rank_126d_base_v063_signal(marketcap, closeadj):
    result = _rank(marketcap, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_rank_252d_base_v064_signal(marketcap, closeadj):
    result = _rank(marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_rank_504d_base_v065_signal(marketcap, closeadj):
    result = _rank(marketcap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_autocorr_21d_base_v066_signal(marketcap):
    result = _autocorr(marketcap, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_autocorr_63d_base_v067_signal(marketcap):
    result = _autocorr(marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_autocorr_126d_base_v068_signal(marketcap):
    result = _autocorr(marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_autocorr_252d_base_v069_signal(marketcap):
    result = _autocorr(marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_autocorr_504d_base_v070_signal(marketcap):
    result = _autocorr(marketcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_std_21d_base_v071_signal(marketcap, closeadj):
    result = _std(marketcap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_std_63d_base_v072_signal(marketcap, closeadj):
    result = _std(marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_std_126d_base_v073_signal(marketcap, closeadj):
    result = _std(marketcap, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_std_252d_base_v074_signal(marketcap, closeadj):
    result = _std(marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of marketcap
def gm_f76_biotech_f76_market_capitalization_usd_std_504d_base_v075_signal(marketcap, closeadj):
    result = _std(marketcap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

