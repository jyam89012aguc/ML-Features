
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_21d_accel_v001_signal(equity):
    base = _mean(equity, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_21d_accel_v002_signal(equity):
    base = _mean(equity, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_21d_accel_v003_signal(equity):
    base = _mean(equity, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_63d_accel_v004_signal(equity):
    base = _mean(equity, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_63d_accel_v005_signal(equity):
    base = _mean(equity, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_63d_accel_v006_signal(equity):
    base = _mean(equity, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_126d_accel_v007_signal(equity):
    base = _mean(equity, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_126d_accel_v008_signal(equity):
    base = _mean(equity, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_126d_accel_v009_signal(equity):
    base = _mean(equity, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_252d_accel_v010_signal(equity):
    base = _mean(equity, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_252d_accel_v011_signal(equity):
    base = _mean(equity, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_252d_accel_v012_signal(equity):
    base = _mean(equity, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_504d_accel_v013_signal(equity):
    base = _mean(equity, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_504d_accel_v014_signal(equity):
    base = _mean(equity, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_504d_accel_v015_signal(equity):
    base = _mean(equity, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_21d_accel_v016_signal(equity):
    base = _mean(_log(equity), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_21d_accel_v017_signal(equity):
    base = _mean(_log(equity), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_21d_accel_v018_signal(equity):
    base = _mean(_log(equity), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_63d_accel_v019_signal(equity):
    base = _mean(_log(equity), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_63d_accel_v020_signal(equity):
    base = _mean(_log(equity), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_63d_accel_v021_signal(equity):
    base = _mean(_log(equity), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_126d_accel_v022_signal(equity):
    base = _mean(_log(equity), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_126d_accel_v023_signal(equity):
    base = _mean(_log(equity), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_126d_accel_v024_signal(equity):
    base = _mean(_log(equity), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_252d_accel_v025_signal(equity):
    base = _mean(_log(equity), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_252d_accel_v026_signal(equity):
    base = _mean(_log(equity), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_252d_accel_v027_signal(equity):
    base = _mean(_log(equity), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_504d_accel_v028_signal(equity):
    base = _mean(_log(equity), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_504d_accel_v029_signal(equity):
    base = _mean(_log(equity), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_504d_accel_v030_signal(equity):
    base = _mean(_log(equity), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_21d_accel_v031_signal(equity):
    base = _z(equity, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_21d_accel_v032_signal(equity):
    base = _z(equity, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_21d_accel_v033_signal(equity):
    base = _z(equity, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_63d_accel_v034_signal(equity):
    base = _z(equity, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_63d_accel_v035_signal(equity):
    base = _z(equity, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_63d_accel_v036_signal(equity):
    base = _z(equity, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_126d_accel_v037_signal(equity):
    base = _z(equity, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_126d_accel_v038_signal(equity):
    base = _z(equity, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_126d_accel_v039_signal(equity):
    base = _z(equity, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_252d_accel_v040_signal(equity):
    base = _z(equity, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_252d_accel_v041_signal(equity):
    base = _z(equity, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_252d_accel_v042_signal(equity):
    base = _z(equity, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_504d_accel_v043_signal(equity):
    base = _z(equity, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_504d_accel_v044_signal(equity):
    base = _z(equity, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_504d_accel_v045_signal(equity):
    base = _z(equity, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_21d_accel_v046_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_21d_accel_v047_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_21d_accel_v048_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_63d_accel_v049_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_63d_accel_v050_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_63d_accel_v051_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_126d_accel_v052_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_126d_accel_v053_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_126d_accel_v054_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_252d_accel_v055_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_252d_accel_v056_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_252d_accel_v057_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_504d_accel_v058_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_504d_accel_v059_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_504d_accel_v060_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_21d_accel_v061_signal(equity, assets):
    base = _safe_div(_mean(equity, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_21d_accel_v062_signal(equity, assets):
    base = _safe_div(_mean(equity, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_21d_accel_v063_signal(equity, assets):
    base = _safe_div(_mean(equity, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_63d_accel_v064_signal(equity, assets):
    base = _safe_div(_mean(equity, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_63d_accel_v065_signal(equity, assets):
    base = _safe_div(_mean(equity, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_63d_accel_v066_signal(equity, assets):
    base = _safe_div(_mean(equity, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_126d_accel_v067_signal(equity, assets):
    base = _safe_div(_mean(equity, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_126d_accel_v068_signal(equity, assets):
    base = _safe_div(_mean(equity, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_126d_accel_v069_signal(equity, assets):
    base = _safe_div(_mean(equity, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_252d_accel_v070_signal(equity, assets):
    base = _safe_div(_mean(equity, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_252d_accel_v071_signal(equity, assets):
    base = _safe_div(_mean(equity, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_252d_accel_v072_signal(equity, assets):
    base = _safe_div(_mean(equity, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_504d_accel_v073_signal(equity, assets):
    base = _safe_div(_mean(equity, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_504d_accel_v074_signal(equity, assets):
    base = _safe_div(_mean(equity, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_504d_accel_v075_signal(equity, assets):
    base = _safe_div(_mean(equity, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_21d_accel_v076_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_21d_accel_v077_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_21d_accel_v078_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_63d_accel_v079_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_63d_accel_v080_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_63d_accel_v081_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_126d_accel_v082_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_126d_accel_v083_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_126d_accel_v084_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_252d_accel_v085_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_252d_accel_v086_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_252d_accel_v087_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_504d_accel_v088_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_504d_accel_v089_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_504d_accel_v090_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_21d_accel_v091_signal(equity):
    base = _safe_div(equity - equity.rolling(21).min(), equity.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_21d_accel_v092_signal(equity):
    base = _safe_div(equity - equity.rolling(21).min(), equity.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_21d_accel_v093_signal(equity):
    base = _safe_div(equity - equity.rolling(21).min(), equity.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_63d_accel_v094_signal(equity):
    base = _safe_div(equity - equity.rolling(63).min(), equity.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_63d_accel_v095_signal(equity):
    base = _safe_div(equity - equity.rolling(63).min(), equity.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_63d_accel_v096_signal(equity):
    base = _safe_div(equity - equity.rolling(63).min(), equity.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_126d_accel_v097_signal(equity):
    base = _safe_div(equity - equity.rolling(126).min(), equity.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_126d_accel_v098_signal(equity):
    base = _safe_div(equity - equity.rolling(126).min(), equity.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_126d_accel_v099_signal(equity):
    base = _safe_div(equity - equity.rolling(126).min(), equity.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_252d_accel_v100_signal(equity):
    base = _safe_div(equity - equity.rolling(252).min(), equity.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_252d_accel_v101_signal(equity):
    base = _safe_div(equity - equity.rolling(252).min(), equity.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_252d_accel_v102_signal(equity):
    base = _safe_div(equity - equity.rolling(252).min(), equity.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_504d_accel_v103_signal(equity):
    base = _safe_div(equity - equity.rolling(504).min(), equity.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_504d_accel_v104_signal(equity):
    base = _safe_div(equity - equity.rolling(504).min(), equity.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_504d_accel_v105_signal(equity):
    base = _safe_div(equity - equity.rolling(504).min(), equity.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_21d_accel_v106_signal(equity):
    base = _safe_div(equity.rolling(21).max() - equity, equity.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_21d_accel_v107_signal(equity):
    base = _safe_div(equity.rolling(21).max() - equity, equity.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_21d_accel_v108_signal(equity):
    base = _safe_div(equity.rolling(21).max() - equity, equity.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_63d_accel_v109_signal(equity):
    base = _safe_div(equity.rolling(63).max() - equity, equity.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_63d_accel_v110_signal(equity):
    base = _safe_div(equity.rolling(63).max() - equity, equity.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_63d_accel_v111_signal(equity):
    base = _safe_div(equity.rolling(63).max() - equity, equity.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_126d_accel_v112_signal(equity):
    base = _safe_div(equity.rolling(126).max() - equity, equity.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_126d_accel_v113_signal(equity):
    base = _safe_div(equity.rolling(126).max() - equity, equity.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_126d_accel_v114_signal(equity):
    base = _safe_div(equity.rolling(126).max() - equity, equity.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_252d_accel_v115_signal(equity):
    base = _safe_div(equity.rolling(252).max() - equity, equity.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_252d_accel_v116_signal(equity):
    base = _safe_div(equity.rolling(252).max() - equity, equity.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_252d_accel_v117_signal(equity):
    base = _safe_div(equity.rolling(252).max() - equity, equity.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_504d_accel_v118_signal(equity):
    base = _safe_div(equity.rolling(504).max() - equity, equity.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_504d_accel_v119_signal(equity):
    base = _safe_div(equity.rolling(504).max() - equity, equity.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_504d_accel_v120_signal(equity):
    base = _safe_div(equity.rolling(504).max() - equity, equity.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_21d_accel_v121_signal(equity):
    base = _safe_div(_mean(equity, 21) - _mean(equity, 42), _mean(equity, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_21d_accel_v122_signal(equity):
    base = _safe_div(_mean(equity, 21) - _mean(equity, 42), _mean(equity, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_21d_accel_v123_signal(equity):
    base = _safe_div(_mean(equity, 21) - _mean(equity, 42), _mean(equity, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_63d_accel_v124_signal(equity):
    base = _safe_div(_mean(equity, 63) - _mean(equity, 126), _mean(equity, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_63d_accel_v125_signal(equity):
    base = _safe_div(_mean(equity, 63) - _mean(equity, 126), _mean(equity, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_63d_accel_v126_signal(equity):
    base = _safe_div(_mean(equity, 63) - _mean(equity, 126), _mean(equity, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_126d_accel_v127_signal(equity):
    base = _safe_div(_mean(equity, 126) - _mean(equity, 252), _mean(equity, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_126d_accel_v128_signal(equity):
    base = _safe_div(_mean(equity, 126) - _mean(equity, 252), _mean(equity, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_126d_accel_v129_signal(equity):
    base = _safe_div(_mean(equity, 126) - _mean(equity, 252), _mean(equity, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_252d_accel_v130_signal(equity):
    base = _safe_div(_mean(equity, 252) - _mean(equity, 504), _mean(equity, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_252d_accel_v131_signal(equity):
    base = _safe_div(_mean(equity, 252) - _mean(equity, 504), _mean(equity, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_252d_accel_v132_signal(equity):
    base = _safe_div(_mean(equity, 252) - _mean(equity, 504), _mean(equity, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_504d_accel_v133_signal(equity):
    base = _safe_div(_mean(equity, 504) - _mean(equity, 1008), _mean(equity, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_504d_accel_v134_signal(equity):
    base = _safe_div(_mean(equity, 504) - _mean(equity, 1008), _mean(equity, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_504d_accel_v135_signal(equity):
    base = _safe_div(_mean(equity, 504) - _mean(equity, 1008), _mean(equity, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_21d_accel_v136_signal(equity):
    base = _std(equity, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_21d_accel_v137_signal(equity):
    base = _std(equity, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_21d_accel_v138_signal(equity):
    base = _std(equity, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_63d_accel_v139_signal(equity):
    base = _std(equity, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_63d_accel_v140_signal(equity):
    base = _std(equity, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_63d_accel_v141_signal(equity):
    base = _std(equity, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_126d_accel_v142_signal(equity):
    base = _std(equity, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_126d_accel_v143_signal(equity):
    base = _std(equity, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_126d_accel_v144_signal(equity):
    base = _std(equity, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_252d_accel_v145_signal(equity):
    base = _std(equity, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_252d_accel_v146_signal(equity):
    base = _std(equity, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_252d_accel_v147_signal(equity):
    base = _std(equity, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_504d_accel_v148_signal(equity):
    base = _std(equity, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_504d_accel_v149_signal(equity):
    base = _std(equity, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_504d_accel_v150_signal(equity):
    base = _std(equity, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

