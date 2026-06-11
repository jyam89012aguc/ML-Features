
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_21d_base_v001_signal(fcf, closeadj):
    result = _mean(fcf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_63d_base_v002_signal(fcf, closeadj):
    result = _mean(fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_126d_base_v003_signal(fcf, closeadj):
    result = _mean(fcf, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_252d_base_v004_signal(fcf, closeadj):
    result = _mean(fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_504d_base_v005_signal(fcf, closeadj):
    result = _mean(fcf, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_21d_base_v006_signal(fcf, closeadj):
    result = _mean(_log(fcf), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_63d_base_v007_signal(fcf, closeadj):
    result = _mean(_log(fcf), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_126d_base_v008_signal(fcf, closeadj):
    result = _mean(_log(fcf), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_252d_base_v009_signal(fcf, closeadj):
    result = _mean(_log(fcf), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_504d_base_v010_signal(fcf, closeadj):
    result = _mean(_log(fcf), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_21d_base_v011_signal(fcf):
    result = _z(fcf, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_63d_base_v012_signal(fcf):
    result = _z(fcf, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_126d_base_v013_signal(fcf):
    result = _z(fcf, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_252d_base_v014_signal(fcf):
    result = _z(fcf, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_504d_base_v015_signal(fcf):
    result = _z(fcf, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_pct_21d_base_v016_signal(fcf):
    result = _pct_change(fcf, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_pct_63d_base_v017_signal(fcf):
    result = _pct_change(fcf, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_pct_126d_base_v018_signal(fcf):
    result = _pct_change(fcf, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_pct_252d_base_v019_signal(fcf):
    result = _pct_change(fcf, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_pct_504d_base_v020_signal(fcf):
    result = _pct_change(fcf, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_21d_base_v021_signal(fcf, sharesbas, closeadj):
    ps = _safe_div(fcf, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_63d_base_v022_signal(fcf, sharesbas, closeadj):
    ps = _safe_div(fcf, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_126d_base_v023_signal(fcf, sharesbas, closeadj):
    ps = _safe_div(fcf, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_252d_base_v024_signal(fcf, sharesbas, closeadj):
    ps = _safe_div(fcf, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_504d_base_v025_signal(fcf, sharesbas, closeadj):
    ps = _safe_div(fcf, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d fcf scaled by assets
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_21d_base_v026_signal(fcf, assets):
    scaled = _safe_div(fcf, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d fcf scaled by assets
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_63d_base_v027_signal(fcf, assets):
    scaled = _safe_div(fcf, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d fcf scaled by assets
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_126d_base_v028_signal(fcf, assets):
    scaled = _safe_div(fcf, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d fcf scaled by assets
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_252d_base_v029_signal(fcf, assets):
    scaled = _safe_div(fcf, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d fcf scaled by assets
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_504d_base_v030_signal(fcf, assets):
    scaled = _safe_div(fcf, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d fcf scaled by marketcap
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_21d_base_v031_signal(fcf, marketcap):
    scaled = _safe_div(fcf, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d fcf scaled by marketcap
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_63d_base_v032_signal(fcf, marketcap):
    scaled = _safe_div(fcf, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d fcf scaled by marketcap
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_126d_base_v033_signal(fcf, marketcap):
    scaled = _safe_div(fcf, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d fcf scaled by marketcap
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_252d_base_v034_signal(fcf, marketcap):
    scaled = _safe_div(fcf, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d fcf scaled by marketcap
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_504d_base_v035_signal(fcf, marketcap):
    scaled = _safe_div(fcf, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_21d_base_v036_signal(fcf):
    low = fcf.rolling(21).min()
    result = _safe_div(fcf - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_63d_base_v037_signal(fcf):
    low = fcf.rolling(63).min()
    result = _safe_div(fcf - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_126d_base_v038_signal(fcf):
    low = fcf.rolling(126).min()
    result = _safe_div(fcf - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_252d_base_v039_signal(fcf):
    low = fcf.rolling(252).min()
    result = _safe_div(fcf - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_504d_base_v040_signal(fcf):
    low = fcf.rolling(504).min()
    result = _safe_div(fcf - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_21d_base_v041_signal(fcf):
    high = fcf.rolling(21).max()
    result = _safe_div(high - fcf, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_63d_base_v042_signal(fcf):
    high = fcf.rolling(63).max()
    result = _safe_div(high - fcf, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_126d_base_v043_signal(fcf):
    high = fcf.rolling(126).max()
    result = _safe_div(high - fcf, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_252d_base_v044_signal(fcf):
    high = fcf.rolling(252).max()
    result = _safe_div(high - fcf, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_504d_base_v045_signal(fcf):
    high = fcf.rolling(504).max()
    result = _safe_div(high - fcf, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_21d_base_v046_signal(fcf):
    m1 = _mean(fcf, 21)
    m2 = _mean(fcf, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_63d_base_v047_signal(fcf):
    m1 = _mean(fcf, 63)
    m2 = _mean(fcf, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_126d_base_v048_signal(fcf):
    m1 = _mean(fcf, 126)
    m2 = _mean(fcf, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_252d_base_v049_signal(fcf):
    m1 = _mean(fcf, 252)
    m2 = _mean(fcf, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_504d_base_v050_signal(fcf):
    m1 = _mean(fcf, 504)
    m2 = _mean(fcf, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_skew_21d_base_v051_signal(fcf):
    result = _skew(fcf, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_skew_63d_base_v052_signal(fcf):
    result = _skew(fcf, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_skew_126d_base_v053_signal(fcf):
    result = _skew(fcf, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_skew_252d_base_v054_signal(fcf):
    result = _skew(fcf, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_skew_504d_base_v055_signal(fcf):
    result = _skew(fcf, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_kurt_21d_base_v056_signal(fcf):
    result = _kurt(fcf, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_kurt_63d_base_v057_signal(fcf):
    result = _kurt(fcf, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_kurt_126d_base_v058_signal(fcf):
    result = _kurt(fcf, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_kurt_252d_base_v059_signal(fcf):
    result = _kurt(fcf, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_kurt_504d_base_v060_signal(fcf):
    result = _kurt(fcf, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_rank_21d_base_v061_signal(fcf, closeadj):
    result = _rank(fcf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_rank_63d_base_v062_signal(fcf, closeadj):
    result = _rank(fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_rank_126d_base_v063_signal(fcf, closeadj):
    result = _rank(fcf, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_rank_252d_base_v064_signal(fcf, closeadj):
    result = _rank(fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_rank_504d_base_v065_signal(fcf, closeadj):
    result = _rank(fcf, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_autocorr_21d_base_v066_signal(fcf):
    result = _autocorr(fcf, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_autocorr_63d_base_v067_signal(fcf):
    result = _autocorr(fcf, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_autocorr_126d_base_v068_signal(fcf):
    result = _autocorr(fcf, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_autocorr_252d_base_v069_signal(fcf):
    result = _autocorr(fcf, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_autocorr_504d_base_v070_signal(fcf):
    result = _autocorr(fcf, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_std_21d_base_v071_signal(fcf, closeadj):
    result = _std(fcf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_std_63d_base_v072_signal(fcf, closeadj):
    result = _std(fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_std_126d_base_v073_signal(fcf, closeadj):
    result = _std(fcf, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_std_252d_base_v074_signal(fcf, closeadj):
    result = _std(fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_std_504d_base_v075_signal(fcf, closeadj):
    result = _std(fcf, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

