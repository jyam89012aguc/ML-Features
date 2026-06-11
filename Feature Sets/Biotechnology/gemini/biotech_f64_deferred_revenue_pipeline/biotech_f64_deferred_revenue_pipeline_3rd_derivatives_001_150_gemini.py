
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_21d_accel_v001_signal(deferredrev):
    base = _mean(deferredrev, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_21d_accel_v002_signal(deferredrev):
    base = _mean(deferredrev, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_21d_accel_v003_signal(deferredrev):
    base = _mean(deferredrev, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_63d_accel_v004_signal(deferredrev):
    base = _mean(deferredrev, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_63d_accel_v005_signal(deferredrev):
    base = _mean(deferredrev, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_63d_accel_v006_signal(deferredrev):
    base = _mean(deferredrev, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_126d_accel_v007_signal(deferredrev):
    base = _mean(deferredrev, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_126d_accel_v008_signal(deferredrev):
    base = _mean(deferredrev, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_126d_accel_v009_signal(deferredrev):
    base = _mean(deferredrev, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_252d_accel_v010_signal(deferredrev):
    base = _mean(deferredrev, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_252d_accel_v011_signal(deferredrev):
    base = _mean(deferredrev, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_252d_accel_v012_signal(deferredrev):
    base = _mean(deferredrev, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_504d_accel_v013_signal(deferredrev):
    base = _mean(deferredrev, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_504d_accel_v014_signal(deferredrev):
    base = _mean(deferredrev, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_504d_accel_v015_signal(deferredrev):
    base = _mean(deferredrev, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_21d_accel_v016_signal(deferredrev):
    base = _mean(_log(deferredrev), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_21d_accel_v017_signal(deferredrev):
    base = _mean(_log(deferredrev), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_21d_accel_v018_signal(deferredrev):
    base = _mean(_log(deferredrev), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_63d_accel_v019_signal(deferredrev):
    base = _mean(_log(deferredrev), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_63d_accel_v020_signal(deferredrev):
    base = _mean(_log(deferredrev), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_63d_accel_v021_signal(deferredrev):
    base = _mean(_log(deferredrev), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_126d_accel_v022_signal(deferredrev):
    base = _mean(_log(deferredrev), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_126d_accel_v023_signal(deferredrev):
    base = _mean(_log(deferredrev), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_126d_accel_v024_signal(deferredrev):
    base = _mean(_log(deferredrev), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_252d_accel_v025_signal(deferredrev):
    base = _mean(_log(deferredrev), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_252d_accel_v026_signal(deferredrev):
    base = _mean(_log(deferredrev), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_252d_accel_v027_signal(deferredrev):
    base = _mean(_log(deferredrev), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_504d_accel_v028_signal(deferredrev):
    base = _mean(_log(deferredrev), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_504d_accel_v029_signal(deferredrev):
    base = _mean(_log(deferredrev), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_504d_accel_v030_signal(deferredrev):
    base = _mean(_log(deferredrev), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_21d_accel_v031_signal(deferredrev):
    base = _z(deferredrev, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_21d_accel_v032_signal(deferredrev):
    base = _z(deferredrev, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_21d_accel_v033_signal(deferredrev):
    base = _z(deferredrev, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_63d_accel_v034_signal(deferredrev):
    base = _z(deferredrev, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_63d_accel_v035_signal(deferredrev):
    base = _z(deferredrev, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_63d_accel_v036_signal(deferredrev):
    base = _z(deferredrev, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_126d_accel_v037_signal(deferredrev):
    base = _z(deferredrev, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_126d_accel_v038_signal(deferredrev):
    base = _z(deferredrev, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_126d_accel_v039_signal(deferredrev):
    base = _z(deferredrev, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_252d_accel_v040_signal(deferredrev):
    base = _z(deferredrev, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_252d_accel_v041_signal(deferredrev):
    base = _z(deferredrev, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_252d_accel_v042_signal(deferredrev):
    base = _z(deferredrev, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_504d_accel_v043_signal(deferredrev):
    base = _z(deferredrev, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_504d_accel_v044_signal(deferredrev):
    base = _z(deferredrev, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_504d_accel_v045_signal(deferredrev):
    base = _z(deferredrev, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_21d_accel_v046_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_21d_accel_v047_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_21d_accel_v048_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_63d_accel_v049_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_63d_accel_v050_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_63d_accel_v051_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_126d_accel_v052_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_126d_accel_v053_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_126d_accel_v054_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_252d_accel_v055_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_252d_accel_v056_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_252d_accel_v057_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_504d_accel_v058_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_504d_accel_v059_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_504d_accel_v060_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_21d_accel_v061_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_21d_accel_v062_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_21d_accel_v063_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_63d_accel_v064_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_63d_accel_v065_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_63d_accel_v066_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_126d_accel_v067_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_126d_accel_v068_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_126d_accel_v069_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_252d_accel_v070_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_252d_accel_v071_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_252d_accel_v072_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_504d_accel_v073_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_504d_accel_v074_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_504d_accel_v075_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_21d_accel_v076_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_21d_accel_v077_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_21d_accel_v078_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_63d_accel_v079_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_63d_accel_v080_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_63d_accel_v081_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_126d_accel_v082_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_126d_accel_v083_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_126d_accel_v084_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_252d_accel_v085_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_252d_accel_v086_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_252d_accel_v087_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_504d_accel_v088_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_504d_accel_v089_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_504d_accel_v090_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_21d_accel_v091_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(21).min(), deferredrev.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_21d_accel_v092_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(21).min(), deferredrev.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_21d_accel_v093_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(21).min(), deferredrev.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_63d_accel_v094_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(63).min(), deferredrev.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_63d_accel_v095_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(63).min(), deferredrev.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_63d_accel_v096_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(63).min(), deferredrev.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_126d_accel_v097_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(126).min(), deferredrev.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_126d_accel_v098_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(126).min(), deferredrev.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_126d_accel_v099_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(126).min(), deferredrev.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_252d_accel_v100_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(252).min(), deferredrev.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_252d_accel_v101_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(252).min(), deferredrev.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_252d_accel_v102_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(252).min(), deferredrev.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_504d_accel_v103_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(504).min(), deferredrev.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_504d_accel_v104_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(504).min(), deferredrev.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_504d_accel_v105_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(504).min(), deferredrev.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_21d_accel_v106_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(21).max() - deferredrev, deferredrev.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_21d_accel_v107_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(21).max() - deferredrev, deferredrev.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_21d_accel_v108_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(21).max() - deferredrev, deferredrev.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_63d_accel_v109_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(63).max() - deferredrev, deferredrev.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_63d_accel_v110_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(63).max() - deferredrev, deferredrev.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_63d_accel_v111_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(63).max() - deferredrev, deferredrev.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_126d_accel_v112_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(126).max() - deferredrev, deferredrev.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_126d_accel_v113_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(126).max() - deferredrev, deferredrev.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_126d_accel_v114_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(126).max() - deferredrev, deferredrev.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_252d_accel_v115_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(252).max() - deferredrev, deferredrev.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_252d_accel_v116_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(252).max() - deferredrev, deferredrev.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_252d_accel_v117_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(252).max() - deferredrev, deferredrev.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_504d_accel_v118_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(504).max() - deferredrev, deferredrev.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_504d_accel_v119_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(504).max() - deferredrev, deferredrev.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_504d_accel_v120_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(504).max() - deferredrev, deferredrev.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_21d_accel_v121_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 21) - _mean(deferredrev, 42), _mean(deferredrev, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_21d_accel_v122_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 21) - _mean(deferredrev, 42), _mean(deferredrev, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_21d_accel_v123_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 21) - _mean(deferredrev, 42), _mean(deferredrev, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_63d_accel_v124_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 63) - _mean(deferredrev, 126), _mean(deferredrev, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_63d_accel_v125_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 63) - _mean(deferredrev, 126), _mean(deferredrev, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_63d_accel_v126_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 63) - _mean(deferredrev, 126), _mean(deferredrev, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_126d_accel_v127_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 126) - _mean(deferredrev, 252), _mean(deferredrev, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_126d_accel_v128_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 126) - _mean(deferredrev, 252), _mean(deferredrev, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_126d_accel_v129_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 126) - _mean(deferredrev, 252), _mean(deferredrev, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_252d_accel_v130_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 252) - _mean(deferredrev, 504), _mean(deferredrev, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_252d_accel_v131_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 252) - _mean(deferredrev, 504), _mean(deferredrev, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_252d_accel_v132_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 252) - _mean(deferredrev, 504), _mean(deferredrev, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_504d_accel_v133_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 504) - _mean(deferredrev, 1008), _mean(deferredrev, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_504d_accel_v134_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 504) - _mean(deferredrev, 1008), _mean(deferredrev, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_504d_accel_v135_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 504) - _mean(deferredrev, 1008), _mean(deferredrev, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_21d_accel_v136_signal(deferredrev):
    base = _std(deferredrev, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_21d_accel_v137_signal(deferredrev):
    base = _std(deferredrev, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_21d_accel_v138_signal(deferredrev):
    base = _std(deferredrev, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_63d_accel_v139_signal(deferredrev):
    base = _std(deferredrev, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_63d_accel_v140_signal(deferredrev):
    base = _std(deferredrev, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_63d_accel_v141_signal(deferredrev):
    base = _std(deferredrev, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_126d_accel_v142_signal(deferredrev):
    base = _std(deferredrev, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_126d_accel_v143_signal(deferredrev):
    base = _std(deferredrev, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_126d_accel_v144_signal(deferredrev):
    base = _std(deferredrev, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_252d_accel_v145_signal(deferredrev):
    base = _std(deferredrev, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_252d_accel_v146_signal(deferredrev):
    base = _std(deferredrev, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_252d_accel_v147_signal(deferredrev):
    base = _std(deferredrev, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_504d_accel_v148_signal(deferredrev):
    base = _std(deferredrev, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_504d_accel_v149_signal(deferredrev):
    base = _std(deferredrev, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_504d_accel_v150_signal(deferredrev):
    base = _std(deferredrev, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

