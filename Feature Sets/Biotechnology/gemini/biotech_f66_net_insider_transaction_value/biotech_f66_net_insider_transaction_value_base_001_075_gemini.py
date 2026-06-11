
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_raw_21d_base_v001_signal(transactionvalue, closeadj):
    result = _mean(transactionvalue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_raw_63d_base_v002_signal(transactionvalue, closeadj):
    result = _mean(transactionvalue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_raw_126d_base_v003_signal(transactionvalue, closeadj):
    result = _mean(transactionvalue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_raw_252d_base_v004_signal(transactionvalue, closeadj):
    result = _mean(transactionvalue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_raw_504d_base_v005_signal(transactionvalue, closeadj):
    result = _mean(transactionvalue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_log_21d_base_v006_signal(transactionvalue, closeadj):
    result = _mean(_log(transactionvalue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_log_63d_base_v007_signal(transactionvalue, closeadj):
    result = _mean(_log(transactionvalue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_log_126d_base_v008_signal(transactionvalue, closeadj):
    result = _mean(_log(transactionvalue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_log_252d_base_v009_signal(transactionvalue, closeadj):
    result = _mean(_log(transactionvalue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_log_504d_base_v010_signal(transactionvalue, closeadj):
    result = _mean(_log(transactionvalue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_z_21d_base_v011_signal(transactionvalue):
    result = _z(transactionvalue, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_z_63d_base_v012_signal(transactionvalue):
    result = _z(transactionvalue, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_z_126d_base_v013_signal(transactionvalue):
    result = _z(transactionvalue, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_z_252d_base_v014_signal(transactionvalue):
    result = _z(transactionvalue, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_z_504d_base_v015_signal(transactionvalue):
    result = _z(transactionvalue, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_pct_21d_base_v016_signal(transactionvalue):
    result = _pct_change(transactionvalue, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_pct_63d_base_v017_signal(transactionvalue):
    result = _pct_change(transactionvalue, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_pct_126d_base_v018_signal(transactionvalue):
    result = _pct_change(transactionvalue, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_pct_252d_base_v019_signal(transactionvalue):
    result = _pct_change(transactionvalue, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_pct_504d_base_v020_signal(transactionvalue):
    result = _pct_change(transactionvalue, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_ps_21d_base_v021_signal(transactionvalue, sharesbas, closeadj):
    ps = _safe_div(transactionvalue, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_ps_63d_base_v022_signal(transactionvalue, sharesbas, closeadj):
    ps = _safe_div(transactionvalue, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_ps_126d_base_v023_signal(transactionvalue, sharesbas, closeadj):
    ps = _safe_div(transactionvalue, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_ps_252d_base_v024_signal(transactionvalue, sharesbas, closeadj):
    ps = _safe_div(transactionvalue, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_ps_504d_base_v025_signal(transactionvalue, sharesbas, closeadj):
    ps = _safe_div(transactionvalue, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d transactionvalue scaled by assets
def gm_f66_biotech_f66_net_insider_transaction_value_asset_scaled_21d_base_v026_signal(transactionvalue, assets):
    scaled = _safe_div(transactionvalue, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d transactionvalue scaled by assets
def gm_f66_biotech_f66_net_insider_transaction_value_asset_scaled_63d_base_v027_signal(transactionvalue, assets):
    scaled = _safe_div(transactionvalue, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d transactionvalue scaled by assets
def gm_f66_biotech_f66_net_insider_transaction_value_asset_scaled_126d_base_v028_signal(transactionvalue, assets):
    scaled = _safe_div(transactionvalue, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d transactionvalue scaled by assets
def gm_f66_biotech_f66_net_insider_transaction_value_asset_scaled_252d_base_v029_signal(transactionvalue, assets):
    scaled = _safe_div(transactionvalue, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d transactionvalue scaled by assets
def gm_f66_biotech_f66_net_insider_transaction_value_asset_scaled_504d_base_v030_signal(transactionvalue, assets):
    scaled = _safe_div(transactionvalue, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d transactionvalue scaled by marketcap
def gm_f66_biotech_f66_net_insider_transaction_value_mcap_scaled_21d_base_v031_signal(transactionvalue, marketcap):
    scaled = _safe_div(transactionvalue, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d transactionvalue scaled by marketcap
def gm_f66_biotech_f66_net_insider_transaction_value_mcap_scaled_63d_base_v032_signal(transactionvalue, marketcap):
    scaled = _safe_div(transactionvalue, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d transactionvalue scaled by marketcap
def gm_f66_biotech_f66_net_insider_transaction_value_mcap_scaled_126d_base_v033_signal(transactionvalue, marketcap):
    scaled = _safe_div(transactionvalue, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d transactionvalue scaled by marketcap
def gm_f66_biotech_f66_net_insider_transaction_value_mcap_scaled_252d_base_v034_signal(transactionvalue, marketcap):
    scaled = _safe_div(transactionvalue, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d transactionvalue scaled by marketcap
def gm_f66_biotech_f66_net_insider_transaction_value_mcap_scaled_504d_base_v035_signal(transactionvalue, marketcap):
    scaled = _safe_div(transactionvalue, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_dist_low_21d_base_v036_signal(transactionvalue):
    low = transactionvalue.rolling(21).min()
    result = _safe_div(transactionvalue - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_dist_low_63d_base_v037_signal(transactionvalue):
    low = transactionvalue.rolling(63).min()
    result = _safe_div(transactionvalue - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_dist_low_126d_base_v038_signal(transactionvalue):
    low = transactionvalue.rolling(126).min()
    result = _safe_div(transactionvalue - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_dist_low_252d_base_v039_signal(transactionvalue):
    low = transactionvalue.rolling(252).min()
    result = _safe_div(transactionvalue - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_dist_low_504d_base_v040_signal(transactionvalue):
    low = transactionvalue.rolling(504).min()
    result = _safe_div(transactionvalue - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_dist_high_21d_base_v041_signal(transactionvalue):
    high = transactionvalue.rolling(21).max()
    result = _safe_div(high - transactionvalue, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_dist_high_63d_base_v042_signal(transactionvalue):
    high = transactionvalue.rolling(63).max()
    result = _safe_div(high - transactionvalue, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_dist_high_126d_base_v043_signal(transactionvalue):
    high = transactionvalue.rolling(126).max()
    result = _safe_div(high - transactionvalue, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_dist_high_252d_base_v044_signal(transactionvalue):
    high = transactionvalue.rolling(252).max()
    result = _safe_div(high - transactionvalue, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_dist_high_504d_base_v045_signal(transactionvalue):
    high = transactionvalue.rolling(504).max()
    result = _safe_div(high - transactionvalue, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_mom_21d_base_v046_signal(transactionvalue):
    m1 = _mean(transactionvalue, 21)
    m2 = _mean(transactionvalue, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_mom_63d_base_v047_signal(transactionvalue):
    m1 = _mean(transactionvalue, 63)
    m2 = _mean(transactionvalue, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_mom_126d_base_v048_signal(transactionvalue):
    m1 = _mean(transactionvalue, 126)
    m2 = _mean(transactionvalue, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_mom_252d_base_v049_signal(transactionvalue):
    m1 = _mean(transactionvalue, 252)
    m2 = _mean(transactionvalue, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_mom_504d_base_v050_signal(transactionvalue):
    m1 = _mean(transactionvalue, 504)
    m2 = _mean(transactionvalue, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_skew_21d_base_v051_signal(transactionvalue):
    result = _skew(transactionvalue, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_skew_63d_base_v052_signal(transactionvalue):
    result = _skew(transactionvalue, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_skew_126d_base_v053_signal(transactionvalue):
    result = _skew(transactionvalue, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_skew_252d_base_v054_signal(transactionvalue):
    result = _skew(transactionvalue, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_skew_504d_base_v055_signal(transactionvalue):
    result = _skew(transactionvalue, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_kurt_21d_base_v056_signal(transactionvalue):
    result = _kurt(transactionvalue, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_kurt_63d_base_v057_signal(transactionvalue):
    result = _kurt(transactionvalue, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_kurt_126d_base_v058_signal(transactionvalue):
    result = _kurt(transactionvalue, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_kurt_252d_base_v059_signal(transactionvalue):
    result = _kurt(transactionvalue, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_kurt_504d_base_v060_signal(transactionvalue):
    result = _kurt(transactionvalue, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_rank_21d_base_v061_signal(transactionvalue, closeadj):
    result = _rank(transactionvalue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_rank_63d_base_v062_signal(transactionvalue, closeadj):
    result = _rank(transactionvalue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_rank_126d_base_v063_signal(transactionvalue, closeadj):
    result = _rank(transactionvalue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_rank_252d_base_v064_signal(transactionvalue, closeadj):
    result = _rank(transactionvalue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_rank_504d_base_v065_signal(transactionvalue, closeadj):
    result = _rank(transactionvalue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_autocorr_21d_base_v066_signal(transactionvalue):
    result = _autocorr(transactionvalue, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_autocorr_63d_base_v067_signal(transactionvalue):
    result = _autocorr(transactionvalue, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_autocorr_126d_base_v068_signal(transactionvalue):
    result = _autocorr(transactionvalue, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_autocorr_252d_base_v069_signal(transactionvalue):
    result = _autocorr(transactionvalue, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_autocorr_504d_base_v070_signal(transactionvalue):
    result = _autocorr(transactionvalue, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_std_21d_base_v071_signal(transactionvalue, closeadj):
    result = _std(transactionvalue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_std_63d_base_v072_signal(transactionvalue, closeadj):
    result = _std(transactionvalue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_std_126d_base_v073_signal(transactionvalue, closeadj):
    result = _std(transactionvalue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_std_252d_base_v074_signal(transactionvalue, closeadj):
    result = _std(transactionvalue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of transactionvalue
def gm_f66_biotech_f66_net_insider_transaction_value_std_504d_base_v075_signal(transactionvalue, closeadj):
    result = _std(transactionvalue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

