
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_raw_21d_accel_v001_signal(marketcap):
    base = _mean(marketcap, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_raw_21d_accel_v002_signal(marketcap):
    base = _mean(marketcap, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_raw_21d_accel_v003_signal(marketcap):
    base = _mean(marketcap, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_raw_63d_accel_v004_signal(marketcap):
    base = _mean(marketcap, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_raw_63d_accel_v005_signal(marketcap):
    base = _mean(marketcap, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_raw_63d_accel_v006_signal(marketcap):
    base = _mean(marketcap, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_raw_126d_accel_v007_signal(marketcap):
    base = _mean(marketcap, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_raw_126d_accel_v008_signal(marketcap):
    base = _mean(marketcap, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_raw_126d_accel_v009_signal(marketcap):
    base = _mean(marketcap, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_raw_252d_accel_v010_signal(marketcap):
    base = _mean(marketcap, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_raw_252d_accel_v011_signal(marketcap):
    base = _mean(marketcap, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_raw_252d_accel_v012_signal(marketcap):
    base = _mean(marketcap, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_raw_504d_accel_v013_signal(marketcap):
    base = _mean(marketcap, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_raw_504d_accel_v014_signal(marketcap):
    base = _mean(marketcap, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_raw_504d_accel_v015_signal(marketcap):
    base = _mean(marketcap, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_log_21d_accel_v016_signal(marketcap):
    base = _mean(_log(marketcap), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_log_21d_accel_v017_signal(marketcap):
    base = _mean(_log(marketcap), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_log_21d_accel_v018_signal(marketcap):
    base = _mean(_log(marketcap), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_log_63d_accel_v019_signal(marketcap):
    base = _mean(_log(marketcap), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_log_63d_accel_v020_signal(marketcap):
    base = _mean(_log(marketcap), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_log_63d_accel_v021_signal(marketcap):
    base = _mean(_log(marketcap), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_log_126d_accel_v022_signal(marketcap):
    base = _mean(_log(marketcap), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_log_126d_accel_v023_signal(marketcap):
    base = _mean(_log(marketcap), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_log_126d_accel_v024_signal(marketcap):
    base = _mean(_log(marketcap), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_log_252d_accel_v025_signal(marketcap):
    base = _mean(_log(marketcap), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_log_252d_accel_v026_signal(marketcap):
    base = _mean(_log(marketcap), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_log_252d_accel_v027_signal(marketcap):
    base = _mean(_log(marketcap), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_log_504d_accel_v028_signal(marketcap):
    base = _mean(_log(marketcap), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_log_504d_accel_v029_signal(marketcap):
    base = _mean(_log(marketcap), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_log_504d_accel_v030_signal(marketcap):
    base = _mean(_log(marketcap), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_z_21d_accel_v031_signal(marketcap):
    base = _z(marketcap, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_z_21d_accel_v032_signal(marketcap):
    base = _z(marketcap, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_z_21d_accel_v033_signal(marketcap):
    base = _z(marketcap, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_z_63d_accel_v034_signal(marketcap):
    base = _z(marketcap, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_z_63d_accel_v035_signal(marketcap):
    base = _z(marketcap, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_z_63d_accel_v036_signal(marketcap):
    base = _z(marketcap, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_z_126d_accel_v037_signal(marketcap):
    base = _z(marketcap, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_z_126d_accel_v038_signal(marketcap):
    base = _z(marketcap, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_z_126d_accel_v039_signal(marketcap):
    base = _z(marketcap, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_z_252d_accel_v040_signal(marketcap):
    base = _z(marketcap, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_z_252d_accel_v041_signal(marketcap):
    base = _z(marketcap, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_z_252d_accel_v042_signal(marketcap):
    base = _z(marketcap, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_z_504d_accel_v043_signal(marketcap):
    base = _z(marketcap, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_z_504d_accel_v044_signal(marketcap):
    base = _z(marketcap, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_z_504d_accel_v045_signal(marketcap):
    base = _z(marketcap, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_ps_21d_accel_v046_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_ps_21d_accel_v047_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_ps_21d_accel_v048_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_ps_63d_accel_v049_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_ps_63d_accel_v050_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_ps_63d_accel_v051_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_ps_126d_accel_v052_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_ps_126d_accel_v053_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_ps_126d_accel_v054_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_ps_252d_accel_v055_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_ps_252d_accel_v056_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_ps_252d_accel_v057_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_ps_504d_accel_v058_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_ps_504d_accel_v059_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_ps_504d_accel_v060_signal(marketcap, sharesbas):
    base = _safe_div(_mean(marketcap, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_21d_accel_v061_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_21d_accel_v062_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_21d_accel_v063_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_63d_accel_v064_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_63d_accel_v065_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_63d_accel_v066_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_126d_accel_v067_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_126d_accel_v068_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_126d_accel_v069_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_252d_accel_v070_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_252d_accel_v071_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_252d_accel_v072_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_504d_accel_v073_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_504d_accel_v074_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_asset_scaled_504d_accel_v075_signal(marketcap, assets):
    base = _safe_div(_mean(marketcap, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_21d_accel_v076_signal(marketcap):
    base = _safe_div(_mean(marketcap, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_21d_accel_v077_signal(marketcap):
    base = _safe_div(_mean(marketcap, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_21d_accel_v078_signal(marketcap):
    base = _safe_div(_mean(marketcap, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_63d_accel_v079_signal(marketcap):
    base = _safe_div(_mean(marketcap, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_63d_accel_v080_signal(marketcap):
    base = _safe_div(_mean(marketcap, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_63d_accel_v081_signal(marketcap):
    base = _safe_div(_mean(marketcap, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_126d_accel_v082_signal(marketcap):
    base = _safe_div(_mean(marketcap, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_126d_accel_v083_signal(marketcap):
    base = _safe_div(_mean(marketcap, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_126d_accel_v084_signal(marketcap):
    base = _safe_div(_mean(marketcap, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_252d_accel_v085_signal(marketcap):
    base = _safe_div(_mean(marketcap, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_252d_accel_v086_signal(marketcap):
    base = _safe_div(_mean(marketcap, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_252d_accel_v087_signal(marketcap):
    base = _safe_div(_mean(marketcap, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_504d_accel_v088_signal(marketcap):
    base = _safe_div(_mean(marketcap, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_504d_accel_v089_signal(marketcap):
    base = _safe_div(_mean(marketcap, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mcap_scaled_504d_accel_v090_signal(marketcap):
    base = _safe_div(_mean(marketcap, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_21d_accel_v091_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(21).min(), marketcap.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_21d_accel_v092_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(21).min(), marketcap.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_21d_accel_v093_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(21).min(), marketcap.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_63d_accel_v094_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(63).min(), marketcap.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_63d_accel_v095_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(63).min(), marketcap.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_63d_accel_v096_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(63).min(), marketcap.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_126d_accel_v097_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(126).min(), marketcap.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_126d_accel_v098_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(126).min(), marketcap.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_126d_accel_v099_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(126).min(), marketcap.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_252d_accel_v100_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(252).min(), marketcap.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_252d_accel_v101_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(252).min(), marketcap.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_252d_accel_v102_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(252).min(), marketcap.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_504d_accel_v103_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(504).min(), marketcap.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_504d_accel_v104_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(504).min(), marketcap.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_low_504d_accel_v105_signal(marketcap):
    base = _safe_div(marketcap - marketcap.rolling(504).min(), marketcap.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_21d_accel_v106_signal(marketcap):
    base = _safe_div(marketcap.rolling(21).max() - marketcap, marketcap.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_21d_accel_v107_signal(marketcap):
    base = _safe_div(marketcap.rolling(21).max() - marketcap, marketcap.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_21d_accel_v108_signal(marketcap):
    base = _safe_div(marketcap.rolling(21).max() - marketcap, marketcap.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_63d_accel_v109_signal(marketcap):
    base = _safe_div(marketcap.rolling(63).max() - marketcap, marketcap.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_63d_accel_v110_signal(marketcap):
    base = _safe_div(marketcap.rolling(63).max() - marketcap, marketcap.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_63d_accel_v111_signal(marketcap):
    base = _safe_div(marketcap.rolling(63).max() - marketcap, marketcap.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_126d_accel_v112_signal(marketcap):
    base = _safe_div(marketcap.rolling(126).max() - marketcap, marketcap.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_126d_accel_v113_signal(marketcap):
    base = _safe_div(marketcap.rolling(126).max() - marketcap, marketcap.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_126d_accel_v114_signal(marketcap):
    base = _safe_div(marketcap.rolling(126).max() - marketcap, marketcap.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_252d_accel_v115_signal(marketcap):
    base = _safe_div(marketcap.rolling(252).max() - marketcap, marketcap.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_252d_accel_v116_signal(marketcap):
    base = _safe_div(marketcap.rolling(252).max() - marketcap, marketcap.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_252d_accel_v117_signal(marketcap):
    base = _safe_div(marketcap.rolling(252).max() - marketcap, marketcap.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_504d_accel_v118_signal(marketcap):
    base = _safe_div(marketcap.rolling(504).max() - marketcap, marketcap.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_504d_accel_v119_signal(marketcap):
    base = _safe_div(marketcap.rolling(504).max() - marketcap, marketcap.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_dist_high_504d_accel_v120_signal(marketcap):
    base = _safe_div(marketcap.rolling(504).max() - marketcap, marketcap.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mom_21d_accel_v121_signal(marketcap):
    base = _safe_div(_mean(marketcap, 21) - _mean(marketcap, 42), _mean(marketcap, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mom_21d_accel_v122_signal(marketcap):
    base = _safe_div(_mean(marketcap, 21) - _mean(marketcap, 42), _mean(marketcap, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mom_21d_accel_v123_signal(marketcap):
    base = _safe_div(_mean(marketcap, 21) - _mean(marketcap, 42), _mean(marketcap, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mom_63d_accel_v124_signal(marketcap):
    base = _safe_div(_mean(marketcap, 63) - _mean(marketcap, 126), _mean(marketcap, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mom_63d_accel_v125_signal(marketcap):
    base = _safe_div(_mean(marketcap, 63) - _mean(marketcap, 126), _mean(marketcap, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mom_63d_accel_v126_signal(marketcap):
    base = _safe_div(_mean(marketcap, 63) - _mean(marketcap, 126), _mean(marketcap, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mom_126d_accel_v127_signal(marketcap):
    base = _safe_div(_mean(marketcap, 126) - _mean(marketcap, 252), _mean(marketcap, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mom_126d_accel_v128_signal(marketcap):
    base = _safe_div(_mean(marketcap, 126) - _mean(marketcap, 252), _mean(marketcap, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mom_126d_accel_v129_signal(marketcap):
    base = _safe_div(_mean(marketcap, 126) - _mean(marketcap, 252), _mean(marketcap, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mom_252d_accel_v130_signal(marketcap):
    base = _safe_div(_mean(marketcap, 252) - _mean(marketcap, 504), _mean(marketcap, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mom_252d_accel_v131_signal(marketcap):
    base = _safe_div(_mean(marketcap, 252) - _mean(marketcap, 504), _mean(marketcap, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mom_252d_accel_v132_signal(marketcap):
    base = _safe_div(_mean(marketcap, 252) - _mean(marketcap, 504), _mean(marketcap, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mom_504d_accel_v133_signal(marketcap):
    base = _safe_div(_mean(marketcap, 504) - _mean(marketcap, 1008), _mean(marketcap, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mom_504d_accel_v134_signal(marketcap):
    base = _safe_div(_mean(marketcap, 504) - _mean(marketcap, 1008), _mean(marketcap, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_mom_504d_accel_v135_signal(marketcap):
    base = _safe_div(_mean(marketcap, 504) - _mean(marketcap, 1008), _mean(marketcap, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_vol_21d_accel_v136_signal(marketcap):
    base = _std(marketcap, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_vol_21d_accel_v137_signal(marketcap):
    base = _std(marketcap, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_vol_21d_accel_v138_signal(marketcap):
    base = _std(marketcap, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_vol_63d_accel_v139_signal(marketcap):
    base = _std(marketcap, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_vol_63d_accel_v140_signal(marketcap):
    base = _std(marketcap, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_vol_63d_accel_v141_signal(marketcap):
    base = _std(marketcap, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_vol_126d_accel_v142_signal(marketcap):
    base = _std(marketcap, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_vol_126d_accel_v143_signal(marketcap):
    base = _std(marketcap, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_vol_126d_accel_v144_signal(marketcap):
    base = _std(marketcap, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_vol_252d_accel_v145_signal(marketcap):
    base = _std(marketcap, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_vol_252d_accel_v146_signal(marketcap):
    base = _std(marketcap, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_vol_252d_accel_v147_signal(marketcap):
    base = _std(marketcap, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_vol_504d_accel_v148_signal(marketcap):
    base = _std(marketcap, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_vol_504d_accel_v149_signal(marketcap):
    base = _std(marketcap, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol marketcap
def gm_f79_biotech_f79_price_to_cash_ratio_vol_504d_accel_v150_signal(marketcap):
    base = _std(marketcap, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

