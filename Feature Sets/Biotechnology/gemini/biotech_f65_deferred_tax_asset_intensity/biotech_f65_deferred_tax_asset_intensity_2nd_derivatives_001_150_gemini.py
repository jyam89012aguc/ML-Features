
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_21d_slope_v001_signal(taxassets):
    base = _mean(taxassets, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_21d_slope_v002_signal(taxassets):
    base = _mean(taxassets, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_21d_slope_v003_signal(taxassets):
    base = _mean(taxassets, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_63d_slope_v004_signal(taxassets):
    base = _mean(taxassets, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_63d_slope_v005_signal(taxassets):
    base = _mean(taxassets, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_63d_slope_v006_signal(taxassets):
    base = _mean(taxassets, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_126d_slope_v007_signal(taxassets):
    base = _mean(taxassets, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_126d_slope_v008_signal(taxassets):
    base = _mean(taxassets, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_126d_slope_v009_signal(taxassets):
    base = _mean(taxassets, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_252d_slope_v010_signal(taxassets):
    base = _mean(taxassets, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_252d_slope_v011_signal(taxassets):
    base = _mean(taxassets, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_252d_slope_v012_signal(taxassets):
    base = _mean(taxassets, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_504d_slope_v013_signal(taxassets):
    base = _mean(taxassets, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_504d_slope_v014_signal(taxassets):
    base = _mean(taxassets, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_raw_504d_slope_v015_signal(taxassets):
    base = _mean(taxassets, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_21d_slope_v016_signal(taxassets):
    base = _mean(_log(taxassets), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_21d_slope_v017_signal(taxassets):
    base = _mean(_log(taxassets), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_21d_slope_v018_signal(taxassets):
    base = _mean(_log(taxassets), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_63d_slope_v019_signal(taxassets):
    base = _mean(_log(taxassets), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_63d_slope_v020_signal(taxassets):
    base = _mean(_log(taxassets), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_63d_slope_v021_signal(taxassets):
    base = _mean(_log(taxassets), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_126d_slope_v022_signal(taxassets):
    base = _mean(_log(taxassets), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_126d_slope_v023_signal(taxassets):
    base = _mean(_log(taxassets), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_126d_slope_v024_signal(taxassets):
    base = _mean(_log(taxassets), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_252d_slope_v025_signal(taxassets):
    base = _mean(_log(taxassets), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_252d_slope_v026_signal(taxassets):
    base = _mean(_log(taxassets), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_252d_slope_v027_signal(taxassets):
    base = _mean(_log(taxassets), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_504d_slope_v028_signal(taxassets):
    base = _mean(_log(taxassets), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_504d_slope_v029_signal(taxassets):
    base = _mean(_log(taxassets), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_log_504d_slope_v030_signal(taxassets):
    base = _mean(_log(taxassets), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_21d_slope_v031_signal(taxassets):
    base = _z(taxassets, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_21d_slope_v032_signal(taxassets):
    base = _z(taxassets, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_21d_slope_v033_signal(taxassets):
    base = _z(taxassets, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_63d_slope_v034_signal(taxassets):
    base = _z(taxassets, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_63d_slope_v035_signal(taxassets):
    base = _z(taxassets, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_63d_slope_v036_signal(taxassets):
    base = _z(taxassets, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_126d_slope_v037_signal(taxassets):
    base = _z(taxassets, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_126d_slope_v038_signal(taxassets):
    base = _z(taxassets, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_126d_slope_v039_signal(taxassets):
    base = _z(taxassets, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_252d_slope_v040_signal(taxassets):
    base = _z(taxassets, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_252d_slope_v041_signal(taxassets):
    base = _z(taxassets, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_252d_slope_v042_signal(taxassets):
    base = _z(taxassets, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_504d_slope_v043_signal(taxassets):
    base = _z(taxassets, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_504d_slope_v044_signal(taxassets):
    base = _z(taxassets, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_z_504d_slope_v045_signal(taxassets):
    base = _z(taxassets, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_21d_slope_v046_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_21d_slope_v047_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_21d_slope_v048_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_63d_slope_v049_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_63d_slope_v050_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_63d_slope_v051_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_126d_slope_v052_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_126d_slope_v053_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_126d_slope_v054_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_252d_slope_v055_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_252d_slope_v056_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_252d_slope_v057_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_504d_slope_v058_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_504d_slope_v059_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_ps_504d_slope_v060_signal(taxassets, sharesbas):
    base = _safe_div(_mean(taxassets, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_21d_slope_v061_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_21d_slope_v062_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_21d_slope_v063_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_63d_slope_v064_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_63d_slope_v065_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_63d_slope_v066_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_126d_slope_v067_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_126d_slope_v068_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_126d_slope_v069_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_252d_slope_v070_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_252d_slope_v071_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_252d_slope_v072_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_504d_slope_v073_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_504d_slope_v074_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_asset_scaled_504d_slope_v075_signal(taxassets, assets):
    base = _safe_div(_mean(taxassets, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_21d_slope_v076_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_21d_slope_v077_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_21d_slope_v078_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_63d_slope_v079_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_63d_slope_v080_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_63d_slope_v081_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_126d_slope_v082_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_126d_slope_v083_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_126d_slope_v084_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_252d_slope_v085_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_252d_slope_v086_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_252d_slope_v087_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_504d_slope_v088_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_504d_slope_v089_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mcap_scaled_504d_slope_v090_signal(taxassets, marketcap):
    base = _safe_div(_mean(taxassets, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_21d_slope_v091_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(21).min(), taxassets.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_21d_slope_v092_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(21).min(), taxassets.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_21d_slope_v093_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(21).min(), taxassets.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_63d_slope_v094_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(63).min(), taxassets.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_63d_slope_v095_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(63).min(), taxassets.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_63d_slope_v096_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(63).min(), taxassets.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_126d_slope_v097_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(126).min(), taxassets.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_126d_slope_v098_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(126).min(), taxassets.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_126d_slope_v099_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(126).min(), taxassets.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_252d_slope_v100_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(252).min(), taxassets.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_252d_slope_v101_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(252).min(), taxassets.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_252d_slope_v102_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(252).min(), taxassets.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_504d_slope_v103_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(504).min(), taxassets.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_504d_slope_v104_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(504).min(), taxassets.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_low_504d_slope_v105_signal(taxassets):
    base = _safe_div(taxassets - taxassets.rolling(504).min(), taxassets.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_21d_slope_v106_signal(taxassets):
    base = _safe_div(taxassets.rolling(21).max() - taxassets, taxassets.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_21d_slope_v107_signal(taxassets):
    base = _safe_div(taxassets.rolling(21).max() - taxassets, taxassets.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_21d_slope_v108_signal(taxassets):
    base = _safe_div(taxassets.rolling(21).max() - taxassets, taxassets.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_63d_slope_v109_signal(taxassets):
    base = _safe_div(taxassets.rolling(63).max() - taxassets, taxassets.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_63d_slope_v110_signal(taxassets):
    base = _safe_div(taxassets.rolling(63).max() - taxassets, taxassets.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_63d_slope_v111_signal(taxassets):
    base = _safe_div(taxassets.rolling(63).max() - taxassets, taxassets.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_126d_slope_v112_signal(taxassets):
    base = _safe_div(taxassets.rolling(126).max() - taxassets, taxassets.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_126d_slope_v113_signal(taxassets):
    base = _safe_div(taxassets.rolling(126).max() - taxassets, taxassets.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_126d_slope_v114_signal(taxassets):
    base = _safe_div(taxassets.rolling(126).max() - taxassets, taxassets.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_252d_slope_v115_signal(taxassets):
    base = _safe_div(taxassets.rolling(252).max() - taxassets, taxassets.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_252d_slope_v116_signal(taxassets):
    base = _safe_div(taxassets.rolling(252).max() - taxassets, taxassets.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_252d_slope_v117_signal(taxassets):
    base = _safe_div(taxassets.rolling(252).max() - taxassets, taxassets.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_504d_slope_v118_signal(taxassets):
    base = _safe_div(taxassets.rolling(504).max() - taxassets, taxassets.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_504d_slope_v119_signal(taxassets):
    base = _safe_div(taxassets.rolling(504).max() - taxassets, taxassets.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_dist_high_504d_slope_v120_signal(taxassets):
    base = _safe_div(taxassets.rolling(504).max() - taxassets, taxassets.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_21d_slope_v121_signal(taxassets):
    base = _safe_div(_mean(taxassets, 21) - _mean(taxassets, 42), _mean(taxassets, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_21d_slope_v122_signal(taxassets):
    base = _safe_div(_mean(taxassets, 21) - _mean(taxassets, 42), _mean(taxassets, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_21d_slope_v123_signal(taxassets):
    base = _safe_div(_mean(taxassets, 21) - _mean(taxassets, 42), _mean(taxassets, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_63d_slope_v124_signal(taxassets):
    base = _safe_div(_mean(taxassets, 63) - _mean(taxassets, 126), _mean(taxassets, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_63d_slope_v125_signal(taxassets):
    base = _safe_div(_mean(taxassets, 63) - _mean(taxassets, 126), _mean(taxassets, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_63d_slope_v126_signal(taxassets):
    base = _safe_div(_mean(taxassets, 63) - _mean(taxassets, 126), _mean(taxassets, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_126d_slope_v127_signal(taxassets):
    base = _safe_div(_mean(taxassets, 126) - _mean(taxassets, 252), _mean(taxassets, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_126d_slope_v128_signal(taxassets):
    base = _safe_div(_mean(taxassets, 126) - _mean(taxassets, 252), _mean(taxassets, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_126d_slope_v129_signal(taxassets):
    base = _safe_div(_mean(taxassets, 126) - _mean(taxassets, 252), _mean(taxassets, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_252d_slope_v130_signal(taxassets):
    base = _safe_div(_mean(taxassets, 252) - _mean(taxassets, 504), _mean(taxassets, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_252d_slope_v131_signal(taxassets):
    base = _safe_div(_mean(taxassets, 252) - _mean(taxassets, 504), _mean(taxassets, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_252d_slope_v132_signal(taxassets):
    base = _safe_div(_mean(taxassets, 252) - _mean(taxassets, 504), _mean(taxassets, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_504d_slope_v133_signal(taxassets):
    base = _safe_div(_mean(taxassets, 504) - _mean(taxassets, 1008), _mean(taxassets, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_504d_slope_v134_signal(taxassets):
    base = _safe_div(_mean(taxassets, 504) - _mean(taxassets, 1008), _mean(taxassets, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_mom_504d_slope_v135_signal(taxassets):
    base = _safe_div(_mean(taxassets, 504) - _mean(taxassets, 1008), _mean(taxassets, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_21d_slope_v136_signal(taxassets):
    base = _std(taxassets, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_21d_slope_v137_signal(taxassets):
    base = _std(taxassets, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_21d_slope_v138_signal(taxassets):
    base = _std(taxassets, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_63d_slope_v139_signal(taxassets):
    base = _std(taxassets, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_63d_slope_v140_signal(taxassets):
    base = _std(taxassets, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_63d_slope_v141_signal(taxassets):
    base = _std(taxassets, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_126d_slope_v142_signal(taxassets):
    base = _std(taxassets, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_126d_slope_v143_signal(taxassets):
    base = _std(taxassets, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_126d_slope_v144_signal(taxassets):
    base = _std(taxassets, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_252d_slope_v145_signal(taxassets):
    base = _std(taxassets, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_252d_slope_v146_signal(taxassets):
    base = _std(taxassets, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_252d_slope_v147_signal(taxassets):
    base = _std(taxassets, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_504d_slope_v148_signal(taxassets):
    base = _std(taxassets, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_504d_slope_v149_signal(taxassets):
    base = _std(taxassets, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol taxassets
def gm_f65_biotech_f65_deferred_tax_asset_intensity_vol_504d_slope_v150_signal(taxassets):
    base = _std(taxassets, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

