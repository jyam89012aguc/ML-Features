
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed close
def gm_f97_biotech_f97_historical_volatility_regime_raw_21d_base_v001_signal(close, closeadj):
    result = _mean(close, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed close
def gm_f97_biotech_f97_historical_volatility_regime_raw_63d_base_v002_signal(close, closeadj):
    result = _mean(close, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed close
def gm_f97_biotech_f97_historical_volatility_regime_raw_126d_base_v003_signal(close, closeadj):
    result = _mean(close, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed close
def gm_f97_biotech_f97_historical_volatility_regime_raw_252d_base_v004_signal(close, closeadj):
    result = _mean(close, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed close
def gm_f97_biotech_f97_historical_volatility_regime_raw_504d_base_v005_signal(close, closeadj):
    result = _mean(close, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed close
def gm_f97_biotech_f97_historical_volatility_regime_log_21d_base_v006_signal(close, closeadj):
    result = _mean(_log(close), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed close
def gm_f97_biotech_f97_historical_volatility_regime_log_63d_base_v007_signal(close, closeadj):
    result = _mean(_log(close), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed close
def gm_f97_biotech_f97_historical_volatility_regime_log_126d_base_v008_signal(close, closeadj):
    result = _mean(_log(close), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed close
def gm_f97_biotech_f97_historical_volatility_regime_log_252d_base_v009_signal(close, closeadj):
    result = _mean(_log(close), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed close
def gm_f97_biotech_f97_historical_volatility_regime_log_504d_base_v010_signal(close, closeadj):
    result = _mean(_log(close), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of close
def gm_f97_biotech_f97_historical_volatility_regime_z_21d_base_v011_signal(close):
    result = _z(close, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of close
def gm_f97_biotech_f97_historical_volatility_regime_z_63d_base_v012_signal(close):
    result = _z(close, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of close
def gm_f97_biotech_f97_historical_volatility_regime_z_126d_base_v013_signal(close):
    result = _z(close, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of close
def gm_f97_biotech_f97_historical_volatility_regime_z_252d_base_v014_signal(close):
    result = _z(close, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of close
def gm_f97_biotech_f97_historical_volatility_regime_z_504d_base_v015_signal(close):
    result = _z(close, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of close
def gm_f97_biotech_f97_historical_volatility_regime_pct_21d_base_v016_signal(close):
    result = _pct_change(close, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of close
def gm_f97_biotech_f97_historical_volatility_regime_pct_63d_base_v017_signal(close):
    result = _pct_change(close, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of close
def gm_f97_biotech_f97_historical_volatility_regime_pct_126d_base_v018_signal(close):
    result = _pct_change(close, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of close
def gm_f97_biotech_f97_historical_volatility_regime_pct_252d_base_v019_signal(close):
    result = _pct_change(close, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of close
def gm_f97_biotech_f97_historical_volatility_regime_pct_504d_base_v020_signal(close):
    result = _pct_change(close, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share close
def gm_f97_biotech_f97_historical_volatility_regime_ps_21d_base_v021_signal(close, sharesbas, closeadj):
    ps = _safe_div(close, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share close
def gm_f97_biotech_f97_historical_volatility_regime_ps_63d_base_v022_signal(close, sharesbas, closeadj):
    ps = _safe_div(close, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share close
def gm_f97_biotech_f97_historical_volatility_regime_ps_126d_base_v023_signal(close, sharesbas, closeadj):
    ps = _safe_div(close, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share close
def gm_f97_biotech_f97_historical_volatility_regime_ps_252d_base_v024_signal(close, sharesbas, closeadj):
    ps = _safe_div(close, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share close
def gm_f97_biotech_f97_historical_volatility_regime_ps_504d_base_v025_signal(close, sharesbas, closeadj):
    ps = _safe_div(close, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d close scaled by assets
def gm_f97_biotech_f97_historical_volatility_regime_asset_scaled_21d_base_v026_signal(close, assets):
    scaled = _safe_div(close, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d close scaled by assets
def gm_f97_biotech_f97_historical_volatility_regime_asset_scaled_63d_base_v027_signal(close, assets):
    scaled = _safe_div(close, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d close scaled by assets
def gm_f97_biotech_f97_historical_volatility_regime_asset_scaled_126d_base_v028_signal(close, assets):
    scaled = _safe_div(close, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d close scaled by assets
def gm_f97_biotech_f97_historical_volatility_regime_asset_scaled_252d_base_v029_signal(close, assets):
    scaled = _safe_div(close, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d close scaled by assets
def gm_f97_biotech_f97_historical_volatility_regime_asset_scaled_504d_base_v030_signal(close, assets):
    scaled = _safe_div(close, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d close scaled by marketcap
def gm_f97_biotech_f97_historical_volatility_regime_mcap_scaled_21d_base_v031_signal(close, marketcap):
    scaled = _safe_div(close, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d close scaled by marketcap
def gm_f97_biotech_f97_historical_volatility_regime_mcap_scaled_63d_base_v032_signal(close, marketcap):
    scaled = _safe_div(close, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d close scaled by marketcap
def gm_f97_biotech_f97_historical_volatility_regime_mcap_scaled_126d_base_v033_signal(close, marketcap):
    scaled = _safe_div(close, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d close scaled by marketcap
def gm_f97_biotech_f97_historical_volatility_regime_mcap_scaled_252d_base_v034_signal(close, marketcap):
    scaled = _safe_div(close, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d close scaled by marketcap
def gm_f97_biotech_f97_historical_volatility_regime_mcap_scaled_504d_base_v035_signal(close, marketcap):
    scaled = _safe_div(close, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low close
def gm_f97_biotech_f97_historical_volatility_regime_dist_low_21d_base_v036_signal(close):
    low = close.rolling(21).min()
    result = _safe_div(close - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low close
def gm_f97_biotech_f97_historical_volatility_regime_dist_low_63d_base_v037_signal(close):
    low = close.rolling(63).min()
    result = _safe_div(close - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low close
def gm_f97_biotech_f97_historical_volatility_regime_dist_low_126d_base_v038_signal(close):
    low = close.rolling(126).min()
    result = _safe_div(close - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low close
def gm_f97_biotech_f97_historical_volatility_regime_dist_low_252d_base_v039_signal(close):
    low = close.rolling(252).min()
    result = _safe_div(close - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low close
def gm_f97_biotech_f97_historical_volatility_regime_dist_low_504d_base_v040_signal(close):
    low = close.rolling(504).min()
    result = _safe_div(close - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high close
def gm_f97_biotech_f97_historical_volatility_regime_dist_high_21d_base_v041_signal(close):
    high = close.rolling(21).max()
    result = _safe_div(high - close, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high close
def gm_f97_biotech_f97_historical_volatility_regime_dist_high_63d_base_v042_signal(close):
    high = close.rolling(63).max()
    result = _safe_div(high - close, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high close
def gm_f97_biotech_f97_historical_volatility_regime_dist_high_126d_base_v043_signal(close):
    high = close.rolling(126).max()
    result = _safe_div(high - close, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high close
def gm_f97_biotech_f97_historical_volatility_regime_dist_high_252d_base_v044_signal(close):
    high = close.rolling(252).max()
    result = _safe_div(high - close, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high close
def gm_f97_biotech_f97_historical_volatility_regime_dist_high_504d_base_v045_signal(close):
    high = close.rolling(504).max()
    result = _safe_div(high - close, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of close
def gm_f97_biotech_f97_historical_volatility_regime_mom_21d_base_v046_signal(close):
    m1 = _mean(close, 21)
    m2 = _mean(close, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of close
def gm_f97_biotech_f97_historical_volatility_regime_mom_63d_base_v047_signal(close):
    m1 = _mean(close, 63)
    m2 = _mean(close, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of close
def gm_f97_biotech_f97_historical_volatility_regime_mom_126d_base_v048_signal(close):
    m1 = _mean(close, 126)
    m2 = _mean(close, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of close
def gm_f97_biotech_f97_historical_volatility_regime_mom_252d_base_v049_signal(close):
    m1 = _mean(close, 252)
    m2 = _mean(close, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of close
def gm_f97_biotech_f97_historical_volatility_regime_mom_504d_base_v050_signal(close):
    m1 = _mean(close, 504)
    m2 = _mean(close, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of close
def gm_f97_biotech_f97_historical_volatility_regime_skew_21d_base_v051_signal(close):
    result = _skew(close, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of close
def gm_f97_biotech_f97_historical_volatility_regime_skew_63d_base_v052_signal(close):
    result = _skew(close, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of close
def gm_f97_biotech_f97_historical_volatility_regime_skew_126d_base_v053_signal(close):
    result = _skew(close, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of close
def gm_f97_biotech_f97_historical_volatility_regime_skew_252d_base_v054_signal(close):
    result = _skew(close, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of close
def gm_f97_biotech_f97_historical_volatility_regime_skew_504d_base_v055_signal(close):
    result = _skew(close, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of close
def gm_f97_biotech_f97_historical_volatility_regime_kurt_21d_base_v056_signal(close):
    result = _kurt(close, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of close
def gm_f97_biotech_f97_historical_volatility_regime_kurt_63d_base_v057_signal(close):
    result = _kurt(close, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of close
def gm_f97_biotech_f97_historical_volatility_regime_kurt_126d_base_v058_signal(close):
    result = _kurt(close, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of close
def gm_f97_biotech_f97_historical_volatility_regime_kurt_252d_base_v059_signal(close):
    result = _kurt(close, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of close
def gm_f97_biotech_f97_historical_volatility_regime_kurt_504d_base_v060_signal(close):
    result = _kurt(close, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of close
def gm_f97_biotech_f97_historical_volatility_regime_rank_21d_base_v061_signal(close, closeadj):
    result = _rank(close, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of close
def gm_f97_biotech_f97_historical_volatility_regime_rank_63d_base_v062_signal(close, closeadj):
    result = _rank(close, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of close
def gm_f97_biotech_f97_historical_volatility_regime_rank_126d_base_v063_signal(close, closeadj):
    result = _rank(close, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of close
def gm_f97_biotech_f97_historical_volatility_regime_rank_252d_base_v064_signal(close, closeadj):
    result = _rank(close, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of close
def gm_f97_biotech_f97_historical_volatility_regime_rank_504d_base_v065_signal(close, closeadj):
    result = _rank(close, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of close
def gm_f97_biotech_f97_historical_volatility_regime_autocorr_21d_base_v066_signal(close):
    result = _autocorr(close, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of close
def gm_f97_biotech_f97_historical_volatility_regime_autocorr_63d_base_v067_signal(close):
    result = _autocorr(close, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of close
def gm_f97_biotech_f97_historical_volatility_regime_autocorr_126d_base_v068_signal(close):
    result = _autocorr(close, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of close
def gm_f97_biotech_f97_historical_volatility_regime_autocorr_252d_base_v069_signal(close):
    result = _autocorr(close, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of close
def gm_f97_biotech_f97_historical_volatility_regime_autocorr_504d_base_v070_signal(close):
    result = _autocorr(close, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of close
def gm_f97_biotech_f97_historical_volatility_regime_std_21d_base_v071_signal(close, closeadj):
    result = _std(close, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of close
def gm_f97_biotech_f97_historical_volatility_regime_std_63d_base_v072_signal(close, closeadj):
    result = _std(close, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of close
def gm_f97_biotech_f97_historical_volatility_regime_std_126d_base_v073_signal(close, closeadj):
    result = _std(close, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of close
def gm_f97_biotech_f97_historical_volatility_regime_std_252d_base_v074_signal(close, closeadj):
    result = _std(close, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of close
def gm_f97_biotech_f97_historical_volatility_regime_std_504d_base_v075_signal(close, closeadj):
    result = _std(close, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

