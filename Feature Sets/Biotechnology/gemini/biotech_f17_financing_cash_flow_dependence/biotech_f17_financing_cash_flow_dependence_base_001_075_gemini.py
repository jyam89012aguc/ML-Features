
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_21d_base_v001_signal(ncff, closeadj):
    result = _mean(ncff, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_63d_base_v002_signal(ncff, closeadj):
    result = _mean(ncff, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_126d_base_v003_signal(ncff, closeadj):
    result = _mean(ncff, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_252d_base_v004_signal(ncff, closeadj):
    result = _mean(ncff, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_504d_base_v005_signal(ncff, closeadj):
    result = _mean(ncff, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_21d_base_v006_signal(ncff, closeadj):
    result = _mean(_log(ncff), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_63d_base_v007_signal(ncff, closeadj):
    result = _mean(_log(ncff), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_126d_base_v008_signal(ncff, closeadj):
    result = _mean(_log(ncff), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_252d_base_v009_signal(ncff, closeadj):
    result = _mean(_log(ncff), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_504d_base_v010_signal(ncff, closeadj):
    result = _mean(_log(ncff), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_21d_base_v011_signal(ncff):
    result = _z(ncff, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_63d_base_v012_signal(ncff):
    result = _z(ncff, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_126d_base_v013_signal(ncff):
    result = _z(ncff, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_252d_base_v014_signal(ncff):
    result = _z(ncff, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_504d_base_v015_signal(ncff):
    result = _z(ncff, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_pct_21d_base_v016_signal(ncff):
    result = _pct_change(ncff, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_pct_63d_base_v017_signal(ncff):
    result = _pct_change(ncff, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_pct_126d_base_v018_signal(ncff):
    result = _pct_change(ncff, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_pct_252d_base_v019_signal(ncff):
    result = _pct_change(ncff, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_pct_504d_base_v020_signal(ncff):
    result = _pct_change(ncff, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_21d_base_v021_signal(ncff, sharesbas, closeadj):
    ps = _safe_div(ncff, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_63d_base_v022_signal(ncff, sharesbas, closeadj):
    ps = _safe_div(ncff, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_126d_base_v023_signal(ncff, sharesbas, closeadj):
    ps = _safe_div(ncff, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_252d_base_v024_signal(ncff, sharesbas, closeadj):
    ps = _safe_div(ncff, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_504d_base_v025_signal(ncff, sharesbas, closeadj):
    ps = _safe_div(ncff, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ncff scaled by assets
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_21d_base_v026_signal(ncff, assets):
    scaled = _safe_div(ncff, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ncff scaled by assets
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_63d_base_v027_signal(ncff, assets):
    scaled = _safe_div(ncff, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ncff scaled by assets
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_126d_base_v028_signal(ncff, assets):
    scaled = _safe_div(ncff, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ncff scaled by assets
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_252d_base_v029_signal(ncff, assets):
    scaled = _safe_div(ncff, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ncff scaled by assets
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_504d_base_v030_signal(ncff, assets):
    scaled = _safe_div(ncff, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ncff scaled by marketcap
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_21d_base_v031_signal(ncff, marketcap):
    scaled = _safe_div(ncff, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ncff scaled by marketcap
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_63d_base_v032_signal(ncff, marketcap):
    scaled = _safe_div(ncff, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ncff scaled by marketcap
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_126d_base_v033_signal(ncff, marketcap):
    scaled = _safe_div(ncff, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ncff scaled by marketcap
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_252d_base_v034_signal(ncff, marketcap):
    scaled = _safe_div(ncff, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ncff scaled by marketcap
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_504d_base_v035_signal(ncff, marketcap):
    scaled = _safe_div(ncff, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_21d_base_v036_signal(ncff):
    low = ncff.rolling(21).min()
    result = _safe_div(ncff - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_63d_base_v037_signal(ncff):
    low = ncff.rolling(63).min()
    result = _safe_div(ncff - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_126d_base_v038_signal(ncff):
    low = ncff.rolling(126).min()
    result = _safe_div(ncff - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_252d_base_v039_signal(ncff):
    low = ncff.rolling(252).min()
    result = _safe_div(ncff - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_504d_base_v040_signal(ncff):
    low = ncff.rolling(504).min()
    result = _safe_div(ncff - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_21d_base_v041_signal(ncff):
    high = ncff.rolling(21).max()
    result = _safe_div(high - ncff, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_63d_base_v042_signal(ncff):
    high = ncff.rolling(63).max()
    result = _safe_div(high - ncff, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_126d_base_v043_signal(ncff):
    high = ncff.rolling(126).max()
    result = _safe_div(high - ncff, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_252d_base_v044_signal(ncff):
    high = ncff.rolling(252).max()
    result = _safe_div(high - ncff, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_504d_base_v045_signal(ncff):
    high = ncff.rolling(504).max()
    result = _safe_div(high - ncff, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_21d_base_v046_signal(ncff):
    m1 = _mean(ncff, 21)
    m2 = _mean(ncff, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_63d_base_v047_signal(ncff):
    m1 = _mean(ncff, 63)
    m2 = _mean(ncff, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_126d_base_v048_signal(ncff):
    m1 = _mean(ncff, 126)
    m2 = _mean(ncff, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_252d_base_v049_signal(ncff):
    m1 = _mean(ncff, 252)
    m2 = _mean(ncff, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_504d_base_v050_signal(ncff):
    m1 = _mean(ncff, 504)
    m2 = _mean(ncff, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_skew_21d_base_v051_signal(ncff):
    result = _skew(ncff, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_skew_63d_base_v052_signal(ncff):
    result = _skew(ncff, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_skew_126d_base_v053_signal(ncff):
    result = _skew(ncff, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_skew_252d_base_v054_signal(ncff):
    result = _skew(ncff, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_skew_504d_base_v055_signal(ncff):
    result = _skew(ncff, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_kurt_21d_base_v056_signal(ncff):
    result = _kurt(ncff, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_kurt_63d_base_v057_signal(ncff):
    result = _kurt(ncff, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_kurt_126d_base_v058_signal(ncff):
    result = _kurt(ncff, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_kurt_252d_base_v059_signal(ncff):
    result = _kurt(ncff, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_kurt_504d_base_v060_signal(ncff):
    result = _kurt(ncff, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_rank_21d_base_v061_signal(ncff, closeadj):
    result = _rank(ncff, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_rank_63d_base_v062_signal(ncff, closeadj):
    result = _rank(ncff, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_rank_126d_base_v063_signal(ncff, closeadj):
    result = _rank(ncff, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_rank_252d_base_v064_signal(ncff, closeadj):
    result = _rank(ncff, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_rank_504d_base_v065_signal(ncff, closeadj):
    result = _rank(ncff, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_autocorr_21d_base_v066_signal(ncff):
    result = _autocorr(ncff, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_autocorr_63d_base_v067_signal(ncff):
    result = _autocorr(ncff, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_autocorr_126d_base_v068_signal(ncff):
    result = _autocorr(ncff, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_autocorr_252d_base_v069_signal(ncff):
    result = _autocorr(ncff, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_autocorr_504d_base_v070_signal(ncff):
    result = _autocorr(ncff, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_std_21d_base_v071_signal(ncff, closeadj):
    result = _std(ncff, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_std_63d_base_v072_signal(ncff, closeadj):
    result = _std(ncff, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_std_126d_base_v073_signal(ncff, closeadj):
    result = _std(ncff, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_std_252d_base_v074_signal(ncff, closeadj):
    result = _std(ncff, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_std_504d_base_v075_signal(ncff, closeadj):
    result = _std(ncff, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

