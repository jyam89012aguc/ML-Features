
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_21d_base_v001_signal(capex, closeadj):
    result = _mean(capex, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_63d_base_v002_signal(capex, closeadj):
    result = _mean(capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_126d_base_v003_signal(capex, closeadj):
    result = _mean(capex, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_252d_base_v004_signal(capex, closeadj):
    result = _mean(capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_504d_base_v005_signal(capex, closeadj):
    result = _mean(capex, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_21d_base_v006_signal(capex, closeadj):
    result = _mean(_log(capex), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_63d_base_v007_signal(capex, closeadj):
    result = _mean(_log(capex), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_126d_base_v008_signal(capex, closeadj):
    result = _mean(_log(capex), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_252d_base_v009_signal(capex, closeadj):
    result = _mean(_log(capex), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_504d_base_v010_signal(capex, closeadj):
    result = _mean(_log(capex), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_21d_base_v011_signal(capex):
    result = _z(capex, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_63d_base_v012_signal(capex):
    result = _z(capex, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_126d_base_v013_signal(capex):
    result = _z(capex, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_252d_base_v014_signal(capex):
    result = _z(capex, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_504d_base_v015_signal(capex):
    result = _z(capex, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_pct_21d_base_v016_signal(capex):
    result = _pct_change(capex, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_pct_63d_base_v017_signal(capex):
    result = _pct_change(capex, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_pct_126d_base_v018_signal(capex):
    result = _pct_change(capex, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_pct_252d_base_v019_signal(capex):
    result = _pct_change(capex, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_pct_504d_base_v020_signal(capex):
    result = _pct_change(capex, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_21d_base_v021_signal(capex, sharesbas, closeadj):
    ps = _safe_div(capex, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_63d_base_v022_signal(capex, sharesbas, closeadj):
    ps = _safe_div(capex, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_126d_base_v023_signal(capex, sharesbas, closeadj):
    ps = _safe_div(capex, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_252d_base_v024_signal(capex, sharesbas, closeadj):
    ps = _safe_div(capex, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_504d_base_v025_signal(capex, sharesbas, closeadj):
    ps = _safe_div(capex, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of capex to assets
def gm_f15_biotech_f15_capital_expenditure_intensity_ratio_assets_21d_base_v026_signal(capex, assets):
    ratio = _safe_div(capex, assets)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of capex to assets
def gm_f15_biotech_f15_capital_expenditure_intensity_ratio_assets_63d_base_v027_signal(capex, assets):
    ratio = _safe_div(capex, assets)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of capex to assets
def gm_f15_biotech_f15_capital_expenditure_intensity_ratio_assets_126d_base_v028_signal(capex, assets):
    ratio = _safe_div(capex, assets)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of capex to assets
def gm_f15_biotech_f15_capital_expenditure_intensity_ratio_assets_252d_base_v029_signal(capex, assets):
    ratio = _safe_div(capex, assets)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of capex to assets
def gm_f15_biotech_f15_capital_expenditure_intensity_ratio_assets_504d_base_v030_signal(capex, assets):
    ratio = _safe_div(capex, assets)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d capex scaled by assets
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_21d_base_v031_signal(capex, assets):
    scaled = _safe_div(capex, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d capex scaled by assets
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_63d_base_v032_signal(capex, assets):
    scaled = _safe_div(capex, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d capex scaled by assets
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_126d_base_v033_signal(capex, assets):
    scaled = _safe_div(capex, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d capex scaled by assets
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_252d_base_v034_signal(capex, assets):
    scaled = _safe_div(capex, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d capex scaled by assets
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_504d_base_v035_signal(capex, assets):
    scaled = _safe_div(capex, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d capex scaled by marketcap
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_21d_base_v036_signal(capex, marketcap):
    scaled = _safe_div(capex, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d capex scaled by marketcap
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_63d_base_v037_signal(capex, marketcap):
    scaled = _safe_div(capex, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d capex scaled by marketcap
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_126d_base_v038_signal(capex, marketcap):
    scaled = _safe_div(capex, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d capex scaled by marketcap
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_252d_base_v039_signal(capex, marketcap):
    scaled = _safe_div(capex, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d capex scaled by marketcap
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_504d_base_v040_signal(capex, marketcap):
    scaled = _safe_div(capex, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_21d_base_v041_signal(capex):
    low = capex.rolling(21).min()
    result = _safe_div(capex - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_63d_base_v042_signal(capex):
    low = capex.rolling(63).min()
    result = _safe_div(capex - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_126d_base_v043_signal(capex):
    low = capex.rolling(126).min()
    result = _safe_div(capex - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_252d_base_v044_signal(capex):
    low = capex.rolling(252).min()
    result = _safe_div(capex - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_504d_base_v045_signal(capex):
    low = capex.rolling(504).min()
    result = _safe_div(capex - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_21d_base_v046_signal(capex):
    high = capex.rolling(21).max()
    result = _safe_div(high - capex, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_63d_base_v047_signal(capex):
    high = capex.rolling(63).max()
    result = _safe_div(high - capex, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_126d_base_v048_signal(capex):
    high = capex.rolling(126).max()
    result = _safe_div(high - capex, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_252d_base_v049_signal(capex):
    high = capex.rolling(252).max()
    result = _safe_div(high - capex, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_504d_base_v050_signal(capex):
    high = capex.rolling(504).max()
    result = _safe_div(high - capex, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_21d_base_v051_signal(capex):
    m1 = _mean(capex, 21)
    m2 = _mean(capex, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_63d_base_v052_signal(capex):
    m1 = _mean(capex, 63)
    m2 = _mean(capex, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_126d_base_v053_signal(capex):
    m1 = _mean(capex, 126)
    m2 = _mean(capex, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_252d_base_v054_signal(capex):
    m1 = _mean(capex, 252)
    m2 = _mean(capex, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_504d_base_v055_signal(capex):
    m1 = _mean(capex, 504)
    m2 = _mean(capex, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_skew_21d_base_v056_signal(capex):
    result = _skew(capex, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_skew_63d_base_v057_signal(capex):
    result = _skew(capex, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_skew_126d_base_v058_signal(capex):
    result = _skew(capex, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_skew_252d_base_v059_signal(capex):
    result = _skew(capex, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_skew_504d_base_v060_signal(capex):
    result = _skew(capex, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_kurt_21d_base_v061_signal(capex):
    result = _kurt(capex, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_kurt_63d_base_v062_signal(capex):
    result = _kurt(capex, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_kurt_126d_base_v063_signal(capex):
    result = _kurt(capex, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_kurt_252d_base_v064_signal(capex):
    result = _kurt(capex, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_kurt_504d_base_v065_signal(capex):
    result = _kurt(capex, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_rank_21d_base_v066_signal(capex, closeadj):
    result = _rank(capex, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_rank_63d_base_v067_signal(capex, closeadj):
    result = _rank(capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_rank_126d_base_v068_signal(capex, closeadj):
    result = _rank(capex, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_rank_252d_base_v069_signal(capex, closeadj):
    result = _rank(capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_rank_504d_base_v070_signal(capex, closeadj):
    result = _rank(capex, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_autocorr_21d_base_v071_signal(capex):
    result = _autocorr(capex, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_autocorr_63d_base_v072_signal(capex):
    result = _autocorr(capex, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_autocorr_126d_base_v073_signal(capex):
    result = _autocorr(capex, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_autocorr_252d_base_v074_signal(capex):
    result = _autocorr(capex, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of capex
def gm_f15_biotech_f15_capital_expenditure_intensity_autocorr_504d_base_v075_signal(capex):
    result = _autocorr(capex, 504)
    return result.replace([np.inf, -np.inf], np.nan)

