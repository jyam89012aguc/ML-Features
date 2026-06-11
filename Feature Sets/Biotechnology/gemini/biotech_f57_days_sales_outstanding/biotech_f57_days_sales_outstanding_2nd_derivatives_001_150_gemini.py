
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_21d_slope_v001_signal(receivables):
    base = _mean(receivables, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_21d_slope_v002_signal(receivables):
    base = _mean(receivables, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_21d_slope_v003_signal(receivables):
    base = _mean(receivables, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_63d_slope_v004_signal(receivables):
    base = _mean(receivables, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_63d_slope_v005_signal(receivables):
    base = _mean(receivables, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_63d_slope_v006_signal(receivables):
    base = _mean(receivables, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_126d_slope_v007_signal(receivables):
    base = _mean(receivables, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_126d_slope_v008_signal(receivables):
    base = _mean(receivables, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_126d_slope_v009_signal(receivables):
    base = _mean(receivables, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_252d_slope_v010_signal(receivables):
    base = _mean(receivables, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_252d_slope_v011_signal(receivables):
    base = _mean(receivables, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_252d_slope_v012_signal(receivables):
    base = _mean(receivables, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_504d_slope_v013_signal(receivables):
    base = _mean(receivables, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_504d_slope_v014_signal(receivables):
    base = _mean(receivables, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw receivables
def gm_f57_biotech_f57_days_sales_outstanding_raw_504d_slope_v015_signal(receivables):
    base = _mean(receivables, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_21d_slope_v016_signal(receivables):
    base = _mean(_log(receivables), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_21d_slope_v017_signal(receivables):
    base = _mean(_log(receivables), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_21d_slope_v018_signal(receivables):
    base = _mean(_log(receivables), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_63d_slope_v019_signal(receivables):
    base = _mean(_log(receivables), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_63d_slope_v020_signal(receivables):
    base = _mean(_log(receivables), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_63d_slope_v021_signal(receivables):
    base = _mean(_log(receivables), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_126d_slope_v022_signal(receivables):
    base = _mean(_log(receivables), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_126d_slope_v023_signal(receivables):
    base = _mean(_log(receivables), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_126d_slope_v024_signal(receivables):
    base = _mean(_log(receivables), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_252d_slope_v025_signal(receivables):
    base = _mean(_log(receivables), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_252d_slope_v026_signal(receivables):
    base = _mean(_log(receivables), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_252d_slope_v027_signal(receivables):
    base = _mean(_log(receivables), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_504d_slope_v028_signal(receivables):
    base = _mean(_log(receivables), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_504d_slope_v029_signal(receivables):
    base = _mean(_log(receivables), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log receivables
def gm_f57_biotech_f57_days_sales_outstanding_log_504d_slope_v030_signal(receivables):
    base = _mean(_log(receivables), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_21d_slope_v031_signal(receivables):
    base = _z(receivables, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_21d_slope_v032_signal(receivables):
    base = _z(receivables, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_21d_slope_v033_signal(receivables):
    base = _z(receivables, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_63d_slope_v034_signal(receivables):
    base = _z(receivables, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_63d_slope_v035_signal(receivables):
    base = _z(receivables, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_63d_slope_v036_signal(receivables):
    base = _z(receivables, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_126d_slope_v037_signal(receivables):
    base = _z(receivables, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_126d_slope_v038_signal(receivables):
    base = _z(receivables, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_126d_slope_v039_signal(receivables):
    base = _z(receivables, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_252d_slope_v040_signal(receivables):
    base = _z(receivables, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_252d_slope_v041_signal(receivables):
    base = _z(receivables, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_252d_slope_v042_signal(receivables):
    base = _z(receivables, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_504d_slope_v043_signal(receivables):
    base = _z(receivables, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_504d_slope_v044_signal(receivables):
    base = _z(receivables, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z receivables
def gm_f57_biotech_f57_days_sales_outstanding_z_504d_slope_v045_signal(receivables):
    base = _z(receivables, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_21d_slope_v046_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_21d_slope_v047_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_21d_slope_v048_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_63d_slope_v049_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_63d_slope_v050_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_63d_slope_v051_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_126d_slope_v052_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_126d_slope_v053_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_126d_slope_v054_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_252d_slope_v055_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_252d_slope_v056_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_252d_slope_v057_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_504d_slope_v058_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_504d_slope_v059_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps receivables
def gm_f57_biotech_f57_days_sales_outstanding_ps_504d_slope_v060_signal(receivables, sharesbas):
    base = _safe_div(_mean(receivables, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_21d_slope_v061_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_21d_slope_v062_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_21d_slope_v063_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_63d_slope_v064_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_63d_slope_v065_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_63d_slope_v066_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_126d_slope_v067_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_126d_slope_v068_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_126d_slope_v069_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_252d_slope_v070_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_252d_slope_v071_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_252d_slope_v072_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_504d_slope_v073_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_504d_slope_v074_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_asset_scaled_504d_slope_v075_signal(receivables, assets):
    base = _safe_div(_mean(receivables, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_21d_slope_v076_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_21d_slope_v077_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_21d_slope_v078_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_63d_slope_v079_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_63d_slope_v080_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_63d_slope_v081_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_126d_slope_v082_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_126d_slope_v083_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_126d_slope_v084_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_252d_slope_v085_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_252d_slope_v086_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_252d_slope_v087_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_504d_slope_v088_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_504d_slope_v089_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled receivables
def gm_f57_biotech_f57_days_sales_outstanding_mcap_scaled_504d_slope_v090_signal(receivables, marketcap):
    base = _safe_div(_mean(receivables, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_21d_slope_v091_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(21).min(), receivables.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_21d_slope_v092_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(21).min(), receivables.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_21d_slope_v093_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(21).min(), receivables.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_63d_slope_v094_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(63).min(), receivables.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_63d_slope_v095_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(63).min(), receivables.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_63d_slope_v096_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(63).min(), receivables.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_126d_slope_v097_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(126).min(), receivables.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_126d_slope_v098_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(126).min(), receivables.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_126d_slope_v099_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(126).min(), receivables.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_252d_slope_v100_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(252).min(), receivables.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_252d_slope_v101_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(252).min(), receivables.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_252d_slope_v102_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(252).min(), receivables.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_504d_slope_v103_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(504).min(), receivables.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_504d_slope_v104_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(504).min(), receivables.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_low_504d_slope_v105_signal(receivables):
    base = _safe_div(receivables - receivables.rolling(504).min(), receivables.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_21d_slope_v106_signal(receivables):
    base = _safe_div(receivables.rolling(21).max() - receivables, receivables.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_21d_slope_v107_signal(receivables):
    base = _safe_div(receivables.rolling(21).max() - receivables, receivables.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_21d_slope_v108_signal(receivables):
    base = _safe_div(receivables.rolling(21).max() - receivables, receivables.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_63d_slope_v109_signal(receivables):
    base = _safe_div(receivables.rolling(63).max() - receivables, receivables.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_63d_slope_v110_signal(receivables):
    base = _safe_div(receivables.rolling(63).max() - receivables, receivables.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_63d_slope_v111_signal(receivables):
    base = _safe_div(receivables.rolling(63).max() - receivables, receivables.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_126d_slope_v112_signal(receivables):
    base = _safe_div(receivables.rolling(126).max() - receivables, receivables.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_126d_slope_v113_signal(receivables):
    base = _safe_div(receivables.rolling(126).max() - receivables, receivables.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_126d_slope_v114_signal(receivables):
    base = _safe_div(receivables.rolling(126).max() - receivables, receivables.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_252d_slope_v115_signal(receivables):
    base = _safe_div(receivables.rolling(252).max() - receivables, receivables.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_252d_slope_v116_signal(receivables):
    base = _safe_div(receivables.rolling(252).max() - receivables, receivables.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_252d_slope_v117_signal(receivables):
    base = _safe_div(receivables.rolling(252).max() - receivables, receivables.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_504d_slope_v118_signal(receivables):
    base = _safe_div(receivables.rolling(504).max() - receivables, receivables.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_504d_slope_v119_signal(receivables):
    base = _safe_div(receivables.rolling(504).max() - receivables, receivables.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high receivables
def gm_f57_biotech_f57_days_sales_outstanding_dist_high_504d_slope_v120_signal(receivables):
    base = _safe_div(receivables.rolling(504).max() - receivables, receivables.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_21d_slope_v121_signal(receivables):
    base = _safe_div(_mean(receivables, 21) - _mean(receivables, 42), _mean(receivables, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_21d_slope_v122_signal(receivables):
    base = _safe_div(_mean(receivables, 21) - _mean(receivables, 42), _mean(receivables, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_21d_slope_v123_signal(receivables):
    base = _safe_div(_mean(receivables, 21) - _mean(receivables, 42), _mean(receivables, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_63d_slope_v124_signal(receivables):
    base = _safe_div(_mean(receivables, 63) - _mean(receivables, 126), _mean(receivables, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_63d_slope_v125_signal(receivables):
    base = _safe_div(_mean(receivables, 63) - _mean(receivables, 126), _mean(receivables, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_63d_slope_v126_signal(receivables):
    base = _safe_div(_mean(receivables, 63) - _mean(receivables, 126), _mean(receivables, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_126d_slope_v127_signal(receivables):
    base = _safe_div(_mean(receivables, 126) - _mean(receivables, 252), _mean(receivables, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_126d_slope_v128_signal(receivables):
    base = _safe_div(_mean(receivables, 126) - _mean(receivables, 252), _mean(receivables, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_126d_slope_v129_signal(receivables):
    base = _safe_div(_mean(receivables, 126) - _mean(receivables, 252), _mean(receivables, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_252d_slope_v130_signal(receivables):
    base = _safe_div(_mean(receivables, 252) - _mean(receivables, 504), _mean(receivables, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_252d_slope_v131_signal(receivables):
    base = _safe_div(_mean(receivables, 252) - _mean(receivables, 504), _mean(receivables, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_252d_slope_v132_signal(receivables):
    base = _safe_div(_mean(receivables, 252) - _mean(receivables, 504), _mean(receivables, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_504d_slope_v133_signal(receivables):
    base = _safe_div(_mean(receivables, 504) - _mean(receivables, 1008), _mean(receivables, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_504d_slope_v134_signal(receivables):
    base = _safe_div(_mean(receivables, 504) - _mean(receivables, 1008), _mean(receivables, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom receivables
def gm_f57_biotech_f57_days_sales_outstanding_mom_504d_slope_v135_signal(receivables):
    base = _safe_div(_mean(receivables, 504) - _mean(receivables, 1008), _mean(receivables, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_21d_slope_v136_signal(receivables):
    base = _std(receivables, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_21d_slope_v137_signal(receivables):
    base = _std(receivables, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_21d_slope_v138_signal(receivables):
    base = _std(receivables, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_63d_slope_v139_signal(receivables):
    base = _std(receivables, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_63d_slope_v140_signal(receivables):
    base = _std(receivables, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_63d_slope_v141_signal(receivables):
    base = _std(receivables, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_126d_slope_v142_signal(receivables):
    base = _std(receivables, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_126d_slope_v143_signal(receivables):
    base = _std(receivables, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_126d_slope_v144_signal(receivables):
    base = _std(receivables, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_252d_slope_v145_signal(receivables):
    base = _std(receivables, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_252d_slope_v146_signal(receivables):
    base = _std(receivables, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_252d_slope_v147_signal(receivables):
    base = _std(receivables, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_504d_slope_v148_signal(receivables):
    base = _std(receivables, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_504d_slope_v149_signal(receivables):
    base = _std(receivables, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol receivables
def gm_f57_biotech_f57_days_sales_outstanding_vol_504d_slope_v150_signal(receivables):
    base = _std(receivables, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

