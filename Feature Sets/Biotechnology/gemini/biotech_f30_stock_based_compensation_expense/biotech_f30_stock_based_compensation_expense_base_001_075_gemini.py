
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_21d_base_v001_signal(sbcomp, closeadj):
    result = _mean(sbcomp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_63d_base_v002_signal(sbcomp, closeadj):
    result = _mean(sbcomp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_126d_base_v003_signal(sbcomp, closeadj):
    result = _mean(sbcomp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_252d_base_v004_signal(sbcomp, closeadj):
    result = _mean(sbcomp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_504d_base_v005_signal(sbcomp, closeadj):
    result = _mean(sbcomp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_21d_base_v006_signal(sbcomp, closeadj):
    result = _mean(_log(sbcomp), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_63d_base_v007_signal(sbcomp, closeadj):
    result = _mean(_log(sbcomp), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_126d_base_v008_signal(sbcomp, closeadj):
    result = _mean(_log(sbcomp), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_252d_base_v009_signal(sbcomp, closeadj):
    result = _mean(_log(sbcomp), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_504d_base_v010_signal(sbcomp, closeadj):
    result = _mean(_log(sbcomp), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_21d_base_v011_signal(sbcomp):
    result = _z(sbcomp, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_63d_base_v012_signal(sbcomp):
    result = _z(sbcomp, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_126d_base_v013_signal(sbcomp):
    result = _z(sbcomp, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_252d_base_v014_signal(sbcomp):
    result = _z(sbcomp, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_504d_base_v015_signal(sbcomp):
    result = _z(sbcomp, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_pct_21d_base_v016_signal(sbcomp):
    result = _pct_change(sbcomp, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_pct_63d_base_v017_signal(sbcomp):
    result = _pct_change(sbcomp, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_pct_126d_base_v018_signal(sbcomp):
    result = _pct_change(sbcomp, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_pct_252d_base_v019_signal(sbcomp):
    result = _pct_change(sbcomp, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_pct_504d_base_v020_signal(sbcomp):
    result = _pct_change(sbcomp, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_21d_base_v021_signal(sbcomp, sharesbas, closeadj):
    ps = _safe_div(sbcomp, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_63d_base_v022_signal(sbcomp, sharesbas, closeadj):
    ps = _safe_div(sbcomp, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_126d_base_v023_signal(sbcomp, sharesbas, closeadj):
    ps = _safe_div(sbcomp, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_252d_base_v024_signal(sbcomp, sharesbas, closeadj):
    ps = _safe_div(sbcomp, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_504d_base_v025_signal(sbcomp, sharesbas, closeadj):
    ps = _safe_div(sbcomp, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sbcomp scaled by assets
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_21d_base_v026_signal(sbcomp, assets):
    scaled = _safe_div(sbcomp, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sbcomp scaled by assets
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_63d_base_v027_signal(sbcomp, assets):
    scaled = _safe_div(sbcomp, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sbcomp scaled by assets
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_126d_base_v028_signal(sbcomp, assets):
    scaled = _safe_div(sbcomp, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sbcomp scaled by assets
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_252d_base_v029_signal(sbcomp, assets):
    scaled = _safe_div(sbcomp, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sbcomp scaled by assets
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_504d_base_v030_signal(sbcomp, assets):
    scaled = _safe_div(sbcomp, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sbcomp scaled by marketcap
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_21d_base_v031_signal(sbcomp, marketcap):
    scaled = _safe_div(sbcomp, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sbcomp scaled by marketcap
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_63d_base_v032_signal(sbcomp, marketcap):
    scaled = _safe_div(sbcomp, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sbcomp scaled by marketcap
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_126d_base_v033_signal(sbcomp, marketcap):
    scaled = _safe_div(sbcomp, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sbcomp scaled by marketcap
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_252d_base_v034_signal(sbcomp, marketcap):
    scaled = _safe_div(sbcomp, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sbcomp scaled by marketcap
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_504d_base_v035_signal(sbcomp, marketcap):
    scaled = _safe_div(sbcomp, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_21d_base_v036_signal(sbcomp):
    low = sbcomp.rolling(21).min()
    result = _safe_div(sbcomp - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_63d_base_v037_signal(sbcomp):
    low = sbcomp.rolling(63).min()
    result = _safe_div(sbcomp - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_126d_base_v038_signal(sbcomp):
    low = sbcomp.rolling(126).min()
    result = _safe_div(sbcomp - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_252d_base_v039_signal(sbcomp):
    low = sbcomp.rolling(252).min()
    result = _safe_div(sbcomp - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_504d_base_v040_signal(sbcomp):
    low = sbcomp.rolling(504).min()
    result = _safe_div(sbcomp - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_21d_base_v041_signal(sbcomp):
    high = sbcomp.rolling(21).max()
    result = _safe_div(high - sbcomp, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_63d_base_v042_signal(sbcomp):
    high = sbcomp.rolling(63).max()
    result = _safe_div(high - sbcomp, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_126d_base_v043_signal(sbcomp):
    high = sbcomp.rolling(126).max()
    result = _safe_div(high - sbcomp, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_252d_base_v044_signal(sbcomp):
    high = sbcomp.rolling(252).max()
    result = _safe_div(high - sbcomp, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_504d_base_v045_signal(sbcomp):
    high = sbcomp.rolling(504).max()
    result = _safe_div(high - sbcomp, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_21d_base_v046_signal(sbcomp):
    m1 = _mean(sbcomp, 21)
    m2 = _mean(sbcomp, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_63d_base_v047_signal(sbcomp):
    m1 = _mean(sbcomp, 63)
    m2 = _mean(sbcomp, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_126d_base_v048_signal(sbcomp):
    m1 = _mean(sbcomp, 126)
    m2 = _mean(sbcomp, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_252d_base_v049_signal(sbcomp):
    m1 = _mean(sbcomp, 252)
    m2 = _mean(sbcomp, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_504d_base_v050_signal(sbcomp):
    m1 = _mean(sbcomp, 504)
    m2 = _mean(sbcomp, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_skew_21d_base_v051_signal(sbcomp):
    result = _skew(sbcomp, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_skew_63d_base_v052_signal(sbcomp):
    result = _skew(sbcomp, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_skew_126d_base_v053_signal(sbcomp):
    result = _skew(sbcomp, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_skew_252d_base_v054_signal(sbcomp):
    result = _skew(sbcomp, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_skew_504d_base_v055_signal(sbcomp):
    result = _skew(sbcomp, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_kurt_21d_base_v056_signal(sbcomp):
    result = _kurt(sbcomp, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_kurt_63d_base_v057_signal(sbcomp):
    result = _kurt(sbcomp, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_kurt_126d_base_v058_signal(sbcomp):
    result = _kurt(sbcomp, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_kurt_252d_base_v059_signal(sbcomp):
    result = _kurt(sbcomp, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_kurt_504d_base_v060_signal(sbcomp):
    result = _kurt(sbcomp, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_rank_21d_base_v061_signal(sbcomp, closeadj):
    result = _rank(sbcomp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_rank_63d_base_v062_signal(sbcomp, closeadj):
    result = _rank(sbcomp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_rank_126d_base_v063_signal(sbcomp, closeadj):
    result = _rank(sbcomp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_rank_252d_base_v064_signal(sbcomp, closeadj):
    result = _rank(sbcomp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_rank_504d_base_v065_signal(sbcomp, closeadj):
    result = _rank(sbcomp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_autocorr_21d_base_v066_signal(sbcomp):
    result = _autocorr(sbcomp, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_autocorr_63d_base_v067_signal(sbcomp):
    result = _autocorr(sbcomp, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_autocorr_126d_base_v068_signal(sbcomp):
    result = _autocorr(sbcomp, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_autocorr_252d_base_v069_signal(sbcomp):
    result = _autocorr(sbcomp, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_autocorr_504d_base_v070_signal(sbcomp):
    result = _autocorr(sbcomp, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_std_21d_base_v071_signal(sbcomp, closeadj):
    result = _std(sbcomp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_std_63d_base_v072_signal(sbcomp, closeadj):
    result = _std(sbcomp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_std_126d_base_v073_signal(sbcomp, closeadj):
    result = _std(sbcomp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_std_252d_base_v074_signal(sbcomp, closeadj):
    result = _std(sbcomp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_std_504d_base_v075_signal(sbcomp, closeadj):
    result = _std(sbcomp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

