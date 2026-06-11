
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_21d_slope_v001_signal(cor):
    base = _mean(cor, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_21d_slope_v002_signal(cor):
    base = _mean(cor, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_21d_slope_v003_signal(cor):
    base = _mean(cor, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_63d_slope_v004_signal(cor):
    base = _mean(cor, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_63d_slope_v005_signal(cor):
    base = _mean(cor, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_63d_slope_v006_signal(cor):
    base = _mean(cor, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_126d_slope_v007_signal(cor):
    base = _mean(cor, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_126d_slope_v008_signal(cor):
    base = _mean(cor, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_126d_slope_v009_signal(cor):
    base = _mean(cor, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_252d_slope_v010_signal(cor):
    base = _mean(cor, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_252d_slope_v011_signal(cor):
    base = _mean(cor, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_252d_slope_v012_signal(cor):
    base = _mean(cor, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_504d_slope_v013_signal(cor):
    base = _mean(cor, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_504d_slope_v014_signal(cor):
    base = _mean(cor, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw cor
def gm_f59_biotech_f59_inventory_turnover_ratio_raw_504d_slope_v015_signal(cor):
    base = _mean(cor, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_21d_slope_v016_signal(cor):
    base = _mean(_log(cor), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_21d_slope_v017_signal(cor):
    base = _mean(_log(cor), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_21d_slope_v018_signal(cor):
    base = _mean(_log(cor), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_63d_slope_v019_signal(cor):
    base = _mean(_log(cor), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_63d_slope_v020_signal(cor):
    base = _mean(_log(cor), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_63d_slope_v021_signal(cor):
    base = _mean(_log(cor), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_126d_slope_v022_signal(cor):
    base = _mean(_log(cor), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_126d_slope_v023_signal(cor):
    base = _mean(_log(cor), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_126d_slope_v024_signal(cor):
    base = _mean(_log(cor), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_252d_slope_v025_signal(cor):
    base = _mean(_log(cor), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_252d_slope_v026_signal(cor):
    base = _mean(_log(cor), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_252d_slope_v027_signal(cor):
    base = _mean(_log(cor), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_504d_slope_v028_signal(cor):
    base = _mean(_log(cor), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_504d_slope_v029_signal(cor):
    base = _mean(_log(cor), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log cor
def gm_f59_biotech_f59_inventory_turnover_ratio_log_504d_slope_v030_signal(cor):
    base = _mean(_log(cor), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_21d_slope_v031_signal(cor):
    base = _z(cor, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_21d_slope_v032_signal(cor):
    base = _z(cor, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_21d_slope_v033_signal(cor):
    base = _z(cor, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_63d_slope_v034_signal(cor):
    base = _z(cor, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_63d_slope_v035_signal(cor):
    base = _z(cor, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_63d_slope_v036_signal(cor):
    base = _z(cor, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_126d_slope_v037_signal(cor):
    base = _z(cor, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_126d_slope_v038_signal(cor):
    base = _z(cor, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_126d_slope_v039_signal(cor):
    base = _z(cor, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_252d_slope_v040_signal(cor):
    base = _z(cor, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_252d_slope_v041_signal(cor):
    base = _z(cor, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_252d_slope_v042_signal(cor):
    base = _z(cor, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_504d_slope_v043_signal(cor):
    base = _z(cor, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_504d_slope_v044_signal(cor):
    base = _z(cor, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z cor
def gm_f59_biotech_f59_inventory_turnover_ratio_z_504d_slope_v045_signal(cor):
    base = _z(cor, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_21d_slope_v046_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_21d_slope_v047_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_21d_slope_v048_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_63d_slope_v049_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_63d_slope_v050_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_63d_slope_v051_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_126d_slope_v052_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_126d_slope_v053_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_126d_slope_v054_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_252d_slope_v055_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_252d_slope_v056_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_252d_slope_v057_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_504d_slope_v058_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_504d_slope_v059_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps cor
def gm_f59_biotech_f59_inventory_turnover_ratio_ps_504d_slope_v060_signal(cor, sharesbas):
    base = _safe_div(_mean(cor, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_21d_slope_v061_signal(cor, assets):
    base = _safe_div(_mean(cor, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_21d_slope_v062_signal(cor, assets):
    base = _safe_div(_mean(cor, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_21d_slope_v063_signal(cor, assets):
    base = _safe_div(_mean(cor, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_63d_slope_v064_signal(cor, assets):
    base = _safe_div(_mean(cor, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_63d_slope_v065_signal(cor, assets):
    base = _safe_div(_mean(cor, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_63d_slope_v066_signal(cor, assets):
    base = _safe_div(_mean(cor, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_126d_slope_v067_signal(cor, assets):
    base = _safe_div(_mean(cor, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_126d_slope_v068_signal(cor, assets):
    base = _safe_div(_mean(cor, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_126d_slope_v069_signal(cor, assets):
    base = _safe_div(_mean(cor, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_252d_slope_v070_signal(cor, assets):
    base = _safe_div(_mean(cor, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_252d_slope_v071_signal(cor, assets):
    base = _safe_div(_mean(cor, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_252d_slope_v072_signal(cor, assets):
    base = _safe_div(_mean(cor, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_504d_slope_v073_signal(cor, assets):
    base = _safe_div(_mean(cor, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_504d_slope_v074_signal(cor, assets):
    base = _safe_div(_mean(cor, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_asset_scaled_504d_slope_v075_signal(cor, assets):
    base = _safe_div(_mean(cor, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_21d_slope_v076_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_21d_slope_v077_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_21d_slope_v078_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_63d_slope_v079_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_63d_slope_v080_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_63d_slope_v081_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_126d_slope_v082_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_126d_slope_v083_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_126d_slope_v084_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_252d_slope_v085_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_252d_slope_v086_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_252d_slope_v087_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_504d_slope_v088_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_504d_slope_v089_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mcap_scaled_504d_slope_v090_signal(cor, marketcap):
    base = _safe_div(_mean(cor, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_21d_slope_v091_signal(cor):
    base = _safe_div(cor - cor.rolling(21).min(), cor.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_21d_slope_v092_signal(cor):
    base = _safe_div(cor - cor.rolling(21).min(), cor.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_21d_slope_v093_signal(cor):
    base = _safe_div(cor - cor.rolling(21).min(), cor.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_63d_slope_v094_signal(cor):
    base = _safe_div(cor - cor.rolling(63).min(), cor.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_63d_slope_v095_signal(cor):
    base = _safe_div(cor - cor.rolling(63).min(), cor.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_63d_slope_v096_signal(cor):
    base = _safe_div(cor - cor.rolling(63).min(), cor.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_126d_slope_v097_signal(cor):
    base = _safe_div(cor - cor.rolling(126).min(), cor.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_126d_slope_v098_signal(cor):
    base = _safe_div(cor - cor.rolling(126).min(), cor.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_126d_slope_v099_signal(cor):
    base = _safe_div(cor - cor.rolling(126).min(), cor.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_252d_slope_v100_signal(cor):
    base = _safe_div(cor - cor.rolling(252).min(), cor.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_252d_slope_v101_signal(cor):
    base = _safe_div(cor - cor.rolling(252).min(), cor.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_252d_slope_v102_signal(cor):
    base = _safe_div(cor - cor.rolling(252).min(), cor.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_504d_slope_v103_signal(cor):
    base = _safe_div(cor - cor.rolling(504).min(), cor.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_504d_slope_v104_signal(cor):
    base = _safe_div(cor - cor.rolling(504).min(), cor.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_low_504d_slope_v105_signal(cor):
    base = _safe_div(cor - cor.rolling(504).min(), cor.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_21d_slope_v106_signal(cor):
    base = _safe_div(cor.rolling(21).max() - cor, cor.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_21d_slope_v107_signal(cor):
    base = _safe_div(cor.rolling(21).max() - cor, cor.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_21d_slope_v108_signal(cor):
    base = _safe_div(cor.rolling(21).max() - cor, cor.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_63d_slope_v109_signal(cor):
    base = _safe_div(cor.rolling(63).max() - cor, cor.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_63d_slope_v110_signal(cor):
    base = _safe_div(cor.rolling(63).max() - cor, cor.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_63d_slope_v111_signal(cor):
    base = _safe_div(cor.rolling(63).max() - cor, cor.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_126d_slope_v112_signal(cor):
    base = _safe_div(cor.rolling(126).max() - cor, cor.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_126d_slope_v113_signal(cor):
    base = _safe_div(cor.rolling(126).max() - cor, cor.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_126d_slope_v114_signal(cor):
    base = _safe_div(cor.rolling(126).max() - cor, cor.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_252d_slope_v115_signal(cor):
    base = _safe_div(cor.rolling(252).max() - cor, cor.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_252d_slope_v116_signal(cor):
    base = _safe_div(cor.rolling(252).max() - cor, cor.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_252d_slope_v117_signal(cor):
    base = _safe_div(cor.rolling(252).max() - cor, cor.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_504d_slope_v118_signal(cor):
    base = _safe_div(cor.rolling(504).max() - cor, cor.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_504d_slope_v119_signal(cor):
    base = _safe_div(cor.rolling(504).max() - cor, cor.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high cor
def gm_f59_biotech_f59_inventory_turnover_ratio_dist_high_504d_slope_v120_signal(cor):
    base = _safe_div(cor.rolling(504).max() - cor, cor.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_21d_slope_v121_signal(cor):
    base = _safe_div(_mean(cor, 21) - _mean(cor, 42), _mean(cor, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_21d_slope_v122_signal(cor):
    base = _safe_div(_mean(cor, 21) - _mean(cor, 42), _mean(cor, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_21d_slope_v123_signal(cor):
    base = _safe_div(_mean(cor, 21) - _mean(cor, 42), _mean(cor, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_63d_slope_v124_signal(cor):
    base = _safe_div(_mean(cor, 63) - _mean(cor, 126), _mean(cor, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_63d_slope_v125_signal(cor):
    base = _safe_div(_mean(cor, 63) - _mean(cor, 126), _mean(cor, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_63d_slope_v126_signal(cor):
    base = _safe_div(_mean(cor, 63) - _mean(cor, 126), _mean(cor, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_126d_slope_v127_signal(cor):
    base = _safe_div(_mean(cor, 126) - _mean(cor, 252), _mean(cor, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_126d_slope_v128_signal(cor):
    base = _safe_div(_mean(cor, 126) - _mean(cor, 252), _mean(cor, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_126d_slope_v129_signal(cor):
    base = _safe_div(_mean(cor, 126) - _mean(cor, 252), _mean(cor, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_252d_slope_v130_signal(cor):
    base = _safe_div(_mean(cor, 252) - _mean(cor, 504), _mean(cor, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_252d_slope_v131_signal(cor):
    base = _safe_div(_mean(cor, 252) - _mean(cor, 504), _mean(cor, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_252d_slope_v132_signal(cor):
    base = _safe_div(_mean(cor, 252) - _mean(cor, 504), _mean(cor, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_504d_slope_v133_signal(cor):
    base = _safe_div(_mean(cor, 504) - _mean(cor, 1008), _mean(cor, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_504d_slope_v134_signal(cor):
    base = _safe_div(_mean(cor, 504) - _mean(cor, 1008), _mean(cor, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom cor
def gm_f59_biotech_f59_inventory_turnover_ratio_mom_504d_slope_v135_signal(cor):
    base = _safe_div(_mean(cor, 504) - _mean(cor, 1008), _mean(cor, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_21d_slope_v136_signal(cor):
    base = _std(cor, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_21d_slope_v137_signal(cor):
    base = _std(cor, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_21d_slope_v138_signal(cor):
    base = _std(cor, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_63d_slope_v139_signal(cor):
    base = _std(cor, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_63d_slope_v140_signal(cor):
    base = _std(cor, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_63d_slope_v141_signal(cor):
    base = _std(cor, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_126d_slope_v142_signal(cor):
    base = _std(cor, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_126d_slope_v143_signal(cor):
    base = _std(cor, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_126d_slope_v144_signal(cor):
    base = _std(cor, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_252d_slope_v145_signal(cor):
    base = _std(cor, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_252d_slope_v146_signal(cor):
    base = _std(cor, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_252d_slope_v147_signal(cor):
    base = _std(cor, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_504d_slope_v148_signal(cor):
    base = _std(cor, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_504d_slope_v149_signal(cor):
    base = _std(cor, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol cor
def gm_f59_biotech_f59_inventory_turnover_ratio_vol_504d_slope_v150_signal(cor):
    base = _std(cor, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

