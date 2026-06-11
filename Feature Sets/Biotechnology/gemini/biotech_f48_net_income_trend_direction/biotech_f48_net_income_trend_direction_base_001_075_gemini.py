
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed netinc
def gm_f48_biotech_f48_net_income_trend_direction_raw_21d_base_v001_signal(netinc, closeadj):
    result = _mean(netinc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed netinc
def gm_f48_biotech_f48_net_income_trend_direction_raw_63d_base_v002_signal(netinc, closeadj):
    result = _mean(netinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed netinc
def gm_f48_biotech_f48_net_income_trend_direction_raw_126d_base_v003_signal(netinc, closeadj):
    result = _mean(netinc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed netinc
def gm_f48_biotech_f48_net_income_trend_direction_raw_252d_base_v004_signal(netinc, closeadj):
    result = _mean(netinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed netinc
def gm_f48_biotech_f48_net_income_trend_direction_raw_504d_base_v005_signal(netinc, closeadj):
    result = _mean(netinc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed netinc
def gm_f48_biotech_f48_net_income_trend_direction_log_21d_base_v006_signal(netinc, closeadj):
    result = _mean(_log(netinc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed netinc
def gm_f48_biotech_f48_net_income_trend_direction_log_63d_base_v007_signal(netinc, closeadj):
    result = _mean(_log(netinc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed netinc
def gm_f48_biotech_f48_net_income_trend_direction_log_126d_base_v008_signal(netinc, closeadj):
    result = _mean(_log(netinc), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed netinc
def gm_f48_biotech_f48_net_income_trend_direction_log_252d_base_v009_signal(netinc, closeadj):
    result = _mean(_log(netinc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed netinc
def gm_f48_biotech_f48_net_income_trend_direction_log_504d_base_v010_signal(netinc, closeadj):
    result = _mean(_log(netinc), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of netinc
def gm_f48_biotech_f48_net_income_trend_direction_z_21d_base_v011_signal(netinc):
    result = _z(netinc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of netinc
def gm_f48_biotech_f48_net_income_trend_direction_z_63d_base_v012_signal(netinc):
    result = _z(netinc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of netinc
def gm_f48_biotech_f48_net_income_trend_direction_z_126d_base_v013_signal(netinc):
    result = _z(netinc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of netinc
def gm_f48_biotech_f48_net_income_trend_direction_z_252d_base_v014_signal(netinc):
    result = _z(netinc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of netinc
def gm_f48_biotech_f48_net_income_trend_direction_z_504d_base_v015_signal(netinc):
    result = _z(netinc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of netinc
def gm_f48_biotech_f48_net_income_trend_direction_pct_21d_base_v016_signal(netinc):
    result = _pct_change(netinc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of netinc
def gm_f48_biotech_f48_net_income_trend_direction_pct_63d_base_v017_signal(netinc):
    result = _pct_change(netinc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of netinc
def gm_f48_biotech_f48_net_income_trend_direction_pct_126d_base_v018_signal(netinc):
    result = _pct_change(netinc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of netinc
def gm_f48_biotech_f48_net_income_trend_direction_pct_252d_base_v019_signal(netinc):
    result = _pct_change(netinc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of netinc
def gm_f48_biotech_f48_net_income_trend_direction_pct_504d_base_v020_signal(netinc):
    result = _pct_change(netinc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share netinc
def gm_f48_biotech_f48_net_income_trend_direction_ps_21d_base_v021_signal(netinc, sharesbas, closeadj):
    ps = _safe_div(netinc, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share netinc
def gm_f48_biotech_f48_net_income_trend_direction_ps_63d_base_v022_signal(netinc, sharesbas, closeadj):
    ps = _safe_div(netinc, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share netinc
def gm_f48_biotech_f48_net_income_trend_direction_ps_126d_base_v023_signal(netinc, sharesbas, closeadj):
    ps = _safe_div(netinc, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share netinc
def gm_f48_biotech_f48_net_income_trend_direction_ps_252d_base_v024_signal(netinc, sharesbas, closeadj):
    ps = _safe_div(netinc, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share netinc
def gm_f48_biotech_f48_net_income_trend_direction_ps_504d_base_v025_signal(netinc, sharesbas, closeadj):
    ps = _safe_div(netinc, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d netinc scaled by assets
def gm_f48_biotech_f48_net_income_trend_direction_asset_scaled_21d_base_v026_signal(netinc, assets):
    scaled = _safe_div(netinc, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d netinc scaled by assets
def gm_f48_biotech_f48_net_income_trend_direction_asset_scaled_63d_base_v027_signal(netinc, assets):
    scaled = _safe_div(netinc, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d netinc scaled by assets
def gm_f48_biotech_f48_net_income_trend_direction_asset_scaled_126d_base_v028_signal(netinc, assets):
    scaled = _safe_div(netinc, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d netinc scaled by assets
def gm_f48_biotech_f48_net_income_trend_direction_asset_scaled_252d_base_v029_signal(netinc, assets):
    scaled = _safe_div(netinc, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d netinc scaled by assets
def gm_f48_biotech_f48_net_income_trend_direction_asset_scaled_504d_base_v030_signal(netinc, assets):
    scaled = _safe_div(netinc, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d netinc scaled by marketcap
def gm_f48_biotech_f48_net_income_trend_direction_mcap_scaled_21d_base_v031_signal(netinc, marketcap):
    scaled = _safe_div(netinc, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d netinc scaled by marketcap
def gm_f48_biotech_f48_net_income_trend_direction_mcap_scaled_63d_base_v032_signal(netinc, marketcap):
    scaled = _safe_div(netinc, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d netinc scaled by marketcap
def gm_f48_biotech_f48_net_income_trend_direction_mcap_scaled_126d_base_v033_signal(netinc, marketcap):
    scaled = _safe_div(netinc, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d netinc scaled by marketcap
def gm_f48_biotech_f48_net_income_trend_direction_mcap_scaled_252d_base_v034_signal(netinc, marketcap):
    scaled = _safe_div(netinc, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d netinc scaled by marketcap
def gm_f48_biotech_f48_net_income_trend_direction_mcap_scaled_504d_base_v035_signal(netinc, marketcap):
    scaled = _safe_div(netinc, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low netinc
def gm_f48_biotech_f48_net_income_trend_direction_dist_low_21d_base_v036_signal(netinc):
    low = netinc.rolling(21).min()
    result = _safe_div(netinc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low netinc
def gm_f48_biotech_f48_net_income_trend_direction_dist_low_63d_base_v037_signal(netinc):
    low = netinc.rolling(63).min()
    result = _safe_div(netinc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low netinc
def gm_f48_biotech_f48_net_income_trend_direction_dist_low_126d_base_v038_signal(netinc):
    low = netinc.rolling(126).min()
    result = _safe_div(netinc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low netinc
def gm_f48_biotech_f48_net_income_trend_direction_dist_low_252d_base_v039_signal(netinc):
    low = netinc.rolling(252).min()
    result = _safe_div(netinc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low netinc
def gm_f48_biotech_f48_net_income_trend_direction_dist_low_504d_base_v040_signal(netinc):
    low = netinc.rolling(504).min()
    result = _safe_div(netinc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high netinc
def gm_f48_biotech_f48_net_income_trend_direction_dist_high_21d_base_v041_signal(netinc):
    high = netinc.rolling(21).max()
    result = _safe_div(high - netinc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high netinc
def gm_f48_biotech_f48_net_income_trend_direction_dist_high_63d_base_v042_signal(netinc):
    high = netinc.rolling(63).max()
    result = _safe_div(high - netinc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high netinc
def gm_f48_biotech_f48_net_income_trend_direction_dist_high_126d_base_v043_signal(netinc):
    high = netinc.rolling(126).max()
    result = _safe_div(high - netinc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high netinc
def gm_f48_biotech_f48_net_income_trend_direction_dist_high_252d_base_v044_signal(netinc):
    high = netinc.rolling(252).max()
    result = _safe_div(high - netinc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high netinc
def gm_f48_biotech_f48_net_income_trend_direction_dist_high_504d_base_v045_signal(netinc):
    high = netinc.rolling(504).max()
    result = _safe_div(high - netinc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of netinc
def gm_f48_biotech_f48_net_income_trend_direction_mom_21d_base_v046_signal(netinc):
    m1 = _mean(netinc, 21)
    m2 = _mean(netinc, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of netinc
def gm_f48_biotech_f48_net_income_trend_direction_mom_63d_base_v047_signal(netinc):
    m1 = _mean(netinc, 63)
    m2 = _mean(netinc, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of netinc
def gm_f48_biotech_f48_net_income_trend_direction_mom_126d_base_v048_signal(netinc):
    m1 = _mean(netinc, 126)
    m2 = _mean(netinc, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of netinc
def gm_f48_biotech_f48_net_income_trend_direction_mom_252d_base_v049_signal(netinc):
    m1 = _mean(netinc, 252)
    m2 = _mean(netinc, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of netinc
def gm_f48_biotech_f48_net_income_trend_direction_mom_504d_base_v050_signal(netinc):
    m1 = _mean(netinc, 504)
    m2 = _mean(netinc, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of netinc
def gm_f48_biotech_f48_net_income_trend_direction_skew_21d_base_v051_signal(netinc):
    result = _skew(netinc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of netinc
def gm_f48_biotech_f48_net_income_trend_direction_skew_63d_base_v052_signal(netinc):
    result = _skew(netinc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of netinc
def gm_f48_biotech_f48_net_income_trend_direction_skew_126d_base_v053_signal(netinc):
    result = _skew(netinc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of netinc
def gm_f48_biotech_f48_net_income_trend_direction_skew_252d_base_v054_signal(netinc):
    result = _skew(netinc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of netinc
def gm_f48_biotech_f48_net_income_trend_direction_skew_504d_base_v055_signal(netinc):
    result = _skew(netinc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of netinc
def gm_f48_biotech_f48_net_income_trend_direction_kurt_21d_base_v056_signal(netinc):
    result = _kurt(netinc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of netinc
def gm_f48_biotech_f48_net_income_trend_direction_kurt_63d_base_v057_signal(netinc):
    result = _kurt(netinc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of netinc
def gm_f48_biotech_f48_net_income_trend_direction_kurt_126d_base_v058_signal(netinc):
    result = _kurt(netinc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of netinc
def gm_f48_biotech_f48_net_income_trend_direction_kurt_252d_base_v059_signal(netinc):
    result = _kurt(netinc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of netinc
def gm_f48_biotech_f48_net_income_trend_direction_kurt_504d_base_v060_signal(netinc):
    result = _kurt(netinc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of netinc
def gm_f48_biotech_f48_net_income_trend_direction_rank_21d_base_v061_signal(netinc, closeadj):
    result = _rank(netinc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of netinc
def gm_f48_biotech_f48_net_income_trend_direction_rank_63d_base_v062_signal(netinc, closeadj):
    result = _rank(netinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of netinc
def gm_f48_biotech_f48_net_income_trend_direction_rank_126d_base_v063_signal(netinc, closeadj):
    result = _rank(netinc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of netinc
def gm_f48_biotech_f48_net_income_trend_direction_rank_252d_base_v064_signal(netinc, closeadj):
    result = _rank(netinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of netinc
def gm_f48_biotech_f48_net_income_trend_direction_rank_504d_base_v065_signal(netinc, closeadj):
    result = _rank(netinc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of netinc
def gm_f48_biotech_f48_net_income_trend_direction_autocorr_21d_base_v066_signal(netinc):
    result = _autocorr(netinc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of netinc
def gm_f48_biotech_f48_net_income_trend_direction_autocorr_63d_base_v067_signal(netinc):
    result = _autocorr(netinc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of netinc
def gm_f48_biotech_f48_net_income_trend_direction_autocorr_126d_base_v068_signal(netinc):
    result = _autocorr(netinc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of netinc
def gm_f48_biotech_f48_net_income_trend_direction_autocorr_252d_base_v069_signal(netinc):
    result = _autocorr(netinc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of netinc
def gm_f48_biotech_f48_net_income_trend_direction_autocorr_504d_base_v070_signal(netinc):
    result = _autocorr(netinc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of netinc
def gm_f48_biotech_f48_net_income_trend_direction_std_21d_base_v071_signal(netinc, closeadj):
    result = _std(netinc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of netinc
def gm_f48_biotech_f48_net_income_trend_direction_std_63d_base_v072_signal(netinc, closeadj):
    result = _std(netinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of netinc
def gm_f48_biotech_f48_net_income_trend_direction_std_126d_base_v073_signal(netinc, closeadj):
    result = _std(netinc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of netinc
def gm_f48_biotech_f48_net_income_trend_direction_std_252d_base_v074_signal(netinc, closeadj):
    result = _std(netinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of netinc
def gm_f48_biotech_f48_net_income_trend_direction_std_504d_base_v075_signal(netinc, closeadj):
    result = _std(netinc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

