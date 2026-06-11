
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_21d_slope_v001_signal(ncff):
    base = _mean(ncff, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_21d_slope_v002_signal(ncff):
    base = _mean(ncff, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_21d_slope_v003_signal(ncff):
    base = _mean(ncff, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_63d_slope_v004_signal(ncff):
    base = _mean(ncff, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_63d_slope_v005_signal(ncff):
    base = _mean(ncff, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_63d_slope_v006_signal(ncff):
    base = _mean(ncff, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_126d_slope_v007_signal(ncff):
    base = _mean(ncff, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_126d_slope_v008_signal(ncff):
    base = _mean(ncff, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_126d_slope_v009_signal(ncff):
    base = _mean(ncff, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_252d_slope_v010_signal(ncff):
    base = _mean(ncff, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_252d_slope_v011_signal(ncff):
    base = _mean(ncff, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_252d_slope_v012_signal(ncff):
    base = _mean(ncff, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_504d_slope_v013_signal(ncff):
    base = _mean(ncff, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_504d_slope_v014_signal(ncff):
    base = _mean(ncff, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_raw_504d_slope_v015_signal(ncff):
    base = _mean(ncff, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_21d_slope_v016_signal(ncff):
    base = _mean(_log(ncff), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_21d_slope_v017_signal(ncff):
    base = _mean(_log(ncff), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_21d_slope_v018_signal(ncff):
    base = _mean(_log(ncff), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_63d_slope_v019_signal(ncff):
    base = _mean(_log(ncff), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_63d_slope_v020_signal(ncff):
    base = _mean(_log(ncff), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_63d_slope_v021_signal(ncff):
    base = _mean(_log(ncff), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_126d_slope_v022_signal(ncff):
    base = _mean(_log(ncff), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_126d_slope_v023_signal(ncff):
    base = _mean(_log(ncff), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_126d_slope_v024_signal(ncff):
    base = _mean(_log(ncff), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_252d_slope_v025_signal(ncff):
    base = _mean(_log(ncff), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_252d_slope_v026_signal(ncff):
    base = _mean(_log(ncff), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_252d_slope_v027_signal(ncff):
    base = _mean(_log(ncff), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_504d_slope_v028_signal(ncff):
    base = _mean(_log(ncff), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_504d_slope_v029_signal(ncff):
    base = _mean(_log(ncff), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_log_504d_slope_v030_signal(ncff):
    base = _mean(_log(ncff), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_21d_slope_v031_signal(ncff):
    base = _z(ncff, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_21d_slope_v032_signal(ncff):
    base = _z(ncff, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_21d_slope_v033_signal(ncff):
    base = _z(ncff, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_63d_slope_v034_signal(ncff):
    base = _z(ncff, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_63d_slope_v035_signal(ncff):
    base = _z(ncff, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_63d_slope_v036_signal(ncff):
    base = _z(ncff, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_126d_slope_v037_signal(ncff):
    base = _z(ncff, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_126d_slope_v038_signal(ncff):
    base = _z(ncff, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_126d_slope_v039_signal(ncff):
    base = _z(ncff, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_252d_slope_v040_signal(ncff):
    base = _z(ncff, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_252d_slope_v041_signal(ncff):
    base = _z(ncff, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_252d_slope_v042_signal(ncff):
    base = _z(ncff, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_504d_slope_v043_signal(ncff):
    base = _z(ncff, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_504d_slope_v044_signal(ncff):
    base = _z(ncff, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_z_504d_slope_v045_signal(ncff):
    base = _z(ncff, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_21d_slope_v046_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_21d_slope_v047_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_21d_slope_v048_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_63d_slope_v049_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_63d_slope_v050_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_63d_slope_v051_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_126d_slope_v052_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_126d_slope_v053_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_126d_slope_v054_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_252d_slope_v055_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_252d_slope_v056_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_252d_slope_v057_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_504d_slope_v058_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_504d_slope_v059_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ps_504d_slope_v060_signal(ncff, sharesbas):
    base = _safe_div(_mean(ncff, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_21d_slope_v061_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_21d_slope_v062_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_21d_slope_v063_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_63d_slope_v064_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_63d_slope_v065_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_63d_slope_v066_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_126d_slope_v067_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_126d_slope_v068_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_126d_slope_v069_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_252d_slope_v070_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_252d_slope_v071_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_252d_slope_v072_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_504d_slope_v073_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_504d_slope_v074_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_asset_scaled_504d_slope_v075_signal(ncff, assets):
    base = _safe_div(_mean(ncff, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_21d_slope_v076_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_21d_slope_v077_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_21d_slope_v078_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_63d_slope_v079_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_63d_slope_v080_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_63d_slope_v081_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_126d_slope_v082_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_126d_slope_v083_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_126d_slope_v084_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_252d_slope_v085_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_252d_slope_v086_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_252d_slope_v087_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_504d_slope_v088_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_504d_slope_v089_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mcap_scaled_504d_slope_v090_signal(ncff, marketcap):
    base = _safe_div(_mean(ncff, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_21d_slope_v091_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(21).min(), ncff.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_21d_slope_v092_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(21).min(), ncff.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_21d_slope_v093_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(21).min(), ncff.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_63d_slope_v094_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(63).min(), ncff.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_63d_slope_v095_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(63).min(), ncff.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_63d_slope_v096_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(63).min(), ncff.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_126d_slope_v097_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(126).min(), ncff.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_126d_slope_v098_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(126).min(), ncff.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_126d_slope_v099_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(126).min(), ncff.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_252d_slope_v100_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(252).min(), ncff.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_252d_slope_v101_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(252).min(), ncff.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_252d_slope_v102_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(252).min(), ncff.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_504d_slope_v103_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(504).min(), ncff.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_504d_slope_v104_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(504).min(), ncff.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_low_504d_slope_v105_signal(ncff):
    base = _safe_div(ncff - ncff.rolling(504).min(), ncff.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_21d_slope_v106_signal(ncff):
    base = _safe_div(ncff.rolling(21).max() - ncff, ncff.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_21d_slope_v107_signal(ncff):
    base = _safe_div(ncff.rolling(21).max() - ncff, ncff.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_21d_slope_v108_signal(ncff):
    base = _safe_div(ncff.rolling(21).max() - ncff, ncff.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_63d_slope_v109_signal(ncff):
    base = _safe_div(ncff.rolling(63).max() - ncff, ncff.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_63d_slope_v110_signal(ncff):
    base = _safe_div(ncff.rolling(63).max() - ncff, ncff.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_63d_slope_v111_signal(ncff):
    base = _safe_div(ncff.rolling(63).max() - ncff, ncff.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_126d_slope_v112_signal(ncff):
    base = _safe_div(ncff.rolling(126).max() - ncff, ncff.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_126d_slope_v113_signal(ncff):
    base = _safe_div(ncff.rolling(126).max() - ncff, ncff.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_126d_slope_v114_signal(ncff):
    base = _safe_div(ncff.rolling(126).max() - ncff, ncff.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_252d_slope_v115_signal(ncff):
    base = _safe_div(ncff.rolling(252).max() - ncff, ncff.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_252d_slope_v116_signal(ncff):
    base = _safe_div(ncff.rolling(252).max() - ncff, ncff.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_252d_slope_v117_signal(ncff):
    base = _safe_div(ncff.rolling(252).max() - ncff, ncff.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_504d_slope_v118_signal(ncff):
    base = _safe_div(ncff.rolling(504).max() - ncff, ncff.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_504d_slope_v119_signal(ncff):
    base = _safe_div(ncff.rolling(504).max() - ncff, ncff.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_dist_high_504d_slope_v120_signal(ncff):
    base = _safe_div(ncff.rolling(504).max() - ncff, ncff.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_21d_slope_v121_signal(ncff):
    base = _safe_div(_mean(ncff, 21) - _mean(ncff, 42), _mean(ncff, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_21d_slope_v122_signal(ncff):
    base = _safe_div(_mean(ncff, 21) - _mean(ncff, 42), _mean(ncff, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_21d_slope_v123_signal(ncff):
    base = _safe_div(_mean(ncff, 21) - _mean(ncff, 42), _mean(ncff, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_63d_slope_v124_signal(ncff):
    base = _safe_div(_mean(ncff, 63) - _mean(ncff, 126), _mean(ncff, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_63d_slope_v125_signal(ncff):
    base = _safe_div(_mean(ncff, 63) - _mean(ncff, 126), _mean(ncff, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_63d_slope_v126_signal(ncff):
    base = _safe_div(_mean(ncff, 63) - _mean(ncff, 126), _mean(ncff, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_126d_slope_v127_signal(ncff):
    base = _safe_div(_mean(ncff, 126) - _mean(ncff, 252), _mean(ncff, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_126d_slope_v128_signal(ncff):
    base = _safe_div(_mean(ncff, 126) - _mean(ncff, 252), _mean(ncff, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_126d_slope_v129_signal(ncff):
    base = _safe_div(_mean(ncff, 126) - _mean(ncff, 252), _mean(ncff, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_252d_slope_v130_signal(ncff):
    base = _safe_div(_mean(ncff, 252) - _mean(ncff, 504), _mean(ncff, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_252d_slope_v131_signal(ncff):
    base = _safe_div(_mean(ncff, 252) - _mean(ncff, 504), _mean(ncff, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_252d_slope_v132_signal(ncff):
    base = _safe_div(_mean(ncff, 252) - _mean(ncff, 504), _mean(ncff, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_504d_slope_v133_signal(ncff):
    base = _safe_div(_mean(ncff, 504) - _mean(ncff, 1008), _mean(ncff, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_504d_slope_v134_signal(ncff):
    base = _safe_div(_mean(ncff, 504) - _mean(ncff, 1008), _mean(ncff, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mom_504d_slope_v135_signal(ncff):
    base = _safe_div(_mean(ncff, 504) - _mean(ncff, 1008), _mean(ncff, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_21d_slope_v136_signal(ncff):
    base = _std(ncff, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_21d_slope_v137_signal(ncff):
    base = _std(ncff, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_21d_slope_v138_signal(ncff):
    base = _std(ncff, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_63d_slope_v139_signal(ncff):
    base = _std(ncff, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_63d_slope_v140_signal(ncff):
    base = _std(ncff, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_63d_slope_v141_signal(ncff):
    base = _std(ncff, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_126d_slope_v142_signal(ncff):
    base = _std(ncff, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_126d_slope_v143_signal(ncff):
    base = _std(ncff, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_126d_slope_v144_signal(ncff):
    base = _std(ncff, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_252d_slope_v145_signal(ncff):
    base = _std(ncff, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_252d_slope_v146_signal(ncff):
    base = _std(ncff, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_252d_slope_v147_signal(ncff):
    base = _std(ncff, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_504d_slope_v148_signal(ncff):
    base = _std(ncff, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_504d_slope_v149_signal(ncff):
    base = _std(ncff, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_vol_504d_slope_v150_signal(ncff):
    base = _std(ncff, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

