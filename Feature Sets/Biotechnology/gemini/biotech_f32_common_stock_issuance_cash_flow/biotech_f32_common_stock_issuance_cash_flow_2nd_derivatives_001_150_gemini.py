
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_21d_slope_v001_signal(ncfcommon):
    base = _mean(ncfcommon, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_21d_slope_v002_signal(ncfcommon):
    base = _mean(ncfcommon, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_21d_slope_v003_signal(ncfcommon):
    base = _mean(ncfcommon, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_63d_slope_v004_signal(ncfcommon):
    base = _mean(ncfcommon, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_63d_slope_v005_signal(ncfcommon):
    base = _mean(ncfcommon, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_63d_slope_v006_signal(ncfcommon):
    base = _mean(ncfcommon, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_126d_slope_v007_signal(ncfcommon):
    base = _mean(ncfcommon, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_126d_slope_v008_signal(ncfcommon):
    base = _mean(ncfcommon, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_126d_slope_v009_signal(ncfcommon):
    base = _mean(ncfcommon, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_252d_slope_v010_signal(ncfcommon):
    base = _mean(ncfcommon, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_252d_slope_v011_signal(ncfcommon):
    base = _mean(ncfcommon, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_252d_slope_v012_signal(ncfcommon):
    base = _mean(ncfcommon, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_504d_slope_v013_signal(ncfcommon):
    base = _mean(ncfcommon, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_504d_slope_v014_signal(ncfcommon):
    base = _mean(ncfcommon, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_raw_504d_slope_v015_signal(ncfcommon):
    base = _mean(ncfcommon, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_21d_slope_v016_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_21d_slope_v017_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_21d_slope_v018_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_63d_slope_v019_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_63d_slope_v020_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_63d_slope_v021_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_126d_slope_v022_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_126d_slope_v023_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_126d_slope_v024_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_252d_slope_v025_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_252d_slope_v026_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_252d_slope_v027_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_504d_slope_v028_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_504d_slope_v029_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_log_504d_slope_v030_signal(ncfcommon):
    base = _mean(_log(ncfcommon), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_21d_slope_v031_signal(ncfcommon):
    base = _z(ncfcommon, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_21d_slope_v032_signal(ncfcommon):
    base = _z(ncfcommon, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_21d_slope_v033_signal(ncfcommon):
    base = _z(ncfcommon, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_63d_slope_v034_signal(ncfcommon):
    base = _z(ncfcommon, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_63d_slope_v035_signal(ncfcommon):
    base = _z(ncfcommon, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_63d_slope_v036_signal(ncfcommon):
    base = _z(ncfcommon, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_126d_slope_v037_signal(ncfcommon):
    base = _z(ncfcommon, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_126d_slope_v038_signal(ncfcommon):
    base = _z(ncfcommon, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_126d_slope_v039_signal(ncfcommon):
    base = _z(ncfcommon, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_252d_slope_v040_signal(ncfcommon):
    base = _z(ncfcommon, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_252d_slope_v041_signal(ncfcommon):
    base = _z(ncfcommon, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_252d_slope_v042_signal(ncfcommon):
    base = _z(ncfcommon, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_504d_slope_v043_signal(ncfcommon):
    base = _z(ncfcommon, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_504d_slope_v044_signal(ncfcommon):
    base = _z(ncfcommon, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_z_504d_slope_v045_signal(ncfcommon):
    base = _z(ncfcommon, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_21d_slope_v046_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_21d_slope_v047_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_21d_slope_v048_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_63d_slope_v049_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_63d_slope_v050_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_63d_slope_v051_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_126d_slope_v052_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_126d_slope_v053_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_126d_slope_v054_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_252d_slope_v055_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_252d_slope_v056_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_252d_slope_v057_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_504d_slope_v058_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_504d_slope_v059_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ps_504d_slope_v060_signal(ncfcommon, sharesbas):
    base = _safe_div(_mean(ncfcommon, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_21d_slope_v061_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_21d_slope_v062_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_21d_slope_v063_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_63d_slope_v064_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_63d_slope_v065_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_63d_slope_v066_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_126d_slope_v067_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_126d_slope_v068_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_126d_slope_v069_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_252d_slope_v070_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_252d_slope_v071_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_252d_slope_v072_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_504d_slope_v073_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_504d_slope_v074_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_asset_scaled_504d_slope_v075_signal(ncfcommon, assets):
    base = _safe_div(_mean(ncfcommon, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_21d_slope_v076_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_21d_slope_v077_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_21d_slope_v078_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_63d_slope_v079_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_63d_slope_v080_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_63d_slope_v081_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_126d_slope_v082_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_126d_slope_v083_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_126d_slope_v084_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_252d_slope_v085_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_252d_slope_v086_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_252d_slope_v087_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_504d_slope_v088_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_504d_slope_v089_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mcap_scaled_504d_slope_v090_signal(ncfcommon, marketcap):
    base = _safe_div(_mean(ncfcommon, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_21d_slope_v091_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(21).min(), ncfcommon.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_21d_slope_v092_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(21).min(), ncfcommon.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_21d_slope_v093_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(21).min(), ncfcommon.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_63d_slope_v094_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(63).min(), ncfcommon.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_63d_slope_v095_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(63).min(), ncfcommon.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_63d_slope_v096_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(63).min(), ncfcommon.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_126d_slope_v097_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(126).min(), ncfcommon.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_126d_slope_v098_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(126).min(), ncfcommon.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_126d_slope_v099_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(126).min(), ncfcommon.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_252d_slope_v100_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(252).min(), ncfcommon.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_252d_slope_v101_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(252).min(), ncfcommon.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_252d_slope_v102_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(252).min(), ncfcommon.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_504d_slope_v103_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(504).min(), ncfcommon.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_504d_slope_v104_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(504).min(), ncfcommon.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_low_504d_slope_v105_signal(ncfcommon):
    base = _safe_div(ncfcommon - ncfcommon.rolling(504).min(), ncfcommon.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_21d_slope_v106_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(21).max() - ncfcommon, ncfcommon.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_21d_slope_v107_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(21).max() - ncfcommon, ncfcommon.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_21d_slope_v108_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(21).max() - ncfcommon, ncfcommon.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_63d_slope_v109_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(63).max() - ncfcommon, ncfcommon.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_63d_slope_v110_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(63).max() - ncfcommon, ncfcommon.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_63d_slope_v111_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(63).max() - ncfcommon, ncfcommon.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_126d_slope_v112_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(126).max() - ncfcommon, ncfcommon.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_126d_slope_v113_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(126).max() - ncfcommon, ncfcommon.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_126d_slope_v114_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(126).max() - ncfcommon, ncfcommon.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_252d_slope_v115_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(252).max() - ncfcommon, ncfcommon.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_252d_slope_v116_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(252).max() - ncfcommon, ncfcommon.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_252d_slope_v117_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(252).max() - ncfcommon, ncfcommon.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_504d_slope_v118_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(504).max() - ncfcommon, ncfcommon.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_504d_slope_v119_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(504).max() - ncfcommon, ncfcommon.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_dist_high_504d_slope_v120_signal(ncfcommon):
    base = _safe_div(ncfcommon.rolling(504).max() - ncfcommon, ncfcommon.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_21d_slope_v121_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 21) - _mean(ncfcommon, 42), _mean(ncfcommon, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_21d_slope_v122_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 21) - _mean(ncfcommon, 42), _mean(ncfcommon, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_21d_slope_v123_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 21) - _mean(ncfcommon, 42), _mean(ncfcommon, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_63d_slope_v124_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 63) - _mean(ncfcommon, 126), _mean(ncfcommon, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_63d_slope_v125_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 63) - _mean(ncfcommon, 126), _mean(ncfcommon, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_63d_slope_v126_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 63) - _mean(ncfcommon, 126), _mean(ncfcommon, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_126d_slope_v127_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 126) - _mean(ncfcommon, 252), _mean(ncfcommon, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_126d_slope_v128_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 126) - _mean(ncfcommon, 252), _mean(ncfcommon, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_126d_slope_v129_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 126) - _mean(ncfcommon, 252), _mean(ncfcommon, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_252d_slope_v130_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 252) - _mean(ncfcommon, 504), _mean(ncfcommon, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_252d_slope_v131_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 252) - _mean(ncfcommon, 504), _mean(ncfcommon, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_252d_slope_v132_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 252) - _mean(ncfcommon, 504), _mean(ncfcommon, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_504d_slope_v133_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 504) - _mean(ncfcommon, 1008), _mean(ncfcommon, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_504d_slope_v134_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 504) - _mean(ncfcommon, 1008), _mean(ncfcommon, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mom_504d_slope_v135_signal(ncfcommon):
    base = _safe_div(_mean(ncfcommon, 504) - _mean(ncfcommon, 1008), _mean(ncfcommon, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_21d_slope_v136_signal(ncfcommon):
    base = _std(ncfcommon, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_21d_slope_v137_signal(ncfcommon):
    base = _std(ncfcommon, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_21d_slope_v138_signal(ncfcommon):
    base = _std(ncfcommon, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_63d_slope_v139_signal(ncfcommon):
    base = _std(ncfcommon, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_63d_slope_v140_signal(ncfcommon):
    base = _std(ncfcommon, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_63d_slope_v141_signal(ncfcommon):
    base = _std(ncfcommon, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_126d_slope_v142_signal(ncfcommon):
    base = _std(ncfcommon, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_126d_slope_v143_signal(ncfcommon):
    base = _std(ncfcommon, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_126d_slope_v144_signal(ncfcommon):
    base = _std(ncfcommon, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_252d_slope_v145_signal(ncfcommon):
    base = _std(ncfcommon, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_252d_slope_v146_signal(ncfcommon):
    base = _std(ncfcommon, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_252d_slope_v147_signal(ncfcommon):
    base = _std(ncfcommon, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_504d_slope_v148_signal(ncfcommon):
    base = _std(ncfcommon, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_504d_slope_v149_signal(ncfcommon):
    base = _std(ncfcommon, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_vol_504d_slope_v150_signal(ncfcommon):
    base = _std(ncfcommon, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

