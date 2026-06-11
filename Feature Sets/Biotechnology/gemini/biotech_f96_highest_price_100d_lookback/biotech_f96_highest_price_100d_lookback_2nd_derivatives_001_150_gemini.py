
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw close
def gm_f96_biotech_f96_highest_price_100d_lookback_raw_21d_slope_v001_signal(close):
    base = _mean(close, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw close
def gm_f96_biotech_f96_highest_price_100d_lookback_raw_21d_slope_v002_signal(close):
    base = _mean(close, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw close
def gm_f96_biotech_f96_highest_price_100d_lookback_raw_21d_slope_v003_signal(close):
    base = _mean(close, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw close
def gm_f96_biotech_f96_highest_price_100d_lookback_raw_63d_slope_v004_signal(close):
    base = _mean(close, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw close
def gm_f96_biotech_f96_highest_price_100d_lookback_raw_63d_slope_v005_signal(close):
    base = _mean(close, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw close
def gm_f96_biotech_f96_highest_price_100d_lookback_raw_63d_slope_v006_signal(close):
    base = _mean(close, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw close
def gm_f96_biotech_f96_highest_price_100d_lookback_raw_126d_slope_v007_signal(close):
    base = _mean(close, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw close
def gm_f96_biotech_f96_highest_price_100d_lookback_raw_126d_slope_v008_signal(close):
    base = _mean(close, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw close
def gm_f96_biotech_f96_highest_price_100d_lookback_raw_126d_slope_v009_signal(close):
    base = _mean(close, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw close
def gm_f96_biotech_f96_highest_price_100d_lookback_raw_252d_slope_v010_signal(close):
    base = _mean(close, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw close
def gm_f96_biotech_f96_highest_price_100d_lookback_raw_252d_slope_v011_signal(close):
    base = _mean(close, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw close
def gm_f96_biotech_f96_highest_price_100d_lookback_raw_252d_slope_v012_signal(close):
    base = _mean(close, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw close
def gm_f96_biotech_f96_highest_price_100d_lookback_raw_504d_slope_v013_signal(close):
    base = _mean(close, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw close
def gm_f96_biotech_f96_highest_price_100d_lookback_raw_504d_slope_v014_signal(close):
    base = _mean(close, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw close
def gm_f96_biotech_f96_highest_price_100d_lookback_raw_504d_slope_v015_signal(close):
    base = _mean(close, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log close
def gm_f96_biotech_f96_highest_price_100d_lookback_log_21d_slope_v016_signal(close):
    base = _mean(_log(close), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log close
def gm_f96_biotech_f96_highest_price_100d_lookback_log_21d_slope_v017_signal(close):
    base = _mean(_log(close), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log close
def gm_f96_biotech_f96_highest_price_100d_lookback_log_21d_slope_v018_signal(close):
    base = _mean(_log(close), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log close
def gm_f96_biotech_f96_highest_price_100d_lookback_log_63d_slope_v019_signal(close):
    base = _mean(_log(close), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log close
def gm_f96_biotech_f96_highest_price_100d_lookback_log_63d_slope_v020_signal(close):
    base = _mean(_log(close), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log close
def gm_f96_biotech_f96_highest_price_100d_lookback_log_63d_slope_v021_signal(close):
    base = _mean(_log(close), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log close
def gm_f96_biotech_f96_highest_price_100d_lookback_log_126d_slope_v022_signal(close):
    base = _mean(_log(close), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log close
def gm_f96_biotech_f96_highest_price_100d_lookback_log_126d_slope_v023_signal(close):
    base = _mean(_log(close), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log close
def gm_f96_biotech_f96_highest_price_100d_lookback_log_126d_slope_v024_signal(close):
    base = _mean(_log(close), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log close
def gm_f96_biotech_f96_highest_price_100d_lookback_log_252d_slope_v025_signal(close):
    base = _mean(_log(close), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log close
def gm_f96_biotech_f96_highest_price_100d_lookback_log_252d_slope_v026_signal(close):
    base = _mean(_log(close), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log close
def gm_f96_biotech_f96_highest_price_100d_lookback_log_252d_slope_v027_signal(close):
    base = _mean(_log(close), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log close
def gm_f96_biotech_f96_highest_price_100d_lookback_log_504d_slope_v028_signal(close):
    base = _mean(_log(close), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log close
def gm_f96_biotech_f96_highest_price_100d_lookback_log_504d_slope_v029_signal(close):
    base = _mean(_log(close), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log close
def gm_f96_biotech_f96_highest_price_100d_lookback_log_504d_slope_v030_signal(close):
    base = _mean(_log(close), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z close
def gm_f96_biotech_f96_highest_price_100d_lookback_z_21d_slope_v031_signal(close):
    base = _z(close, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z close
def gm_f96_biotech_f96_highest_price_100d_lookback_z_21d_slope_v032_signal(close):
    base = _z(close, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z close
def gm_f96_biotech_f96_highest_price_100d_lookback_z_21d_slope_v033_signal(close):
    base = _z(close, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z close
def gm_f96_biotech_f96_highest_price_100d_lookback_z_63d_slope_v034_signal(close):
    base = _z(close, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z close
def gm_f96_biotech_f96_highest_price_100d_lookback_z_63d_slope_v035_signal(close):
    base = _z(close, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z close
def gm_f96_biotech_f96_highest_price_100d_lookback_z_63d_slope_v036_signal(close):
    base = _z(close, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z close
def gm_f96_biotech_f96_highest_price_100d_lookback_z_126d_slope_v037_signal(close):
    base = _z(close, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z close
def gm_f96_biotech_f96_highest_price_100d_lookback_z_126d_slope_v038_signal(close):
    base = _z(close, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z close
def gm_f96_biotech_f96_highest_price_100d_lookback_z_126d_slope_v039_signal(close):
    base = _z(close, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z close
def gm_f96_biotech_f96_highest_price_100d_lookback_z_252d_slope_v040_signal(close):
    base = _z(close, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z close
def gm_f96_biotech_f96_highest_price_100d_lookback_z_252d_slope_v041_signal(close):
    base = _z(close, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z close
def gm_f96_biotech_f96_highest_price_100d_lookback_z_252d_slope_v042_signal(close):
    base = _z(close, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z close
def gm_f96_biotech_f96_highest_price_100d_lookback_z_504d_slope_v043_signal(close):
    base = _z(close, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z close
def gm_f96_biotech_f96_highest_price_100d_lookback_z_504d_slope_v044_signal(close):
    base = _z(close, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z close
def gm_f96_biotech_f96_highest_price_100d_lookback_z_504d_slope_v045_signal(close):
    base = _z(close, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps close
def gm_f96_biotech_f96_highest_price_100d_lookback_ps_21d_slope_v046_signal(close, sharesbas):
    base = _safe_div(_mean(close, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps close
def gm_f96_biotech_f96_highest_price_100d_lookback_ps_21d_slope_v047_signal(close, sharesbas):
    base = _safe_div(_mean(close, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps close
def gm_f96_biotech_f96_highest_price_100d_lookback_ps_21d_slope_v048_signal(close, sharesbas):
    base = _safe_div(_mean(close, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps close
def gm_f96_biotech_f96_highest_price_100d_lookback_ps_63d_slope_v049_signal(close, sharesbas):
    base = _safe_div(_mean(close, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps close
def gm_f96_biotech_f96_highest_price_100d_lookback_ps_63d_slope_v050_signal(close, sharesbas):
    base = _safe_div(_mean(close, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps close
def gm_f96_biotech_f96_highest_price_100d_lookback_ps_63d_slope_v051_signal(close, sharesbas):
    base = _safe_div(_mean(close, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps close
def gm_f96_biotech_f96_highest_price_100d_lookback_ps_126d_slope_v052_signal(close, sharesbas):
    base = _safe_div(_mean(close, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps close
def gm_f96_biotech_f96_highest_price_100d_lookback_ps_126d_slope_v053_signal(close, sharesbas):
    base = _safe_div(_mean(close, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps close
def gm_f96_biotech_f96_highest_price_100d_lookback_ps_126d_slope_v054_signal(close, sharesbas):
    base = _safe_div(_mean(close, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps close
def gm_f96_biotech_f96_highest_price_100d_lookback_ps_252d_slope_v055_signal(close, sharesbas):
    base = _safe_div(_mean(close, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps close
def gm_f96_biotech_f96_highest_price_100d_lookback_ps_252d_slope_v056_signal(close, sharesbas):
    base = _safe_div(_mean(close, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps close
def gm_f96_biotech_f96_highest_price_100d_lookback_ps_252d_slope_v057_signal(close, sharesbas):
    base = _safe_div(_mean(close, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps close
def gm_f96_biotech_f96_highest_price_100d_lookback_ps_504d_slope_v058_signal(close, sharesbas):
    base = _safe_div(_mean(close, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps close
def gm_f96_biotech_f96_highest_price_100d_lookback_ps_504d_slope_v059_signal(close, sharesbas):
    base = _safe_div(_mean(close, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps close
def gm_f96_biotech_f96_highest_price_100d_lookback_ps_504d_slope_v060_signal(close, sharesbas):
    base = _safe_div(_mean(close, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_asset_scaled_21d_slope_v061_signal(close, assets):
    base = _safe_div(_mean(close, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_asset_scaled_21d_slope_v062_signal(close, assets):
    base = _safe_div(_mean(close, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_asset_scaled_21d_slope_v063_signal(close, assets):
    base = _safe_div(_mean(close, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_asset_scaled_63d_slope_v064_signal(close, assets):
    base = _safe_div(_mean(close, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_asset_scaled_63d_slope_v065_signal(close, assets):
    base = _safe_div(_mean(close, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_asset_scaled_63d_slope_v066_signal(close, assets):
    base = _safe_div(_mean(close, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_asset_scaled_126d_slope_v067_signal(close, assets):
    base = _safe_div(_mean(close, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_asset_scaled_126d_slope_v068_signal(close, assets):
    base = _safe_div(_mean(close, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_asset_scaled_126d_slope_v069_signal(close, assets):
    base = _safe_div(_mean(close, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_asset_scaled_252d_slope_v070_signal(close, assets):
    base = _safe_div(_mean(close, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_asset_scaled_252d_slope_v071_signal(close, assets):
    base = _safe_div(_mean(close, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_asset_scaled_252d_slope_v072_signal(close, assets):
    base = _safe_div(_mean(close, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_asset_scaled_504d_slope_v073_signal(close, assets):
    base = _safe_div(_mean(close, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_asset_scaled_504d_slope_v074_signal(close, assets):
    base = _safe_div(_mean(close, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_asset_scaled_504d_slope_v075_signal(close, assets):
    base = _safe_div(_mean(close, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_mcap_scaled_21d_slope_v076_signal(close, marketcap):
    base = _safe_div(_mean(close, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_mcap_scaled_21d_slope_v077_signal(close, marketcap):
    base = _safe_div(_mean(close, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_mcap_scaled_21d_slope_v078_signal(close, marketcap):
    base = _safe_div(_mean(close, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_mcap_scaled_63d_slope_v079_signal(close, marketcap):
    base = _safe_div(_mean(close, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_mcap_scaled_63d_slope_v080_signal(close, marketcap):
    base = _safe_div(_mean(close, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_mcap_scaled_63d_slope_v081_signal(close, marketcap):
    base = _safe_div(_mean(close, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_mcap_scaled_126d_slope_v082_signal(close, marketcap):
    base = _safe_div(_mean(close, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_mcap_scaled_126d_slope_v083_signal(close, marketcap):
    base = _safe_div(_mean(close, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_mcap_scaled_126d_slope_v084_signal(close, marketcap):
    base = _safe_div(_mean(close, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_mcap_scaled_252d_slope_v085_signal(close, marketcap):
    base = _safe_div(_mean(close, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_mcap_scaled_252d_slope_v086_signal(close, marketcap):
    base = _safe_div(_mean(close, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_mcap_scaled_252d_slope_v087_signal(close, marketcap):
    base = _safe_div(_mean(close, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_mcap_scaled_504d_slope_v088_signal(close, marketcap):
    base = _safe_div(_mean(close, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_mcap_scaled_504d_slope_v089_signal(close, marketcap):
    base = _safe_div(_mean(close, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled close
def gm_f96_biotech_f96_highest_price_100d_lookback_mcap_scaled_504d_slope_v090_signal(close, marketcap):
    base = _safe_div(_mean(close, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_low_21d_slope_v091_signal(close):
    base = _safe_div(close - close.rolling(21).min(), close.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_low_21d_slope_v092_signal(close):
    base = _safe_div(close - close.rolling(21).min(), close.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_low_21d_slope_v093_signal(close):
    base = _safe_div(close - close.rolling(21).min(), close.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_low_63d_slope_v094_signal(close):
    base = _safe_div(close - close.rolling(63).min(), close.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_low_63d_slope_v095_signal(close):
    base = _safe_div(close - close.rolling(63).min(), close.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_low_63d_slope_v096_signal(close):
    base = _safe_div(close - close.rolling(63).min(), close.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_low_126d_slope_v097_signal(close):
    base = _safe_div(close - close.rolling(126).min(), close.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_low_126d_slope_v098_signal(close):
    base = _safe_div(close - close.rolling(126).min(), close.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_low_126d_slope_v099_signal(close):
    base = _safe_div(close - close.rolling(126).min(), close.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_low_252d_slope_v100_signal(close):
    base = _safe_div(close - close.rolling(252).min(), close.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_low_252d_slope_v101_signal(close):
    base = _safe_div(close - close.rolling(252).min(), close.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_low_252d_slope_v102_signal(close):
    base = _safe_div(close - close.rolling(252).min(), close.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_low_504d_slope_v103_signal(close):
    base = _safe_div(close - close.rolling(504).min(), close.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_low_504d_slope_v104_signal(close):
    base = _safe_div(close - close.rolling(504).min(), close.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_low_504d_slope_v105_signal(close):
    base = _safe_div(close - close.rolling(504).min(), close.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_high_21d_slope_v106_signal(close):
    base = _safe_div(close.rolling(21).max() - close, close.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_high_21d_slope_v107_signal(close):
    base = _safe_div(close.rolling(21).max() - close, close.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_high_21d_slope_v108_signal(close):
    base = _safe_div(close.rolling(21).max() - close, close.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_high_63d_slope_v109_signal(close):
    base = _safe_div(close.rolling(63).max() - close, close.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_high_63d_slope_v110_signal(close):
    base = _safe_div(close.rolling(63).max() - close, close.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_high_63d_slope_v111_signal(close):
    base = _safe_div(close.rolling(63).max() - close, close.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_high_126d_slope_v112_signal(close):
    base = _safe_div(close.rolling(126).max() - close, close.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_high_126d_slope_v113_signal(close):
    base = _safe_div(close.rolling(126).max() - close, close.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_high_126d_slope_v114_signal(close):
    base = _safe_div(close.rolling(126).max() - close, close.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_high_252d_slope_v115_signal(close):
    base = _safe_div(close.rolling(252).max() - close, close.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_high_252d_slope_v116_signal(close):
    base = _safe_div(close.rolling(252).max() - close, close.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_high_252d_slope_v117_signal(close):
    base = _safe_div(close.rolling(252).max() - close, close.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_high_504d_slope_v118_signal(close):
    base = _safe_div(close.rolling(504).max() - close, close.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_high_504d_slope_v119_signal(close):
    base = _safe_div(close.rolling(504).max() - close, close.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high close
def gm_f96_biotech_f96_highest_price_100d_lookback_dist_high_504d_slope_v120_signal(close):
    base = _safe_div(close.rolling(504).max() - close, close.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom close
def gm_f96_biotech_f96_highest_price_100d_lookback_mom_21d_slope_v121_signal(close):
    base = _safe_div(_mean(close, 21) - _mean(close, 42), _mean(close, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom close
def gm_f96_biotech_f96_highest_price_100d_lookback_mom_21d_slope_v122_signal(close):
    base = _safe_div(_mean(close, 21) - _mean(close, 42), _mean(close, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom close
def gm_f96_biotech_f96_highest_price_100d_lookback_mom_21d_slope_v123_signal(close):
    base = _safe_div(_mean(close, 21) - _mean(close, 42), _mean(close, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom close
def gm_f96_biotech_f96_highest_price_100d_lookback_mom_63d_slope_v124_signal(close):
    base = _safe_div(_mean(close, 63) - _mean(close, 126), _mean(close, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom close
def gm_f96_biotech_f96_highest_price_100d_lookback_mom_63d_slope_v125_signal(close):
    base = _safe_div(_mean(close, 63) - _mean(close, 126), _mean(close, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom close
def gm_f96_biotech_f96_highest_price_100d_lookback_mom_63d_slope_v126_signal(close):
    base = _safe_div(_mean(close, 63) - _mean(close, 126), _mean(close, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom close
def gm_f96_biotech_f96_highest_price_100d_lookback_mom_126d_slope_v127_signal(close):
    base = _safe_div(_mean(close, 126) - _mean(close, 252), _mean(close, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom close
def gm_f96_biotech_f96_highest_price_100d_lookback_mom_126d_slope_v128_signal(close):
    base = _safe_div(_mean(close, 126) - _mean(close, 252), _mean(close, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom close
def gm_f96_biotech_f96_highest_price_100d_lookback_mom_126d_slope_v129_signal(close):
    base = _safe_div(_mean(close, 126) - _mean(close, 252), _mean(close, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom close
def gm_f96_biotech_f96_highest_price_100d_lookback_mom_252d_slope_v130_signal(close):
    base = _safe_div(_mean(close, 252) - _mean(close, 504), _mean(close, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom close
def gm_f96_biotech_f96_highest_price_100d_lookback_mom_252d_slope_v131_signal(close):
    base = _safe_div(_mean(close, 252) - _mean(close, 504), _mean(close, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom close
def gm_f96_biotech_f96_highest_price_100d_lookback_mom_252d_slope_v132_signal(close):
    base = _safe_div(_mean(close, 252) - _mean(close, 504), _mean(close, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom close
def gm_f96_biotech_f96_highest_price_100d_lookback_mom_504d_slope_v133_signal(close):
    base = _safe_div(_mean(close, 504) - _mean(close, 1008), _mean(close, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom close
def gm_f96_biotech_f96_highest_price_100d_lookback_mom_504d_slope_v134_signal(close):
    base = _safe_div(_mean(close, 504) - _mean(close, 1008), _mean(close, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom close
def gm_f96_biotech_f96_highest_price_100d_lookback_mom_504d_slope_v135_signal(close):
    base = _safe_div(_mean(close, 504) - _mean(close, 1008), _mean(close, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol close
def gm_f96_biotech_f96_highest_price_100d_lookback_vol_21d_slope_v136_signal(close):
    base = _std(close, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol close
def gm_f96_biotech_f96_highest_price_100d_lookback_vol_21d_slope_v137_signal(close):
    base = _std(close, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol close
def gm_f96_biotech_f96_highest_price_100d_lookback_vol_21d_slope_v138_signal(close):
    base = _std(close, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol close
def gm_f96_biotech_f96_highest_price_100d_lookback_vol_63d_slope_v139_signal(close):
    base = _std(close, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol close
def gm_f96_biotech_f96_highest_price_100d_lookback_vol_63d_slope_v140_signal(close):
    base = _std(close, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol close
def gm_f96_biotech_f96_highest_price_100d_lookback_vol_63d_slope_v141_signal(close):
    base = _std(close, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol close
def gm_f96_biotech_f96_highest_price_100d_lookback_vol_126d_slope_v142_signal(close):
    base = _std(close, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol close
def gm_f96_biotech_f96_highest_price_100d_lookback_vol_126d_slope_v143_signal(close):
    base = _std(close, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol close
def gm_f96_biotech_f96_highest_price_100d_lookback_vol_126d_slope_v144_signal(close):
    base = _std(close, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol close
def gm_f96_biotech_f96_highest_price_100d_lookback_vol_252d_slope_v145_signal(close):
    base = _std(close, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol close
def gm_f96_biotech_f96_highest_price_100d_lookback_vol_252d_slope_v146_signal(close):
    base = _std(close, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol close
def gm_f96_biotech_f96_highest_price_100d_lookback_vol_252d_slope_v147_signal(close):
    base = _std(close, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol close
def gm_f96_biotech_f96_highest_price_100d_lookback_vol_504d_slope_v148_signal(close):
    base = _std(close, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol close
def gm_f96_biotech_f96_highest_price_100d_lookback_vol_504d_slope_v149_signal(close):
    base = _std(close, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol close
def gm_f96_biotech_f96_highest_price_100d_lookback_vol_504d_slope_v150_signal(close):
    base = _std(close, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

