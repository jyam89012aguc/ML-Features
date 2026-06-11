
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_raw_21d_base_v001_signal(ev, closeadj):
    result = _mean(ev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_raw_63d_base_v002_signal(ev, closeadj):
    result = _mean(ev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_raw_126d_base_v003_signal(ev, closeadj):
    result = _mean(ev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_raw_252d_base_v004_signal(ev, closeadj):
    result = _mean(ev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_raw_504d_base_v005_signal(ev, closeadj):
    result = _mean(ev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_log_21d_base_v006_signal(ev, closeadj):
    result = _mean(_log(ev), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_log_63d_base_v007_signal(ev, closeadj):
    result = _mean(_log(ev), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_log_126d_base_v008_signal(ev, closeadj):
    result = _mean(_log(ev), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_log_252d_base_v009_signal(ev, closeadj):
    result = _mean(_log(ev), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_log_504d_base_v010_signal(ev, closeadj):
    result = _mean(_log(ev), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_z_21d_base_v011_signal(ev):
    result = _z(ev, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_z_63d_base_v012_signal(ev):
    result = _z(ev, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_z_126d_base_v013_signal(ev):
    result = _z(ev, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_z_252d_base_v014_signal(ev):
    result = _z(ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_z_504d_base_v015_signal(ev):
    result = _z(ev, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_pct_21d_base_v016_signal(ev):
    result = _pct_change(ev, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_pct_63d_base_v017_signal(ev):
    result = _pct_change(ev, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_pct_126d_base_v018_signal(ev):
    result = _pct_change(ev, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_pct_252d_base_v019_signal(ev):
    result = _pct_change(ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_pct_504d_base_v020_signal(ev):
    result = _pct_change(ev, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_ps_21d_base_v021_signal(ev, sharesbas, closeadj):
    ps = _safe_div(ev, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_ps_63d_base_v022_signal(ev, sharesbas, closeadj):
    ps = _safe_div(ev, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_ps_126d_base_v023_signal(ev, sharesbas, closeadj):
    ps = _safe_div(ev, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_ps_252d_base_v024_signal(ev, sharesbas, closeadj):
    ps = _safe_div(ev, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_ps_504d_base_v025_signal(ev, sharesbas, closeadj):
    ps = _safe_div(ev, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of ev to rnd
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_ratio_rnd_21d_base_v026_signal(ev, rnd):
    ratio = _safe_div(ev, rnd)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of ev to rnd
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_ratio_rnd_63d_base_v027_signal(ev, rnd):
    ratio = _safe_div(ev, rnd)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of ev to rnd
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_ratio_rnd_126d_base_v028_signal(ev, rnd):
    ratio = _safe_div(ev, rnd)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of ev to rnd
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_ratio_rnd_252d_base_v029_signal(ev, rnd):
    ratio = _safe_div(ev, rnd)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of ev to rnd
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_ratio_rnd_504d_base_v030_signal(ev, rnd):
    ratio = _safe_div(ev, rnd)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ev scaled by assets
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_asset_scaled_21d_base_v031_signal(ev, assets):
    scaled = _safe_div(ev, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ev scaled by assets
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_asset_scaled_63d_base_v032_signal(ev, assets):
    scaled = _safe_div(ev, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ev scaled by assets
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_asset_scaled_126d_base_v033_signal(ev, assets):
    scaled = _safe_div(ev, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ev scaled by assets
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_asset_scaled_252d_base_v034_signal(ev, assets):
    scaled = _safe_div(ev, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ev scaled by assets
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_asset_scaled_504d_base_v035_signal(ev, assets):
    scaled = _safe_div(ev, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ev scaled by marketcap
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_mcap_scaled_21d_base_v036_signal(ev, marketcap):
    scaled = _safe_div(ev, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ev scaled by marketcap
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_mcap_scaled_63d_base_v037_signal(ev, marketcap):
    scaled = _safe_div(ev, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ev scaled by marketcap
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_mcap_scaled_126d_base_v038_signal(ev, marketcap):
    scaled = _safe_div(ev, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ev scaled by marketcap
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_mcap_scaled_252d_base_v039_signal(ev, marketcap):
    scaled = _safe_div(ev, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ev scaled by marketcap
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_mcap_scaled_504d_base_v040_signal(ev, marketcap):
    scaled = _safe_div(ev, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_dist_low_21d_base_v041_signal(ev):
    low = ev.rolling(21).min()
    result = _safe_div(ev - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_dist_low_63d_base_v042_signal(ev):
    low = ev.rolling(63).min()
    result = _safe_div(ev - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_dist_low_126d_base_v043_signal(ev):
    low = ev.rolling(126).min()
    result = _safe_div(ev - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_dist_low_252d_base_v044_signal(ev):
    low = ev.rolling(252).min()
    result = _safe_div(ev - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_dist_low_504d_base_v045_signal(ev):
    low = ev.rolling(504).min()
    result = _safe_div(ev - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_dist_high_21d_base_v046_signal(ev):
    high = ev.rolling(21).max()
    result = _safe_div(high - ev, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_dist_high_63d_base_v047_signal(ev):
    high = ev.rolling(63).max()
    result = _safe_div(high - ev, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_dist_high_126d_base_v048_signal(ev):
    high = ev.rolling(126).max()
    result = _safe_div(high - ev, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_dist_high_252d_base_v049_signal(ev):
    high = ev.rolling(252).max()
    result = _safe_div(high - ev, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_dist_high_504d_base_v050_signal(ev):
    high = ev.rolling(504).max()
    result = _safe_div(high - ev, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_mom_21d_base_v051_signal(ev):
    m1 = _mean(ev, 21)
    m2 = _mean(ev, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_mom_63d_base_v052_signal(ev):
    m1 = _mean(ev, 63)
    m2 = _mean(ev, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_mom_126d_base_v053_signal(ev):
    m1 = _mean(ev, 126)
    m2 = _mean(ev, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_mom_252d_base_v054_signal(ev):
    m1 = _mean(ev, 252)
    m2 = _mean(ev, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_mom_504d_base_v055_signal(ev):
    m1 = _mean(ev, 504)
    m2 = _mean(ev, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_skew_21d_base_v056_signal(ev):
    result = _skew(ev, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_skew_63d_base_v057_signal(ev):
    result = _skew(ev, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_skew_126d_base_v058_signal(ev):
    result = _skew(ev, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_skew_252d_base_v059_signal(ev):
    result = _skew(ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_skew_504d_base_v060_signal(ev):
    result = _skew(ev, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_kurt_21d_base_v061_signal(ev):
    result = _kurt(ev, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_kurt_63d_base_v062_signal(ev):
    result = _kurt(ev, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_kurt_126d_base_v063_signal(ev):
    result = _kurt(ev, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_kurt_252d_base_v064_signal(ev):
    result = _kurt(ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_kurt_504d_base_v065_signal(ev):
    result = _kurt(ev, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_rank_21d_base_v066_signal(ev, closeadj):
    result = _rank(ev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_rank_63d_base_v067_signal(ev, closeadj):
    result = _rank(ev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_rank_126d_base_v068_signal(ev, closeadj):
    result = _rank(ev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_rank_252d_base_v069_signal(ev, closeadj):
    result = _rank(ev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_rank_504d_base_v070_signal(ev, closeadj):
    result = _rank(ev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_autocorr_21d_base_v071_signal(ev):
    result = _autocorr(ev, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_autocorr_63d_base_v072_signal(ev):
    result = _autocorr(ev, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_autocorr_126d_base_v073_signal(ev):
    result = _autocorr(ev, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_autocorr_252d_base_v074_signal(ev):
    result = _autocorr(ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of ev
def gm_f85_biotech_f85_relative_ev_to_rnd_to_sector_autocorr_504d_base_v075_signal(ev):
    result = _autocorr(ev, 504)
    return result.replace([np.inf, -np.inf], np.nan)

