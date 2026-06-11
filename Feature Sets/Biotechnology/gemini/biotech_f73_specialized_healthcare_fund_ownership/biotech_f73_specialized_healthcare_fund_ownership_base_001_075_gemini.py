
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_raw_21d_base_v001_signal(investorname, closeadj):
    result = _mean(investorname, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_raw_63d_base_v002_signal(investorname, closeadj):
    result = _mean(investorname, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_raw_126d_base_v003_signal(investorname, closeadj):
    result = _mean(investorname, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_raw_252d_base_v004_signal(investorname, closeadj):
    result = _mean(investorname, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_raw_504d_base_v005_signal(investorname, closeadj):
    result = _mean(investorname, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_log_21d_base_v006_signal(investorname, closeadj):
    result = _mean(_log(investorname), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_log_63d_base_v007_signal(investorname, closeadj):
    result = _mean(_log(investorname), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_log_126d_base_v008_signal(investorname, closeadj):
    result = _mean(_log(investorname), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_log_252d_base_v009_signal(investorname, closeadj):
    result = _mean(_log(investorname), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_log_504d_base_v010_signal(investorname, closeadj):
    result = _mean(_log(investorname), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_z_21d_base_v011_signal(investorname):
    result = _z(investorname, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_z_63d_base_v012_signal(investorname):
    result = _z(investorname, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_z_126d_base_v013_signal(investorname):
    result = _z(investorname, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_z_252d_base_v014_signal(investorname):
    result = _z(investorname, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_z_504d_base_v015_signal(investorname):
    result = _z(investorname, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_pct_21d_base_v016_signal(investorname):
    result = _pct_change(investorname, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_pct_63d_base_v017_signal(investorname):
    result = _pct_change(investorname, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_pct_126d_base_v018_signal(investorname):
    result = _pct_change(investorname, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_pct_252d_base_v019_signal(investorname):
    result = _pct_change(investorname, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_pct_504d_base_v020_signal(investorname):
    result = _pct_change(investorname, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_ps_21d_base_v021_signal(investorname, sharesbas, closeadj):
    ps = _safe_div(investorname, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_ps_63d_base_v022_signal(investorname, sharesbas, closeadj):
    ps = _safe_div(investorname, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_ps_126d_base_v023_signal(investorname, sharesbas, closeadj):
    ps = _safe_div(investorname, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_ps_252d_base_v024_signal(investorname, sharesbas, closeadj):
    ps = _safe_div(investorname, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_ps_504d_base_v025_signal(investorname, sharesbas, closeadj):
    ps = _safe_div(investorname, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of investorname to units
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_ratio_units_21d_base_v026_signal(investorname, units):
    ratio = _safe_div(investorname, units)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of investorname to units
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_ratio_units_63d_base_v027_signal(investorname, units):
    ratio = _safe_div(investorname, units)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of investorname to units
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_ratio_units_126d_base_v028_signal(investorname, units):
    ratio = _safe_div(investorname, units)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of investorname to units
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_ratio_units_252d_base_v029_signal(investorname, units):
    ratio = _safe_div(investorname, units)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of investorname to units
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_ratio_units_504d_base_v030_signal(investorname, units):
    ratio = _safe_div(investorname, units)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d investorname scaled by assets
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_asset_scaled_21d_base_v031_signal(investorname, assets):
    scaled = _safe_div(investorname, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d investorname scaled by assets
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_asset_scaled_63d_base_v032_signal(investorname, assets):
    scaled = _safe_div(investorname, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d investorname scaled by assets
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_asset_scaled_126d_base_v033_signal(investorname, assets):
    scaled = _safe_div(investorname, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d investorname scaled by assets
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_asset_scaled_252d_base_v034_signal(investorname, assets):
    scaled = _safe_div(investorname, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d investorname scaled by assets
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_asset_scaled_504d_base_v035_signal(investorname, assets):
    scaled = _safe_div(investorname, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d investorname scaled by marketcap
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_mcap_scaled_21d_base_v036_signal(investorname, marketcap):
    scaled = _safe_div(investorname, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d investorname scaled by marketcap
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_mcap_scaled_63d_base_v037_signal(investorname, marketcap):
    scaled = _safe_div(investorname, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d investorname scaled by marketcap
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_mcap_scaled_126d_base_v038_signal(investorname, marketcap):
    scaled = _safe_div(investorname, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d investorname scaled by marketcap
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_mcap_scaled_252d_base_v039_signal(investorname, marketcap):
    scaled = _safe_div(investorname, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d investorname scaled by marketcap
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_mcap_scaled_504d_base_v040_signal(investorname, marketcap):
    scaled = _safe_div(investorname, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_dist_low_21d_base_v041_signal(investorname):
    low = investorname.rolling(21).min()
    result = _safe_div(investorname - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_dist_low_63d_base_v042_signal(investorname):
    low = investorname.rolling(63).min()
    result = _safe_div(investorname - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_dist_low_126d_base_v043_signal(investorname):
    low = investorname.rolling(126).min()
    result = _safe_div(investorname - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_dist_low_252d_base_v044_signal(investorname):
    low = investorname.rolling(252).min()
    result = _safe_div(investorname - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_dist_low_504d_base_v045_signal(investorname):
    low = investorname.rolling(504).min()
    result = _safe_div(investorname - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_dist_high_21d_base_v046_signal(investorname):
    high = investorname.rolling(21).max()
    result = _safe_div(high - investorname, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_dist_high_63d_base_v047_signal(investorname):
    high = investorname.rolling(63).max()
    result = _safe_div(high - investorname, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_dist_high_126d_base_v048_signal(investorname):
    high = investorname.rolling(126).max()
    result = _safe_div(high - investorname, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_dist_high_252d_base_v049_signal(investorname):
    high = investorname.rolling(252).max()
    result = _safe_div(high - investorname, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_dist_high_504d_base_v050_signal(investorname):
    high = investorname.rolling(504).max()
    result = _safe_div(high - investorname, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_mom_21d_base_v051_signal(investorname):
    m1 = _mean(investorname, 21)
    m2 = _mean(investorname, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_mom_63d_base_v052_signal(investorname):
    m1 = _mean(investorname, 63)
    m2 = _mean(investorname, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_mom_126d_base_v053_signal(investorname):
    m1 = _mean(investorname, 126)
    m2 = _mean(investorname, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_mom_252d_base_v054_signal(investorname):
    m1 = _mean(investorname, 252)
    m2 = _mean(investorname, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_mom_504d_base_v055_signal(investorname):
    m1 = _mean(investorname, 504)
    m2 = _mean(investorname, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_skew_21d_base_v056_signal(investorname):
    result = _skew(investorname, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_skew_63d_base_v057_signal(investorname):
    result = _skew(investorname, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_skew_126d_base_v058_signal(investorname):
    result = _skew(investorname, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_skew_252d_base_v059_signal(investorname):
    result = _skew(investorname, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_skew_504d_base_v060_signal(investorname):
    result = _skew(investorname, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_kurt_21d_base_v061_signal(investorname):
    result = _kurt(investorname, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_kurt_63d_base_v062_signal(investorname):
    result = _kurt(investorname, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_kurt_126d_base_v063_signal(investorname):
    result = _kurt(investorname, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_kurt_252d_base_v064_signal(investorname):
    result = _kurt(investorname, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_kurt_504d_base_v065_signal(investorname):
    result = _kurt(investorname, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_rank_21d_base_v066_signal(investorname, closeadj):
    result = _rank(investorname, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_rank_63d_base_v067_signal(investorname, closeadj):
    result = _rank(investorname, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_rank_126d_base_v068_signal(investorname, closeadj):
    result = _rank(investorname, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_rank_252d_base_v069_signal(investorname, closeadj):
    result = _rank(investorname, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_rank_504d_base_v070_signal(investorname, closeadj):
    result = _rank(investorname, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_autocorr_21d_base_v071_signal(investorname):
    result = _autocorr(investorname, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_autocorr_63d_base_v072_signal(investorname):
    result = _autocorr(investorname, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_autocorr_126d_base_v073_signal(investorname):
    result = _autocorr(investorname, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_autocorr_252d_base_v074_signal(investorname):
    result = _autocorr(investorname, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of investorname
def gm_f73_biotech_f73_specialized_healthcare_fund_ownership_autocorr_504d_base_v075_signal(investorname):
    result = _autocorr(investorname, 504)
    return result.replace([np.inf, -np.inf], np.nan)

