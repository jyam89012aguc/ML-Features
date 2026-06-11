
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_21d_accel_v001_signal(taxassets):
    base = _mean(taxassets, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_21d_accel_v002_signal(taxassets):
    base = _mean(taxassets, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_21d_accel_v003_signal(taxassets):
    base = _mean(taxassets, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_63d_accel_v004_signal(taxassets):
    base = _mean(taxassets, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_63d_accel_v005_signal(taxassets):
    base = _mean(taxassets, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_63d_accel_v006_signal(taxassets):
    base = _mean(taxassets, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_126d_accel_v007_signal(taxassets):
    base = _mean(taxassets, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_126d_accel_v008_signal(taxassets):
    base = _mean(taxassets, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_126d_accel_v009_signal(taxassets):
    base = _mean(taxassets, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_252d_accel_v010_signal(taxassets):
    base = _mean(taxassets, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_252d_accel_v011_signal(taxassets):
    base = _mean(taxassets, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_252d_accel_v012_signal(taxassets):
    base = _mean(taxassets, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_504d_accel_v013_signal(taxassets):
    base = _mean(taxassets, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_504d_accel_v014_signal(taxassets):
    base = _mean(taxassets, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_504d_accel_v015_signal(taxassets):
    base = _mean(taxassets, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_21d_accel_v016_signal(taxassets):
    base = _mean(_log(taxassets), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_21d_accel_v017_signal(taxassets):
    base = _mean(_log(taxassets), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_21d_accel_v018_signal(taxassets):
    base = _mean(_log(taxassets), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_63d_accel_v019_signal(taxassets):
    base = _mean(_log(taxassets), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_63d_accel_v020_signal(taxassets):
    base = _mean(_log(taxassets), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_63d_accel_v021_signal(taxassets):
    base = _mean(_log(taxassets), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_126d_accel_v022_signal(taxassets):
    base = _mean(_log(taxassets), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_126d_accel_v023_signal(taxassets):
    base = _mean(_log(taxassets), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_126d_accel_v024_signal(taxassets):
    base = _mean(_log(taxassets), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_252d_accel_v025_signal(taxassets):
    base = _mean(_log(taxassets), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_252d_accel_v026_signal(taxassets):
    base = _mean(_log(taxassets), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_252d_accel_v027_signal(taxassets):
    base = _mean(_log(taxassets), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_504d_accel_v028_signal(taxassets):
    base = _mean(_log(taxassets), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_504d_accel_v029_signal(taxassets):
    base = _mean(_log(taxassets), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_504d_accel_v030_signal(taxassets):
    base = _mean(_log(taxassets), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_21d_accel_v031_signal(taxassets):
    base = _z(taxassets, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_21d_accel_v032_signal(taxassets):
    base = _z(taxassets, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_21d_accel_v033_signal(taxassets):
    base = _z(taxassets, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_63d_accel_v034_signal(taxassets):
    base = _z(taxassets, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_63d_accel_v035_signal(taxassets):
    base = _z(taxassets, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_63d_accel_v036_signal(taxassets):
    base = _z(taxassets, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_126d_accel_v037_signal(taxassets):
    base = _z(taxassets, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_126d_accel_v038_signal(taxassets):
    base = _z(taxassets, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_126d_accel_v039_signal(taxassets):
    base = _z(taxassets, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_252d_accel_v040_signal(taxassets):
    base = _z(taxassets, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_252d_accel_v041_signal(taxassets):
    base = _z(taxassets, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_252d_accel_v042_signal(taxassets):
    base = _z(taxassets, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_504d_accel_v043_signal(taxassets):
    base = _z(taxassets, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_504d_accel_v044_signal(taxassets):
    base = _z(taxassets, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_504d_accel_v045_signal(taxassets):
    base = _z(taxassets, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_21d_accel_v046_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_21d_accel_v047_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_21d_accel_v048_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_63d_accel_v049_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_63d_accel_v050_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_63d_accel_v051_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_126d_accel_v052_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_126d_accel_v053_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_126d_accel_v054_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_252d_accel_v055_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_252d_accel_v056_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_252d_accel_v057_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_504d_accel_v058_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_504d_accel_v059_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_504d_accel_v060_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_21d_accel_v061_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_21d_accel_v062_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_21d_accel_v063_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_63d_accel_v064_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_63d_accel_v065_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_63d_accel_v066_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_126d_accel_v067_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_126d_accel_v068_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_126d_accel_v069_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_252d_accel_v070_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_252d_accel_v071_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_252d_accel_v072_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_504d_accel_v073_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_504d_accel_v074_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_504d_accel_v075_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_21d_accel_v076_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_21d_accel_v077_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_21d_accel_v078_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_63d_accel_v079_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_63d_accel_v080_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_63d_accel_v081_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_126d_accel_v082_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_126d_accel_v083_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_126d_accel_v084_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_252d_accel_v085_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_252d_accel_v086_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_252d_accel_v087_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_504d_accel_v088_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_504d_accel_v089_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_504d_accel_v090_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_21d_accel_v091_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(21).min(), taxassets.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_21d_accel_v092_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(21).min(), taxassets.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_21d_accel_v093_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(21).min(), taxassets.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_63d_accel_v094_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(63).min(), taxassets.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_63d_accel_v095_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(63).min(), taxassets.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_63d_accel_v096_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(63).min(), taxassets.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_126d_accel_v097_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(126).min(), taxassets.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_126d_accel_v098_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(126).min(), taxassets.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_126d_accel_v099_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(126).min(), taxassets.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_252d_accel_v100_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(252).min(), taxassets.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_252d_accel_v101_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(252).min(), taxassets.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_252d_accel_v102_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(252).min(), taxassets.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_504d_accel_v103_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(504).min(), taxassets.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_504d_accel_v104_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(504).min(), taxassets.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_504d_accel_v105_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(504).min(), taxassets.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_21d_accel_v106_signal(taxassets):
    base = _safe_div(taxassets.rolling(21).max() - taxassets, taxassets.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_21d_accel_v107_signal(taxassets):
    base = _safe_div(taxassets.rolling(21).max() - taxassets, taxassets.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_21d_accel_v108_signal(taxassets):
    base = _safe_div(taxassets.rolling(21).max() - taxassets, taxassets.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_63d_accel_v109_signal(taxassets):
    base = _safe_div(taxassets.rolling(63).max() - taxassets, taxassets.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_63d_accel_v110_signal(taxassets):
    base = _safe_div(taxassets.rolling(63).max() - taxassets, taxassets.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_63d_accel_v111_signal(taxassets):
    base = _safe_div(taxassets.rolling(63).max() - taxassets, taxassets.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_126d_accel_v112_signal(taxassets):
    base = _safe_div(taxassets.rolling(126).max() - taxassets, taxassets.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_126d_accel_v113_signal(taxassets):
    base = _safe_div(taxassets.rolling(126).max() - taxassets, taxassets.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_126d_accel_v114_signal(taxassets):
    base = _safe_div(taxassets.rolling(126).max() - taxassets, taxassets.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_252d_accel_v115_signal(taxassets):
    base = _safe_div(taxassets.rolling(252).max() - taxassets, taxassets.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_252d_accel_v116_signal(taxassets):
    base = _safe_div(taxassets.rolling(252).max() - taxassets, taxassets.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_252d_accel_v117_signal(taxassets):
    base = _safe_div(taxassets.rolling(252).max() - taxassets, taxassets.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_504d_accel_v118_signal(taxassets):
    base = _safe_div(taxassets.rolling(504).max() - taxassets, taxassets.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_504d_accel_v119_signal(taxassets):
    base = _safe_div(taxassets.rolling(504).max() - taxassets, taxassets.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_504d_accel_v120_signal(taxassets):
    base = _safe_div(taxassets.rolling(504).max() - taxassets, taxassets.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_21d_accel_v121_signal(taxassets):
    base = _safe_div(_mean(taxassets, 21) - _mean(taxassets, 42), _mean(taxassets, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_21d_accel_v122_signal(taxassets):
    base = _safe_div(_mean(taxassets, 21) - _mean(taxassets, 42), _mean(taxassets, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_21d_accel_v123_signal(taxassets):
    base = _safe_div(_mean(taxassets, 21) - _mean(taxassets, 42), _mean(taxassets, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_63d_accel_v124_signal(taxassets):
    base = _safe_div(_mean(taxassets, 63) - _mean(taxassets, 126), _mean(taxassets, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_63d_accel_v125_signal(taxassets):
    base = _safe_div(_mean(taxassets, 63) - _mean(taxassets, 126), _mean(taxassets, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_63d_accel_v126_signal(taxassets):
    base = _safe_div(_mean(taxassets, 63) - _mean(taxassets, 126), _mean(taxassets, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_126d_accel_v127_signal(taxassets):
    base = _safe_div(_mean(taxassets, 126) - _mean(taxassets, 252), _mean(taxassets, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_126d_accel_v128_signal(taxassets):
    base = _safe_div(_mean(taxassets, 126) - _mean(taxassets, 252), _mean(taxassets, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_126d_accel_v129_signal(taxassets):
    base = _safe_div(_mean(taxassets, 126) - _mean(taxassets, 252), _mean(taxassets, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_252d_accel_v130_signal(taxassets):
    base = _safe_div(_mean(taxassets, 252) - _mean(taxassets, 504), _mean(taxassets, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_252d_accel_v131_signal(taxassets):
    base = _safe_div(_mean(taxassets, 252) - _mean(taxassets, 504), _mean(taxassets, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_252d_accel_v132_signal(taxassets):
    base = _safe_div(_mean(taxassets, 252) - _mean(taxassets, 504), _mean(taxassets, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_504d_accel_v133_signal(taxassets):
    base = _safe_div(_mean(taxassets, 504) - _mean(taxassets, 1008), _mean(taxassets, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_504d_accel_v134_signal(taxassets):
    base = _safe_div(_mean(taxassets, 504) - _mean(taxassets, 1008), _mean(taxassets, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_504d_accel_v135_signal(taxassets):
    base = _safe_div(_mean(taxassets, 504) - _mean(taxassets, 1008), _mean(taxassets, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_21d_accel_v136_signal(taxassets):
    base = _std(taxassets, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_21d_accel_v137_signal(taxassets):
    base = _std(taxassets, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_21d_accel_v138_signal(taxassets):
    base = _std(taxassets, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_63d_accel_v139_signal(taxassets):
    base = _std(taxassets, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_63d_accel_v140_signal(taxassets):
    base = _std(taxassets, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_63d_accel_v141_signal(taxassets):
    base = _std(taxassets, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_126d_accel_v142_signal(taxassets):
    base = _std(taxassets, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_126d_accel_v143_signal(taxassets):
    base = _std(taxassets, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_126d_accel_v144_signal(taxassets):
    base = _std(taxassets, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_252d_accel_v145_signal(taxassets):
    base = _std(taxassets, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_252d_accel_v146_signal(taxassets):
    base = _std(taxassets, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_252d_accel_v147_signal(taxassets):
    base = _std(taxassets, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_504d_accel_v148_signal(taxassets):
    base = _std(taxassets, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_504d_accel_v149_signal(taxassets):
    base = _std(taxassets, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_504d_accel_v150_signal(taxassets):
    base = _std(taxassets, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

