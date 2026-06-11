
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_raw_21d_slope_v001_signal(cashneq):
    base = _mean(cashneq, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_raw_21d_slope_v002_signal(cashneq):
    base = _mean(cashneq, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_raw_21d_slope_v003_signal(cashneq):
    base = _mean(cashneq, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_raw_63d_slope_v004_signal(cashneq):
    base = _mean(cashneq, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_raw_63d_slope_v005_signal(cashneq):
    base = _mean(cashneq, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_raw_63d_slope_v006_signal(cashneq):
    base = _mean(cashneq, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_raw_126d_slope_v007_signal(cashneq):
    base = _mean(cashneq, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_raw_126d_slope_v008_signal(cashneq):
    base = _mean(cashneq, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_raw_126d_slope_v009_signal(cashneq):
    base = _mean(cashneq, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_raw_252d_slope_v010_signal(cashneq):
    base = _mean(cashneq, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_raw_252d_slope_v011_signal(cashneq):
    base = _mean(cashneq, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_raw_252d_slope_v012_signal(cashneq):
    base = _mean(cashneq, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_raw_504d_slope_v013_signal(cashneq):
    base = _mean(cashneq, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_raw_504d_slope_v014_signal(cashneq):
    base = _mean(cashneq, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_raw_504d_slope_v015_signal(cashneq):
    base = _mean(cashneq, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_log_21d_slope_v016_signal(cashneq):
    base = _mean(_log(cashneq), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_log_21d_slope_v017_signal(cashneq):
    base = _mean(_log(cashneq), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_log_21d_slope_v018_signal(cashneq):
    base = _mean(_log(cashneq), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_log_63d_slope_v019_signal(cashneq):
    base = _mean(_log(cashneq), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_log_63d_slope_v020_signal(cashneq):
    base = _mean(_log(cashneq), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_log_63d_slope_v021_signal(cashneq):
    base = _mean(_log(cashneq), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_log_126d_slope_v022_signal(cashneq):
    base = _mean(_log(cashneq), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_log_126d_slope_v023_signal(cashneq):
    base = _mean(_log(cashneq), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_log_126d_slope_v024_signal(cashneq):
    base = _mean(_log(cashneq), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_log_252d_slope_v025_signal(cashneq):
    base = _mean(_log(cashneq), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_log_252d_slope_v026_signal(cashneq):
    base = _mean(_log(cashneq), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_log_252d_slope_v027_signal(cashneq):
    base = _mean(_log(cashneq), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_log_504d_slope_v028_signal(cashneq):
    base = _mean(_log(cashneq), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_log_504d_slope_v029_signal(cashneq):
    base = _mean(_log(cashneq), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_log_504d_slope_v030_signal(cashneq):
    base = _mean(_log(cashneq), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_z_21d_slope_v031_signal(cashneq):
    base = _z(cashneq, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_z_21d_slope_v032_signal(cashneq):
    base = _z(cashneq, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_z_21d_slope_v033_signal(cashneq):
    base = _z(cashneq, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_z_63d_slope_v034_signal(cashneq):
    base = _z(cashneq, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_z_63d_slope_v035_signal(cashneq):
    base = _z(cashneq, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_z_63d_slope_v036_signal(cashneq):
    base = _z(cashneq, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_z_126d_slope_v037_signal(cashneq):
    base = _z(cashneq, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_z_126d_slope_v038_signal(cashneq):
    base = _z(cashneq, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_z_126d_slope_v039_signal(cashneq):
    base = _z(cashneq, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_z_252d_slope_v040_signal(cashneq):
    base = _z(cashneq, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_z_252d_slope_v041_signal(cashneq):
    base = _z(cashneq, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_z_252d_slope_v042_signal(cashneq):
    base = _z(cashneq, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_z_504d_slope_v043_signal(cashneq):
    base = _z(cashneq, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_z_504d_slope_v044_signal(cashneq):
    base = _z(cashneq, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_z_504d_slope_v045_signal(cashneq):
    base = _z(cashneq, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ps_21d_slope_v046_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ps_21d_slope_v047_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ps_21d_slope_v048_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ps_63d_slope_v049_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ps_63d_slope_v050_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ps_63d_slope_v051_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ps_126d_slope_v052_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ps_126d_slope_v053_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ps_126d_slope_v054_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ps_252d_slope_v055_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ps_252d_slope_v056_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ps_252d_slope_v057_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ps_504d_slope_v058_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ps_504d_slope_v059_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ps_504d_slope_v060_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_asset_scaled_21d_slope_v061_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_asset_scaled_21d_slope_v062_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_asset_scaled_21d_slope_v063_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_asset_scaled_63d_slope_v064_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_asset_scaled_63d_slope_v065_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_asset_scaled_63d_slope_v066_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_asset_scaled_126d_slope_v067_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_asset_scaled_126d_slope_v068_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_asset_scaled_126d_slope_v069_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_asset_scaled_252d_slope_v070_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_asset_scaled_252d_slope_v071_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_asset_scaled_252d_slope_v072_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_asset_scaled_504d_slope_v073_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_asset_scaled_504d_slope_v074_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_asset_scaled_504d_slope_v075_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mcap_scaled_21d_slope_v076_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mcap_scaled_21d_slope_v077_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mcap_scaled_21d_slope_v078_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mcap_scaled_63d_slope_v079_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mcap_scaled_63d_slope_v080_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mcap_scaled_63d_slope_v081_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mcap_scaled_126d_slope_v082_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mcap_scaled_126d_slope_v083_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mcap_scaled_126d_slope_v084_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mcap_scaled_252d_slope_v085_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mcap_scaled_252d_slope_v086_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mcap_scaled_252d_slope_v087_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mcap_scaled_504d_slope_v088_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mcap_scaled_504d_slope_v089_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mcap_scaled_504d_slope_v090_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_low_21d_slope_v091_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(21).min(), cashneq.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_low_21d_slope_v092_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(21).min(), cashneq.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_low_21d_slope_v093_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(21).min(), cashneq.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_low_63d_slope_v094_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(63).min(), cashneq.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_low_63d_slope_v095_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(63).min(), cashneq.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_low_63d_slope_v096_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(63).min(), cashneq.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_low_126d_slope_v097_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(126).min(), cashneq.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_low_126d_slope_v098_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(126).min(), cashneq.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_low_126d_slope_v099_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(126).min(), cashneq.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_low_252d_slope_v100_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(252).min(), cashneq.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_low_252d_slope_v101_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(252).min(), cashneq.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_low_252d_slope_v102_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(252).min(), cashneq.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_low_504d_slope_v103_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(504).min(), cashneq.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_low_504d_slope_v104_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(504).min(), cashneq.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_low_504d_slope_v105_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(504).min(), cashneq.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_high_21d_slope_v106_signal(cashneq):
    base = _safe_div(cashneq.rolling(21).max() - cashneq, cashneq.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_high_21d_slope_v107_signal(cashneq):
    base = _safe_div(cashneq.rolling(21).max() - cashneq, cashneq.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_high_21d_slope_v108_signal(cashneq):
    base = _safe_div(cashneq.rolling(21).max() - cashneq, cashneq.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_high_63d_slope_v109_signal(cashneq):
    base = _safe_div(cashneq.rolling(63).max() - cashneq, cashneq.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_high_63d_slope_v110_signal(cashneq):
    base = _safe_div(cashneq.rolling(63).max() - cashneq, cashneq.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_high_63d_slope_v111_signal(cashneq):
    base = _safe_div(cashneq.rolling(63).max() - cashneq, cashneq.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_high_126d_slope_v112_signal(cashneq):
    base = _safe_div(cashneq.rolling(126).max() - cashneq, cashneq.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_high_126d_slope_v113_signal(cashneq):
    base = _safe_div(cashneq.rolling(126).max() - cashneq, cashneq.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_high_126d_slope_v114_signal(cashneq):
    base = _safe_div(cashneq.rolling(126).max() - cashneq, cashneq.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_high_252d_slope_v115_signal(cashneq):
    base = _safe_div(cashneq.rolling(252).max() - cashneq, cashneq.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_high_252d_slope_v116_signal(cashneq):
    base = _safe_div(cashneq.rolling(252).max() - cashneq, cashneq.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_high_252d_slope_v117_signal(cashneq):
    base = _safe_div(cashneq.rolling(252).max() - cashneq, cashneq.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_high_504d_slope_v118_signal(cashneq):
    base = _safe_div(cashneq.rolling(504).max() - cashneq, cashneq.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_high_504d_slope_v119_signal(cashneq):
    base = _safe_div(cashneq.rolling(504).max() - cashneq, cashneq.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_dist_high_504d_slope_v120_signal(cashneq):
    base = _safe_div(cashneq.rolling(504).max() - cashneq, cashneq.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mom_21d_slope_v121_signal(cashneq):
    base = _safe_div(_mean(cashneq, 21) - _mean(cashneq, 42), _mean(cashneq, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mom_21d_slope_v122_signal(cashneq):
    base = _safe_div(_mean(cashneq, 21) - _mean(cashneq, 42), _mean(cashneq, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mom_21d_slope_v123_signal(cashneq):
    base = _safe_div(_mean(cashneq, 21) - _mean(cashneq, 42), _mean(cashneq, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mom_63d_slope_v124_signal(cashneq):
    base = _safe_div(_mean(cashneq, 63) - _mean(cashneq, 126), _mean(cashneq, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mom_63d_slope_v125_signal(cashneq):
    base = _safe_div(_mean(cashneq, 63) - _mean(cashneq, 126), _mean(cashneq, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mom_63d_slope_v126_signal(cashneq):
    base = _safe_div(_mean(cashneq, 63) - _mean(cashneq, 126), _mean(cashneq, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mom_126d_slope_v127_signal(cashneq):
    base = _safe_div(_mean(cashneq, 126) - _mean(cashneq, 252), _mean(cashneq, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mom_126d_slope_v128_signal(cashneq):
    base = _safe_div(_mean(cashneq, 126) - _mean(cashneq, 252), _mean(cashneq, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mom_126d_slope_v129_signal(cashneq):
    base = _safe_div(_mean(cashneq, 126) - _mean(cashneq, 252), _mean(cashneq, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mom_252d_slope_v130_signal(cashneq):
    base = _safe_div(_mean(cashneq, 252) - _mean(cashneq, 504), _mean(cashneq, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mom_252d_slope_v131_signal(cashneq):
    base = _safe_div(_mean(cashneq, 252) - _mean(cashneq, 504), _mean(cashneq, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mom_252d_slope_v132_signal(cashneq):
    base = _safe_div(_mean(cashneq, 252) - _mean(cashneq, 504), _mean(cashneq, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mom_504d_slope_v133_signal(cashneq):
    base = _safe_div(_mean(cashneq, 504) - _mean(cashneq, 1008), _mean(cashneq, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mom_504d_slope_v134_signal(cashneq):
    base = _safe_div(_mean(cashneq, 504) - _mean(cashneq, 1008), _mean(cashneq, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mom_504d_slope_v135_signal(cashneq):
    base = _safe_div(_mean(cashneq, 504) - _mean(cashneq, 1008), _mean(cashneq, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_vol_21d_slope_v136_signal(cashneq):
    base = _std(cashneq, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_vol_21d_slope_v137_signal(cashneq):
    base = _std(cashneq, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_vol_21d_slope_v138_signal(cashneq):
    base = _std(cashneq, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_vol_63d_slope_v139_signal(cashneq):
    base = _std(cashneq, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_vol_63d_slope_v140_signal(cashneq):
    base = _std(cashneq, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_vol_63d_slope_v141_signal(cashneq):
    base = _std(cashneq, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_vol_126d_slope_v142_signal(cashneq):
    base = _std(cashneq, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_vol_126d_slope_v143_signal(cashneq):
    base = _std(cashneq, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_vol_126d_slope_v144_signal(cashneq):
    base = _std(cashneq, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_vol_252d_slope_v145_signal(cashneq):
    base = _std(cashneq, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_vol_252d_slope_v146_signal(cashneq):
    base = _std(cashneq, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_vol_252d_slope_v147_signal(cashneq):
    base = _std(cashneq, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_vol_504d_slope_v148_signal(cashneq):
    base = _std(cashneq, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_vol_504d_slope_v149_signal(cashneq):
    base = _std(cashneq, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_vol_504d_slope_v150_signal(cashneq):
    base = _std(cashneq, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

