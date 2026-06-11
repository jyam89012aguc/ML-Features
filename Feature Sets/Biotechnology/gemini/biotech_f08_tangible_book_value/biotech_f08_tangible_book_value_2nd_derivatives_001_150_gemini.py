
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw assets
def gm_f08_biotech_f08_tangible_book_value_raw_21d_slope_v001_signal(assets):
    base = _mean(assets, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw assets
def gm_f08_biotech_f08_tangible_book_value_raw_21d_slope_v002_signal(assets):
    base = _mean(assets, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw assets
def gm_f08_biotech_f08_tangible_book_value_raw_21d_slope_v003_signal(assets):
    base = _mean(assets, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw assets
def gm_f08_biotech_f08_tangible_book_value_raw_63d_slope_v004_signal(assets):
    base = _mean(assets, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw assets
def gm_f08_biotech_f08_tangible_book_value_raw_63d_slope_v005_signal(assets):
    base = _mean(assets, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw assets
def gm_f08_biotech_f08_tangible_book_value_raw_63d_slope_v006_signal(assets):
    base = _mean(assets, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw assets
def gm_f08_biotech_f08_tangible_book_value_raw_126d_slope_v007_signal(assets):
    base = _mean(assets, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw assets
def gm_f08_biotech_f08_tangible_book_value_raw_126d_slope_v008_signal(assets):
    base = _mean(assets, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw assets
def gm_f08_biotech_f08_tangible_book_value_raw_126d_slope_v009_signal(assets):
    base = _mean(assets, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw assets
def gm_f08_biotech_f08_tangible_book_value_raw_252d_slope_v010_signal(assets):
    base = _mean(assets, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw assets
def gm_f08_biotech_f08_tangible_book_value_raw_252d_slope_v011_signal(assets):
    base = _mean(assets, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw assets
def gm_f08_biotech_f08_tangible_book_value_raw_252d_slope_v012_signal(assets):
    base = _mean(assets, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw assets
def gm_f08_biotech_f08_tangible_book_value_raw_504d_slope_v013_signal(assets):
    base = _mean(assets, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw assets
def gm_f08_biotech_f08_tangible_book_value_raw_504d_slope_v014_signal(assets):
    base = _mean(assets, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw assets
def gm_f08_biotech_f08_tangible_book_value_raw_504d_slope_v015_signal(assets):
    base = _mean(assets, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log assets
def gm_f08_biotech_f08_tangible_book_value_log_21d_slope_v016_signal(assets):
    base = _mean(_log(assets), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log assets
def gm_f08_biotech_f08_tangible_book_value_log_21d_slope_v017_signal(assets):
    base = _mean(_log(assets), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log assets
def gm_f08_biotech_f08_tangible_book_value_log_21d_slope_v018_signal(assets):
    base = _mean(_log(assets), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log assets
def gm_f08_biotech_f08_tangible_book_value_log_63d_slope_v019_signal(assets):
    base = _mean(_log(assets), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log assets
def gm_f08_biotech_f08_tangible_book_value_log_63d_slope_v020_signal(assets):
    base = _mean(_log(assets), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log assets
def gm_f08_biotech_f08_tangible_book_value_log_63d_slope_v021_signal(assets):
    base = _mean(_log(assets), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log assets
def gm_f08_biotech_f08_tangible_book_value_log_126d_slope_v022_signal(assets):
    base = _mean(_log(assets), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log assets
def gm_f08_biotech_f08_tangible_book_value_log_126d_slope_v023_signal(assets):
    base = _mean(_log(assets), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log assets
def gm_f08_biotech_f08_tangible_book_value_log_126d_slope_v024_signal(assets):
    base = _mean(_log(assets), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log assets
def gm_f08_biotech_f08_tangible_book_value_log_252d_slope_v025_signal(assets):
    base = _mean(_log(assets), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log assets
def gm_f08_biotech_f08_tangible_book_value_log_252d_slope_v026_signal(assets):
    base = _mean(_log(assets), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log assets
def gm_f08_biotech_f08_tangible_book_value_log_252d_slope_v027_signal(assets):
    base = _mean(_log(assets), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log assets
def gm_f08_biotech_f08_tangible_book_value_log_504d_slope_v028_signal(assets):
    base = _mean(_log(assets), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log assets
def gm_f08_biotech_f08_tangible_book_value_log_504d_slope_v029_signal(assets):
    base = _mean(_log(assets), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log assets
def gm_f08_biotech_f08_tangible_book_value_log_504d_slope_v030_signal(assets):
    base = _mean(_log(assets), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z assets
def gm_f08_biotech_f08_tangible_book_value_z_21d_slope_v031_signal(assets):
    base = _z(assets, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z assets
def gm_f08_biotech_f08_tangible_book_value_z_21d_slope_v032_signal(assets):
    base = _z(assets, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z assets
def gm_f08_biotech_f08_tangible_book_value_z_21d_slope_v033_signal(assets):
    base = _z(assets, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z assets
def gm_f08_biotech_f08_tangible_book_value_z_63d_slope_v034_signal(assets):
    base = _z(assets, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z assets
def gm_f08_biotech_f08_tangible_book_value_z_63d_slope_v035_signal(assets):
    base = _z(assets, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z assets
def gm_f08_biotech_f08_tangible_book_value_z_63d_slope_v036_signal(assets):
    base = _z(assets, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z assets
def gm_f08_biotech_f08_tangible_book_value_z_126d_slope_v037_signal(assets):
    base = _z(assets, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z assets
def gm_f08_biotech_f08_tangible_book_value_z_126d_slope_v038_signal(assets):
    base = _z(assets, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z assets
def gm_f08_biotech_f08_tangible_book_value_z_126d_slope_v039_signal(assets):
    base = _z(assets, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z assets
def gm_f08_biotech_f08_tangible_book_value_z_252d_slope_v040_signal(assets):
    base = _z(assets, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z assets
def gm_f08_biotech_f08_tangible_book_value_z_252d_slope_v041_signal(assets):
    base = _z(assets, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z assets
def gm_f08_biotech_f08_tangible_book_value_z_252d_slope_v042_signal(assets):
    base = _z(assets, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z assets
def gm_f08_biotech_f08_tangible_book_value_z_504d_slope_v043_signal(assets):
    base = _z(assets, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z assets
def gm_f08_biotech_f08_tangible_book_value_z_504d_slope_v044_signal(assets):
    base = _z(assets, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z assets
def gm_f08_biotech_f08_tangible_book_value_z_504d_slope_v045_signal(assets):
    base = _z(assets, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps assets
def gm_f08_biotech_f08_tangible_book_value_ps_21d_slope_v046_signal(assets, sharesbas):
    base = _safe_div(_mean(assets, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps assets
def gm_f08_biotech_f08_tangible_book_value_ps_21d_slope_v047_signal(assets, sharesbas):
    base = _safe_div(_mean(assets, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps assets
def gm_f08_biotech_f08_tangible_book_value_ps_21d_slope_v048_signal(assets, sharesbas):
    base = _safe_div(_mean(assets, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps assets
def gm_f08_biotech_f08_tangible_book_value_ps_63d_slope_v049_signal(assets, sharesbas):
    base = _safe_div(_mean(assets, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps assets
def gm_f08_biotech_f08_tangible_book_value_ps_63d_slope_v050_signal(assets, sharesbas):
    base = _safe_div(_mean(assets, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps assets
def gm_f08_biotech_f08_tangible_book_value_ps_63d_slope_v051_signal(assets, sharesbas):
    base = _safe_div(_mean(assets, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps assets
def gm_f08_biotech_f08_tangible_book_value_ps_126d_slope_v052_signal(assets, sharesbas):
    base = _safe_div(_mean(assets, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps assets
def gm_f08_biotech_f08_tangible_book_value_ps_126d_slope_v053_signal(assets, sharesbas):
    base = _safe_div(_mean(assets, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps assets
def gm_f08_biotech_f08_tangible_book_value_ps_126d_slope_v054_signal(assets, sharesbas):
    base = _safe_div(_mean(assets, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps assets
def gm_f08_biotech_f08_tangible_book_value_ps_252d_slope_v055_signal(assets, sharesbas):
    base = _safe_div(_mean(assets, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps assets
def gm_f08_biotech_f08_tangible_book_value_ps_252d_slope_v056_signal(assets, sharesbas):
    base = _safe_div(_mean(assets, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps assets
def gm_f08_biotech_f08_tangible_book_value_ps_252d_slope_v057_signal(assets, sharesbas):
    base = _safe_div(_mean(assets, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps assets
def gm_f08_biotech_f08_tangible_book_value_ps_504d_slope_v058_signal(assets, sharesbas):
    base = _safe_div(_mean(assets, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps assets
def gm_f08_biotech_f08_tangible_book_value_ps_504d_slope_v059_signal(assets, sharesbas):
    base = _safe_div(_mean(assets, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps assets
def gm_f08_biotech_f08_tangible_book_value_ps_504d_slope_v060_signal(assets, sharesbas):
    base = _safe_div(_mean(assets, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_21d_slope_v061_signal(assets):
    base = _safe_div(_mean(assets, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_21d_slope_v062_signal(assets):
    base = _safe_div(_mean(assets, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_21d_slope_v063_signal(assets):
    base = _safe_div(_mean(assets, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_63d_slope_v064_signal(assets):
    base = _safe_div(_mean(assets, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_63d_slope_v065_signal(assets):
    base = _safe_div(_mean(assets, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_63d_slope_v066_signal(assets):
    base = _safe_div(_mean(assets, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_126d_slope_v067_signal(assets):
    base = _safe_div(_mean(assets, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_126d_slope_v068_signal(assets):
    base = _safe_div(_mean(assets, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_126d_slope_v069_signal(assets):
    base = _safe_div(_mean(assets, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_252d_slope_v070_signal(assets):
    base = _safe_div(_mean(assets, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_252d_slope_v071_signal(assets):
    base = _safe_div(_mean(assets, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_252d_slope_v072_signal(assets):
    base = _safe_div(_mean(assets, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_504d_slope_v073_signal(assets):
    base = _safe_div(_mean(assets, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_504d_slope_v074_signal(assets):
    base = _safe_div(_mean(assets, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_504d_slope_v075_signal(assets):
    base = _safe_div(_mean(assets, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled assets
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_21d_slope_v076_signal(assets, marketcap):
    base = _safe_div(_mean(assets, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled assets
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_21d_slope_v077_signal(assets, marketcap):
    base = _safe_div(_mean(assets, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled assets
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_21d_slope_v078_signal(assets, marketcap):
    base = _safe_div(_mean(assets, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled assets
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_63d_slope_v079_signal(assets, marketcap):
    base = _safe_div(_mean(assets, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled assets
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_63d_slope_v080_signal(assets, marketcap):
    base = _safe_div(_mean(assets, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled assets
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_63d_slope_v081_signal(assets, marketcap):
    base = _safe_div(_mean(assets, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled assets
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_126d_slope_v082_signal(assets, marketcap):
    base = _safe_div(_mean(assets, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled assets
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_126d_slope_v083_signal(assets, marketcap):
    base = _safe_div(_mean(assets, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled assets
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_126d_slope_v084_signal(assets, marketcap):
    base = _safe_div(_mean(assets, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled assets
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_252d_slope_v085_signal(assets, marketcap):
    base = _safe_div(_mean(assets, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled assets
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_252d_slope_v086_signal(assets, marketcap):
    base = _safe_div(_mean(assets, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled assets
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_252d_slope_v087_signal(assets, marketcap):
    base = _safe_div(_mean(assets, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled assets
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_504d_slope_v088_signal(assets, marketcap):
    base = _safe_div(_mean(assets, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled assets
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_504d_slope_v089_signal(assets, marketcap):
    base = _safe_div(_mean(assets, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled assets
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_504d_slope_v090_signal(assets, marketcap):
    base = _safe_div(_mean(assets, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_21d_slope_v091_signal(assets):
    base = _safe_div(assets - assets.rolling(21).min(), assets.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_21d_slope_v092_signal(assets):
    base = _safe_div(assets - assets.rolling(21).min(), assets.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_21d_slope_v093_signal(assets):
    base = _safe_div(assets - assets.rolling(21).min(), assets.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_63d_slope_v094_signal(assets):
    base = _safe_div(assets - assets.rolling(63).min(), assets.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_63d_slope_v095_signal(assets):
    base = _safe_div(assets - assets.rolling(63).min(), assets.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_63d_slope_v096_signal(assets):
    base = _safe_div(assets - assets.rolling(63).min(), assets.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_126d_slope_v097_signal(assets):
    base = _safe_div(assets - assets.rolling(126).min(), assets.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_126d_slope_v098_signal(assets):
    base = _safe_div(assets - assets.rolling(126).min(), assets.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_126d_slope_v099_signal(assets):
    base = _safe_div(assets - assets.rolling(126).min(), assets.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_252d_slope_v100_signal(assets):
    base = _safe_div(assets - assets.rolling(252).min(), assets.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_252d_slope_v101_signal(assets):
    base = _safe_div(assets - assets.rolling(252).min(), assets.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_252d_slope_v102_signal(assets):
    base = _safe_div(assets - assets.rolling(252).min(), assets.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_504d_slope_v103_signal(assets):
    base = _safe_div(assets - assets.rolling(504).min(), assets.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_504d_slope_v104_signal(assets):
    base = _safe_div(assets - assets.rolling(504).min(), assets.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_504d_slope_v105_signal(assets):
    base = _safe_div(assets - assets.rolling(504).min(), assets.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_21d_slope_v106_signal(assets):
    base = _safe_div(assets.rolling(21).max() - assets, assets.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_21d_slope_v107_signal(assets):
    base = _safe_div(assets.rolling(21).max() - assets, assets.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_21d_slope_v108_signal(assets):
    base = _safe_div(assets.rolling(21).max() - assets, assets.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_63d_slope_v109_signal(assets):
    base = _safe_div(assets.rolling(63).max() - assets, assets.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_63d_slope_v110_signal(assets):
    base = _safe_div(assets.rolling(63).max() - assets, assets.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_63d_slope_v111_signal(assets):
    base = _safe_div(assets.rolling(63).max() - assets, assets.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_126d_slope_v112_signal(assets):
    base = _safe_div(assets.rolling(126).max() - assets, assets.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_126d_slope_v113_signal(assets):
    base = _safe_div(assets.rolling(126).max() - assets, assets.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_126d_slope_v114_signal(assets):
    base = _safe_div(assets.rolling(126).max() - assets, assets.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_252d_slope_v115_signal(assets):
    base = _safe_div(assets.rolling(252).max() - assets, assets.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_252d_slope_v116_signal(assets):
    base = _safe_div(assets.rolling(252).max() - assets, assets.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_252d_slope_v117_signal(assets):
    base = _safe_div(assets.rolling(252).max() - assets, assets.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_504d_slope_v118_signal(assets):
    base = _safe_div(assets.rolling(504).max() - assets, assets.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_504d_slope_v119_signal(assets):
    base = _safe_div(assets.rolling(504).max() - assets, assets.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_504d_slope_v120_signal(assets):
    base = _safe_div(assets.rolling(504).max() - assets, assets.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom assets
def gm_f08_biotech_f08_tangible_book_value_mom_21d_slope_v121_signal(assets):
    base = _safe_div(_mean(assets, 21) - _mean(assets, 42), _mean(assets, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom assets
def gm_f08_biotech_f08_tangible_book_value_mom_21d_slope_v122_signal(assets):
    base = _safe_div(_mean(assets, 21) - _mean(assets, 42), _mean(assets, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom assets
def gm_f08_biotech_f08_tangible_book_value_mom_21d_slope_v123_signal(assets):
    base = _safe_div(_mean(assets, 21) - _mean(assets, 42), _mean(assets, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom assets
def gm_f08_biotech_f08_tangible_book_value_mom_63d_slope_v124_signal(assets):
    base = _safe_div(_mean(assets, 63) - _mean(assets, 126), _mean(assets, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom assets
def gm_f08_biotech_f08_tangible_book_value_mom_63d_slope_v125_signal(assets):
    base = _safe_div(_mean(assets, 63) - _mean(assets, 126), _mean(assets, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom assets
def gm_f08_biotech_f08_tangible_book_value_mom_63d_slope_v126_signal(assets):
    base = _safe_div(_mean(assets, 63) - _mean(assets, 126), _mean(assets, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom assets
def gm_f08_biotech_f08_tangible_book_value_mom_126d_slope_v127_signal(assets):
    base = _safe_div(_mean(assets, 126) - _mean(assets, 252), _mean(assets, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom assets
def gm_f08_biotech_f08_tangible_book_value_mom_126d_slope_v128_signal(assets):
    base = _safe_div(_mean(assets, 126) - _mean(assets, 252), _mean(assets, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom assets
def gm_f08_biotech_f08_tangible_book_value_mom_126d_slope_v129_signal(assets):
    base = _safe_div(_mean(assets, 126) - _mean(assets, 252), _mean(assets, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom assets
def gm_f08_biotech_f08_tangible_book_value_mom_252d_slope_v130_signal(assets):
    base = _safe_div(_mean(assets, 252) - _mean(assets, 504), _mean(assets, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom assets
def gm_f08_biotech_f08_tangible_book_value_mom_252d_slope_v131_signal(assets):
    base = _safe_div(_mean(assets, 252) - _mean(assets, 504), _mean(assets, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom assets
def gm_f08_biotech_f08_tangible_book_value_mom_252d_slope_v132_signal(assets):
    base = _safe_div(_mean(assets, 252) - _mean(assets, 504), _mean(assets, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom assets
def gm_f08_biotech_f08_tangible_book_value_mom_504d_slope_v133_signal(assets):
    base = _safe_div(_mean(assets, 504) - _mean(assets, 1008), _mean(assets, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom assets
def gm_f08_biotech_f08_tangible_book_value_mom_504d_slope_v134_signal(assets):
    base = _safe_div(_mean(assets, 504) - _mean(assets, 1008), _mean(assets, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom assets
def gm_f08_biotech_f08_tangible_book_value_mom_504d_slope_v135_signal(assets):
    base = _safe_div(_mean(assets, 504) - _mean(assets, 1008), _mean(assets, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol assets
def gm_f08_biotech_f08_tangible_book_value_vol_21d_slope_v136_signal(assets):
    base = _std(assets, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol assets
def gm_f08_biotech_f08_tangible_book_value_vol_21d_slope_v137_signal(assets):
    base = _std(assets, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol assets
def gm_f08_biotech_f08_tangible_book_value_vol_21d_slope_v138_signal(assets):
    base = _std(assets, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol assets
def gm_f08_biotech_f08_tangible_book_value_vol_63d_slope_v139_signal(assets):
    base = _std(assets, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol assets
def gm_f08_biotech_f08_tangible_book_value_vol_63d_slope_v140_signal(assets):
    base = _std(assets, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol assets
def gm_f08_biotech_f08_tangible_book_value_vol_63d_slope_v141_signal(assets):
    base = _std(assets, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol assets
def gm_f08_biotech_f08_tangible_book_value_vol_126d_slope_v142_signal(assets):
    base = _std(assets, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol assets
def gm_f08_biotech_f08_tangible_book_value_vol_126d_slope_v143_signal(assets):
    base = _std(assets, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol assets
def gm_f08_biotech_f08_tangible_book_value_vol_126d_slope_v144_signal(assets):
    base = _std(assets, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol assets
def gm_f08_biotech_f08_tangible_book_value_vol_252d_slope_v145_signal(assets):
    base = _std(assets, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol assets
def gm_f08_biotech_f08_tangible_book_value_vol_252d_slope_v146_signal(assets):
    base = _std(assets, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol assets
def gm_f08_biotech_f08_tangible_book_value_vol_252d_slope_v147_signal(assets):
    base = _std(assets, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol assets
def gm_f08_biotech_f08_tangible_book_value_vol_504d_slope_v148_signal(assets):
    base = _std(assets, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol assets
def gm_f08_biotech_f08_tangible_book_value_vol_504d_slope_v149_signal(assets):
    base = _std(assets, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol assets
def gm_f08_biotech_f08_tangible_book_value_vol_504d_slope_v150_signal(assets):
    base = _std(assets, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

