
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_21d_slope_v001_signal(epsdil):
    base = _mean(epsdil, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_21d_slope_v002_signal(epsdil):
    base = _mean(epsdil, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_21d_slope_v003_signal(epsdil):
    base = _mean(epsdil, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_63d_slope_v004_signal(epsdil):
    base = _mean(epsdil, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_63d_slope_v005_signal(epsdil):
    base = _mean(epsdil, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_63d_slope_v006_signal(epsdil):
    base = _mean(epsdil, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_126d_slope_v007_signal(epsdil):
    base = _mean(epsdil, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_126d_slope_v008_signal(epsdil):
    base = _mean(epsdil, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_126d_slope_v009_signal(epsdil):
    base = _mean(epsdil, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_252d_slope_v010_signal(epsdil):
    base = _mean(epsdil, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_252d_slope_v011_signal(epsdil):
    base = _mean(epsdil, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_252d_slope_v012_signal(epsdil):
    base = _mean(epsdil, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_504d_slope_v013_signal(epsdil):
    base = _mean(epsdil, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_504d_slope_v014_signal(epsdil):
    base = _mean(epsdil, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_504d_slope_v015_signal(epsdil):
    base = _mean(epsdil, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_21d_slope_v016_signal(epsdil):
    base = _mean(_log(epsdil), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_21d_slope_v017_signal(epsdil):
    base = _mean(_log(epsdil), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_21d_slope_v018_signal(epsdil):
    base = _mean(_log(epsdil), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_63d_slope_v019_signal(epsdil):
    base = _mean(_log(epsdil), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_63d_slope_v020_signal(epsdil):
    base = _mean(_log(epsdil), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_63d_slope_v021_signal(epsdil):
    base = _mean(_log(epsdil), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_126d_slope_v022_signal(epsdil):
    base = _mean(_log(epsdil), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_126d_slope_v023_signal(epsdil):
    base = _mean(_log(epsdil), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_126d_slope_v024_signal(epsdil):
    base = _mean(_log(epsdil), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_252d_slope_v025_signal(epsdil):
    base = _mean(_log(epsdil), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_252d_slope_v026_signal(epsdil):
    base = _mean(_log(epsdil), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_252d_slope_v027_signal(epsdil):
    base = _mean(_log(epsdil), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_504d_slope_v028_signal(epsdil):
    base = _mean(_log(epsdil), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_504d_slope_v029_signal(epsdil):
    base = _mean(_log(epsdil), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_504d_slope_v030_signal(epsdil):
    base = _mean(_log(epsdil), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_21d_slope_v031_signal(epsdil):
    base = _z(epsdil, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_21d_slope_v032_signal(epsdil):
    base = _z(epsdil, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_21d_slope_v033_signal(epsdil):
    base = _z(epsdil, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_63d_slope_v034_signal(epsdil):
    base = _z(epsdil, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_63d_slope_v035_signal(epsdil):
    base = _z(epsdil, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_63d_slope_v036_signal(epsdil):
    base = _z(epsdil, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_126d_slope_v037_signal(epsdil):
    base = _z(epsdil, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_126d_slope_v038_signal(epsdil):
    base = _z(epsdil, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_126d_slope_v039_signal(epsdil):
    base = _z(epsdil, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_252d_slope_v040_signal(epsdil):
    base = _z(epsdil, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_252d_slope_v041_signal(epsdil):
    base = _z(epsdil, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_252d_slope_v042_signal(epsdil):
    base = _z(epsdil, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_504d_slope_v043_signal(epsdil):
    base = _z(epsdil, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_504d_slope_v044_signal(epsdil):
    base = _z(epsdil, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_504d_slope_v045_signal(epsdil):
    base = _z(epsdil, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_21d_slope_v046_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_21d_slope_v047_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_21d_slope_v048_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_63d_slope_v049_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_63d_slope_v050_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_63d_slope_v051_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_126d_slope_v052_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_126d_slope_v053_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_126d_slope_v054_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_252d_slope_v055_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_252d_slope_v056_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_252d_slope_v057_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_504d_slope_v058_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_504d_slope_v059_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_504d_slope_v060_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_21d_slope_v061_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_21d_slope_v062_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_21d_slope_v063_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_63d_slope_v064_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_63d_slope_v065_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_63d_slope_v066_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_126d_slope_v067_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_126d_slope_v068_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_126d_slope_v069_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_252d_slope_v070_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_252d_slope_v071_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_252d_slope_v072_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_504d_slope_v073_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_504d_slope_v074_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_504d_slope_v075_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_21d_slope_v076_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_21d_slope_v077_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_21d_slope_v078_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_63d_slope_v079_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_63d_slope_v080_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_63d_slope_v081_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_126d_slope_v082_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_126d_slope_v083_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_126d_slope_v084_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_252d_slope_v085_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_252d_slope_v086_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_252d_slope_v087_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_504d_slope_v088_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_504d_slope_v089_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_504d_slope_v090_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_21d_slope_v091_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(21).min(), epsdil.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_21d_slope_v092_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(21).min(), epsdil.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_21d_slope_v093_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(21).min(), epsdil.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_63d_slope_v094_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(63).min(), epsdil.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_63d_slope_v095_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(63).min(), epsdil.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_63d_slope_v096_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(63).min(), epsdil.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_126d_slope_v097_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(126).min(), epsdil.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_126d_slope_v098_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(126).min(), epsdil.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_126d_slope_v099_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(126).min(), epsdil.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_252d_slope_v100_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(252).min(), epsdil.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_252d_slope_v101_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(252).min(), epsdil.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_252d_slope_v102_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(252).min(), epsdil.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_504d_slope_v103_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(504).min(), epsdil.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_504d_slope_v104_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(504).min(), epsdil.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_504d_slope_v105_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(504).min(), epsdil.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_21d_slope_v106_signal(epsdil):
    base = _safe_div(epsdil.rolling(21).max() - epsdil, epsdil.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_21d_slope_v107_signal(epsdil):
    base = _safe_div(epsdil.rolling(21).max() - epsdil, epsdil.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_21d_slope_v108_signal(epsdil):
    base = _safe_div(epsdil.rolling(21).max() - epsdil, epsdil.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_63d_slope_v109_signal(epsdil):
    base = _safe_div(epsdil.rolling(63).max() - epsdil, epsdil.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_63d_slope_v110_signal(epsdil):
    base = _safe_div(epsdil.rolling(63).max() - epsdil, epsdil.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_63d_slope_v111_signal(epsdil):
    base = _safe_div(epsdil.rolling(63).max() - epsdil, epsdil.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_126d_slope_v112_signal(epsdil):
    base = _safe_div(epsdil.rolling(126).max() - epsdil, epsdil.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_126d_slope_v113_signal(epsdil):
    base = _safe_div(epsdil.rolling(126).max() - epsdil, epsdil.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_126d_slope_v114_signal(epsdil):
    base = _safe_div(epsdil.rolling(126).max() - epsdil, epsdil.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_252d_slope_v115_signal(epsdil):
    base = _safe_div(epsdil.rolling(252).max() - epsdil, epsdil.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_252d_slope_v116_signal(epsdil):
    base = _safe_div(epsdil.rolling(252).max() - epsdil, epsdil.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_252d_slope_v117_signal(epsdil):
    base = _safe_div(epsdil.rolling(252).max() - epsdil, epsdil.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_504d_slope_v118_signal(epsdil):
    base = _safe_div(epsdil.rolling(504).max() - epsdil, epsdil.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_504d_slope_v119_signal(epsdil):
    base = _safe_div(epsdil.rolling(504).max() - epsdil, epsdil.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_504d_slope_v120_signal(epsdil):
    base = _safe_div(epsdil.rolling(504).max() - epsdil, epsdil.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_21d_slope_v121_signal(epsdil):
    base = _safe_div(_mean(epsdil, 21) - _mean(epsdil, 42), _mean(epsdil, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_21d_slope_v122_signal(epsdil):
    base = _safe_div(_mean(epsdil, 21) - _mean(epsdil, 42), _mean(epsdil, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_21d_slope_v123_signal(epsdil):
    base = _safe_div(_mean(epsdil, 21) - _mean(epsdil, 42), _mean(epsdil, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_63d_slope_v124_signal(epsdil):
    base = _safe_div(_mean(epsdil, 63) - _mean(epsdil, 126), _mean(epsdil, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_63d_slope_v125_signal(epsdil):
    base = _safe_div(_mean(epsdil, 63) - _mean(epsdil, 126), _mean(epsdil, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_63d_slope_v126_signal(epsdil):
    base = _safe_div(_mean(epsdil, 63) - _mean(epsdil, 126), _mean(epsdil, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_126d_slope_v127_signal(epsdil):
    base = _safe_div(_mean(epsdil, 126) - _mean(epsdil, 252), _mean(epsdil, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_126d_slope_v128_signal(epsdil):
    base = _safe_div(_mean(epsdil, 126) - _mean(epsdil, 252), _mean(epsdil, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_126d_slope_v129_signal(epsdil):
    base = _safe_div(_mean(epsdil, 126) - _mean(epsdil, 252), _mean(epsdil, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_252d_slope_v130_signal(epsdil):
    base = _safe_div(_mean(epsdil, 252) - _mean(epsdil, 504), _mean(epsdil, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_252d_slope_v131_signal(epsdil):
    base = _safe_div(_mean(epsdil, 252) - _mean(epsdil, 504), _mean(epsdil, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_252d_slope_v132_signal(epsdil):
    base = _safe_div(_mean(epsdil, 252) - _mean(epsdil, 504), _mean(epsdil, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_504d_slope_v133_signal(epsdil):
    base = _safe_div(_mean(epsdil, 504) - _mean(epsdil, 1008), _mean(epsdil, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_504d_slope_v134_signal(epsdil):
    base = _safe_div(_mean(epsdil, 504) - _mean(epsdil, 1008), _mean(epsdil, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_504d_slope_v135_signal(epsdil):
    base = _safe_div(_mean(epsdil, 504) - _mean(epsdil, 1008), _mean(epsdil, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_21d_slope_v136_signal(epsdil):
    base = _std(epsdil, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_21d_slope_v137_signal(epsdil):
    base = _std(epsdil, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_21d_slope_v138_signal(epsdil):
    base = _std(epsdil, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_63d_slope_v139_signal(epsdil):
    base = _std(epsdil, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_63d_slope_v140_signal(epsdil):
    base = _std(epsdil, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_63d_slope_v141_signal(epsdil):
    base = _std(epsdil, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_126d_slope_v142_signal(epsdil):
    base = _std(epsdil, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_126d_slope_v143_signal(epsdil):
    base = _std(epsdil, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_126d_slope_v144_signal(epsdil):
    base = _std(epsdil, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_252d_slope_v145_signal(epsdil):
    base = _std(epsdil, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_252d_slope_v146_signal(epsdil):
    base = _std(epsdil, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_252d_slope_v147_signal(epsdil):
    base = _std(epsdil, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_504d_slope_v148_signal(epsdil):
    base = _std(epsdil, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_504d_slope_v149_signal(epsdil):
    base = _std(epsdil, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_504d_slope_v150_signal(epsdil):
    base = _std(epsdil, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

