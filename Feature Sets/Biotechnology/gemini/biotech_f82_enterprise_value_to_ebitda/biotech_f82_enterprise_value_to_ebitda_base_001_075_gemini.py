
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_raw_21d_base_v001_signal(evebitda, closeadj):
    result = _mean(evebitda, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_raw_63d_base_v002_signal(evebitda, closeadj):
    result = _mean(evebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_raw_126d_base_v003_signal(evebitda, closeadj):
    result = _mean(evebitda, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_raw_252d_base_v004_signal(evebitda, closeadj):
    result = _mean(evebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_raw_504d_base_v005_signal(evebitda, closeadj):
    result = _mean(evebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_log_21d_base_v006_signal(evebitda, closeadj):
    result = _mean(_log(evebitda), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_log_63d_base_v007_signal(evebitda, closeadj):
    result = _mean(_log(evebitda), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_log_126d_base_v008_signal(evebitda, closeadj):
    result = _mean(_log(evebitda), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_log_252d_base_v009_signal(evebitda, closeadj):
    result = _mean(_log(evebitda), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_log_504d_base_v010_signal(evebitda, closeadj):
    result = _mean(_log(evebitda), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_z_21d_base_v011_signal(evebitda):
    result = _z(evebitda, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_z_63d_base_v012_signal(evebitda):
    result = _z(evebitda, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_z_126d_base_v013_signal(evebitda):
    result = _z(evebitda, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_z_252d_base_v014_signal(evebitda):
    result = _z(evebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_z_504d_base_v015_signal(evebitda):
    result = _z(evebitda, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_pct_21d_base_v016_signal(evebitda):
    result = _pct_change(evebitda, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_pct_63d_base_v017_signal(evebitda):
    result = _pct_change(evebitda, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_pct_126d_base_v018_signal(evebitda):
    result = _pct_change(evebitda, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_pct_252d_base_v019_signal(evebitda):
    result = _pct_change(evebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_pct_504d_base_v020_signal(evebitda):
    result = _pct_change(evebitda, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ps_21d_base_v021_signal(evebitda, sharesbas, closeadj):
    ps = _safe_div(evebitda, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ps_63d_base_v022_signal(evebitda, sharesbas, closeadj):
    ps = _safe_div(evebitda, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ps_126d_base_v023_signal(evebitda, sharesbas, closeadj):
    ps = _safe_div(evebitda, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ps_252d_base_v024_signal(evebitda, sharesbas, closeadj):
    ps = _safe_div(evebitda, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ps_504d_base_v025_signal(evebitda, sharesbas, closeadj):
    ps = _safe_div(evebitda, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of evebitda to ebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ratio_ebitda_21d_base_v026_signal(evebitda, ebitda):
    ratio = _safe_div(evebitda, ebitda)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of evebitda to ebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ratio_ebitda_63d_base_v027_signal(evebitda, ebitda):
    ratio = _safe_div(evebitda, ebitda)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of evebitda to ebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ratio_ebitda_126d_base_v028_signal(evebitda, ebitda):
    ratio = _safe_div(evebitda, ebitda)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of evebitda to ebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ratio_ebitda_252d_base_v029_signal(evebitda, ebitda):
    ratio = _safe_div(evebitda, ebitda)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of evebitda to ebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ratio_ebitda_504d_base_v030_signal(evebitda, ebitda):
    ratio = _safe_div(evebitda, ebitda)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d evebitda scaled by assets
def gm_f82_biotech_f82_enterprise_value_to_ebitda_asset_scaled_21d_base_v031_signal(evebitda, assets):
    scaled = _safe_div(evebitda, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d evebitda scaled by assets
def gm_f82_biotech_f82_enterprise_value_to_ebitda_asset_scaled_63d_base_v032_signal(evebitda, assets):
    scaled = _safe_div(evebitda, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d evebitda scaled by assets
def gm_f82_biotech_f82_enterprise_value_to_ebitda_asset_scaled_126d_base_v033_signal(evebitda, assets):
    scaled = _safe_div(evebitda, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d evebitda scaled by assets
def gm_f82_biotech_f82_enterprise_value_to_ebitda_asset_scaled_252d_base_v034_signal(evebitda, assets):
    scaled = _safe_div(evebitda, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d evebitda scaled by assets
def gm_f82_biotech_f82_enterprise_value_to_ebitda_asset_scaled_504d_base_v035_signal(evebitda, assets):
    scaled = _safe_div(evebitda, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d evebitda scaled by marketcap
def gm_f82_biotech_f82_enterprise_value_to_ebitda_mcap_scaled_21d_base_v036_signal(evebitda, marketcap):
    scaled = _safe_div(evebitda, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d evebitda scaled by marketcap
def gm_f82_biotech_f82_enterprise_value_to_ebitda_mcap_scaled_63d_base_v037_signal(evebitda, marketcap):
    scaled = _safe_div(evebitda, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d evebitda scaled by marketcap
def gm_f82_biotech_f82_enterprise_value_to_ebitda_mcap_scaled_126d_base_v038_signal(evebitda, marketcap):
    scaled = _safe_div(evebitda, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d evebitda scaled by marketcap
def gm_f82_biotech_f82_enterprise_value_to_ebitda_mcap_scaled_252d_base_v039_signal(evebitda, marketcap):
    scaled = _safe_div(evebitda, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d evebitda scaled by marketcap
def gm_f82_biotech_f82_enterprise_value_to_ebitda_mcap_scaled_504d_base_v040_signal(evebitda, marketcap):
    scaled = _safe_div(evebitda, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_dist_low_21d_base_v041_signal(evebitda):
    low = evebitda.rolling(21).min()
    result = _safe_div(evebitda - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_dist_low_63d_base_v042_signal(evebitda):
    low = evebitda.rolling(63).min()
    result = _safe_div(evebitda - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_dist_low_126d_base_v043_signal(evebitda):
    low = evebitda.rolling(126).min()
    result = _safe_div(evebitda - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_dist_low_252d_base_v044_signal(evebitda):
    low = evebitda.rolling(252).min()
    result = _safe_div(evebitda - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_dist_low_504d_base_v045_signal(evebitda):
    low = evebitda.rolling(504).min()
    result = _safe_div(evebitda - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_dist_high_21d_base_v046_signal(evebitda):
    high = evebitda.rolling(21).max()
    result = _safe_div(high - evebitda, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_dist_high_63d_base_v047_signal(evebitda):
    high = evebitda.rolling(63).max()
    result = _safe_div(high - evebitda, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_dist_high_126d_base_v048_signal(evebitda):
    high = evebitda.rolling(126).max()
    result = _safe_div(high - evebitda, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_dist_high_252d_base_v049_signal(evebitda):
    high = evebitda.rolling(252).max()
    result = _safe_div(high - evebitda, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_dist_high_504d_base_v050_signal(evebitda):
    high = evebitda.rolling(504).max()
    result = _safe_div(high - evebitda, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d levebitdael momentum of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_mom_21d_base_v051_signal(evebitda):
    m1 = _mean(evebitda, 21)
    m2 = _mean(evebitda, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d levebitdael momentum of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_mom_63d_base_v052_signal(evebitda):
    m1 = _mean(evebitda, 63)
    m2 = _mean(evebitda, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d levebitdael momentum of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_mom_126d_base_v053_signal(evebitda):
    m1 = _mean(evebitda, 126)
    m2 = _mean(evebitda, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d levebitdael momentum of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_mom_252d_base_v054_signal(evebitda):
    m1 = _mean(evebitda, 252)
    m2 = _mean(evebitda, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d levebitdael momentum of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_mom_504d_base_v055_signal(evebitda):
    m1 = _mean(evebitda, 504)
    m2 = _mean(evebitda, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_skew_21d_base_v056_signal(evebitda):
    result = _skew(evebitda, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_skew_63d_base_v057_signal(evebitda):
    result = _skew(evebitda, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_skew_126d_base_v058_signal(evebitda):
    result = _skew(evebitda, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_skew_252d_base_v059_signal(evebitda):
    result = _skew(evebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_skew_504d_base_v060_signal(evebitda):
    result = _skew(evebitda, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_kurt_21d_base_v061_signal(evebitda):
    result = _kurt(evebitda, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_kurt_63d_base_v062_signal(evebitda):
    result = _kurt(evebitda, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_kurt_126d_base_v063_signal(evebitda):
    result = _kurt(evebitda, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_kurt_252d_base_v064_signal(evebitda):
    result = _kurt(evebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_kurt_504d_base_v065_signal(evebitda):
    result = _kurt(evebitda, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_rank_21d_base_v066_signal(evebitda, closeadj):
    result = _rank(evebitda, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_rank_63d_base_v067_signal(evebitda, closeadj):
    result = _rank(evebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_rank_126d_base_v068_signal(evebitda, closeadj):
    result = _rank(evebitda, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_rank_252d_base_v069_signal(evebitda, closeadj):
    result = _rank(evebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_rank_504d_base_v070_signal(evebitda, closeadj):
    result = _rank(evebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_autocorr_21d_base_v071_signal(evebitda):
    result = _autocorr(evebitda, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_autocorr_63d_base_v072_signal(evebitda):
    result = _autocorr(evebitda, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_autocorr_126d_base_v073_signal(evebitda):
    result = _autocorr(evebitda, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_autocorr_252d_base_v074_signal(evebitda):
    result = _autocorr(evebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of evebitda
def gm_f82_biotech_f82_enterprise_value_to_ebitda_autocorr_504d_base_v075_signal(evebitda):
    result = _autocorr(evebitda, 504)
    return result.replace([np.inf, -np.inf], np.nan)

