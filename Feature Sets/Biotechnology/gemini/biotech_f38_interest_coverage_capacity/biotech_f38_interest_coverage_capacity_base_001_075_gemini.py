
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_21d_base_v001_signal(ebit, closeadj):
    result = _mean(ebit, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_63d_base_v002_signal(ebit, closeadj):
    result = _mean(ebit, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_126d_base_v003_signal(ebit, closeadj):
    result = _mean(ebit, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_252d_base_v004_signal(ebit, closeadj):
    result = _mean(ebit, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_504d_base_v005_signal(ebit, closeadj):
    result = _mean(ebit, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_21d_base_v006_signal(ebit, closeadj):
    result = _mean(_log(ebit), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_63d_base_v007_signal(ebit, closeadj):
    result = _mean(_log(ebit), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_126d_base_v008_signal(ebit, closeadj):
    result = _mean(_log(ebit), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_252d_base_v009_signal(ebit, closeadj):
    result = _mean(_log(ebit), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_504d_base_v010_signal(ebit, closeadj):
    result = _mean(_log(ebit), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_21d_base_v011_signal(ebit):
    result = _z(ebit, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_63d_base_v012_signal(ebit):
    result = _z(ebit, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_126d_base_v013_signal(ebit):
    result = _z(ebit, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_252d_base_v014_signal(ebit):
    result = _z(ebit, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_504d_base_v015_signal(ebit):
    result = _z(ebit, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_pct_21d_base_v016_signal(ebit):
    result = _pct_change(ebit, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_pct_63d_base_v017_signal(ebit):
    result = _pct_change(ebit, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_pct_126d_base_v018_signal(ebit):
    result = _pct_change(ebit, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_pct_252d_base_v019_signal(ebit):
    result = _pct_change(ebit, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_pct_504d_base_v020_signal(ebit):
    result = _pct_change(ebit, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_21d_base_v021_signal(ebit, sharesbas, closeadj):
    ps = _safe_div(ebit, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_63d_base_v022_signal(ebit, sharesbas, closeadj):
    ps = _safe_div(ebit, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_126d_base_v023_signal(ebit, sharesbas, closeadj):
    ps = _safe_div(ebit, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_252d_base_v024_signal(ebit, sharesbas, closeadj):
    ps = _safe_div(ebit, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_504d_base_v025_signal(ebit, sharesbas, closeadj):
    ps = _safe_div(ebit, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of ebit to intexp
def gm_f38_biotech_f38_interest_coverage_capacity_ratio_intexp_21d_base_v026_signal(ebit, intexp):
    ratio = _safe_div(ebit, intexp)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of ebit to intexp
def gm_f38_biotech_f38_interest_coverage_capacity_ratio_intexp_63d_base_v027_signal(ebit, intexp):
    ratio = _safe_div(ebit, intexp)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of ebit to intexp
def gm_f38_biotech_f38_interest_coverage_capacity_ratio_intexp_126d_base_v028_signal(ebit, intexp):
    ratio = _safe_div(ebit, intexp)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of ebit to intexp
def gm_f38_biotech_f38_interest_coverage_capacity_ratio_intexp_252d_base_v029_signal(ebit, intexp):
    ratio = _safe_div(ebit, intexp)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of ebit to intexp
def gm_f38_biotech_f38_interest_coverage_capacity_ratio_intexp_504d_base_v030_signal(ebit, intexp):
    ratio = _safe_div(ebit, intexp)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ebit scaled by assets
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_21d_base_v031_signal(ebit, assets):
    scaled = _safe_div(ebit, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ebit scaled by assets
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_63d_base_v032_signal(ebit, assets):
    scaled = _safe_div(ebit, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ebit scaled by assets
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_126d_base_v033_signal(ebit, assets):
    scaled = _safe_div(ebit, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ebit scaled by assets
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_252d_base_v034_signal(ebit, assets):
    scaled = _safe_div(ebit, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ebit scaled by assets
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_504d_base_v035_signal(ebit, assets):
    scaled = _safe_div(ebit, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ebit scaled by marketcap
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_21d_base_v036_signal(ebit, marketcap):
    scaled = _safe_div(ebit, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ebit scaled by marketcap
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_63d_base_v037_signal(ebit, marketcap):
    scaled = _safe_div(ebit, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ebit scaled by marketcap
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_126d_base_v038_signal(ebit, marketcap):
    scaled = _safe_div(ebit, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ebit scaled by marketcap
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_252d_base_v039_signal(ebit, marketcap):
    scaled = _safe_div(ebit, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ebit scaled by marketcap
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_504d_base_v040_signal(ebit, marketcap):
    scaled = _safe_div(ebit, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_21d_base_v041_signal(ebit):
    low = ebit.rolling(21).min()
    result = _safe_div(ebit - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_63d_base_v042_signal(ebit):
    low = ebit.rolling(63).min()
    result = _safe_div(ebit - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_126d_base_v043_signal(ebit):
    low = ebit.rolling(126).min()
    result = _safe_div(ebit - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_252d_base_v044_signal(ebit):
    low = ebit.rolling(252).min()
    result = _safe_div(ebit - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_504d_base_v045_signal(ebit):
    low = ebit.rolling(504).min()
    result = _safe_div(ebit - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_21d_base_v046_signal(ebit):
    high = ebit.rolling(21).max()
    result = _safe_div(high - ebit, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_63d_base_v047_signal(ebit):
    high = ebit.rolling(63).max()
    result = _safe_div(high - ebit, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_126d_base_v048_signal(ebit):
    high = ebit.rolling(126).max()
    result = _safe_div(high - ebit, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_252d_base_v049_signal(ebit):
    high = ebit.rolling(252).max()
    result = _safe_div(high - ebit, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_504d_base_v050_signal(ebit):
    high = ebit.rolling(504).max()
    result = _safe_div(high - ebit, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_21d_base_v051_signal(ebit):
    m1 = _mean(ebit, 21)
    m2 = _mean(ebit, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_63d_base_v052_signal(ebit):
    m1 = _mean(ebit, 63)
    m2 = _mean(ebit, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_126d_base_v053_signal(ebit):
    m1 = _mean(ebit, 126)
    m2 = _mean(ebit, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_252d_base_v054_signal(ebit):
    m1 = _mean(ebit, 252)
    m2 = _mean(ebit, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_504d_base_v055_signal(ebit):
    m1 = _mean(ebit, 504)
    m2 = _mean(ebit, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_skew_21d_base_v056_signal(ebit):
    result = _skew(ebit, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_skew_63d_base_v057_signal(ebit):
    result = _skew(ebit, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_skew_126d_base_v058_signal(ebit):
    result = _skew(ebit, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_skew_252d_base_v059_signal(ebit):
    result = _skew(ebit, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_skew_504d_base_v060_signal(ebit):
    result = _skew(ebit, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_kurt_21d_base_v061_signal(ebit):
    result = _kurt(ebit, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_kurt_63d_base_v062_signal(ebit):
    result = _kurt(ebit, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_kurt_126d_base_v063_signal(ebit):
    result = _kurt(ebit, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_kurt_252d_base_v064_signal(ebit):
    result = _kurt(ebit, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_kurt_504d_base_v065_signal(ebit):
    result = _kurt(ebit, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_rank_21d_base_v066_signal(ebit, closeadj):
    result = _rank(ebit, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_rank_63d_base_v067_signal(ebit, closeadj):
    result = _rank(ebit, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_rank_126d_base_v068_signal(ebit, closeadj):
    result = _rank(ebit, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_rank_252d_base_v069_signal(ebit, closeadj):
    result = _rank(ebit, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_rank_504d_base_v070_signal(ebit, closeadj):
    result = _rank(ebit, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_autocorr_21d_base_v071_signal(ebit):
    result = _autocorr(ebit, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_autocorr_63d_base_v072_signal(ebit):
    result = _autocorr(ebit, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_autocorr_126d_base_v073_signal(ebit):
    result = _autocorr(ebit, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_autocorr_252d_base_v074_signal(ebit):
    result = _autocorr(ebit, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of ebit
def gm_f38_biotech_f38_interest_coverage_capacity_autocorr_504d_base_v075_signal(ebit):
    result = _autocorr(ebit, 504)
    return result.replace([np.inf, -np.inf], np.nan)

