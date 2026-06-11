
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed roe
def gm_f53_biotech_f53_return_on_equity_profitability_raw_21d_base_v001_signal(roe, closeadj):
    result = _mean(roe, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed roe
def gm_f53_biotech_f53_return_on_equity_profitability_raw_63d_base_v002_signal(roe, closeadj):
    result = _mean(roe, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed roe
def gm_f53_biotech_f53_return_on_equity_profitability_raw_126d_base_v003_signal(roe, closeadj):
    result = _mean(roe, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed roe
def gm_f53_biotech_f53_return_on_equity_profitability_raw_252d_base_v004_signal(roe, closeadj):
    result = _mean(roe, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed roe
def gm_f53_biotech_f53_return_on_equity_profitability_raw_504d_base_v005_signal(roe, closeadj):
    result = _mean(roe, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed roe
def gm_f53_biotech_f53_return_on_equity_profitability_log_21d_base_v006_signal(roe, closeadj):
    result = _mean(_log(roe), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed roe
def gm_f53_biotech_f53_return_on_equity_profitability_log_63d_base_v007_signal(roe, closeadj):
    result = _mean(_log(roe), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed roe
def gm_f53_biotech_f53_return_on_equity_profitability_log_126d_base_v008_signal(roe, closeadj):
    result = _mean(_log(roe), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed roe
def gm_f53_biotech_f53_return_on_equity_profitability_log_252d_base_v009_signal(roe, closeadj):
    result = _mean(_log(roe), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed roe
def gm_f53_biotech_f53_return_on_equity_profitability_log_504d_base_v010_signal(roe, closeadj):
    result = _mean(_log(roe), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of roe
def gm_f53_biotech_f53_return_on_equity_profitability_z_21d_base_v011_signal(roe):
    result = _z(roe, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roe
def gm_f53_biotech_f53_return_on_equity_profitability_z_63d_base_v012_signal(roe):
    result = _z(roe, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roe
def gm_f53_biotech_f53_return_on_equity_profitability_z_126d_base_v013_signal(roe):
    result = _z(roe, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roe
def gm_f53_biotech_f53_return_on_equity_profitability_z_252d_base_v014_signal(roe):
    result = _z(roe, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roe
def gm_f53_biotech_f53_return_on_equity_profitability_z_504d_base_v015_signal(roe):
    result = _z(roe, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of roe
def gm_f53_biotech_f53_return_on_equity_profitability_pct_21d_base_v016_signal(roe):
    result = _pct_change(roe, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of roe
def gm_f53_biotech_f53_return_on_equity_profitability_pct_63d_base_v017_signal(roe):
    result = _pct_change(roe, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of roe
def gm_f53_biotech_f53_return_on_equity_profitability_pct_126d_base_v018_signal(roe):
    result = _pct_change(roe, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of roe
def gm_f53_biotech_f53_return_on_equity_profitability_pct_252d_base_v019_signal(roe):
    result = _pct_change(roe, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of roe
def gm_f53_biotech_f53_return_on_equity_profitability_pct_504d_base_v020_signal(roe):
    result = _pct_change(roe, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share roe
def gm_f53_biotech_f53_return_on_equity_profitability_ps_21d_base_v021_signal(roe, sharesbas, closeadj):
    ps = _safe_div(roe, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share roe
def gm_f53_biotech_f53_return_on_equity_profitability_ps_63d_base_v022_signal(roe, sharesbas, closeadj):
    ps = _safe_div(roe, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share roe
def gm_f53_biotech_f53_return_on_equity_profitability_ps_126d_base_v023_signal(roe, sharesbas, closeadj):
    ps = _safe_div(roe, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share roe
def gm_f53_biotech_f53_return_on_equity_profitability_ps_252d_base_v024_signal(roe, sharesbas, closeadj):
    ps = _safe_div(roe, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share roe
def gm_f53_biotech_f53_return_on_equity_profitability_ps_504d_base_v025_signal(roe, sharesbas, closeadj):
    ps = _safe_div(roe, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of roe to equity
def gm_f53_biotech_f53_return_on_equity_profitability_ratio_equity_21d_base_v026_signal(roe, equity):
    ratio = _safe_div(roe, equity)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of roe to equity
def gm_f53_biotech_f53_return_on_equity_profitability_ratio_equity_63d_base_v027_signal(roe, equity):
    ratio = _safe_div(roe, equity)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of roe to equity
def gm_f53_biotech_f53_return_on_equity_profitability_ratio_equity_126d_base_v028_signal(roe, equity):
    ratio = _safe_div(roe, equity)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of roe to equity
def gm_f53_biotech_f53_return_on_equity_profitability_ratio_equity_252d_base_v029_signal(roe, equity):
    ratio = _safe_div(roe, equity)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of roe to equity
def gm_f53_biotech_f53_return_on_equity_profitability_ratio_equity_504d_base_v030_signal(roe, equity):
    ratio = _safe_div(roe, equity)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d roe scaled by assets
def gm_f53_biotech_f53_return_on_equity_profitability_asset_scaled_21d_base_v031_signal(roe, assets):
    scaled = _safe_div(roe, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d roe scaled by assets
def gm_f53_biotech_f53_return_on_equity_profitability_asset_scaled_63d_base_v032_signal(roe, assets):
    scaled = _safe_div(roe, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d roe scaled by assets
def gm_f53_biotech_f53_return_on_equity_profitability_asset_scaled_126d_base_v033_signal(roe, assets):
    scaled = _safe_div(roe, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d roe scaled by assets
def gm_f53_biotech_f53_return_on_equity_profitability_asset_scaled_252d_base_v034_signal(roe, assets):
    scaled = _safe_div(roe, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d roe scaled by assets
def gm_f53_biotech_f53_return_on_equity_profitability_asset_scaled_504d_base_v035_signal(roe, assets):
    scaled = _safe_div(roe, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d roe scaled by marketcap
def gm_f53_biotech_f53_return_on_equity_profitability_mcap_scaled_21d_base_v036_signal(roe, marketcap):
    scaled = _safe_div(roe, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d roe scaled by marketcap
def gm_f53_biotech_f53_return_on_equity_profitability_mcap_scaled_63d_base_v037_signal(roe, marketcap):
    scaled = _safe_div(roe, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d roe scaled by marketcap
def gm_f53_biotech_f53_return_on_equity_profitability_mcap_scaled_126d_base_v038_signal(roe, marketcap):
    scaled = _safe_div(roe, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d roe scaled by marketcap
def gm_f53_biotech_f53_return_on_equity_profitability_mcap_scaled_252d_base_v039_signal(roe, marketcap):
    scaled = _safe_div(roe, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d roe scaled by marketcap
def gm_f53_biotech_f53_return_on_equity_profitability_mcap_scaled_504d_base_v040_signal(roe, marketcap):
    scaled = _safe_div(roe, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low roe
def gm_f53_biotech_f53_return_on_equity_profitability_dist_low_21d_base_v041_signal(roe):
    low = roe.rolling(21).min()
    result = _safe_div(roe - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low roe
def gm_f53_biotech_f53_return_on_equity_profitability_dist_low_63d_base_v042_signal(roe):
    low = roe.rolling(63).min()
    result = _safe_div(roe - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low roe
def gm_f53_biotech_f53_return_on_equity_profitability_dist_low_126d_base_v043_signal(roe):
    low = roe.rolling(126).min()
    result = _safe_div(roe - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low roe
def gm_f53_biotech_f53_return_on_equity_profitability_dist_low_252d_base_v044_signal(roe):
    low = roe.rolling(252).min()
    result = _safe_div(roe - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low roe
def gm_f53_biotech_f53_return_on_equity_profitability_dist_low_504d_base_v045_signal(roe):
    low = roe.rolling(504).min()
    result = _safe_div(roe - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high roe
def gm_f53_biotech_f53_return_on_equity_profitability_dist_high_21d_base_v046_signal(roe):
    high = roe.rolling(21).max()
    result = _safe_div(high - roe, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high roe
def gm_f53_biotech_f53_return_on_equity_profitability_dist_high_63d_base_v047_signal(roe):
    high = roe.rolling(63).max()
    result = _safe_div(high - roe, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high roe
def gm_f53_biotech_f53_return_on_equity_profitability_dist_high_126d_base_v048_signal(roe):
    high = roe.rolling(126).max()
    result = _safe_div(high - roe, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high roe
def gm_f53_biotech_f53_return_on_equity_profitability_dist_high_252d_base_v049_signal(roe):
    high = roe.rolling(252).max()
    result = _safe_div(high - roe, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high roe
def gm_f53_biotech_f53_return_on_equity_profitability_dist_high_504d_base_v050_signal(roe):
    high = roe.rolling(504).max()
    result = _safe_div(high - roe, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of roe
def gm_f53_biotech_f53_return_on_equity_profitability_mom_21d_base_v051_signal(roe):
    m1 = _mean(roe, 21)
    m2 = _mean(roe, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of roe
def gm_f53_biotech_f53_return_on_equity_profitability_mom_63d_base_v052_signal(roe):
    m1 = _mean(roe, 63)
    m2 = _mean(roe, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of roe
def gm_f53_biotech_f53_return_on_equity_profitability_mom_126d_base_v053_signal(roe):
    m1 = _mean(roe, 126)
    m2 = _mean(roe, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of roe
def gm_f53_biotech_f53_return_on_equity_profitability_mom_252d_base_v054_signal(roe):
    m1 = _mean(roe, 252)
    m2 = _mean(roe, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of roe
def gm_f53_biotech_f53_return_on_equity_profitability_mom_504d_base_v055_signal(roe):
    m1 = _mean(roe, 504)
    m2 = _mean(roe, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of roe
def gm_f53_biotech_f53_return_on_equity_profitability_skew_21d_base_v056_signal(roe):
    result = _skew(roe, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of roe
def gm_f53_biotech_f53_return_on_equity_profitability_skew_63d_base_v057_signal(roe):
    result = _skew(roe, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of roe
def gm_f53_biotech_f53_return_on_equity_profitability_skew_126d_base_v058_signal(roe):
    result = _skew(roe, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of roe
def gm_f53_biotech_f53_return_on_equity_profitability_skew_252d_base_v059_signal(roe):
    result = _skew(roe, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of roe
def gm_f53_biotech_f53_return_on_equity_profitability_skew_504d_base_v060_signal(roe):
    result = _skew(roe, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of roe
def gm_f53_biotech_f53_return_on_equity_profitability_kurt_21d_base_v061_signal(roe):
    result = _kurt(roe, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of roe
def gm_f53_biotech_f53_return_on_equity_profitability_kurt_63d_base_v062_signal(roe):
    result = _kurt(roe, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of roe
def gm_f53_biotech_f53_return_on_equity_profitability_kurt_126d_base_v063_signal(roe):
    result = _kurt(roe, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of roe
def gm_f53_biotech_f53_return_on_equity_profitability_kurt_252d_base_v064_signal(roe):
    result = _kurt(roe, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of roe
def gm_f53_biotech_f53_return_on_equity_profitability_kurt_504d_base_v065_signal(roe):
    result = _kurt(roe, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of roe
def gm_f53_biotech_f53_return_on_equity_profitability_rank_21d_base_v066_signal(roe, closeadj):
    result = _rank(roe, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of roe
def gm_f53_biotech_f53_return_on_equity_profitability_rank_63d_base_v067_signal(roe, closeadj):
    result = _rank(roe, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of roe
def gm_f53_biotech_f53_return_on_equity_profitability_rank_126d_base_v068_signal(roe, closeadj):
    result = _rank(roe, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of roe
def gm_f53_biotech_f53_return_on_equity_profitability_rank_252d_base_v069_signal(roe, closeadj):
    result = _rank(roe, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of roe
def gm_f53_biotech_f53_return_on_equity_profitability_rank_504d_base_v070_signal(roe, closeadj):
    result = _rank(roe, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of roe
def gm_f53_biotech_f53_return_on_equity_profitability_autocorr_21d_base_v071_signal(roe):
    result = _autocorr(roe, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of roe
def gm_f53_biotech_f53_return_on_equity_profitability_autocorr_63d_base_v072_signal(roe):
    result = _autocorr(roe, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of roe
def gm_f53_biotech_f53_return_on_equity_profitability_autocorr_126d_base_v073_signal(roe):
    result = _autocorr(roe, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of roe
def gm_f53_biotech_f53_return_on_equity_profitability_autocorr_252d_base_v074_signal(roe):
    result = _autocorr(roe, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of roe
def gm_f53_biotech_f53_return_on_equity_profitability_autocorr_504d_base_v075_signal(roe):
    result = _autocorr(roe, 504)
    return result.replace([np.inf, -np.inf], np.nan)

