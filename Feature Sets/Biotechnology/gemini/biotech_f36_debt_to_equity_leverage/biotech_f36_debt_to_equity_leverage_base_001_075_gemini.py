
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_21d_base_v001_signal(deratio, closeadj):
    result = _mean(deratio, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_63d_base_v002_signal(deratio, closeadj):
    result = _mean(deratio, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_126d_base_v003_signal(deratio, closeadj):
    result = _mean(deratio, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_252d_base_v004_signal(deratio, closeadj):
    result = _mean(deratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_504d_base_v005_signal(deratio, closeadj):
    result = _mean(deratio, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_log_21d_base_v006_signal(deratio, closeadj):
    result = _mean(_log(deratio), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_log_63d_base_v007_signal(deratio, closeadj):
    result = _mean(_log(deratio), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_log_126d_base_v008_signal(deratio, closeadj):
    result = _mean(_log(deratio), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_log_252d_base_v009_signal(deratio, closeadj):
    result = _mean(_log(deratio), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_log_504d_base_v010_signal(deratio, closeadj):
    result = _mean(_log(deratio), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_z_21d_base_v011_signal(deratio):
    result = _z(deratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_z_63d_base_v012_signal(deratio):
    result = _z(deratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_z_126d_base_v013_signal(deratio):
    result = _z(deratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_z_252d_base_v014_signal(deratio):
    result = _z(deratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_z_504d_base_v015_signal(deratio):
    result = _z(deratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_pct_21d_base_v016_signal(deratio):
    result = _pct_change(deratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_pct_63d_base_v017_signal(deratio):
    result = _pct_change(deratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_pct_126d_base_v018_signal(deratio):
    result = _pct_change(deratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_pct_252d_base_v019_signal(deratio):
    result = _pct_change(deratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_pct_504d_base_v020_signal(deratio):
    result = _pct_change(deratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_21d_base_v021_signal(deratio, sharesbas, closeadj):
    ps = _safe_div(deratio, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_63d_base_v022_signal(deratio, sharesbas, closeadj):
    ps = _safe_div(deratio, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_126d_base_v023_signal(deratio, sharesbas, closeadj):
    ps = _safe_div(deratio, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_252d_base_v024_signal(deratio, sharesbas, closeadj):
    ps = _safe_div(deratio, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_504d_base_v025_signal(deratio, sharesbas, closeadj):
    ps = _safe_div(deratio, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of deratio to equity
def gm_f36_biotech_f36_debt_to_equity_leverage_ratio_equity_21d_base_v026_signal(deratio, equity):
    ratio = _safe_div(deratio, equity)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of deratio to equity
def gm_f36_biotech_f36_debt_to_equity_leverage_ratio_equity_63d_base_v027_signal(deratio, equity):
    ratio = _safe_div(deratio, equity)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of deratio to equity
def gm_f36_biotech_f36_debt_to_equity_leverage_ratio_equity_126d_base_v028_signal(deratio, equity):
    ratio = _safe_div(deratio, equity)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of deratio to equity
def gm_f36_biotech_f36_debt_to_equity_leverage_ratio_equity_252d_base_v029_signal(deratio, equity):
    ratio = _safe_div(deratio, equity)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of deratio to equity
def gm_f36_biotech_f36_debt_to_equity_leverage_ratio_equity_504d_base_v030_signal(deratio, equity):
    ratio = _safe_div(deratio, equity)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d deratio scaled by assets
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_21d_base_v031_signal(deratio, assets):
    scaled = _safe_div(deratio, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d deratio scaled by assets
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_63d_base_v032_signal(deratio, assets):
    scaled = _safe_div(deratio, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d deratio scaled by assets
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_126d_base_v033_signal(deratio, assets):
    scaled = _safe_div(deratio, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d deratio scaled by assets
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_252d_base_v034_signal(deratio, assets):
    scaled = _safe_div(deratio, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d deratio scaled by assets
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_504d_base_v035_signal(deratio, assets):
    scaled = _safe_div(deratio, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d deratio scaled by marketcap
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_21d_base_v036_signal(deratio, marketcap):
    scaled = _safe_div(deratio, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d deratio scaled by marketcap
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_63d_base_v037_signal(deratio, marketcap):
    scaled = _safe_div(deratio, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d deratio scaled by marketcap
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_126d_base_v038_signal(deratio, marketcap):
    scaled = _safe_div(deratio, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d deratio scaled by marketcap
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_252d_base_v039_signal(deratio, marketcap):
    scaled = _safe_div(deratio, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d deratio scaled by marketcap
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_504d_base_v040_signal(deratio, marketcap):
    scaled = _safe_div(deratio, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_21d_base_v041_signal(deratio):
    low = deratio.rolling(21).min()
    result = _safe_div(deratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_63d_base_v042_signal(deratio):
    low = deratio.rolling(63).min()
    result = _safe_div(deratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_126d_base_v043_signal(deratio):
    low = deratio.rolling(126).min()
    result = _safe_div(deratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_252d_base_v044_signal(deratio):
    low = deratio.rolling(252).min()
    result = _safe_div(deratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_504d_base_v045_signal(deratio):
    low = deratio.rolling(504).min()
    result = _safe_div(deratio - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_21d_base_v046_signal(deratio):
    high = deratio.rolling(21).max()
    result = _safe_div(high - deratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_63d_base_v047_signal(deratio):
    high = deratio.rolling(63).max()
    result = _safe_div(high - deratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_126d_base_v048_signal(deratio):
    high = deratio.rolling(126).max()
    result = _safe_div(high - deratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_252d_base_v049_signal(deratio):
    high = deratio.rolling(252).max()
    result = _safe_div(high - deratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_504d_base_v050_signal(deratio):
    high = deratio.rolling(504).max()
    result = _safe_div(high - deratio, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_21d_base_v051_signal(deratio):
    m1 = _mean(deratio, 21)
    m2 = _mean(deratio, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_63d_base_v052_signal(deratio):
    m1 = _mean(deratio, 63)
    m2 = _mean(deratio, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_126d_base_v053_signal(deratio):
    m1 = _mean(deratio, 126)
    m2 = _mean(deratio, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_252d_base_v054_signal(deratio):
    m1 = _mean(deratio, 252)
    m2 = _mean(deratio, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_504d_base_v055_signal(deratio):
    m1 = _mean(deratio, 504)
    m2 = _mean(deratio, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_skew_21d_base_v056_signal(deratio):
    result = _skew(deratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_skew_63d_base_v057_signal(deratio):
    result = _skew(deratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_skew_126d_base_v058_signal(deratio):
    result = _skew(deratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_skew_252d_base_v059_signal(deratio):
    result = _skew(deratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_skew_504d_base_v060_signal(deratio):
    result = _skew(deratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_kurt_21d_base_v061_signal(deratio):
    result = _kurt(deratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_kurt_63d_base_v062_signal(deratio):
    result = _kurt(deratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_kurt_126d_base_v063_signal(deratio):
    result = _kurt(deratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_kurt_252d_base_v064_signal(deratio):
    result = _kurt(deratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_kurt_504d_base_v065_signal(deratio):
    result = _kurt(deratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_rank_21d_base_v066_signal(deratio, closeadj):
    result = _rank(deratio, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_rank_63d_base_v067_signal(deratio, closeadj):
    result = _rank(deratio, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_rank_126d_base_v068_signal(deratio, closeadj):
    result = _rank(deratio, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_rank_252d_base_v069_signal(deratio, closeadj):
    result = _rank(deratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_rank_504d_base_v070_signal(deratio, closeadj):
    result = _rank(deratio, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_autocorr_21d_base_v071_signal(deratio):
    result = _autocorr(deratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_autocorr_63d_base_v072_signal(deratio):
    result = _autocorr(deratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_autocorr_126d_base_v073_signal(deratio):
    result = _autocorr(deratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_autocorr_252d_base_v074_signal(deratio):
    result = _autocorr(deratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of deratio
def gm_f36_biotech_f36_debt_to_equity_leverage_autocorr_504d_base_v075_signal(deratio):
    result = _autocorr(deratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

