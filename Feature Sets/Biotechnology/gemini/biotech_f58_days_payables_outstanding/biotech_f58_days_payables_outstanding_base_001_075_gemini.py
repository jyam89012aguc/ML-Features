
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed dpo
def gm_f58_biotech_f58_days_payables_outstanding_raw_21d_base_v001_signal(dpo, closeadj):
    result = _mean(dpo, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed dpo
def gm_f58_biotech_f58_days_payables_outstanding_raw_63d_base_v002_signal(dpo, closeadj):
    result = _mean(dpo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed dpo
def gm_f58_biotech_f58_days_payables_outstanding_raw_126d_base_v003_signal(dpo, closeadj):
    result = _mean(dpo, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed dpo
def gm_f58_biotech_f58_days_payables_outstanding_raw_252d_base_v004_signal(dpo, closeadj):
    result = _mean(dpo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed dpo
def gm_f58_biotech_f58_days_payables_outstanding_raw_504d_base_v005_signal(dpo, closeadj):
    result = _mean(dpo, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed dpo
def gm_f58_biotech_f58_days_payables_outstanding_log_21d_base_v006_signal(dpo, closeadj):
    result = _mean(_log(dpo), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed dpo
def gm_f58_biotech_f58_days_payables_outstanding_log_63d_base_v007_signal(dpo, closeadj):
    result = _mean(_log(dpo), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed dpo
def gm_f58_biotech_f58_days_payables_outstanding_log_126d_base_v008_signal(dpo, closeadj):
    result = _mean(_log(dpo), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed dpo
def gm_f58_biotech_f58_days_payables_outstanding_log_252d_base_v009_signal(dpo, closeadj):
    result = _mean(_log(dpo), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed dpo
def gm_f58_biotech_f58_days_payables_outstanding_log_504d_base_v010_signal(dpo, closeadj):
    result = _mean(_log(dpo), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of dpo
def gm_f58_biotech_f58_days_payables_outstanding_z_21d_base_v011_signal(dpo):
    result = _z(dpo, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dpo
def gm_f58_biotech_f58_days_payables_outstanding_z_63d_base_v012_signal(dpo):
    result = _z(dpo, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dpo
def gm_f58_biotech_f58_days_payables_outstanding_z_126d_base_v013_signal(dpo):
    result = _z(dpo, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dpo
def gm_f58_biotech_f58_days_payables_outstanding_z_252d_base_v014_signal(dpo):
    result = _z(dpo, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dpo
def gm_f58_biotech_f58_days_payables_outstanding_z_504d_base_v015_signal(dpo):
    result = _z(dpo, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of dpo
def gm_f58_biotech_f58_days_payables_outstanding_pct_21d_base_v016_signal(dpo):
    result = _pct_change(dpo, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of dpo
def gm_f58_biotech_f58_days_payables_outstanding_pct_63d_base_v017_signal(dpo):
    result = _pct_change(dpo, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of dpo
def gm_f58_biotech_f58_days_payables_outstanding_pct_126d_base_v018_signal(dpo):
    result = _pct_change(dpo, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of dpo
def gm_f58_biotech_f58_days_payables_outstanding_pct_252d_base_v019_signal(dpo):
    result = _pct_change(dpo, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of dpo
def gm_f58_biotech_f58_days_payables_outstanding_pct_504d_base_v020_signal(dpo):
    result = _pct_change(dpo, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share dpo
def gm_f58_biotech_f58_days_payables_outstanding_ps_21d_base_v021_signal(dpo, sharesbas, closeadj):
    ps = _safe_div(dpo, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share dpo
def gm_f58_biotech_f58_days_payables_outstanding_ps_63d_base_v022_signal(dpo, sharesbas, closeadj):
    ps = _safe_div(dpo, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share dpo
def gm_f58_biotech_f58_days_payables_outstanding_ps_126d_base_v023_signal(dpo, sharesbas, closeadj):
    ps = _safe_div(dpo, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share dpo
def gm_f58_biotech_f58_days_payables_outstanding_ps_252d_base_v024_signal(dpo, sharesbas, closeadj):
    ps = _safe_div(dpo, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share dpo
def gm_f58_biotech_f58_days_payables_outstanding_ps_504d_base_v025_signal(dpo, sharesbas, closeadj):
    ps = _safe_div(dpo, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of dpo to cor
def gm_f58_biotech_f58_days_payables_outstanding_ratio_cor_21d_base_v026_signal(dpo, cor):
    ratio = _safe_div(dpo, cor)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of dpo to cor
def gm_f58_biotech_f58_days_payables_outstanding_ratio_cor_63d_base_v027_signal(dpo, cor):
    ratio = _safe_div(dpo, cor)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of dpo to cor
def gm_f58_biotech_f58_days_payables_outstanding_ratio_cor_126d_base_v028_signal(dpo, cor):
    ratio = _safe_div(dpo, cor)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of dpo to cor
def gm_f58_biotech_f58_days_payables_outstanding_ratio_cor_252d_base_v029_signal(dpo, cor):
    ratio = _safe_div(dpo, cor)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of dpo to cor
def gm_f58_biotech_f58_days_payables_outstanding_ratio_cor_504d_base_v030_signal(dpo, cor):
    ratio = _safe_div(dpo, cor)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d dpo scaled by assets
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_21d_base_v031_signal(dpo, assets):
    scaled = _safe_div(dpo, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d dpo scaled by assets
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_63d_base_v032_signal(dpo, assets):
    scaled = _safe_div(dpo, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d dpo scaled by assets
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_126d_base_v033_signal(dpo, assets):
    scaled = _safe_div(dpo, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d dpo scaled by assets
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_252d_base_v034_signal(dpo, assets):
    scaled = _safe_div(dpo, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d dpo scaled by assets
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_504d_base_v035_signal(dpo, assets):
    scaled = _safe_div(dpo, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d dpo scaled by marketcap
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_21d_base_v036_signal(dpo, marketcap):
    scaled = _safe_div(dpo, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d dpo scaled by marketcap
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_63d_base_v037_signal(dpo, marketcap):
    scaled = _safe_div(dpo, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d dpo scaled by marketcap
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_126d_base_v038_signal(dpo, marketcap):
    scaled = _safe_div(dpo, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d dpo scaled by marketcap
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_252d_base_v039_signal(dpo, marketcap):
    scaled = _safe_div(dpo, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d dpo scaled by marketcap
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_504d_base_v040_signal(dpo, marketcap):
    scaled = _safe_div(dpo, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low dpo
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_21d_base_v041_signal(dpo):
    low = dpo.rolling(21).min()
    result = _safe_div(dpo - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low dpo
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_63d_base_v042_signal(dpo):
    low = dpo.rolling(63).min()
    result = _safe_div(dpo - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low dpo
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_126d_base_v043_signal(dpo):
    low = dpo.rolling(126).min()
    result = _safe_div(dpo - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low dpo
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_252d_base_v044_signal(dpo):
    low = dpo.rolling(252).min()
    result = _safe_div(dpo - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low dpo
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_504d_base_v045_signal(dpo):
    low = dpo.rolling(504).min()
    result = _safe_div(dpo - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high dpo
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_21d_base_v046_signal(dpo):
    high = dpo.rolling(21).max()
    result = _safe_div(high - dpo, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high dpo
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_63d_base_v047_signal(dpo):
    high = dpo.rolling(63).max()
    result = _safe_div(high - dpo, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high dpo
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_126d_base_v048_signal(dpo):
    high = dpo.rolling(126).max()
    result = _safe_div(high - dpo, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high dpo
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_252d_base_v049_signal(dpo):
    high = dpo.rolling(252).max()
    result = _safe_div(high - dpo, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high dpo
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_504d_base_v050_signal(dpo):
    high = dpo.rolling(504).max()
    result = _safe_div(high - dpo, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of dpo
def gm_f58_biotech_f58_days_payables_outstanding_mom_21d_base_v051_signal(dpo):
    m1 = _mean(dpo, 21)
    m2 = _mean(dpo, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of dpo
def gm_f58_biotech_f58_days_payables_outstanding_mom_63d_base_v052_signal(dpo):
    m1 = _mean(dpo, 63)
    m2 = _mean(dpo, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of dpo
def gm_f58_biotech_f58_days_payables_outstanding_mom_126d_base_v053_signal(dpo):
    m1 = _mean(dpo, 126)
    m2 = _mean(dpo, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of dpo
def gm_f58_biotech_f58_days_payables_outstanding_mom_252d_base_v054_signal(dpo):
    m1 = _mean(dpo, 252)
    m2 = _mean(dpo, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of dpo
def gm_f58_biotech_f58_days_payables_outstanding_mom_504d_base_v055_signal(dpo):
    m1 = _mean(dpo, 504)
    m2 = _mean(dpo, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of dpo
def gm_f58_biotech_f58_days_payables_outstanding_skew_21d_base_v056_signal(dpo):
    result = _skew(dpo, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of dpo
def gm_f58_biotech_f58_days_payables_outstanding_skew_63d_base_v057_signal(dpo):
    result = _skew(dpo, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of dpo
def gm_f58_biotech_f58_days_payables_outstanding_skew_126d_base_v058_signal(dpo):
    result = _skew(dpo, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of dpo
def gm_f58_biotech_f58_days_payables_outstanding_skew_252d_base_v059_signal(dpo):
    result = _skew(dpo, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of dpo
def gm_f58_biotech_f58_days_payables_outstanding_skew_504d_base_v060_signal(dpo):
    result = _skew(dpo, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of dpo
def gm_f58_biotech_f58_days_payables_outstanding_kurt_21d_base_v061_signal(dpo):
    result = _kurt(dpo, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of dpo
def gm_f58_biotech_f58_days_payables_outstanding_kurt_63d_base_v062_signal(dpo):
    result = _kurt(dpo, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of dpo
def gm_f58_biotech_f58_days_payables_outstanding_kurt_126d_base_v063_signal(dpo):
    result = _kurt(dpo, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of dpo
def gm_f58_biotech_f58_days_payables_outstanding_kurt_252d_base_v064_signal(dpo):
    result = _kurt(dpo, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of dpo
def gm_f58_biotech_f58_days_payables_outstanding_kurt_504d_base_v065_signal(dpo):
    result = _kurt(dpo, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of dpo
def gm_f58_biotech_f58_days_payables_outstanding_rank_21d_base_v066_signal(dpo, closeadj):
    result = _rank(dpo, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of dpo
def gm_f58_biotech_f58_days_payables_outstanding_rank_63d_base_v067_signal(dpo, closeadj):
    result = _rank(dpo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of dpo
def gm_f58_biotech_f58_days_payables_outstanding_rank_126d_base_v068_signal(dpo, closeadj):
    result = _rank(dpo, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of dpo
def gm_f58_biotech_f58_days_payables_outstanding_rank_252d_base_v069_signal(dpo, closeadj):
    result = _rank(dpo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of dpo
def gm_f58_biotech_f58_days_payables_outstanding_rank_504d_base_v070_signal(dpo, closeadj):
    result = _rank(dpo, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of dpo
def gm_f58_biotech_f58_days_payables_outstanding_autocorr_21d_base_v071_signal(dpo):
    result = _autocorr(dpo, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of dpo
def gm_f58_biotech_f58_days_payables_outstanding_autocorr_63d_base_v072_signal(dpo):
    result = _autocorr(dpo, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of dpo
def gm_f58_biotech_f58_days_payables_outstanding_autocorr_126d_base_v073_signal(dpo):
    result = _autocorr(dpo, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of dpo
def gm_f58_biotech_f58_days_payables_outstanding_autocorr_252d_base_v074_signal(dpo):
    result = _autocorr(dpo, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of dpo
def gm_f58_biotech_f58_days_payables_outstanding_autocorr_504d_base_v075_signal(dpo):
    result = _autocorr(dpo, 504)
    return result.replace([np.inf, -np.inf], np.nan)

