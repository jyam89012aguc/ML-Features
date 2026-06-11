
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_21d_accel_v001_signal(cor):
    base = _mean(cor, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_21d_accel_v002_signal(cor):
    base = _mean(cor, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_21d_accel_v003_signal(cor):
    base = _mean(cor, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_63d_accel_v004_signal(cor):
    base = _mean(cor, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_63d_accel_v005_signal(cor):
    base = _mean(cor, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_63d_accel_v006_signal(cor):
    base = _mean(cor, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_126d_accel_v007_signal(cor):
    base = _mean(cor, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_126d_accel_v008_signal(cor):
    base = _mean(cor, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_126d_accel_v009_signal(cor):
    base = _mean(cor, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_252d_accel_v010_signal(cor):
    base = _mean(cor, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_252d_accel_v011_signal(cor):
    base = _mean(cor, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_252d_accel_v012_signal(cor):
    base = _mean(cor, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_504d_accel_v013_signal(cor):
    base = _mean(cor, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_504d_accel_v014_signal(cor):
    base = _mean(cor, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_504d_accel_v015_signal(cor):
    base = _mean(cor, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_21d_accel_v016_signal(cor):
    base = _mean(_log(cor), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_21d_accel_v017_signal(cor):
    base = _mean(_log(cor), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_21d_accel_v018_signal(cor):
    base = _mean(_log(cor), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_63d_accel_v019_signal(cor):
    base = _mean(_log(cor), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_63d_accel_v020_signal(cor):
    base = _mean(_log(cor), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_63d_accel_v021_signal(cor):
    base = _mean(_log(cor), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_126d_accel_v022_signal(cor):
    base = _mean(_log(cor), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_126d_accel_v023_signal(cor):
    base = _mean(_log(cor), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_126d_accel_v024_signal(cor):
    base = _mean(_log(cor), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_252d_accel_v025_signal(cor):
    base = _mean(_log(cor), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_252d_accel_v026_signal(cor):
    base = _mean(_log(cor), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_252d_accel_v027_signal(cor):
    base = _mean(_log(cor), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_504d_accel_v028_signal(cor):
    base = _mean(_log(cor), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_504d_accel_v029_signal(cor):
    base = _mean(_log(cor), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_504d_accel_v030_signal(cor):
    base = _mean(_log(cor), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_21d_accel_v031_signal(cor):
    base = _z(cor, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_21d_accel_v032_signal(cor):
    base = _z(cor, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_21d_accel_v033_signal(cor):
    base = _z(cor, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_63d_accel_v034_signal(cor):
    base = _z(cor, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_63d_accel_v035_signal(cor):
    base = _z(cor, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_63d_accel_v036_signal(cor):
    base = _z(cor, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_126d_accel_v037_signal(cor):
    base = _z(cor, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_126d_accel_v038_signal(cor):
    base = _z(cor, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_126d_accel_v039_signal(cor):
    base = _z(cor, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_252d_accel_v040_signal(cor):
    base = _z(cor, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_252d_accel_v041_signal(cor):
    base = _z(cor, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_252d_accel_v042_signal(cor):
    base = _z(cor, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_504d_accel_v043_signal(cor):
    base = _z(cor, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_504d_accel_v044_signal(cor):
    base = _z(cor, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_504d_accel_v045_signal(cor):
    base = _z(cor, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_21d_accel_v046_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_21d_accel_v047_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_21d_accel_v048_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_63d_accel_v049_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_63d_accel_v050_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_63d_accel_v051_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_126d_accel_v052_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_126d_accel_v053_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_126d_accel_v054_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_252d_accel_v055_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_252d_accel_v056_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_252d_accel_v057_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_504d_accel_v058_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_504d_accel_v059_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_504d_accel_v060_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_21d_accel_v061_signal(cor, assets):
    base = _safe_div(_mean(cor, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_21d_accel_v062_signal(cor, assets):
    base = _safe_div(_mean(cor, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_21d_accel_v063_signal(cor, assets):
    base = _safe_div(_mean(cor, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_63d_accel_v064_signal(cor, assets):
    base = _safe_div(_mean(cor, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_63d_accel_v065_signal(cor, assets):
    base = _safe_div(_mean(cor, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_63d_accel_v066_signal(cor, assets):
    base = _safe_div(_mean(cor, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_126d_accel_v067_signal(cor, assets):
    base = _safe_div(_mean(cor, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_126d_accel_v068_signal(cor, assets):
    base = _safe_div(_mean(cor, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_126d_accel_v069_signal(cor, assets):
    base = _safe_div(_mean(cor, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_252d_accel_v070_signal(cor, assets):
    base = _safe_div(_mean(cor, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_252d_accel_v071_signal(cor, assets):
    base = _safe_div(_mean(cor, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_252d_accel_v072_signal(cor, assets):
    base = _safe_div(_mean(cor, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_504d_accel_v073_signal(cor, assets):
    base = _safe_div(_mean(cor, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_504d_accel_v074_signal(cor, assets):
    base = _safe_div(_mean(cor, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_504d_accel_v075_signal(cor, assets):
    base = _safe_div(_mean(cor, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_21d_accel_v076_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_21d_accel_v077_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_21d_accel_v078_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_63d_accel_v079_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_63d_accel_v080_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_63d_accel_v081_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_126d_accel_v082_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_126d_accel_v083_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_126d_accel_v084_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_252d_accel_v085_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_252d_accel_v086_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_252d_accel_v087_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_504d_accel_v088_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_504d_accel_v089_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_504d_accel_v090_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_21d_accel_v091_signal(cor):
    base = _safe_div(cor - cor.rolling(21).min(), cor.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_21d_accel_v092_signal(cor):
    base = _safe_div(cor - cor.rolling(21).min(), cor.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_21d_accel_v093_signal(cor):
    base = _safe_div(cor - cor.rolling(21).min(), cor.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_63d_accel_v094_signal(cor):
    base = _safe_div(cor - cor.rolling(63).min(), cor.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_63d_accel_v095_signal(cor):
    base = _safe_div(cor - cor.rolling(63).min(), cor.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_63d_accel_v096_signal(cor):
    base = _safe_div(cor - cor.rolling(63).min(), cor.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_126d_accel_v097_signal(cor):
    base = _safe_div(cor - cor.rolling(126).min(), cor.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_126d_accel_v098_signal(cor):
    base = _safe_div(cor - cor.rolling(126).min(), cor.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_126d_accel_v099_signal(cor):
    base = _safe_div(cor - cor.rolling(126).min(), cor.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_252d_accel_v100_signal(cor):
    base = _safe_div(cor - cor.rolling(252).min(), cor.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_252d_accel_v101_signal(cor):
    base = _safe_div(cor - cor.rolling(252).min(), cor.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_252d_accel_v102_signal(cor):
    base = _safe_div(cor - cor.rolling(252).min(), cor.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_504d_accel_v103_signal(cor):
    base = _safe_div(cor - cor.rolling(504).min(), cor.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_504d_accel_v104_signal(cor):
    base = _safe_div(cor - cor.rolling(504).min(), cor.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_504d_accel_v105_signal(cor):
    base = _safe_div(cor - cor.rolling(504).min(), cor.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_21d_accel_v106_signal(cor):
    base = _safe_div(cor.rolling(21).max() - cor, cor.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_21d_accel_v107_signal(cor):
    base = _safe_div(cor.rolling(21).max() - cor, cor.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_21d_accel_v108_signal(cor):
    base = _safe_div(cor.rolling(21).max() - cor, cor.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_63d_accel_v109_signal(cor):
    base = _safe_div(cor.rolling(63).max() - cor, cor.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_63d_accel_v110_signal(cor):
    base = _safe_div(cor.rolling(63).max() - cor, cor.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_63d_accel_v111_signal(cor):
    base = _safe_div(cor.rolling(63).max() - cor, cor.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_126d_accel_v112_signal(cor):
    base = _safe_div(cor.rolling(126).max() - cor, cor.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_126d_accel_v113_signal(cor):
    base = _safe_div(cor.rolling(126).max() - cor, cor.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_126d_accel_v114_signal(cor):
    base = _safe_div(cor.rolling(126).max() - cor, cor.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_252d_accel_v115_signal(cor):
    base = _safe_div(cor.rolling(252).max() - cor, cor.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_252d_accel_v116_signal(cor):
    base = _safe_div(cor.rolling(252).max() - cor, cor.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_252d_accel_v117_signal(cor):
    base = _safe_div(cor.rolling(252).max() - cor, cor.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_504d_accel_v118_signal(cor):
    base = _safe_div(cor.rolling(504).max() - cor, cor.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_504d_accel_v119_signal(cor):
    base = _safe_div(cor.rolling(504).max() - cor, cor.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_504d_accel_v120_signal(cor):
    base = _safe_div(cor.rolling(504).max() - cor, cor.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_21d_accel_v121_signal(cor):
    base = _safe_div(_mean(cor, 21) - _mean(cor, 42), _mean(cor, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_21d_accel_v122_signal(cor):
    base = _safe_div(_mean(cor, 21) - _mean(cor, 42), _mean(cor, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_21d_accel_v123_signal(cor):
    base = _safe_div(_mean(cor, 21) - _mean(cor, 42), _mean(cor, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_63d_accel_v124_signal(cor):
    base = _safe_div(_mean(cor, 63) - _mean(cor, 126), _mean(cor, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_63d_accel_v125_signal(cor):
    base = _safe_div(_mean(cor, 63) - _mean(cor, 126), _mean(cor, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_63d_accel_v126_signal(cor):
    base = _safe_div(_mean(cor, 63) - _mean(cor, 126), _mean(cor, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_126d_accel_v127_signal(cor):
    base = _safe_div(_mean(cor, 126) - _mean(cor, 252), _mean(cor, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_126d_accel_v128_signal(cor):
    base = _safe_div(_mean(cor, 126) - _mean(cor, 252), _mean(cor, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_126d_accel_v129_signal(cor):
    base = _safe_div(_mean(cor, 126) - _mean(cor, 252), _mean(cor, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_252d_accel_v130_signal(cor):
    base = _safe_div(_mean(cor, 252) - _mean(cor, 504), _mean(cor, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_252d_accel_v131_signal(cor):
    base = _safe_div(_mean(cor, 252) - _mean(cor, 504), _mean(cor, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_252d_accel_v132_signal(cor):
    base = _safe_div(_mean(cor, 252) - _mean(cor, 504), _mean(cor, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_504d_accel_v133_signal(cor):
    base = _safe_div(_mean(cor, 504) - _mean(cor, 1008), _mean(cor, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_504d_accel_v134_signal(cor):
    base = _safe_div(_mean(cor, 504) - _mean(cor, 1008), _mean(cor, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_504d_accel_v135_signal(cor):
    base = _safe_div(_mean(cor, 504) - _mean(cor, 1008), _mean(cor, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_21d_accel_v136_signal(cor):
    base = _std(cor, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_21d_accel_v137_signal(cor):
    base = _std(cor, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_21d_accel_v138_signal(cor):
    base = _std(cor, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_63d_accel_v139_signal(cor):
    base = _std(cor, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_63d_accel_v140_signal(cor):
    base = _std(cor, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_63d_accel_v141_signal(cor):
    base = _std(cor, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_126d_accel_v142_signal(cor):
    base = _std(cor, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_126d_accel_v143_signal(cor):
    base = _std(cor, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_126d_accel_v144_signal(cor):
    base = _std(cor, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_252d_accel_v145_signal(cor):
    base = _std(cor, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_252d_accel_v146_signal(cor):
    base = _std(cor, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_252d_accel_v147_signal(cor):
    base = _std(cor, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_504d_accel_v148_signal(cor):
    base = _std(cor, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_504d_accel_v149_signal(cor):
    base = _std(cor, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_504d_accel_v150_signal(cor):
    base = _std(cor, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

