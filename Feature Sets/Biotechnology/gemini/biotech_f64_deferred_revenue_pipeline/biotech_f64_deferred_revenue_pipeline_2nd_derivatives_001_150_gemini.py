
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_21d_slope_v001_signal(deferredrev):
    base = _mean(deferredrev, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_21d_slope_v002_signal(deferredrev):
    base = _mean(deferredrev, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_21d_slope_v003_signal(deferredrev):
    base = _mean(deferredrev, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_63d_slope_v004_signal(deferredrev):
    base = _mean(deferredrev, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_63d_slope_v005_signal(deferredrev):
    base = _mean(deferredrev, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_63d_slope_v006_signal(deferredrev):
    base = _mean(deferredrev, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_126d_slope_v007_signal(deferredrev):
    base = _mean(deferredrev, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_126d_slope_v008_signal(deferredrev):
    base = _mean(deferredrev, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_126d_slope_v009_signal(deferredrev):
    base = _mean(deferredrev, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_252d_slope_v010_signal(deferredrev):
    base = _mean(deferredrev, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_252d_slope_v011_signal(deferredrev):
    base = _mean(deferredrev, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_252d_slope_v012_signal(deferredrev):
    base = _mean(deferredrev, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_504d_slope_v013_signal(deferredrev):
    base = _mean(deferredrev, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_504d_slope_v014_signal(deferredrev):
    base = _mean(deferredrev, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_raw_504d_slope_v015_signal(deferredrev):
    base = _mean(deferredrev, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_21d_slope_v016_signal(deferredrev):
    base = _mean(_log(deferredrev), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_21d_slope_v017_signal(deferredrev):
    base = _mean(_log(deferredrev), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_21d_slope_v018_signal(deferredrev):
    base = _mean(_log(deferredrev), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_63d_slope_v019_signal(deferredrev):
    base = _mean(_log(deferredrev), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_63d_slope_v020_signal(deferredrev):
    base = _mean(_log(deferredrev), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_63d_slope_v021_signal(deferredrev):
    base = _mean(_log(deferredrev), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_126d_slope_v022_signal(deferredrev):
    base = _mean(_log(deferredrev), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_126d_slope_v023_signal(deferredrev):
    base = _mean(_log(deferredrev), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_126d_slope_v024_signal(deferredrev):
    base = _mean(_log(deferredrev), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_252d_slope_v025_signal(deferredrev):
    base = _mean(_log(deferredrev), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_252d_slope_v026_signal(deferredrev):
    base = _mean(_log(deferredrev), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_252d_slope_v027_signal(deferredrev):
    base = _mean(_log(deferredrev), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_504d_slope_v028_signal(deferredrev):
    base = _mean(_log(deferredrev), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_504d_slope_v029_signal(deferredrev):
    base = _mean(_log(deferredrev), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_log_504d_slope_v030_signal(deferredrev):
    base = _mean(_log(deferredrev), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_21d_slope_v031_signal(deferredrev):
    base = _z(deferredrev, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_21d_slope_v032_signal(deferredrev):
    base = _z(deferredrev, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_21d_slope_v033_signal(deferredrev):
    base = _z(deferredrev, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_63d_slope_v034_signal(deferredrev):
    base = _z(deferredrev, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_63d_slope_v035_signal(deferredrev):
    base = _z(deferredrev, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_63d_slope_v036_signal(deferredrev):
    base = _z(deferredrev, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_126d_slope_v037_signal(deferredrev):
    base = _z(deferredrev, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_126d_slope_v038_signal(deferredrev):
    base = _z(deferredrev, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_126d_slope_v039_signal(deferredrev):
    base = _z(deferredrev, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_252d_slope_v040_signal(deferredrev):
    base = _z(deferredrev, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_252d_slope_v041_signal(deferredrev):
    base = _z(deferredrev, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_252d_slope_v042_signal(deferredrev):
    base = _z(deferredrev, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_504d_slope_v043_signal(deferredrev):
    base = _z(deferredrev, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_504d_slope_v044_signal(deferredrev):
    base = _z(deferredrev, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_z_504d_slope_v045_signal(deferredrev):
    base = _z(deferredrev, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_21d_slope_v046_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_21d_slope_v047_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_21d_slope_v048_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_63d_slope_v049_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_63d_slope_v050_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_63d_slope_v051_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_126d_slope_v052_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_126d_slope_v053_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_126d_slope_v054_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_252d_slope_v055_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_252d_slope_v056_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_252d_slope_v057_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_504d_slope_v058_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_504d_slope_v059_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_ps_504d_slope_v060_signal(deferredrev, sharesbas):
    base = _safe_div(_mean(deferredrev, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_21d_slope_v061_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_21d_slope_v062_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_21d_slope_v063_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_63d_slope_v064_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_63d_slope_v065_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_63d_slope_v066_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_126d_slope_v067_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_126d_slope_v068_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_126d_slope_v069_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_252d_slope_v070_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_252d_slope_v071_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_252d_slope_v072_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_504d_slope_v073_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_504d_slope_v074_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_asset_scaled_504d_slope_v075_signal(deferredrev, assets):
    base = _safe_div(_mean(deferredrev, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_21d_slope_v076_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_21d_slope_v077_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_21d_slope_v078_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_63d_slope_v079_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_63d_slope_v080_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_63d_slope_v081_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_126d_slope_v082_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_126d_slope_v083_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_126d_slope_v084_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_252d_slope_v085_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_252d_slope_v086_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_252d_slope_v087_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_504d_slope_v088_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_504d_slope_v089_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mcap_scaled_504d_slope_v090_signal(deferredrev, marketcap):
    base = _safe_div(_mean(deferredrev, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_21d_slope_v091_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(21).min(), deferredrev.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_21d_slope_v092_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(21).min(), deferredrev.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_21d_slope_v093_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(21).min(), deferredrev.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_63d_slope_v094_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(63).min(), deferredrev.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_63d_slope_v095_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(63).min(), deferredrev.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_63d_slope_v096_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(63).min(), deferredrev.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_126d_slope_v097_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(126).min(), deferredrev.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_126d_slope_v098_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(126).min(), deferredrev.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_126d_slope_v099_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(126).min(), deferredrev.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_252d_slope_v100_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(252).min(), deferredrev.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_252d_slope_v101_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(252).min(), deferredrev.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_252d_slope_v102_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(252).min(), deferredrev.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_504d_slope_v103_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(504).min(), deferredrev.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_504d_slope_v104_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(504).min(), deferredrev.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_low_504d_slope_v105_signal(deferredrev):
    base = _safe_div(deferredrev - deferredrev.rolling(504).min(), deferredrev.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_21d_slope_v106_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(21).max() - deferredrev, deferredrev.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_21d_slope_v107_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(21).max() - deferredrev, deferredrev.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_21d_slope_v108_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(21).max() - deferredrev, deferredrev.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_63d_slope_v109_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(63).max() - deferredrev, deferredrev.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_63d_slope_v110_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(63).max() - deferredrev, deferredrev.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_63d_slope_v111_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(63).max() - deferredrev, deferredrev.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_126d_slope_v112_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(126).max() - deferredrev, deferredrev.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_126d_slope_v113_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(126).max() - deferredrev, deferredrev.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_126d_slope_v114_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(126).max() - deferredrev, deferredrev.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_252d_slope_v115_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(252).max() - deferredrev, deferredrev.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_252d_slope_v116_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(252).max() - deferredrev, deferredrev.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_252d_slope_v117_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(252).max() - deferredrev, deferredrev.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_504d_slope_v118_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(504).max() - deferredrev, deferredrev.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_504d_slope_v119_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(504).max() - deferredrev, deferredrev.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_dist_high_504d_slope_v120_signal(deferredrev):
    base = _safe_div(deferredrev.rolling(504).max() - deferredrev, deferredrev.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_21d_slope_v121_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 21) - _mean(deferredrev, 42), _mean(deferredrev, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_21d_slope_v122_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 21) - _mean(deferredrev, 42), _mean(deferredrev, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_21d_slope_v123_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 21) - _mean(deferredrev, 42), _mean(deferredrev, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_63d_slope_v124_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 63) - _mean(deferredrev, 126), _mean(deferredrev, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_63d_slope_v125_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 63) - _mean(deferredrev, 126), _mean(deferredrev, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_63d_slope_v126_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 63) - _mean(deferredrev, 126), _mean(deferredrev, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_126d_slope_v127_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 126) - _mean(deferredrev, 252), _mean(deferredrev, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_126d_slope_v128_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 126) - _mean(deferredrev, 252), _mean(deferredrev, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_126d_slope_v129_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 126) - _mean(deferredrev, 252), _mean(deferredrev, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_252d_slope_v130_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 252) - _mean(deferredrev, 504), _mean(deferredrev, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_252d_slope_v131_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 252) - _mean(deferredrev, 504), _mean(deferredrev, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_252d_slope_v132_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 252) - _mean(deferredrev, 504), _mean(deferredrev, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_504d_slope_v133_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 504) - _mean(deferredrev, 1008), _mean(deferredrev, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_504d_slope_v134_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 504) - _mean(deferredrev, 1008), _mean(deferredrev, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_mom_504d_slope_v135_signal(deferredrev):
    base = _safe_div(_mean(deferredrev, 504) - _mean(deferredrev, 1008), _mean(deferredrev, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_21d_slope_v136_signal(deferredrev):
    base = _std(deferredrev, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_21d_slope_v137_signal(deferredrev):
    base = _std(deferredrev, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_21d_slope_v138_signal(deferredrev):
    base = _std(deferredrev, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_63d_slope_v139_signal(deferredrev):
    base = _std(deferredrev, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_63d_slope_v140_signal(deferredrev):
    base = _std(deferredrev, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_63d_slope_v141_signal(deferredrev):
    base = _std(deferredrev, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_126d_slope_v142_signal(deferredrev):
    base = _std(deferredrev, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_126d_slope_v143_signal(deferredrev):
    base = _std(deferredrev, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_126d_slope_v144_signal(deferredrev):
    base = _std(deferredrev, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_252d_slope_v145_signal(deferredrev):
    base = _std(deferredrev, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_252d_slope_v146_signal(deferredrev):
    base = _std(deferredrev, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_252d_slope_v147_signal(deferredrev):
    base = _std(deferredrev, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_504d_slope_v148_signal(deferredrev):
    base = _std(deferredrev, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_504d_slope_v149_signal(deferredrev):
    base = _std(deferredrev, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol deferredrev
def gm_f64_biotech_f64_deferred_revenue_pipeline_vol_504d_slope_v150_signal(deferredrev):
    base = _std(deferredrev, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

