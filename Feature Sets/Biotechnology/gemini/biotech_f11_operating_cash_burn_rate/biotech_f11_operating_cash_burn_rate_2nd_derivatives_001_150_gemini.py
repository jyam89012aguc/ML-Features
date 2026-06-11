
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_raw_21d_slope_v001_signal(ncfo):
    base = _mean(ncfo, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_raw_21d_slope_v002_signal(ncfo):
    base = _mean(ncfo, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_raw_21d_slope_v003_signal(ncfo):
    base = _mean(ncfo, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_raw_63d_slope_v004_signal(ncfo):
    base = _mean(ncfo, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_raw_63d_slope_v005_signal(ncfo):
    base = _mean(ncfo, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_raw_63d_slope_v006_signal(ncfo):
    base = _mean(ncfo, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_raw_126d_slope_v007_signal(ncfo):
    base = _mean(ncfo, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_raw_126d_slope_v008_signal(ncfo):
    base = _mean(ncfo, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_raw_126d_slope_v009_signal(ncfo):
    base = _mean(ncfo, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_raw_252d_slope_v010_signal(ncfo):
    base = _mean(ncfo, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_raw_252d_slope_v011_signal(ncfo):
    base = _mean(ncfo, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_raw_252d_slope_v012_signal(ncfo):
    base = _mean(ncfo, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_raw_504d_slope_v013_signal(ncfo):
    base = _mean(ncfo, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_raw_504d_slope_v014_signal(ncfo):
    base = _mean(ncfo, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_raw_504d_slope_v015_signal(ncfo):
    base = _mean(ncfo, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_log_21d_slope_v016_signal(ncfo):
    base = _mean(_log(ncfo), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_log_21d_slope_v017_signal(ncfo):
    base = _mean(_log(ncfo), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_log_21d_slope_v018_signal(ncfo):
    base = _mean(_log(ncfo), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_log_63d_slope_v019_signal(ncfo):
    base = _mean(_log(ncfo), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_log_63d_slope_v020_signal(ncfo):
    base = _mean(_log(ncfo), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_log_63d_slope_v021_signal(ncfo):
    base = _mean(_log(ncfo), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_log_126d_slope_v022_signal(ncfo):
    base = _mean(_log(ncfo), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_log_126d_slope_v023_signal(ncfo):
    base = _mean(_log(ncfo), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_log_126d_slope_v024_signal(ncfo):
    base = _mean(_log(ncfo), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_log_252d_slope_v025_signal(ncfo):
    base = _mean(_log(ncfo), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_log_252d_slope_v026_signal(ncfo):
    base = _mean(_log(ncfo), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_log_252d_slope_v027_signal(ncfo):
    base = _mean(_log(ncfo), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_log_504d_slope_v028_signal(ncfo):
    base = _mean(_log(ncfo), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_log_504d_slope_v029_signal(ncfo):
    base = _mean(_log(ncfo), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_log_504d_slope_v030_signal(ncfo):
    base = _mean(_log(ncfo), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_z_21d_slope_v031_signal(ncfo):
    base = _z(ncfo, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_z_21d_slope_v032_signal(ncfo):
    base = _z(ncfo, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_z_21d_slope_v033_signal(ncfo):
    base = _z(ncfo, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_z_63d_slope_v034_signal(ncfo):
    base = _z(ncfo, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_z_63d_slope_v035_signal(ncfo):
    base = _z(ncfo, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_z_63d_slope_v036_signal(ncfo):
    base = _z(ncfo, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_z_126d_slope_v037_signal(ncfo):
    base = _z(ncfo, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_z_126d_slope_v038_signal(ncfo):
    base = _z(ncfo, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_z_126d_slope_v039_signal(ncfo):
    base = _z(ncfo, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_z_252d_slope_v040_signal(ncfo):
    base = _z(ncfo, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_z_252d_slope_v041_signal(ncfo):
    base = _z(ncfo, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_z_252d_slope_v042_signal(ncfo):
    base = _z(ncfo, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_z_504d_slope_v043_signal(ncfo):
    base = _z(ncfo, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_z_504d_slope_v044_signal(ncfo):
    base = _z(ncfo, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_z_504d_slope_v045_signal(ncfo):
    base = _z(ncfo, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_ps_21d_slope_v046_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_ps_21d_slope_v047_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_ps_21d_slope_v048_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_ps_63d_slope_v049_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_ps_63d_slope_v050_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_ps_63d_slope_v051_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_ps_126d_slope_v052_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_ps_126d_slope_v053_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_ps_126d_slope_v054_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_ps_252d_slope_v055_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_ps_252d_slope_v056_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_ps_252d_slope_v057_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_ps_504d_slope_v058_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_ps_504d_slope_v059_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_ps_504d_slope_v060_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_asset_scaled_21d_slope_v061_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_asset_scaled_21d_slope_v062_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_asset_scaled_21d_slope_v063_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_asset_scaled_63d_slope_v064_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_asset_scaled_63d_slope_v065_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_asset_scaled_63d_slope_v066_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_asset_scaled_126d_slope_v067_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_asset_scaled_126d_slope_v068_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_asset_scaled_126d_slope_v069_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_asset_scaled_252d_slope_v070_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_asset_scaled_252d_slope_v071_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_asset_scaled_252d_slope_v072_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_asset_scaled_504d_slope_v073_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_asset_scaled_504d_slope_v074_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_asset_scaled_504d_slope_v075_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mcap_scaled_21d_slope_v076_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mcap_scaled_21d_slope_v077_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mcap_scaled_21d_slope_v078_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mcap_scaled_63d_slope_v079_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mcap_scaled_63d_slope_v080_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mcap_scaled_63d_slope_v081_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mcap_scaled_126d_slope_v082_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mcap_scaled_126d_slope_v083_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mcap_scaled_126d_slope_v084_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mcap_scaled_252d_slope_v085_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mcap_scaled_252d_slope_v086_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mcap_scaled_252d_slope_v087_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mcap_scaled_504d_slope_v088_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mcap_scaled_504d_slope_v089_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mcap_scaled_504d_slope_v090_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_low_21d_slope_v091_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(21).min(), ncfo.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_low_21d_slope_v092_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(21).min(), ncfo.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_low_21d_slope_v093_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(21).min(), ncfo.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_low_63d_slope_v094_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(63).min(), ncfo.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_low_63d_slope_v095_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(63).min(), ncfo.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_low_63d_slope_v096_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(63).min(), ncfo.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_low_126d_slope_v097_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(126).min(), ncfo.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_low_126d_slope_v098_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(126).min(), ncfo.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_low_126d_slope_v099_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(126).min(), ncfo.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_low_252d_slope_v100_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(252).min(), ncfo.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_low_252d_slope_v101_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(252).min(), ncfo.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_low_252d_slope_v102_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(252).min(), ncfo.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_low_504d_slope_v103_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(504).min(), ncfo.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_low_504d_slope_v104_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(504).min(), ncfo.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_low_504d_slope_v105_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(504).min(), ncfo.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_high_21d_slope_v106_signal(ncfo):
    base = _safe_div(ncfo.rolling(21).max() - ncfo, ncfo.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_high_21d_slope_v107_signal(ncfo):
    base = _safe_div(ncfo.rolling(21).max() - ncfo, ncfo.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_high_21d_slope_v108_signal(ncfo):
    base = _safe_div(ncfo.rolling(21).max() - ncfo, ncfo.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_high_63d_slope_v109_signal(ncfo):
    base = _safe_div(ncfo.rolling(63).max() - ncfo, ncfo.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_high_63d_slope_v110_signal(ncfo):
    base = _safe_div(ncfo.rolling(63).max() - ncfo, ncfo.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_high_63d_slope_v111_signal(ncfo):
    base = _safe_div(ncfo.rolling(63).max() - ncfo, ncfo.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_high_126d_slope_v112_signal(ncfo):
    base = _safe_div(ncfo.rolling(126).max() - ncfo, ncfo.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_high_126d_slope_v113_signal(ncfo):
    base = _safe_div(ncfo.rolling(126).max() - ncfo, ncfo.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_high_126d_slope_v114_signal(ncfo):
    base = _safe_div(ncfo.rolling(126).max() - ncfo, ncfo.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_high_252d_slope_v115_signal(ncfo):
    base = _safe_div(ncfo.rolling(252).max() - ncfo, ncfo.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_high_252d_slope_v116_signal(ncfo):
    base = _safe_div(ncfo.rolling(252).max() - ncfo, ncfo.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_high_252d_slope_v117_signal(ncfo):
    base = _safe_div(ncfo.rolling(252).max() - ncfo, ncfo.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_high_504d_slope_v118_signal(ncfo):
    base = _safe_div(ncfo.rolling(504).max() - ncfo, ncfo.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_high_504d_slope_v119_signal(ncfo):
    base = _safe_div(ncfo.rolling(504).max() - ncfo, ncfo.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_dist_high_504d_slope_v120_signal(ncfo):
    base = _safe_div(ncfo.rolling(504).max() - ncfo, ncfo.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mom_21d_slope_v121_signal(ncfo):
    base = _safe_div(_mean(ncfo, 21) - _mean(ncfo, 42), _mean(ncfo, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mom_21d_slope_v122_signal(ncfo):
    base = _safe_div(_mean(ncfo, 21) - _mean(ncfo, 42), _mean(ncfo, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mom_21d_slope_v123_signal(ncfo):
    base = _safe_div(_mean(ncfo, 21) - _mean(ncfo, 42), _mean(ncfo, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mom_63d_slope_v124_signal(ncfo):
    base = _safe_div(_mean(ncfo, 63) - _mean(ncfo, 126), _mean(ncfo, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mom_63d_slope_v125_signal(ncfo):
    base = _safe_div(_mean(ncfo, 63) - _mean(ncfo, 126), _mean(ncfo, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mom_63d_slope_v126_signal(ncfo):
    base = _safe_div(_mean(ncfo, 63) - _mean(ncfo, 126), _mean(ncfo, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mom_126d_slope_v127_signal(ncfo):
    base = _safe_div(_mean(ncfo, 126) - _mean(ncfo, 252), _mean(ncfo, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mom_126d_slope_v128_signal(ncfo):
    base = _safe_div(_mean(ncfo, 126) - _mean(ncfo, 252), _mean(ncfo, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mom_126d_slope_v129_signal(ncfo):
    base = _safe_div(_mean(ncfo, 126) - _mean(ncfo, 252), _mean(ncfo, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mom_252d_slope_v130_signal(ncfo):
    base = _safe_div(_mean(ncfo, 252) - _mean(ncfo, 504), _mean(ncfo, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mom_252d_slope_v131_signal(ncfo):
    base = _safe_div(_mean(ncfo, 252) - _mean(ncfo, 504), _mean(ncfo, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mom_252d_slope_v132_signal(ncfo):
    base = _safe_div(_mean(ncfo, 252) - _mean(ncfo, 504), _mean(ncfo, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mom_504d_slope_v133_signal(ncfo):
    base = _safe_div(_mean(ncfo, 504) - _mean(ncfo, 1008), _mean(ncfo, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mom_504d_slope_v134_signal(ncfo):
    base = _safe_div(_mean(ncfo, 504) - _mean(ncfo, 1008), _mean(ncfo, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_mom_504d_slope_v135_signal(ncfo):
    base = _safe_div(_mean(ncfo, 504) - _mean(ncfo, 1008), _mean(ncfo, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_vol_21d_slope_v136_signal(ncfo):
    base = _std(ncfo, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_vol_21d_slope_v137_signal(ncfo):
    base = _std(ncfo, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_vol_21d_slope_v138_signal(ncfo):
    base = _std(ncfo, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_vol_63d_slope_v139_signal(ncfo):
    base = _std(ncfo, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_vol_63d_slope_v140_signal(ncfo):
    base = _std(ncfo, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_vol_63d_slope_v141_signal(ncfo):
    base = _std(ncfo, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_vol_126d_slope_v142_signal(ncfo):
    base = _std(ncfo, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_vol_126d_slope_v143_signal(ncfo):
    base = _std(ncfo, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_vol_126d_slope_v144_signal(ncfo):
    base = _std(ncfo, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_vol_252d_slope_v145_signal(ncfo):
    base = _std(ncfo, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_vol_252d_slope_v146_signal(ncfo):
    base = _std(ncfo, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_vol_252d_slope_v147_signal(ncfo):
    base = _std(ncfo, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_vol_504d_slope_v148_signal(ncfo):
    base = _std(ncfo, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_vol_504d_slope_v149_signal(ncfo):
    base = _std(ncfo, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol ncfo
def gm_f11_biotech_f11_operating_cash_burn_rate_vol_504d_slope_v150_signal(ncfo):
    base = _std(ncfo, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

