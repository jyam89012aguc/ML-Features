
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_21d_base_v001_signal(debtc, closeadj):
    result = _mean(debtc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_63d_base_v002_signal(debtc, closeadj):
    result = _mean(debtc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_126d_base_v003_signal(debtc, closeadj):
    result = _mean(debtc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_252d_base_v004_signal(debtc, closeadj):
    result = _mean(debtc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_504d_base_v005_signal(debtc, closeadj):
    result = _mean(debtc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_21d_base_v006_signal(debtc, closeadj):
    result = _mean(_log(debtc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_63d_base_v007_signal(debtc, closeadj):
    result = _mean(_log(debtc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_126d_base_v008_signal(debtc, closeadj):
    result = _mean(_log(debtc), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_252d_base_v009_signal(debtc, closeadj):
    result = _mean(_log(debtc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_504d_base_v010_signal(debtc, closeadj):
    result = _mean(_log(debtc), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_21d_base_v011_signal(debtc):
    result = _z(debtc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_63d_base_v012_signal(debtc):
    result = _z(debtc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_126d_base_v013_signal(debtc):
    result = _z(debtc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_252d_base_v014_signal(debtc):
    result = _z(debtc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_504d_base_v015_signal(debtc):
    result = _z(debtc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_pct_21d_base_v016_signal(debtc):
    result = _pct_change(debtc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_pct_63d_base_v017_signal(debtc):
    result = _pct_change(debtc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_pct_126d_base_v018_signal(debtc):
    result = _pct_change(debtc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_pct_252d_base_v019_signal(debtc):
    result = _pct_change(debtc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_pct_504d_base_v020_signal(debtc):
    result = _pct_change(debtc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_21d_base_v021_signal(debtc, sharesbas, closeadj):
    ps = _safe_div(debtc, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_63d_base_v022_signal(debtc, sharesbas, closeadj):
    ps = _safe_div(debtc, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_126d_base_v023_signal(debtc, sharesbas, closeadj):
    ps = _safe_div(debtc, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_252d_base_v024_signal(debtc, sharesbas, closeadj):
    ps = _safe_div(debtc, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_504d_base_v025_signal(debtc, sharesbas, closeadj):
    ps = _safe_div(debtc, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of debtc to debt
def gm_f37_biotech_f37_short_term_debt_dominance_ratio_debt_21d_base_v026_signal(debtc, debt):
    ratio = _safe_div(debtc, debt)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of debtc to debt
def gm_f37_biotech_f37_short_term_debt_dominance_ratio_debt_63d_base_v027_signal(debtc, debt):
    ratio = _safe_div(debtc, debt)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of debtc to debt
def gm_f37_biotech_f37_short_term_debt_dominance_ratio_debt_126d_base_v028_signal(debtc, debt):
    ratio = _safe_div(debtc, debt)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of debtc to debt
def gm_f37_biotech_f37_short_term_debt_dominance_ratio_debt_252d_base_v029_signal(debtc, debt):
    ratio = _safe_div(debtc, debt)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of debtc to debt
def gm_f37_biotech_f37_short_term_debt_dominance_ratio_debt_504d_base_v030_signal(debtc, debt):
    ratio = _safe_div(debtc, debt)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d debtc scaled by assets
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_21d_base_v031_signal(debtc, assets):
    scaled = _safe_div(debtc, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d debtc scaled by assets
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_63d_base_v032_signal(debtc, assets):
    scaled = _safe_div(debtc, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d debtc scaled by assets
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_126d_base_v033_signal(debtc, assets):
    scaled = _safe_div(debtc, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d debtc scaled by assets
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_252d_base_v034_signal(debtc, assets):
    scaled = _safe_div(debtc, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d debtc scaled by assets
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_504d_base_v035_signal(debtc, assets):
    scaled = _safe_div(debtc, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d debtc scaled by marketcap
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_21d_base_v036_signal(debtc, marketcap):
    scaled = _safe_div(debtc, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d debtc scaled by marketcap
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_63d_base_v037_signal(debtc, marketcap):
    scaled = _safe_div(debtc, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d debtc scaled by marketcap
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_126d_base_v038_signal(debtc, marketcap):
    scaled = _safe_div(debtc, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d debtc scaled by marketcap
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_252d_base_v039_signal(debtc, marketcap):
    scaled = _safe_div(debtc, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d debtc scaled by marketcap
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_504d_base_v040_signal(debtc, marketcap):
    scaled = _safe_div(debtc, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_21d_base_v041_signal(debtc):
    low = debtc.rolling(21).min()
    result = _safe_div(debtc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_63d_base_v042_signal(debtc):
    low = debtc.rolling(63).min()
    result = _safe_div(debtc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_126d_base_v043_signal(debtc):
    low = debtc.rolling(126).min()
    result = _safe_div(debtc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_252d_base_v044_signal(debtc):
    low = debtc.rolling(252).min()
    result = _safe_div(debtc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_504d_base_v045_signal(debtc):
    low = debtc.rolling(504).min()
    result = _safe_div(debtc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_21d_base_v046_signal(debtc):
    high = debtc.rolling(21).max()
    result = _safe_div(high - debtc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_63d_base_v047_signal(debtc):
    high = debtc.rolling(63).max()
    result = _safe_div(high - debtc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_126d_base_v048_signal(debtc):
    high = debtc.rolling(126).max()
    result = _safe_div(high - debtc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_252d_base_v049_signal(debtc):
    high = debtc.rolling(252).max()
    result = _safe_div(high - debtc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_504d_base_v050_signal(debtc):
    high = debtc.rolling(504).max()
    result = _safe_div(high - debtc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_21d_base_v051_signal(debtc):
    m1 = _mean(debtc, 21)
    m2 = _mean(debtc, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_63d_base_v052_signal(debtc):
    m1 = _mean(debtc, 63)
    m2 = _mean(debtc, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_126d_base_v053_signal(debtc):
    m1 = _mean(debtc, 126)
    m2 = _mean(debtc, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_252d_base_v054_signal(debtc):
    m1 = _mean(debtc, 252)
    m2 = _mean(debtc, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_504d_base_v055_signal(debtc):
    m1 = _mean(debtc, 504)
    m2 = _mean(debtc, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_skew_21d_base_v056_signal(debtc):
    result = _skew(debtc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_skew_63d_base_v057_signal(debtc):
    result = _skew(debtc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_skew_126d_base_v058_signal(debtc):
    result = _skew(debtc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_skew_252d_base_v059_signal(debtc):
    result = _skew(debtc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_skew_504d_base_v060_signal(debtc):
    result = _skew(debtc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_kurt_21d_base_v061_signal(debtc):
    result = _kurt(debtc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_kurt_63d_base_v062_signal(debtc):
    result = _kurt(debtc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_kurt_126d_base_v063_signal(debtc):
    result = _kurt(debtc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_kurt_252d_base_v064_signal(debtc):
    result = _kurt(debtc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_kurt_504d_base_v065_signal(debtc):
    result = _kurt(debtc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_rank_21d_base_v066_signal(debtc, closeadj):
    result = _rank(debtc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_rank_63d_base_v067_signal(debtc, closeadj):
    result = _rank(debtc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_rank_126d_base_v068_signal(debtc, closeadj):
    result = _rank(debtc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_rank_252d_base_v069_signal(debtc, closeadj):
    result = _rank(debtc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_rank_504d_base_v070_signal(debtc, closeadj):
    result = _rank(debtc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_autocorr_21d_base_v071_signal(debtc):
    result = _autocorr(debtc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_autocorr_63d_base_v072_signal(debtc):
    result = _autocorr(debtc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_autocorr_126d_base_v073_signal(debtc):
    result = _autocorr(debtc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_autocorr_252d_base_v074_signal(debtc):
    result = _autocorr(debtc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of debtc
def gm_f37_biotech_f37_short_term_debt_dominance_autocorr_504d_base_v075_signal(debtc):
    result = _autocorr(debtc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

