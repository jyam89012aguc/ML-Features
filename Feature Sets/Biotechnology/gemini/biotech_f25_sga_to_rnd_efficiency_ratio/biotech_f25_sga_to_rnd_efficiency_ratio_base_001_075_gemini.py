
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_21d_base_v001_signal(sgna, closeadj):
    result = _mean(sgna, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_63d_base_v002_signal(sgna, closeadj):
    result = _mean(sgna, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_126d_base_v003_signal(sgna, closeadj):
    result = _mean(sgna, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_252d_base_v004_signal(sgna, closeadj):
    result = _mean(sgna, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_504d_base_v005_signal(sgna, closeadj):
    result = _mean(sgna, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_21d_base_v006_signal(sgna, closeadj):
    result = _mean(_log(sgna), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_63d_base_v007_signal(sgna, closeadj):
    result = _mean(_log(sgna), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_126d_base_v008_signal(sgna, closeadj):
    result = _mean(_log(sgna), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_252d_base_v009_signal(sgna, closeadj):
    result = _mean(_log(sgna), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_504d_base_v010_signal(sgna, closeadj):
    result = _mean(_log(sgna), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_21d_base_v011_signal(sgna):
    result = _z(sgna, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_63d_base_v012_signal(sgna):
    result = _z(sgna, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_126d_base_v013_signal(sgna):
    result = _z(sgna, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_252d_base_v014_signal(sgna):
    result = _z(sgna, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_504d_base_v015_signal(sgna):
    result = _z(sgna, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_pct_21d_base_v016_signal(sgna):
    result = _pct_change(sgna, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_pct_63d_base_v017_signal(sgna):
    result = _pct_change(sgna, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_pct_126d_base_v018_signal(sgna):
    result = _pct_change(sgna, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_pct_252d_base_v019_signal(sgna):
    result = _pct_change(sgna, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_pct_504d_base_v020_signal(sgna):
    result = _pct_change(sgna, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_21d_base_v021_signal(sgna, sharesbas, closeadj):
    ps = _safe_div(sgna, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_63d_base_v022_signal(sgna, sharesbas, closeadj):
    ps = _safe_div(sgna, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_126d_base_v023_signal(sgna, sharesbas, closeadj):
    ps = _safe_div(sgna, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_252d_base_v024_signal(sgna, sharesbas, closeadj):
    ps = _safe_div(sgna, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_504d_base_v025_signal(sgna, sharesbas, closeadj):
    ps = _safe_div(sgna, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of sgna to rnd
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ratio_rnd_21d_base_v026_signal(sgna, rnd):
    ratio = _safe_div(sgna, rnd)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of sgna to rnd
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ratio_rnd_63d_base_v027_signal(sgna, rnd):
    ratio = _safe_div(sgna, rnd)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of sgna to rnd
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ratio_rnd_126d_base_v028_signal(sgna, rnd):
    ratio = _safe_div(sgna, rnd)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of sgna to rnd
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ratio_rnd_252d_base_v029_signal(sgna, rnd):
    ratio = _safe_div(sgna, rnd)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of sgna to rnd
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ratio_rnd_504d_base_v030_signal(sgna, rnd):
    ratio = _safe_div(sgna, rnd)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sgna scaled by assets
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_21d_base_v031_signal(sgna, assets):
    scaled = _safe_div(sgna, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sgna scaled by assets
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_63d_base_v032_signal(sgna, assets):
    scaled = _safe_div(sgna, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sgna scaled by assets
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_126d_base_v033_signal(sgna, assets):
    scaled = _safe_div(sgna, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sgna scaled by assets
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_252d_base_v034_signal(sgna, assets):
    scaled = _safe_div(sgna, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sgna scaled by assets
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_504d_base_v035_signal(sgna, assets):
    scaled = _safe_div(sgna, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sgna scaled by marketcap
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_21d_base_v036_signal(sgna, marketcap):
    scaled = _safe_div(sgna, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sgna scaled by marketcap
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_63d_base_v037_signal(sgna, marketcap):
    scaled = _safe_div(sgna, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sgna scaled by marketcap
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_126d_base_v038_signal(sgna, marketcap):
    scaled = _safe_div(sgna, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sgna scaled by marketcap
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_252d_base_v039_signal(sgna, marketcap):
    scaled = _safe_div(sgna, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sgna scaled by marketcap
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_504d_base_v040_signal(sgna, marketcap):
    scaled = _safe_div(sgna, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_21d_base_v041_signal(sgna):
    low = sgna.rolling(21).min()
    result = _safe_div(sgna - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_63d_base_v042_signal(sgna):
    low = sgna.rolling(63).min()
    result = _safe_div(sgna - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_126d_base_v043_signal(sgna):
    low = sgna.rolling(126).min()
    result = _safe_div(sgna - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_252d_base_v044_signal(sgna):
    low = sgna.rolling(252).min()
    result = _safe_div(sgna - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_504d_base_v045_signal(sgna):
    low = sgna.rolling(504).min()
    result = _safe_div(sgna - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_21d_base_v046_signal(sgna):
    high = sgna.rolling(21).max()
    result = _safe_div(high - sgna, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_63d_base_v047_signal(sgna):
    high = sgna.rolling(63).max()
    result = _safe_div(high - sgna, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_126d_base_v048_signal(sgna):
    high = sgna.rolling(126).max()
    result = _safe_div(high - sgna, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_252d_base_v049_signal(sgna):
    high = sgna.rolling(252).max()
    result = _safe_div(high - sgna, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_504d_base_v050_signal(sgna):
    high = sgna.rolling(504).max()
    result = _safe_div(high - sgna, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_21d_base_v051_signal(sgna):
    m1 = _mean(sgna, 21)
    m2 = _mean(sgna, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_63d_base_v052_signal(sgna):
    m1 = _mean(sgna, 63)
    m2 = _mean(sgna, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_126d_base_v053_signal(sgna):
    m1 = _mean(sgna, 126)
    m2 = _mean(sgna, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_252d_base_v054_signal(sgna):
    m1 = _mean(sgna, 252)
    m2 = _mean(sgna, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_504d_base_v055_signal(sgna):
    m1 = _mean(sgna, 504)
    m2 = _mean(sgna, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_skew_21d_base_v056_signal(sgna):
    result = _skew(sgna, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_skew_63d_base_v057_signal(sgna):
    result = _skew(sgna, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_skew_126d_base_v058_signal(sgna):
    result = _skew(sgna, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_skew_252d_base_v059_signal(sgna):
    result = _skew(sgna, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_skew_504d_base_v060_signal(sgna):
    result = _skew(sgna, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_kurt_21d_base_v061_signal(sgna):
    result = _kurt(sgna, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_kurt_63d_base_v062_signal(sgna):
    result = _kurt(sgna, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_kurt_126d_base_v063_signal(sgna):
    result = _kurt(sgna, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_kurt_252d_base_v064_signal(sgna):
    result = _kurt(sgna, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_kurt_504d_base_v065_signal(sgna):
    result = _kurt(sgna, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_rank_21d_base_v066_signal(sgna, closeadj):
    result = _rank(sgna, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_rank_63d_base_v067_signal(sgna, closeadj):
    result = _rank(sgna, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_rank_126d_base_v068_signal(sgna, closeadj):
    result = _rank(sgna, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_rank_252d_base_v069_signal(sgna, closeadj):
    result = _rank(sgna, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_rank_504d_base_v070_signal(sgna, closeadj):
    result = _rank(sgna, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_autocorr_21d_base_v071_signal(sgna):
    result = _autocorr(sgna, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_autocorr_63d_base_v072_signal(sgna):
    result = _autocorr(sgna, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_autocorr_126d_base_v073_signal(sgna):
    result = _autocorr(sgna, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_autocorr_252d_base_v074_signal(sgna):
    result = _autocorr(sgna, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_autocorr_504d_base_v075_signal(sgna):
    result = _autocorr(sgna, 504)
    return result.replace([np.inf, -np.inf], np.nan)

