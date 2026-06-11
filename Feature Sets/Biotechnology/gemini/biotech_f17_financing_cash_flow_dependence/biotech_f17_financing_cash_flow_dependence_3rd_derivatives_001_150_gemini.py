
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_21d_accel_v001_signal(ncff):
    base = _mean(ncff, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_21d_accel_v002_signal(ncff):
    base = _mean(ncff, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_21d_accel_v003_signal(ncff):
    base = _mean(ncff, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_63d_accel_v004_signal(ncff):
    base = _mean(ncff, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_63d_accel_v005_signal(ncff):
    base = _mean(ncff, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_63d_accel_v006_signal(ncff):
    base = _mean(ncff, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_126d_accel_v007_signal(ncff):
    base = _mean(ncff, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_126d_accel_v008_signal(ncff):
    base = _mean(ncff, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_126d_accel_v009_signal(ncff):
    base = _mean(ncff, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_252d_accel_v010_signal(ncff):
    base = _mean(ncff, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_252d_accel_v011_signal(ncff):
    base = _mean(ncff, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_252d_accel_v012_signal(ncff):
    base = _mean(ncff, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_504d_accel_v013_signal(ncff):
    base = _mean(ncff, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_504d_accel_v014_signal(ncff):
    base = _mean(ncff, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_504d_accel_v015_signal(ncff):
    base = _mean(ncff, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_21d_accel_v016_signal(ncff):
    base = _mean(_log(ncff), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_21d_accel_v017_signal(ncff):
    base = _mean(_log(ncff), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_21d_accel_v018_signal(ncff):
    base = _mean(_log(ncff), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_63d_accel_v019_signal(ncff):
    base = _mean(_log(ncff), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_63d_accel_v020_signal(ncff):
    base = _mean(_log(ncff), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_63d_accel_v021_signal(ncff):
    base = _mean(_log(ncff), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_126d_accel_v022_signal(ncff):
    base = _mean(_log(ncff), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_126d_accel_v023_signal(ncff):
    base = _mean(_log(ncff), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_126d_accel_v024_signal(ncff):
    base = _mean(_log(ncff), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_252d_accel_v025_signal(ncff):
    base = _mean(_log(ncff), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_252d_accel_v026_signal(ncff):
    base = _mean(_log(ncff), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_252d_accel_v027_signal(ncff):
    base = _mean(_log(ncff), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_504d_accel_v028_signal(ncff):
    base = _mean(_log(ncff), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_504d_accel_v029_signal(ncff):
    base = _mean(_log(ncff), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_504d_accel_v030_signal(ncff):
    base = _mean(_log(ncff), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_21d_accel_v031_signal(ncff):
    base = _z(ncff, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_21d_accel_v032_signal(ncff):
    base = _z(ncff, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_21d_accel_v033_signal(ncff):
    base = _z(ncff, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_63d_accel_v034_signal(ncff):
    base = _z(ncff, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_63d_accel_v035_signal(ncff):
    base = _z(ncff, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_63d_accel_v036_signal(ncff):
    base = _z(ncff, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_126d_accel_v037_signal(ncff):
    base = _z(ncff, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_126d_accel_v038_signal(ncff):
    base = _z(ncff, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_126d_accel_v039_signal(ncff):
    base = _z(ncff, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_252d_accel_v040_signal(ncff):
    base = _z(ncff, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_252d_accel_v041_signal(ncff):
    base = _z(ncff, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_252d_accel_v042_signal(ncff):
    base = _z(ncff, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_504d_accel_v043_signal(ncff):
    base = _z(ncff, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_504d_accel_v044_signal(ncff):
    base = _z(ncff, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_504d_accel_v045_signal(ncff):
    base = _z(ncff, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_21d_accel_v046_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_21d_accel_v047_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_21d_accel_v048_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_63d_accel_v049_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_63d_accel_v050_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_63d_accel_v051_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_126d_accel_v052_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_126d_accel_v053_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_126d_accel_v054_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_252d_accel_v055_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_252d_accel_v056_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_252d_accel_v057_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_504d_accel_v058_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_504d_accel_v059_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_504d_accel_v060_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_21d_accel_v061_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_21d_accel_v062_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_21d_accel_v063_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_63d_accel_v064_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_63d_accel_v065_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_63d_accel_v066_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_126d_accel_v067_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_126d_accel_v068_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_126d_accel_v069_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_252d_accel_v070_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_252d_accel_v071_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_252d_accel_v072_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_504d_accel_v073_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_504d_accel_v074_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_504d_accel_v075_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_21d_accel_v076_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_21d_accel_v077_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_21d_accel_v078_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_63d_accel_v079_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_63d_accel_v080_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_63d_accel_v081_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_126d_accel_v082_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_126d_accel_v083_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_126d_accel_v084_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_252d_accel_v085_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_252d_accel_v086_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_252d_accel_v087_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_504d_accel_v088_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_504d_accel_v089_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_504d_accel_v090_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_21d_accel_v091_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(21).min(), ncff.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_21d_accel_v092_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(21).min(), ncff.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_21d_accel_v093_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(21).min(), ncff.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_63d_accel_v094_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(63).min(), ncff.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_63d_accel_v095_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(63).min(), ncff.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_63d_accel_v096_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(63).min(), ncff.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_126d_accel_v097_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(126).min(), ncff.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_126d_accel_v098_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(126).min(), ncff.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_126d_accel_v099_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(126).min(), ncff.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_252d_accel_v100_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(252).min(), ncff.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_252d_accel_v101_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(252).min(), ncff.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_252d_accel_v102_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(252).min(), ncff.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_504d_accel_v103_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(504).min(), ncff.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_504d_accel_v104_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(504).min(), ncff.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_504d_accel_v105_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(504).min(), ncff.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_21d_accel_v106_signal(ncff):
    base = _safe_div(ncff.rolling(21).max() - ncff, ncff.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_21d_accel_v107_signal(ncff):
    base = _safe_div(ncff.rolling(21).max() - ncff, ncff.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_21d_accel_v108_signal(ncff):
    base = _safe_div(ncff.rolling(21).max() - ncff, ncff.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_63d_accel_v109_signal(ncff):
    base = _safe_div(ncff.rolling(63).max() - ncff, ncff.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_63d_accel_v110_signal(ncff):
    base = _safe_div(ncff.rolling(63).max() - ncff, ncff.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_63d_accel_v111_signal(ncff):
    base = _safe_div(ncff.rolling(63).max() - ncff, ncff.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_126d_accel_v112_signal(ncff):
    base = _safe_div(ncff.rolling(126).max() - ncff, ncff.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_126d_accel_v113_signal(ncff):
    base = _safe_div(ncff.rolling(126).max() - ncff, ncff.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_126d_accel_v114_signal(ncff):
    base = _safe_div(ncff.rolling(126).max() - ncff, ncff.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_252d_accel_v115_signal(ncff):
    base = _safe_div(ncff.rolling(252).max() - ncff, ncff.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_252d_accel_v116_signal(ncff):
    base = _safe_div(ncff.rolling(252).max() - ncff, ncff.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_252d_accel_v117_signal(ncff):
    base = _safe_div(ncff.rolling(252).max() - ncff, ncff.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_504d_accel_v118_signal(ncff):
    base = _safe_div(ncff.rolling(504).max() - ncff, ncff.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_504d_accel_v119_signal(ncff):
    base = _safe_div(ncff.rolling(504).max() - ncff, ncff.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_504d_accel_v120_signal(ncff):
    base = _safe_div(ncff.rolling(504).max() - ncff, ncff.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_21d_accel_v121_signal(ncff):
    base = _safe_div(_mean(ncff, 21) - _mean(ncff, 42), _mean(ncff, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_21d_accel_v122_signal(ncff):
    base = _safe_div(_mean(ncff, 21) - _mean(ncff, 42), _mean(ncff, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_21d_accel_v123_signal(ncff):
    base = _safe_div(_mean(ncff, 21) - _mean(ncff, 42), _mean(ncff, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_63d_accel_v124_signal(ncff):
    base = _safe_div(_mean(ncff, 63) - _mean(ncff, 126), _mean(ncff, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_63d_accel_v125_signal(ncff):
    base = _safe_div(_mean(ncff, 63) - _mean(ncff, 126), _mean(ncff, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_63d_accel_v126_signal(ncff):
    base = _safe_div(_mean(ncff, 63) - _mean(ncff, 126), _mean(ncff, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_126d_accel_v127_signal(ncff):
    base = _safe_div(_mean(ncff, 126) - _mean(ncff, 252), _mean(ncff, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_126d_accel_v128_signal(ncff):
    base = _safe_div(_mean(ncff, 126) - _mean(ncff, 252), _mean(ncff, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_126d_accel_v129_signal(ncff):
    base = _safe_div(_mean(ncff, 126) - _mean(ncff, 252), _mean(ncff, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_252d_accel_v130_signal(ncff):
    base = _safe_div(_mean(ncff, 252) - _mean(ncff, 504), _mean(ncff, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_252d_accel_v131_signal(ncff):
    base = _safe_div(_mean(ncff, 252) - _mean(ncff, 504), _mean(ncff, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_252d_accel_v132_signal(ncff):
    base = _safe_div(_mean(ncff, 252) - _mean(ncff, 504), _mean(ncff, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_504d_accel_v133_signal(ncff):
    base = _safe_div(_mean(ncff, 504) - _mean(ncff, 1008), _mean(ncff, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_504d_accel_v134_signal(ncff):
    base = _safe_div(_mean(ncff, 504) - _mean(ncff, 1008), _mean(ncff, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_504d_accel_v135_signal(ncff):
    base = _safe_div(_mean(ncff, 504) - _mean(ncff, 1008), _mean(ncff, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_21d_accel_v136_signal(ncff):
    base = _std(ncff, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_21d_accel_v137_signal(ncff):
    base = _std(ncff, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_21d_accel_v138_signal(ncff):
    base = _std(ncff, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_63d_accel_v139_signal(ncff):
    base = _std(ncff, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_63d_accel_v140_signal(ncff):
    base = _std(ncff, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_63d_accel_v141_signal(ncff):
    base = _std(ncff, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_126d_accel_v142_signal(ncff):
    base = _std(ncff, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_126d_accel_v143_signal(ncff):
    base = _std(ncff, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_126d_accel_v144_signal(ncff):
    base = _std(ncff, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_252d_accel_v145_signal(ncff):
    base = _std(ncff, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_252d_accel_v146_signal(ncff):
    base = _std(ncff, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_252d_accel_v147_signal(ncff):
    base = _std(ncff, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_504d_accel_v148_signal(ncff):
    base = _std(ncff, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_504d_accel_v149_signal(ncff):
    base = _std(ncff, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_504d_accel_v150_signal(ncff):
    base = _std(ncff, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

