
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_21d_slope_v001_signal(assetsc):
    base = _mean(assetsc, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_21d_slope_v002_signal(assetsc):
    base = _mean(assetsc, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_21d_slope_v003_signal(assetsc):
    base = _mean(assetsc, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_63d_slope_v004_signal(assetsc):
    base = _mean(assetsc, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_63d_slope_v005_signal(assetsc):
    base = _mean(assetsc, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_63d_slope_v006_signal(assetsc):
    base = _mean(assetsc, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_126d_slope_v007_signal(assetsc):
    base = _mean(assetsc, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_126d_slope_v008_signal(assetsc):
    base = _mean(assetsc, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_126d_slope_v009_signal(assetsc):
    base = _mean(assetsc, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_252d_slope_v010_signal(assetsc):
    base = _mean(assetsc, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_252d_slope_v011_signal(assetsc):
    base = _mean(assetsc, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_252d_slope_v012_signal(assetsc):
    base = _mean(assetsc, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_504d_slope_v013_signal(assetsc):
    base = _mean(assetsc, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_504d_slope_v014_signal(assetsc):
    base = _mean(assetsc, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw assetsc
def gm_f62_biotech_f62_operating_accruals_quality_raw_504d_slope_v015_signal(assetsc):
    base = _mean(assetsc, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_21d_slope_v016_signal(assetsc):
    base = _mean(_log(assetsc), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_21d_slope_v017_signal(assetsc):
    base = _mean(_log(assetsc), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_21d_slope_v018_signal(assetsc):
    base = _mean(_log(assetsc), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_63d_slope_v019_signal(assetsc):
    base = _mean(_log(assetsc), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_63d_slope_v020_signal(assetsc):
    base = _mean(_log(assetsc), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_63d_slope_v021_signal(assetsc):
    base = _mean(_log(assetsc), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_126d_slope_v022_signal(assetsc):
    base = _mean(_log(assetsc), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_126d_slope_v023_signal(assetsc):
    base = _mean(_log(assetsc), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_126d_slope_v024_signal(assetsc):
    base = _mean(_log(assetsc), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_252d_slope_v025_signal(assetsc):
    base = _mean(_log(assetsc), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_252d_slope_v026_signal(assetsc):
    base = _mean(_log(assetsc), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_252d_slope_v027_signal(assetsc):
    base = _mean(_log(assetsc), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_504d_slope_v028_signal(assetsc):
    base = _mean(_log(assetsc), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_504d_slope_v029_signal(assetsc):
    base = _mean(_log(assetsc), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log assetsc
def gm_f62_biotech_f62_operating_accruals_quality_log_504d_slope_v030_signal(assetsc):
    base = _mean(_log(assetsc), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_21d_slope_v031_signal(assetsc):
    base = _z(assetsc, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_21d_slope_v032_signal(assetsc):
    base = _z(assetsc, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_21d_slope_v033_signal(assetsc):
    base = _z(assetsc, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_63d_slope_v034_signal(assetsc):
    base = _z(assetsc, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_63d_slope_v035_signal(assetsc):
    base = _z(assetsc, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_63d_slope_v036_signal(assetsc):
    base = _z(assetsc, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_126d_slope_v037_signal(assetsc):
    base = _z(assetsc, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_126d_slope_v038_signal(assetsc):
    base = _z(assetsc, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_126d_slope_v039_signal(assetsc):
    base = _z(assetsc, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_252d_slope_v040_signal(assetsc):
    base = _z(assetsc, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_252d_slope_v041_signal(assetsc):
    base = _z(assetsc, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_252d_slope_v042_signal(assetsc):
    base = _z(assetsc, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_504d_slope_v043_signal(assetsc):
    base = _z(assetsc, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_504d_slope_v044_signal(assetsc):
    base = _z(assetsc, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z assetsc
def gm_f62_biotech_f62_operating_accruals_quality_z_504d_slope_v045_signal(assetsc):
    base = _z(assetsc, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_21d_slope_v046_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_21d_slope_v047_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_21d_slope_v048_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_63d_slope_v049_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_63d_slope_v050_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_63d_slope_v051_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_126d_slope_v052_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_126d_slope_v053_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_126d_slope_v054_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_252d_slope_v055_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_252d_slope_v056_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_252d_slope_v057_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_504d_slope_v058_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_504d_slope_v059_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps assetsc
def gm_f62_biotech_f62_operating_accruals_quality_ps_504d_slope_v060_signal(assetsc, sharesbas):
    base = _safe_div(_mean(assetsc, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_21d_slope_v061_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_21d_slope_v062_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_21d_slope_v063_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_63d_slope_v064_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_63d_slope_v065_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_63d_slope_v066_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_126d_slope_v067_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_126d_slope_v068_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_126d_slope_v069_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_252d_slope_v070_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_252d_slope_v071_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_252d_slope_v072_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_504d_slope_v073_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_504d_slope_v074_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_asset_scaled_504d_slope_v075_signal(assetsc, assets):
    base = _safe_div(_mean(assetsc, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_21d_slope_v076_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_21d_slope_v077_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_21d_slope_v078_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_63d_slope_v079_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_63d_slope_v080_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_63d_slope_v081_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_126d_slope_v082_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_126d_slope_v083_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_126d_slope_v084_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_252d_slope_v085_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_252d_slope_v086_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_252d_slope_v087_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_504d_slope_v088_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_504d_slope_v089_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mcap_scaled_504d_slope_v090_signal(assetsc, marketcap):
    base = _safe_div(_mean(assetsc, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_21d_slope_v091_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(21).min(), assetsc.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_21d_slope_v092_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(21).min(), assetsc.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_21d_slope_v093_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(21).min(), assetsc.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_63d_slope_v094_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(63).min(), assetsc.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_63d_slope_v095_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(63).min(), assetsc.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_63d_slope_v096_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(63).min(), assetsc.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_126d_slope_v097_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(126).min(), assetsc.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_126d_slope_v098_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(126).min(), assetsc.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_126d_slope_v099_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(126).min(), assetsc.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_252d_slope_v100_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(252).min(), assetsc.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_252d_slope_v101_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(252).min(), assetsc.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_252d_slope_v102_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(252).min(), assetsc.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_504d_slope_v103_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(504).min(), assetsc.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_504d_slope_v104_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(504).min(), assetsc.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_low_504d_slope_v105_signal(assetsc):
    base = _safe_div(assetsc - assetsc.rolling(504).min(), assetsc.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_21d_slope_v106_signal(assetsc):
    base = _safe_div(assetsc.rolling(21).max() - assetsc, assetsc.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_21d_slope_v107_signal(assetsc):
    base = _safe_div(assetsc.rolling(21).max() - assetsc, assetsc.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_21d_slope_v108_signal(assetsc):
    base = _safe_div(assetsc.rolling(21).max() - assetsc, assetsc.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_63d_slope_v109_signal(assetsc):
    base = _safe_div(assetsc.rolling(63).max() - assetsc, assetsc.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_63d_slope_v110_signal(assetsc):
    base = _safe_div(assetsc.rolling(63).max() - assetsc, assetsc.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_63d_slope_v111_signal(assetsc):
    base = _safe_div(assetsc.rolling(63).max() - assetsc, assetsc.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_126d_slope_v112_signal(assetsc):
    base = _safe_div(assetsc.rolling(126).max() - assetsc, assetsc.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_126d_slope_v113_signal(assetsc):
    base = _safe_div(assetsc.rolling(126).max() - assetsc, assetsc.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_126d_slope_v114_signal(assetsc):
    base = _safe_div(assetsc.rolling(126).max() - assetsc, assetsc.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_252d_slope_v115_signal(assetsc):
    base = _safe_div(assetsc.rolling(252).max() - assetsc, assetsc.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_252d_slope_v116_signal(assetsc):
    base = _safe_div(assetsc.rolling(252).max() - assetsc, assetsc.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_252d_slope_v117_signal(assetsc):
    base = _safe_div(assetsc.rolling(252).max() - assetsc, assetsc.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_504d_slope_v118_signal(assetsc):
    base = _safe_div(assetsc.rolling(504).max() - assetsc, assetsc.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_504d_slope_v119_signal(assetsc):
    base = _safe_div(assetsc.rolling(504).max() - assetsc, assetsc.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high assetsc
def gm_f62_biotech_f62_operating_accruals_quality_dist_high_504d_slope_v120_signal(assetsc):
    base = _safe_div(assetsc.rolling(504).max() - assetsc, assetsc.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_21d_slope_v121_signal(assetsc):
    base = _safe_div(_mean(assetsc, 21) - _mean(assetsc, 42), _mean(assetsc, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_21d_slope_v122_signal(assetsc):
    base = _safe_div(_mean(assetsc, 21) - _mean(assetsc, 42), _mean(assetsc, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_21d_slope_v123_signal(assetsc):
    base = _safe_div(_mean(assetsc, 21) - _mean(assetsc, 42), _mean(assetsc, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_63d_slope_v124_signal(assetsc):
    base = _safe_div(_mean(assetsc, 63) - _mean(assetsc, 126), _mean(assetsc, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_63d_slope_v125_signal(assetsc):
    base = _safe_div(_mean(assetsc, 63) - _mean(assetsc, 126), _mean(assetsc, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_63d_slope_v126_signal(assetsc):
    base = _safe_div(_mean(assetsc, 63) - _mean(assetsc, 126), _mean(assetsc, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_126d_slope_v127_signal(assetsc):
    base = _safe_div(_mean(assetsc, 126) - _mean(assetsc, 252), _mean(assetsc, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_126d_slope_v128_signal(assetsc):
    base = _safe_div(_mean(assetsc, 126) - _mean(assetsc, 252), _mean(assetsc, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_126d_slope_v129_signal(assetsc):
    base = _safe_div(_mean(assetsc, 126) - _mean(assetsc, 252), _mean(assetsc, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_252d_slope_v130_signal(assetsc):
    base = _safe_div(_mean(assetsc, 252) - _mean(assetsc, 504), _mean(assetsc, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_252d_slope_v131_signal(assetsc):
    base = _safe_div(_mean(assetsc, 252) - _mean(assetsc, 504), _mean(assetsc, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_252d_slope_v132_signal(assetsc):
    base = _safe_div(_mean(assetsc, 252) - _mean(assetsc, 504), _mean(assetsc, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_504d_slope_v133_signal(assetsc):
    base = _safe_div(_mean(assetsc, 504) - _mean(assetsc, 1008), _mean(assetsc, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_504d_slope_v134_signal(assetsc):
    base = _safe_div(_mean(assetsc, 504) - _mean(assetsc, 1008), _mean(assetsc, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom assetsc
def gm_f62_biotech_f62_operating_accruals_quality_mom_504d_slope_v135_signal(assetsc):
    base = _safe_div(_mean(assetsc, 504) - _mean(assetsc, 1008), _mean(assetsc, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_21d_slope_v136_signal(assetsc):
    base = _std(assetsc, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_21d_slope_v137_signal(assetsc):
    base = _std(assetsc, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_21d_slope_v138_signal(assetsc):
    base = _std(assetsc, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_63d_slope_v139_signal(assetsc):
    base = _std(assetsc, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_63d_slope_v140_signal(assetsc):
    base = _std(assetsc, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_63d_slope_v141_signal(assetsc):
    base = _std(assetsc, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_126d_slope_v142_signal(assetsc):
    base = _std(assetsc, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_126d_slope_v143_signal(assetsc):
    base = _std(assetsc, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_126d_slope_v144_signal(assetsc):
    base = _std(assetsc, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_252d_slope_v145_signal(assetsc):
    base = _std(assetsc, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_252d_slope_v146_signal(assetsc):
    base = _std(assetsc, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_252d_slope_v147_signal(assetsc):
    base = _std(assetsc, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_504d_slope_v148_signal(assetsc):
    base = _std(assetsc, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_504d_slope_v149_signal(assetsc):
    base = _std(assetsc, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol assetsc
def gm_f62_biotech_f62_operating_accruals_quality_vol_504d_slope_v150_signal(assetsc):
    base = _std(assetsc, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

