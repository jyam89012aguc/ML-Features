
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_21d_accel_v001_signal(currentratio):
    base = _mean(currentratio, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_21d_accel_v002_signal(currentratio):
    base = _mean(currentratio, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_21d_accel_v003_signal(currentratio):
    base = _mean(currentratio, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_63d_accel_v004_signal(currentratio):
    base = _mean(currentratio, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_63d_accel_v005_signal(currentratio):
    base = _mean(currentratio, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_63d_accel_v006_signal(currentratio):
    base = _mean(currentratio, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_126d_accel_v007_signal(currentratio):
    base = _mean(currentratio, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_126d_accel_v008_signal(currentratio):
    base = _mean(currentratio, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_126d_accel_v009_signal(currentratio):
    base = _mean(currentratio, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_252d_accel_v010_signal(currentratio):
    base = _mean(currentratio, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_252d_accel_v011_signal(currentratio):
    base = _mean(currentratio, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_252d_accel_v012_signal(currentratio):
    base = _mean(currentratio, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_504d_accel_v013_signal(currentratio):
    base = _mean(currentratio, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_504d_accel_v014_signal(currentratio):
    base = _mean(currentratio, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw currentratio
def gm_f04_biotech_f04_current_ratio_solvency_raw_504d_accel_v015_signal(currentratio):
    base = _mean(currentratio, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_21d_accel_v016_signal(currentratio):
    base = _mean(_log(currentratio), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_21d_accel_v017_signal(currentratio):
    base = _mean(_log(currentratio), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_21d_accel_v018_signal(currentratio):
    base = _mean(_log(currentratio), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_63d_accel_v019_signal(currentratio):
    base = _mean(_log(currentratio), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_63d_accel_v020_signal(currentratio):
    base = _mean(_log(currentratio), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_63d_accel_v021_signal(currentratio):
    base = _mean(_log(currentratio), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_126d_accel_v022_signal(currentratio):
    base = _mean(_log(currentratio), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_126d_accel_v023_signal(currentratio):
    base = _mean(_log(currentratio), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_126d_accel_v024_signal(currentratio):
    base = _mean(_log(currentratio), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_252d_accel_v025_signal(currentratio):
    base = _mean(_log(currentratio), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_252d_accel_v026_signal(currentratio):
    base = _mean(_log(currentratio), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_252d_accel_v027_signal(currentratio):
    base = _mean(_log(currentratio), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_504d_accel_v028_signal(currentratio):
    base = _mean(_log(currentratio), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_504d_accel_v029_signal(currentratio):
    base = _mean(_log(currentratio), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log currentratio
def gm_f04_biotech_f04_current_ratio_solvency_log_504d_accel_v030_signal(currentratio):
    base = _mean(_log(currentratio), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_21d_accel_v031_signal(currentratio):
    base = _z(currentratio, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_21d_accel_v032_signal(currentratio):
    base = _z(currentratio, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_21d_accel_v033_signal(currentratio):
    base = _z(currentratio, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_63d_accel_v034_signal(currentratio):
    base = _z(currentratio, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_63d_accel_v035_signal(currentratio):
    base = _z(currentratio, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_63d_accel_v036_signal(currentratio):
    base = _z(currentratio, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_126d_accel_v037_signal(currentratio):
    base = _z(currentratio, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_126d_accel_v038_signal(currentratio):
    base = _z(currentratio, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_126d_accel_v039_signal(currentratio):
    base = _z(currentratio, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_252d_accel_v040_signal(currentratio):
    base = _z(currentratio, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_252d_accel_v041_signal(currentratio):
    base = _z(currentratio, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_252d_accel_v042_signal(currentratio):
    base = _z(currentratio, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_504d_accel_v043_signal(currentratio):
    base = _z(currentratio, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_504d_accel_v044_signal(currentratio):
    base = _z(currentratio, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z currentratio
def gm_f04_biotech_f04_current_ratio_solvency_z_504d_accel_v045_signal(currentratio):
    base = _z(currentratio, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_21d_accel_v046_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_21d_accel_v047_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_21d_accel_v048_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_63d_accel_v049_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_63d_accel_v050_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_63d_accel_v051_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_126d_accel_v052_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_126d_accel_v053_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_126d_accel_v054_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_252d_accel_v055_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_252d_accel_v056_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_252d_accel_v057_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_504d_accel_v058_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_504d_accel_v059_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps currentratio
def gm_f04_biotech_f04_current_ratio_solvency_ps_504d_accel_v060_signal(currentratio, sharesbas):
    base = _safe_div(_mean(currentratio, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_21d_accel_v061_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_21d_accel_v062_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_21d_accel_v063_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_63d_accel_v064_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_63d_accel_v065_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_63d_accel_v066_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_126d_accel_v067_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_126d_accel_v068_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_126d_accel_v069_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_252d_accel_v070_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_252d_accel_v071_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_252d_accel_v072_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_504d_accel_v073_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_504d_accel_v074_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_asset_scaled_504d_accel_v075_signal(currentratio, assets):
    base = _safe_div(_mean(currentratio, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_21d_accel_v076_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_21d_accel_v077_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_21d_accel_v078_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_63d_accel_v079_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_63d_accel_v080_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_63d_accel_v081_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_126d_accel_v082_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_126d_accel_v083_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_126d_accel_v084_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_252d_accel_v085_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_252d_accel_v086_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_252d_accel_v087_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_504d_accel_v088_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_504d_accel_v089_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mcap_scaled_504d_accel_v090_signal(currentratio, marketcap):
    base = _safe_div(_mean(currentratio, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_21d_accel_v091_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(21).min(), currentratio.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_21d_accel_v092_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(21).min(), currentratio.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_21d_accel_v093_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(21).min(), currentratio.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_63d_accel_v094_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(63).min(), currentratio.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_63d_accel_v095_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(63).min(), currentratio.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_63d_accel_v096_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(63).min(), currentratio.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_126d_accel_v097_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(126).min(), currentratio.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_126d_accel_v098_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(126).min(), currentratio.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_126d_accel_v099_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(126).min(), currentratio.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_252d_accel_v100_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(252).min(), currentratio.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_252d_accel_v101_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(252).min(), currentratio.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_252d_accel_v102_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(252).min(), currentratio.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_504d_accel_v103_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(504).min(), currentratio.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_504d_accel_v104_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(504).min(), currentratio.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_low_504d_accel_v105_signal(currentratio):
    base = _safe_div(currentratio - currentratio.rolling(504).min(), currentratio.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_21d_accel_v106_signal(currentratio):
    base = _safe_div(currentratio.rolling(21).max() - currentratio, currentratio.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_21d_accel_v107_signal(currentratio):
    base = _safe_div(currentratio.rolling(21).max() - currentratio, currentratio.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_21d_accel_v108_signal(currentratio):
    base = _safe_div(currentratio.rolling(21).max() - currentratio, currentratio.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_63d_accel_v109_signal(currentratio):
    base = _safe_div(currentratio.rolling(63).max() - currentratio, currentratio.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_63d_accel_v110_signal(currentratio):
    base = _safe_div(currentratio.rolling(63).max() - currentratio, currentratio.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_63d_accel_v111_signal(currentratio):
    base = _safe_div(currentratio.rolling(63).max() - currentratio, currentratio.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_126d_accel_v112_signal(currentratio):
    base = _safe_div(currentratio.rolling(126).max() - currentratio, currentratio.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_126d_accel_v113_signal(currentratio):
    base = _safe_div(currentratio.rolling(126).max() - currentratio, currentratio.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_126d_accel_v114_signal(currentratio):
    base = _safe_div(currentratio.rolling(126).max() - currentratio, currentratio.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_252d_accel_v115_signal(currentratio):
    base = _safe_div(currentratio.rolling(252).max() - currentratio, currentratio.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_252d_accel_v116_signal(currentratio):
    base = _safe_div(currentratio.rolling(252).max() - currentratio, currentratio.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_252d_accel_v117_signal(currentratio):
    base = _safe_div(currentratio.rolling(252).max() - currentratio, currentratio.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_504d_accel_v118_signal(currentratio):
    base = _safe_div(currentratio.rolling(504).max() - currentratio, currentratio.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_504d_accel_v119_signal(currentratio):
    base = _safe_div(currentratio.rolling(504).max() - currentratio, currentratio.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high currentratio
def gm_f04_biotech_f04_current_ratio_solvency_dist_high_504d_accel_v120_signal(currentratio):
    base = _safe_div(currentratio.rolling(504).max() - currentratio, currentratio.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_21d_accel_v121_signal(currentratio):
    base = _safe_div(_mean(currentratio, 21) - _mean(currentratio, 42), _mean(currentratio, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_21d_accel_v122_signal(currentratio):
    base = _safe_div(_mean(currentratio, 21) - _mean(currentratio, 42), _mean(currentratio, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_21d_accel_v123_signal(currentratio):
    base = _safe_div(_mean(currentratio, 21) - _mean(currentratio, 42), _mean(currentratio, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_63d_accel_v124_signal(currentratio):
    base = _safe_div(_mean(currentratio, 63) - _mean(currentratio, 126), _mean(currentratio, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_63d_accel_v125_signal(currentratio):
    base = _safe_div(_mean(currentratio, 63) - _mean(currentratio, 126), _mean(currentratio, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_63d_accel_v126_signal(currentratio):
    base = _safe_div(_mean(currentratio, 63) - _mean(currentratio, 126), _mean(currentratio, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_126d_accel_v127_signal(currentratio):
    base = _safe_div(_mean(currentratio, 126) - _mean(currentratio, 252), _mean(currentratio, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_126d_accel_v128_signal(currentratio):
    base = _safe_div(_mean(currentratio, 126) - _mean(currentratio, 252), _mean(currentratio, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_126d_accel_v129_signal(currentratio):
    base = _safe_div(_mean(currentratio, 126) - _mean(currentratio, 252), _mean(currentratio, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_252d_accel_v130_signal(currentratio):
    base = _safe_div(_mean(currentratio, 252) - _mean(currentratio, 504), _mean(currentratio, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_252d_accel_v131_signal(currentratio):
    base = _safe_div(_mean(currentratio, 252) - _mean(currentratio, 504), _mean(currentratio, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_252d_accel_v132_signal(currentratio):
    base = _safe_div(_mean(currentratio, 252) - _mean(currentratio, 504), _mean(currentratio, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_504d_accel_v133_signal(currentratio):
    base = _safe_div(_mean(currentratio, 504) - _mean(currentratio, 1008), _mean(currentratio, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_504d_accel_v134_signal(currentratio):
    base = _safe_div(_mean(currentratio, 504) - _mean(currentratio, 1008), _mean(currentratio, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom currentratio
def gm_f04_biotech_f04_current_ratio_solvency_mom_504d_accel_v135_signal(currentratio):
    base = _safe_div(_mean(currentratio, 504) - _mean(currentratio, 1008), _mean(currentratio, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_21d_accel_v136_signal(currentratio):
    base = _std(currentratio, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_21d_accel_v137_signal(currentratio):
    base = _std(currentratio, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_21d_accel_v138_signal(currentratio):
    base = _std(currentratio, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_63d_accel_v139_signal(currentratio):
    base = _std(currentratio, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_63d_accel_v140_signal(currentratio):
    base = _std(currentratio, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_63d_accel_v141_signal(currentratio):
    base = _std(currentratio, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_126d_accel_v142_signal(currentratio):
    base = _std(currentratio, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_126d_accel_v143_signal(currentratio):
    base = _std(currentratio, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_126d_accel_v144_signal(currentratio):
    base = _std(currentratio, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_252d_accel_v145_signal(currentratio):
    base = _std(currentratio, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_252d_accel_v146_signal(currentratio):
    base = _std(currentratio, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_252d_accel_v147_signal(currentratio):
    base = _std(currentratio, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_504d_accel_v148_signal(currentratio):
    base = _std(currentratio, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_504d_accel_v149_signal(currentratio):
    base = _std(currentratio, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol currentratio
def gm_f04_biotech_f04_current_ratio_solvency_vol_504d_accel_v150_signal(currentratio):
    base = _std(currentratio, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

