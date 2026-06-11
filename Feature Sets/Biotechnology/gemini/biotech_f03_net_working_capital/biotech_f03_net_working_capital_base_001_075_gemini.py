
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed workingcapital
def gm_f03_biotech_f03_net_working_capital_raw_21d_base_v001_signal(workingcapital, closeadj):
    result = _mean(workingcapital, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed workingcapital
def gm_f03_biotech_f03_net_working_capital_raw_63d_base_v002_signal(workingcapital, closeadj):
    result = _mean(workingcapital, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed workingcapital
def gm_f03_biotech_f03_net_working_capital_raw_126d_base_v003_signal(workingcapital, closeadj):
    result = _mean(workingcapital, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed workingcapital
def gm_f03_biotech_f03_net_working_capital_raw_252d_base_v004_signal(workingcapital, closeadj):
    result = _mean(workingcapital, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed workingcapital
def gm_f03_biotech_f03_net_working_capital_raw_504d_base_v005_signal(workingcapital, closeadj):
    result = _mean(workingcapital, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed workingcapital
def gm_f03_biotech_f03_net_working_capital_log_21d_base_v006_signal(workingcapital, closeadj):
    result = _mean(_log(workingcapital), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed workingcapital
def gm_f03_biotech_f03_net_working_capital_log_63d_base_v007_signal(workingcapital, closeadj):
    result = _mean(_log(workingcapital), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed workingcapital
def gm_f03_biotech_f03_net_working_capital_log_126d_base_v008_signal(workingcapital, closeadj):
    result = _mean(_log(workingcapital), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed workingcapital
def gm_f03_biotech_f03_net_working_capital_log_252d_base_v009_signal(workingcapital, closeadj):
    result = _mean(_log(workingcapital), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed workingcapital
def gm_f03_biotech_f03_net_working_capital_log_504d_base_v010_signal(workingcapital, closeadj):
    result = _mean(_log(workingcapital), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of workingcapital
def gm_f03_biotech_f03_net_working_capital_z_21d_base_v011_signal(workingcapital):
    result = _z(workingcapital, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of workingcapital
def gm_f03_biotech_f03_net_working_capital_z_63d_base_v012_signal(workingcapital):
    result = _z(workingcapital, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of workingcapital
def gm_f03_biotech_f03_net_working_capital_z_126d_base_v013_signal(workingcapital):
    result = _z(workingcapital, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of workingcapital
def gm_f03_biotech_f03_net_working_capital_z_252d_base_v014_signal(workingcapital):
    result = _z(workingcapital, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of workingcapital
def gm_f03_biotech_f03_net_working_capital_z_504d_base_v015_signal(workingcapital):
    result = _z(workingcapital, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of workingcapital
def gm_f03_biotech_f03_net_working_capital_pct_21d_base_v016_signal(workingcapital):
    result = _pct_change(workingcapital, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of workingcapital
def gm_f03_biotech_f03_net_working_capital_pct_63d_base_v017_signal(workingcapital):
    result = _pct_change(workingcapital, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of workingcapital
def gm_f03_biotech_f03_net_working_capital_pct_126d_base_v018_signal(workingcapital):
    result = _pct_change(workingcapital, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of workingcapital
def gm_f03_biotech_f03_net_working_capital_pct_252d_base_v019_signal(workingcapital):
    result = _pct_change(workingcapital, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of workingcapital
def gm_f03_biotech_f03_net_working_capital_pct_504d_base_v020_signal(workingcapital):
    result = _pct_change(workingcapital, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share workingcapital
def gm_f03_biotech_f03_net_working_capital_ps_21d_base_v021_signal(workingcapital, sharesbas, closeadj):
    ps = _safe_div(workingcapital, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share workingcapital
def gm_f03_biotech_f03_net_working_capital_ps_63d_base_v022_signal(workingcapital, sharesbas, closeadj):
    ps = _safe_div(workingcapital, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share workingcapital
def gm_f03_biotech_f03_net_working_capital_ps_126d_base_v023_signal(workingcapital, sharesbas, closeadj):
    ps = _safe_div(workingcapital, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share workingcapital
def gm_f03_biotech_f03_net_working_capital_ps_252d_base_v024_signal(workingcapital, sharesbas, closeadj):
    ps = _safe_div(workingcapital, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share workingcapital
def gm_f03_biotech_f03_net_working_capital_ps_504d_base_v025_signal(workingcapital, sharesbas, closeadj):
    ps = _safe_div(workingcapital, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of workingcapital to liabilitiesc
def gm_f03_biotech_f03_net_working_capital_ratio_liabilitiesc_21d_base_v026_signal(workingcapital, liabilitiesc):
    ratio = _safe_div(workingcapital, liabilitiesc)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of workingcapital to liabilitiesc
def gm_f03_biotech_f03_net_working_capital_ratio_liabilitiesc_63d_base_v027_signal(workingcapital, liabilitiesc):
    ratio = _safe_div(workingcapital, liabilitiesc)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of workingcapital to liabilitiesc
def gm_f03_biotech_f03_net_working_capital_ratio_liabilitiesc_126d_base_v028_signal(workingcapital, liabilitiesc):
    ratio = _safe_div(workingcapital, liabilitiesc)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of workingcapital to liabilitiesc
def gm_f03_biotech_f03_net_working_capital_ratio_liabilitiesc_252d_base_v029_signal(workingcapital, liabilitiesc):
    ratio = _safe_div(workingcapital, liabilitiesc)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of workingcapital to liabilitiesc
def gm_f03_biotech_f03_net_working_capital_ratio_liabilitiesc_504d_base_v030_signal(workingcapital, liabilitiesc):
    ratio = _safe_div(workingcapital, liabilitiesc)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d workingcapital scaled by assets
def gm_f03_biotech_f03_net_working_capital_asset_scaled_21d_base_v031_signal(workingcapital, assets):
    scaled = _safe_div(workingcapital, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d workingcapital scaled by assets
def gm_f03_biotech_f03_net_working_capital_asset_scaled_63d_base_v032_signal(workingcapital, assets):
    scaled = _safe_div(workingcapital, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d workingcapital scaled by assets
def gm_f03_biotech_f03_net_working_capital_asset_scaled_126d_base_v033_signal(workingcapital, assets):
    scaled = _safe_div(workingcapital, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d workingcapital scaled by assets
def gm_f03_biotech_f03_net_working_capital_asset_scaled_252d_base_v034_signal(workingcapital, assets):
    scaled = _safe_div(workingcapital, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d workingcapital scaled by assets
def gm_f03_biotech_f03_net_working_capital_asset_scaled_504d_base_v035_signal(workingcapital, assets):
    scaled = _safe_div(workingcapital, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d workingcapital scaled by marketcap
def gm_f03_biotech_f03_net_working_capital_mcap_scaled_21d_base_v036_signal(workingcapital, marketcap):
    scaled = _safe_div(workingcapital, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d workingcapital scaled by marketcap
def gm_f03_biotech_f03_net_working_capital_mcap_scaled_63d_base_v037_signal(workingcapital, marketcap):
    scaled = _safe_div(workingcapital, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d workingcapital scaled by marketcap
def gm_f03_biotech_f03_net_working_capital_mcap_scaled_126d_base_v038_signal(workingcapital, marketcap):
    scaled = _safe_div(workingcapital, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d workingcapital scaled by marketcap
def gm_f03_biotech_f03_net_working_capital_mcap_scaled_252d_base_v039_signal(workingcapital, marketcap):
    scaled = _safe_div(workingcapital, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d workingcapital scaled by marketcap
def gm_f03_biotech_f03_net_working_capital_mcap_scaled_504d_base_v040_signal(workingcapital, marketcap):
    scaled = _safe_div(workingcapital, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low workingcapital
def gm_f03_biotech_f03_net_working_capital_dist_low_21d_base_v041_signal(workingcapital):
    low = workingcapital.rolling(21).min()
    result = _safe_div(workingcapital - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low workingcapital
def gm_f03_biotech_f03_net_working_capital_dist_low_63d_base_v042_signal(workingcapital):
    low = workingcapital.rolling(63).min()
    result = _safe_div(workingcapital - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low workingcapital
def gm_f03_biotech_f03_net_working_capital_dist_low_126d_base_v043_signal(workingcapital):
    low = workingcapital.rolling(126).min()
    result = _safe_div(workingcapital - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low workingcapital
def gm_f03_biotech_f03_net_working_capital_dist_low_252d_base_v044_signal(workingcapital):
    low = workingcapital.rolling(252).min()
    result = _safe_div(workingcapital - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low workingcapital
def gm_f03_biotech_f03_net_working_capital_dist_low_504d_base_v045_signal(workingcapital):
    low = workingcapital.rolling(504).min()
    result = _safe_div(workingcapital - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high workingcapital
def gm_f03_biotech_f03_net_working_capital_dist_high_21d_base_v046_signal(workingcapital):
    high = workingcapital.rolling(21).max()
    result = _safe_div(high - workingcapital, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high workingcapital
def gm_f03_biotech_f03_net_working_capital_dist_high_63d_base_v047_signal(workingcapital):
    high = workingcapital.rolling(63).max()
    result = _safe_div(high - workingcapital, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high workingcapital
def gm_f03_biotech_f03_net_working_capital_dist_high_126d_base_v048_signal(workingcapital):
    high = workingcapital.rolling(126).max()
    result = _safe_div(high - workingcapital, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high workingcapital
def gm_f03_biotech_f03_net_working_capital_dist_high_252d_base_v049_signal(workingcapital):
    high = workingcapital.rolling(252).max()
    result = _safe_div(high - workingcapital, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high workingcapital
def gm_f03_biotech_f03_net_working_capital_dist_high_504d_base_v050_signal(workingcapital):
    high = workingcapital.rolling(504).max()
    result = _safe_div(high - workingcapital, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of workingcapital
def gm_f03_biotech_f03_net_working_capital_mom_21d_base_v051_signal(workingcapital):
    m1 = _mean(workingcapital, 21)
    m2 = _mean(workingcapital, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of workingcapital
def gm_f03_biotech_f03_net_working_capital_mom_63d_base_v052_signal(workingcapital):
    m1 = _mean(workingcapital, 63)
    m2 = _mean(workingcapital, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of workingcapital
def gm_f03_biotech_f03_net_working_capital_mom_126d_base_v053_signal(workingcapital):
    m1 = _mean(workingcapital, 126)
    m2 = _mean(workingcapital, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of workingcapital
def gm_f03_biotech_f03_net_working_capital_mom_252d_base_v054_signal(workingcapital):
    m1 = _mean(workingcapital, 252)
    m2 = _mean(workingcapital, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of workingcapital
def gm_f03_biotech_f03_net_working_capital_mom_504d_base_v055_signal(workingcapital):
    m1 = _mean(workingcapital, 504)
    m2 = _mean(workingcapital, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of workingcapital
def gm_f03_biotech_f03_net_working_capital_skew_21d_base_v056_signal(workingcapital):
    result = _skew(workingcapital, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of workingcapital
def gm_f03_biotech_f03_net_working_capital_skew_63d_base_v057_signal(workingcapital):
    result = _skew(workingcapital, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of workingcapital
def gm_f03_biotech_f03_net_working_capital_skew_126d_base_v058_signal(workingcapital):
    result = _skew(workingcapital, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of workingcapital
def gm_f03_biotech_f03_net_working_capital_skew_252d_base_v059_signal(workingcapital):
    result = _skew(workingcapital, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of workingcapital
def gm_f03_biotech_f03_net_working_capital_skew_504d_base_v060_signal(workingcapital):
    result = _skew(workingcapital, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of workingcapital
def gm_f03_biotech_f03_net_working_capital_kurt_21d_base_v061_signal(workingcapital):
    result = _kurt(workingcapital, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of workingcapital
def gm_f03_biotech_f03_net_working_capital_kurt_63d_base_v062_signal(workingcapital):
    result = _kurt(workingcapital, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of workingcapital
def gm_f03_biotech_f03_net_working_capital_kurt_126d_base_v063_signal(workingcapital):
    result = _kurt(workingcapital, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of workingcapital
def gm_f03_biotech_f03_net_working_capital_kurt_252d_base_v064_signal(workingcapital):
    result = _kurt(workingcapital, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of workingcapital
def gm_f03_biotech_f03_net_working_capital_kurt_504d_base_v065_signal(workingcapital):
    result = _kurt(workingcapital, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of workingcapital
def gm_f03_biotech_f03_net_working_capital_rank_21d_base_v066_signal(workingcapital, closeadj):
    result = _rank(workingcapital, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of workingcapital
def gm_f03_biotech_f03_net_working_capital_rank_63d_base_v067_signal(workingcapital, closeadj):
    result = _rank(workingcapital, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of workingcapital
def gm_f03_biotech_f03_net_working_capital_rank_126d_base_v068_signal(workingcapital, closeadj):
    result = _rank(workingcapital, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of workingcapital
def gm_f03_biotech_f03_net_working_capital_rank_252d_base_v069_signal(workingcapital, closeadj):
    result = _rank(workingcapital, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of workingcapital
def gm_f03_biotech_f03_net_working_capital_rank_504d_base_v070_signal(workingcapital, closeadj):
    result = _rank(workingcapital, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of workingcapital
def gm_f03_biotech_f03_net_working_capital_autocorr_21d_base_v071_signal(workingcapital):
    result = _autocorr(workingcapital, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of workingcapital
def gm_f03_biotech_f03_net_working_capital_autocorr_63d_base_v072_signal(workingcapital):
    result = _autocorr(workingcapital, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of workingcapital
def gm_f03_biotech_f03_net_working_capital_autocorr_126d_base_v073_signal(workingcapital):
    result = _autocorr(workingcapital, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of workingcapital
def gm_f03_biotech_f03_net_working_capital_autocorr_252d_base_v074_signal(workingcapital):
    result = _autocorr(workingcapital, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of workingcapital
def gm_f03_biotech_f03_net_working_capital_autocorr_504d_base_v075_signal(workingcapital):
    result = _autocorr(workingcapital, 504)
    return result.replace([np.inf, -np.inf], np.nan)

