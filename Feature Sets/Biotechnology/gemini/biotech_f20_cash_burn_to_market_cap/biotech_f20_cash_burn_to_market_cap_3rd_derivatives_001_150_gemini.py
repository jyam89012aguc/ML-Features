
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_raw_21d_accel_v001_signal(ncfo):
    base = _mean(ncfo, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_raw_21d_accel_v002_signal(ncfo):
    base = _mean(ncfo, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_raw_21d_accel_v003_signal(ncfo):
    base = _mean(ncfo, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_raw_63d_accel_v004_signal(ncfo):
    base = _mean(ncfo, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_raw_63d_accel_v005_signal(ncfo):
    base = _mean(ncfo, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_raw_63d_accel_v006_signal(ncfo):
    base = _mean(ncfo, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_raw_126d_accel_v007_signal(ncfo):
    base = _mean(ncfo, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_raw_126d_accel_v008_signal(ncfo):
    base = _mean(ncfo, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_raw_126d_accel_v009_signal(ncfo):
    base = _mean(ncfo, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_raw_252d_accel_v010_signal(ncfo):
    base = _mean(ncfo, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_raw_252d_accel_v011_signal(ncfo):
    base = _mean(ncfo, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_raw_252d_accel_v012_signal(ncfo):
    base = _mean(ncfo, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_raw_504d_accel_v013_signal(ncfo):
    base = _mean(ncfo, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_raw_504d_accel_v014_signal(ncfo):
    base = _mean(ncfo, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_raw_504d_accel_v015_signal(ncfo):
    base = _mean(ncfo, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_log_21d_accel_v016_signal(ncfo):
    base = _mean(_log(ncfo), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_log_21d_accel_v017_signal(ncfo):
    base = _mean(_log(ncfo), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_log_21d_accel_v018_signal(ncfo):
    base = _mean(_log(ncfo), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_log_63d_accel_v019_signal(ncfo):
    base = _mean(_log(ncfo), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_log_63d_accel_v020_signal(ncfo):
    base = _mean(_log(ncfo), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_log_63d_accel_v021_signal(ncfo):
    base = _mean(_log(ncfo), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_log_126d_accel_v022_signal(ncfo):
    base = _mean(_log(ncfo), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_log_126d_accel_v023_signal(ncfo):
    base = _mean(_log(ncfo), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_log_126d_accel_v024_signal(ncfo):
    base = _mean(_log(ncfo), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_log_252d_accel_v025_signal(ncfo):
    base = _mean(_log(ncfo), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_log_252d_accel_v026_signal(ncfo):
    base = _mean(_log(ncfo), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_log_252d_accel_v027_signal(ncfo):
    base = _mean(_log(ncfo), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_log_504d_accel_v028_signal(ncfo):
    base = _mean(_log(ncfo), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_log_504d_accel_v029_signal(ncfo):
    base = _mean(_log(ncfo), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_log_504d_accel_v030_signal(ncfo):
    base = _mean(_log(ncfo), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_z_21d_accel_v031_signal(ncfo):
    base = _z(ncfo, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_z_21d_accel_v032_signal(ncfo):
    base = _z(ncfo, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_z_21d_accel_v033_signal(ncfo):
    base = _z(ncfo, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_z_63d_accel_v034_signal(ncfo):
    base = _z(ncfo, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_z_63d_accel_v035_signal(ncfo):
    base = _z(ncfo, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_z_63d_accel_v036_signal(ncfo):
    base = _z(ncfo, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_z_126d_accel_v037_signal(ncfo):
    base = _z(ncfo, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_z_126d_accel_v038_signal(ncfo):
    base = _z(ncfo, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_z_126d_accel_v039_signal(ncfo):
    base = _z(ncfo, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_z_252d_accel_v040_signal(ncfo):
    base = _z(ncfo, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_z_252d_accel_v041_signal(ncfo):
    base = _z(ncfo, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_z_252d_accel_v042_signal(ncfo):
    base = _z(ncfo, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_z_504d_accel_v043_signal(ncfo):
    base = _z(ncfo, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_z_504d_accel_v044_signal(ncfo):
    base = _z(ncfo, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_z_504d_accel_v045_signal(ncfo):
    base = _z(ncfo, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_ps_21d_accel_v046_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_ps_21d_accel_v047_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_ps_21d_accel_v048_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_ps_63d_accel_v049_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_ps_63d_accel_v050_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_ps_63d_accel_v051_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_ps_126d_accel_v052_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_ps_126d_accel_v053_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_ps_126d_accel_v054_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_ps_252d_accel_v055_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_ps_252d_accel_v056_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_ps_252d_accel_v057_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_ps_504d_accel_v058_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_ps_504d_accel_v059_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_ps_504d_accel_v060_signal(ncfo, sharesbas):
    base = _safe_div(_mean(ncfo, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_asset_scaled_21d_accel_v061_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_asset_scaled_21d_accel_v062_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_asset_scaled_21d_accel_v063_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_asset_scaled_63d_accel_v064_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_asset_scaled_63d_accel_v065_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_asset_scaled_63d_accel_v066_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_asset_scaled_126d_accel_v067_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_asset_scaled_126d_accel_v068_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_asset_scaled_126d_accel_v069_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_asset_scaled_252d_accel_v070_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_asset_scaled_252d_accel_v071_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_asset_scaled_252d_accel_v072_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_asset_scaled_504d_accel_v073_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_asset_scaled_504d_accel_v074_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_asset_scaled_504d_accel_v075_signal(ncfo, assets):
    base = _safe_div(_mean(ncfo, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mcap_scaled_21d_accel_v076_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mcap_scaled_21d_accel_v077_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mcap_scaled_21d_accel_v078_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mcap_scaled_63d_accel_v079_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mcap_scaled_63d_accel_v080_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mcap_scaled_63d_accel_v081_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mcap_scaled_126d_accel_v082_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mcap_scaled_126d_accel_v083_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mcap_scaled_126d_accel_v084_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mcap_scaled_252d_accel_v085_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mcap_scaled_252d_accel_v086_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mcap_scaled_252d_accel_v087_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mcap_scaled_504d_accel_v088_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mcap_scaled_504d_accel_v089_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mcap_scaled_504d_accel_v090_signal(ncfo, marketcap):
    base = _safe_div(_mean(ncfo, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_low_21d_accel_v091_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(21).min(), ncfo.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_low_21d_accel_v092_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(21).min(), ncfo.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_low_21d_accel_v093_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(21).min(), ncfo.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_low_63d_accel_v094_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(63).min(), ncfo.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_low_63d_accel_v095_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(63).min(), ncfo.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_low_63d_accel_v096_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(63).min(), ncfo.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_low_126d_accel_v097_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(126).min(), ncfo.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_low_126d_accel_v098_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(126).min(), ncfo.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_low_126d_accel_v099_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(126).min(), ncfo.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_low_252d_accel_v100_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(252).min(), ncfo.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_low_252d_accel_v101_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(252).min(), ncfo.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_low_252d_accel_v102_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(252).min(), ncfo.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_low_504d_accel_v103_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(504).min(), ncfo.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_low_504d_accel_v104_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(504).min(), ncfo.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_low_504d_accel_v105_signal(ncfo):
    base = _safe_div(ncfo - ncfo.rolling(504).min(), ncfo.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_high_21d_accel_v106_signal(ncfo):
    base = _safe_div(ncfo.rolling(21).max() - ncfo, ncfo.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_high_21d_accel_v107_signal(ncfo):
    base = _safe_div(ncfo.rolling(21).max() - ncfo, ncfo.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_high_21d_accel_v108_signal(ncfo):
    base = _safe_div(ncfo.rolling(21).max() - ncfo, ncfo.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_high_63d_accel_v109_signal(ncfo):
    base = _safe_div(ncfo.rolling(63).max() - ncfo, ncfo.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_high_63d_accel_v110_signal(ncfo):
    base = _safe_div(ncfo.rolling(63).max() - ncfo, ncfo.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_high_63d_accel_v111_signal(ncfo):
    base = _safe_div(ncfo.rolling(63).max() - ncfo, ncfo.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_high_126d_accel_v112_signal(ncfo):
    base = _safe_div(ncfo.rolling(126).max() - ncfo, ncfo.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_high_126d_accel_v113_signal(ncfo):
    base = _safe_div(ncfo.rolling(126).max() - ncfo, ncfo.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_high_126d_accel_v114_signal(ncfo):
    base = _safe_div(ncfo.rolling(126).max() - ncfo, ncfo.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_high_252d_accel_v115_signal(ncfo):
    base = _safe_div(ncfo.rolling(252).max() - ncfo, ncfo.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_high_252d_accel_v116_signal(ncfo):
    base = _safe_div(ncfo.rolling(252).max() - ncfo, ncfo.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_high_252d_accel_v117_signal(ncfo):
    base = _safe_div(ncfo.rolling(252).max() - ncfo, ncfo.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_high_504d_accel_v118_signal(ncfo):
    base = _safe_div(ncfo.rolling(504).max() - ncfo, ncfo.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_high_504d_accel_v119_signal(ncfo):
    base = _safe_div(ncfo.rolling(504).max() - ncfo, ncfo.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_dist_high_504d_accel_v120_signal(ncfo):
    base = _safe_div(ncfo.rolling(504).max() - ncfo, ncfo.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mom_21d_accel_v121_signal(ncfo):
    base = _safe_div(_mean(ncfo, 21) - _mean(ncfo, 42), _mean(ncfo, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mom_21d_accel_v122_signal(ncfo):
    base = _safe_div(_mean(ncfo, 21) - _mean(ncfo, 42), _mean(ncfo, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mom_21d_accel_v123_signal(ncfo):
    base = _safe_div(_mean(ncfo, 21) - _mean(ncfo, 42), _mean(ncfo, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mom_63d_accel_v124_signal(ncfo):
    base = _safe_div(_mean(ncfo, 63) - _mean(ncfo, 126), _mean(ncfo, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mom_63d_accel_v125_signal(ncfo):
    base = _safe_div(_mean(ncfo, 63) - _mean(ncfo, 126), _mean(ncfo, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mom_63d_accel_v126_signal(ncfo):
    base = _safe_div(_mean(ncfo, 63) - _mean(ncfo, 126), _mean(ncfo, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mom_126d_accel_v127_signal(ncfo):
    base = _safe_div(_mean(ncfo, 126) - _mean(ncfo, 252), _mean(ncfo, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mom_126d_accel_v128_signal(ncfo):
    base = _safe_div(_mean(ncfo, 126) - _mean(ncfo, 252), _mean(ncfo, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mom_126d_accel_v129_signal(ncfo):
    base = _safe_div(_mean(ncfo, 126) - _mean(ncfo, 252), _mean(ncfo, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mom_252d_accel_v130_signal(ncfo):
    base = _safe_div(_mean(ncfo, 252) - _mean(ncfo, 504), _mean(ncfo, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mom_252d_accel_v131_signal(ncfo):
    base = _safe_div(_mean(ncfo, 252) - _mean(ncfo, 504), _mean(ncfo, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mom_252d_accel_v132_signal(ncfo):
    base = _safe_div(_mean(ncfo, 252) - _mean(ncfo, 504), _mean(ncfo, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mom_504d_accel_v133_signal(ncfo):
    base = _safe_div(_mean(ncfo, 504) - _mean(ncfo, 1008), _mean(ncfo, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mom_504d_accel_v134_signal(ncfo):
    base = _safe_div(_mean(ncfo, 504) - _mean(ncfo, 1008), _mean(ncfo, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_mom_504d_accel_v135_signal(ncfo):
    base = _safe_div(_mean(ncfo, 504) - _mean(ncfo, 1008), _mean(ncfo, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_vol_21d_accel_v136_signal(ncfo):
    base = _std(ncfo, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_vol_21d_accel_v137_signal(ncfo):
    base = _std(ncfo, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_vol_21d_accel_v138_signal(ncfo):
    base = _std(ncfo, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_vol_63d_accel_v139_signal(ncfo):
    base = _std(ncfo, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_vol_63d_accel_v140_signal(ncfo):
    base = _std(ncfo, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_vol_63d_accel_v141_signal(ncfo):
    base = _std(ncfo, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_vol_126d_accel_v142_signal(ncfo):
    base = _std(ncfo, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_vol_126d_accel_v143_signal(ncfo):
    base = _std(ncfo, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_vol_126d_accel_v144_signal(ncfo):
    base = _std(ncfo, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_vol_252d_accel_v145_signal(ncfo):
    base = _std(ncfo, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_vol_252d_accel_v146_signal(ncfo):
    base = _std(ncfo, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_vol_252d_accel_v147_signal(ncfo):
    base = _std(ncfo, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_vol_504d_accel_v148_signal(ncfo):
    base = _std(ncfo, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_vol_504d_accel_v149_signal(ncfo):
    base = _std(ncfo, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol ncfo
def gm_f20_biotech_f20_cash_burn_to_market_cap_vol_504d_accel_v150_signal(ncfo):
    base = _std(ncfo, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

