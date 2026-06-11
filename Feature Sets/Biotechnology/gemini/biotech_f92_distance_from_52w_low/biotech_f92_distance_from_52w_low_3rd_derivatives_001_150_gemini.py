
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw close
def gm_f92_biotech_f92_distance_from_52w_low_raw_21d_accel_v001_signal(close):
    base = _mean(close, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw close
def gm_f92_biotech_f92_distance_from_52w_low_raw_21d_accel_v002_signal(close):
    base = _mean(close, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw close
def gm_f92_biotech_f92_distance_from_52w_low_raw_21d_accel_v003_signal(close):
    base = _mean(close, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw close
def gm_f92_biotech_f92_distance_from_52w_low_raw_63d_accel_v004_signal(close):
    base = _mean(close, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw close
def gm_f92_biotech_f92_distance_from_52w_low_raw_63d_accel_v005_signal(close):
    base = _mean(close, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw close
def gm_f92_biotech_f92_distance_from_52w_low_raw_63d_accel_v006_signal(close):
    base = _mean(close, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw close
def gm_f92_biotech_f92_distance_from_52w_low_raw_126d_accel_v007_signal(close):
    base = _mean(close, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw close
def gm_f92_biotech_f92_distance_from_52w_low_raw_126d_accel_v008_signal(close):
    base = _mean(close, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw close
def gm_f92_biotech_f92_distance_from_52w_low_raw_126d_accel_v009_signal(close):
    base = _mean(close, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw close
def gm_f92_biotech_f92_distance_from_52w_low_raw_252d_accel_v010_signal(close):
    base = _mean(close, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw close
def gm_f92_biotech_f92_distance_from_52w_low_raw_252d_accel_v011_signal(close):
    base = _mean(close, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw close
def gm_f92_biotech_f92_distance_from_52w_low_raw_252d_accel_v012_signal(close):
    base = _mean(close, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw close
def gm_f92_biotech_f92_distance_from_52w_low_raw_504d_accel_v013_signal(close):
    base = _mean(close, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw close
def gm_f92_biotech_f92_distance_from_52w_low_raw_504d_accel_v014_signal(close):
    base = _mean(close, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw close
def gm_f92_biotech_f92_distance_from_52w_low_raw_504d_accel_v015_signal(close):
    base = _mean(close, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log close
def gm_f92_biotech_f92_distance_from_52w_low_log_21d_accel_v016_signal(close):
    base = _mean(_log(close), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log close
def gm_f92_biotech_f92_distance_from_52w_low_log_21d_accel_v017_signal(close):
    base = _mean(_log(close), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log close
def gm_f92_biotech_f92_distance_from_52w_low_log_21d_accel_v018_signal(close):
    base = _mean(_log(close), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log close
def gm_f92_biotech_f92_distance_from_52w_low_log_63d_accel_v019_signal(close):
    base = _mean(_log(close), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log close
def gm_f92_biotech_f92_distance_from_52w_low_log_63d_accel_v020_signal(close):
    base = _mean(_log(close), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log close
def gm_f92_biotech_f92_distance_from_52w_low_log_63d_accel_v021_signal(close):
    base = _mean(_log(close), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log close
def gm_f92_biotech_f92_distance_from_52w_low_log_126d_accel_v022_signal(close):
    base = _mean(_log(close), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log close
def gm_f92_biotech_f92_distance_from_52w_low_log_126d_accel_v023_signal(close):
    base = _mean(_log(close), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log close
def gm_f92_biotech_f92_distance_from_52w_low_log_126d_accel_v024_signal(close):
    base = _mean(_log(close), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log close
def gm_f92_biotech_f92_distance_from_52w_low_log_252d_accel_v025_signal(close):
    base = _mean(_log(close), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log close
def gm_f92_biotech_f92_distance_from_52w_low_log_252d_accel_v026_signal(close):
    base = _mean(_log(close), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log close
def gm_f92_biotech_f92_distance_from_52w_low_log_252d_accel_v027_signal(close):
    base = _mean(_log(close), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log close
def gm_f92_biotech_f92_distance_from_52w_low_log_504d_accel_v028_signal(close):
    base = _mean(_log(close), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log close
def gm_f92_biotech_f92_distance_from_52w_low_log_504d_accel_v029_signal(close):
    base = _mean(_log(close), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log close
def gm_f92_biotech_f92_distance_from_52w_low_log_504d_accel_v030_signal(close):
    base = _mean(_log(close), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z close
def gm_f92_biotech_f92_distance_from_52w_low_z_21d_accel_v031_signal(close):
    base = _z(close, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z close
def gm_f92_biotech_f92_distance_from_52w_low_z_21d_accel_v032_signal(close):
    base = _z(close, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z close
def gm_f92_biotech_f92_distance_from_52w_low_z_21d_accel_v033_signal(close):
    base = _z(close, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z close
def gm_f92_biotech_f92_distance_from_52w_low_z_63d_accel_v034_signal(close):
    base = _z(close, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z close
def gm_f92_biotech_f92_distance_from_52w_low_z_63d_accel_v035_signal(close):
    base = _z(close, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z close
def gm_f92_biotech_f92_distance_from_52w_low_z_63d_accel_v036_signal(close):
    base = _z(close, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z close
def gm_f92_biotech_f92_distance_from_52w_low_z_126d_accel_v037_signal(close):
    base = _z(close, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z close
def gm_f92_biotech_f92_distance_from_52w_low_z_126d_accel_v038_signal(close):
    base = _z(close, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z close
def gm_f92_biotech_f92_distance_from_52w_low_z_126d_accel_v039_signal(close):
    base = _z(close, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z close
def gm_f92_biotech_f92_distance_from_52w_low_z_252d_accel_v040_signal(close):
    base = _z(close, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z close
def gm_f92_biotech_f92_distance_from_52w_low_z_252d_accel_v041_signal(close):
    base = _z(close, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z close
def gm_f92_biotech_f92_distance_from_52w_low_z_252d_accel_v042_signal(close):
    base = _z(close, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z close
def gm_f92_biotech_f92_distance_from_52w_low_z_504d_accel_v043_signal(close):
    base = _z(close, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z close
def gm_f92_biotech_f92_distance_from_52w_low_z_504d_accel_v044_signal(close):
    base = _z(close, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z close
def gm_f92_biotech_f92_distance_from_52w_low_z_504d_accel_v045_signal(close):
    base = _z(close, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps close
def gm_f92_biotech_f92_distance_from_52w_low_ps_21d_accel_v046_signal(close, sharesbas):
    base = _safe_div(_mean(close, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps close
def gm_f92_biotech_f92_distance_from_52w_low_ps_21d_accel_v047_signal(close, sharesbas):
    base = _safe_div(_mean(close, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps close
def gm_f92_biotech_f92_distance_from_52w_low_ps_21d_accel_v048_signal(close, sharesbas):
    base = _safe_div(_mean(close, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps close
def gm_f92_biotech_f92_distance_from_52w_low_ps_63d_accel_v049_signal(close, sharesbas):
    base = _safe_div(_mean(close, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps close
def gm_f92_biotech_f92_distance_from_52w_low_ps_63d_accel_v050_signal(close, sharesbas):
    base = _safe_div(_mean(close, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps close
def gm_f92_biotech_f92_distance_from_52w_low_ps_63d_accel_v051_signal(close, sharesbas):
    base = _safe_div(_mean(close, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps close
def gm_f92_biotech_f92_distance_from_52w_low_ps_126d_accel_v052_signal(close, sharesbas):
    base = _safe_div(_mean(close, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps close
def gm_f92_biotech_f92_distance_from_52w_low_ps_126d_accel_v053_signal(close, sharesbas):
    base = _safe_div(_mean(close, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps close
def gm_f92_biotech_f92_distance_from_52w_low_ps_126d_accel_v054_signal(close, sharesbas):
    base = _safe_div(_mean(close, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps close
def gm_f92_biotech_f92_distance_from_52w_low_ps_252d_accel_v055_signal(close, sharesbas):
    base = _safe_div(_mean(close, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps close
def gm_f92_biotech_f92_distance_from_52w_low_ps_252d_accel_v056_signal(close, sharesbas):
    base = _safe_div(_mean(close, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps close
def gm_f92_biotech_f92_distance_from_52w_low_ps_252d_accel_v057_signal(close, sharesbas):
    base = _safe_div(_mean(close, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps close
def gm_f92_biotech_f92_distance_from_52w_low_ps_504d_accel_v058_signal(close, sharesbas):
    base = _safe_div(_mean(close, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps close
def gm_f92_biotech_f92_distance_from_52w_low_ps_504d_accel_v059_signal(close, sharesbas):
    base = _safe_div(_mean(close, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps close
def gm_f92_biotech_f92_distance_from_52w_low_ps_504d_accel_v060_signal(close, sharesbas):
    base = _safe_div(_mean(close, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_asset_scaled_21d_accel_v061_signal(close, assets):
    base = _safe_div(_mean(close, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_asset_scaled_21d_accel_v062_signal(close, assets):
    base = _safe_div(_mean(close, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_asset_scaled_21d_accel_v063_signal(close, assets):
    base = _safe_div(_mean(close, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_asset_scaled_63d_accel_v064_signal(close, assets):
    base = _safe_div(_mean(close, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_asset_scaled_63d_accel_v065_signal(close, assets):
    base = _safe_div(_mean(close, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_asset_scaled_63d_accel_v066_signal(close, assets):
    base = _safe_div(_mean(close, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_asset_scaled_126d_accel_v067_signal(close, assets):
    base = _safe_div(_mean(close, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_asset_scaled_126d_accel_v068_signal(close, assets):
    base = _safe_div(_mean(close, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_asset_scaled_126d_accel_v069_signal(close, assets):
    base = _safe_div(_mean(close, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_asset_scaled_252d_accel_v070_signal(close, assets):
    base = _safe_div(_mean(close, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_asset_scaled_252d_accel_v071_signal(close, assets):
    base = _safe_div(_mean(close, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_asset_scaled_252d_accel_v072_signal(close, assets):
    base = _safe_div(_mean(close, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_asset_scaled_504d_accel_v073_signal(close, assets):
    base = _safe_div(_mean(close, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_asset_scaled_504d_accel_v074_signal(close, assets):
    base = _safe_div(_mean(close, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_asset_scaled_504d_accel_v075_signal(close, assets):
    base = _safe_div(_mean(close, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_mcap_scaled_21d_accel_v076_signal(close, marketcap):
    base = _safe_div(_mean(close, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_mcap_scaled_21d_accel_v077_signal(close, marketcap):
    base = _safe_div(_mean(close, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_mcap_scaled_21d_accel_v078_signal(close, marketcap):
    base = _safe_div(_mean(close, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_mcap_scaled_63d_accel_v079_signal(close, marketcap):
    base = _safe_div(_mean(close, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_mcap_scaled_63d_accel_v080_signal(close, marketcap):
    base = _safe_div(_mean(close, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_mcap_scaled_63d_accel_v081_signal(close, marketcap):
    base = _safe_div(_mean(close, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_mcap_scaled_126d_accel_v082_signal(close, marketcap):
    base = _safe_div(_mean(close, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_mcap_scaled_126d_accel_v083_signal(close, marketcap):
    base = _safe_div(_mean(close, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_mcap_scaled_126d_accel_v084_signal(close, marketcap):
    base = _safe_div(_mean(close, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_mcap_scaled_252d_accel_v085_signal(close, marketcap):
    base = _safe_div(_mean(close, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_mcap_scaled_252d_accel_v086_signal(close, marketcap):
    base = _safe_div(_mean(close, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_mcap_scaled_252d_accel_v087_signal(close, marketcap):
    base = _safe_div(_mean(close, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_mcap_scaled_504d_accel_v088_signal(close, marketcap):
    base = _safe_div(_mean(close, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_mcap_scaled_504d_accel_v089_signal(close, marketcap):
    base = _safe_div(_mean(close, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled close
def gm_f92_biotech_f92_distance_from_52w_low_mcap_scaled_504d_accel_v090_signal(close, marketcap):
    base = _safe_div(_mean(close, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low close
def gm_f92_biotech_f92_distance_from_52w_low_dist_low_21d_accel_v091_signal(close):
    base = _safe_div(close - close.rolling(21).min(), close.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low close
def gm_f92_biotech_f92_distance_from_52w_low_dist_low_21d_accel_v092_signal(close):
    base = _safe_div(close - close.rolling(21).min(), close.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low close
def gm_f92_biotech_f92_distance_from_52w_low_dist_low_21d_accel_v093_signal(close):
    base = _safe_div(close - close.rolling(21).min(), close.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low close
def gm_f92_biotech_f92_distance_from_52w_low_dist_low_63d_accel_v094_signal(close):
    base = _safe_div(close - close.rolling(63).min(), close.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low close
def gm_f92_biotech_f92_distance_from_52w_low_dist_low_63d_accel_v095_signal(close):
    base = _safe_div(close - close.rolling(63).min(), close.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low close
def gm_f92_biotech_f92_distance_from_52w_low_dist_low_63d_accel_v096_signal(close):
    base = _safe_div(close - close.rolling(63).min(), close.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low close
def gm_f92_biotech_f92_distance_from_52w_low_dist_low_126d_accel_v097_signal(close):
    base = _safe_div(close - close.rolling(126).min(), close.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low close
def gm_f92_biotech_f92_distance_from_52w_low_dist_low_126d_accel_v098_signal(close):
    base = _safe_div(close - close.rolling(126).min(), close.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low close
def gm_f92_biotech_f92_distance_from_52w_low_dist_low_126d_accel_v099_signal(close):
    base = _safe_div(close - close.rolling(126).min(), close.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low close
def gm_f92_biotech_f92_distance_from_52w_low_dist_low_252d_accel_v100_signal(close):
    base = _safe_div(close - close.rolling(252).min(), close.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low close
def gm_f92_biotech_f92_distance_from_52w_low_dist_low_252d_accel_v101_signal(close):
    base = _safe_div(close - close.rolling(252).min(), close.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low close
def gm_f92_biotech_f92_distance_from_52w_low_dist_low_252d_accel_v102_signal(close):
    base = _safe_div(close - close.rolling(252).min(), close.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low close
def gm_f92_biotech_f92_distance_from_52w_low_dist_low_504d_accel_v103_signal(close):
    base = _safe_div(close - close.rolling(504).min(), close.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low close
def gm_f92_biotech_f92_distance_from_52w_low_dist_low_504d_accel_v104_signal(close):
    base = _safe_div(close - close.rolling(504).min(), close.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low close
def gm_f92_biotech_f92_distance_from_52w_low_dist_low_504d_accel_v105_signal(close):
    base = _safe_div(close - close.rolling(504).min(), close.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high close
def gm_f92_biotech_f92_distance_from_52w_low_dist_high_21d_accel_v106_signal(close):
    base = _safe_div(close.rolling(21).max() - close, close.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high close
def gm_f92_biotech_f92_distance_from_52w_low_dist_high_21d_accel_v107_signal(close):
    base = _safe_div(close.rolling(21).max() - close, close.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high close
def gm_f92_biotech_f92_distance_from_52w_low_dist_high_21d_accel_v108_signal(close):
    base = _safe_div(close.rolling(21).max() - close, close.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high close
def gm_f92_biotech_f92_distance_from_52w_low_dist_high_63d_accel_v109_signal(close):
    base = _safe_div(close.rolling(63).max() - close, close.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high close
def gm_f92_biotech_f92_distance_from_52w_low_dist_high_63d_accel_v110_signal(close):
    base = _safe_div(close.rolling(63).max() - close, close.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high close
def gm_f92_biotech_f92_distance_from_52w_low_dist_high_63d_accel_v111_signal(close):
    base = _safe_div(close.rolling(63).max() - close, close.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high close
def gm_f92_biotech_f92_distance_from_52w_low_dist_high_126d_accel_v112_signal(close):
    base = _safe_div(close.rolling(126).max() - close, close.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high close
def gm_f92_biotech_f92_distance_from_52w_low_dist_high_126d_accel_v113_signal(close):
    base = _safe_div(close.rolling(126).max() - close, close.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high close
def gm_f92_biotech_f92_distance_from_52w_low_dist_high_126d_accel_v114_signal(close):
    base = _safe_div(close.rolling(126).max() - close, close.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high close
def gm_f92_biotech_f92_distance_from_52w_low_dist_high_252d_accel_v115_signal(close):
    base = _safe_div(close.rolling(252).max() - close, close.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high close
def gm_f92_biotech_f92_distance_from_52w_low_dist_high_252d_accel_v116_signal(close):
    base = _safe_div(close.rolling(252).max() - close, close.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high close
def gm_f92_biotech_f92_distance_from_52w_low_dist_high_252d_accel_v117_signal(close):
    base = _safe_div(close.rolling(252).max() - close, close.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high close
def gm_f92_biotech_f92_distance_from_52w_low_dist_high_504d_accel_v118_signal(close):
    base = _safe_div(close.rolling(504).max() - close, close.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high close
def gm_f92_biotech_f92_distance_from_52w_low_dist_high_504d_accel_v119_signal(close):
    base = _safe_div(close.rolling(504).max() - close, close.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high close
def gm_f92_biotech_f92_distance_from_52w_low_dist_high_504d_accel_v120_signal(close):
    base = _safe_div(close.rolling(504).max() - close, close.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom close
def gm_f92_biotech_f92_distance_from_52w_low_mom_21d_accel_v121_signal(close):
    base = _safe_div(_mean(close, 21) - _mean(close, 42), _mean(close, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom close
def gm_f92_biotech_f92_distance_from_52w_low_mom_21d_accel_v122_signal(close):
    base = _safe_div(_mean(close, 21) - _mean(close, 42), _mean(close, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom close
def gm_f92_biotech_f92_distance_from_52w_low_mom_21d_accel_v123_signal(close):
    base = _safe_div(_mean(close, 21) - _mean(close, 42), _mean(close, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom close
def gm_f92_biotech_f92_distance_from_52w_low_mom_63d_accel_v124_signal(close):
    base = _safe_div(_mean(close, 63) - _mean(close, 126), _mean(close, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom close
def gm_f92_biotech_f92_distance_from_52w_low_mom_63d_accel_v125_signal(close):
    base = _safe_div(_mean(close, 63) - _mean(close, 126), _mean(close, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom close
def gm_f92_biotech_f92_distance_from_52w_low_mom_63d_accel_v126_signal(close):
    base = _safe_div(_mean(close, 63) - _mean(close, 126), _mean(close, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom close
def gm_f92_biotech_f92_distance_from_52w_low_mom_126d_accel_v127_signal(close):
    base = _safe_div(_mean(close, 126) - _mean(close, 252), _mean(close, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom close
def gm_f92_biotech_f92_distance_from_52w_low_mom_126d_accel_v128_signal(close):
    base = _safe_div(_mean(close, 126) - _mean(close, 252), _mean(close, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom close
def gm_f92_biotech_f92_distance_from_52w_low_mom_126d_accel_v129_signal(close):
    base = _safe_div(_mean(close, 126) - _mean(close, 252), _mean(close, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom close
def gm_f92_biotech_f92_distance_from_52w_low_mom_252d_accel_v130_signal(close):
    base = _safe_div(_mean(close, 252) - _mean(close, 504), _mean(close, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom close
def gm_f92_biotech_f92_distance_from_52w_low_mom_252d_accel_v131_signal(close):
    base = _safe_div(_mean(close, 252) - _mean(close, 504), _mean(close, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom close
def gm_f92_biotech_f92_distance_from_52w_low_mom_252d_accel_v132_signal(close):
    base = _safe_div(_mean(close, 252) - _mean(close, 504), _mean(close, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom close
def gm_f92_biotech_f92_distance_from_52w_low_mom_504d_accel_v133_signal(close):
    base = _safe_div(_mean(close, 504) - _mean(close, 1008), _mean(close, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom close
def gm_f92_biotech_f92_distance_from_52w_low_mom_504d_accel_v134_signal(close):
    base = _safe_div(_mean(close, 504) - _mean(close, 1008), _mean(close, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom close
def gm_f92_biotech_f92_distance_from_52w_low_mom_504d_accel_v135_signal(close):
    base = _safe_div(_mean(close, 504) - _mean(close, 1008), _mean(close, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol close
def gm_f92_biotech_f92_distance_from_52w_low_vol_21d_accel_v136_signal(close):
    base = _std(close, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol close
def gm_f92_biotech_f92_distance_from_52w_low_vol_21d_accel_v137_signal(close):
    base = _std(close, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol close
def gm_f92_biotech_f92_distance_from_52w_low_vol_21d_accel_v138_signal(close):
    base = _std(close, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol close
def gm_f92_biotech_f92_distance_from_52w_low_vol_63d_accel_v139_signal(close):
    base = _std(close, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol close
def gm_f92_biotech_f92_distance_from_52w_low_vol_63d_accel_v140_signal(close):
    base = _std(close, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol close
def gm_f92_biotech_f92_distance_from_52w_low_vol_63d_accel_v141_signal(close):
    base = _std(close, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol close
def gm_f92_biotech_f92_distance_from_52w_low_vol_126d_accel_v142_signal(close):
    base = _std(close, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol close
def gm_f92_biotech_f92_distance_from_52w_low_vol_126d_accel_v143_signal(close):
    base = _std(close, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol close
def gm_f92_biotech_f92_distance_from_52w_low_vol_126d_accel_v144_signal(close):
    base = _std(close, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol close
def gm_f92_biotech_f92_distance_from_52w_low_vol_252d_accel_v145_signal(close):
    base = _std(close, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol close
def gm_f92_biotech_f92_distance_from_52w_low_vol_252d_accel_v146_signal(close):
    base = _std(close, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol close
def gm_f92_biotech_f92_distance_from_52w_low_vol_252d_accel_v147_signal(close):
    base = _std(close, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol close
def gm_f92_biotech_f92_distance_from_52w_low_vol_504d_accel_v148_signal(close):
    base = _std(close, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol close
def gm_f92_biotech_f92_distance_from_52w_low_vol_504d_accel_v149_signal(close):
    base = _std(close, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol close
def gm_f92_biotech_f92_distance_from_52w_low_vol_504d_accel_v150_signal(close):
    base = _std(close, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

