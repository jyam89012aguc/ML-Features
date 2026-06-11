
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_21d_slope_v001_signal(currentratio):
    base = _mean(currentratio, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_21d_slope_v002_signal(currentratio):
    base = _mean(currentratio, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_21d_slope_v003_signal(currentratio):
    base = _mean(currentratio, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_63d_slope_v004_signal(currentratio):
    base = _mean(currentratio, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_63d_slope_v005_signal(currentratio):
    base = _mean(currentratio, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_63d_slope_v006_signal(currentratio):
    base = _mean(currentratio, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_126d_slope_v007_signal(currentratio):
    base = _mean(currentratio, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_126d_slope_v008_signal(currentratio):
    base = _mean(currentratio, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_126d_slope_v009_signal(currentratio):
    base = _mean(currentratio, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_252d_slope_v010_signal(currentratio):
    base = _mean(currentratio, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_252d_slope_v011_signal(currentratio):
    base = _mean(currentratio, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_252d_slope_v012_signal(currentratio):
    base = _mean(currentratio, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_504d_slope_v013_signal(currentratio):
    base = _mean(currentratio, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_504d_slope_v014_signal(currentratio):
    base = _mean(currentratio, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_504d_slope_v015_signal(currentratio):
    base = _mean(currentratio, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_21d_slope_v016_signal(currentratio):
    base = _mean(_log(currentratio), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_21d_slope_v017_signal(currentratio):
    base = _mean(_log(currentratio), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_21d_slope_v018_signal(currentratio):
    base = _mean(_log(currentratio), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_63d_slope_v019_signal(currentratio):
    base = _mean(_log(currentratio), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_63d_slope_v020_signal(currentratio):
    base = _mean(_log(currentratio), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_63d_slope_v021_signal(currentratio):
    base = _mean(_log(currentratio), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_126d_slope_v022_signal(currentratio):
    base = _mean(_log(currentratio), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_126d_slope_v023_signal(currentratio):
    base = _mean(_log(currentratio), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_126d_slope_v024_signal(currentratio):
    base = _mean(_log(currentratio), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_252d_slope_v025_signal(currentratio):
    base = _mean(_log(currentratio), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_252d_slope_v026_signal(currentratio):
    base = _mean(_log(currentratio), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_252d_slope_v027_signal(currentratio):
    base = _mean(_log(currentratio), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_504d_slope_v028_signal(currentratio):
    base = _mean(_log(currentratio), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_504d_slope_v029_signal(currentratio):
    base = _mean(_log(currentratio), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_504d_slope_v030_signal(currentratio):
    base = _mean(_log(currentratio), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_21d_slope_v031_signal(currentratio):
    base = _z(currentratio, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_21d_slope_v032_signal(currentratio):
    base = _z(currentratio, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_21d_slope_v033_signal(currentratio):
    base = _z(currentratio, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_63d_slope_v034_signal(currentratio):
    base = _z(currentratio, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_63d_slope_v035_signal(currentratio):
    base = _z(currentratio, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_63d_slope_v036_signal(currentratio):
    base = _z(currentratio, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_126d_slope_v037_signal(currentratio):
    base = _z(currentratio, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_126d_slope_v038_signal(currentratio):
    base = _z(currentratio, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_126d_slope_v039_signal(currentratio):
    base = _z(currentratio, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_252d_slope_v040_signal(currentratio):
    base = _z(currentratio, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_252d_slope_v041_signal(currentratio):
    base = _z(currentratio, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_252d_slope_v042_signal(currentratio):
    base = _z(currentratio, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_504d_slope_v043_signal(currentratio):
    base = _z(currentratio, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_504d_slope_v044_signal(currentratio):
    base = _z(currentratio, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_504d_slope_v045_signal(currentratio):
    base = _z(currentratio, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_21d_slope_v046_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_21d_slope_v047_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_21d_slope_v048_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_63d_slope_v049_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_63d_slope_v050_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_63d_slope_v051_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_126d_slope_v052_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_126d_slope_v053_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_126d_slope_v054_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_252d_slope_v055_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_252d_slope_v056_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_252d_slope_v057_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_504d_slope_v058_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_504d_slope_v059_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_504d_slope_v060_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_21d_slope_v061_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_21d_slope_v062_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_21d_slope_v063_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_63d_slope_v064_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_63d_slope_v065_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_63d_slope_v066_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_126d_slope_v067_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_126d_slope_v068_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_126d_slope_v069_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_252d_slope_v070_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_252d_slope_v071_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_252d_slope_v072_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_504d_slope_v073_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_504d_slope_v074_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_504d_slope_v075_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_21d_slope_v076_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_21d_slope_v077_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_21d_slope_v078_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_63d_slope_v079_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_63d_slope_v080_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_63d_slope_v081_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_126d_slope_v082_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_126d_slope_v083_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_126d_slope_v084_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_252d_slope_v085_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_252d_slope_v086_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_252d_slope_v087_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_504d_slope_v088_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_504d_slope_v089_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_504d_slope_v090_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_21d_slope_v091_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(21).min(), currentratio.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_21d_slope_v092_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(21).min(), currentratio.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_21d_slope_v093_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(21).min(), currentratio.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_63d_slope_v094_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(63).min(), currentratio.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_63d_slope_v095_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(63).min(), currentratio.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_63d_slope_v096_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(63).min(), currentratio.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_126d_slope_v097_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(126).min(), currentratio.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_126d_slope_v098_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(126).min(), currentratio.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_126d_slope_v099_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(126).min(), currentratio.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_252d_slope_v100_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(252).min(), currentratio.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_252d_slope_v101_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(252).min(), currentratio.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_252d_slope_v102_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(252).min(), currentratio.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_504d_slope_v103_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(504).min(), currentratio.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_504d_slope_v104_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(504).min(), currentratio.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_504d_slope_v105_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(504).min(), currentratio.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_21d_slope_v106_signal(currentratio):
    base = _safe_div(currentratio.rolling(21).max() - currentratio, currentratio.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_21d_slope_v107_signal(currentratio):
    base = _safe_div(currentratio.rolling(21).max() - currentratio, currentratio.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_21d_slope_v108_signal(currentratio):
    base = _safe_div(currentratio.rolling(21).max() - currentratio, currentratio.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_63d_slope_v109_signal(currentratio):
    base = _safe_div(currentratio.rolling(63).max() - currentratio, currentratio.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_63d_slope_v110_signal(currentratio):
    base = _safe_div(currentratio.rolling(63).max() - currentratio, currentratio.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_63d_slope_v111_signal(currentratio):
    base = _safe_div(currentratio.rolling(63).max() - currentratio, currentratio.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_126d_slope_v112_signal(currentratio):
    base = _safe_div(currentratio.rolling(126).max() - currentratio, currentratio.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_126d_slope_v113_signal(currentratio):
    base = _safe_div(currentratio.rolling(126).max() - currentratio, currentratio.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_126d_slope_v114_signal(currentratio):
    base = _safe_div(currentratio.rolling(126).max() - currentratio, currentratio.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_252d_slope_v115_signal(currentratio):
    base = _safe_div(currentratio.rolling(252).max() - currentratio, currentratio.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_252d_slope_v116_signal(currentratio):
    base = _safe_div(currentratio.rolling(252).max() - currentratio, currentratio.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_252d_slope_v117_signal(currentratio):
    base = _safe_div(currentratio.rolling(252).max() - currentratio, currentratio.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_504d_slope_v118_signal(currentratio):
    base = _safe_div(currentratio.rolling(504).max() - currentratio, currentratio.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_504d_slope_v119_signal(currentratio):
    base = _safe_div(currentratio.rolling(504).max() - currentratio, currentratio.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_504d_slope_v120_signal(currentratio):
    base = _safe_div(currentratio.rolling(504).max() - currentratio, currentratio.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_21d_slope_v121_signal(currentratio):
    base = _safe_div(_mean(currentratio, 21) - _mean(currentratio, 42), _mean(currentratio, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_21d_slope_v122_signal(currentratio):
    base = _safe_div(_mean(currentratio, 21) - _mean(currentratio, 42), _mean(currentratio, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_21d_slope_v123_signal(currentratio):
    base = _safe_div(_mean(currentratio, 21) - _mean(currentratio, 42), _mean(currentratio, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_63d_slope_v124_signal(currentratio):
    base = _safe_div(_mean(currentratio, 63) - _mean(currentratio, 126), _mean(currentratio, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_63d_slope_v125_signal(currentratio):
    base = _safe_div(_mean(currentratio, 63) - _mean(currentratio, 126), _mean(currentratio, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_63d_slope_v126_signal(currentratio):
    base = _safe_div(_mean(currentratio, 63) - _mean(currentratio, 126), _mean(currentratio, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_126d_slope_v127_signal(currentratio):
    base = _safe_div(_mean(currentratio, 126) - _mean(currentratio, 252), _mean(currentratio, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_126d_slope_v128_signal(currentratio):
    base = _safe_div(_mean(currentratio, 126) - _mean(currentratio, 252), _mean(currentratio, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_126d_slope_v129_signal(currentratio):
    base = _safe_div(_mean(currentratio, 126) - _mean(currentratio, 252), _mean(currentratio, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_252d_slope_v130_signal(currentratio):
    base = _safe_div(_mean(currentratio, 252) - _mean(currentratio, 504), _mean(currentratio, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_252d_slope_v131_signal(currentratio):
    base = _safe_div(_mean(currentratio, 252) - _mean(currentratio, 504), _mean(currentratio, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_252d_slope_v132_signal(currentratio):
    base = _safe_div(_mean(currentratio, 252) - _mean(currentratio, 504), _mean(currentratio, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_504d_slope_v133_signal(currentratio):
    base = _safe_div(_mean(currentratio, 504) - _mean(currentratio, 1008), _mean(currentratio, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_504d_slope_v134_signal(currentratio):
    base = _safe_div(_mean(currentratio, 504) - _mean(currentratio, 1008), _mean(currentratio, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_504d_slope_v135_signal(currentratio):
    base = _safe_div(_mean(currentratio, 504) - _mean(currentratio, 1008), _mean(currentratio, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_21d_slope_v136_signal(currentratio):
    base = _std(currentratio, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_21d_slope_v137_signal(currentratio):
    base = _std(currentratio, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_21d_slope_v138_signal(currentratio):
    base = _std(currentratio, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_63d_slope_v139_signal(currentratio):
    base = _std(currentratio, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_63d_slope_v140_signal(currentratio):
    base = _std(currentratio, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_63d_slope_v141_signal(currentratio):
    base = _std(currentratio, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_126d_slope_v142_signal(currentratio):
    base = _std(currentratio, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_126d_slope_v143_signal(currentratio):
    base = _std(currentratio, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_126d_slope_v144_signal(currentratio):
    base = _std(currentratio, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_252d_slope_v145_signal(currentratio):
    base = _std(currentratio, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_252d_slope_v146_signal(currentratio):
    base = _std(currentratio, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_252d_slope_v147_signal(currentratio):
    base = _std(currentratio, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_504d_slope_v148_signal(currentratio):
    base = _std(currentratio, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_504d_slope_v149_signal(currentratio):
    base = _std(currentratio, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_504d_slope_v150_signal(currentratio):
    base = _std(currentratio, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

