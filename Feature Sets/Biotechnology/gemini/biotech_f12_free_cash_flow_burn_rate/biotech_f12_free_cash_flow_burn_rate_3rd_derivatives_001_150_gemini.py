
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_21d_accel_v001_signal(fcf):
    base = _mean(fcf, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_21d_accel_v002_signal(fcf):
    base = _mean(fcf, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_21d_accel_v003_signal(fcf):
    base = _mean(fcf, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_63d_accel_v004_signal(fcf):
    base = _mean(fcf, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_63d_accel_v005_signal(fcf):
    base = _mean(fcf, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_63d_accel_v006_signal(fcf):
    base = _mean(fcf, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_126d_accel_v007_signal(fcf):
    base = _mean(fcf, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_126d_accel_v008_signal(fcf):
    base = _mean(fcf, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_126d_accel_v009_signal(fcf):
    base = _mean(fcf, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_252d_accel_v010_signal(fcf):
    base = _mean(fcf, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_252d_accel_v011_signal(fcf):
    base = _mean(fcf, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_252d_accel_v012_signal(fcf):
    base = _mean(fcf, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_504d_accel_v013_signal(fcf):
    base = _mean(fcf, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_504d_accel_v014_signal(fcf):
    base = _mean(fcf, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_504d_accel_v015_signal(fcf):
    base = _mean(fcf, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_21d_accel_v016_signal(fcf):
    base = _mean(_log(fcf), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_21d_accel_v017_signal(fcf):
    base = _mean(_log(fcf), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_21d_accel_v018_signal(fcf):
    base = _mean(_log(fcf), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_63d_accel_v019_signal(fcf):
    base = _mean(_log(fcf), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_63d_accel_v020_signal(fcf):
    base = _mean(_log(fcf), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_63d_accel_v021_signal(fcf):
    base = _mean(_log(fcf), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_126d_accel_v022_signal(fcf):
    base = _mean(_log(fcf), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_126d_accel_v023_signal(fcf):
    base = _mean(_log(fcf), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_126d_accel_v024_signal(fcf):
    base = _mean(_log(fcf), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_252d_accel_v025_signal(fcf):
    base = _mean(_log(fcf), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_252d_accel_v026_signal(fcf):
    base = _mean(_log(fcf), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_252d_accel_v027_signal(fcf):
    base = _mean(_log(fcf), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_504d_accel_v028_signal(fcf):
    base = _mean(_log(fcf), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_504d_accel_v029_signal(fcf):
    base = _mean(_log(fcf), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_504d_accel_v030_signal(fcf):
    base = _mean(_log(fcf), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_21d_accel_v031_signal(fcf):
    base = _z(fcf, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_21d_accel_v032_signal(fcf):
    base = _z(fcf, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_21d_accel_v033_signal(fcf):
    base = _z(fcf, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_63d_accel_v034_signal(fcf):
    base = _z(fcf, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_63d_accel_v035_signal(fcf):
    base = _z(fcf, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_63d_accel_v036_signal(fcf):
    base = _z(fcf, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_126d_accel_v037_signal(fcf):
    base = _z(fcf, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_126d_accel_v038_signal(fcf):
    base = _z(fcf, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_126d_accel_v039_signal(fcf):
    base = _z(fcf, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_252d_accel_v040_signal(fcf):
    base = _z(fcf, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_252d_accel_v041_signal(fcf):
    base = _z(fcf, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_252d_accel_v042_signal(fcf):
    base = _z(fcf, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_504d_accel_v043_signal(fcf):
    base = _z(fcf, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_504d_accel_v044_signal(fcf):
    base = _z(fcf, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_504d_accel_v045_signal(fcf):
    base = _z(fcf, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_21d_accel_v046_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_21d_accel_v047_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_21d_accel_v048_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_63d_accel_v049_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_63d_accel_v050_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_63d_accel_v051_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_126d_accel_v052_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_126d_accel_v053_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_126d_accel_v054_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_252d_accel_v055_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_252d_accel_v056_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_252d_accel_v057_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_504d_accel_v058_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_504d_accel_v059_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_504d_accel_v060_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_21d_accel_v061_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_21d_accel_v062_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_21d_accel_v063_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_63d_accel_v064_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_63d_accel_v065_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_63d_accel_v066_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_126d_accel_v067_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_126d_accel_v068_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_126d_accel_v069_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_252d_accel_v070_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_252d_accel_v071_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_252d_accel_v072_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_504d_accel_v073_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_504d_accel_v074_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_504d_accel_v075_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_21d_accel_v076_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_21d_accel_v077_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_21d_accel_v078_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_63d_accel_v079_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_63d_accel_v080_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_63d_accel_v081_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_126d_accel_v082_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_126d_accel_v083_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_126d_accel_v084_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_252d_accel_v085_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_252d_accel_v086_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_252d_accel_v087_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_504d_accel_v088_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_504d_accel_v089_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_504d_accel_v090_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_21d_accel_v091_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(21).min(), fcf.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_21d_accel_v092_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(21).min(), fcf.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_21d_accel_v093_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(21).min(), fcf.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_63d_accel_v094_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(63).min(), fcf.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_63d_accel_v095_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(63).min(), fcf.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_63d_accel_v096_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(63).min(), fcf.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_126d_accel_v097_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(126).min(), fcf.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_126d_accel_v098_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(126).min(), fcf.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_126d_accel_v099_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(126).min(), fcf.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_252d_accel_v100_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(252).min(), fcf.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_252d_accel_v101_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(252).min(), fcf.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_252d_accel_v102_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(252).min(), fcf.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_504d_accel_v103_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(504).min(), fcf.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_504d_accel_v104_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(504).min(), fcf.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_504d_accel_v105_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(504).min(), fcf.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_21d_accel_v106_signal(fcf):
    base = _safe_div(fcf.rolling(21).max() - fcf, fcf.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_21d_accel_v107_signal(fcf):
    base = _safe_div(fcf.rolling(21).max() - fcf, fcf.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_21d_accel_v108_signal(fcf):
    base = _safe_div(fcf.rolling(21).max() - fcf, fcf.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_63d_accel_v109_signal(fcf):
    base = _safe_div(fcf.rolling(63).max() - fcf, fcf.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_63d_accel_v110_signal(fcf):
    base = _safe_div(fcf.rolling(63).max() - fcf, fcf.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_63d_accel_v111_signal(fcf):
    base = _safe_div(fcf.rolling(63).max() - fcf, fcf.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_126d_accel_v112_signal(fcf):
    base = _safe_div(fcf.rolling(126).max() - fcf, fcf.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_126d_accel_v113_signal(fcf):
    base = _safe_div(fcf.rolling(126).max() - fcf, fcf.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_126d_accel_v114_signal(fcf):
    base = _safe_div(fcf.rolling(126).max() - fcf, fcf.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_252d_accel_v115_signal(fcf):
    base = _safe_div(fcf.rolling(252).max() - fcf, fcf.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_252d_accel_v116_signal(fcf):
    base = _safe_div(fcf.rolling(252).max() - fcf, fcf.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_252d_accel_v117_signal(fcf):
    base = _safe_div(fcf.rolling(252).max() - fcf, fcf.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_504d_accel_v118_signal(fcf):
    base = _safe_div(fcf.rolling(504).max() - fcf, fcf.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_504d_accel_v119_signal(fcf):
    base = _safe_div(fcf.rolling(504).max() - fcf, fcf.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_504d_accel_v120_signal(fcf):
    base = _safe_div(fcf.rolling(504).max() - fcf, fcf.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_21d_accel_v121_signal(fcf):
    base = _safe_div(_mean(fcf, 21) - _mean(fcf, 42), _mean(fcf, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_21d_accel_v122_signal(fcf):
    base = _safe_div(_mean(fcf, 21) - _mean(fcf, 42), _mean(fcf, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_21d_accel_v123_signal(fcf):
    base = _safe_div(_mean(fcf, 21) - _mean(fcf, 42), _mean(fcf, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_63d_accel_v124_signal(fcf):
    base = _safe_div(_mean(fcf, 63) - _mean(fcf, 126), _mean(fcf, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_63d_accel_v125_signal(fcf):
    base = _safe_div(_mean(fcf, 63) - _mean(fcf, 126), _mean(fcf, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_63d_accel_v126_signal(fcf):
    base = _safe_div(_mean(fcf, 63) - _mean(fcf, 126), _mean(fcf, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_126d_accel_v127_signal(fcf):
    base = _safe_div(_mean(fcf, 126) - _mean(fcf, 252), _mean(fcf, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_126d_accel_v128_signal(fcf):
    base = _safe_div(_mean(fcf, 126) - _mean(fcf, 252), _mean(fcf, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_126d_accel_v129_signal(fcf):
    base = _safe_div(_mean(fcf, 126) - _mean(fcf, 252), _mean(fcf, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_252d_accel_v130_signal(fcf):
    base = _safe_div(_mean(fcf, 252) - _mean(fcf, 504), _mean(fcf, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_252d_accel_v131_signal(fcf):
    base = _safe_div(_mean(fcf, 252) - _mean(fcf, 504), _mean(fcf, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_252d_accel_v132_signal(fcf):
    base = _safe_div(_mean(fcf, 252) - _mean(fcf, 504), _mean(fcf, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_504d_accel_v133_signal(fcf):
    base = _safe_div(_mean(fcf, 504) - _mean(fcf, 1008), _mean(fcf, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_504d_accel_v134_signal(fcf):
    base = _safe_div(_mean(fcf, 504) - _mean(fcf, 1008), _mean(fcf, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_504d_accel_v135_signal(fcf):
    base = _safe_div(_mean(fcf, 504) - _mean(fcf, 1008), _mean(fcf, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_21d_accel_v136_signal(fcf):
    base = _std(fcf, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_21d_accel_v137_signal(fcf):
    base = _std(fcf, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_21d_accel_v138_signal(fcf):
    base = _std(fcf, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_63d_accel_v139_signal(fcf):
    base = _std(fcf, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_63d_accel_v140_signal(fcf):
    base = _std(fcf, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_63d_accel_v141_signal(fcf):
    base = _std(fcf, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_126d_accel_v142_signal(fcf):
    base = _std(fcf, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_126d_accel_v143_signal(fcf):
    base = _std(fcf, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_126d_accel_v144_signal(fcf):
    base = _std(fcf, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_252d_accel_v145_signal(fcf):
    base = _std(fcf, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_252d_accel_v146_signal(fcf):
    base = _std(fcf, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_252d_accel_v147_signal(fcf):
    base = _std(fcf, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_504d_accel_v148_signal(fcf):
    base = _std(fcf, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_504d_accel_v149_signal(fcf):
    base = _std(fcf, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_504d_accel_v150_signal(fcf):
    base = _std(fcf, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

