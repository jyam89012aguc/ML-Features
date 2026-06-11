
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_21d_accel_v001_signal(receivables):
    base = _mean(receivables, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_21d_accel_v002_signal(receivables):
    base = _mean(receivables, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_21d_accel_v003_signal(receivables):
    base = _mean(receivables, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_63d_accel_v004_signal(receivables):
    base = _mean(receivables, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_63d_accel_v005_signal(receivables):
    base = _mean(receivables, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_63d_accel_v006_signal(receivables):
    base = _mean(receivables, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_126d_accel_v007_signal(receivables):
    base = _mean(receivables, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_126d_accel_v008_signal(receivables):
    base = _mean(receivables, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_126d_accel_v009_signal(receivables):
    base = _mean(receivables, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_252d_accel_v010_signal(receivables):
    base = _mean(receivables, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_252d_accel_v011_signal(receivables):
    base = _mean(receivables, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_252d_accel_v012_signal(receivables):
    base = _mean(receivables, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_504d_accel_v013_signal(receivables):
    base = _mean(receivables, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_504d_accel_v014_signal(receivables):
    base = _mean(receivables, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_504d_accel_v015_signal(receivables):
    base = _mean(receivables, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_21d_accel_v016_signal(receivables):
    base = _mean(_log(receivables), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_21d_accel_v017_signal(receivables):
    base = _mean(_log(receivables), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_21d_accel_v018_signal(receivables):
    base = _mean(_log(receivables), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_63d_accel_v019_signal(receivables):
    base = _mean(_log(receivables), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_63d_accel_v020_signal(receivables):
    base = _mean(_log(receivables), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_63d_accel_v021_signal(receivables):
    base = _mean(_log(receivables), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_126d_accel_v022_signal(receivables):
    base = _mean(_log(receivables), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_126d_accel_v023_signal(receivables):
    base = _mean(_log(receivables), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_126d_accel_v024_signal(receivables):
    base = _mean(_log(receivables), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_252d_accel_v025_signal(receivables):
    base = _mean(_log(receivables), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_252d_accel_v026_signal(receivables):
    base = _mean(_log(receivables), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_252d_accel_v027_signal(receivables):
    base = _mean(_log(receivables), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_504d_accel_v028_signal(receivables):
    base = _mean(_log(receivables), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_504d_accel_v029_signal(receivables):
    base = _mean(_log(receivables), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_504d_accel_v030_signal(receivables):
    base = _mean(_log(receivables), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_21d_accel_v031_signal(receivables):
    base = _z(receivables, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_21d_accel_v032_signal(receivables):
    base = _z(receivables, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_21d_accel_v033_signal(receivables):
    base = _z(receivables, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_63d_accel_v034_signal(receivables):
    base = _z(receivables, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_63d_accel_v035_signal(receivables):
    base = _z(receivables, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_63d_accel_v036_signal(receivables):
    base = _z(receivables, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_126d_accel_v037_signal(receivables):
    base = _z(receivables, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_126d_accel_v038_signal(receivables):
    base = _z(receivables, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_126d_accel_v039_signal(receivables):
    base = _z(receivables, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_252d_accel_v040_signal(receivables):
    base = _z(receivables, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_252d_accel_v041_signal(receivables):
    base = _z(receivables, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_252d_accel_v042_signal(receivables):
    base = _z(receivables, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_504d_accel_v043_signal(receivables):
    base = _z(receivables, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_504d_accel_v044_signal(receivables):
    base = _z(receivables, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_504d_accel_v045_signal(receivables):
    base = _z(receivables, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_21d_accel_v046_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_21d_accel_v047_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_21d_accel_v048_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_63d_accel_v049_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_63d_accel_v050_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_63d_accel_v051_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_126d_accel_v052_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_126d_accel_v053_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_126d_accel_v054_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_252d_accel_v055_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_252d_accel_v056_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_252d_accel_v057_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_504d_accel_v058_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_504d_accel_v059_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_504d_accel_v060_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_21d_accel_v061_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_21d_accel_v062_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_21d_accel_v063_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_63d_accel_v064_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_63d_accel_v065_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_63d_accel_v066_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_126d_accel_v067_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_126d_accel_v068_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_126d_accel_v069_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_252d_accel_v070_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_252d_accel_v071_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_252d_accel_v072_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_504d_accel_v073_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_504d_accel_v074_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_504d_accel_v075_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_21d_accel_v076_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_21d_accel_v077_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_21d_accel_v078_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_63d_accel_v079_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_63d_accel_v080_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_63d_accel_v081_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_126d_accel_v082_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_126d_accel_v083_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_126d_accel_v084_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_252d_accel_v085_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_252d_accel_v086_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_252d_accel_v087_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_504d_accel_v088_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_504d_accel_v089_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_504d_accel_v090_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_21d_accel_v091_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(21).min(), receivables.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_21d_accel_v092_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(21).min(), receivables.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_21d_accel_v093_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(21).min(), receivables.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_63d_accel_v094_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(63).min(), receivables.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_63d_accel_v095_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(63).min(), receivables.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_63d_accel_v096_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(63).min(), receivables.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_126d_accel_v097_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(126).min(), receivables.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_126d_accel_v098_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(126).min(), receivables.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_126d_accel_v099_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(126).min(), receivables.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_252d_accel_v100_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(252).min(), receivables.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_252d_accel_v101_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(252).min(), receivables.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_252d_accel_v102_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(252).min(), receivables.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_504d_accel_v103_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(504).min(), receivables.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_504d_accel_v104_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(504).min(), receivables.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_504d_accel_v105_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(504).min(), receivables.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_21d_accel_v106_signal(receivables):
    base = _safe_div(receivables.rolling(21).max() - receivables, receivables.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_21d_accel_v107_signal(receivables):
    base = _safe_div(receivables.rolling(21).max() - receivables, receivables.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_21d_accel_v108_signal(receivables):
    base = _safe_div(receivables.rolling(21).max() - receivables, receivables.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_63d_accel_v109_signal(receivables):
    base = _safe_div(receivables.rolling(63).max() - receivables, receivables.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_63d_accel_v110_signal(receivables):
    base = _safe_div(receivables.rolling(63).max() - receivables, receivables.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_63d_accel_v111_signal(receivables):
    base = _safe_div(receivables.rolling(63).max() - receivables, receivables.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_126d_accel_v112_signal(receivables):
    base = _safe_div(receivables.rolling(126).max() - receivables, receivables.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_126d_accel_v113_signal(receivables):
    base = _safe_div(receivables.rolling(126).max() - receivables, receivables.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_126d_accel_v114_signal(receivables):
    base = _safe_div(receivables.rolling(126).max() - receivables, receivables.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_252d_accel_v115_signal(receivables):
    base = _safe_div(receivables.rolling(252).max() - receivables, receivables.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_252d_accel_v116_signal(receivables):
    base = _safe_div(receivables.rolling(252).max() - receivables, receivables.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_252d_accel_v117_signal(receivables):
    base = _safe_div(receivables.rolling(252).max() - receivables, receivables.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_504d_accel_v118_signal(receivables):
    base = _safe_div(receivables.rolling(504).max() - receivables, receivables.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_504d_accel_v119_signal(receivables):
    base = _safe_div(receivables.rolling(504).max() - receivables, receivables.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_504d_accel_v120_signal(receivables):
    base = _safe_div(receivables.rolling(504).max() - receivables, receivables.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_21d_accel_v121_signal(receivables):
    base = _safe_div(_mean(receivables, 21) - _mean(receivables, 42), _mean(receivables, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_21d_accel_v122_signal(receivables):
    base = _safe_div(_mean(receivables, 21) - _mean(receivables, 42), _mean(receivables, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_21d_accel_v123_signal(receivables):
    base = _safe_div(_mean(receivables, 21) - _mean(receivables, 42), _mean(receivables, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_63d_accel_v124_signal(receivables):
    base = _safe_div(_mean(receivables, 63) - _mean(receivables, 126), _mean(receivables, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_63d_accel_v125_signal(receivables):
    base = _safe_div(_mean(receivables, 63) - _mean(receivables, 126), _mean(receivables, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_63d_accel_v126_signal(receivables):
    base = _safe_div(_mean(receivables, 63) - _mean(receivables, 126), _mean(receivables, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_126d_accel_v127_signal(receivables):
    base = _safe_div(_mean(receivables, 126) - _mean(receivables, 252), _mean(receivables, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_126d_accel_v128_signal(receivables):
    base = _safe_div(_mean(receivables, 126) - _mean(receivables, 252), _mean(receivables, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_126d_accel_v129_signal(receivables):
    base = _safe_div(_mean(receivables, 126) - _mean(receivables, 252), _mean(receivables, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_252d_accel_v130_signal(receivables):
    base = _safe_div(_mean(receivables, 252) - _mean(receivables, 504), _mean(receivables, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_252d_accel_v131_signal(receivables):
    base = _safe_div(_mean(receivables, 252) - _mean(receivables, 504), _mean(receivables, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_252d_accel_v132_signal(receivables):
    base = _safe_div(_mean(receivables, 252) - _mean(receivables, 504), _mean(receivables, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_504d_accel_v133_signal(receivables):
    base = _safe_div(_mean(receivables, 504) - _mean(receivables, 1008), _mean(receivables, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_504d_accel_v134_signal(receivables):
    base = _safe_div(_mean(receivables, 504) - _mean(receivables, 1008), _mean(receivables, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_504d_accel_v135_signal(receivables):
    base = _safe_div(_mean(receivables, 504) - _mean(receivables, 1008), _mean(receivables, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_21d_accel_v136_signal(receivables):
    base = _std(receivables, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_21d_accel_v137_signal(receivables):
    base = _std(receivables, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_21d_accel_v138_signal(receivables):
    base = _std(receivables, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_63d_accel_v139_signal(receivables):
    base = _std(receivables, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_63d_accel_v140_signal(receivables):
    base = _std(receivables, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_63d_accel_v141_signal(receivables):
    base = _std(receivables, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_126d_accel_v142_signal(receivables):
    base = _std(receivables, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_126d_accel_v143_signal(receivables):
    base = _std(receivables, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_126d_accel_v144_signal(receivables):
    base = _std(receivables, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_252d_accel_v145_signal(receivables):
    base = _std(receivables, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_252d_accel_v146_signal(receivables):
    base = _std(receivables, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_252d_accel_v147_signal(receivables):
    base = _std(receivables, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_504d_accel_v148_signal(receivables):
    base = _std(receivables, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_504d_accel_v149_signal(receivables):
    base = _std(receivables, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_504d_accel_v150_signal(receivables):
    base = _std(receivables, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

