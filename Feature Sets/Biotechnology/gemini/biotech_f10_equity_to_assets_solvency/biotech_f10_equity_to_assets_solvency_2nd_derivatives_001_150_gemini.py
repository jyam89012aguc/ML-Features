
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_21d_slope_v001_signal(equity):
    base = _mean(equity, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_21d_slope_v002_signal(equity):
    base = _mean(equity, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_21d_slope_v003_signal(equity):
    base = _mean(equity, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_63d_slope_v004_signal(equity):
    base = _mean(equity, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_63d_slope_v005_signal(equity):
    base = _mean(equity, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_63d_slope_v006_signal(equity):
    base = _mean(equity, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_126d_slope_v007_signal(equity):
    base = _mean(equity, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_126d_slope_v008_signal(equity):
    base = _mean(equity, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_126d_slope_v009_signal(equity):
    base = _mean(equity, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_252d_slope_v010_signal(equity):
    base = _mean(equity, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_252d_slope_v011_signal(equity):
    base = _mean(equity, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_252d_slope_v012_signal(equity):
    base = _mean(equity, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_504d_slope_v013_signal(equity):
    base = _mean(equity, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_504d_slope_v014_signal(equity):
    base = _mean(equity, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw equity
def gm_f10_biotech_f10_equity_to_assets_solvency_raw_504d_slope_v015_signal(equity):
    base = _mean(equity, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_21d_slope_v016_signal(equity):
    base = _mean(_log(equity), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_21d_slope_v017_signal(equity):
    base = _mean(_log(equity), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_21d_slope_v018_signal(equity):
    base = _mean(_log(equity), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_63d_slope_v019_signal(equity):
    base = _mean(_log(equity), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_63d_slope_v020_signal(equity):
    base = _mean(_log(equity), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_63d_slope_v021_signal(equity):
    base = _mean(_log(equity), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_126d_slope_v022_signal(equity):
    base = _mean(_log(equity), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_126d_slope_v023_signal(equity):
    base = _mean(_log(equity), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_126d_slope_v024_signal(equity):
    base = _mean(_log(equity), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_252d_slope_v025_signal(equity):
    base = _mean(_log(equity), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_252d_slope_v026_signal(equity):
    base = _mean(_log(equity), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_252d_slope_v027_signal(equity):
    base = _mean(_log(equity), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_504d_slope_v028_signal(equity):
    base = _mean(_log(equity), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_504d_slope_v029_signal(equity):
    base = _mean(_log(equity), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log equity
def gm_f10_biotech_f10_equity_to_assets_solvency_log_504d_slope_v030_signal(equity):
    base = _mean(_log(equity), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_21d_slope_v031_signal(equity):
    base = _z(equity, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_21d_slope_v032_signal(equity):
    base = _z(equity, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_21d_slope_v033_signal(equity):
    base = _z(equity, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_63d_slope_v034_signal(equity):
    base = _z(equity, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_63d_slope_v035_signal(equity):
    base = _z(equity, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_63d_slope_v036_signal(equity):
    base = _z(equity, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_126d_slope_v037_signal(equity):
    base = _z(equity, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_126d_slope_v038_signal(equity):
    base = _z(equity, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_126d_slope_v039_signal(equity):
    base = _z(equity, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_252d_slope_v040_signal(equity):
    base = _z(equity, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_252d_slope_v041_signal(equity):
    base = _z(equity, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_252d_slope_v042_signal(equity):
    base = _z(equity, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_504d_slope_v043_signal(equity):
    base = _z(equity, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_504d_slope_v044_signal(equity):
    base = _z(equity, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z equity
def gm_f10_biotech_f10_equity_to_assets_solvency_z_504d_slope_v045_signal(equity):
    base = _z(equity, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_21d_slope_v046_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_21d_slope_v047_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_21d_slope_v048_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_63d_slope_v049_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_63d_slope_v050_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_63d_slope_v051_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_126d_slope_v052_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_126d_slope_v053_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_126d_slope_v054_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_252d_slope_v055_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_252d_slope_v056_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_252d_slope_v057_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_504d_slope_v058_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_504d_slope_v059_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps equity
def gm_f10_biotech_f10_equity_to_assets_solvency_ps_504d_slope_v060_signal(equity, sharesbas):
    base = _safe_div(_mean(equity, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_21d_slope_v061_signal(equity, assets):
    base = _safe_div(_mean(equity, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_21d_slope_v062_signal(equity, assets):
    base = _safe_div(_mean(equity, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_21d_slope_v063_signal(equity, assets):
    base = _safe_div(_mean(equity, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_63d_slope_v064_signal(equity, assets):
    base = _safe_div(_mean(equity, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_63d_slope_v065_signal(equity, assets):
    base = _safe_div(_mean(equity, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_63d_slope_v066_signal(equity, assets):
    base = _safe_div(_mean(equity, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_126d_slope_v067_signal(equity, assets):
    base = _safe_div(_mean(equity, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_126d_slope_v068_signal(equity, assets):
    base = _safe_div(_mean(equity, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_126d_slope_v069_signal(equity, assets):
    base = _safe_div(_mean(equity, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_252d_slope_v070_signal(equity, assets):
    base = _safe_div(_mean(equity, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_252d_slope_v071_signal(equity, assets):
    base = _safe_div(_mean(equity, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_252d_slope_v072_signal(equity, assets):
    base = _safe_div(_mean(equity, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_504d_slope_v073_signal(equity, assets):
    base = _safe_div(_mean(equity, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_504d_slope_v074_signal(equity, assets):
    base = _safe_div(_mean(equity, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_asset_scaled_504d_slope_v075_signal(equity, assets):
    base = _safe_div(_mean(equity, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_21d_slope_v076_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_21d_slope_v077_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_21d_slope_v078_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_63d_slope_v079_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_63d_slope_v080_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_63d_slope_v081_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_126d_slope_v082_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_126d_slope_v083_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_126d_slope_v084_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_252d_slope_v085_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_252d_slope_v086_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_252d_slope_v087_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_504d_slope_v088_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_504d_slope_v089_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mcap_scaled_504d_slope_v090_signal(equity, marketcap):
    base = _safe_div(_mean(equity, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_21d_slope_v091_signal(equity):
    base = _safe_div(equity - equity.rolling(21).min(), equity.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_21d_slope_v092_signal(equity):
    base = _safe_div(equity - equity.rolling(21).min(), equity.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_21d_slope_v093_signal(equity):
    base = _safe_div(equity - equity.rolling(21).min(), equity.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_63d_slope_v094_signal(equity):
    base = _safe_div(equity - equity.rolling(63).min(), equity.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_63d_slope_v095_signal(equity):
    base = _safe_div(equity - equity.rolling(63).min(), equity.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_63d_slope_v096_signal(equity):
    base = _safe_div(equity - equity.rolling(63).min(), equity.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_126d_slope_v097_signal(equity):
    base = _safe_div(equity - equity.rolling(126).min(), equity.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_126d_slope_v098_signal(equity):
    base = _safe_div(equity - equity.rolling(126).min(), equity.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_126d_slope_v099_signal(equity):
    base = _safe_div(equity - equity.rolling(126).min(), equity.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_252d_slope_v100_signal(equity):
    base = _safe_div(equity - equity.rolling(252).min(), equity.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_252d_slope_v101_signal(equity):
    base = _safe_div(equity - equity.rolling(252).min(), equity.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_252d_slope_v102_signal(equity):
    base = _safe_div(equity - equity.rolling(252).min(), equity.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_504d_slope_v103_signal(equity):
    base = _safe_div(equity - equity.rolling(504).min(), equity.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_504d_slope_v104_signal(equity):
    base = _safe_div(equity - equity.rolling(504).min(), equity.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_low_504d_slope_v105_signal(equity):
    base = _safe_div(equity - equity.rolling(504).min(), equity.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_21d_slope_v106_signal(equity):
    base = _safe_div(equity.rolling(21).max() - equity, equity.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_21d_slope_v107_signal(equity):
    base = _safe_div(equity.rolling(21).max() - equity, equity.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_21d_slope_v108_signal(equity):
    base = _safe_div(equity.rolling(21).max() - equity, equity.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_63d_slope_v109_signal(equity):
    base = _safe_div(equity.rolling(63).max() - equity, equity.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_63d_slope_v110_signal(equity):
    base = _safe_div(equity.rolling(63).max() - equity, equity.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_63d_slope_v111_signal(equity):
    base = _safe_div(equity.rolling(63).max() - equity, equity.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_126d_slope_v112_signal(equity):
    base = _safe_div(equity.rolling(126).max() - equity, equity.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_126d_slope_v113_signal(equity):
    base = _safe_div(equity.rolling(126).max() - equity, equity.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_126d_slope_v114_signal(equity):
    base = _safe_div(equity.rolling(126).max() - equity, equity.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_252d_slope_v115_signal(equity):
    base = _safe_div(equity.rolling(252).max() - equity, equity.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_252d_slope_v116_signal(equity):
    base = _safe_div(equity.rolling(252).max() - equity, equity.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_252d_slope_v117_signal(equity):
    base = _safe_div(equity.rolling(252).max() - equity, equity.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_504d_slope_v118_signal(equity):
    base = _safe_div(equity.rolling(504).max() - equity, equity.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_504d_slope_v119_signal(equity):
    base = _safe_div(equity.rolling(504).max() - equity, equity.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high equity
def gm_f10_biotech_f10_equity_to_assets_solvency_dist_high_504d_slope_v120_signal(equity):
    base = _safe_div(equity.rolling(504).max() - equity, equity.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_21d_slope_v121_signal(equity):
    base = _safe_div(_mean(equity, 21) - _mean(equity, 42), _mean(equity, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_21d_slope_v122_signal(equity):
    base = _safe_div(_mean(equity, 21) - _mean(equity, 42), _mean(equity, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_21d_slope_v123_signal(equity):
    base = _safe_div(_mean(equity, 21) - _mean(equity, 42), _mean(equity, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_63d_slope_v124_signal(equity):
    base = _safe_div(_mean(equity, 63) - _mean(equity, 126), _mean(equity, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_63d_slope_v125_signal(equity):
    base = _safe_div(_mean(equity, 63) - _mean(equity, 126), _mean(equity, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_63d_slope_v126_signal(equity):
    base = _safe_div(_mean(equity, 63) - _mean(equity, 126), _mean(equity, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_126d_slope_v127_signal(equity):
    base = _safe_div(_mean(equity, 126) - _mean(equity, 252), _mean(equity, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_126d_slope_v128_signal(equity):
    base = _safe_div(_mean(equity, 126) - _mean(equity, 252), _mean(equity, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_126d_slope_v129_signal(equity):
    base = _safe_div(_mean(equity, 126) - _mean(equity, 252), _mean(equity, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_252d_slope_v130_signal(equity):
    base = _safe_div(_mean(equity, 252) - _mean(equity, 504), _mean(equity, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_252d_slope_v131_signal(equity):
    base = _safe_div(_mean(equity, 252) - _mean(equity, 504), _mean(equity, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_252d_slope_v132_signal(equity):
    base = _safe_div(_mean(equity, 252) - _mean(equity, 504), _mean(equity, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_504d_slope_v133_signal(equity):
    base = _safe_div(_mean(equity, 504) - _mean(equity, 1008), _mean(equity, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_504d_slope_v134_signal(equity):
    base = _safe_div(_mean(equity, 504) - _mean(equity, 1008), _mean(equity, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom equity
def gm_f10_biotech_f10_equity_to_assets_solvency_mom_504d_slope_v135_signal(equity):
    base = _safe_div(_mean(equity, 504) - _mean(equity, 1008), _mean(equity, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_21d_slope_v136_signal(equity):
    base = _std(equity, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_21d_slope_v137_signal(equity):
    base = _std(equity, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_21d_slope_v138_signal(equity):
    base = _std(equity, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_63d_slope_v139_signal(equity):
    base = _std(equity, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_63d_slope_v140_signal(equity):
    base = _std(equity, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_63d_slope_v141_signal(equity):
    base = _std(equity, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_126d_slope_v142_signal(equity):
    base = _std(equity, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_126d_slope_v143_signal(equity):
    base = _std(equity, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_126d_slope_v144_signal(equity):
    base = _std(equity, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_252d_slope_v145_signal(equity):
    base = _std(equity, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_252d_slope_v146_signal(equity):
    base = _std(equity, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_252d_slope_v147_signal(equity):
    base = _std(equity, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_504d_slope_v148_signal(equity):
    base = _std(equity, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_504d_slope_v149_signal(equity):
    base = _std(equity, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol equity
def gm_f10_biotech_f10_equity_to_assets_solvency_vol_504d_slope_v150_signal(equity):
    base = _std(equity, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

