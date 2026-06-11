
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_21d_accel_v001_signal(ncfcommon):
    base = _mean(ncfcommon, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_21d_accel_v002_signal(ncfcommon):
    base = _mean(ncfcommon, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_21d_accel_v003_signal(ncfcommon):
    base = _mean(ncfcommon, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_63d_accel_v004_signal(ncfcommon):
    base = _mean(ncfcommon, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_63d_accel_v005_signal(ncfcommon):
    base = _mean(ncfcommon, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_63d_accel_v006_signal(ncfcommon):
    base = _mean(ncfcommon, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_126d_accel_v007_signal(ncfcommon):
    base = _mean(ncfcommon, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_126d_accel_v008_signal(ncfcommon):
    base = _mean(ncfcommon, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_126d_accel_v009_signal(ncfcommon):
    base = _mean(ncfcommon, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_252d_accel_v010_signal(ncfcommon):
    base = _mean(ncfcommon, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_252d_accel_v011_signal(ncfcommon):
    base = _mean(ncfcommon, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_252d_accel_v012_signal(ncfcommon):
    base = _mean(ncfcommon, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_504d_accel_v013_signal(ncfcommon):
    base = _mean(ncfcommon, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_504d_accel_v014_signal(ncfcommon):
    base = _mean(ncfcommon, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_504d_accel_v015_signal(ncfcommon):
    base = _mean(ncfcommon, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_21d_accel_v016_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_21d_accel_v017_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_21d_accel_v018_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_63d_accel_v019_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_63d_accel_v020_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_63d_accel_v021_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_126d_accel_v022_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_126d_accel_v023_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_126d_accel_v024_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_252d_accel_v025_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_252d_accel_v026_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_252d_accel_v027_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_504d_accel_v028_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_504d_accel_v029_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_504d_accel_v030_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_21d_accel_v031_signal(ncfcommon):
    base = _z(ncfcommon, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_21d_accel_v032_signal(ncfcommon):
    base = _z(ncfcommon, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_21d_accel_v033_signal(ncfcommon):
    base = _z(ncfcommon, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_63d_accel_v034_signal(ncfcommon):
    base = _z(ncfcommon, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_63d_accel_v035_signal(ncfcommon):
    base = _z(ncfcommon, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_63d_accel_v036_signal(ncfcommon):
    base = _z(ncfcommon, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_126d_accel_v037_signal(ncfcommon):
    base = _z(ncfcommon, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_126d_accel_v038_signal(ncfcommon):
    base = _z(ncfcommon, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_126d_accel_v039_signal(ncfcommon):
    base = _z(ncfcommon, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_252d_accel_v040_signal(ncfcommon):
    base = _z(ncfcommon, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_252d_accel_v041_signal(ncfcommon):
    base = _z(ncfcommon, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_252d_accel_v042_signal(ncfcommon):
    base = _z(ncfcommon, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_504d_accel_v043_signal(ncfcommon):
    base = _z(ncfcommon, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_504d_accel_v044_signal(ncfcommon):
    base = _z(ncfcommon, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_504d_accel_v045_signal(ncfcommon):
    base = _z(ncfcommon, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_21d_accel_v046_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_21d_accel_v047_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_21d_accel_v048_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_63d_accel_v049_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_63d_accel_v050_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_63d_accel_v051_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_126d_accel_v052_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_126d_accel_v053_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_126d_accel_v054_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_252d_accel_v055_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_252d_accel_v056_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_252d_accel_v057_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_504d_accel_v058_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_504d_accel_v059_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_504d_accel_v060_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_21d_accel_v061_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_21d_accel_v062_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_21d_accel_v063_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_63d_accel_v064_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_63d_accel_v065_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_63d_accel_v066_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_126d_accel_v067_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_126d_accel_v068_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_126d_accel_v069_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_252d_accel_v070_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_252d_accel_v071_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_252d_accel_v072_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_504d_accel_v073_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_504d_accel_v074_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_504d_accel_v075_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_21d_accel_v076_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_21d_accel_v077_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_21d_accel_v078_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_63d_accel_v079_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_63d_accel_v080_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_63d_accel_v081_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_126d_accel_v082_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_126d_accel_v083_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_126d_accel_v084_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_252d_accel_v085_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_252d_accel_v086_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_252d_accel_v087_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_504d_accel_v088_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_504d_accel_v089_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_504d_accel_v090_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_21d_accel_v091_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(21).min(), ncfcommon.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_21d_accel_v092_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(21).min(), ncfcommon.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_21d_accel_v093_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(21).min(), ncfcommon.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_63d_accel_v094_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(63).min(), ncfcommon.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_63d_accel_v095_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(63).min(), ncfcommon.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_63d_accel_v096_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(63).min(), ncfcommon.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_126d_accel_v097_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(126).min(), ncfcommon.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_126d_accel_v098_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(126).min(), ncfcommon.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_126d_accel_v099_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(126).min(), ncfcommon.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_252d_accel_v100_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(252).min(), ncfcommon.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_252d_accel_v101_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(252).min(), ncfcommon.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_252d_accel_v102_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(252).min(), ncfcommon.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_504d_accel_v103_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(504).min(), ncfcommon.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_504d_accel_v104_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(504).min(), ncfcommon.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_504d_accel_v105_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(504).min(), ncfcommon.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_21d_accel_v106_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(21).max() - ncfcommon, ncfcommon.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_21d_accel_v107_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(21).max() - ncfcommon, ncfcommon.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_21d_accel_v108_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(21).max() - ncfcommon, ncfcommon.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_63d_accel_v109_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(63).max() - ncfcommon, ncfcommon.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_63d_accel_v110_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(63).max() - ncfcommon, ncfcommon.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_63d_accel_v111_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(63).max() - ncfcommon, ncfcommon.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_126d_accel_v112_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(126).max() - ncfcommon, ncfcommon.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_126d_accel_v113_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(126).max() - ncfcommon, ncfcommon.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_126d_accel_v114_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(126).max() - ncfcommon, ncfcommon.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_252d_accel_v115_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(252).max() - ncfcommon, ncfcommon.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_252d_accel_v116_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(252).max() - ncfcommon, ncfcommon.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_252d_accel_v117_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(252).max() - ncfcommon, ncfcommon.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_504d_accel_v118_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(504).max() - ncfcommon, ncfcommon.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_504d_accel_v119_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(504).max() - ncfcommon, ncfcommon.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_504d_accel_v120_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(504).max() - ncfcommon, ncfcommon.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_21d_accel_v121_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 21) - _mean(ncfcommon, 42), _mean(ncfcommon, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_21d_accel_v122_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 21) - _mean(ncfcommon, 42), _mean(ncfcommon, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_21d_accel_v123_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 21) - _mean(ncfcommon, 42), _mean(ncfcommon, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_63d_accel_v124_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 63) - _mean(ncfcommon, 126), _mean(ncfcommon, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_63d_accel_v125_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 63) - _mean(ncfcommon, 126), _mean(ncfcommon, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_63d_accel_v126_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 63) - _mean(ncfcommon, 126), _mean(ncfcommon, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_126d_accel_v127_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 126) - _mean(ncfcommon, 252), _mean(ncfcommon, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_126d_accel_v128_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 126) - _mean(ncfcommon, 252), _mean(ncfcommon, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_126d_accel_v129_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 126) - _mean(ncfcommon, 252), _mean(ncfcommon, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_252d_accel_v130_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 252) - _mean(ncfcommon, 504), _mean(ncfcommon, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_252d_accel_v131_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 252) - _mean(ncfcommon, 504), _mean(ncfcommon, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_252d_accel_v132_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 252) - _mean(ncfcommon, 504), _mean(ncfcommon, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_504d_accel_v133_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 504) - _mean(ncfcommon, 1008), _mean(ncfcommon, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_504d_accel_v134_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 504) - _mean(ncfcommon, 1008), _mean(ncfcommon, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_504d_accel_v135_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 504) - _mean(ncfcommon, 1008), _mean(ncfcommon, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_21d_accel_v136_signal(ncfcommon):
    base = _std(ncfcommon, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_21d_accel_v137_signal(ncfcommon):
    base = _std(ncfcommon, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_21d_accel_v138_signal(ncfcommon):
    base = _std(ncfcommon, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_63d_accel_v139_signal(ncfcommon):
    base = _std(ncfcommon, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_63d_accel_v140_signal(ncfcommon):
    base = _std(ncfcommon, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_63d_accel_v141_signal(ncfcommon):
    base = _std(ncfcommon, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_126d_accel_v142_signal(ncfcommon):
    base = _std(ncfcommon, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_126d_accel_v143_signal(ncfcommon):
    base = _std(ncfcommon, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_126d_accel_v144_signal(ncfcommon):
    base = _std(ncfcommon, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_252d_accel_v145_signal(ncfcommon):
    base = _std(ncfcommon, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_252d_accel_v146_signal(ncfcommon):
    base = _std(ncfcommon, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_252d_accel_v147_signal(ncfcommon):
    base = _std(ncfcommon, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_504d_accel_v148_signal(ncfcommon):
    base = _std(ncfcommon, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_504d_accel_v149_signal(ncfcommon):
    base = _std(ncfcommon, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_504d_accel_v150_signal(ncfcommon):
    base = _std(ncfcommon, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

