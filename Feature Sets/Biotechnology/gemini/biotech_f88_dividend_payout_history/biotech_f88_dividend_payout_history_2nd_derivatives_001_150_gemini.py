
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw action
def gm_f88_biotech_f88_dividend_payout_history_raw_21d_slope_v001_signal(action):
    base = _mean(action, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw action
def gm_f88_biotech_f88_dividend_payout_history_raw_21d_slope_v002_signal(action):
    base = _mean(action, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw action
def gm_f88_biotech_f88_dividend_payout_history_raw_21d_slope_v003_signal(action):
    base = _mean(action, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw action
def gm_f88_biotech_f88_dividend_payout_history_raw_63d_slope_v004_signal(action):
    base = _mean(action, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw action
def gm_f88_biotech_f88_dividend_payout_history_raw_63d_slope_v005_signal(action):
    base = _mean(action, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw action
def gm_f88_biotech_f88_dividend_payout_history_raw_63d_slope_v006_signal(action):
    base = _mean(action, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw action
def gm_f88_biotech_f88_dividend_payout_history_raw_126d_slope_v007_signal(action):
    base = _mean(action, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw action
def gm_f88_biotech_f88_dividend_payout_history_raw_126d_slope_v008_signal(action):
    base = _mean(action, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw action
def gm_f88_biotech_f88_dividend_payout_history_raw_126d_slope_v009_signal(action):
    base = _mean(action, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw action
def gm_f88_biotech_f88_dividend_payout_history_raw_252d_slope_v010_signal(action):
    base = _mean(action, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw action
def gm_f88_biotech_f88_dividend_payout_history_raw_252d_slope_v011_signal(action):
    base = _mean(action, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw action
def gm_f88_biotech_f88_dividend_payout_history_raw_252d_slope_v012_signal(action):
    base = _mean(action, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw action
def gm_f88_biotech_f88_dividend_payout_history_raw_504d_slope_v013_signal(action):
    base = _mean(action, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw action
def gm_f88_biotech_f88_dividend_payout_history_raw_504d_slope_v014_signal(action):
    base = _mean(action, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw action
def gm_f88_biotech_f88_dividend_payout_history_raw_504d_slope_v015_signal(action):
    base = _mean(action, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log action
def gm_f88_biotech_f88_dividend_payout_history_log_21d_slope_v016_signal(action):
    base = _mean(_log(action), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log action
def gm_f88_biotech_f88_dividend_payout_history_log_21d_slope_v017_signal(action):
    base = _mean(_log(action), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log action
def gm_f88_biotech_f88_dividend_payout_history_log_21d_slope_v018_signal(action):
    base = _mean(_log(action), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log action
def gm_f88_biotech_f88_dividend_payout_history_log_63d_slope_v019_signal(action):
    base = _mean(_log(action), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log action
def gm_f88_biotech_f88_dividend_payout_history_log_63d_slope_v020_signal(action):
    base = _mean(_log(action), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log action
def gm_f88_biotech_f88_dividend_payout_history_log_63d_slope_v021_signal(action):
    base = _mean(_log(action), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log action
def gm_f88_biotech_f88_dividend_payout_history_log_126d_slope_v022_signal(action):
    base = _mean(_log(action), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log action
def gm_f88_biotech_f88_dividend_payout_history_log_126d_slope_v023_signal(action):
    base = _mean(_log(action), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log action
def gm_f88_biotech_f88_dividend_payout_history_log_126d_slope_v024_signal(action):
    base = _mean(_log(action), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log action
def gm_f88_biotech_f88_dividend_payout_history_log_252d_slope_v025_signal(action):
    base = _mean(_log(action), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log action
def gm_f88_biotech_f88_dividend_payout_history_log_252d_slope_v026_signal(action):
    base = _mean(_log(action), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log action
def gm_f88_biotech_f88_dividend_payout_history_log_252d_slope_v027_signal(action):
    base = _mean(_log(action), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log action
def gm_f88_biotech_f88_dividend_payout_history_log_504d_slope_v028_signal(action):
    base = _mean(_log(action), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log action
def gm_f88_biotech_f88_dividend_payout_history_log_504d_slope_v029_signal(action):
    base = _mean(_log(action), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log action
def gm_f88_biotech_f88_dividend_payout_history_log_504d_slope_v030_signal(action):
    base = _mean(_log(action), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z action
def gm_f88_biotech_f88_dividend_payout_history_z_21d_slope_v031_signal(action):
    base = _z(action, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z action
def gm_f88_biotech_f88_dividend_payout_history_z_21d_slope_v032_signal(action):
    base = _z(action, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z action
def gm_f88_biotech_f88_dividend_payout_history_z_21d_slope_v033_signal(action):
    base = _z(action, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z action
def gm_f88_biotech_f88_dividend_payout_history_z_63d_slope_v034_signal(action):
    base = _z(action, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z action
def gm_f88_biotech_f88_dividend_payout_history_z_63d_slope_v035_signal(action):
    base = _z(action, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z action
def gm_f88_biotech_f88_dividend_payout_history_z_63d_slope_v036_signal(action):
    base = _z(action, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z action
def gm_f88_biotech_f88_dividend_payout_history_z_126d_slope_v037_signal(action):
    base = _z(action, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z action
def gm_f88_biotech_f88_dividend_payout_history_z_126d_slope_v038_signal(action):
    base = _z(action, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z action
def gm_f88_biotech_f88_dividend_payout_history_z_126d_slope_v039_signal(action):
    base = _z(action, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z action
def gm_f88_biotech_f88_dividend_payout_history_z_252d_slope_v040_signal(action):
    base = _z(action, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z action
def gm_f88_biotech_f88_dividend_payout_history_z_252d_slope_v041_signal(action):
    base = _z(action, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z action
def gm_f88_biotech_f88_dividend_payout_history_z_252d_slope_v042_signal(action):
    base = _z(action, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z action
def gm_f88_biotech_f88_dividend_payout_history_z_504d_slope_v043_signal(action):
    base = _z(action, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z action
def gm_f88_biotech_f88_dividend_payout_history_z_504d_slope_v044_signal(action):
    base = _z(action, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z action
def gm_f88_biotech_f88_dividend_payout_history_z_504d_slope_v045_signal(action):
    base = _z(action, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps action
def gm_f88_biotech_f88_dividend_payout_history_ps_21d_slope_v046_signal(action, sharesbas):
    base = _safe_div(_mean(action, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps action
def gm_f88_biotech_f88_dividend_payout_history_ps_21d_slope_v047_signal(action, sharesbas):
    base = _safe_div(_mean(action, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps action
def gm_f88_biotech_f88_dividend_payout_history_ps_21d_slope_v048_signal(action, sharesbas):
    base = _safe_div(_mean(action, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps action
def gm_f88_biotech_f88_dividend_payout_history_ps_63d_slope_v049_signal(action, sharesbas):
    base = _safe_div(_mean(action, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps action
def gm_f88_biotech_f88_dividend_payout_history_ps_63d_slope_v050_signal(action, sharesbas):
    base = _safe_div(_mean(action, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps action
def gm_f88_biotech_f88_dividend_payout_history_ps_63d_slope_v051_signal(action, sharesbas):
    base = _safe_div(_mean(action, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps action
def gm_f88_biotech_f88_dividend_payout_history_ps_126d_slope_v052_signal(action, sharesbas):
    base = _safe_div(_mean(action, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps action
def gm_f88_biotech_f88_dividend_payout_history_ps_126d_slope_v053_signal(action, sharesbas):
    base = _safe_div(_mean(action, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps action
def gm_f88_biotech_f88_dividend_payout_history_ps_126d_slope_v054_signal(action, sharesbas):
    base = _safe_div(_mean(action, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps action
def gm_f88_biotech_f88_dividend_payout_history_ps_252d_slope_v055_signal(action, sharesbas):
    base = _safe_div(_mean(action, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps action
def gm_f88_biotech_f88_dividend_payout_history_ps_252d_slope_v056_signal(action, sharesbas):
    base = _safe_div(_mean(action, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps action
def gm_f88_biotech_f88_dividend_payout_history_ps_252d_slope_v057_signal(action, sharesbas):
    base = _safe_div(_mean(action, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps action
def gm_f88_biotech_f88_dividend_payout_history_ps_504d_slope_v058_signal(action, sharesbas):
    base = _safe_div(_mean(action, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps action
def gm_f88_biotech_f88_dividend_payout_history_ps_504d_slope_v059_signal(action, sharesbas):
    base = _safe_div(_mean(action, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps action
def gm_f88_biotech_f88_dividend_payout_history_ps_504d_slope_v060_signal(action, sharesbas):
    base = _safe_div(_mean(action, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled action
def gm_f88_biotech_f88_dividend_payout_history_asset_scaled_21d_slope_v061_signal(action, assets):
    base = _safe_div(_mean(action, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled action
def gm_f88_biotech_f88_dividend_payout_history_asset_scaled_21d_slope_v062_signal(action, assets):
    base = _safe_div(_mean(action, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled action
def gm_f88_biotech_f88_dividend_payout_history_asset_scaled_21d_slope_v063_signal(action, assets):
    base = _safe_div(_mean(action, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled action
def gm_f88_biotech_f88_dividend_payout_history_asset_scaled_63d_slope_v064_signal(action, assets):
    base = _safe_div(_mean(action, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled action
def gm_f88_biotech_f88_dividend_payout_history_asset_scaled_63d_slope_v065_signal(action, assets):
    base = _safe_div(_mean(action, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled action
def gm_f88_biotech_f88_dividend_payout_history_asset_scaled_63d_slope_v066_signal(action, assets):
    base = _safe_div(_mean(action, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled action
def gm_f88_biotech_f88_dividend_payout_history_asset_scaled_126d_slope_v067_signal(action, assets):
    base = _safe_div(_mean(action, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled action
def gm_f88_biotech_f88_dividend_payout_history_asset_scaled_126d_slope_v068_signal(action, assets):
    base = _safe_div(_mean(action, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled action
def gm_f88_biotech_f88_dividend_payout_history_asset_scaled_126d_slope_v069_signal(action, assets):
    base = _safe_div(_mean(action, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled action
def gm_f88_biotech_f88_dividend_payout_history_asset_scaled_252d_slope_v070_signal(action, assets):
    base = _safe_div(_mean(action, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled action
def gm_f88_biotech_f88_dividend_payout_history_asset_scaled_252d_slope_v071_signal(action, assets):
    base = _safe_div(_mean(action, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled action
def gm_f88_biotech_f88_dividend_payout_history_asset_scaled_252d_slope_v072_signal(action, assets):
    base = _safe_div(_mean(action, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled action
def gm_f88_biotech_f88_dividend_payout_history_asset_scaled_504d_slope_v073_signal(action, assets):
    base = _safe_div(_mean(action, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled action
def gm_f88_biotech_f88_dividend_payout_history_asset_scaled_504d_slope_v074_signal(action, assets):
    base = _safe_div(_mean(action, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled action
def gm_f88_biotech_f88_dividend_payout_history_asset_scaled_504d_slope_v075_signal(action, assets):
    base = _safe_div(_mean(action, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled action
def gm_f88_biotech_f88_dividend_payout_history_mcap_scaled_21d_slope_v076_signal(action, marketcap):
    base = _safe_div(_mean(action, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled action
def gm_f88_biotech_f88_dividend_payout_history_mcap_scaled_21d_slope_v077_signal(action, marketcap):
    base = _safe_div(_mean(action, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled action
def gm_f88_biotech_f88_dividend_payout_history_mcap_scaled_21d_slope_v078_signal(action, marketcap):
    base = _safe_div(_mean(action, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled action
def gm_f88_biotech_f88_dividend_payout_history_mcap_scaled_63d_slope_v079_signal(action, marketcap):
    base = _safe_div(_mean(action, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled action
def gm_f88_biotech_f88_dividend_payout_history_mcap_scaled_63d_slope_v080_signal(action, marketcap):
    base = _safe_div(_mean(action, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled action
def gm_f88_biotech_f88_dividend_payout_history_mcap_scaled_63d_slope_v081_signal(action, marketcap):
    base = _safe_div(_mean(action, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled action
def gm_f88_biotech_f88_dividend_payout_history_mcap_scaled_126d_slope_v082_signal(action, marketcap):
    base = _safe_div(_mean(action, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled action
def gm_f88_biotech_f88_dividend_payout_history_mcap_scaled_126d_slope_v083_signal(action, marketcap):
    base = _safe_div(_mean(action, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled action
def gm_f88_biotech_f88_dividend_payout_history_mcap_scaled_126d_slope_v084_signal(action, marketcap):
    base = _safe_div(_mean(action, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled action
def gm_f88_biotech_f88_dividend_payout_history_mcap_scaled_252d_slope_v085_signal(action, marketcap):
    base = _safe_div(_mean(action, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled action
def gm_f88_biotech_f88_dividend_payout_history_mcap_scaled_252d_slope_v086_signal(action, marketcap):
    base = _safe_div(_mean(action, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled action
def gm_f88_biotech_f88_dividend_payout_history_mcap_scaled_252d_slope_v087_signal(action, marketcap):
    base = _safe_div(_mean(action, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled action
def gm_f88_biotech_f88_dividend_payout_history_mcap_scaled_504d_slope_v088_signal(action, marketcap):
    base = _safe_div(_mean(action, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled action
def gm_f88_biotech_f88_dividend_payout_history_mcap_scaled_504d_slope_v089_signal(action, marketcap):
    base = _safe_div(_mean(action, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled action
def gm_f88_biotech_f88_dividend_payout_history_mcap_scaled_504d_slope_v090_signal(action, marketcap):
    base = _safe_div(_mean(action, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low action
def gm_f88_biotech_f88_dividend_payout_history_dist_low_21d_slope_v091_signal(action):
    base = _safe_div(action - action.rolling(21).min(), action.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low action
def gm_f88_biotech_f88_dividend_payout_history_dist_low_21d_slope_v092_signal(action):
    base = _safe_div(action - action.rolling(21).min(), action.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low action
def gm_f88_biotech_f88_dividend_payout_history_dist_low_21d_slope_v093_signal(action):
    base = _safe_div(action - action.rolling(21).min(), action.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low action
def gm_f88_biotech_f88_dividend_payout_history_dist_low_63d_slope_v094_signal(action):
    base = _safe_div(action - action.rolling(63).min(), action.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low action
def gm_f88_biotech_f88_dividend_payout_history_dist_low_63d_slope_v095_signal(action):
    base = _safe_div(action - action.rolling(63).min(), action.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low action
def gm_f88_biotech_f88_dividend_payout_history_dist_low_63d_slope_v096_signal(action):
    base = _safe_div(action - action.rolling(63).min(), action.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low action
def gm_f88_biotech_f88_dividend_payout_history_dist_low_126d_slope_v097_signal(action):
    base = _safe_div(action - action.rolling(126).min(), action.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low action
def gm_f88_biotech_f88_dividend_payout_history_dist_low_126d_slope_v098_signal(action):
    base = _safe_div(action - action.rolling(126).min(), action.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low action
def gm_f88_biotech_f88_dividend_payout_history_dist_low_126d_slope_v099_signal(action):
    base = _safe_div(action - action.rolling(126).min(), action.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low action
def gm_f88_biotech_f88_dividend_payout_history_dist_low_252d_slope_v100_signal(action):
    base = _safe_div(action - action.rolling(252).min(), action.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low action
def gm_f88_biotech_f88_dividend_payout_history_dist_low_252d_slope_v101_signal(action):
    base = _safe_div(action - action.rolling(252).min(), action.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low action
def gm_f88_biotech_f88_dividend_payout_history_dist_low_252d_slope_v102_signal(action):
    base = _safe_div(action - action.rolling(252).min(), action.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low action
def gm_f88_biotech_f88_dividend_payout_history_dist_low_504d_slope_v103_signal(action):
    base = _safe_div(action - action.rolling(504).min(), action.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low action
def gm_f88_biotech_f88_dividend_payout_history_dist_low_504d_slope_v104_signal(action):
    base = _safe_div(action - action.rolling(504).min(), action.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low action
def gm_f88_biotech_f88_dividend_payout_history_dist_low_504d_slope_v105_signal(action):
    base = _safe_div(action - action.rolling(504).min(), action.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high action
def gm_f88_biotech_f88_dividend_payout_history_dist_high_21d_slope_v106_signal(action):
    base = _safe_div(action.rolling(21).max() - action, action.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high action
def gm_f88_biotech_f88_dividend_payout_history_dist_high_21d_slope_v107_signal(action):
    base = _safe_div(action.rolling(21).max() - action, action.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high action
def gm_f88_biotech_f88_dividend_payout_history_dist_high_21d_slope_v108_signal(action):
    base = _safe_div(action.rolling(21).max() - action, action.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high action
def gm_f88_biotech_f88_dividend_payout_history_dist_high_63d_slope_v109_signal(action):
    base = _safe_div(action.rolling(63).max() - action, action.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high action
def gm_f88_biotech_f88_dividend_payout_history_dist_high_63d_slope_v110_signal(action):
    base = _safe_div(action.rolling(63).max() - action, action.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high action
def gm_f88_biotech_f88_dividend_payout_history_dist_high_63d_slope_v111_signal(action):
    base = _safe_div(action.rolling(63).max() - action, action.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high action
def gm_f88_biotech_f88_dividend_payout_history_dist_high_126d_slope_v112_signal(action):
    base = _safe_div(action.rolling(126).max() - action, action.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high action
def gm_f88_biotech_f88_dividend_payout_history_dist_high_126d_slope_v113_signal(action):
    base = _safe_div(action.rolling(126).max() - action, action.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high action
def gm_f88_biotech_f88_dividend_payout_history_dist_high_126d_slope_v114_signal(action):
    base = _safe_div(action.rolling(126).max() - action, action.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high action
def gm_f88_biotech_f88_dividend_payout_history_dist_high_252d_slope_v115_signal(action):
    base = _safe_div(action.rolling(252).max() - action, action.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high action
def gm_f88_biotech_f88_dividend_payout_history_dist_high_252d_slope_v116_signal(action):
    base = _safe_div(action.rolling(252).max() - action, action.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high action
def gm_f88_biotech_f88_dividend_payout_history_dist_high_252d_slope_v117_signal(action):
    base = _safe_div(action.rolling(252).max() - action, action.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high action
def gm_f88_biotech_f88_dividend_payout_history_dist_high_504d_slope_v118_signal(action):
    base = _safe_div(action.rolling(504).max() - action, action.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high action
def gm_f88_biotech_f88_dividend_payout_history_dist_high_504d_slope_v119_signal(action):
    base = _safe_div(action.rolling(504).max() - action, action.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high action
def gm_f88_biotech_f88_dividend_payout_history_dist_high_504d_slope_v120_signal(action):
    base = _safe_div(action.rolling(504).max() - action, action.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom action
def gm_f88_biotech_f88_dividend_payout_history_mom_21d_slope_v121_signal(action):
    base = _safe_div(_mean(action, 21) - _mean(action, 42), _mean(action, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom action
def gm_f88_biotech_f88_dividend_payout_history_mom_21d_slope_v122_signal(action):
    base = _safe_div(_mean(action, 21) - _mean(action, 42), _mean(action, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom action
def gm_f88_biotech_f88_dividend_payout_history_mom_21d_slope_v123_signal(action):
    base = _safe_div(_mean(action, 21) - _mean(action, 42), _mean(action, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom action
def gm_f88_biotech_f88_dividend_payout_history_mom_63d_slope_v124_signal(action):
    base = _safe_div(_mean(action, 63) - _mean(action, 126), _mean(action, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom action
def gm_f88_biotech_f88_dividend_payout_history_mom_63d_slope_v125_signal(action):
    base = _safe_div(_mean(action, 63) - _mean(action, 126), _mean(action, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom action
def gm_f88_biotech_f88_dividend_payout_history_mom_63d_slope_v126_signal(action):
    base = _safe_div(_mean(action, 63) - _mean(action, 126), _mean(action, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom action
def gm_f88_biotech_f88_dividend_payout_history_mom_126d_slope_v127_signal(action):
    base = _safe_div(_mean(action, 126) - _mean(action, 252), _mean(action, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom action
def gm_f88_biotech_f88_dividend_payout_history_mom_126d_slope_v128_signal(action):
    base = _safe_div(_mean(action, 126) - _mean(action, 252), _mean(action, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom action
def gm_f88_biotech_f88_dividend_payout_history_mom_126d_slope_v129_signal(action):
    base = _safe_div(_mean(action, 126) - _mean(action, 252), _mean(action, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom action
def gm_f88_biotech_f88_dividend_payout_history_mom_252d_slope_v130_signal(action):
    base = _safe_div(_mean(action, 252) - _mean(action, 504), _mean(action, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom action
def gm_f88_biotech_f88_dividend_payout_history_mom_252d_slope_v131_signal(action):
    base = _safe_div(_mean(action, 252) - _mean(action, 504), _mean(action, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom action
def gm_f88_biotech_f88_dividend_payout_history_mom_252d_slope_v132_signal(action):
    base = _safe_div(_mean(action, 252) - _mean(action, 504), _mean(action, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom action
def gm_f88_biotech_f88_dividend_payout_history_mom_504d_slope_v133_signal(action):
    base = _safe_div(_mean(action, 504) - _mean(action, 1008), _mean(action, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom action
def gm_f88_biotech_f88_dividend_payout_history_mom_504d_slope_v134_signal(action):
    base = _safe_div(_mean(action, 504) - _mean(action, 1008), _mean(action, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom action
def gm_f88_biotech_f88_dividend_payout_history_mom_504d_slope_v135_signal(action):
    base = _safe_div(_mean(action, 504) - _mean(action, 1008), _mean(action, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol action
def gm_f88_biotech_f88_dividend_payout_history_vol_21d_slope_v136_signal(action):
    base = _std(action, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol action
def gm_f88_biotech_f88_dividend_payout_history_vol_21d_slope_v137_signal(action):
    base = _std(action, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol action
def gm_f88_biotech_f88_dividend_payout_history_vol_21d_slope_v138_signal(action):
    base = _std(action, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol action
def gm_f88_biotech_f88_dividend_payout_history_vol_63d_slope_v139_signal(action):
    base = _std(action, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol action
def gm_f88_biotech_f88_dividend_payout_history_vol_63d_slope_v140_signal(action):
    base = _std(action, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol action
def gm_f88_biotech_f88_dividend_payout_history_vol_63d_slope_v141_signal(action):
    base = _std(action, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol action
def gm_f88_biotech_f88_dividend_payout_history_vol_126d_slope_v142_signal(action):
    base = _std(action, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol action
def gm_f88_biotech_f88_dividend_payout_history_vol_126d_slope_v143_signal(action):
    base = _std(action, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol action
def gm_f88_biotech_f88_dividend_payout_history_vol_126d_slope_v144_signal(action):
    base = _std(action, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol action
def gm_f88_biotech_f88_dividend_payout_history_vol_252d_slope_v145_signal(action):
    base = _std(action, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol action
def gm_f88_biotech_f88_dividend_payout_history_vol_252d_slope_v146_signal(action):
    base = _std(action, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol action
def gm_f88_biotech_f88_dividend_payout_history_vol_252d_slope_v147_signal(action):
    base = _std(action, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol action
def gm_f88_biotech_f88_dividend_payout_history_vol_504d_slope_v148_signal(action):
    base = _std(action, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol action
def gm_f88_biotech_f88_dividend_payout_history_vol_504d_slope_v149_signal(action):
    base = _std(action, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol action
def gm_f88_biotech_f88_dividend_payout_history_vol_504d_slope_v150_signal(action):
    base = _std(action, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

