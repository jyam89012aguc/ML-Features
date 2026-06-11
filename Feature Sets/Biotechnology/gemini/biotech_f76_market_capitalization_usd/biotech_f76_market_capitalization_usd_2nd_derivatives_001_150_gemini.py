
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_21d_slope_v001_signal(marketcap):
    base = _mean(marketcap, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_21d_slope_v002_signal(marketcap):
    base = _mean(marketcap, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_21d_slope_v003_signal(marketcap):
    base = _mean(marketcap, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_63d_slope_v004_signal(marketcap):
    base = _mean(marketcap, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_63d_slope_v005_signal(marketcap):
    base = _mean(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_63d_slope_v006_signal(marketcap):
    base = _mean(marketcap, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_126d_slope_v007_signal(marketcap):
    base = _mean(marketcap, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_126d_slope_v008_signal(marketcap):
    base = _mean(marketcap, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_126d_slope_v009_signal(marketcap):
    base = _mean(marketcap, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_252d_slope_v010_signal(marketcap):
    base = _mean(marketcap, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_252d_slope_v011_signal(marketcap):
    base = _mean(marketcap, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_252d_slope_v012_signal(marketcap):
    base = _mean(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_504d_slope_v013_signal(marketcap):
    base = _mean(marketcap, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_504d_slope_v014_signal(marketcap):
    base = _mean(marketcap, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw marketcap
def gm_f76_biotech_f76_market_capitalization_usd_raw_504d_slope_v015_signal(marketcap):
    base = _mean(marketcap, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_21d_slope_v016_signal(marketcap):
    base = _mean(_log(marketcap), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_21d_slope_v017_signal(marketcap):
    base = _mean(_log(marketcap), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_21d_slope_v018_signal(marketcap):
    base = _mean(_log(marketcap), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_63d_slope_v019_signal(marketcap):
    base = _mean(_log(marketcap), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_63d_slope_v020_signal(marketcap):
    base = _mean(_log(marketcap), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_63d_slope_v021_signal(marketcap):
    base = _mean(_log(marketcap), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_126d_slope_v022_signal(marketcap):
    base = _mean(_log(marketcap), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_126d_slope_v023_signal(marketcap):
    base = _mean(_log(marketcap), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_126d_slope_v024_signal(marketcap):
    base = _mean(_log(marketcap), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_252d_slope_v025_signal(marketcap):
    base = _mean(_log(marketcap), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_252d_slope_v026_signal(marketcap):
    base = _mean(_log(marketcap), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_252d_slope_v027_signal(marketcap):
    base = _mean(_log(marketcap), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_504d_slope_v028_signal(marketcap):
    base = _mean(_log(marketcap), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_504d_slope_v029_signal(marketcap):
    base = _mean(_log(marketcap), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log marketcap
def gm_f76_biotech_f76_market_capitalization_usd_log_504d_slope_v030_signal(marketcap):
    base = _mean(_log(marketcap), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_21d_slope_v031_signal(marketcap):
    base = _z(marketcap, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_21d_slope_v032_signal(marketcap):
    base = _z(marketcap, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_21d_slope_v033_signal(marketcap):
    base = _z(marketcap, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_63d_slope_v034_signal(marketcap):
    base = _z(marketcap, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_63d_slope_v035_signal(marketcap):
    base = _z(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_63d_slope_v036_signal(marketcap):
    base = _z(marketcap, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_126d_slope_v037_signal(marketcap):
    base = _z(marketcap, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_126d_slope_v038_signal(marketcap):
    base = _z(marketcap, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_126d_slope_v039_signal(marketcap):
    base = _z(marketcap, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_252d_slope_v040_signal(marketcap):
    base = _z(marketcap, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_252d_slope_v041_signal(marketcap):
    base = _z(marketcap, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_252d_slope_v042_signal(marketcap):
    base = _z(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_504d_slope_v043_signal(marketcap):
    base = _z(marketcap, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_504d_slope_v044_signal(marketcap):
    base = _z(marketcap, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z marketcap
def gm_f76_biotech_f76_market_capitalization_usd_z_504d_slope_v045_signal(marketcap):
    base = _z(marketcap, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_21d_slope_v046_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_21d_slope_v047_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_21d_slope_v048_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_63d_slope_v049_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_63d_slope_v050_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_63d_slope_v051_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_126d_slope_v052_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_126d_slope_v053_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_126d_slope_v054_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_252d_slope_v055_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_252d_slope_v056_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_252d_slope_v057_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_504d_slope_v058_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_504d_slope_v059_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps marketcap
def gm_f76_biotech_f76_market_capitalization_usd_ps_504d_slope_v060_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_21d_slope_v061_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_21d_slope_v062_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_21d_slope_v063_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_63d_slope_v064_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_63d_slope_v065_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_63d_slope_v066_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_126d_slope_v067_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_126d_slope_v068_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_126d_slope_v069_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_252d_slope_v070_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_252d_slope_v071_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_252d_slope_v072_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_504d_slope_v073_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_504d_slope_v074_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_asset_scaled_504d_slope_v075_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_21d_slope_v076_signal(marketcap):
    base = _safe_div(_mean(marketcap, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_21d_slope_v077_signal(marketcap):
    base = _safe_div(_mean(marketcap, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_21d_slope_v078_signal(marketcap):
    base = _safe_div(_mean(marketcap, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_63d_slope_v079_signal(marketcap):
    base = _safe_div(_mean(marketcap, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_63d_slope_v080_signal(marketcap):
    base = _safe_div(_mean(marketcap, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_63d_slope_v081_signal(marketcap):
    base = _safe_div(_mean(marketcap, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_126d_slope_v082_signal(marketcap):
    base = _safe_div(_mean(marketcap, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_126d_slope_v083_signal(marketcap):
    base = _safe_div(_mean(marketcap, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_126d_slope_v084_signal(marketcap):
    base = _safe_div(_mean(marketcap, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_252d_slope_v085_signal(marketcap):
    base = _safe_div(_mean(marketcap, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_252d_slope_v086_signal(marketcap):
    base = _safe_div(_mean(marketcap, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_252d_slope_v087_signal(marketcap):
    base = _safe_div(_mean(marketcap, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_504d_slope_v088_signal(marketcap):
    base = _safe_div(_mean(marketcap, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_504d_slope_v089_signal(marketcap):
    base = _safe_div(_mean(marketcap, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mcap_scaled_504d_slope_v090_signal(marketcap):
    base = _safe_div(_mean(marketcap, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_21d_slope_v091_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(21).min(), marketcap.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_21d_slope_v092_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(21).min(), marketcap.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_21d_slope_v093_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(21).min(), marketcap.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_63d_slope_v094_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(63).min(), marketcap.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_63d_slope_v095_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(63).min(), marketcap.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_63d_slope_v096_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(63).min(), marketcap.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_126d_slope_v097_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(126).min(), marketcap.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_126d_slope_v098_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(126).min(), marketcap.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_126d_slope_v099_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(126).min(), marketcap.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_252d_slope_v100_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(252).min(), marketcap.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_252d_slope_v101_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(252).min(), marketcap.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_252d_slope_v102_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(252).min(), marketcap.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_504d_slope_v103_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(504).min(), marketcap.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_504d_slope_v104_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(504).min(), marketcap.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_low_504d_slope_v105_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(504).min(), marketcap.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_21d_slope_v106_signal(marketcap):
    base = _safe_div(marketcap.rolling(21).max() - marketcap, marketcap.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_21d_slope_v107_signal(marketcap):
    base = _safe_div(marketcap.rolling(21).max() - marketcap, marketcap.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_21d_slope_v108_signal(marketcap):
    base = _safe_div(marketcap.rolling(21).max() - marketcap, marketcap.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_63d_slope_v109_signal(marketcap):
    base = _safe_div(marketcap.rolling(63).max() - marketcap, marketcap.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_63d_slope_v110_signal(marketcap):
    base = _safe_div(marketcap.rolling(63).max() - marketcap, marketcap.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_63d_slope_v111_signal(marketcap):
    base = _safe_div(marketcap.rolling(63).max() - marketcap, marketcap.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_126d_slope_v112_signal(marketcap):
    base = _safe_div(marketcap.rolling(126).max() - marketcap, marketcap.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_126d_slope_v113_signal(marketcap):
    base = _safe_div(marketcap.rolling(126).max() - marketcap, marketcap.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_126d_slope_v114_signal(marketcap):
    base = _safe_div(marketcap.rolling(126).max() - marketcap, marketcap.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_252d_slope_v115_signal(marketcap):
    base = _safe_div(marketcap.rolling(252).max() - marketcap, marketcap.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_252d_slope_v116_signal(marketcap):
    base = _safe_div(marketcap.rolling(252).max() - marketcap, marketcap.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_252d_slope_v117_signal(marketcap):
    base = _safe_div(marketcap.rolling(252).max() - marketcap, marketcap.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_504d_slope_v118_signal(marketcap):
    base = _safe_div(marketcap.rolling(504).max() - marketcap, marketcap.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_504d_slope_v119_signal(marketcap):
    base = _safe_div(marketcap.rolling(504).max() - marketcap, marketcap.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high marketcap
def gm_f76_biotech_f76_market_capitalization_usd_dist_high_504d_slope_v120_signal(marketcap):
    base = _safe_div(marketcap.rolling(504).max() - marketcap, marketcap.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_21d_slope_v121_signal(marketcap):
    base = _safe_div(_mean(marketcap, 21) - _mean(marketcap, 42), _mean(marketcap, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_21d_slope_v122_signal(marketcap):
    base = _safe_div(_mean(marketcap, 21) - _mean(marketcap, 42), _mean(marketcap, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_21d_slope_v123_signal(marketcap):
    base = _safe_div(_mean(marketcap, 21) - _mean(marketcap, 42), _mean(marketcap, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_63d_slope_v124_signal(marketcap):
    base = _safe_div(_mean(marketcap, 63) - _mean(marketcap, 126), _mean(marketcap, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_63d_slope_v125_signal(marketcap):
    base = _safe_div(_mean(marketcap, 63) - _mean(marketcap, 126), _mean(marketcap, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_63d_slope_v126_signal(marketcap):
    base = _safe_div(_mean(marketcap, 63) - _mean(marketcap, 126), _mean(marketcap, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_126d_slope_v127_signal(marketcap):
    base = _safe_div(_mean(marketcap, 126) - _mean(marketcap, 252), _mean(marketcap, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_126d_slope_v128_signal(marketcap):
    base = _safe_div(_mean(marketcap, 126) - _mean(marketcap, 252), _mean(marketcap, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_126d_slope_v129_signal(marketcap):
    base = _safe_div(_mean(marketcap, 126) - _mean(marketcap, 252), _mean(marketcap, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_252d_slope_v130_signal(marketcap):
    base = _safe_div(_mean(marketcap, 252) - _mean(marketcap, 504), _mean(marketcap, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_252d_slope_v131_signal(marketcap):
    base = _safe_div(_mean(marketcap, 252) - _mean(marketcap, 504), _mean(marketcap, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_252d_slope_v132_signal(marketcap):
    base = _safe_div(_mean(marketcap, 252) - _mean(marketcap, 504), _mean(marketcap, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_504d_slope_v133_signal(marketcap):
    base = _safe_div(_mean(marketcap, 504) - _mean(marketcap, 1008), _mean(marketcap, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_504d_slope_v134_signal(marketcap):
    base = _safe_div(_mean(marketcap, 504) - _mean(marketcap, 1008), _mean(marketcap, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom marketcap
def gm_f76_biotech_f76_market_capitalization_usd_mom_504d_slope_v135_signal(marketcap):
    base = _safe_div(_mean(marketcap, 504) - _mean(marketcap, 1008), _mean(marketcap, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol marketcap
def gm_f76_biotech_f76_market_capitalization_usd_vol_21d_slope_v136_signal(marketcap):
    base = _std(marketcap, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol marketcap
def gm_f76_biotech_f76_market_capitalization_usd_vol_21d_slope_v137_signal(marketcap):
    base = _std(marketcap, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol marketcap
def gm_f76_biotech_f76_market_capitalization_usd_vol_21d_slope_v138_signal(marketcap):
    base = _std(marketcap, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol marketcap
def gm_f76_biotech_f76_market_capitalization_usd_vol_63d_slope_v139_signal(marketcap):
    base = _std(marketcap, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol marketcap
def gm_f76_biotech_f76_market_capitalization_usd_vol_63d_slope_v140_signal(marketcap):
    base = _std(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol marketcap
def gm_f76_biotech_f76_market_capitalization_usd_vol_63d_slope_v141_signal(marketcap):
    base = _std(marketcap, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol marketcap
def gm_f76_biotech_f76_market_capitalization_usd_vol_126d_slope_v142_signal(marketcap):
    base = _std(marketcap, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol marketcap
def gm_f76_biotech_f76_market_capitalization_usd_vol_126d_slope_v143_signal(marketcap):
    base = _std(marketcap, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol marketcap
def gm_f76_biotech_f76_market_capitalization_usd_vol_126d_slope_v144_signal(marketcap):
    base = _std(marketcap, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol marketcap
def gm_f76_biotech_f76_market_capitalization_usd_vol_252d_slope_v145_signal(marketcap):
    base = _std(marketcap, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol marketcap
def gm_f76_biotech_f76_market_capitalization_usd_vol_252d_slope_v146_signal(marketcap):
    base = _std(marketcap, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol marketcap
def gm_f76_biotech_f76_market_capitalization_usd_vol_252d_slope_v147_signal(marketcap):
    base = _std(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol marketcap
def gm_f76_biotech_f76_market_capitalization_usd_vol_504d_slope_v148_signal(marketcap):
    base = _std(marketcap, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol marketcap
def gm_f76_biotech_f76_market_capitalization_usd_vol_504d_slope_v149_signal(marketcap):
    base = _std(marketcap, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol marketcap
def gm_f76_biotech_f76_market_capitalization_usd_vol_504d_slope_v150_signal(marketcap):
    base = _std(marketcap, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

