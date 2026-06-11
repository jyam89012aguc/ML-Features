
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed pcash
def gm_f79_biotech_f79_price_to_cash_ratio_raw_21d_base_v001_signal(pcash, closeadj):
    result = _mean(pcash, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed pcash
def gm_f79_biotech_f79_price_to_cash_ratio_raw_63d_base_v002_signal(pcash, closeadj):
    result = _mean(pcash, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed pcash
def gm_f79_biotech_f79_price_to_cash_ratio_raw_126d_base_v003_signal(pcash, closeadj):
    result = _mean(pcash, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed pcash
def gm_f79_biotech_f79_price_to_cash_ratio_raw_252d_base_v004_signal(pcash, closeadj):
    result = _mean(pcash, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed pcash
def gm_f79_biotech_f79_price_to_cash_ratio_raw_504d_base_v005_signal(pcash, closeadj):
    result = _mean(pcash, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed pcash
def gm_f79_biotech_f79_price_to_cash_ratio_log_21d_base_v006_signal(pcash, closeadj):
    result = _mean(_log(pcash), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed pcash
def gm_f79_biotech_f79_price_to_cash_ratio_log_63d_base_v007_signal(pcash, closeadj):
    result = _mean(_log(pcash), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed pcash
def gm_f79_biotech_f79_price_to_cash_ratio_log_126d_base_v008_signal(pcash, closeadj):
    result = _mean(_log(pcash), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed pcash
def gm_f79_biotech_f79_price_to_cash_ratio_log_252d_base_v009_signal(pcash, closeadj):
    result = _mean(_log(pcash), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed pcash
def gm_f79_biotech_f79_price_to_cash_ratio_log_504d_base_v010_signal(pcash, closeadj):
    result = _mean(_log(pcash), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_z_21d_base_v011_signal(pcash):
    result = _z(pcash, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_z_63d_base_v012_signal(pcash):
    result = _z(pcash, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_z_126d_base_v013_signal(pcash):
    result = _z(pcash, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_z_252d_base_v014_signal(pcash):
    result = _z(pcash, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_z_504d_base_v015_signal(pcash):
    result = _z(pcash, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_pct_21d_base_v016_signal(pcash):
    result = _pct_change(pcash, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_pct_63d_base_v017_signal(pcash):
    result = _pct_change(pcash, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_pct_126d_base_v018_signal(pcash):
    result = _pct_change(pcash, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_pct_252d_base_v019_signal(pcash):
    result = _pct_change(pcash, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_pct_504d_base_v020_signal(pcash):
    result = _pct_change(pcash, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share pcash
def gm_f79_biotech_f79_price_to_cash_ratio_ps_21d_base_v021_signal(pcash, sharesbas, closeadj):
    ps = _safe_div(pcash, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share pcash
def gm_f79_biotech_f79_price_to_cash_ratio_ps_63d_base_v022_signal(pcash, sharesbas, closeadj):
    ps = _safe_div(pcash, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share pcash
def gm_f79_biotech_f79_price_to_cash_ratio_ps_126d_base_v023_signal(pcash, sharesbas, closeadj):
    ps = _safe_div(pcash, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share pcash
def gm_f79_biotech_f79_price_to_cash_ratio_ps_252d_base_v024_signal(pcash, sharesbas, closeadj):
    ps = _safe_div(pcash, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share pcash
def gm_f79_biotech_f79_price_to_cash_ratio_ps_504d_base_v025_signal(pcash, sharesbas, closeadj):
    ps = _safe_div(pcash, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of pcash to cashneq
def gm_f79_biotech_f79_price_to_cash_ratio_ratio_cashneq_21d_base_v026_signal(pcash, cashneq):
    ratio = _safe_div(pcash, cashneq)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of pcash to cashneq
def gm_f79_biotech_f79_price_to_cash_ratio_ratio_cashneq_63d_base_v027_signal(pcash, cashneq):
    ratio = _safe_div(pcash, cashneq)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of pcash to cashneq
def gm_f79_biotech_f79_price_to_cash_ratio_ratio_cashneq_126d_base_v028_signal(pcash, cashneq):
    ratio = _safe_div(pcash, cashneq)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of pcash to cashneq
def gm_f79_biotech_f79_price_to_cash_ratio_ratio_cashneq_252d_base_v029_signal(pcash, cashneq):
    ratio = _safe_div(pcash, cashneq)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of pcash to cashneq
def gm_f79_biotech_f79_price_to_cash_ratio_ratio_cashneq_504d_base_v030_signal(pcash, cashneq):
    ratio = _safe_div(pcash, cashneq)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pcash scaled by assets
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_21d_base_v031_signal(pcash, assets):
    scaled = _safe_div(pcash, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pcash scaled by assets
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_63d_base_v032_signal(pcash, assets):
    scaled = _safe_div(pcash, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pcash scaled by assets
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_126d_base_v033_signal(pcash, assets):
    scaled = _safe_div(pcash, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pcash scaled by assets
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_252d_base_v034_signal(pcash, assets):
    scaled = _safe_div(pcash, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pcash scaled by assets
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_504d_base_v035_signal(pcash, assets):
    scaled = _safe_div(pcash, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pcash scaled by pcash
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_21d_base_v036_signal(pcash):
    scaled = _safe_div(pcash, pcash)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pcash scaled by pcash
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_63d_base_v037_signal(pcash):
    scaled = _safe_div(pcash, pcash)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pcash scaled by pcash
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_126d_base_v038_signal(pcash):
    scaled = _safe_div(pcash, pcash)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pcash scaled by pcash
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_252d_base_v039_signal(pcash):
    scaled = _safe_div(pcash, pcash)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pcash scaled by pcash
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_504d_base_v040_signal(pcash):
    scaled = _safe_div(pcash, pcash)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low pcash
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_21d_base_v041_signal(pcash):
    low = pcash.rolling(21).min()
    result = _safe_div(pcash - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low pcash
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_63d_base_v042_signal(pcash):
    low = pcash.rolling(63).min()
    result = _safe_div(pcash - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low pcash
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_126d_base_v043_signal(pcash):
    low = pcash.rolling(126).min()
    result = _safe_div(pcash - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low pcash
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_252d_base_v044_signal(pcash):
    low = pcash.rolling(252).min()
    result = _safe_div(pcash - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low pcash
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_504d_base_v045_signal(pcash):
    low = pcash.rolling(504).min()
    result = _safe_div(pcash - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high pcash
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_21d_base_v046_signal(pcash):
    high = pcash.rolling(21).max()
    result = _safe_div(high - pcash, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high pcash
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_63d_base_v047_signal(pcash):
    high = pcash.rolling(63).max()
    result = _safe_div(high - pcash, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high pcash
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_126d_base_v048_signal(pcash):
    high = pcash.rolling(126).max()
    result = _safe_div(high - pcash, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high pcash
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_252d_base_v049_signal(pcash):
    high = pcash.rolling(252).max()
    result = _safe_div(high - pcash, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high pcash
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_504d_base_v050_signal(pcash):
    high = pcash.rolling(504).max()
    result = _safe_div(high - pcash, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_mom_21d_base_v051_signal(pcash):
    m1 = _mean(pcash, 21)
    m2 = _mean(pcash, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_mom_63d_base_v052_signal(pcash):
    m1 = _mean(pcash, 63)
    m2 = _mean(pcash, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_mom_126d_base_v053_signal(pcash):
    m1 = _mean(pcash, 126)
    m2 = _mean(pcash, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_mom_252d_base_v054_signal(pcash):
    m1 = _mean(pcash, 252)
    m2 = _mean(pcash, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_mom_504d_base_v055_signal(pcash):
    m1 = _mean(pcash, 504)
    m2 = _mean(pcash, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_skew_21d_base_v056_signal(pcash):
    result = _skew(pcash, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_skew_63d_base_v057_signal(pcash):
    result = _skew(pcash, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_skew_126d_base_v058_signal(pcash):
    result = _skew(pcash, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_skew_252d_base_v059_signal(pcash):
    result = _skew(pcash, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_skew_504d_base_v060_signal(pcash):
    result = _skew(pcash, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_kurt_21d_base_v061_signal(pcash):
    result = _kurt(pcash, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_kurt_63d_base_v062_signal(pcash):
    result = _kurt(pcash, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_kurt_126d_base_v063_signal(pcash):
    result = _kurt(pcash, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_kurt_252d_base_v064_signal(pcash):
    result = _kurt(pcash, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_kurt_504d_base_v065_signal(pcash):
    result = _kurt(pcash, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_rank_21d_base_v066_signal(pcash, closeadj):
    result = _rank(pcash, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_rank_63d_base_v067_signal(pcash, closeadj):
    result = _rank(pcash, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_rank_126d_base_v068_signal(pcash, closeadj):
    result = _rank(pcash, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_rank_252d_base_v069_signal(pcash, closeadj):
    result = _rank(pcash, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_rank_504d_base_v070_signal(pcash, closeadj):
    result = _rank(pcash, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_autocorr_21d_base_v071_signal(pcash):
    result = _autocorr(pcash, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_autocorr_63d_base_v072_signal(pcash):
    result = _autocorr(pcash, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_autocorr_126d_base_v073_signal(pcash):
    result = _autocorr(pcash, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_autocorr_252d_base_v074_signal(pcash):
    result = _autocorr(pcash, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of pcash
def gm_f79_biotech_f79_price_to_cash_ratio_autocorr_504d_base_v075_signal(pcash):
    result = _autocorr(pcash, 504)
    return result.replace([np.inf, -np.inf], np.nan)

