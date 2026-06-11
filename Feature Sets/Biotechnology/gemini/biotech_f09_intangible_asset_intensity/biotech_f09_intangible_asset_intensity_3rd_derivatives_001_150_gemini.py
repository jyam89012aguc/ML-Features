
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_21d_accel_v001_signal(intangibles):
    base = _mean(intangibles, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_21d_accel_v002_signal(intangibles):
    base = _mean(intangibles, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_21d_accel_v003_signal(intangibles):
    base = _mean(intangibles, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_63d_accel_v004_signal(intangibles):
    base = _mean(intangibles, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_63d_accel_v005_signal(intangibles):
    base = _mean(intangibles, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_63d_accel_v006_signal(intangibles):
    base = _mean(intangibles, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_126d_accel_v007_signal(intangibles):
    base = _mean(intangibles, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_126d_accel_v008_signal(intangibles):
    base = _mean(intangibles, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_126d_accel_v009_signal(intangibles):
    base = _mean(intangibles, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_252d_accel_v010_signal(intangibles):
    base = _mean(intangibles, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_252d_accel_v011_signal(intangibles):
    base = _mean(intangibles, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_252d_accel_v012_signal(intangibles):
    base = _mean(intangibles, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_504d_accel_v013_signal(intangibles):
    base = _mean(intangibles, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_504d_accel_v014_signal(intangibles):
    base = _mean(intangibles, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_raw_504d_accel_v015_signal(intangibles):
    base = _mean(intangibles, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_21d_accel_v016_signal(intangibles):
    base = _mean(_log(intangibles), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_21d_accel_v017_signal(intangibles):
    base = _mean(_log(intangibles), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_21d_accel_v018_signal(intangibles):
    base = _mean(_log(intangibles), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_63d_accel_v019_signal(intangibles):
    base = _mean(_log(intangibles), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_63d_accel_v020_signal(intangibles):
    base = _mean(_log(intangibles), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_63d_accel_v021_signal(intangibles):
    base = _mean(_log(intangibles), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_126d_accel_v022_signal(intangibles):
    base = _mean(_log(intangibles), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_126d_accel_v023_signal(intangibles):
    base = _mean(_log(intangibles), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_126d_accel_v024_signal(intangibles):
    base = _mean(_log(intangibles), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_252d_accel_v025_signal(intangibles):
    base = _mean(_log(intangibles), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_252d_accel_v026_signal(intangibles):
    base = _mean(_log(intangibles), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_252d_accel_v027_signal(intangibles):
    base = _mean(_log(intangibles), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_504d_accel_v028_signal(intangibles):
    base = _mean(_log(intangibles), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_504d_accel_v029_signal(intangibles):
    base = _mean(_log(intangibles), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_log_504d_accel_v030_signal(intangibles):
    base = _mean(_log(intangibles), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_21d_accel_v031_signal(intangibles):
    base = _z(intangibles, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_21d_accel_v032_signal(intangibles):
    base = _z(intangibles, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_21d_accel_v033_signal(intangibles):
    base = _z(intangibles, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_63d_accel_v034_signal(intangibles):
    base = _z(intangibles, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_63d_accel_v035_signal(intangibles):
    base = _z(intangibles, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_63d_accel_v036_signal(intangibles):
    base = _z(intangibles, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_126d_accel_v037_signal(intangibles):
    base = _z(intangibles, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_126d_accel_v038_signal(intangibles):
    base = _z(intangibles, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_126d_accel_v039_signal(intangibles):
    base = _z(intangibles, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_252d_accel_v040_signal(intangibles):
    base = _z(intangibles, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_252d_accel_v041_signal(intangibles):
    base = _z(intangibles, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_252d_accel_v042_signal(intangibles):
    base = _z(intangibles, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_504d_accel_v043_signal(intangibles):
    base = _z(intangibles, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_504d_accel_v044_signal(intangibles):
    base = _z(intangibles, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_z_504d_accel_v045_signal(intangibles):
    base = _z(intangibles, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_21d_accel_v046_signal(intangibles, sharesbas):
    base = _safe_div(_mean(intangibles, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_21d_accel_v047_signal(intangibles, sharesbas):
    base = _safe_div(_mean(intangibles, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_21d_accel_v048_signal(intangibles, sharesbas):
    base = _safe_div(_mean(intangibles, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_63d_accel_v049_signal(intangibles, sharesbas):
    base = _safe_div(_mean(intangibles, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_63d_accel_v050_signal(intangibles, sharesbas):
    base = _safe_div(_mean(intangibles, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_63d_accel_v051_signal(intangibles, sharesbas):
    base = _safe_div(_mean(intangibles, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_126d_accel_v052_signal(intangibles, sharesbas):
    base = _safe_div(_mean(intangibles, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_126d_accel_v053_signal(intangibles, sharesbas):
    base = _safe_div(_mean(intangibles, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_126d_accel_v054_signal(intangibles, sharesbas):
    base = _safe_div(_mean(intangibles, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_252d_accel_v055_signal(intangibles, sharesbas):
    base = _safe_div(_mean(intangibles, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_252d_accel_v056_signal(intangibles, sharesbas):
    base = _safe_div(_mean(intangibles, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_252d_accel_v057_signal(intangibles, sharesbas):
    base = _safe_div(_mean(intangibles, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_504d_accel_v058_signal(intangibles, sharesbas):
    base = _safe_div(_mean(intangibles, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_504d_accel_v059_signal(intangibles, sharesbas):
    base = _safe_div(_mean(intangibles, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_ps_504d_accel_v060_signal(intangibles, sharesbas):
    base = _safe_div(_mean(intangibles, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_21d_accel_v061_signal(intangibles, assets):
    base = _safe_div(_mean(intangibles, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_21d_accel_v062_signal(intangibles, assets):
    base = _safe_div(_mean(intangibles, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_21d_accel_v063_signal(intangibles, assets):
    base = _safe_div(_mean(intangibles, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_63d_accel_v064_signal(intangibles, assets):
    base = _safe_div(_mean(intangibles, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_63d_accel_v065_signal(intangibles, assets):
    base = _safe_div(_mean(intangibles, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_63d_accel_v066_signal(intangibles, assets):
    base = _safe_div(_mean(intangibles, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_126d_accel_v067_signal(intangibles, assets):
    base = _safe_div(_mean(intangibles, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_126d_accel_v068_signal(intangibles, assets):
    base = _safe_div(_mean(intangibles, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_126d_accel_v069_signal(intangibles, assets):
    base = _safe_div(_mean(intangibles, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_252d_accel_v070_signal(intangibles, assets):
    base = _safe_div(_mean(intangibles, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_252d_accel_v071_signal(intangibles, assets):
    base = _safe_div(_mean(intangibles, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_252d_accel_v072_signal(intangibles, assets):
    base = _safe_div(_mean(intangibles, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_504d_accel_v073_signal(intangibles, assets):
    base = _safe_div(_mean(intangibles, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_504d_accel_v074_signal(intangibles, assets):
    base = _safe_div(_mean(intangibles, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_asset_scaled_504d_accel_v075_signal(intangibles, assets):
    base = _safe_div(_mean(intangibles, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_21d_accel_v076_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_21d_accel_v077_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_21d_accel_v078_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_63d_accel_v079_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_63d_accel_v080_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_63d_accel_v081_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_126d_accel_v082_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_126d_accel_v083_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_126d_accel_v084_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_252d_accel_v085_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_252d_accel_v086_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_252d_accel_v087_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_504d_accel_v088_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_504d_accel_v089_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mcap_scaled_504d_accel_v090_signal(intangibles, marketcap):
    base = _safe_div(_mean(intangibles, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_21d_accel_v091_signal(intangibles):
    base = _safe_div(intangibles - intangibles.rolling(21).min(), intangibles.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_21d_accel_v092_signal(intangibles):
    base = _safe_div(intangibles - intangibles.rolling(21).min(), intangibles.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_21d_accel_v093_signal(intangibles):
    base = _safe_div(intangibles - intangibles.rolling(21).min(), intangibles.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_63d_accel_v094_signal(intangibles):
    base = _safe_div(intangibles - intangibles.rolling(63).min(), intangibles.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_63d_accel_v095_signal(intangibles):
    base = _safe_div(intangibles - intangibles.rolling(63).min(), intangibles.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_63d_accel_v096_signal(intangibles):
    base = _safe_div(intangibles - intangibles.rolling(63).min(), intangibles.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_126d_accel_v097_signal(intangibles):
    base = _safe_div(intangibles - intangibles.rolling(126).min(), intangibles.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_126d_accel_v098_signal(intangibles):
    base = _safe_div(intangibles - intangibles.rolling(126).min(), intangibles.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_126d_accel_v099_signal(intangibles):
    base = _safe_div(intangibles - intangibles.rolling(126).min(), intangibles.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_252d_accel_v100_signal(intangibles):
    base = _safe_div(intangibles - intangibles.rolling(252).min(), intangibles.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_252d_accel_v101_signal(intangibles):
    base = _safe_div(intangibles - intangibles.rolling(252).min(), intangibles.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_252d_accel_v102_signal(intangibles):
    base = _safe_div(intangibles - intangibles.rolling(252).min(), intangibles.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_504d_accel_v103_signal(intangibles):
    base = _safe_div(intangibles - intangibles.rolling(504).min(), intangibles.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_504d_accel_v104_signal(intangibles):
    base = _safe_div(intangibles - intangibles.rolling(504).min(), intangibles.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_low_504d_accel_v105_signal(intangibles):
    base = _safe_div(intangibles - intangibles.rolling(504).min(), intangibles.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_21d_accel_v106_signal(intangibles):
    base = _safe_div(intangibles.rolling(21).max() - intangibles, intangibles.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_21d_accel_v107_signal(intangibles):
    base = _safe_div(intangibles.rolling(21).max() - intangibles, intangibles.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_21d_accel_v108_signal(intangibles):
    base = _safe_div(intangibles.rolling(21).max() - intangibles, intangibles.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_63d_accel_v109_signal(intangibles):
    base = _safe_div(intangibles.rolling(63).max() - intangibles, intangibles.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_63d_accel_v110_signal(intangibles):
    base = _safe_div(intangibles.rolling(63).max() - intangibles, intangibles.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_63d_accel_v111_signal(intangibles):
    base = _safe_div(intangibles.rolling(63).max() - intangibles, intangibles.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_126d_accel_v112_signal(intangibles):
    base = _safe_div(intangibles.rolling(126).max() - intangibles, intangibles.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_126d_accel_v113_signal(intangibles):
    base = _safe_div(intangibles.rolling(126).max() - intangibles, intangibles.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_126d_accel_v114_signal(intangibles):
    base = _safe_div(intangibles.rolling(126).max() - intangibles, intangibles.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_252d_accel_v115_signal(intangibles):
    base = _safe_div(intangibles.rolling(252).max() - intangibles, intangibles.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_252d_accel_v116_signal(intangibles):
    base = _safe_div(intangibles.rolling(252).max() - intangibles, intangibles.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_252d_accel_v117_signal(intangibles):
    base = _safe_div(intangibles.rolling(252).max() - intangibles, intangibles.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_504d_accel_v118_signal(intangibles):
    base = _safe_div(intangibles.rolling(504).max() - intangibles, intangibles.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_504d_accel_v119_signal(intangibles):
    base = _safe_div(intangibles.rolling(504).max() - intangibles, intangibles.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_dist_high_504d_accel_v120_signal(intangibles):
    base = _safe_div(intangibles.rolling(504).max() - intangibles, intangibles.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_21d_accel_v121_signal(intangibles):
    base = _safe_div(_mean(intangibles, 21) - _mean(intangibles, 42), _mean(intangibles, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_21d_accel_v122_signal(intangibles):
    base = _safe_div(_mean(intangibles, 21) - _mean(intangibles, 42), _mean(intangibles, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_21d_accel_v123_signal(intangibles):
    base = _safe_div(_mean(intangibles, 21) - _mean(intangibles, 42), _mean(intangibles, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_63d_accel_v124_signal(intangibles):
    base = _safe_div(_mean(intangibles, 63) - _mean(intangibles, 126), _mean(intangibles, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_63d_accel_v125_signal(intangibles):
    base = _safe_div(_mean(intangibles, 63) - _mean(intangibles, 126), _mean(intangibles, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_63d_accel_v126_signal(intangibles):
    base = _safe_div(_mean(intangibles, 63) - _mean(intangibles, 126), _mean(intangibles, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_126d_accel_v127_signal(intangibles):
    base = _safe_div(_mean(intangibles, 126) - _mean(intangibles, 252), _mean(intangibles, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_126d_accel_v128_signal(intangibles):
    base = _safe_div(_mean(intangibles, 126) - _mean(intangibles, 252), _mean(intangibles, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_126d_accel_v129_signal(intangibles):
    base = _safe_div(_mean(intangibles, 126) - _mean(intangibles, 252), _mean(intangibles, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_252d_accel_v130_signal(intangibles):
    base = _safe_div(_mean(intangibles, 252) - _mean(intangibles, 504), _mean(intangibles, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_252d_accel_v131_signal(intangibles):
    base = _safe_div(_mean(intangibles, 252) - _mean(intangibles, 504), _mean(intangibles, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_252d_accel_v132_signal(intangibles):
    base = _safe_div(_mean(intangibles, 252) - _mean(intangibles, 504), _mean(intangibles, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_504d_accel_v133_signal(intangibles):
    base = _safe_div(_mean(intangibles, 504) - _mean(intangibles, 1008), _mean(intangibles, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_504d_accel_v134_signal(intangibles):
    base = _safe_div(_mean(intangibles, 504) - _mean(intangibles, 1008), _mean(intangibles, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_mom_504d_accel_v135_signal(intangibles):
    base = _safe_div(_mean(intangibles, 504) - _mean(intangibles, 1008), _mean(intangibles, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_vol_21d_accel_v136_signal(intangibles):
    base = _std(intangibles, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_vol_21d_accel_v137_signal(intangibles):
    base = _std(intangibles, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_vol_21d_accel_v138_signal(intangibles):
    base = _std(intangibles, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_vol_63d_accel_v139_signal(intangibles):
    base = _std(intangibles, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_vol_63d_accel_v140_signal(intangibles):
    base = _std(intangibles, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_vol_63d_accel_v141_signal(intangibles):
    base = _std(intangibles, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_vol_126d_accel_v142_signal(intangibles):
    base = _std(intangibles, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_vol_126d_accel_v143_signal(intangibles):
    base = _std(intangibles, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_vol_126d_accel_v144_signal(intangibles):
    base = _std(intangibles, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_vol_252d_accel_v145_signal(intangibles):
    base = _std(intangibles, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_vol_252d_accel_v146_signal(intangibles):
    base = _std(intangibles, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_vol_252d_accel_v147_signal(intangibles):
    base = _std(intangibles, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_vol_504d_accel_v148_signal(intangibles):
    base = _std(intangibles, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_vol_504d_accel_v149_signal(intangibles):
    base = _std(intangibles, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol intangibles
def gm_f09_biotech_f09_intangible_asset_intensity_vol_504d_accel_v150_signal(intangibles):
    base = _std(intangibles, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

