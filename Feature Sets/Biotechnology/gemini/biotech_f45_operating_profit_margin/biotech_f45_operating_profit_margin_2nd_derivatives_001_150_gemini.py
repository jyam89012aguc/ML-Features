
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_21d_slope_v001_signal(opinc):
    base = _mean(opinc, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_21d_slope_v002_signal(opinc):
    base = _mean(opinc, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_21d_slope_v003_signal(opinc):
    base = _mean(opinc, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_63d_slope_v004_signal(opinc):
    base = _mean(opinc, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_63d_slope_v005_signal(opinc):
    base = _mean(opinc, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_63d_slope_v006_signal(opinc):
    base = _mean(opinc, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_126d_slope_v007_signal(opinc):
    base = _mean(opinc, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_126d_slope_v008_signal(opinc):
    base = _mean(opinc, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_126d_slope_v009_signal(opinc):
    base = _mean(opinc, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_252d_slope_v010_signal(opinc):
    base = _mean(opinc, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_252d_slope_v011_signal(opinc):
    base = _mean(opinc, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_252d_slope_v012_signal(opinc):
    base = _mean(opinc, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_504d_slope_v013_signal(opinc):
    base = _mean(opinc, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_504d_slope_v014_signal(opinc):
    base = _mean(opinc, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_504d_slope_v015_signal(opinc):
    base = _mean(opinc, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_21d_slope_v016_signal(opinc):
    base = _mean(_log(opinc), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_21d_slope_v017_signal(opinc):
    base = _mean(_log(opinc), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_21d_slope_v018_signal(opinc):
    base = _mean(_log(opinc), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_63d_slope_v019_signal(opinc):
    base = _mean(_log(opinc), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_63d_slope_v020_signal(opinc):
    base = _mean(_log(opinc), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_63d_slope_v021_signal(opinc):
    base = _mean(_log(opinc), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_126d_slope_v022_signal(opinc):
    base = _mean(_log(opinc), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_126d_slope_v023_signal(opinc):
    base = _mean(_log(opinc), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_126d_slope_v024_signal(opinc):
    base = _mean(_log(opinc), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_252d_slope_v025_signal(opinc):
    base = _mean(_log(opinc), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_252d_slope_v026_signal(opinc):
    base = _mean(_log(opinc), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_252d_slope_v027_signal(opinc):
    base = _mean(_log(opinc), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_504d_slope_v028_signal(opinc):
    base = _mean(_log(opinc), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_504d_slope_v029_signal(opinc):
    base = _mean(_log(opinc), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_504d_slope_v030_signal(opinc):
    base = _mean(_log(opinc), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_21d_slope_v031_signal(opinc):
    base = _z(opinc, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_21d_slope_v032_signal(opinc):
    base = _z(opinc, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_21d_slope_v033_signal(opinc):
    base = _z(opinc, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_63d_slope_v034_signal(opinc):
    base = _z(opinc, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_63d_slope_v035_signal(opinc):
    base = _z(opinc, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_63d_slope_v036_signal(opinc):
    base = _z(opinc, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_126d_slope_v037_signal(opinc):
    base = _z(opinc, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_126d_slope_v038_signal(opinc):
    base = _z(opinc, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_126d_slope_v039_signal(opinc):
    base = _z(opinc, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_252d_slope_v040_signal(opinc):
    base = _z(opinc, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_252d_slope_v041_signal(opinc):
    base = _z(opinc, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_252d_slope_v042_signal(opinc):
    base = _z(opinc, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_504d_slope_v043_signal(opinc):
    base = _z(opinc, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_504d_slope_v044_signal(opinc):
    base = _z(opinc, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_504d_slope_v045_signal(opinc):
    base = _z(opinc, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_21d_slope_v046_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_21d_slope_v047_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_21d_slope_v048_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_63d_slope_v049_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_63d_slope_v050_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_63d_slope_v051_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_126d_slope_v052_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_126d_slope_v053_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_126d_slope_v054_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_252d_slope_v055_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_252d_slope_v056_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_252d_slope_v057_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_504d_slope_v058_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_504d_slope_v059_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_504d_slope_v060_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_21d_slope_v061_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_21d_slope_v062_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_21d_slope_v063_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_63d_slope_v064_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_63d_slope_v065_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_63d_slope_v066_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_126d_slope_v067_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_126d_slope_v068_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_126d_slope_v069_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_252d_slope_v070_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_252d_slope_v071_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_252d_slope_v072_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_504d_slope_v073_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_504d_slope_v074_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_504d_slope_v075_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_21d_slope_v076_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_21d_slope_v077_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_21d_slope_v078_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_63d_slope_v079_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_63d_slope_v080_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_63d_slope_v081_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_126d_slope_v082_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_126d_slope_v083_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_126d_slope_v084_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_252d_slope_v085_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_252d_slope_v086_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_252d_slope_v087_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_504d_slope_v088_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_504d_slope_v089_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_504d_slope_v090_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_21d_slope_v091_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(21).min(), opinc.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_21d_slope_v092_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(21).min(), opinc.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_21d_slope_v093_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(21).min(), opinc.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_63d_slope_v094_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(63).min(), opinc.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_63d_slope_v095_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(63).min(), opinc.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_63d_slope_v096_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(63).min(), opinc.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_126d_slope_v097_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(126).min(), opinc.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_126d_slope_v098_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(126).min(), opinc.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_126d_slope_v099_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(126).min(), opinc.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_252d_slope_v100_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(252).min(), opinc.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_252d_slope_v101_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(252).min(), opinc.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_252d_slope_v102_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(252).min(), opinc.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_504d_slope_v103_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(504).min(), opinc.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_504d_slope_v104_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(504).min(), opinc.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_504d_slope_v105_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(504).min(), opinc.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_21d_slope_v106_signal(opinc):
    base = _safe_div(opinc.rolling(21).max() - opinc, opinc.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_21d_slope_v107_signal(opinc):
    base = _safe_div(opinc.rolling(21).max() - opinc, opinc.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_21d_slope_v108_signal(opinc):
    base = _safe_div(opinc.rolling(21).max() - opinc, opinc.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_63d_slope_v109_signal(opinc):
    base = _safe_div(opinc.rolling(63).max() - opinc, opinc.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_63d_slope_v110_signal(opinc):
    base = _safe_div(opinc.rolling(63).max() - opinc, opinc.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_63d_slope_v111_signal(opinc):
    base = _safe_div(opinc.rolling(63).max() - opinc, opinc.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_126d_slope_v112_signal(opinc):
    base = _safe_div(opinc.rolling(126).max() - opinc, opinc.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_126d_slope_v113_signal(opinc):
    base = _safe_div(opinc.rolling(126).max() - opinc, opinc.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_126d_slope_v114_signal(opinc):
    base = _safe_div(opinc.rolling(126).max() - opinc, opinc.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_252d_slope_v115_signal(opinc):
    base = _safe_div(opinc.rolling(252).max() - opinc, opinc.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_252d_slope_v116_signal(opinc):
    base = _safe_div(opinc.rolling(252).max() - opinc, opinc.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_252d_slope_v117_signal(opinc):
    base = _safe_div(opinc.rolling(252).max() - opinc, opinc.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_504d_slope_v118_signal(opinc):
    base = _safe_div(opinc.rolling(504).max() - opinc, opinc.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_504d_slope_v119_signal(opinc):
    base = _safe_div(opinc.rolling(504).max() - opinc, opinc.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_504d_slope_v120_signal(opinc):
    base = _safe_div(opinc.rolling(504).max() - opinc, opinc.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_21d_slope_v121_signal(opinc):
    base = _safe_div(_mean(opinc, 21) - _mean(opinc, 42), _mean(opinc, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_21d_slope_v122_signal(opinc):
    base = _safe_div(_mean(opinc, 21) - _mean(opinc, 42), _mean(opinc, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_21d_slope_v123_signal(opinc):
    base = _safe_div(_mean(opinc, 21) - _mean(opinc, 42), _mean(opinc, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_63d_slope_v124_signal(opinc):
    base = _safe_div(_mean(opinc, 63) - _mean(opinc, 126), _mean(opinc, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_63d_slope_v125_signal(opinc):
    base = _safe_div(_mean(opinc, 63) - _mean(opinc, 126), _mean(opinc, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_63d_slope_v126_signal(opinc):
    base = _safe_div(_mean(opinc, 63) - _mean(opinc, 126), _mean(opinc, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_126d_slope_v127_signal(opinc):
    base = _safe_div(_mean(opinc, 126) - _mean(opinc, 252), _mean(opinc, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_126d_slope_v128_signal(opinc):
    base = _safe_div(_mean(opinc, 126) - _mean(opinc, 252), _mean(opinc, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_126d_slope_v129_signal(opinc):
    base = _safe_div(_mean(opinc, 126) - _mean(opinc, 252), _mean(opinc, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_252d_slope_v130_signal(opinc):
    base = _safe_div(_mean(opinc, 252) - _mean(opinc, 504), _mean(opinc, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_252d_slope_v131_signal(opinc):
    base = _safe_div(_mean(opinc, 252) - _mean(opinc, 504), _mean(opinc, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_252d_slope_v132_signal(opinc):
    base = _safe_div(_mean(opinc, 252) - _mean(opinc, 504), _mean(opinc, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_504d_slope_v133_signal(opinc):
    base = _safe_div(_mean(opinc, 504) - _mean(opinc, 1008), _mean(opinc, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_504d_slope_v134_signal(opinc):
    base = _safe_div(_mean(opinc, 504) - _mean(opinc, 1008), _mean(opinc, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_504d_slope_v135_signal(opinc):
    base = _safe_div(_mean(opinc, 504) - _mean(opinc, 1008), _mean(opinc, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_21d_slope_v136_signal(opinc):
    base = _std(opinc, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_21d_slope_v137_signal(opinc):
    base = _std(opinc, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_21d_slope_v138_signal(opinc):
    base = _std(opinc, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_63d_slope_v139_signal(opinc):
    base = _std(opinc, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_63d_slope_v140_signal(opinc):
    base = _std(opinc, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_63d_slope_v141_signal(opinc):
    base = _std(opinc, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_126d_slope_v142_signal(opinc):
    base = _std(opinc, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_126d_slope_v143_signal(opinc):
    base = _std(opinc, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_126d_slope_v144_signal(opinc):
    base = _std(opinc, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_252d_slope_v145_signal(opinc):
    base = _std(opinc, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_252d_slope_v146_signal(opinc):
    base = _std(opinc, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_252d_slope_v147_signal(opinc):
    base = _std(opinc, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_504d_slope_v148_signal(opinc):
    base = _std(opinc, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_504d_slope_v149_signal(opinc):
    base = _std(opinc, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_504d_slope_v150_signal(opinc):
    base = _std(opinc, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

