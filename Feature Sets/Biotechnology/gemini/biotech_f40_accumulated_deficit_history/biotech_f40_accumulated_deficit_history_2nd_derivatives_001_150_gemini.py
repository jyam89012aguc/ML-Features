
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_21d_slope_v001_signal(retearn):
    base = _mean(retearn, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_21d_slope_v002_signal(retearn):
    base = _mean(retearn, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_21d_slope_v003_signal(retearn):
    base = _mean(retearn, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_63d_slope_v004_signal(retearn):
    base = _mean(retearn, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_63d_slope_v005_signal(retearn):
    base = _mean(retearn, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_63d_slope_v006_signal(retearn):
    base = _mean(retearn, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_126d_slope_v007_signal(retearn):
    base = _mean(retearn, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_126d_slope_v008_signal(retearn):
    base = _mean(retearn, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_126d_slope_v009_signal(retearn):
    base = _mean(retearn, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_252d_slope_v010_signal(retearn):
    base = _mean(retearn, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_252d_slope_v011_signal(retearn):
    base = _mean(retearn, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_252d_slope_v012_signal(retearn):
    base = _mean(retearn, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_504d_slope_v013_signal(retearn):
    base = _mean(retearn, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_504d_slope_v014_signal(retearn):
    base = _mean(retearn, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw retearn
def gm_f40_biotech_f40_accumulated_deficit_history_raw_504d_slope_v015_signal(retearn):
    base = _mean(retearn, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_21d_slope_v016_signal(retearn):
    base = _mean(_log(retearn), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_21d_slope_v017_signal(retearn):
    base = _mean(_log(retearn), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_21d_slope_v018_signal(retearn):
    base = _mean(_log(retearn), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_63d_slope_v019_signal(retearn):
    base = _mean(_log(retearn), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_63d_slope_v020_signal(retearn):
    base = _mean(_log(retearn), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_63d_slope_v021_signal(retearn):
    base = _mean(_log(retearn), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_126d_slope_v022_signal(retearn):
    base = _mean(_log(retearn), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_126d_slope_v023_signal(retearn):
    base = _mean(_log(retearn), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_126d_slope_v024_signal(retearn):
    base = _mean(_log(retearn), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_252d_slope_v025_signal(retearn):
    base = _mean(_log(retearn), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_252d_slope_v026_signal(retearn):
    base = _mean(_log(retearn), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_252d_slope_v027_signal(retearn):
    base = _mean(_log(retearn), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_504d_slope_v028_signal(retearn):
    base = _mean(_log(retearn), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_504d_slope_v029_signal(retearn):
    base = _mean(_log(retearn), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log retearn
def gm_f40_biotech_f40_accumulated_deficit_history_log_504d_slope_v030_signal(retearn):
    base = _mean(_log(retearn), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_21d_slope_v031_signal(retearn):
    base = _z(retearn, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_21d_slope_v032_signal(retearn):
    base = _z(retearn, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_21d_slope_v033_signal(retearn):
    base = _z(retearn, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_63d_slope_v034_signal(retearn):
    base = _z(retearn, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_63d_slope_v035_signal(retearn):
    base = _z(retearn, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_63d_slope_v036_signal(retearn):
    base = _z(retearn, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_126d_slope_v037_signal(retearn):
    base = _z(retearn, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_126d_slope_v038_signal(retearn):
    base = _z(retearn, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_126d_slope_v039_signal(retearn):
    base = _z(retearn, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_252d_slope_v040_signal(retearn):
    base = _z(retearn, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_252d_slope_v041_signal(retearn):
    base = _z(retearn, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_252d_slope_v042_signal(retearn):
    base = _z(retearn, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_504d_slope_v043_signal(retearn):
    base = _z(retearn, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_504d_slope_v044_signal(retearn):
    base = _z(retearn, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z retearn
def gm_f40_biotech_f40_accumulated_deficit_history_z_504d_slope_v045_signal(retearn):
    base = _z(retearn, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_21d_slope_v046_signal(retearn, sharesbas):
    base = _safe_div(_mean(retearn, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_21d_slope_v047_signal(retearn, sharesbas):
    base = _safe_div(_mean(retearn, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_21d_slope_v048_signal(retearn, sharesbas):
    base = _safe_div(_mean(retearn, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_63d_slope_v049_signal(retearn, sharesbas):
    base = _safe_div(_mean(retearn, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_63d_slope_v050_signal(retearn, sharesbas):
    base = _safe_div(_mean(retearn, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_63d_slope_v051_signal(retearn, sharesbas):
    base = _safe_div(_mean(retearn, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_126d_slope_v052_signal(retearn, sharesbas):
    base = _safe_div(_mean(retearn, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_126d_slope_v053_signal(retearn, sharesbas):
    base = _safe_div(_mean(retearn, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_126d_slope_v054_signal(retearn, sharesbas):
    base = _safe_div(_mean(retearn, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_252d_slope_v055_signal(retearn, sharesbas):
    base = _safe_div(_mean(retearn, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_252d_slope_v056_signal(retearn, sharesbas):
    base = _safe_div(_mean(retearn, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_252d_slope_v057_signal(retearn, sharesbas):
    base = _safe_div(_mean(retearn, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_504d_slope_v058_signal(retearn, sharesbas):
    base = _safe_div(_mean(retearn, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_504d_slope_v059_signal(retearn, sharesbas):
    base = _safe_div(_mean(retearn, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps retearn
def gm_f40_biotech_f40_accumulated_deficit_history_ps_504d_slope_v060_signal(retearn, sharesbas):
    base = _safe_div(_mean(retearn, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_21d_slope_v061_signal(retearn, assets):
    base = _safe_div(_mean(retearn, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_21d_slope_v062_signal(retearn, assets):
    base = _safe_div(_mean(retearn, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_21d_slope_v063_signal(retearn, assets):
    base = _safe_div(_mean(retearn, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_63d_slope_v064_signal(retearn, assets):
    base = _safe_div(_mean(retearn, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_63d_slope_v065_signal(retearn, assets):
    base = _safe_div(_mean(retearn, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_63d_slope_v066_signal(retearn, assets):
    base = _safe_div(_mean(retearn, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_126d_slope_v067_signal(retearn, assets):
    base = _safe_div(_mean(retearn, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_126d_slope_v068_signal(retearn, assets):
    base = _safe_div(_mean(retearn, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_126d_slope_v069_signal(retearn, assets):
    base = _safe_div(_mean(retearn, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_252d_slope_v070_signal(retearn, assets):
    base = _safe_div(_mean(retearn, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_252d_slope_v071_signal(retearn, assets):
    base = _safe_div(_mean(retearn, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_252d_slope_v072_signal(retearn, assets):
    base = _safe_div(_mean(retearn, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_504d_slope_v073_signal(retearn, assets):
    base = _safe_div(_mean(retearn, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_504d_slope_v074_signal(retearn, assets):
    base = _safe_div(_mean(retearn, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_asset_scaled_504d_slope_v075_signal(retearn, assets):
    base = _safe_div(_mean(retearn, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_21d_slope_v076_signal(retearn, marketcap):
    base = _safe_div(_mean(retearn, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_21d_slope_v077_signal(retearn, marketcap):
    base = _safe_div(_mean(retearn, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_21d_slope_v078_signal(retearn, marketcap):
    base = _safe_div(_mean(retearn, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_63d_slope_v079_signal(retearn, marketcap):
    base = _safe_div(_mean(retearn, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_63d_slope_v080_signal(retearn, marketcap):
    base = _safe_div(_mean(retearn, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_63d_slope_v081_signal(retearn, marketcap):
    base = _safe_div(_mean(retearn, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_126d_slope_v082_signal(retearn, marketcap):
    base = _safe_div(_mean(retearn, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_126d_slope_v083_signal(retearn, marketcap):
    base = _safe_div(_mean(retearn, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_126d_slope_v084_signal(retearn, marketcap):
    base = _safe_div(_mean(retearn, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_252d_slope_v085_signal(retearn, marketcap):
    base = _safe_div(_mean(retearn, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_252d_slope_v086_signal(retearn, marketcap):
    base = _safe_div(_mean(retearn, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_252d_slope_v087_signal(retearn, marketcap):
    base = _safe_div(_mean(retearn, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_504d_slope_v088_signal(retearn, marketcap):
    base = _safe_div(_mean(retearn, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_504d_slope_v089_signal(retearn, marketcap):
    base = _safe_div(_mean(retearn, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mcap_scaled_504d_slope_v090_signal(retearn, marketcap):
    base = _safe_div(_mean(retearn, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_21d_slope_v091_signal(retearn):
    base = _safe_div(retearn - retearn.rolling(21).min(), retearn.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_21d_slope_v092_signal(retearn):
    base = _safe_div(retearn - retearn.rolling(21).min(), retearn.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_21d_slope_v093_signal(retearn):
    base = _safe_div(retearn - retearn.rolling(21).min(), retearn.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_63d_slope_v094_signal(retearn):
    base = _safe_div(retearn - retearn.rolling(63).min(), retearn.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_63d_slope_v095_signal(retearn):
    base = _safe_div(retearn - retearn.rolling(63).min(), retearn.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_63d_slope_v096_signal(retearn):
    base = _safe_div(retearn - retearn.rolling(63).min(), retearn.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_126d_slope_v097_signal(retearn):
    base = _safe_div(retearn - retearn.rolling(126).min(), retearn.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_126d_slope_v098_signal(retearn):
    base = _safe_div(retearn - retearn.rolling(126).min(), retearn.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_126d_slope_v099_signal(retearn):
    base = _safe_div(retearn - retearn.rolling(126).min(), retearn.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_252d_slope_v100_signal(retearn):
    base = _safe_div(retearn - retearn.rolling(252).min(), retearn.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_252d_slope_v101_signal(retearn):
    base = _safe_div(retearn - retearn.rolling(252).min(), retearn.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_252d_slope_v102_signal(retearn):
    base = _safe_div(retearn - retearn.rolling(252).min(), retearn.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_504d_slope_v103_signal(retearn):
    base = _safe_div(retearn - retearn.rolling(504).min(), retearn.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_504d_slope_v104_signal(retearn):
    base = _safe_div(retearn - retearn.rolling(504).min(), retearn.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_low_504d_slope_v105_signal(retearn):
    base = _safe_div(retearn - retearn.rolling(504).min(), retearn.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_21d_slope_v106_signal(retearn):
    base = _safe_div(retearn.rolling(21).max() - retearn, retearn.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_21d_slope_v107_signal(retearn):
    base = _safe_div(retearn.rolling(21).max() - retearn, retearn.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_21d_slope_v108_signal(retearn):
    base = _safe_div(retearn.rolling(21).max() - retearn, retearn.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_63d_slope_v109_signal(retearn):
    base = _safe_div(retearn.rolling(63).max() - retearn, retearn.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_63d_slope_v110_signal(retearn):
    base = _safe_div(retearn.rolling(63).max() - retearn, retearn.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_63d_slope_v111_signal(retearn):
    base = _safe_div(retearn.rolling(63).max() - retearn, retearn.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_126d_slope_v112_signal(retearn):
    base = _safe_div(retearn.rolling(126).max() - retearn, retearn.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_126d_slope_v113_signal(retearn):
    base = _safe_div(retearn.rolling(126).max() - retearn, retearn.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_126d_slope_v114_signal(retearn):
    base = _safe_div(retearn.rolling(126).max() - retearn, retearn.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_252d_slope_v115_signal(retearn):
    base = _safe_div(retearn.rolling(252).max() - retearn, retearn.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_252d_slope_v116_signal(retearn):
    base = _safe_div(retearn.rolling(252).max() - retearn, retearn.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_252d_slope_v117_signal(retearn):
    base = _safe_div(retearn.rolling(252).max() - retearn, retearn.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_504d_slope_v118_signal(retearn):
    base = _safe_div(retearn.rolling(504).max() - retearn, retearn.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_504d_slope_v119_signal(retearn):
    base = _safe_div(retearn.rolling(504).max() - retearn, retearn.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high retearn
def gm_f40_biotech_f40_accumulated_deficit_history_dist_high_504d_slope_v120_signal(retearn):
    base = _safe_div(retearn.rolling(504).max() - retearn, retearn.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_21d_slope_v121_signal(retearn):
    base = _safe_div(_mean(retearn, 21) - _mean(retearn, 42), _mean(retearn, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_21d_slope_v122_signal(retearn):
    base = _safe_div(_mean(retearn, 21) - _mean(retearn, 42), _mean(retearn, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_21d_slope_v123_signal(retearn):
    base = _safe_div(_mean(retearn, 21) - _mean(retearn, 42), _mean(retearn, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_63d_slope_v124_signal(retearn):
    base = _safe_div(_mean(retearn, 63) - _mean(retearn, 126), _mean(retearn, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_63d_slope_v125_signal(retearn):
    base = _safe_div(_mean(retearn, 63) - _mean(retearn, 126), _mean(retearn, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_63d_slope_v126_signal(retearn):
    base = _safe_div(_mean(retearn, 63) - _mean(retearn, 126), _mean(retearn, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_126d_slope_v127_signal(retearn):
    base = _safe_div(_mean(retearn, 126) - _mean(retearn, 252), _mean(retearn, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_126d_slope_v128_signal(retearn):
    base = _safe_div(_mean(retearn, 126) - _mean(retearn, 252), _mean(retearn, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_126d_slope_v129_signal(retearn):
    base = _safe_div(_mean(retearn, 126) - _mean(retearn, 252), _mean(retearn, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_252d_slope_v130_signal(retearn):
    base = _safe_div(_mean(retearn, 252) - _mean(retearn, 504), _mean(retearn, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_252d_slope_v131_signal(retearn):
    base = _safe_div(_mean(retearn, 252) - _mean(retearn, 504), _mean(retearn, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_252d_slope_v132_signal(retearn):
    base = _safe_div(_mean(retearn, 252) - _mean(retearn, 504), _mean(retearn, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_504d_slope_v133_signal(retearn):
    base = _safe_div(_mean(retearn, 504) - _mean(retearn, 1008), _mean(retearn, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_504d_slope_v134_signal(retearn):
    base = _safe_div(_mean(retearn, 504) - _mean(retearn, 1008), _mean(retearn, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom retearn
def gm_f40_biotech_f40_accumulated_deficit_history_mom_504d_slope_v135_signal(retearn):
    base = _safe_div(_mean(retearn, 504) - _mean(retearn, 1008), _mean(retearn, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol retearn
def gm_f40_biotech_f40_accumulated_deficit_history_vol_21d_slope_v136_signal(retearn):
    base = _std(retearn, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol retearn
def gm_f40_biotech_f40_accumulated_deficit_history_vol_21d_slope_v137_signal(retearn):
    base = _std(retearn, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol retearn
def gm_f40_biotech_f40_accumulated_deficit_history_vol_21d_slope_v138_signal(retearn):
    base = _std(retearn, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol retearn
def gm_f40_biotech_f40_accumulated_deficit_history_vol_63d_slope_v139_signal(retearn):
    base = _std(retearn, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol retearn
def gm_f40_biotech_f40_accumulated_deficit_history_vol_63d_slope_v140_signal(retearn):
    base = _std(retearn, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol retearn
def gm_f40_biotech_f40_accumulated_deficit_history_vol_63d_slope_v141_signal(retearn):
    base = _std(retearn, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol retearn
def gm_f40_biotech_f40_accumulated_deficit_history_vol_126d_slope_v142_signal(retearn):
    base = _std(retearn, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol retearn
def gm_f40_biotech_f40_accumulated_deficit_history_vol_126d_slope_v143_signal(retearn):
    base = _std(retearn, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol retearn
def gm_f40_biotech_f40_accumulated_deficit_history_vol_126d_slope_v144_signal(retearn):
    base = _std(retearn, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol retearn
def gm_f40_biotech_f40_accumulated_deficit_history_vol_252d_slope_v145_signal(retearn):
    base = _std(retearn, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol retearn
def gm_f40_biotech_f40_accumulated_deficit_history_vol_252d_slope_v146_signal(retearn):
    base = _std(retearn, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol retearn
def gm_f40_biotech_f40_accumulated_deficit_history_vol_252d_slope_v147_signal(retearn):
    base = _std(retearn, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol retearn
def gm_f40_biotech_f40_accumulated_deficit_history_vol_504d_slope_v148_signal(retearn):
    base = _std(retearn, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol retearn
def gm_f40_biotech_f40_accumulated_deficit_history_vol_504d_slope_v149_signal(retearn):
    base = _std(retearn, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol retearn
def gm_f40_biotech_f40_accumulated_deficit_history_vol_504d_slope_v150_signal(retearn):
    base = _std(retearn, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

