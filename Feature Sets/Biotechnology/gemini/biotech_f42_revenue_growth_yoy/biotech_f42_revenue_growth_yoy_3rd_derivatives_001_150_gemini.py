
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw revenue
def gm_f42_biotech_f42_revenue_growth_yoy_raw_21d_accel_v001_signal(revenue):
    base = _mean(revenue, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw revenue
def gm_f42_biotech_f42_revenue_growth_yoy_raw_21d_accel_v002_signal(revenue):
    base = _mean(revenue, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw revenue
def gm_f42_biotech_f42_revenue_growth_yoy_raw_21d_accel_v003_signal(revenue):
    base = _mean(revenue, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw revenue
def gm_f42_biotech_f42_revenue_growth_yoy_raw_63d_accel_v004_signal(revenue):
    base = _mean(revenue, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw revenue
def gm_f42_biotech_f42_revenue_growth_yoy_raw_63d_accel_v005_signal(revenue):
    base = _mean(revenue, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw revenue
def gm_f42_biotech_f42_revenue_growth_yoy_raw_63d_accel_v006_signal(revenue):
    base = _mean(revenue, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw revenue
def gm_f42_biotech_f42_revenue_growth_yoy_raw_126d_accel_v007_signal(revenue):
    base = _mean(revenue, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw revenue
def gm_f42_biotech_f42_revenue_growth_yoy_raw_126d_accel_v008_signal(revenue):
    base = _mean(revenue, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw revenue
def gm_f42_biotech_f42_revenue_growth_yoy_raw_126d_accel_v009_signal(revenue):
    base = _mean(revenue, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw revenue
def gm_f42_biotech_f42_revenue_growth_yoy_raw_252d_accel_v010_signal(revenue):
    base = _mean(revenue, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw revenue
def gm_f42_biotech_f42_revenue_growth_yoy_raw_252d_accel_v011_signal(revenue):
    base = _mean(revenue, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw revenue
def gm_f42_biotech_f42_revenue_growth_yoy_raw_252d_accel_v012_signal(revenue):
    base = _mean(revenue, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw revenue
def gm_f42_biotech_f42_revenue_growth_yoy_raw_504d_accel_v013_signal(revenue):
    base = _mean(revenue, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw revenue
def gm_f42_biotech_f42_revenue_growth_yoy_raw_504d_accel_v014_signal(revenue):
    base = _mean(revenue, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw revenue
def gm_f42_biotech_f42_revenue_growth_yoy_raw_504d_accel_v015_signal(revenue):
    base = _mean(revenue, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log revenue
def gm_f42_biotech_f42_revenue_growth_yoy_log_21d_accel_v016_signal(revenue):
    base = _mean(_log(revenue), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log revenue
def gm_f42_biotech_f42_revenue_growth_yoy_log_21d_accel_v017_signal(revenue):
    base = _mean(_log(revenue), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log revenue
def gm_f42_biotech_f42_revenue_growth_yoy_log_21d_accel_v018_signal(revenue):
    base = _mean(_log(revenue), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log revenue
def gm_f42_biotech_f42_revenue_growth_yoy_log_63d_accel_v019_signal(revenue):
    base = _mean(_log(revenue), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log revenue
def gm_f42_biotech_f42_revenue_growth_yoy_log_63d_accel_v020_signal(revenue):
    base = _mean(_log(revenue), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log revenue
def gm_f42_biotech_f42_revenue_growth_yoy_log_63d_accel_v021_signal(revenue):
    base = _mean(_log(revenue), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log revenue
def gm_f42_biotech_f42_revenue_growth_yoy_log_126d_accel_v022_signal(revenue):
    base = _mean(_log(revenue), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log revenue
def gm_f42_biotech_f42_revenue_growth_yoy_log_126d_accel_v023_signal(revenue):
    base = _mean(_log(revenue), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log revenue
def gm_f42_biotech_f42_revenue_growth_yoy_log_126d_accel_v024_signal(revenue):
    base = _mean(_log(revenue), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log revenue
def gm_f42_biotech_f42_revenue_growth_yoy_log_252d_accel_v025_signal(revenue):
    base = _mean(_log(revenue), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log revenue
def gm_f42_biotech_f42_revenue_growth_yoy_log_252d_accel_v026_signal(revenue):
    base = _mean(_log(revenue), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log revenue
def gm_f42_biotech_f42_revenue_growth_yoy_log_252d_accel_v027_signal(revenue):
    base = _mean(_log(revenue), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log revenue
def gm_f42_biotech_f42_revenue_growth_yoy_log_504d_accel_v028_signal(revenue):
    base = _mean(_log(revenue), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log revenue
def gm_f42_biotech_f42_revenue_growth_yoy_log_504d_accel_v029_signal(revenue):
    base = _mean(_log(revenue), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log revenue
def gm_f42_biotech_f42_revenue_growth_yoy_log_504d_accel_v030_signal(revenue):
    base = _mean(_log(revenue), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z revenue
def gm_f42_biotech_f42_revenue_growth_yoy_z_21d_accel_v031_signal(revenue):
    base = _z(revenue, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z revenue
def gm_f42_biotech_f42_revenue_growth_yoy_z_21d_accel_v032_signal(revenue):
    base = _z(revenue, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z revenue
def gm_f42_biotech_f42_revenue_growth_yoy_z_21d_accel_v033_signal(revenue):
    base = _z(revenue, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z revenue
def gm_f42_biotech_f42_revenue_growth_yoy_z_63d_accel_v034_signal(revenue):
    base = _z(revenue, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z revenue
def gm_f42_biotech_f42_revenue_growth_yoy_z_63d_accel_v035_signal(revenue):
    base = _z(revenue, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z revenue
def gm_f42_biotech_f42_revenue_growth_yoy_z_63d_accel_v036_signal(revenue):
    base = _z(revenue, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z revenue
def gm_f42_biotech_f42_revenue_growth_yoy_z_126d_accel_v037_signal(revenue):
    base = _z(revenue, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z revenue
def gm_f42_biotech_f42_revenue_growth_yoy_z_126d_accel_v038_signal(revenue):
    base = _z(revenue, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z revenue
def gm_f42_biotech_f42_revenue_growth_yoy_z_126d_accel_v039_signal(revenue):
    base = _z(revenue, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z revenue
def gm_f42_biotech_f42_revenue_growth_yoy_z_252d_accel_v040_signal(revenue):
    base = _z(revenue, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z revenue
def gm_f42_biotech_f42_revenue_growth_yoy_z_252d_accel_v041_signal(revenue):
    base = _z(revenue, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z revenue
def gm_f42_biotech_f42_revenue_growth_yoy_z_252d_accel_v042_signal(revenue):
    base = _z(revenue, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z revenue
def gm_f42_biotech_f42_revenue_growth_yoy_z_504d_accel_v043_signal(revenue):
    base = _z(revenue, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z revenue
def gm_f42_biotech_f42_revenue_growth_yoy_z_504d_accel_v044_signal(revenue):
    base = _z(revenue, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z revenue
def gm_f42_biotech_f42_revenue_growth_yoy_z_504d_accel_v045_signal(revenue):
    base = _z(revenue, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps revenue
def gm_f42_biotech_f42_revenue_growth_yoy_ps_21d_accel_v046_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps revenue
def gm_f42_biotech_f42_revenue_growth_yoy_ps_21d_accel_v047_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps revenue
def gm_f42_biotech_f42_revenue_growth_yoy_ps_21d_accel_v048_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps revenue
def gm_f42_biotech_f42_revenue_growth_yoy_ps_63d_accel_v049_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps revenue
def gm_f42_biotech_f42_revenue_growth_yoy_ps_63d_accel_v050_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps revenue
def gm_f42_biotech_f42_revenue_growth_yoy_ps_63d_accel_v051_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps revenue
def gm_f42_biotech_f42_revenue_growth_yoy_ps_126d_accel_v052_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps revenue
def gm_f42_biotech_f42_revenue_growth_yoy_ps_126d_accel_v053_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps revenue
def gm_f42_biotech_f42_revenue_growth_yoy_ps_126d_accel_v054_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps revenue
def gm_f42_biotech_f42_revenue_growth_yoy_ps_252d_accel_v055_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps revenue
def gm_f42_biotech_f42_revenue_growth_yoy_ps_252d_accel_v056_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps revenue
def gm_f42_biotech_f42_revenue_growth_yoy_ps_252d_accel_v057_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps revenue
def gm_f42_biotech_f42_revenue_growth_yoy_ps_504d_accel_v058_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps revenue
def gm_f42_biotech_f42_revenue_growth_yoy_ps_504d_accel_v059_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps revenue
def gm_f42_biotech_f42_revenue_growth_yoy_ps_504d_accel_v060_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_asset_scaled_21d_accel_v061_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_asset_scaled_21d_accel_v062_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_asset_scaled_21d_accel_v063_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_asset_scaled_63d_accel_v064_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_asset_scaled_63d_accel_v065_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_asset_scaled_63d_accel_v066_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_asset_scaled_126d_accel_v067_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_asset_scaled_126d_accel_v068_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_asset_scaled_126d_accel_v069_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_asset_scaled_252d_accel_v070_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_asset_scaled_252d_accel_v071_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_asset_scaled_252d_accel_v072_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_asset_scaled_504d_accel_v073_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_asset_scaled_504d_accel_v074_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_asset_scaled_504d_accel_v075_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mcap_scaled_21d_accel_v076_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mcap_scaled_21d_accel_v077_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mcap_scaled_21d_accel_v078_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mcap_scaled_63d_accel_v079_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mcap_scaled_63d_accel_v080_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mcap_scaled_63d_accel_v081_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mcap_scaled_126d_accel_v082_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mcap_scaled_126d_accel_v083_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mcap_scaled_126d_accel_v084_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mcap_scaled_252d_accel_v085_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mcap_scaled_252d_accel_v086_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mcap_scaled_252d_accel_v087_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mcap_scaled_504d_accel_v088_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mcap_scaled_504d_accel_v089_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mcap_scaled_504d_accel_v090_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_low_21d_accel_v091_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(21).min(), revenue.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_low_21d_accel_v092_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(21).min(), revenue.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_low_21d_accel_v093_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(21).min(), revenue.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_low_63d_accel_v094_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(63).min(), revenue.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_low_63d_accel_v095_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(63).min(), revenue.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_low_63d_accel_v096_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(63).min(), revenue.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_low_126d_accel_v097_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(126).min(), revenue.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_low_126d_accel_v098_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(126).min(), revenue.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_low_126d_accel_v099_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(126).min(), revenue.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_low_252d_accel_v100_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(252).min(), revenue.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_low_252d_accel_v101_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(252).min(), revenue.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_low_252d_accel_v102_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(252).min(), revenue.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_low_504d_accel_v103_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(504).min(), revenue.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_low_504d_accel_v104_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(504).min(), revenue.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_low_504d_accel_v105_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(504).min(), revenue.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_high_21d_accel_v106_signal(revenue):
    base = _safe_div(revenue.rolling(21).max() - revenue, revenue.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_high_21d_accel_v107_signal(revenue):
    base = _safe_div(revenue.rolling(21).max() - revenue, revenue.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_high_21d_accel_v108_signal(revenue):
    base = _safe_div(revenue.rolling(21).max() - revenue, revenue.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_high_63d_accel_v109_signal(revenue):
    base = _safe_div(revenue.rolling(63).max() - revenue, revenue.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_high_63d_accel_v110_signal(revenue):
    base = _safe_div(revenue.rolling(63).max() - revenue, revenue.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_high_63d_accel_v111_signal(revenue):
    base = _safe_div(revenue.rolling(63).max() - revenue, revenue.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_high_126d_accel_v112_signal(revenue):
    base = _safe_div(revenue.rolling(126).max() - revenue, revenue.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_high_126d_accel_v113_signal(revenue):
    base = _safe_div(revenue.rolling(126).max() - revenue, revenue.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_high_126d_accel_v114_signal(revenue):
    base = _safe_div(revenue.rolling(126).max() - revenue, revenue.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_high_252d_accel_v115_signal(revenue):
    base = _safe_div(revenue.rolling(252).max() - revenue, revenue.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_high_252d_accel_v116_signal(revenue):
    base = _safe_div(revenue.rolling(252).max() - revenue, revenue.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_high_252d_accel_v117_signal(revenue):
    base = _safe_div(revenue.rolling(252).max() - revenue, revenue.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_high_504d_accel_v118_signal(revenue):
    base = _safe_div(revenue.rolling(504).max() - revenue, revenue.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_high_504d_accel_v119_signal(revenue):
    base = _safe_div(revenue.rolling(504).max() - revenue, revenue.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high revenue
def gm_f42_biotech_f42_revenue_growth_yoy_dist_high_504d_accel_v120_signal(revenue):
    base = _safe_div(revenue.rolling(504).max() - revenue, revenue.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mom_21d_accel_v121_signal(revenue):
    base = _safe_div(_mean(revenue, 21) - _mean(revenue, 42), _mean(revenue, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mom_21d_accel_v122_signal(revenue):
    base = _safe_div(_mean(revenue, 21) - _mean(revenue, 42), _mean(revenue, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mom_21d_accel_v123_signal(revenue):
    base = _safe_div(_mean(revenue, 21) - _mean(revenue, 42), _mean(revenue, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mom_63d_accel_v124_signal(revenue):
    base = _safe_div(_mean(revenue, 63) - _mean(revenue, 126), _mean(revenue, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mom_63d_accel_v125_signal(revenue):
    base = _safe_div(_mean(revenue, 63) - _mean(revenue, 126), _mean(revenue, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mom_63d_accel_v126_signal(revenue):
    base = _safe_div(_mean(revenue, 63) - _mean(revenue, 126), _mean(revenue, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mom_126d_accel_v127_signal(revenue):
    base = _safe_div(_mean(revenue, 126) - _mean(revenue, 252), _mean(revenue, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mom_126d_accel_v128_signal(revenue):
    base = _safe_div(_mean(revenue, 126) - _mean(revenue, 252), _mean(revenue, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mom_126d_accel_v129_signal(revenue):
    base = _safe_div(_mean(revenue, 126) - _mean(revenue, 252), _mean(revenue, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mom_252d_accel_v130_signal(revenue):
    base = _safe_div(_mean(revenue, 252) - _mean(revenue, 504), _mean(revenue, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mom_252d_accel_v131_signal(revenue):
    base = _safe_div(_mean(revenue, 252) - _mean(revenue, 504), _mean(revenue, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mom_252d_accel_v132_signal(revenue):
    base = _safe_div(_mean(revenue, 252) - _mean(revenue, 504), _mean(revenue, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mom_504d_accel_v133_signal(revenue):
    base = _safe_div(_mean(revenue, 504) - _mean(revenue, 1008), _mean(revenue, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mom_504d_accel_v134_signal(revenue):
    base = _safe_div(_mean(revenue, 504) - _mean(revenue, 1008), _mean(revenue, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom revenue
def gm_f42_biotech_f42_revenue_growth_yoy_mom_504d_accel_v135_signal(revenue):
    base = _safe_div(_mean(revenue, 504) - _mean(revenue, 1008), _mean(revenue, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol revenue
def gm_f42_biotech_f42_revenue_growth_yoy_vol_21d_accel_v136_signal(revenue):
    base = _std(revenue, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol revenue
def gm_f42_biotech_f42_revenue_growth_yoy_vol_21d_accel_v137_signal(revenue):
    base = _std(revenue, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol revenue
def gm_f42_biotech_f42_revenue_growth_yoy_vol_21d_accel_v138_signal(revenue):
    base = _std(revenue, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol revenue
def gm_f42_biotech_f42_revenue_growth_yoy_vol_63d_accel_v139_signal(revenue):
    base = _std(revenue, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol revenue
def gm_f42_biotech_f42_revenue_growth_yoy_vol_63d_accel_v140_signal(revenue):
    base = _std(revenue, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol revenue
def gm_f42_biotech_f42_revenue_growth_yoy_vol_63d_accel_v141_signal(revenue):
    base = _std(revenue, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol revenue
def gm_f42_biotech_f42_revenue_growth_yoy_vol_126d_accel_v142_signal(revenue):
    base = _std(revenue, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol revenue
def gm_f42_biotech_f42_revenue_growth_yoy_vol_126d_accel_v143_signal(revenue):
    base = _std(revenue, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol revenue
def gm_f42_biotech_f42_revenue_growth_yoy_vol_126d_accel_v144_signal(revenue):
    base = _std(revenue, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol revenue
def gm_f42_biotech_f42_revenue_growth_yoy_vol_252d_accel_v145_signal(revenue):
    base = _std(revenue, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol revenue
def gm_f42_biotech_f42_revenue_growth_yoy_vol_252d_accel_v146_signal(revenue):
    base = _std(revenue, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol revenue
def gm_f42_biotech_f42_revenue_growth_yoy_vol_252d_accel_v147_signal(revenue):
    base = _std(revenue, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol revenue
def gm_f42_biotech_f42_revenue_growth_yoy_vol_504d_accel_v148_signal(revenue):
    base = _std(revenue, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol revenue
def gm_f42_biotech_f42_revenue_growth_yoy_vol_504d_accel_v149_signal(revenue):
    base = _std(revenue, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol revenue
def gm_f42_biotech_f42_revenue_growth_yoy_vol_504d_accel_v150_signal(revenue):
    base = _std(revenue, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

