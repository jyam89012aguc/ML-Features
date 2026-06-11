
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw units
def gm_f75_biotech_f75_institutional_capital_flow_net_raw_21d_accel_v001_signal(units):
    base = _mean(units, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw units
def gm_f75_biotech_f75_institutional_capital_flow_net_raw_21d_accel_v002_signal(units):
    base = _mean(units, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw units
def gm_f75_biotech_f75_institutional_capital_flow_net_raw_21d_accel_v003_signal(units):
    base = _mean(units, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw units
def gm_f75_biotech_f75_institutional_capital_flow_net_raw_63d_accel_v004_signal(units):
    base = _mean(units, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw units
def gm_f75_biotech_f75_institutional_capital_flow_net_raw_63d_accel_v005_signal(units):
    base = _mean(units, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw units
def gm_f75_biotech_f75_institutional_capital_flow_net_raw_63d_accel_v006_signal(units):
    base = _mean(units, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw units
def gm_f75_biotech_f75_institutional_capital_flow_net_raw_126d_accel_v007_signal(units):
    base = _mean(units, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw units
def gm_f75_biotech_f75_institutional_capital_flow_net_raw_126d_accel_v008_signal(units):
    base = _mean(units, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw units
def gm_f75_biotech_f75_institutional_capital_flow_net_raw_126d_accel_v009_signal(units):
    base = _mean(units, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw units
def gm_f75_biotech_f75_institutional_capital_flow_net_raw_252d_accel_v010_signal(units):
    base = _mean(units, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw units
def gm_f75_biotech_f75_institutional_capital_flow_net_raw_252d_accel_v011_signal(units):
    base = _mean(units, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw units
def gm_f75_biotech_f75_institutional_capital_flow_net_raw_252d_accel_v012_signal(units):
    base = _mean(units, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw units
def gm_f75_biotech_f75_institutional_capital_flow_net_raw_504d_accel_v013_signal(units):
    base = _mean(units, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw units
def gm_f75_biotech_f75_institutional_capital_flow_net_raw_504d_accel_v014_signal(units):
    base = _mean(units, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw units
def gm_f75_biotech_f75_institutional_capital_flow_net_raw_504d_accel_v015_signal(units):
    base = _mean(units, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log units
def gm_f75_biotech_f75_institutional_capital_flow_net_log_21d_accel_v016_signal(units):
    base = _mean(_log(units), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log units
def gm_f75_biotech_f75_institutional_capital_flow_net_log_21d_accel_v017_signal(units):
    base = _mean(_log(units), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log units
def gm_f75_biotech_f75_institutional_capital_flow_net_log_21d_accel_v018_signal(units):
    base = _mean(_log(units), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log units
def gm_f75_biotech_f75_institutional_capital_flow_net_log_63d_accel_v019_signal(units):
    base = _mean(_log(units), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log units
def gm_f75_biotech_f75_institutional_capital_flow_net_log_63d_accel_v020_signal(units):
    base = _mean(_log(units), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log units
def gm_f75_biotech_f75_institutional_capital_flow_net_log_63d_accel_v021_signal(units):
    base = _mean(_log(units), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log units
def gm_f75_biotech_f75_institutional_capital_flow_net_log_126d_accel_v022_signal(units):
    base = _mean(_log(units), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log units
def gm_f75_biotech_f75_institutional_capital_flow_net_log_126d_accel_v023_signal(units):
    base = _mean(_log(units), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log units
def gm_f75_biotech_f75_institutional_capital_flow_net_log_126d_accel_v024_signal(units):
    base = _mean(_log(units), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log units
def gm_f75_biotech_f75_institutional_capital_flow_net_log_252d_accel_v025_signal(units):
    base = _mean(_log(units), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log units
def gm_f75_biotech_f75_institutional_capital_flow_net_log_252d_accel_v026_signal(units):
    base = _mean(_log(units), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log units
def gm_f75_biotech_f75_institutional_capital_flow_net_log_252d_accel_v027_signal(units):
    base = _mean(_log(units), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log units
def gm_f75_biotech_f75_institutional_capital_flow_net_log_504d_accel_v028_signal(units):
    base = _mean(_log(units), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log units
def gm_f75_biotech_f75_institutional_capital_flow_net_log_504d_accel_v029_signal(units):
    base = _mean(_log(units), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log units
def gm_f75_biotech_f75_institutional_capital_flow_net_log_504d_accel_v030_signal(units):
    base = _mean(_log(units), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z units
def gm_f75_biotech_f75_institutional_capital_flow_net_z_21d_accel_v031_signal(units):
    base = _z(units, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z units
def gm_f75_biotech_f75_institutional_capital_flow_net_z_21d_accel_v032_signal(units):
    base = _z(units, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z units
def gm_f75_biotech_f75_institutional_capital_flow_net_z_21d_accel_v033_signal(units):
    base = _z(units, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z units
def gm_f75_biotech_f75_institutional_capital_flow_net_z_63d_accel_v034_signal(units):
    base = _z(units, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z units
def gm_f75_biotech_f75_institutional_capital_flow_net_z_63d_accel_v035_signal(units):
    base = _z(units, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z units
def gm_f75_biotech_f75_institutional_capital_flow_net_z_63d_accel_v036_signal(units):
    base = _z(units, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z units
def gm_f75_biotech_f75_institutional_capital_flow_net_z_126d_accel_v037_signal(units):
    base = _z(units, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z units
def gm_f75_biotech_f75_institutional_capital_flow_net_z_126d_accel_v038_signal(units):
    base = _z(units, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z units
def gm_f75_biotech_f75_institutional_capital_flow_net_z_126d_accel_v039_signal(units):
    base = _z(units, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z units
def gm_f75_biotech_f75_institutional_capital_flow_net_z_252d_accel_v040_signal(units):
    base = _z(units, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z units
def gm_f75_biotech_f75_institutional_capital_flow_net_z_252d_accel_v041_signal(units):
    base = _z(units, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z units
def gm_f75_biotech_f75_institutional_capital_flow_net_z_252d_accel_v042_signal(units):
    base = _z(units, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z units
def gm_f75_biotech_f75_institutional_capital_flow_net_z_504d_accel_v043_signal(units):
    base = _z(units, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z units
def gm_f75_biotech_f75_institutional_capital_flow_net_z_504d_accel_v044_signal(units):
    base = _z(units, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z units
def gm_f75_biotech_f75_institutional_capital_flow_net_z_504d_accel_v045_signal(units):
    base = _z(units, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps units
def gm_f75_biotech_f75_institutional_capital_flow_net_ps_21d_accel_v046_signal(units, sharesbas):
    base = _safe_div(_mean(units, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps units
def gm_f75_biotech_f75_institutional_capital_flow_net_ps_21d_accel_v047_signal(units, sharesbas):
    base = _safe_div(_mean(units, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps units
def gm_f75_biotech_f75_institutional_capital_flow_net_ps_21d_accel_v048_signal(units, sharesbas):
    base = _safe_div(_mean(units, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps units
def gm_f75_biotech_f75_institutional_capital_flow_net_ps_63d_accel_v049_signal(units, sharesbas):
    base = _safe_div(_mean(units, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps units
def gm_f75_biotech_f75_institutional_capital_flow_net_ps_63d_accel_v050_signal(units, sharesbas):
    base = _safe_div(_mean(units, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps units
def gm_f75_biotech_f75_institutional_capital_flow_net_ps_63d_accel_v051_signal(units, sharesbas):
    base = _safe_div(_mean(units, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps units
def gm_f75_biotech_f75_institutional_capital_flow_net_ps_126d_accel_v052_signal(units, sharesbas):
    base = _safe_div(_mean(units, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps units
def gm_f75_biotech_f75_institutional_capital_flow_net_ps_126d_accel_v053_signal(units, sharesbas):
    base = _safe_div(_mean(units, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps units
def gm_f75_biotech_f75_institutional_capital_flow_net_ps_126d_accel_v054_signal(units, sharesbas):
    base = _safe_div(_mean(units, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps units
def gm_f75_biotech_f75_institutional_capital_flow_net_ps_252d_accel_v055_signal(units, sharesbas):
    base = _safe_div(_mean(units, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps units
def gm_f75_biotech_f75_institutional_capital_flow_net_ps_252d_accel_v056_signal(units, sharesbas):
    base = _safe_div(_mean(units, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps units
def gm_f75_biotech_f75_institutional_capital_flow_net_ps_252d_accel_v057_signal(units, sharesbas):
    base = _safe_div(_mean(units, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps units
def gm_f75_biotech_f75_institutional_capital_flow_net_ps_504d_accel_v058_signal(units, sharesbas):
    base = _safe_div(_mean(units, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps units
def gm_f75_biotech_f75_institutional_capital_flow_net_ps_504d_accel_v059_signal(units, sharesbas):
    base = _safe_div(_mean(units, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps units
def gm_f75_biotech_f75_institutional_capital_flow_net_ps_504d_accel_v060_signal(units, sharesbas):
    base = _safe_div(_mean(units, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_asset_scaled_21d_accel_v061_signal(units, assets):
    base = _safe_div(_mean(units, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_asset_scaled_21d_accel_v062_signal(units, assets):
    base = _safe_div(_mean(units, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_asset_scaled_21d_accel_v063_signal(units, assets):
    base = _safe_div(_mean(units, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_asset_scaled_63d_accel_v064_signal(units, assets):
    base = _safe_div(_mean(units, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_asset_scaled_63d_accel_v065_signal(units, assets):
    base = _safe_div(_mean(units, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_asset_scaled_63d_accel_v066_signal(units, assets):
    base = _safe_div(_mean(units, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_asset_scaled_126d_accel_v067_signal(units, assets):
    base = _safe_div(_mean(units, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_asset_scaled_126d_accel_v068_signal(units, assets):
    base = _safe_div(_mean(units, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_asset_scaled_126d_accel_v069_signal(units, assets):
    base = _safe_div(_mean(units, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_asset_scaled_252d_accel_v070_signal(units, assets):
    base = _safe_div(_mean(units, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_asset_scaled_252d_accel_v071_signal(units, assets):
    base = _safe_div(_mean(units, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_asset_scaled_252d_accel_v072_signal(units, assets):
    base = _safe_div(_mean(units, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_asset_scaled_504d_accel_v073_signal(units, assets):
    base = _safe_div(_mean(units, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_asset_scaled_504d_accel_v074_signal(units, assets):
    base = _safe_div(_mean(units, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_asset_scaled_504d_accel_v075_signal(units, assets):
    base = _safe_div(_mean(units, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_mcap_scaled_21d_accel_v076_signal(units, marketcap):
    base = _safe_div(_mean(units, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_mcap_scaled_21d_accel_v077_signal(units, marketcap):
    base = _safe_div(_mean(units, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_mcap_scaled_21d_accel_v078_signal(units, marketcap):
    base = _safe_div(_mean(units, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_mcap_scaled_63d_accel_v079_signal(units, marketcap):
    base = _safe_div(_mean(units, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_mcap_scaled_63d_accel_v080_signal(units, marketcap):
    base = _safe_div(_mean(units, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_mcap_scaled_63d_accel_v081_signal(units, marketcap):
    base = _safe_div(_mean(units, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_mcap_scaled_126d_accel_v082_signal(units, marketcap):
    base = _safe_div(_mean(units, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_mcap_scaled_126d_accel_v083_signal(units, marketcap):
    base = _safe_div(_mean(units, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_mcap_scaled_126d_accel_v084_signal(units, marketcap):
    base = _safe_div(_mean(units, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_mcap_scaled_252d_accel_v085_signal(units, marketcap):
    base = _safe_div(_mean(units, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_mcap_scaled_252d_accel_v086_signal(units, marketcap):
    base = _safe_div(_mean(units, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_mcap_scaled_252d_accel_v087_signal(units, marketcap):
    base = _safe_div(_mean(units, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_mcap_scaled_504d_accel_v088_signal(units, marketcap):
    base = _safe_div(_mean(units, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_mcap_scaled_504d_accel_v089_signal(units, marketcap):
    base = _safe_div(_mean(units, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled units
def gm_f75_biotech_f75_institutional_capital_flow_net_mcap_scaled_504d_accel_v090_signal(units, marketcap):
    base = _safe_div(_mean(units, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_low_21d_accel_v091_signal(units):
    base = _safe_div(units - units.rolling(21).min(), units.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_low_21d_accel_v092_signal(units):
    base = _safe_div(units - units.rolling(21).min(), units.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_low_21d_accel_v093_signal(units):
    base = _safe_div(units - units.rolling(21).min(), units.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_low_63d_accel_v094_signal(units):
    base = _safe_div(units - units.rolling(63).min(), units.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_low_63d_accel_v095_signal(units):
    base = _safe_div(units - units.rolling(63).min(), units.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_low_63d_accel_v096_signal(units):
    base = _safe_div(units - units.rolling(63).min(), units.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_low_126d_accel_v097_signal(units):
    base = _safe_div(units - units.rolling(126).min(), units.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_low_126d_accel_v098_signal(units):
    base = _safe_div(units - units.rolling(126).min(), units.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_low_126d_accel_v099_signal(units):
    base = _safe_div(units - units.rolling(126).min(), units.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_low_252d_accel_v100_signal(units):
    base = _safe_div(units - units.rolling(252).min(), units.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_low_252d_accel_v101_signal(units):
    base = _safe_div(units - units.rolling(252).min(), units.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_low_252d_accel_v102_signal(units):
    base = _safe_div(units - units.rolling(252).min(), units.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_low_504d_accel_v103_signal(units):
    base = _safe_div(units - units.rolling(504).min(), units.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_low_504d_accel_v104_signal(units):
    base = _safe_div(units - units.rolling(504).min(), units.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_low_504d_accel_v105_signal(units):
    base = _safe_div(units - units.rolling(504).min(), units.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_high_21d_accel_v106_signal(units):
    base = _safe_div(units.rolling(21).max() - units, units.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_high_21d_accel_v107_signal(units):
    base = _safe_div(units.rolling(21).max() - units, units.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_high_21d_accel_v108_signal(units):
    base = _safe_div(units.rolling(21).max() - units, units.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_high_63d_accel_v109_signal(units):
    base = _safe_div(units.rolling(63).max() - units, units.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_high_63d_accel_v110_signal(units):
    base = _safe_div(units.rolling(63).max() - units, units.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_high_63d_accel_v111_signal(units):
    base = _safe_div(units.rolling(63).max() - units, units.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_high_126d_accel_v112_signal(units):
    base = _safe_div(units.rolling(126).max() - units, units.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_high_126d_accel_v113_signal(units):
    base = _safe_div(units.rolling(126).max() - units, units.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_high_126d_accel_v114_signal(units):
    base = _safe_div(units.rolling(126).max() - units, units.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_high_252d_accel_v115_signal(units):
    base = _safe_div(units.rolling(252).max() - units, units.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_high_252d_accel_v116_signal(units):
    base = _safe_div(units.rolling(252).max() - units, units.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_high_252d_accel_v117_signal(units):
    base = _safe_div(units.rolling(252).max() - units, units.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_high_504d_accel_v118_signal(units):
    base = _safe_div(units.rolling(504).max() - units, units.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_high_504d_accel_v119_signal(units):
    base = _safe_div(units.rolling(504).max() - units, units.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high units
def gm_f75_biotech_f75_institutional_capital_flow_net_dist_high_504d_accel_v120_signal(units):
    base = _safe_div(units.rolling(504).max() - units, units.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom units
def gm_f75_biotech_f75_institutional_capital_flow_net_mom_21d_accel_v121_signal(units):
    base = _safe_div(_mean(units, 21) - _mean(units, 42), _mean(units, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom units
def gm_f75_biotech_f75_institutional_capital_flow_net_mom_21d_accel_v122_signal(units):
    base = _safe_div(_mean(units, 21) - _mean(units, 42), _mean(units, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom units
def gm_f75_biotech_f75_institutional_capital_flow_net_mom_21d_accel_v123_signal(units):
    base = _safe_div(_mean(units, 21) - _mean(units, 42), _mean(units, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom units
def gm_f75_biotech_f75_institutional_capital_flow_net_mom_63d_accel_v124_signal(units):
    base = _safe_div(_mean(units, 63) - _mean(units, 126), _mean(units, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom units
def gm_f75_biotech_f75_institutional_capital_flow_net_mom_63d_accel_v125_signal(units):
    base = _safe_div(_mean(units, 63) - _mean(units, 126), _mean(units, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom units
def gm_f75_biotech_f75_institutional_capital_flow_net_mom_63d_accel_v126_signal(units):
    base = _safe_div(_mean(units, 63) - _mean(units, 126), _mean(units, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom units
def gm_f75_biotech_f75_institutional_capital_flow_net_mom_126d_accel_v127_signal(units):
    base = _safe_div(_mean(units, 126) - _mean(units, 252), _mean(units, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom units
def gm_f75_biotech_f75_institutional_capital_flow_net_mom_126d_accel_v128_signal(units):
    base = _safe_div(_mean(units, 126) - _mean(units, 252), _mean(units, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom units
def gm_f75_biotech_f75_institutional_capital_flow_net_mom_126d_accel_v129_signal(units):
    base = _safe_div(_mean(units, 126) - _mean(units, 252), _mean(units, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom units
def gm_f75_biotech_f75_institutional_capital_flow_net_mom_252d_accel_v130_signal(units):
    base = _safe_div(_mean(units, 252) - _mean(units, 504), _mean(units, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom units
def gm_f75_biotech_f75_institutional_capital_flow_net_mom_252d_accel_v131_signal(units):
    base = _safe_div(_mean(units, 252) - _mean(units, 504), _mean(units, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom units
def gm_f75_biotech_f75_institutional_capital_flow_net_mom_252d_accel_v132_signal(units):
    base = _safe_div(_mean(units, 252) - _mean(units, 504), _mean(units, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom units
def gm_f75_biotech_f75_institutional_capital_flow_net_mom_504d_accel_v133_signal(units):
    base = _safe_div(_mean(units, 504) - _mean(units, 1008), _mean(units, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom units
def gm_f75_biotech_f75_institutional_capital_flow_net_mom_504d_accel_v134_signal(units):
    base = _safe_div(_mean(units, 504) - _mean(units, 1008), _mean(units, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom units
def gm_f75_biotech_f75_institutional_capital_flow_net_mom_504d_accel_v135_signal(units):
    base = _safe_div(_mean(units, 504) - _mean(units, 1008), _mean(units, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol units
def gm_f75_biotech_f75_institutional_capital_flow_net_vol_21d_accel_v136_signal(units):
    base = _std(units, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol units
def gm_f75_biotech_f75_institutional_capital_flow_net_vol_21d_accel_v137_signal(units):
    base = _std(units, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol units
def gm_f75_biotech_f75_institutional_capital_flow_net_vol_21d_accel_v138_signal(units):
    base = _std(units, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol units
def gm_f75_biotech_f75_institutional_capital_flow_net_vol_63d_accel_v139_signal(units):
    base = _std(units, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol units
def gm_f75_biotech_f75_institutional_capital_flow_net_vol_63d_accel_v140_signal(units):
    base = _std(units, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol units
def gm_f75_biotech_f75_institutional_capital_flow_net_vol_63d_accel_v141_signal(units):
    base = _std(units, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol units
def gm_f75_biotech_f75_institutional_capital_flow_net_vol_126d_accel_v142_signal(units):
    base = _std(units, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol units
def gm_f75_biotech_f75_institutional_capital_flow_net_vol_126d_accel_v143_signal(units):
    base = _std(units, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol units
def gm_f75_biotech_f75_institutional_capital_flow_net_vol_126d_accel_v144_signal(units):
    base = _std(units, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol units
def gm_f75_biotech_f75_institutional_capital_flow_net_vol_252d_accel_v145_signal(units):
    base = _std(units, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol units
def gm_f75_biotech_f75_institutional_capital_flow_net_vol_252d_accel_v146_signal(units):
    base = _std(units, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol units
def gm_f75_biotech_f75_institutional_capital_flow_net_vol_252d_accel_v147_signal(units):
    base = _std(units, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol units
def gm_f75_biotech_f75_institutional_capital_flow_net_vol_504d_accel_v148_signal(units):
    base = _std(units, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol units
def gm_f75_biotech_f75_institutional_capital_flow_net_vol_504d_accel_v149_signal(units):
    base = _std(units, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol units
def gm_f75_biotech_f75_institutional_capital_flow_net_vol_504d_accel_v150_signal(units):
    base = _std(units, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

