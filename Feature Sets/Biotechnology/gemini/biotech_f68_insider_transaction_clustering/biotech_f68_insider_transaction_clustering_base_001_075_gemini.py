
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_21d_base_v001_signal(ownername, closeadj):
    result = _mean(ownername, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_63d_base_v002_signal(ownername, closeadj):
    result = _mean(ownername, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_126d_base_v003_signal(ownername, closeadj):
    result = _mean(ownername, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_252d_base_v004_signal(ownername, closeadj):
    result = _mean(ownername, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_504d_base_v005_signal(ownername, closeadj):
    result = _mean(ownername, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_21d_base_v006_signal(ownername, closeadj):
    result = _mean(_log(ownername), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_63d_base_v007_signal(ownername, closeadj):
    result = _mean(_log(ownername), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_126d_base_v008_signal(ownername, closeadj):
    result = _mean(_log(ownername), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_252d_base_v009_signal(ownername, closeadj):
    result = _mean(_log(ownername), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_504d_base_v010_signal(ownername, closeadj):
    result = _mean(_log(ownername), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_21d_base_v011_signal(ownername):
    result = _z(ownername, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_63d_base_v012_signal(ownername):
    result = _z(ownername, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_126d_base_v013_signal(ownername):
    result = _z(ownername, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_252d_base_v014_signal(ownername):
    result = _z(ownername, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_504d_base_v015_signal(ownername):
    result = _z(ownername, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_pct_21d_base_v016_signal(ownername):
    result = _pct_change(ownername, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_pct_63d_base_v017_signal(ownername):
    result = _pct_change(ownername, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_pct_126d_base_v018_signal(ownername):
    result = _pct_change(ownername, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_pct_252d_base_v019_signal(ownername):
    result = _pct_change(ownername, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_pct_504d_base_v020_signal(ownername):
    result = _pct_change(ownername, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_21d_base_v021_signal(ownername, sharesbas, closeadj):
    ps = _safe_div(ownername, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_63d_base_v022_signal(ownername, sharesbas, closeadj):
    ps = _safe_div(ownername, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_126d_base_v023_signal(ownername, sharesbas, closeadj):
    ps = _safe_div(ownername, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_252d_base_v024_signal(ownername, sharesbas, closeadj):
    ps = _safe_div(ownername, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_504d_base_v025_signal(ownername, sharesbas, closeadj):
    ps = _safe_div(ownername, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ownername scaled by assets
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_21d_base_v026_signal(ownername, assets):
    scaled = _safe_div(ownername, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ownername scaled by assets
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_63d_base_v027_signal(ownername, assets):
    scaled = _safe_div(ownername, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ownername scaled by assets
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_126d_base_v028_signal(ownername, assets):
    scaled = _safe_div(ownername, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ownername scaled by assets
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_252d_base_v029_signal(ownername, assets):
    scaled = _safe_div(ownername, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ownername scaled by assets
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_504d_base_v030_signal(ownername, assets):
    scaled = _safe_div(ownername, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ownername scaled by marketcap
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_21d_base_v031_signal(ownername, marketcap):
    scaled = _safe_div(ownername, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ownername scaled by marketcap
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_63d_base_v032_signal(ownername, marketcap):
    scaled = _safe_div(ownername, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ownername scaled by marketcap
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_126d_base_v033_signal(ownername, marketcap):
    scaled = _safe_div(ownername, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ownername scaled by marketcap
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_252d_base_v034_signal(ownername, marketcap):
    scaled = _safe_div(ownername, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ownername scaled by marketcap
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_504d_base_v035_signal(ownername, marketcap):
    scaled = _safe_div(ownername, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_21d_base_v036_signal(ownername):
    low = ownername.rolling(21).min()
    result = _safe_div(ownername - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_63d_base_v037_signal(ownername):
    low = ownername.rolling(63).min()
    result = _safe_div(ownername - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_126d_base_v038_signal(ownername):
    low = ownername.rolling(126).min()
    result = _safe_div(ownername - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_252d_base_v039_signal(ownername):
    low = ownername.rolling(252).min()
    result = _safe_div(ownername - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_504d_base_v040_signal(ownername):
    low = ownername.rolling(504).min()
    result = _safe_div(ownername - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_21d_base_v041_signal(ownername):
    high = ownername.rolling(21).max()
    result = _safe_div(high - ownername, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_63d_base_v042_signal(ownername):
    high = ownername.rolling(63).max()
    result = _safe_div(high - ownername, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_126d_base_v043_signal(ownername):
    high = ownername.rolling(126).max()
    result = _safe_div(high - ownername, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_252d_base_v044_signal(ownername):
    high = ownername.rolling(252).max()
    result = _safe_div(high - ownername, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_504d_base_v045_signal(ownername):
    high = ownername.rolling(504).max()
    result = _safe_div(high - ownername, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_21d_base_v046_signal(ownername):
    m1 = _mean(ownername, 21)
    m2 = _mean(ownername, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_63d_base_v047_signal(ownername):
    m1 = _mean(ownername, 63)
    m2 = _mean(ownername, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_126d_base_v048_signal(ownername):
    m1 = _mean(ownername, 126)
    m2 = _mean(ownername, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_252d_base_v049_signal(ownername):
    m1 = _mean(ownername, 252)
    m2 = _mean(ownername, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_504d_base_v050_signal(ownername):
    m1 = _mean(ownername, 504)
    m2 = _mean(ownername, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_skew_21d_base_v051_signal(ownername):
    result = _skew(ownername, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_skew_63d_base_v052_signal(ownername):
    result = _skew(ownername, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_skew_126d_base_v053_signal(ownername):
    result = _skew(ownername, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_skew_252d_base_v054_signal(ownername):
    result = _skew(ownername, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_skew_504d_base_v055_signal(ownername):
    result = _skew(ownername, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_kurt_21d_base_v056_signal(ownername):
    result = _kurt(ownername, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_kurt_63d_base_v057_signal(ownername):
    result = _kurt(ownername, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_kurt_126d_base_v058_signal(ownername):
    result = _kurt(ownername, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_kurt_252d_base_v059_signal(ownername):
    result = _kurt(ownername, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_kurt_504d_base_v060_signal(ownername):
    result = _kurt(ownername, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_rank_21d_base_v061_signal(ownername, closeadj):
    result = _rank(ownername, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_rank_63d_base_v062_signal(ownername, closeadj):
    result = _rank(ownername, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_rank_126d_base_v063_signal(ownername, closeadj):
    result = _rank(ownername, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_rank_252d_base_v064_signal(ownername, closeadj):
    result = _rank(ownername, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_rank_504d_base_v065_signal(ownername, closeadj):
    result = _rank(ownername, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_autocorr_21d_base_v066_signal(ownername):
    result = _autocorr(ownername, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_autocorr_63d_base_v067_signal(ownername):
    result = _autocorr(ownername, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_autocorr_126d_base_v068_signal(ownername):
    result = _autocorr(ownername, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_autocorr_252d_base_v069_signal(ownername):
    result = _autocorr(ownername, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_autocorr_504d_base_v070_signal(ownername):
    result = _autocorr(ownername, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_std_21d_base_v071_signal(ownername, closeadj):
    result = _std(ownername, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_std_63d_base_v072_signal(ownername, closeadj):
    result = _std(ownername, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_std_126d_base_v073_signal(ownername, closeadj):
    result = _std(ownername, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_std_252d_base_v074_signal(ownername, closeadj):
    result = _std(ownername, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_std_504d_base_v075_signal(ownername, closeadj):
    result = _std(ownername, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

