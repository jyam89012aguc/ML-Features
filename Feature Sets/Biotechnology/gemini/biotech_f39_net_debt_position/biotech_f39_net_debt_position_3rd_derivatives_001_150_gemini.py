
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw debt
def gm_f39_biotech_f39_net_debt_position_raw_21d_accel_v001_signal(debt):
    base = _mean(debt, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw debt
def gm_f39_biotech_f39_net_debt_position_raw_21d_accel_v002_signal(debt):
    base = _mean(debt, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw debt
def gm_f39_biotech_f39_net_debt_position_raw_21d_accel_v003_signal(debt):
    base = _mean(debt, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw debt
def gm_f39_biotech_f39_net_debt_position_raw_63d_accel_v004_signal(debt):
    base = _mean(debt, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw debt
def gm_f39_biotech_f39_net_debt_position_raw_63d_accel_v005_signal(debt):
    base = _mean(debt, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw debt
def gm_f39_biotech_f39_net_debt_position_raw_63d_accel_v006_signal(debt):
    base = _mean(debt, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw debt
def gm_f39_biotech_f39_net_debt_position_raw_126d_accel_v007_signal(debt):
    base = _mean(debt, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw debt
def gm_f39_biotech_f39_net_debt_position_raw_126d_accel_v008_signal(debt):
    base = _mean(debt, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw debt
def gm_f39_biotech_f39_net_debt_position_raw_126d_accel_v009_signal(debt):
    base = _mean(debt, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw debt
def gm_f39_biotech_f39_net_debt_position_raw_252d_accel_v010_signal(debt):
    base = _mean(debt, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw debt
def gm_f39_biotech_f39_net_debt_position_raw_252d_accel_v011_signal(debt):
    base = _mean(debt, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw debt
def gm_f39_biotech_f39_net_debt_position_raw_252d_accel_v012_signal(debt):
    base = _mean(debt, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw debt
def gm_f39_biotech_f39_net_debt_position_raw_504d_accel_v013_signal(debt):
    base = _mean(debt, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw debt
def gm_f39_biotech_f39_net_debt_position_raw_504d_accel_v014_signal(debt):
    base = _mean(debt, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw debt
def gm_f39_biotech_f39_net_debt_position_raw_504d_accel_v015_signal(debt):
    base = _mean(debt, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log debt
def gm_f39_biotech_f39_net_debt_position_log_21d_accel_v016_signal(debt):
    base = _mean(_log(debt), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log debt
def gm_f39_biotech_f39_net_debt_position_log_21d_accel_v017_signal(debt):
    base = _mean(_log(debt), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log debt
def gm_f39_biotech_f39_net_debt_position_log_21d_accel_v018_signal(debt):
    base = _mean(_log(debt), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log debt
def gm_f39_biotech_f39_net_debt_position_log_63d_accel_v019_signal(debt):
    base = _mean(_log(debt), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log debt
def gm_f39_biotech_f39_net_debt_position_log_63d_accel_v020_signal(debt):
    base = _mean(_log(debt), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log debt
def gm_f39_biotech_f39_net_debt_position_log_63d_accel_v021_signal(debt):
    base = _mean(_log(debt), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log debt
def gm_f39_biotech_f39_net_debt_position_log_126d_accel_v022_signal(debt):
    base = _mean(_log(debt), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log debt
def gm_f39_biotech_f39_net_debt_position_log_126d_accel_v023_signal(debt):
    base = _mean(_log(debt), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log debt
def gm_f39_biotech_f39_net_debt_position_log_126d_accel_v024_signal(debt):
    base = _mean(_log(debt), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log debt
def gm_f39_biotech_f39_net_debt_position_log_252d_accel_v025_signal(debt):
    base = _mean(_log(debt), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log debt
def gm_f39_biotech_f39_net_debt_position_log_252d_accel_v026_signal(debt):
    base = _mean(_log(debt), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log debt
def gm_f39_biotech_f39_net_debt_position_log_252d_accel_v027_signal(debt):
    base = _mean(_log(debt), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log debt
def gm_f39_biotech_f39_net_debt_position_log_504d_accel_v028_signal(debt):
    base = _mean(_log(debt), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log debt
def gm_f39_biotech_f39_net_debt_position_log_504d_accel_v029_signal(debt):
    base = _mean(_log(debt), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log debt
def gm_f39_biotech_f39_net_debt_position_log_504d_accel_v030_signal(debt):
    base = _mean(_log(debt), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z debt
def gm_f39_biotech_f39_net_debt_position_z_21d_accel_v031_signal(debt):
    base = _z(debt, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z debt
def gm_f39_biotech_f39_net_debt_position_z_21d_accel_v032_signal(debt):
    base = _z(debt, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z debt
def gm_f39_biotech_f39_net_debt_position_z_21d_accel_v033_signal(debt):
    base = _z(debt, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z debt
def gm_f39_biotech_f39_net_debt_position_z_63d_accel_v034_signal(debt):
    base = _z(debt, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z debt
def gm_f39_biotech_f39_net_debt_position_z_63d_accel_v035_signal(debt):
    base = _z(debt, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z debt
def gm_f39_biotech_f39_net_debt_position_z_63d_accel_v036_signal(debt):
    base = _z(debt, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z debt
def gm_f39_biotech_f39_net_debt_position_z_126d_accel_v037_signal(debt):
    base = _z(debt, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z debt
def gm_f39_biotech_f39_net_debt_position_z_126d_accel_v038_signal(debt):
    base = _z(debt, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z debt
def gm_f39_biotech_f39_net_debt_position_z_126d_accel_v039_signal(debt):
    base = _z(debt, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z debt
def gm_f39_biotech_f39_net_debt_position_z_252d_accel_v040_signal(debt):
    base = _z(debt, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z debt
def gm_f39_biotech_f39_net_debt_position_z_252d_accel_v041_signal(debt):
    base = _z(debt, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z debt
def gm_f39_biotech_f39_net_debt_position_z_252d_accel_v042_signal(debt):
    base = _z(debt, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z debt
def gm_f39_biotech_f39_net_debt_position_z_504d_accel_v043_signal(debt):
    base = _z(debt, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z debt
def gm_f39_biotech_f39_net_debt_position_z_504d_accel_v044_signal(debt):
    base = _z(debt, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z debt
def gm_f39_biotech_f39_net_debt_position_z_504d_accel_v045_signal(debt):
    base = _z(debt, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps debt
def gm_f39_biotech_f39_net_debt_position_ps_21d_accel_v046_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps debt
def gm_f39_biotech_f39_net_debt_position_ps_21d_accel_v047_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps debt
def gm_f39_biotech_f39_net_debt_position_ps_21d_accel_v048_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps debt
def gm_f39_biotech_f39_net_debt_position_ps_63d_accel_v049_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps debt
def gm_f39_biotech_f39_net_debt_position_ps_63d_accel_v050_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps debt
def gm_f39_biotech_f39_net_debt_position_ps_63d_accel_v051_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps debt
def gm_f39_biotech_f39_net_debt_position_ps_126d_accel_v052_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps debt
def gm_f39_biotech_f39_net_debt_position_ps_126d_accel_v053_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps debt
def gm_f39_biotech_f39_net_debt_position_ps_126d_accel_v054_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps debt
def gm_f39_biotech_f39_net_debt_position_ps_252d_accel_v055_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps debt
def gm_f39_biotech_f39_net_debt_position_ps_252d_accel_v056_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps debt
def gm_f39_biotech_f39_net_debt_position_ps_252d_accel_v057_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps debt
def gm_f39_biotech_f39_net_debt_position_ps_504d_accel_v058_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps debt
def gm_f39_biotech_f39_net_debt_position_ps_504d_accel_v059_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps debt
def gm_f39_biotech_f39_net_debt_position_ps_504d_accel_v060_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled debt
def gm_f39_biotech_f39_net_debt_position_asset_scaled_21d_accel_v061_signal(debt, assets):
    base = _safe_div(_mean(debt, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled debt
def gm_f39_biotech_f39_net_debt_position_asset_scaled_21d_accel_v062_signal(debt, assets):
    base = _safe_div(_mean(debt, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled debt
def gm_f39_biotech_f39_net_debt_position_asset_scaled_21d_accel_v063_signal(debt, assets):
    base = _safe_div(_mean(debt, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled debt
def gm_f39_biotech_f39_net_debt_position_asset_scaled_63d_accel_v064_signal(debt, assets):
    base = _safe_div(_mean(debt, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled debt
def gm_f39_biotech_f39_net_debt_position_asset_scaled_63d_accel_v065_signal(debt, assets):
    base = _safe_div(_mean(debt, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled debt
def gm_f39_biotech_f39_net_debt_position_asset_scaled_63d_accel_v066_signal(debt, assets):
    base = _safe_div(_mean(debt, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled debt
def gm_f39_biotech_f39_net_debt_position_asset_scaled_126d_accel_v067_signal(debt, assets):
    base = _safe_div(_mean(debt, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled debt
def gm_f39_biotech_f39_net_debt_position_asset_scaled_126d_accel_v068_signal(debt, assets):
    base = _safe_div(_mean(debt, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled debt
def gm_f39_biotech_f39_net_debt_position_asset_scaled_126d_accel_v069_signal(debt, assets):
    base = _safe_div(_mean(debt, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled debt
def gm_f39_biotech_f39_net_debt_position_asset_scaled_252d_accel_v070_signal(debt, assets):
    base = _safe_div(_mean(debt, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled debt
def gm_f39_biotech_f39_net_debt_position_asset_scaled_252d_accel_v071_signal(debt, assets):
    base = _safe_div(_mean(debt, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled debt
def gm_f39_biotech_f39_net_debt_position_asset_scaled_252d_accel_v072_signal(debt, assets):
    base = _safe_div(_mean(debt, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled debt
def gm_f39_biotech_f39_net_debt_position_asset_scaled_504d_accel_v073_signal(debt, assets):
    base = _safe_div(_mean(debt, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled debt
def gm_f39_biotech_f39_net_debt_position_asset_scaled_504d_accel_v074_signal(debt, assets):
    base = _safe_div(_mean(debt, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled debt
def gm_f39_biotech_f39_net_debt_position_asset_scaled_504d_accel_v075_signal(debt, assets):
    base = _safe_div(_mean(debt, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled debt
def gm_f39_biotech_f39_net_debt_position_mcap_scaled_21d_accel_v076_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled debt
def gm_f39_biotech_f39_net_debt_position_mcap_scaled_21d_accel_v077_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled debt
def gm_f39_biotech_f39_net_debt_position_mcap_scaled_21d_accel_v078_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled debt
def gm_f39_biotech_f39_net_debt_position_mcap_scaled_63d_accel_v079_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled debt
def gm_f39_biotech_f39_net_debt_position_mcap_scaled_63d_accel_v080_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled debt
def gm_f39_biotech_f39_net_debt_position_mcap_scaled_63d_accel_v081_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled debt
def gm_f39_biotech_f39_net_debt_position_mcap_scaled_126d_accel_v082_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled debt
def gm_f39_biotech_f39_net_debt_position_mcap_scaled_126d_accel_v083_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled debt
def gm_f39_biotech_f39_net_debt_position_mcap_scaled_126d_accel_v084_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled debt
def gm_f39_biotech_f39_net_debt_position_mcap_scaled_252d_accel_v085_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled debt
def gm_f39_biotech_f39_net_debt_position_mcap_scaled_252d_accel_v086_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled debt
def gm_f39_biotech_f39_net_debt_position_mcap_scaled_252d_accel_v087_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled debt
def gm_f39_biotech_f39_net_debt_position_mcap_scaled_504d_accel_v088_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled debt
def gm_f39_biotech_f39_net_debt_position_mcap_scaled_504d_accel_v089_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled debt
def gm_f39_biotech_f39_net_debt_position_mcap_scaled_504d_accel_v090_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low debt
def gm_f39_biotech_f39_net_debt_position_dist_low_21d_accel_v091_signal(debt):
    base = _safe_div(debt - debt.rolling(21).min(), debt.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low debt
def gm_f39_biotech_f39_net_debt_position_dist_low_21d_accel_v092_signal(debt):
    base = _safe_div(debt - debt.rolling(21).min(), debt.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low debt
def gm_f39_biotech_f39_net_debt_position_dist_low_21d_accel_v093_signal(debt):
    base = _safe_div(debt - debt.rolling(21).min(), debt.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low debt
def gm_f39_biotech_f39_net_debt_position_dist_low_63d_accel_v094_signal(debt):
    base = _safe_div(debt - debt.rolling(63).min(), debt.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low debt
def gm_f39_biotech_f39_net_debt_position_dist_low_63d_accel_v095_signal(debt):
    base = _safe_div(debt - debt.rolling(63).min(), debt.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low debt
def gm_f39_biotech_f39_net_debt_position_dist_low_63d_accel_v096_signal(debt):
    base = _safe_div(debt - debt.rolling(63).min(), debt.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low debt
def gm_f39_biotech_f39_net_debt_position_dist_low_126d_accel_v097_signal(debt):
    base = _safe_div(debt - debt.rolling(126).min(), debt.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low debt
def gm_f39_biotech_f39_net_debt_position_dist_low_126d_accel_v098_signal(debt):
    base = _safe_div(debt - debt.rolling(126).min(), debt.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low debt
def gm_f39_biotech_f39_net_debt_position_dist_low_126d_accel_v099_signal(debt):
    base = _safe_div(debt - debt.rolling(126).min(), debt.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low debt
def gm_f39_biotech_f39_net_debt_position_dist_low_252d_accel_v100_signal(debt):
    base = _safe_div(debt - debt.rolling(252).min(), debt.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low debt
def gm_f39_biotech_f39_net_debt_position_dist_low_252d_accel_v101_signal(debt):
    base = _safe_div(debt - debt.rolling(252).min(), debt.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low debt
def gm_f39_biotech_f39_net_debt_position_dist_low_252d_accel_v102_signal(debt):
    base = _safe_div(debt - debt.rolling(252).min(), debt.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low debt
def gm_f39_biotech_f39_net_debt_position_dist_low_504d_accel_v103_signal(debt):
    base = _safe_div(debt - debt.rolling(504).min(), debt.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low debt
def gm_f39_biotech_f39_net_debt_position_dist_low_504d_accel_v104_signal(debt):
    base = _safe_div(debt - debt.rolling(504).min(), debt.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low debt
def gm_f39_biotech_f39_net_debt_position_dist_low_504d_accel_v105_signal(debt):
    base = _safe_div(debt - debt.rolling(504).min(), debt.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high debt
def gm_f39_biotech_f39_net_debt_position_dist_high_21d_accel_v106_signal(debt):
    base = _safe_div(debt.rolling(21).max() - debt, debt.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high debt
def gm_f39_biotech_f39_net_debt_position_dist_high_21d_accel_v107_signal(debt):
    base = _safe_div(debt.rolling(21).max() - debt, debt.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high debt
def gm_f39_biotech_f39_net_debt_position_dist_high_21d_accel_v108_signal(debt):
    base = _safe_div(debt.rolling(21).max() - debt, debt.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high debt
def gm_f39_biotech_f39_net_debt_position_dist_high_63d_accel_v109_signal(debt):
    base = _safe_div(debt.rolling(63).max() - debt, debt.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high debt
def gm_f39_biotech_f39_net_debt_position_dist_high_63d_accel_v110_signal(debt):
    base = _safe_div(debt.rolling(63).max() - debt, debt.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high debt
def gm_f39_biotech_f39_net_debt_position_dist_high_63d_accel_v111_signal(debt):
    base = _safe_div(debt.rolling(63).max() - debt, debt.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high debt
def gm_f39_biotech_f39_net_debt_position_dist_high_126d_accel_v112_signal(debt):
    base = _safe_div(debt.rolling(126).max() - debt, debt.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high debt
def gm_f39_biotech_f39_net_debt_position_dist_high_126d_accel_v113_signal(debt):
    base = _safe_div(debt.rolling(126).max() - debt, debt.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high debt
def gm_f39_biotech_f39_net_debt_position_dist_high_126d_accel_v114_signal(debt):
    base = _safe_div(debt.rolling(126).max() - debt, debt.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high debt
def gm_f39_biotech_f39_net_debt_position_dist_high_252d_accel_v115_signal(debt):
    base = _safe_div(debt.rolling(252).max() - debt, debt.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high debt
def gm_f39_biotech_f39_net_debt_position_dist_high_252d_accel_v116_signal(debt):
    base = _safe_div(debt.rolling(252).max() - debt, debt.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high debt
def gm_f39_biotech_f39_net_debt_position_dist_high_252d_accel_v117_signal(debt):
    base = _safe_div(debt.rolling(252).max() - debt, debt.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high debt
def gm_f39_biotech_f39_net_debt_position_dist_high_504d_accel_v118_signal(debt):
    base = _safe_div(debt.rolling(504).max() - debt, debt.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high debt
def gm_f39_biotech_f39_net_debt_position_dist_high_504d_accel_v119_signal(debt):
    base = _safe_div(debt.rolling(504).max() - debt, debt.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high debt
def gm_f39_biotech_f39_net_debt_position_dist_high_504d_accel_v120_signal(debt):
    base = _safe_div(debt.rolling(504).max() - debt, debt.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom debt
def gm_f39_biotech_f39_net_debt_position_mom_21d_accel_v121_signal(debt):
    base = _safe_div(_mean(debt, 21) - _mean(debt, 42), _mean(debt, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom debt
def gm_f39_biotech_f39_net_debt_position_mom_21d_accel_v122_signal(debt):
    base = _safe_div(_mean(debt, 21) - _mean(debt, 42), _mean(debt, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom debt
def gm_f39_biotech_f39_net_debt_position_mom_21d_accel_v123_signal(debt):
    base = _safe_div(_mean(debt, 21) - _mean(debt, 42), _mean(debt, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom debt
def gm_f39_biotech_f39_net_debt_position_mom_63d_accel_v124_signal(debt):
    base = _safe_div(_mean(debt, 63) - _mean(debt, 126), _mean(debt, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom debt
def gm_f39_biotech_f39_net_debt_position_mom_63d_accel_v125_signal(debt):
    base = _safe_div(_mean(debt, 63) - _mean(debt, 126), _mean(debt, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom debt
def gm_f39_biotech_f39_net_debt_position_mom_63d_accel_v126_signal(debt):
    base = _safe_div(_mean(debt, 63) - _mean(debt, 126), _mean(debt, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom debt
def gm_f39_biotech_f39_net_debt_position_mom_126d_accel_v127_signal(debt):
    base = _safe_div(_mean(debt, 126) - _mean(debt, 252), _mean(debt, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom debt
def gm_f39_biotech_f39_net_debt_position_mom_126d_accel_v128_signal(debt):
    base = _safe_div(_mean(debt, 126) - _mean(debt, 252), _mean(debt, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom debt
def gm_f39_biotech_f39_net_debt_position_mom_126d_accel_v129_signal(debt):
    base = _safe_div(_mean(debt, 126) - _mean(debt, 252), _mean(debt, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom debt
def gm_f39_biotech_f39_net_debt_position_mom_252d_accel_v130_signal(debt):
    base = _safe_div(_mean(debt, 252) - _mean(debt, 504), _mean(debt, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom debt
def gm_f39_biotech_f39_net_debt_position_mom_252d_accel_v131_signal(debt):
    base = _safe_div(_mean(debt, 252) - _mean(debt, 504), _mean(debt, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom debt
def gm_f39_biotech_f39_net_debt_position_mom_252d_accel_v132_signal(debt):
    base = _safe_div(_mean(debt, 252) - _mean(debt, 504), _mean(debt, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom debt
def gm_f39_biotech_f39_net_debt_position_mom_504d_accel_v133_signal(debt):
    base = _safe_div(_mean(debt, 504) - _mean(debt, 1008), _mean(debt, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom debt
def gm_f39_biotech_f39_net_debt_position_mom_504d_accel_v134_signal(debt):
    base = _safe_div(_mean(debt, 504) - _mean(debt, 1008), _mean(debt, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom debt
def gm_f39_biotech_f39_net_debt_position_mom_504d_accel_v135_signal(debt):
    base = _safe_div(_mean(debt, 504) - _mean(debt, 1008), _mean(debt, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol debt
def gm_f39_biotech_f39_net_debt_position_vol_21d_accel_v136_signal(debt):
    base = _std(debt, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol debt
def gm_f39_biotech_f39_net_debt_position_vol_21d_accel_v137_signal(debt):
    base = _std(debt, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol debt
def gm_f39_biotech_f39_net_debt_position_vol_21d_accel_v138_signal(debt):
    base = _std(debt, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol debt
def gm_f39_biotech_f39_net_debt_position_vol_63d_accel_v139_signal(debt):
    base = _std(debt, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol debt
def gm_f39_biotech_f39_net_debt_position_vol_63d_accel_v140_signal(debt):
    base = _std(debt, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol debt
def gm_f39_biotech_f39_net_debt_position_vol_63d_accel_v141_signal(debt):
    base = _std(debt, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol debt
def gm_f39_biotech_f39_net_debt_position_vol_126d_accel_v142_signal(debt):
    base = _std(debt, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol debt
def gm_f39_biotech_f39_net_debt_position_vol_126d_accel_v143_signal(debt):
    base = _std(debt, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol debt
def gm_f39_biotech_f39_net_debt_position_vol_126d_accel_v144_signal(debt):
    base = _std(debt, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol debt
def gm_f39_biotech_f39_net_debt_position_vol_252d_accel_v145_signal(debt):
    base = _std(debt, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol debt
def gm_f39_biotech_f39_net_debt_position_vol_252d_accel_v146_signal(debt):
    base = _std(debt, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol debt
def gm_f39_biotech_f39_net_debt_position_vol_252d_accel_v147_signal(debt):
    base = _std(debt, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol debt
def gm_f39_biotech_f39_net_debt_position_vol_504d_accel_v148_signal(debt):
    base = _std(debt, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol debt
def gm_f39_biotech_f39_net_debt_position_vol_504d_accel_v149_signal(debt):
    base = _std(debt, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol debt
def gm_f39_biotech_f39_net_debt_position_vol_504d_accel_v150_signal(debt):
    base = _std(debt, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

