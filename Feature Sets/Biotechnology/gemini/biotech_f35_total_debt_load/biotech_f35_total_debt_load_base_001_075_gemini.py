
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed debt
def gm_f35_biotech_f35_total_debt_load_raw_21d_base_v001_signal(debt, closeadj):
    result = _mean(debt, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed debt
def gm_f35_biotech_f35_total_debt_load_raw_63d_base_v002_signal(debt, closeadj):
    result = _mean(debt, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed debt
def gm_f35_biotech_f35_total_debt_load_raw_126d_base_v003_signal(debt, closeadj):
    result = _mean(debt, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed debt
def gm_f35_biotech_f35_total_debt_load_raw_252d_base_v004_signal(debt, closeadj):
    result = _mean(debt, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed debt
def gm_f35_biotech_f35_total_debt_load_raw_504d_base_v005_signal(debt, closeadj):
    result = _mean(debt, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed debt
def gm_f35_biotech_f35_total_debt_load_log_21d_base_v006_signal(debt, closeadj):
    result = _mean(_log(debt), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed debt
def gm_f35_biotech_f35_total_debt_load_log_63d_base_v007_signal(debt, closeadj):
    result = _mean(_log(debt), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed debt
def gm_f35_biotech_f35_total_debt_load_log_126d_base_v008_signal(debt, closeadj):
    result = _mean(_log(debt), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed debt
def gm_f35_biotech_f35_total_debt_load_log_252d_base_v009_signal(debt, closeadj):
    result = _mean(_log(debt), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed debt
def gm_f35_biotech_f35_total_debt_load_log_504d_base_v010_signal(debt, closeadj):
    result = _mean(_log(debt), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of debt
def gm_f35_biotech_f35_total_debt_load_z_21d_base_v011_signal(debt):
    result = _z(debt, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of debt
def gm_f35_biotech_f35_total_debt_load_z_63d_base_v012_signal(debt):
    result = _z(debt, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of debt
def gm_f35_biotech_f35_total_debt_load_z_126d_base_v013_signal(debt):
    result = _z(debt, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of debt
def gm_f35_biotech_f35_total_debt_load_z_252d_base_v014_signal(debt):
    result = _z(debt, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of debt
def gm_f35_biotech_f35_total_debt_load_z_504d_base_v015_signal(debt):
    result = _z(debt, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of debt
def gm_f35_biotech_f35_total_debt_load_pct_21d_base_v016_signal(debt):
    result = _pct_change(debt, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of debt
def gm_f35_biotech_f35_total_debt_load_pct_63d_base_v017_signal(debt):
    result = _pct_change(debt, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of debt
def gm_f35_biotech_f35_total_debt_load_pct_126d_base_v018_signal(debt):
    result = _pct_change(debt, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of debt
def gm_f35_biotech_f35_total_debt_load_pct_252d_base_v019_signal(debt):
    result = _pct_change(debt, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of debt
def gm_f35_biotech_f35_total_debt_load_pct_504d_base_v020_signal(debt):
    result = _pct_change(debt, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share debt
def gm_f35_biotech_f35_total_debt_load_ps_21d_base_v021_signal(debt, sharesbas, closeadj):
    ps = _safe_div(debt, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share debt
def gm_f35_biotech_f35_total_debt_load_ps_63d_base_v022_signal(debt, sharesbas, closeadj):
    ps = _safe_div(debt, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share debt
def gm_f35_biotech_f35_total_debt_load_ps_126d_base_v023_signal(debt, sharesbas, closeadj):
    ps = _safe_div(debt, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share debt
def gm_f35_biotech_f35_total_debt_load_ps_252d_base_v024_signal(debt, sharesbas, closeadj):
    ps = _safe_div(debt, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share debt
def gm_f35_biotech_f35_total_debt_load_ps_504d_base_v025_signal(debt, sharesbas, closeadj):
    ps = _safe_div(debt, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d debt scaled by assets
def gm_f35_biotech_f35_total_debt_load_asset_scaled_21d_base_v026_signal(debt, assets):
    scaled = _safe_div(debt, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d debt scaled by assets
def gm_f35_biotech_f35_total_debt_load_asset_scaled_63d_base_v027_signal(debt, assets):
    scaled = _safe_div(debt, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d debt scaled by assets
def gm_f35_biotech_f35_total_debt_load_asset_scaled_126d_base_v028_signal(debt, assets):
    scaled = _safe_div(debt, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d debt scaled by assets
def gm_f35_biotech_f35_total_debt_load_asset_scaled_252d_base_v029_signal(debt, assets):
    scaled = _safe_div(debt, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d debt scaled by assets
def gm_f35_biotech_f35_total_debt_load_asset_scaled_504d_base_v030_signal(debt, assets):
    scaled = _safe_div(debt, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d debt scaled by marketcap
def gm_f35_biotech_f35_total_debt_load_mcap_scaled_21d_base_v031_signal(debt, marketcap):
    scaled = _safe_div(debt, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d debt scaled by marketcap
def gm_f35_biotech_f35_total_debt_load_mcap_scaled_63d_base_v032_signal(debt, marketcap):
    scaled = _safe_div(debt, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d debt scaled by marketcap
def gm_f35_biotech_f35_total_debt_load_mcap_scaled_126d_base_v033_signal(debt, marketcap):
    scaled = _safe_div(debt, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d debt scaled by marketcap
def gm_f35_biotech_f35_total_debt_load_mcap_scaled_252d_base_v034_signal(debt, marketcap):
    scaled = _safe_div(debt, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d debt scaled by marketcap
def gm_f35_biotech_f35_total_debt_load_mcap_scaled_504d_base_v035_signal(debt, marketcap):
    scaled = _safe_div(debt, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low debt
def gm_f35_biotech_f35_total_debt_load_dist_low_21d_base_v036_signal(debt):
    low = debt.rolling(21).min()
    result = _safe_div(debt - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low debt
def gm_f35_biotech_f35_total_debt_load_dist_low_63d_base_v037_signal(debt):
    low = debt.rolling(63).min()
    result = _safe_div(debt - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low debt
def gm_f35_biotech_f35_total_debt_load_dist_low_126d_base_v038_signal(debt):
    low = debt.rolling(126).min()
    result = _safe_div(debt - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low debt
def gm_f35_biotech_f35_total_debt_load_dist_low_252d_base_v039_signal(debt):
    low = debt.rolling(252).min()
    result = _safe_div(debt - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low debt
def gm_f35_biotech_f35_total_debt_load_dist_low_504d_base_v040_signal(debt):
    low = debt.rolling(504).min()
    result = _safe_div(debt - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high debt
def gm_f35_biotech_f35_total_debt_load_dist_high_21d_base_v041_signal(debt):
    high = debt.rolling(21).max()
    result = _safe_div(high - debt, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high debt
def gm_f35_biotech_f35_total_debt_load_dist_high_63d_base_v042_signal(debt):
    high = debt.rolling(63).max()
    result = _safe_div(high - debt, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high debt
def gm_f35_biotech_f35_total_debt_load_dist_high_126d_base_v043_signal(debt):
    high = debt.rolling(126).max()
    result = _safe_div(high - debt, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high debt
def gm_f35_biotech_f35_total_debt_load_dist_high_252d_base_v044_signal(debt):
    high = debt.rolling(252).max()
    result = _safe_div(high - debt, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high debt
def gm_f35_biotech_f35_total_debt_load_dist_high_504d_base_v045_signal(debt):
    high = debt.rolling(504).max()
    result = _safe_div(high - debt, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of debt
def gm_f35_biotech_f35_total_debt_load_mom_21d_base_v046_signal(debt):
    m1 = _mean(debt, 21)
    m2 = _mean(debt, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of debt
def gm_f35_biotech_f35_total_debt_load_mom_63d_base_v047_signal(debt):
    m1 = _mean(debt, 63)
    m2 = _mean(debt, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of debt
def gm_f35_biotech_f35_total_debt_load_mom_126d_base_v048_signal(debt):
    m1 = _mean(debt, 126)
    m2 = _mean(debt, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of debt
def gm_f35_biotech_f35_total_debt_load_mom_252d_base_v049_signal(debt):
    m1 = _mean(debt, 252)
    m2 = _mean(debt, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of debt
def gm_f35_biotech_f35_total_debt_load_mom_504d_base_v050_signal(debt):
    m1 = _mean(debt, 504)
    m2 = _mean(debt, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of debt
def gm_f35_biotech_f35_total_debt_load_skew_21d_base_v051_signal(debt):
    result = _skew(debt, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of debt
def gm_f35_biotech_f35_total_debt_load_skew_63d_base_v052_signal(debt):
    result = _skew(debt, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of debt
def gm_f35_biotech_f35_total_debt_load_skew_126d_base_v053_signal(debt):
    result = _skew(debt, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of debt
def gm_f35_biotech_f35_total_debt_load_skew_252d_base_v054_signal(debt):
    result = _skew(debt, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of debt
def gm_f35_biotech_f35_total_debt_load_skew_504d_base_v055_signal(debt):
    result = _skew(debt, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of debt
def gm_f35_biotech_f35_total_debt_load_kurt_21d_base_v056_signal(debt):
    result = _kurt(debt, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of debt
def gm_f35_biotech_f35_total_debt_load_kurt_63d_base_v057_signal(debt):
    result = _kurt(debt, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of debt
def gm_f35_biotech_f35_total_debt_load_kurt_126d_base_v058_signal(debt):
    result = _kurt(debt, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of debt
def gm_f35_biotech_f35_total_debt_load_kurt_252d_base_v059_signal(debt):
    result = _kurt(debt, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of debt
def gm_f35_biotech_f35_total_debt_load_kurt_504d_base_v060_signal(debt):
    result = _kurt(debt, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of debt
def gm_f35_biotech_f35_total_debt_load_rank_21d_base_v061_signal(debt, closeadj):
    result = _rank(debt, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of debt
def gm_f35_biotech_f35_total_debt_load_rank_63d_base_v062_signal(debt, closeadj):
    result = _rank(debt, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of debt
def gm_f35_biotech_f35_total_debt_load_rank_126d_base_v063_signal(debt, closeadj):
    result = _rank(debt, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of debt
def gm_f35_biotech_f35_total_debt_load_rank_252d_base_v064_signal(debt, closeadj):
    result = _rank(debt, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of debt
def gm_f35_biotech_f35_total_debt_load_rank_504d_base_v065_signal(debt, closeadj):
    result = _rank(debt, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of debt
def gm_f35_biotech_f35_total_debt_load_autocorr_21d_base_v066_signal(debt):
    result = _autocorr(debt, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of debt
def gm_f35_biotech_f35_total_debt_load_autocorr_63d_base_v067_signal(debt):
    result = _autocorr(debt, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of debt
def gm_f35_biotech_f35_total_debt_load_autocorr_126d_base_v068_signal(debt):
    result = _autocorr(debt, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of debt
def gm_f35_biotech_f35_total_debt_load_autocorr_252d_base_v069_signal(debt):
    result = _autocorr(debt, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of debt
def gm_f35_biotech_f35_total_debt_load_autocorr_504d_base_v070_signal(debt):
    result = _autocorr(debt, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of debt
def gm_f35_biotech_f35_total_debt_load_std_21d_base_v071_signal(debt, closeadj):
    result = _std(debt, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of debt
def gm_f35_biotech_f35_total_debt_load_std_63d_base_v072_signal(debt, closeadj):
    result = _std(debt, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of debt
def gm_f35_biotech_f35_total_debt_load_std_126d_base_v073_signal(debt, closeadj):
    result = _std(debt, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of debt
def gm_f35_biotech_f35_total_debt_load_std_252d_base_v074_signal(debt, closeadj):
    result = _std(debt, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of debt
def gm_f35_biotech_f35_total_debt_load_std_504d_base_v075_signal(debt, closeadj):
    result = _std(debt, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

