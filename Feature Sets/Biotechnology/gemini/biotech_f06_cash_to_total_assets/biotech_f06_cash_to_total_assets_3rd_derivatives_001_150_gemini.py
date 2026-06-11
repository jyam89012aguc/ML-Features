
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw cashneq
def gm_f06_biotech_f06_cash_to_total_assets_raw_21d_accel_v001_signal(cashneq):
    base = _mean(cashneq, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw cashneq
def gm_f06_biotech_f06_cash_to_total_assets_raw_21d_accel_v002_signal(cashneq):
    base = _mean(cashneq, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw cashneq
def gm_f06_biotech_f06_cash_to_total_assets_raw_21d_accel_v003_signal(cashneq):
    base = _mean(cashneq, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw cashneq
def gm_f06_biotech_f06_cash_to_total_assets_raw_63d_accel_v004_signal(cashneq):
    base = _mean(cashneq, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw cashneq
def gm_f06_biotech_f06_cash_to_total_assets_raw_63d_accel_v005_signal(cashneq):
    base = _mean(cashneq, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw cashneq
def gm_f06_biotech_f06_cash_to_total_assets_raw_63d_accel_v006_signal(cashneq):
    base = _mean(cashneq, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw cashneq
def gm_f06_biotech_f06_cash_to_total_assets_raw_126d_accel_v007_signal(cashneq):
    base = _mean(cashneq, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw cashneq
def gm_f06_biotech_f06_cash_to_total_assets_raw_126d_accel_v008_signal(cashneq):
    base = _mean(cashneq, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw cashneq
def gm_f06_biotech_f06_cash_to_total_assets_raw_126d_accel_v009_signal(cashneq):
    base = _mean(cashneq, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw cashneq
def gm_f06_biotech_f06_cash_to_total_assets_raw_252d_accel_v010_signal(cashneq):
    base = _mean(cashneq, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw cashneq
def gm_f06_biotech_f06_cash_to_total_assets_raw_252d_accel_v011_signal(cashneq):
    base = _mean(cashneq, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw cashneq
def gm_f06_biotech_f06_cash_to_total_assets_raw_252d_accel_v012_signal(cashneq):
    base = _mean(cashneq, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw cashneq
def gm_f06_biotech_f06_cash_to_total_assets_raw_504d_accel_v013_signal(cashneq):
    base = _mean(cashneq, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw cashneq
def gm_f06_biotech_f06_cash_to_total_assets_raw_504d_accel_v014_signal(cashneq):
    base = _mean(cashneq, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw cashneq
def gm_f06_biotech_f06_cash_to_total_assets_raw_504d_accel_v015_signal(cashneq):
    base = _mean(cashneq, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log cashneq
def gm_f06_biotech_f06_cash_to_total_assets_log_21d_accel_v016_signal(cashneq):
    base = _mean(_log(cashneq), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log cashneq
def gm_f06_biotech_f06_cash_to_total_assets_log_21d_accel_v017_signal(cashneq):
    base = _mean(_log(cashneq), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log cashneq
def gm_f06_biotech_f06_cash_to_total_assets_log_21d_accel_v018_signal(cashneq):
    base = _mean(_log(cashneq), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log cashneq
def gm_f06_biotech_f06_cash_to_total_assets_log_63d_accel_v019_signal(cashneq):
    base = _mean(_log(cashneq), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log cashneq
def gm_f06_biotech_f06_cash_to_total_assets_log_63d_accel_v020_signal(cashneq):
    base = _mean(_log(cashneq), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log cashneq
def gm_f06_biotech_f06_cash_to_total_assets_log_63d_accel_v021_signal(cashneq):
    base = _mean(_log(cashneq), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log cashneq
def gm_f06_biotech_f06_cash_to_total_assets_log_126d_accel_v022_signal(cashneq):
    base = _mean(_log(cashneq), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log cashneq
def gm_f06_biotech_f06_cash_to_total_assets_log_126d_accel_v023_signal(cashneq):
    base = _mean(_log(cashneq), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log cashneq
def gm_f06_biotech_f06_cash_to_total_assets_log_126d_accel_v024_signal(cashneq):
    base = _mean(_log(cashneq), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log cashneq
def gm_f06_biotech_f06_cash_to_total_assets_log_252d_accel_v025_signal(cashneq):
    base = _mean(_log(cashneq), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log cashneq
def gm_f06_biotech_f06_cash_to_total_assets_log_252d_accel_v026_signal(cashneq):
    base = _mean(_log(cashneq), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log cashneq
def gm_f06_biotech_f06_cash_to_total_assets_log_252d_accel_v027_signal(cashneq):
    base = _mean(_log(cashneq), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log cashneq
def gm_f06_biotech_f06_cash_to_total_assets_log_504d_accel_v028_signal(cashneq):
    base = _mean(_log(cashneq), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log cashneq
def gm_f06_biotech_f06_cash_to_total_assets_log_504d_accel_v029_signal(cashneq):
    base = _mean(_log(cashneq), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log cashneq
def gm_f06_biotech_f06_cash_to_total_assets_log_504d_accel_v030_signal(cashneq):
    base = _mean(_log(cashneq), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z cashneq
def gm_f06_biotech_f06_cash_to_total_assets_z_21d_accel_v031_signal(cashneq):
    base = _z(cashneq, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z cashneq
def gm_f06_biotech_f06_cash_to_total_assets_z_21d_accel_v032_signal(cashneq):
    base = _z(cashneq, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z cashneq
def gm_f06_biotech_f06_cash_to_total_assets_z_21d_accel_v033_signal(cashneq):
    base = _z(cashneq, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z cashneq
def gm_f06_biotech_f06_cash_to_total_assets_z_63d_accel_v034_signal(cashneq):
    base = _z(cashneq, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z cashneq
def gm_f06_biotech_f06_cash_to_total_assets_z_63d_accel_v035_signal(cashneq):
    base = _z(cashneq, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z cashneq
def gm_f06_biotech_f06_cash_to_total_assets_z_63d_accel_v036_signal(cashneq):
    base = _z(cashneq, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z cashneq
def gm_f06_biotech_f06_cash_to_total_assets_z_126d_accel_v037_signal(cashneq):
    base = _z(cashneq, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z cashneq
def gm_f06_biotech_f06_cash_to_total_assets_z_126d_accel_v038_signal(cashneq):
    base = _z(cashneq, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z cashneq
def gm_f06_biotech_f06_cash_to_total_assets_z_126d_accel_v039_signal(cashneq):
    base = _z(cashneq, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z cashneq
def gm_f06_biotech_f06_cash_to_total_assets_z_252d_accel_v040_signal(cashneq):
    base = _z(cashneq, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z cashneq
def gm_f06_biotech_f06_cash_to_total_assets_z_252d_accel_v041_signal(cashneq):
    base = _z(cashneq, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z cashneq
def gm_f06_biotech_f06_cash_to_total_assets_z_252d_accel_v042_signal(cashneq):
    base = _z(cashneq, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z cashneq
def gm_f06_biotech_f06_cash_to_total_assets_z_504d_accel_v043_signal(cashneq):
    base = _z(cashneq, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z cashneq
def gm_f06_biotech_f06_cash_to_total_assets_z_504d_accel_v044_signal(cashneq):
    base = _z(cashneq, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z cashneq
def gm_f06_biotech_f06_cash_to_total_assets_z_504d_accel_v045_signal(cashneq):
    base = _z(cashneq, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps cashneq
def gm_f06_biotech_f06_cash_to_total_assets_ps_21d_accel_v046_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps cashneq
def gm_f06_biotech_f06_cash_to_total_assets_ps_21d_accel_v047_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps cashneq
def gm_f06_biotech_f06_cash_to_total_assets_ps_21d_accel_v048_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps cashneq
def gm_f06_biotech_f06_cash_to_total_assets_ps_63d_accel_v049_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps cashneq
def gm_f06_biotech_f06_cash_to_total_assets_ps_63d_accel_v050_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps cashneq
def gm_f06_biotech_f06_cash_to_total_assets_ps_63d_accel_v051_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps cashneq
def gm_f06_biotech_f06_cash_to_total_assets_ps_126d_accel_v052_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps cashneq
def gm_f06_biotech_f06_cash_to_total_assets_ps_126d_accel_v053_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps cashneq
def gm_f06_biotech_f06_cash_to_total_assets_ps_126d_accel_v054_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps cashneq
def gm_f06_biotech_f06_cash_to_total_assets_ps_252d_accel_v055_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps cashneq
def gm_f06_biotech_f06_cash_to_total_assets_ps_252d_accel_v056_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps cashneq
def gm_f06_biotech_f06_cash_to_total_assets_ps_252d_accel_v057_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps cashneq
def gm_f06_biotech_f06_cash_to_total_assets_ps_504d_accel_v058_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps cashneq
def gm_f06_biotech_f06_cash_to_total_assets_ps_504d_accel_v059_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps cashneq
def gm_f06_biotech_f06_cash_to_total_assets_ps_504d_accel_v060_signal(cashneq, sharesbas):
    base = _safe_div(_mean(cashneq, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_asset_scaled_21d_accel_v061_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_asset_scaled_21d_accel_v062_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_asset_scaled_21d_accel_v063_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_asset_scaled_63d_accel_v064_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_asset_scaled_63d_accel_v065_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_asset_scaled_63d_accel_v066_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_asset_scaled_126d_accel_v067_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_asset_scaled_126d_accel_v068_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_asset_scaled_126d_accel_v069_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_asset_scaled_252d_accel_v070_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_asset_scaled_252d_accel_v071_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_asset_scaled_252d_accel_v072_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_asset_scaled_504d_accel_v073_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_asset_scaled_504d_accel_v074_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_asset_scaled_504d_accel_v075_signal(cashneq, assets):
    base = _safe_div(_mean(cashneq, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mcap_scaled_21d_accel_v076_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mcap_scaled_21d_accel_v077_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mcap_scaled_21d_accel_v078_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mcap_scaled_63d_accel_v079_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mcap_scaled_63d_accel_v080_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mcap_scaled_63d_accel_v081_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mcap_scaled_126d_accel_v082_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mcap_scaled_126d_accel_v083_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mcap_scaled_126d_accel_v084_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mcap_scaled_252d_accel_v085_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mcap_scaled_252d_accel_v086_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mcap_scaled_252d_accel_v087_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mcap_scaled_504d_accel_v088_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mcap_scaled_504d_accel_v089_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mcap_scaled_504d_accel_v090_signal(cashneq, marketcap):
    base = _safe_div(_mean(cashneq, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_low_21d_accel_v091_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(21).min(), cashneq.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_low_21d_accel_v092_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(21).min(), cashneq.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_low_21d_accel_v093_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(21).min(), cashneq.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_low_63d_accel_v094_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(63).min(), cashneq.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_low_63d_accel_v095_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(63).min(), cashneq.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_low_63d_accel_v096_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(63).min(), cashneq.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_low_126d_accel_v097_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(126).min(), cashneq.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_low_126d_accel_v098_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(126).min(), cashneq.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_low_126d_accel_v099_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(126).min(), cashneq.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_low_252d_accel_v100_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(252).min(), cashneq.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_low_252d_accel_v101_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(252).min(), cashneq.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_low_252d_accel_v102_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(252).min(), cashneq.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_low_504d_accel_v103_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(504).min(), cashneq.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_low_504d_accel_v104_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(504).min(), cashneq.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_low_504d_accel_v105_signal(cashneq):
    base = _safe_div(cashneq - cashneq.rolling(504).min(), cashneq.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_high_21d_accel_v106_signal(cashneq):
    base = _safe_div(cashneq.rolling(21).max() - cashneq, cashneq.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_high_21d_accel_v107_signal(cashneq):
    base = _safe_div(cashneq.rolling(21).max() - cashneq, cashneq.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_high_21d_accel_v108_signal(cashneq):
    base = _safe_div(cashneq.rolling(21).max() - cashneq, cashneq.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_high_63d_accel_v109_signal(cashneq):
    base = _safe_div(cashneq.rolling(63).max() - cashneq, cashneq.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_high_63d_accel_v110_signal(cashneq):
    base = _safe_div(cashneq.rolling(63).max() - cashneq, cashneq.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_high_63d_accel_v111_signal(cashneq):
    base = _safe_div(cashneq.rolling(63).max() - cashneq, cashneq.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_high_126d_accel_v112_signal(cashneq):
    base = _safe_div(cashneq.rolling(126).max() - cashneq, cashneq.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_high_126d_accel_v113_signal(cashneq):
    base = _safe_div(cashneq.rolling(126).max() - cashneq, cashneq.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_high_126d_accel_v114_signal(cashneq):
    base = _safe_div(cashneq.rolling(126).max() - cashneq, cashneq.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_high_252d_accel_v115_signal(cashneq):
    base = _safe_div(cashneq.rolling(252).max() - cashneq, cashneq.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_high_252d_accel_v116_signal(cashneq):
    base = _safe_div(cashneq.rolling(252).max() - cashneq, cashneq.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_high_252d_accel_v117_signal(cashneq):
    base = _safe_div(cashneq.rolling(252).max() - cashneq, cashneq.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_high_504d_accel_v118_signal(cashneq):
    base = _safe_div(cashneq.rolling(504).max() - cashneq, cashneq.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_high_504d_accel_v119_signal(cashneq):
    base = _safe_div(cashneq.rolling(504).max() - cashneq, cashneq.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high cashneq
def gm_f06_biotech_f06_cash_to_total_assets_dist_high_504d_accel_v120_signal(cashneq):
    base = _safe_div(cashneq.rolling(504).max() - cashneq, cashneq.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mom_21d_accel_v121_signal(cashneq):
    base = _safe_div(_mean(cashneq, 21) - _mean(cashneq, 42), _mean(cashneq, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mom_21d_accel_v122_signal(cashneq):
    base = _safe_div(_mean(cashneq, 21) - _mean(cashneq, 42), _mean(cashneq, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mom_21d_accel_v123_signal(cashneq):
    base = _safe_div(_mean(cashneq, 21) - _mean(cashneq, 42), _mean(cashneq, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mom_63d_accel_v124_signal(cashneq):
    base = _safe_div(_mean(cashneq, 63) - _mean(cashneq, 126), _mean(cashneq, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mom_63d_accel_v125_signal(cashneq):
    base = _safe_div(_mean(cashneq, 63) - _mean(cashneq, 126), _mean(cashneq, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mom_63d_accel_v126_signal(cashneq):
    base = _safe_div(_mean(cashneq, 63) - _mean(cashneq, 126), _mean(cashneq, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mom_126d_accel_v127_signal(cashneq):
    base = _safe_div(_mean(cashneq, 126) - _mean(cashneq, 252), _mean(cashneq, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mom_126d_accel_v128_signal(cashneq):
    base = _safe_div(_mean(cashneq, 126) - _mean(cashneq, 252), _mean(cashneq, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mom_126d_accel_v129_signal(cashneq):
    base = _safe_div(_mean(cashneq, 126) - _mean(cashneq, 252), _mean(cashneq, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mom_252d_accel_v130_signal(cashneq):
    base = _safe_div(_mean(cashneq, 252) - _mean(cashneq, 504), _mean(cashneq, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mom_252d_accel_v131_signal(cashneq):
    base = _safe_div(_mean(cashneq, 252) - _mean(cashneq, 504), _mean(cashneq, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mom_252d_accel_v132_signal(cashneq):
    base = _safe_div(_mean(cashneq, 252) - _mean(cashneq, 504), _mean(cashneq, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mom_504d_accel_v133_signal(cashneq):
    base = _safe_div(_mean(cashneq, 504) - _mean(cashneq, 1008), _mean(cashneq, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mom_504d_accel_v134_signal(cashneq):
    base = _safe_div(_mean(cashneq, 504) - _mean(cashneq, 1008), _mean(cashneq, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom cashneq
def gm_f06_biotech_f06_cash_to_total_assets_mom_504d_accel_v135_signal(cashneq):
    base = _safe_div(_mean(cashneq, 504) - _mean(cashneq, 1008), _mean(cashneq, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol cashneq
def gm_f06_biotech_f06_cash_to_total_assets_vol_21d_accel_v136_signal(cashneq):
    base = _std(cashneq, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol cashneq
def gm_f06_biotech_f06_cash_to_total_assets_vol_21d_accel_v137_signal(cashneq):
    base = _std(cashneq, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol cashneq
def gm_f06_biotech_f06_cash_to_total_assets_vol_21d_accel_v138_signal(cashneq):
    base = _std(cashneq, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol cashneq
def gm_f06_biotech_f06_cash_to_total_assets_vol_63d_accel_v139_signal(cashneq):
    base = _std(cashneq, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol cashneq
def gm_f06_biotech_f06_cash_to_total_assets_vol_63d_accel_v140_signal(cashneq):
    base = _std(cashneq, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol cashneq
def gm_f06_biotech_f06_cash_to_total_assets_vol_63d_accel_v141_signal(cashneq):
    base = _std(cashneq, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol cashneq
def gm_f06_biotech_f06_cash_to_total_assets_vol_126d_accel_v142_signal(cashneq):
    base = _std(cashneq, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol cashneq
def gm_f06_biotech_f06_cash_to_total_assets_vol_126d_accel_v143_signal(cashneq):
    base = _std(cashneq, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol cashneq
def gm_f06_biotech_f06_cash_to_total_assets_vol_126d_accel_v144_signal(cashneq):
    base = _std(cashneq, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol cashneq
def gm_f06_biotech_f06_cash_to_total_assets_vol_252d_accel_v145_signal(cashneq):
    base = _std(cashneq, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol cashneq
def gm_f06_biotech_f06_cash_to_total_assets_vol_252d_accel_v146_signal(cashneq):
    base = _std(cashneq, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol cashneq
def gm_f06_biotech_f06_cash_to_total_assets_vol_252d_accel_v147_signal(cashneq):
    base = _std(cashneq, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol cashneq
def gm_f06_biotech_f06_cash_to_total_assets_vol_504d_accel_v148_signal(cashneq):
    base = _std(cashneq, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol cashneq
def gm_f06_biotech_f06_cash_to_total_assets_vol_504d_accel_v149_signal(cashneq):
    base = _std(cashneq, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol cashneq
def gm_f06_biotech_f06_cash_to_total_assets_vol_504d_accel_v150_signal(cashneq):
    base = _std(cashneq, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

