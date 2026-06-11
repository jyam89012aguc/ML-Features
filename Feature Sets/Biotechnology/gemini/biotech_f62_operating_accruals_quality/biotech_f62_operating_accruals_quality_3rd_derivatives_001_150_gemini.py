
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_21d_accel_v001_signal(assetsc):
    base = _mean(assetsc, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_21d_accel_v002_signal(assetsc):
    base = _mean(assetsc, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_21d_accel_v003_signal(assetsc):
    base = _mean(assetsc, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_63d_accel_v004_signal(assetsc):
    base = _mean(assetsc, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_63d_accel_v005_signal(assetsc):
    base = _mean(assetsc, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_63d_accel_v006_signal(assetsc):
    base = _mean(assetsc, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_126d_accel_v007_signal(assetsc):
    base = _mean(assetsc, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_126d_accel_v008_signal(assetsc):
    base = _mean(assetsc, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_126d_accel_v009_signal(assetsc):
    base = _mean(assetsc, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_252d_accel_v010_signal(assetsc):
    base = _mean(assetsc, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_252d_accel_v011_signal(assetsc):
    base = _mean(assetsc, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_252d_accel_v012_signal(assetsc):
    base = _mean(assetsc, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_504d_accel_v013_signal(assetsc):
    base = _mean(assetsc, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_504d_accel_v014_signal(assetsc):
    base = _mean(assetsc, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_504d_accel_v015_signal(assetsc):
    base = _mean(assetsc, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_21d_accel_v016_signal(assetsc):
    base = _mean(_log(assetsc), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_21d_accel_v017_signal(assetsc):
    base = _mean(_log(assetsc), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_21d_accel_v018_signal(assetsc):
    base = _mean(_log(assetsc), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_63d_accel_v019_signal(assetsc):
    base = _mean(_log(assetsc), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_63d_accel_v020_signal(assetsc):
    base = _mean(_log(assetsc), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_63d_accel_v021_signal(assetsc):
    base = _mean(_log(assetsc), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_126d_accel_v022_signal(assetsc):
    base = _mean(_log(assetsc), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_126d_accel_v023_signal(assetsc):
    base = _mean(_log(assetsc), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_126d_accel_v024_signal(assetsc):
    base = _mean(_log(assetsc), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_252d_accel_v025_signal(assetsc):
    base = _mean(_log(assetsc), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_252d_accel_v026_signal(assetsc):
    base = _mean(_log(assetsc), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_252d_accel_v027_signal(assetsc):
    base = _mean(_log(assetsc), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_504d_accel_v028_signal(assetsc):
    base = _mean(_log(assetsc), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_504d_accel_v029_signal(assetsc):
    base = _mean(_log(assetsc), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_504d_accel_v030_signal(assetsc):
    base = _mean(_log(assetsc), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_21d_accel_v031_signal(assetsc):
    base = _z(assetsc, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_21d_accel_v032_signal(assetsc):
    base = _z(assetsc, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_21d_accel_v033_signal(assetsc):
    base = _z(assetsc, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_63d_accel_v034_signal(assetsc):
    base = _z(assetsc, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_63d_accel_v035_signal(assetsc):
    base = _z(assetsc, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_63d_accel_v036_signal(assetsc):
    base = _z(assetsc, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_126d_accel_v037_signal(assetsc):
    base = _z(assetsc, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_126d_accel_v038_signal(assetsc):
    base = _z(assetsc, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_126d_accel_v039_signal(assetsc):
    base = _z(assetsc, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_252d_accel_v040_signal(assetsc):
    base = _z(assetsc, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_252d_accel_v041_signal(assetsc):
    base = _z(assetsc, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_252d_accel_v042_signal(assetsc):
    base = _z(assetsc, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_504d_accel_v043_signal(assetsc):
    base = _z(assetsc, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_504d_accel_v044_signal(assetsc):
    base = _z(assetsc, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_504d_accel_v045_signal(assetsc):
    base = _z(assetsc, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_21d_accel_v046_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_21d_accel_v047_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_21d_accel_v048_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_63d_accel_v049_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_63d_accel_v050_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_63d_accel_v051_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_126d_accel_v052_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_126d_accel_v053_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_126d_accel_v054_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_252d_accel_v055_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_252d_accel_v056_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_252d_accel_v057_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_504d_accel_v058_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_504d_accel_v059_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_504d_accel_v060_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_21d_accel_v061_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_21d_accel_v062_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_21d_accel_v063_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_63d_accel_v064_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_63d_accel_v065_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_63d_accel_v066_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_126d_accel_v067_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_126d_accel_v068_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_126d_accel_v069_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_252d_accel_v070_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_252d_accel_v071_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_252d_accel_v072_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_504d_accel_v073_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_504d_accel_v074_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_504d_accel_v075_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_21d_accel_v076_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_21d_accel_v077_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_21d_accel_v078_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_63d_accel_v079_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_63d_accel_v080_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_63d_accel_v081_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_126d_accel_v082_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_126d_accel_v083_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_126d_accel_v084_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_252d_accel_v085_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_252d_accel_v086_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_252d_accel_v087_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_504d_accel_v088_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_504d_accel_v089_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_504d_accel_v090_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_21d_accel_v091_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(21).min(), assetsc.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_21d_accel_v092_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(21).min(), assetsc.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_21d_accel_v093_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(21).min(), assetsc.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_63d_accel_v094_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(63).min(), assetsc.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_63d_accel_v095_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(63).min(), assetsc.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_63d_accel_v096_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(63).min(), assetsc.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_126d_accel_v097_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(126).min(), assetsc.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_126d_accel_v098_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(126).min(), assetsc.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_126d_accel_v099_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(126).min(), assetsc.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_252d_accel_v100_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(252).min(), assetsc.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_252d_accel_v101_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(252).min(), assetsc.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_252d_accel_v102_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(252).min(), assetsc.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_504d_accel_v103_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(504).min(), assetsc.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_504d_accel_v104_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(504).min(), assetsc.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_504d_accel_v105_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(504).min(), assetsc.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_21d_accel_v106_signal(assetsc):
    base = _safe_div(assetsc.rolling(21).max() - assetsc, assetsc.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_21d_accel_v107_signal(assetsc):
    base = _safe_div(assetsc.rolling(21).max() - assetsc, assetsc.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_21d_accel_v108_signal(assetsc):
    base = _safe_div(assetsc.rolling(21).max() - assetsc, assetsc.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_63d_accel_v109_signal(assetsc):
    base = _safe_div(assetsc.rolling(63).max() - assetsc, assetsc.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_63d_accel_v110_signal(assetsc):
    base = _safe_div(assetsc.rolling(63).max() - assetsc, assetsc.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_63d_accel_v111_signal(assetsc):
    base = _safe_div(assetsc.rolling(63).max() - assetsc, assetsc.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_126d_accel_v112_signal(assetsc):
    base = _safe_div(assetsc.rolling(126).max() - assetsc, assetsc.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_126d_accel_v113_signal(assetsc):
    base = _safe_div(assetsc.rolling(126).max() - assetsc, assetsc.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_126d_accel_v114_signal(assetsc):
    base = _safe_div(assetsc.rolling(126).max() - assetsc, assetsc.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_252d_accel_v115_signal(assetsc):
    base = _safe_div(assetsc.rolling(252).max() - assetsc, assetsc.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_252d_accel_v116_signal(assetsc):
    base = _safe_div(assetsc.rolling(252).max() - assetsc, assetsc.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_252d_accel_v117_signal(assetsc):
    base = _safe_div(assetsc.rolling(252).max() - assetsc, assetsc.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_504d_accel_v118_signal(assetsc):
    base = _safe_div(assetsc.rolling(504).max() - assetsc, assetsc.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_504d_accel_v119_signal(assetsc):
    base = _safe_div(assetsc.rolling(504).max() - assetsc, assetsc.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_504d_accel_v120_signal(assetsc):
    base = _safe_div(assetsc.rolling(504).max() - assetsc, assetsc.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_21d_accel_v121_signal(assetsc):
    base = _safe_div(_mean(assetsc, 21) - _mean(assetsc, 42), _mean(assetsc, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_21d_accel_v122_signal(assetsc):
    base = _safe_div(_mean(assetsc, 21) - _mean(assetsc, 42), _mean(assetsc, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_21d_accel_v123_signal(assetsc):
    base = _safe_div(_mean(assetsc, 21) - _mean(assetsc, 42), _mean(assetsc, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_63d_accel_v124_signal(assetsc):
    base = _safe_div(_mean(assetsc, 63) - _mean(assetsc, 126), _mean(assetsc, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_63d_accel_v125_signal(assetsc):
    base = _safe_div(_mean(assetsc, 63) - _mean(assetsc, 126), _mean(assetsc, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_63d_accel_v126_signal(assetsc):
    base = _safe_div(_mean(assetsc, 63) - _mean(assetsc, 126), _mean(assetsc, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_126d_accel_v127_signal(assetsc):
    base = _safe_div(_mean(assetsc, 126) - _mean(assetsc, 252), _mean(assetsc, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_126d_accel_v128_signal(assetsc):
    base = _safe_div(_mean(assetsc, 126) - _mean(assetsc, 252), _mean(assetsc, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_126d_accel_v129_signal(assetsc):
    base = _safe_div(_mean(assetsc, 126) - _mean(assetsc, 252), _mean(assetsc, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_252d_accel_v130_signal(assetsc):
    base = _safe_div(_mean(assetsc, 252) - _mean(assetsc, 504), _mean(assetsc, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_252d_accel_v131_signal(assetsc):
    base = _safe_div(_mean(assetsc, 252) - _mean(assetsc, 504), _mean(assetsc, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_252d_accel_v132_signal(assetsc):
    base = _safe_div(_mean(assetsc, 252) - _mean(assetsc, 504), _mean(assetsc, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_504d_accel_v133_signal(assetsc):
    base = _safe_div(_mean(assetsc, 504) - _mean(assetsc, 1008), _mean(assetsc, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_504d_accel_v134_signal(assetsc):
    base = _safe_div(_mean(assetsc, 504) - _mean(assetsc, 1008), _mean(assetsc, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_504d_accel_v135_signal(assetsc):
    base = _safe_div(_mean(assetsc, 504) - _mean(assetsc, 1008), _mean(assetsc, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_21d_accel_v136_signal(assetsc):
    base = _std(assetsc, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_21d_accel_v137_signal(assetsc):
    base = _std(assetsc, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_21d_accel_v138_signal(assetsc):
    base = _std(assetsc, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_63d_accel_v139_signal(assetsc):
    base = _std(assetsc, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_63d_accel_v140_signal(assetsc):
    base = _std(assetsc, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_63d_accel_v141_signal(assetsc):
    base = _std(assetsc, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_126d_accel_v142_signal(assetsc):
    base = _std(assetsc, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_126d_accel_v143_signal(assetsc):
    base = _std(assetsc, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_126d_accel_v144_signal(assetsc):
    base = _std(assetsc, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_252d_accel_v145_signal(assetsc):
    base = _std(assetsc, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_252d_accel_v146_signal(assetsc):
    base = _std(assetsc, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_252d_accel_v147_signal(assetsc):
    base = _std(assetsc, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_504d_accel_v148_signal(assetsc):
    base = _std(assetsc, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_504d_accel_v149_signal(assetsc):
    base = _std(assetsc, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_504d_accel_v150_signal(assetsc):
    base = _std(assetsc, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

