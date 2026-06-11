
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_21d_base_v001_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(sharesownedfollowingtransaction, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_63d_base_v002_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(sharesownedfollowingtransaction, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_126d_base_v003_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(sharesownedfollowingtransaction, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_252d_base_v004_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(sharesownedfollowingtransaction, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_504d_base_v005_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(sharesownedfollowingtransaction, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_21d_base_v006_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(_log(sharesownedfollowingtransaction), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_63d_base_v007_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(_log(sharesownedfollowingtransaction), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_126d_base_v008_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(_log(sharesownedfollowingtransaction), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_252d_base_v009_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(_log(sharesownedfollowingtransaction), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_504d_base_v010_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(_log(sharesownedfollowingtransaction), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_21d_base_v011_signal(sharesownedfollowingtransaction):
    result = _z(sharesownedfollowingtransaction, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_63d_base_v012_signal(sharesownedfollowingtransaction):
    result = _z(sharesownedfollowingtransaction, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_126d_base_v013_signal(sharesownedfollowingtransaction):
    result = _z(sharesownedfollowingtransaction, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_252d_base_v014_signal(sharesownedfollowingtransaction):
    result = _z(sharesownedfollowingtransaction, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_504d_base_v015_signal(sharesownedfollowingtransaction):
    result = _z(sharesownedfollowingtransaction, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_pct_21d_base_v016_signal(sharesownedfollowingtransaction):
    result = _pct_change(sharesownedfollowingtransaction, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_pct_63d_base_v017_signal(sharesownedfollowingtransaction):
    result = _pct_change(sharesownedfollowingtransaction, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_pct_126d_base_v018_signal(sharesownedfollowingtransaction):
    result = _pct_change(sharesownedfollowingtransaction, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_pct_252d_base_v019_signal(sharesownedfollowingtransaction):
    result = _pct_change(sharesownedfollowingtransaction, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_pct_504d_base_v020_signal(sharesownedfollowingtransaction):
    result = _pct_change(sharesownedfollowingtransaction, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_21d_base_v021_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    ps = _safe_div(sharesownedfollowingtransaction, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_63d_base_v022_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    ps = _safe_div(sharesownedfollowingtransaction, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_126d_base_v023_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    ps = _safe_div(sharesownedfollowingtransaction, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_252d_base_v024_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    ps = _safe_div(sharesownedfollowingtransaction, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_504d_base_v025_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    ps = _safe_div(sharesownedfollowingtransaction, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of sharesownedfollowingtransaction to sharesbas
def gm_f70_biotech_f70_total_insider_ownership_pct_ratio_sharesbas_21d_base_v026_signal(sharesownedfollowingtransaction, sharesbas):
    ratio = _safe_div(sharesownedfollowingtransaction, sharesbas)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of sharesownedfollowingtransaction to sharesbas
def gm_f70_biotech_f70_total_insider_ownership_pct_ratio_sharesbas_63d_base_v027_signal(sharesownedfollowingtransaction, sharesbas):
    ratio = _safe_div(sharesownedfollowingtransaction, sharesbas)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of sharesownedfollowingtransaction to sharesbas
def gm_f70_biotech_f70_total_insider_ownership_pct_ratio_sharesbas_126d_base_v028_signal(sharesownedfollowingtransaction, sharesbas):
    ratio = _safe_div(sharesownedfollowingtransaction, sharesbas)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of sharesownedfollowingtransaction to sharesbas
def gm_f70_biotech_f70_total_insider_ownership_pct_ratio_sharesbas_252d_base_v029_signal(sharesownedfollowingtransaction, sharesbas):
    ratio = _safe_div(sharesownedfollowingtransaction, sharesbas)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of sharesownedfollowingtransaction to sharesbas
def gm_f70_biotech_f70_total_insider_ownership_pct_ratio_sharesbas_504d_base_v030_signal(sharesownedfollowingtransaction, sharesbas):
    ratio = _safe_div(sharesownedfollowingtransaction, sharesbas)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sharesownedfollowingtransaction scaled by assets
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_21d_base_v031_signal(sharesownedfollowingtransaction, assets):
    scaled = _safe_div(sharesownedfollowingtransaction, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sharesownedfollowingtransaction scaled by assets
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_63d_base_v032_signal(sharesownedfollowingtransaction, assets):
    scaled = _safe_div(sharesownedfollowingtransaction, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sharesownedfollowingtransaction scaled by assets
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_126d_base_v033_signal(sharesownedfollowingtransaction, assets):
    scaled = _safe_div(sharesownedfollowingtransaction, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sharesownedfollowingtransaction scaled by assets
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_252d_base_v034_signal(sharesownedfollowingtransaction, assets):
    scaled = _safe_div(sharesownedfollowingtransaction, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sharesownedfollowingtransaction scaled by assets
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_504d_base_v035_signal(sharesownedfollowingtransaction, assets):
    scaled = _safe_div(sharesownedfollowingtransaction, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sharesownedfollowingtransaction scaled by marketcap
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_21d_base_v036_signal(sharesownedfollowingtransaction, marketcap):
    scaled = _safe_div(sharesownedfollowingtransaction, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sharesownedfollowingtransaction scaled by marketcap
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_63d_base_v037_signal(sharesownedfollowingtransaction, marketcap):
    scaled = _safe_div(sharesownedfollowingtransaction, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sharesownedfollowingtransaction scaled by marketcap
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_126d_base_v038_signal(sharesownedfollowingtransaction, marketcap):
    scaled = _safe_div(sharesownedfollowingtransaction, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sharesownedfollowingtransaction scaled by marketcap
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_252d_base_v039_signal(sharesownedfollowingtransaction, marketcap):
    scaled = _safe_div(sharesownedfollowingtransaction, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sharesownedfollowingtransaction scaled by marketcap
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_504d_base_v040_signal(sharesownedfollowingtransaction, marketcap):
    scaled = _safe_div(sharesownedfollowingtransaction, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_21d_base_v041_signal(sharesownedfollowingtransaction):
    low = sharesownedfollowingtransaction.rolling(21).min()
    result = _safe_div(sharesownedfollowingtransaction - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_63d_base_v042_signal(sharesownedfollowingtransaction):
    low = sharesownedfollowingtransaction.rolling(63).min()
    result = _safe_div(sharesownedfollowingtransaction - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_126d_base_v043_signal(sharesownedfollowingtransaction):
    low = sharesownedfollowingtransaction.rolling(126).min()
    result = _safe_div(sharesownedfollowingtransaction - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_252d_base_v044_signal(sharesownedfollowingtransaction):
    low = sharesownedfollowingtransaction.rolling(252).min()
    result = _safe_div(sharesownedfollowingtransaction - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_504d_base_v045_signal(sharesownedfollowingtransaction):
    low = sharesownedfollowingtransaction.rolling(504).min()
    result = _safe_div(sharesownedfollowingtransaction - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_21d_base_v046_signal(sharesownedfollowingtransaction):
    high = sharesownedfollowingtransaction.rolling(21).max()
    result = _safe_div(high - sharesownedfollowingtransaction, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_63d_base_v047_signal(sharesownedfollowingtransaction):
    high = sharesownedfollowingtransaction.rolling(63).max()
    result = _safe_div(high - sharesownedfollowingtransaction, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_126d_base_v048_signal(sharesownedfollowingtransaction):
    high = sharesownedfollowingtransaction.rolling(126).max()
    result = _safe_div(high - sharesownedfollowingtransaction, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_252d_base_v049_signal(sharesownedfollowingtransaction):
    high = sharesownedfollowingtransaction.rolling(252).max()
    result = _safe_div(high - sharesownedfollowingtransaction, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_504d_base_v050_signal(sharesownedfollowingtransaction):
    high = sharesownedfollowingtransaction.rolling(504).max()
    result = _safe_div(high - sharesownedfollowingtransaction, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_21d_base_v051_signal(sharesownedfollowingtransaction):
    m1 = _mean(sharesownedfollowingtransaction, 21)
    m2 = _mean(sharesownedfollowingtransaction, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_63d_base_v052_signal(sharesownedfollowingtransaction):
    m1 = _mean(sharesownedfollowingtransaction, 63)
    m2 = _mean(sharesownedfollowingtransaction, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_126d_base_v053_signal(sharesownedfollowingtransaction):
    m1 = _mean(sharesownedfollowingtransaction, 126)
    m2 = _mean(sharesownedfollowingtransaction, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_252d_base_v054_signal(sharesownedfollowingtransaction):
    m1 = _mean(sharesownedfollowingtransaction, 252)
    m2 = _mean(sharesownedfollowingtransaction, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_504d_base_v055_signal(sharesownedfollowingtransaction):
    m1 = _mean(sharesownedfollowingtransaction, 504)
    m2 = _mean(sharesownedfollowingtransaction, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_skew_21d_base_v056_signal(sharesownedfollowingtransaction):
    result = _skew(sharesownedfollowingtransaction, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_skew_63d_base_v057_signal(sharesownedfollowingtransaction):
    result = _skew(sharesownedfollowingtransaction, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_skew_126d_base_v058_signal(sharesownedfollowingtransaction):
    result = _skew(sharesownedfollowingtransaction, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_skew_252d_base_v059_signal(sharesownedfollowingtransaction):
    result = _skew(sharesownedfollowingtransaction, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_skew_504d_base_v060_signal(sharesownedfollowingtransaction):
    result = _skew(sharesownedfollowingtransaction, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_kurt_21d_base_v061_signal(sharesownedfollowingtransaction):
    result = _kurt(sharesownedfollowingtransaction, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_kurt_63d_base_v062_signal(sharesownedfollowingtransaction):
    result = _kurt(sharesownedfollowingtransaction, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_kurt_126d_base_v063_signal(sharesownedfollowingtransaction):
    result = _kurt(sharesownedfollowingtransaction, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_kurt_252d_base_v064_signal(sharesownedfollowingtransaction):
    result = _kurt(sharesownedfollowingtransaction, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_kurt_504d_base_v065_signal(sharesownedfollowingtransaction):
    result = _kurt(sharesownedfollowingtransaction, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_rank_21d_base_v066_signal(sharesownedfollowingtransaction, closeadj):
    result = _rank(sharesownedfollowingtransaction, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_rank_63d_base_v067_signal(sharesownedfollowingtransaction, closeadj):
    result = _rank(sharesownedfollowingtransaction, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_rank_126d_base_v068_signal(sharesownedfollowingtransaction, closeadj):
    result = _rank(sharesownedfollowingtransaction, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_rank_252d_base_v069_signal(sharesownedfollowingtransaction, closeadj):
    result = _rank(sharesownedfollowingtransaction, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_rank_504d_base_v070_signal(sharesownedfollowingtransaction, closeadj):
    result = _rank(sharesownedfollowingtransaction, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_autocorr_21d_base_v071_signal(sharesownedfollowingtransaction):
    result = _autocorr(sharesownedfollowingtransaction, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_autocorr_63d_base_v072_signal(sharesownedfollowingtransaction):
    result = _autocorr(sharesownedfollowingtransaction, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_autocorr_126d_base_v073_signal(sharesownedfollowingtransaction):
    result = _autocorr(sharesownedfollowingtransaction, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_autocorr_252d_base_v074_signal(sharesownedfollowingtransaction):
    result = _autocorr(sharesownedfollowingtransaction, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_autocorr_504d_base_v075_signal(sharesownedfollowingtransaction):
    result = _autocorr(sharesownedfollowingtransaction, 504)
    return result.replace([np.inf, -np.inf], np.nan)

