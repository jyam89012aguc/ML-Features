
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw action
def gm_f90_biotech_f90_corporate_event_density_score_raw_21d_accel_v001_signal(action):
    base = _mean(action, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw action
def gm_f90_biotech_f90_corporate_event_density_score_raw_21d_accel_v002_signal(action):
    base = _mean(action, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw action
def gm_f90_biotech_f90_corporate_event_density_score_raw_21d_accel_v003_signal(action):
    base = _mean(action, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw action
def gm_f90_biotech_f90_corporate_event_density_score_raw_63d_accel_v004_signal(action):
    base = _mean(action, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw action
def gm_f90_biotech_f90_corporate_event_density_score_raw_63d_accel_v005_signal(action):
    base = _mean(action, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw action
def gm_f90_biotech_f90_corporate_event_density_score_raw_63d_accel_v006_signal(action):
    base = _mean(action, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw action
def gm_f90_biotech_f90_corporate_event_density_score_raw_126d_accel_v007_signal(action):
    base = _mean(action, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw action
def gm_f90_biotech_f90_corporate_event_density_score_raw_126d_accel_v008_signal(action):
    base = _mean(action, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw action
def gm_f90_biotech_f90_corporate_event_density_score_raw_126d_accel_v009_signal(action):
    base = _mean(action, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw action
def gm_f90_biotech_f90_corporate_event_density_score_raw_252d_accel_v010_signal(action):
    base = _mean(action, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw action
def gm_f90_biotech_f90_corporate_event_density_score_raw_252d_accel_v011_signal(action):
    base = _mean(action, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw action
def gm_f90_biotech_f90_corporate_event_density_score_raw_252d_accel_v012_signal(action):
    base = _mean(action, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw action
def gm_f90_biotech_f90_corporate_event_density_score_raw_504d_accel_v013_signal(action):
    base = _mean(action, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw action
def gm_f90_biotech_f90_corporate_event_density_score_raw_504d_accel_v014_signal(action):
    base = _mean(action, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw action
def gm_f90_biotech_f90_corporate_event_density_score_raw_504d_accel_v015_signal(action):
    base = _mean(action, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log action
def gm_f90_biotech_f90_corporate_event_density_score_log_21d_accel_v016_signal(action):
    base = _mean(_log(action), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log action
def gm_f90_biotech_f90_corporate_event_density_score_log_21d_accel_v017_signal(action):
    base = _mean(_log(action), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log action
def gm_f90_biotech_f90_corporate_event_density_score_log_21d_accel_v018_signal(action):
    base = _mean(_log(action), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log action
def gm_f90_biotech_f90_corporate_event_density_score_log_63d_accel_v019_signal(action):
    base = _mean(_log(action), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log action
def gm_f90_biotech_f90_corporate_event_density_score_log_63d_accel_v020_signal(action):
    base = _mean(_log(action), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log action
def gm_f90_biotech_f90_corporate_event_density_score_log_63d_accel_v021_signal(action):
    base = _mean(_log(action), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log action
def gm_f90_biotech_f90_corporate_event_density_score_log_126d_accel_v022_signal(action):
    base = _mean(_log(action), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log action
def gm_f90_biotech_f90_corporate_event_density_score_log_126d_accel_v023_signal(action):
    base = _mean(_log(action), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log action
def gm_f90_biotech_f90_corporate_event_density_score_log_126d_accel_v024_signal(action):
    base = _mean(_log(action), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log action
def gm_f90_biotech_f90_corporate_event_density_score_log_252d_accel_v025_signal(action):
    base = _mean(_log(action), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log action
def gm_f90_biotech_f90_corporate_event_density_score_log_252d_accel_v026_signal(action):
    base = _mean(_log(action), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log action
def gm_f90_biotech_f90_corporate_event_density_score_log_252d_accel_v027_signal(action):
    base = _mean(_log(action), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log action
def gm_f90_biotech_f90_corporate_event_density_score_log_504d_accel_v028_signal(action):
    base = _mean(_log(action), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log action
def gm_f90_biotech_f90_corporate_event_density_score_log_504d_accel_v029_signal(action):
    base = _mean(_log(action), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log action
def gm_f90_biotech_f90_corporate_event_density_score_log_504d_accel_v030_signal(action):
    base = _mean(_log(action), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z action
def gm_f90_biotech_f90_corporate_event_density_score_z_21d_accel_v031_signal(action):
    base = _z(action, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z action
def gm_f90_biotech_f90_corporate_event_density_score_z_21d_accel_v032_signal(action):
    base = _z(action, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z action
def gm_f90_biotech_f90_corporate_event_density_score_z_21d_accel_v033_signal(action):
    base = _z(action, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z action
def gm_f90_biotech_f90_corporate_event_density_score_z_63d_accel_v034_signal(action):
    base = _z(action, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z action
def gm_f90_biotech_f90_corporate_event_density_score_z_63d_accel_v035_signal(action):
    base = _z(action, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z action
def gm_f90_biotech_f90_corporate_event_density_score_z_63d_accel_v036_signal(action):
    base = _z(action, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z action
def gm_f90_biotech_f90_corporate_event_density_score_z_126d_accel_v037_signal(action):
    base = _z(action, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z action
def gm_f90_biotech_f90_corporate_event_density_score_z_126d_accel_v038_signal(action):
    base = _z(action, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z action
def gm_f90_biotech_f90_corporate_event_density_score_z_126d_accel_v039_signal(action):
    base = _z(action, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z action
def gm_f90_biotech_f90_corporate_event_density_score_z_252d_accel_v040_signal(action):
    base = _z(action, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z action
def gm_f90_biotech_f90_corporate_event_density_score_z_252d_accel_v041_signal(action):
    base = _z(action, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z action
def gm_f90_biotech_f90_corporate_event_density_score_z_252d_accel_v042_signal(action):
    base = _z(action, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z action
def gm_f90_biotech_f90_corporate_event_density_score_z_504d_accel_v043_signal(action):
    base = _z(action, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z action
def gm_f90_biotech_f90_corporate_event_density_score_z_504d_accel_v044_signal(action):
    base = _z(action, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z action
def gm_f90_biotech_f90_corporate_event_density_score_z_504d_accel_v045_signal(action):
    base = _z(action, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps action
def gm_f90_biotech_f90_corporate_event_density_score_ps_21d_accel_v046_signal(action, sharesbas):
    base = _safe_div(_mean(action, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps action
def gm_f90_biotech_f90_corporate_event_density_score_ps_21d_accel_v047_signal(action, sharesbas):
    base = _safe_div(_mean(action, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps action
def gm_f90_biotech_f90_corporate_event_density_score_ps_21d_accel_v048_signal(action, sharesbas):
    base = _safe_div(_mean(action, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps action
def gm_f90_biotech_f90_corporate_event_density_score_ps_63d_accel_v049_signal(action, sharesbas):
    base = _safe_div(_mean(action, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps action
def gm_f90_biotech_f90_corporate_event_density_score_ps_63d_accel_v050_signal(action, sharesbas):
    base = _safe_div(_mean(action, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps action
def gm_f90_biotech_f90_corporate_event_density_score_ps_63d_accel_v051_signal(action, sharesbas):
    base = _safe_div(_mean(action, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps action
def gm_f90_biotech_f90_corporate_event_density_score_ps_126d_accel_v052_signal(action, sharesbas):
    base = _safe_div(_mean(action, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps action
def gm_f90_biotech_f90_corporate_event_density_score_ps_126d_accel_v053_signal(action, sharesbas):
    base = _safe_div(_mean(action, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps action
def gm_f90_biotech_f90_corporate_event_density_score_ps_126d_accel_v054_signal(action, sharesbas):
    base = _safe_div(_mean(action, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps action
def gm_f90_biotech_f90_corporate_event_density_score_ps_252d_accel_v055_signal(action, sharesbas):
    base = _safe_div(_mean(action, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps action
def gm_f90_biotech_f90_corporate_event_density_score_ps_252d_accel_v056_signal(action, sharesbas):
    base = _safe_div(_mean(action, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps action
def gm_f90_biotech_f90_corporate_event_density_score_ps_252d_accel_v057_signal(action, sharesbas):
    base = _safe_div(_mean(action, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps action
def gm_f90_biotech_f90_corporate_event_density_score_ps_504d_accel_v058_signal(action, sharesbas):
    base = _safe_div(_mean(action, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps action
def gm_f90_biotech_f90_corporate_event_density_score_ps_504d_accel_v059_signal(action, sharesbas):
    base = _safe_div(_mean(action, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps action
def gm_f90_biotech_f90_corporate_event_density_score_ps_504d_accel_v060_signal(action, sharesbas):
    base = _safe_div(_mean(action, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_asset_scaled_21d_accel_v061_signal(action, assets):
    base = _safe_div(_mean(action, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_asset_scaled_21d_accel_v062_signal(action, assets):
    base = _safe_div(_mean(action, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_asset_scaled_21d_accel_v063_signal(action, assets):
    base = _safe_div(_mean(action, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_asset_scaled_63d_accel_v064_signal(action, assets):
    base = _safe_div(_mean(action, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_asset_scaled_63d_accel_v065_signal(action, assets):
    base = _safe_div(_mean(action, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_asset_scaled_63d_accel_v066_signal(action, assets):
    base = _safe_div(_mean(action, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_asset_scaled_126d_accel_v067_signal(action, assets):
    base = _safe_div(_mean(action, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_asset_scaled_126d_accel_v068_signal(action, assets):
    base = _safe_div(_mean(action, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_asset_scaled_126d_accel_v069_signal(action, assets):
    base = _safe_div(_mean(action, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_asset_scaled_252d_accel_v070_signal(action, assets):
    base = _safe_div(_mean(action, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_asset_scaled_252d_accel_v071_signal(action, assets):
    base = _safe_div(_mean(action, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_asset_scaled_252d_accel_v072_signal(action, assets):
    base = _safe_div(_mean(action, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_asset_scaled_504d_accel_v073_signal(action, assets):
    base = _safe_div(_mean(action, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_asset_scaled_504d_accel_v074_signal(action, assets):
    base = _safe_div(_mean(action, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_asset_scaled_504d_accel_v075_signal(action, assets):
    base = _safe_div(_mean(action, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_mcap_scaled_21d_accel_v076_signal(action, marketcap):
    base = _safe_div(_mean(action, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_mcap_scaled_21d_accel_v077_signal(action, marketcap):
    base = _safe_div(_mean(action, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_mcap_scaled_21d_accel_v078_signal(action, marketcap):
    base = _safe_div(_mean(action, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_mcap_scaled_63d_accel_v079_signal(action, marketcap):
    base = _safe_div(_mean(action, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_mcap_scaled_63d_accel_v080_signal(action, marketcap):
    base = _safe_div(_mean(action, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_mcap_scaled_63d_accel_v081_signal(action, marketcap):
    base = _safe_div(_mean(action, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_mcap_scaled_126d_accel_v082_signal(action, marketcap):
    base = _safe_div(_mean(action, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_mcap_scaled_126d_accel_v083_signal(action, marketcap):
    base = _safe_div(_mean(action, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_mcap_scaled_126d_accel_v084_signal(action, marketcap):
    base = _safe_div(_mean(action, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_mcap_scaled_252d_accel_v085_signal(action, marketcap):
    base = _safe_div(_mean(action, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_mcap_scaled_252d_accel_v086_signal(action, marketcap):
    base = _safe_div(_mean(action, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_mcap_scaled_252d_accel_v087_signal(action, marketcap):
    base = _safe_div(_mean(action, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_mcap_scaled_504d_accel_v088_signal(action, marketcap):
    base = _safe_div(_mean(action, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_mcap_scaled_504d_accel_v089_signal(action, marketcap):
    base = _safe_div(_mean(action, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled action
def gm_f90_biotech_f90_corporate_event_density_score_mcap_scaled_504d_accel_v090_signal(action, marketcap):
    base = _safe_div(_mean(action, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low action
def gm_f90_biotech_f90_corporate_event_density_score_dist_low_21d_accel_v091_signal(action):
    base = _safe_div(action - action.rolling(21).min(), action.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low action
def gm_f90_biotech_f90_corporate_event_density_score_dist_low_21d_accel_v092_signal(action):
    base = _safe_div(action - action.rolling(21).min(), action.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low action
def gm_f90_biotech_f90_corporate_event_density_score_dist_low_21d_accel_v093_signal(action):
    base = _safe_div(action - action.rolling(21).min(), action.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low action
def gm_f90_biotech_f90_corporate_event_density_score_dist_low_63d_accel_v094_signal(action):
    base = _safe_div(action - action.rolling(63).min(), action.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low action
def gm_f90_biotech_f90_corporate_event_density_score_dist_low_63d_accel_v095_signal(action):
    base = _safe_div(action - action.rolling(63).min(), action.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low action
def gm_f90_biotech_f90_corporate_event_density_score_dist_low_63d_accel_v096_signal(action):
    base = _safe_div(action - action.rolling(63).min(), action.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low action
def gm_f90_biotech_f90_corporate_event_density_score_dist_low_126d_accel_v097_signal(action):
    base = _safe_div(action - action.rolling(126).min(), action.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low action
def gm_f90_biotech_f90_corporate_event_density_score_dist_low_126d_accel_v098_signal(action):
    base = _safe_div(action - action.rolling(126).min(), action.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low action
def gm_f90_biotech_f90_corporate_event_density_score_dist_low_126d_accel_v099_signal(action):
    base = _safe_div(action - action.rolling(126).min(), action.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low action
def gm_f90_biotech_f90_corporate_event_density_score_dist_low_252d_accel_v100_signal(action):
    base = _safe_div(action - action.rolling(252).min(), action.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low action
def gm_f90_biotech_f90_corporate_event_density_score_dist_low_252d_accel_v101_signal(action):
    base = _safe_div(action - action.rolling(252).min(), action.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low action
def gm_f90_biotech_f90_corporate_event_density_score_dist_low_252d_accel_v102_signal(action):
    base = _safe_div(action - action.rolling(252).min(), action.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low action
def gm_f90_biotech_f90_corporate_event_density_score_dist_low_504d_accel_v103_signal(action):
    base = _safe_div(action - action.rolling(504).min(), action.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low action
def gm_f90_biotech_f90_corporate_event_density_score_dist_low_504d_accel_v104_signal(action):
    base = _safe_div(action - action.rolling(504).min(), action.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low action
def gm_f90_biotech_f90_corporate_event_density_score_dist_low_504d_accel_v105_signal(action):
    base = _safe_div(action - action.rolling(504).min(), action.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high action
def gm_f90_biotech_f90_corporate_event_density_score_dist_high_21d_accel_v106_signal(action):
    base = _safe_div(action.rolling(21).max() - action, action.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high action
def gm_f90_biotech_f90_corporate_event_density_score_dist_high_21d_accel_v107_signal(action):
    base = _safe_div(action.rolling(21).max() - action, action.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high action
def gm_f90_biotech_f90_corporate_event_density_score_dist_high_21d_accel_v108_signal(action):
    base = _safe_div(action.rolling(21).max() - action, action.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high action
def gm_f90_biotech_f90_corporate_event_density_score_dist_high_63d_accel_v109_signal(action):
    base = _safe_div(action.rolling(63).max() - action, action.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high action
def gm_f90_biotech_f90_corporate_event_density_score_dist_high_63d_accel_v110_signal(action):
    base = _safe_div(action.rolling(63).max() - action, action.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high action
def gm_f90_biotech_f90_corporate_event_density_score_dist_high_63d_accel_v111_signal(action):
    base = _safe_div(action.rolling(63).max() - action, action.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high action
def gm_f90_biotech_f90_corporate_event_density_score_dist_high_126d_accel_v112_signal(action):
    base = _safe_div(action.rolling(126).max() - action, action.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high action
def gm_f90_biotech_f90_corporate_event_density_score_dist_high_126d_accel_v113_signal(action):
    base = _safe_div(action.rolling(126).max() - action, action.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high action
def gm_f90_biotech_f90_corporate_event_density_score_dist_high_126d_accel_v114_signal(action):
    base = _safe_div(action.rolling(126).max() - action, action.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high action
def gm_f90_biotech_f90_corporate_event_density_score_dist_high_252d_accel_v115_signal(action):
    base = _safe_div(action.rolling(252).max() - action, action.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high action
def gm_f90_biotech_f90_corporate_event_density_score_dist_high_252d_accel_v116_signal(action):
    base = _safe_div(action.rolling(252).max() - action, action.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high action
def gm_f90_biotech_f90_corporate_event_density_score_dist_high_252d_accel_v117_signal(action):
    base = _safe_div(action.rolling(252).max() - action, action.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high action
def gm_f90_biotech_f90_corporate_event_density_score_dist_high_504d_accel_v118_signal(action):
    base = _safe_div(action.rolling(504).max() - action, action.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high action
def gm_f90_biotech_f90_corporate_event_density_score_dist_high_504d_accel_v119_signal(action):
    base = _safe_div(action.rolling(504).max() - action, action.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high action
def gm_f90_biotech_f90_corporate_event_density_score_dist_high_504d_accel_v120_signal(action):
    base = _safe_div(action.rolling(504).max() - action, action.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom action
def gm_f90_biotech_f90_corporate_event_density_score_mom_21d_accel_v121_signal(action):
    base = _safe_div(_mean(action, 21) - _mean(action, 42), _mean(action, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom action
def gm_f90_biotech_f90_corporate_event_density_score_mom_21d_accel_v122_signal(action):
    base = _safe_div(_mean(action, 21) - _mean(action, 42), _mean(action, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom action
def gm_f90_biotech_f90_corporate_event_density_score_mom_21d_accel_v123_signal(action):
    base = _safe_div(_mean(action, 21) - _mean(action, 42), _mean(action, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom action
def gm_f90_biotech_f90_corporate_event_density_score_mom_63d_accel_v124_signal(action):
    base = _safe_div(_mean(action, 63) - _mean(action, 126), _mean(action, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom action
def gm_f90_biotech_f90_corporate_event_density_score_mom_63d_accel_v125_signal(action):
    base = _safe_div(_mean(action, 63) - _mean(action, 126), _mean(action, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom action
def gm_f90_biotech_f90_corporate_event_density_score_mom_63d_accel_v126_signal(action):
    base = _safe_div(_mean(action, 63) - _mean(action, 126), _mean(action, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom action
def gm_f90_biotech_f90_corporate_event_density_score_mom_126d_accel_v127_signal(action):
    base = _safe_div(_mean(action, 126) - _mean(action, 252), _mean(action, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom action
def gm_f90_biotech_f90_corporate_event_density_score_mom_126d_accel_v128_signal(action):
    base = _safe_div(_mean(action, 126) - _mean(action, 252), _mean(action, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom action
def gm_f90_biotech_f90_corporate_event_density_score_mom_126d_accel_v129_signal(action):
    base = _safe_div(_mean(action, 126) - _mean(action, 252), _mean(action, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom action
def gm_f90_biotech_f90_corporate_event_density_score_mom_252d_accel_v130_signal(action):
    base = _safe_div(_mean(action, 252) - _mean(action, 504), _mean(action, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom action
def gm_f90_biotech_f90_corporate_event_density_score_mom_252d_accel_v131_signal(action):
    base = _safe_div(_mean(action, 252) - _mean(action, 504), _mean(action, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom action
def gm_f90_biotech_f90_corporate_event_density_score_mom_252d_accel_v132_signal(action):
    base = _safe_div(_mean(action, 252) - _mean(action, 504), _mean(action, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom action
def gm_f90_biotech_f90_corporate_event_density_score_mom_504d_accel_v133_signal(action):
    base = _safe_div(_mean(action, 504) - _mean(action, 1008), _mean(action, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom action
def gm_f90_biotech_f90_corporate_event_density_score_mom_504d_accel_v134_signal(action):
    base = _safe_div(_mean(action, 504) - _mean(action, 1008), _mean(action, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom action
def gm_f90_biotech_f90_corporate_event_density_score_mom_504d_accel_v135_signal(action):
    base = _safe_div(_mean(action, 504) - _mean(action, 1008), _mean(action, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol action
def gm_f90_biotech_f90_corporate_event_density_score_vol_21d_accel_v136_signal(action):
    base = _std(action, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol action
def gm_f90_biotech_f90_corporate_event_density_score_vol_21d_accel_v137_signal(action):
    base = _std(action, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol action
def gm_f90_biotech_f90_corporate_event_density_score_vol_21d_accel_v138_signal(action):
    base = _std(action, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol action
def gm_f90_biotech_f90_corporate_event_density_score_vol_63d_accel_v139_signal(action):
    base = _std(action, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol action
def gm_f90_biotech_f90_corporate_event_density_score_vol_63d_accel_v140_signal(action):
    base = _std(action, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol action
def gm_f90_biotech_f90_corporate_event_density_score_vol_63d_accel_v141_signal(action):
    base = _std(action, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol action
def gm_f90_biotech_f90_corporate_event_density_score_vol_126d_accel_v142_signal(action):
    base = _std(action, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol action
def gm_f90_biotech_f90_corporate_event_density_score_vol_126d_accel_v143_signal(action):
    base = _std(action, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol action
def gm_f90_biotech_f90_corporate_event_density_score_vol_126d_accel_v144_signal(action):
    base = _std(action, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol action
def gm_f90_biotech_f90_corporate_event_density_score_vol_252d_accel_v145_signal(action):
    base = _std(action, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol action
def gm_f90_biotech_f90_corporate_event_density_score_vol_252d_accel_v146_signal(action):
    base = _std(action, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol action
def gm_f90_biotech_f90_corporate_event_density_score_vol_252d_accel_v147_signal(action):
    base = _std(action, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol action
def gm_f90_biotech_f90_corporate_event_density_score_vol_504d_accel_v148_signal(action):
    base = _std(action, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol action
def gm_f90_biotech_f90_corporate_event_density_score_vol_504d_accel_v149_signal(action):
    base = _std(action, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol action
def gm_f90_biotech_f90_corporate_event_density_score_vol_504d_accel_v150_signal(action):
    base = _std(action, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

