
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw units
def gm_f74_biotech_f74_institutional_holder_concentration_raw_21d_slope_v001_signal(units):
    base = _mean(units, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw units
def gm_f74_biotech_f74_institutional_holder_concentration_raw_21d_slope_v002_signal(units):
    base = _mean(units, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw units
def gm_f74_biotech_f74_institutional_holder_concentration_raw_21d_slope_v003_signal(units):
    base = _mean(units, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw units
def gm_f74_biotech_f74_institutional_holder_concentration_raw_63d_slope_v004_signal(units):
    base = _mean(units, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw units
def gm_f74_biotech_f74_institutional_holder_concentration_raw_63d_slope_v005_signal(units):
    base = _mean(units, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw units
def gm_f74_biotech_f74_institutional_holder_concentration_raw_63d_slope_v006_signal(units):
    base = _mean(units, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw units
def gm_f74_biotech_f74_institutional_holder_concentration_raw_126d_slope_v007_signal(units):
    base = _mean(units, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw units
def gm_f74_biotech_f74_institutional_holder_concentration_raw_126d_slope_v008_signal(units):
    base = _mean(units, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw units
def gm_f74_biotech_f74_institutional_holder_concentration_raw_126d_slope_v009_signal(units):
    base = _mean(units, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw units
def gm_f74_biotech_f74_institutional_holder_concentration_raw_252d_slope_v010_signal(units):
    base = _mean(units, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw units
def gm_f74_biotech_f74_institutional_holder_concentration_raw_252d_slope_v011_signal(units):
    base = _mean(units, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw units
def gm_f74_biotech_f74_institutional_holder_concentration_raw_252d_slope_v012_signal(units):
    base = _mean(units, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw units
def gm_f74_biotech_f74_institutional_holder_concentration_raw_504d_slope_v013_signal(units):
    base = _mean(units, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw units
def gm_f74_biotech_f74_institutional_holder_concentration_raw_504d_slope_v014_signal(units):
    base = _mean(units, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw units
def gm_f74_biotech_f74_institutional_holder_concentration_raw_504d_slope_v015_signal(units):
    base = _mean(units, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log units
def gm_f74_biotech_f74_institutional_holder_concentration_log_21d_slope_v016_signal(units):
    base = _mean(_log(units), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log units
def gm_f74_biotech_f74_institutional_holder_concentration_log_21d_slope_v017_signal(units):
    base = _mean(_log(units), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log units
def gm_f74_biotech_f74_institutional_holder_concentration_log_21d_slope_v018_signal(units):
    base = _mean(_log(units), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log units
def gm_f74_biotech_f74_institutional_holder_concentration_log_63d_slope_v019_signal(units):
    base = _mean(_log(units), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log units
def gm_f74_biotech_f74_institutional_holder_concentration_log_63d_slope_v020_signal(units):
    base = _mean(_log(units), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log units
def gm_f74_biotech_f74_institutional_holder_concentration_log_63d_slope_v021_signal(units):
    base = _mean(_log(units), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log units
def gm_f74_biotech_f74_institutional_holder_concentration_log_126d_slope_v022_signal(units):
    base = _mean(_log(units), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log units
def gm_f74_biotech_f74_institutional_holder_concentration_log_126d_slope_v023_signal(units):
    base = _mean(_log(units), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log units
def gm_f74_biotech_f74_institutional_holder_concentration_log_126d_slope_v024_signal(units):
    base = _mean(_log(units), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log units
def gm_f74_biotech_f74_institutional_holder_concentration_log_252d_slope_v025_signal(units):
    base = _mean(_log(units), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log units
def gm_f74_biotech_f74_institutional_holder_concentration_log_252d_slope_v026_signal(units):
    base = _mean(_log(units), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log units
def gm_f74_biotech_f74_institutional_holder_concentration_log_252d_slope_v027_signal(units):
    base = _mean(_log(units), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log units
def gm_f74_biotech_f74_institutional_holder_concentration_log_504d_slope_v028_signal(units):
    base = _mean(_log(units), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log units
def gm_f74_biotech_f74_institutional_holder_concentration_log_504d_slope_v029_signal(units):
    base = _mean(_log(units), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log units
def gm_f74_biotech_f74_institutional_holder_concentration_log_504d_slope_v030_signal(units):
    base = _mean(_log(units), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z units
def gm_f74_biotech_f74_institutional_holder_concentration_z_21d_slope_v031_signal(units):
    base = _z(units, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z units
def gm_f74_biotech_f74_institutional_holder_concentration_z_21d_slope_v032_signal(units):
    base = _z(units, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z units
def gm_f74_biotech_f74_institutional_holder_concentration_z_21d_slope_v033_signal(units):
    base = _z(units, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z units
def gm_f74_biotech_f74_institutional_holder_concentration_z_63d_slope_v034_signal(units):
    base = _z(units, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z units
def gm_f74_biotech_f74_institutional_holder_concentration_z_63d_slope_v035_signal(units):
    base = _z(units, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z units
def gm_f74_biotech_f74_institutional_holder_concentration_z_63d_slope_v036_signal(units):
    base = _z(units, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z units
def gm_f74_biotech_f74_institutional_holder_concentration_z_126d_slope_v037_signal(units):
    base = _z(units, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z units
def gm_f74_biotech_f74_institutional_holder_concentration_z_126d_slope_v038_signal(units):
    base = _z(units, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z units
def gm_f74_biotech_f74_institutional_holder_concentration_z_126d_slope_v039_signal(units):
    base = _z(units, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z units
def gm_f74_biotech_f74_institutional_holder_concentration_z_252d_slope_v040_signal(units):
    base = _z(units, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z units
def gm_f74_biotech_f74_institutional_holder_concentration_z_252d_slope_v041_signal(units):
    base = _z(units, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z units
def gm_f74_biotech_f74_institutional_holder_concentration_z_252d_slope_v042_signal(units):
    base = _z(units, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z units
def gm_f74_biotech_f74_institutional_holder_concentration_z_504d_slope_v043_signal(units):
    base = _z(units, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z units
def gm_f74_biotech_f74_institutional_holder_concentration_z_504d_slope_v044_signal(units):
    base = _z(units, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z units
def gm_f74_biotech_f74_institutional_holder_concentration_z_504d_slope_v045_signal(units):
    base = _z(units, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps units
def gm_f74_biotech_f74_institutional_holder_concentration_ps_21d_slope_v046_signal(units, sharesbas):
    base = _safe_div(_mean(units, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps units
def gm_f74_biotech_f74_institutional_holder_concentration_ps_21d_slope_v047_signal(units, sharesbas):
    base = _safe_div(_mean(units, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps units
def gm_f74_biotech_f74_institutional_holder_concentration_ps_21d_slope_v048_signal(units, sharesbas):
    base = _safe_div(_mean(units, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps units
def gm_f74_biotech_f74_institutional_holder_concentration_ps_63d_slope_v049_signal(units, sharesbas):
    base = _safe_div(_mean(units, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps units
def gm_f74_biotech_f74_institutional_holder_concentration_ps_63d_slope_v050_signal(units, sharesbas):
    base = _safe_div(_mean(units, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps units
def gm_f74_biotech_f74_institutional_holder_concentration_ps_63d_slope_v051_signal(units, sharesbas):
    base = _safe_div(_mean(units, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps units
def gm_f74_biotech_f74_institutional_holder_concentration_ps_126d_slope_v052_signal(units, sharesbas):
    base = _safe_div(_mean(units, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps units
def gm_f74_biotech_f74_institutional_holder_concentration_ps_126d_slope_v053_signal(units, sharesbas):
    base = _safe_div(_mean(units, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps units
def gm_f74_biotech_f74_institutional_holder_concentration_ps_126d_slope_v054_signal(units, sharesbas):
    base = _safe_div(_mean(units, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps units
def gm_f74_biotech_f74_institutional_holder_concentration_ps_252d_slope_v055_signal(units, sharesbas):
    base = _safe_div(_mean(units, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps units
def gm_f74_biotech_f74_institutional_holder_concentration_ps_252d_slope_v056_signal(units, sharesbas):
    base = _safe_div(_mean(units, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps units
def gm_f74_biotech_f74_institutional_holder_concentration_ps_252d_slope_v057_signal(units, sharesbas):
    base = _safe_div(_mean(units, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps units
def gm_f74_biotech_f74_institutional_holder_concentration_ps_504d_slope_v058_signal(units, sharesbas):
    base = _safe_div(_mean(units, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps units
def gm_f74_biotech_f74_institutional_holder_concentration_ps_504d_slope_v059_signal(units, sharesbas):
    base = _safe_div(_mean(units, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps units
def gm_f74_biotech_f74_institutional_holder_concentration_ps_504d_slope_v060_signal(units, sharesbas):
    base = _safe_div(_mean(units, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_asset_scaled_21d_slope_v061_signal(units, assets):
    base = _safe_div(_mean(units, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_asset_scaled_21d_slope_v062_signal(units, assets):
    base = _safe_div(_mean(units, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_asset_scaled_21d_slope_v063_signal(units, assets):
    base = _safe_div(_mean(units, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_asset_scaled_63d_slope_v064_signal(units, assets):
    base = _safe_div(_mean(units, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_asset_scaled_63d_slope_v065_signal(units, assets):
    base = _safe_div(_mean(units, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_asset_scaled_63d_slope_v066_signal(units, assets):
    base = _safe_div(_mean(units, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_asset_scaled_126d_slope_v067_signal(units, assets):
    base = _safe_div(_mean(units, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_asset_scaled_126d_slope_v068_signal(units, assets):
    base = _safe_div(_mean(units, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_asset_scaled_126d_slope_v069_signal(units, assets):
    base = _safe_div(_mean(units, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_asset_scaled_252d_slope_v070_signal(units, assets):
    base = _safe_div(_mean(units, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_asset_scaled_252d_slope_v071_signal(units, assets):
    base = _safe_div(_mean(units, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_asset_scaled_252d_slope_v072_signal(units, assets):
    base = _safe_div(_mean(units, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_asset_scaled_504d_slope_v073_signal(units, assets):
    base = _safe_div(_mean(units, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_asset_scaled_504d_slope_v074_signal(units, assets):
    base = _safe_div(_mean(units, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_asset_scaled_504d_slope_v075_signal(units, assets):
    base = _safe_div(_mean(units, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_mcap_scaled_21d_slope_v076_signal(units, marketcap):
    base = _safe_div(_mean(units, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_mcap_scaled_21d_slope_v077_signal(units, marketcap):
    base = _safe_div(_mean(units, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_mcap_scaled_21d_slope_v078_signal(units, marketcap):
    base = _safe_div(_mean(units, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_mcap_scaled_63d_slope_v079_signal(units, marketcap):
    base = _safe_div(_mean(units, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_mcap_scaled_63d_slope_v080_signal(units, marketcap):
    base = _safe_div(_mean(units, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_mcap_scaled_63d_slope_v081_signal(units, marketcap):
    base = _safe_div(_mean(units, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_mcap_scaled_126d_slope_v082_signal(units, marketcap):
    base = _safe_div(_mean(units, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_mcap_scaled_126d_slope_v083_signal(units, marketcap):
    base = _safe_div(_mean(units, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_mcap_scaled_126d_slope_v084_signal(units, marketcap):
    base = _safe_div(_mean(units, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_mcap_scaled_252d_slope_v085_signal(units, marketcap):
    base = _safe_div(_mean(units, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_mcap_scaled_252d_slope_v086_signal(units, marketcap):
    base = _safe_div(_mean(units, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_mcap_scaled_252d_slope_v087_signal(units, marketcap):
    base = _safe_div(_mean(units, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_mcap_scaled_504d_slope_v088_signal(units, marketcap):
    base = _safe_div(_mean(units, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_mcap_scaled_504d_slope_v089_signal(units, marketcap):
    base = _safe_div(_mean(units, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled units
def gm_f74_biotech_f74_institutional_holder_concentration_mcap_scaled_504d_slope_v090_signal(units, marketcap):
    base = _safe_div(_mean(units, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_low_21d_slope_v091_signal(units):
    base = _safe_div(units - units.rolling(21).min(), units.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_low_21d_slope_v092_signal(units):
    base = _safe_div(units - units.rolling(21).min(), units.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_low_21d_slope_v093_signal(units):
    base = _safe_div(units - units.rolling(21).min(), units.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_low_63d_slope_v094_signal(units):
    base = _safe_div(units - units.rolling(63).min(), units.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_low_63d_slope_v095_signal(units):
    base = _safe_div(units - units.rolling(63).min(), units.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_low_63d_slope_v096_signal(units):
    base = _safe_div(units - units.rolling(63).min(), units.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_low_126d_slope_v097_signal(units):
    base = _safe_div(units - units.rolling(126).min(), units.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_low_126d_slope_v098_signal(units):
    base = _safe_div(units - units.rolling(126).min(), units.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_low_126d_slope_v099_signal(units):
    base = _safe_div(units - units.rolling(126).min(), units.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_low_252d_slope_v100_signal(units):
    base = _safe_div(units - units.rolling(252).min(), units.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_low_252d_slope_v101_signal(units):
    base = _safe_div(units - units.rolling(252).min(), units.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_low_252d_slope_v102_signal(units):
    base = _safe_div(units - units.rolling(252).min(), units.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_low_504d_slope_v103_signal(units):
    base = _safe_div(units - units.rolling(504).min(), units.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_low_504d_slope_v104_signal(units):
    base = _safe_div(units - units.rolling(504).min(), units.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_low_504d_slope_v105_signal(units):
    base = _safe_div(units - units.rolling(504).min(), units.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_high_21d_slope_v106_signal(units):
    base = _safe_div(units.rolling(21).max() - units, units.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_high_21d_slope_v107_signal(units):
    base = _safe_div(units.rolling(21).max() - units, units.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_high_21d_slope_v108_signal(units):
    base = _safe_div(units.rolling(21).max() - units, units.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_high_63d_slope_v109_signal(units):
    base = _safe_div(units.rolling(63).max() - units, units.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_high_63d_slope_v110_signal(units):
    base = _safe_div(units.rolling(63).max() - units, units.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_high_63d_slope_v111_signal(units):
    base = _safe_div(units.rolling(63).max() - units, units.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_high_126d_slope_v112_signal(units):
    base = _safe_div(units.rolling(126).max() - units, units.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_high_126d_slope_v113_signal(units):
    base = _safe_div(units.rolling(126).max() - units, units.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_high_126d_slope_v114_signal(units):
    base = _safe_div(units.rolling(126).max() - units, units.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_high_252d_slope_v115_signal(units):
    base = _safe_div(units.rolling(252).max() - units, units.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_high_252d_slope_v116_signal(units):
    base = _safe_div(units.rolling(252).max() - units, units.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_high_252d_slope_v117_signal(units):
    base = _safe_div(units.rolling(252).max() - units, units.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_high_504d_slope_v118_signal(units):
    base = _safe_div(units.rolling(504).max() - units, units.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_high_504d_slope_v119_signal(units):
    base = _safe_div(units.rolling(504).max() - units, units.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high units
def gm_f74_biotech_f74_institutional_holder_concentration_dist_high_504d_slope_v120_signal(units):
    base = _safe_div(units.rolling(504).max() - units, units.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom units
def gm_f74_biotech_f74_institutional_holder_concentration_mom_21d_slope_v121_signal(units):
    base = _safe_div(_mean(units, 21) - _mean(units, 42), _mean(units, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom units
def gm_f74_biotech_f74_institutional_holder_concentration_mom_21d_slope_v122_signal(units):
    base = _safe_div(_mean(units, 21) - _mean(units, 42), _mean(units, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom units
def gm_f74_biotech_f74_institutional_holder_concentration_mom_21d_slope_v123_signal(units):
    base = _safe_div(_mean(units, 21) - _mean(units, 42), _mean(units, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom units
def gm_f74_biotech_f74_institutional_holder_concentration_mom_63d_slope_v124_signal(units):
    base = _safe_div(_mean(units, 63) - _mean(units, 126), _mean(units, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom units
def gm_f74_biotech_f74_institutional_holder_concentration_mom_63d_slope_v125_signal(units):
    base = _safe_div(_mean(units, 63) - _mean(units, 126), _mean(units, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom units
def gm_f74_biotech_f74_institutional_holder_concentration_mom_63d_slope_v126_signal(units):
    base = _safe_div(_mean(units, 63) - _mean(units, 126), _mean(units, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom units
def gm_f74_biotech_f74_institutional_holder_concentration_mom_126d_slope_v127_signal(units):
    base = _safe_div(_mean(units, 126) - _mean(units, 252), _mean(units, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom units
def gm_f74_biotech_f74_institutional_holder_concentration_mom_126d_slope_v128_signal(units):
    base = _safe_div(_mean(units, 126) - _mean(units, 252), _mean(units, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom units
def gm_f74_biotech_f74_institutional_holder_concentration_mom_126d_slope_v129_signal(units):
    base = _safe_div(_mean(units, 126) - _mean(units, 252), _mean(units, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom units
def gm_f74_biotech_f74_institutional_holder_concentration_mom_252d_slope_v130_signal(units):
    base = _safe_div(_mean(units, 252) - _mean(units, 504), _mean(units, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom units
def gm_f74_biotech_f74_institutional_holder_concentration_mom_252d_slope_v131_signal(units):
    base = _safe_div(_mean(units, 252) - _mean(units, 504), _mean(units, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom units
def gm_f74_biotech_f74_institutional_holder_concentration_mom_252d_slope_v132_signal(units):
    base = _safe_div(_mean(units, 252) - _mean(units, 504), _mean(units, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom units
def gm_f74_biotech_f74_institutional_holder_concentration_mom_504d_slope_v133_signal(units):
    base = _safe_div(_mean(units, 504) - _mean(units, 1008), _mean(units, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom units
def gm_f74_biotech_f74_institutional_holder_concentration_mom_504d_slope_v134_signal(units):
    base = _safe_div(_mean(units, 504) - _mean(units, 1008), _mean(units, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom units
def gm_f74_biotech_f74_institutional_holder_concentration_mom_504d_slope_v135_signal(units):
    base = _safe_div(_mean(units, 504) - _mean(units, 1008), _mean(units, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol units
def gm_f74_biotech_f74_institutional_holder_concentration_vol_21d_slope_v136_signal(units):
    base = _std(units, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol units
def gm_f74_biotech_f74_institutional_holder_concentration_vol_21d_slope_v137_signal(units):
    base = _std(units, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol units
def gm_f74_biotech_f74_institutional_holder_concentration_vol_21d_slope_v138_signal(units):
    base = _std(units, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol units
def gm_f74_biotech_f74_institutional_holder_concentration_vol_63d_slope_v139_signal(units):
    base = _std(units, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol units
def gm_f74_biotech_f74_institutional_holder_concentration_vol_63d_slope_v140_signal(units):
    base = _std(units, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol units
def gm_f74_biotech_f74_institutional_holder_concentration_vol_63d_slope_v141_signal(units):
    base = _std(units, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol units
def gm_f74_biotech_f74_institutional_holder_concentration_vol_126d_slope_v142_signal(units):
    base = _std(units, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol units
def gm_f74_biotech_f74_institutional_holder_concentration_vol_126d_slope_v143_signal(units):
    base = _std(units, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol units
def gm_f74_biotech_f74_institutional_holder_concentration_vol_126d_slope_v144_signal(units):
    base = _std(units, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol units
def gm_f74_biotech_f74_institutional_holder_concentration_vol_252d_slope_v145_signal(units):
    base = _std(units, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol units
def gm_f74_biotech_f74_institutional_holder_concentration_vol_252d_slope_v146_signal(units):
    base = _std(units, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol units
def gm_f74_biotech_f74_institutional_holder_concentration_vol_252d_slope_v147_signal(units):
    base = _std(units, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol units
def gm_f74_biotech_f74_institutional_holder_concentration_vol_504d_slope_v148_signal(units):
    base = _std(units, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol units
def gm_f74_biotech_f74_institutional_holder_concentration_vol_504d_slope_v149_signal(units):
    base = _std(units, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol units
def gm_f74_biotech_f74_institutional_holder_concentration_vol_504d_slope_v150_signal(units):
    base = _std(units, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

