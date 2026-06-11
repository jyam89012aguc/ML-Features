
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_raw_21d_base_v001_signal(runway, closeadj):
    result = _mean(runway, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_raw_63d_base_v002_signal(runway, closeadj):
    result = _mean(runway, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_raw_126d_base_v003_signal(runway, closeadj):
    result = _mean(runway, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_raw_252d_base_v004_signal(runway, closeadj):
    result = _mean(runway, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_raw_504d_base_v005_signal(runway, closeadj):
    result = _mean(runway, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_log_21d_base_v006_signal(runway, closeadj):
    result = _mean(_log(runway), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_log_63d_base_v007_signal(runway, closeadj):
    result = _mean(_log(runway), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_log_126d_base_v008_signal(runway, closeadj):
    result = _mean(_log(runway), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_log_252d_base_v009_signal(runway, closeadj):
    result = _mean(_log(runway), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_log_504d_base_v010_signal(runway, closeadj):
    result = _mean(_log(runway), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_z_21d_base_v011_signal(runway):
    result = _z(runway, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_z_63d_base_v012_signal(runway):
    result = _z(runway, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_z_126d_base_v013_signal(runway):
    result = _z(runway, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_z_252d_base_v014_signal(runway):
    result = _z(runway, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_z_504d_base_v015_signal(runway):
    result = _z(runway, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_pct_21d_base_v016_signal(runway):
    result = _pct_change(runway, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_pct_63d_base_v017_signal(runway):
    result = _pct_change(runway, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_pct_126d_base_v018_signal(runway):
    result = _pct_change(runway, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_pct_252d_base_v019_signal(runway):
    result = _pct_change(runway, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_pct_504d_base_v020_signal(runway):
    result = _pct_change(runway, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_ps_21d_base_v021_signal(runway, sharesbas, closeadj):
    ps = _safe_div(runway, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_ps_63d_base_v022_signal(runway, sharesbas, closeadj):
    ps = _safe_div(runway, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_ps_126d_base_v023_signal(runway, sharesbas, closeadj):
    ps = _safe_div(runway, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_ps_252d_base_v024_signal(runway, sharesbas, closeadj):
    ps = _safe_div(runway, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_ps_504d_base_v025_signal(runway, sharesbas, closeadj):
    ps = _safe_div(runway, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of runway to debtc
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_ratio_debtc_21d_base_v026_signal(runway, debtc):
    ratio = _safe_div(runway, debtc)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of runway to debtc
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_ratio_debtc_63d_base_v027_signal(runway, debtc):
    ratio = _safe_div(runway, debtc)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of runway to debtc
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_ratio_debtc_126d_base_v028_signal(runway, debtc):
    ratio = _safe_div(runway, debtc)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of runway to debtc
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_ratio_debtc_252d_base_v029_signal(runway, debtc):
    ratio = _safe_div(runway, debtc)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of runway to debtc
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_ratio_debtc_504d_base_v030_signal(runway, debtc):
    ratio = _safe_div(runway, debtc)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of runway to ncfo
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_ratio_ncfo_21d_base_v031_signal(runway, ncfo):
    ratio = _safe_div(runway, ncfo)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of runway to ncfo
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_ratio_ncfo_63d_base_v032_signal(runway, ncfo):
    ratio = _safe_div(runway, ncfo)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of runway to ncfo
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_ratio_ncfo_126d_base_v033_signal(runway, ncfo):
    ratio = _safe_div(runway, ncfo)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of runway to ncfo
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_ratio_ncfo_252d_base_v034_signal(runway, ncfo):
    ratio = _safe_div(runway, ncfo)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of runway to ncfo
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_ratio_ncfo_504d_base_v035_signal(runway, ncfo):
    ratio = _safe_div(runway, ncfo)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d runway scaled by assets
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_asset_scaled_21d_base_v036_signal(runway, assets):
    scaled = _safe_div(runway, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d runway scaled by assets
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_asset_scaled_63d_base_v037_signal(runway, assets):
    scaled = _safe_div(runway, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d runway scaled by assets
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_asset_scaled_126d_base_v038_signal(runway, assets):
    scaled = _safe_div(runway, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d runway scaled by assets
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_asset_scaled_252d_base_v039_signal(runway, assets):
    scaled = _safe_div(runway, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d runway scaled by assets
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_asset_scaled_504d_base_v040_signal(runway, assets):
    scaled = _safe_div(runway, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d runway scaled by marketcap
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_mcap_scaled_21d_base_v041_signal(runway, marketcap):
    scaled = _safe_div(runway, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d runway scaled by marketcap
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_mcap_scaled_63d_base_v042_signal(runway, marketcap):
    scaled = _safe_div(runway, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d runway scaled by marketcap
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_mcap_scaled_126d_base_v043_signal(runway, marketcap):
    scaled = _safe_div(runway, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d runway scaled by marketcap
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_mcap_scaled_252d_base_v044_signal(runway, marketcap):
    scaled = _safe_div(runway, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d runway scaled by marketcap
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_mcap_scaled_504d_base_v045_signal(runway, marketcap):
    scaled = _safe_div(runway, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_dist_low_21d_base_v046_signal(runway):
    low = runway.rolling(21).min()
    result = _safe_div(runway - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_dist_low_63d_base_v047_signal(runway):
    low = runway.rolling(63).min()
    result = _safe_div(runway - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_dist_low_126d_base_v048_signal(runway):
    low = runway.rolling(126).min()
    result = _safe_div(runway - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_dist_low_252d_base_v049_signal(runway):
    low = runway.rolling(252).min()
    result = _safe_div(runway - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_dist_low_504d_base_v050_signal(runway):
    low = runway.rolling(504).min()
    result = _safe_div(runway - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_dist_high_21d_base_v051_signal(runway):
    high = runway.rolling(21).max()
    result = _safe_div(high - runway, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_dist_high_63d_base_v052_signal(runway):
    high = runway.rolling(63).max()
    result = _safe_div(high - runway, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_dist_high_126d_base_v053_signal(runway):
    high = runway.rolling(126).max()
    result = _safe_div(high - runway, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_dist_high_252d_base_v054_signal(runway):
    high = runway.rolling(252).max()
    result = _safe_div(high - runway, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_dist_high_504d_base_v055_signal(runway):
    high = runway.rolling(504).max()
    result = _safe_div(high - runway, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_mom_21d_base_v056_signal(runway):
    m1 = _mean(runway, 21)
    m2 = _mean(runway, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_mom_63d_base_v057_signal(runway):
    m1 = _mean(runway, 63)
    m2 = _mean(runway, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_mom_126d_base_v058_signal(runway):
    m1 = _mean(runway, 126)
    m2 = _mean(runway, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_mom_252d_base_v059_signal(runway):
    m1 = _mean(runway, 252)
    m2 = _mean(runway, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_mom_504d_base_v060_signal(runway):
    m1 = _mean(runway, 504)
    m2 = _mean(runway, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_skew_21d_base_v061_signal(runway):
    result = _skew(runway, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_skew_63d_base_v062_signal(runway):
    result = _skew(runway, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_skew_126d_base_v063_signal(runway):
    result = _skew(runway, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_skew_252d_base_v064_signal(runway):
    result = _skew(runway, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_skew_504d_base_v065_signal(runway):
    result = _skew(runway, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_kurt_21d_base_v066_signal(runway):
    result = _kurt(runway, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_kurt_63d_base_v067_signal(runway):
    result = _kurt(runway, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_kurt_126d_base_v068_signal(runway):
    result = _kurt(runway, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_kurt_252d_base_v069_signal(runway):
    result = _kurt(runway, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_kurt_504d_base_v070_signal(runway):
    result = _kurt(runway, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_rank_21d_base_v071_signal(runway, closeadj):
    result = _rank(runway, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_rank_63d_base_v072_signal(runway, closeadj):
    result = _rank(runway, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_rank_126d_base_v073_signal(runway, closeadj):
    result = _rank(runway, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_rank_252d_base_v074_signal(runway, closeadj):
    result = _rank(runway, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of runway
def gm_f19_biotech_f19_adjusted_burn_adjusted_runway_rank_504d_base_v075_signal(runway, closeadj):
    result = _rank(runway, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

