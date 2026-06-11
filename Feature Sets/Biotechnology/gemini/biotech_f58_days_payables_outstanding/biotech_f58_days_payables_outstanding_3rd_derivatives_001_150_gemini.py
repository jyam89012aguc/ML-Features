
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw payables
def gm_f58_biotech_f58_days_payables_outstanding_raw_21d_accel_v001_signal(payables):
    base = _mean(payables, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw payables
def gm_f58_biotech_f58_days_payables_outstanding_raw_21d_accel_v002_signal(payables):
    base = _mean(payables, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw payables
def gm_f58_biotech_f58_days_payables_outstanding_raw_21d_accel_v003_signal(payables):
    base = _mean(payables, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw payables
def gm_f58_biotech_f58_days_payables_outstanding_raw_63d_accel_v004_signal(payables):
    base = _mean(payables, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw payables
def gm_f58_biotech_f58_days_payables_outstanding_raw_63d_accel_v005_signal(payables):
    base = _mean(payables, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw payables
def gm_f58_biotech_f58_days_payables_outstanding_raw_63d_accel_v006_signal(payables):
    base = _mean(payables, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw payables
def gm_f58_biotech_f58_days_payables_outstanding_raw_126d_accel_v007_signal(payables):
    base = _mean(payables, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw payables
def gm_f58_biotech_f58_days_payables_outstanding_raw_126d_accel_v008_signal(payables):
    base = _mean(payables, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw payables
def gm_f58_biotech_f58_days_payables_outstanding_raw_126d_accel_v009_signal(payables):
    base = _mean(payables, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw payables
def gm_f58_biotech_f58_days_payables_outstanding_raw_252d_accel_v010_signal(payables):
    base = _mean(payables, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw payables
def gm_f58_biotech_f58_days_payables_outstanding_raw_252d_accel_v011_signal(payables):
    base = _mean(payables, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw payables
def gm_f58_biotech_f58_days_payables_outstanding_raw_252d_accel_v012_signal(payables):
    base = _mean(payables, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw payables
def gm_f58_biotech_f58_days_payables_outstanding_raw_504d_accel_v013_signal(payables):
    base = _mean(payables, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw payables
def gm_f58_biotech_f58_days_payables_outstanding_raw_504d_accel_v014_signal(payables):
    base = _mean(payables, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw payables
def gm_f58_biotech_f58_days_payables_outstanding_raw_504d_accel_v015_signal(payables):
    base = _mean(payables, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log payables
def gm_f58_biotech_f58_days_payables_outstanding_log_21d_accel_v016_signal(payables):
    base = _mean(_log(payables), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log payables
def gm_f58_biotech_f58_days_payables_outstanding_log_21d_accel_v017_signal(payables):
    base = _mean(_log(payables), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log payables
def gm_f58_biotech_f58_days_payables_outstanding_log_21d_accel_v018_signal(payables):
    base = _mean(_log(payables), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log payables
def gm_f58_biotech_f58_days_payables_outstanding_log_63d_accel_v019_signal(payables):
    base = _mean(_log(payables), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log payables
def gm_f58_biotech_f58_days_payables_outstanding_log_63d_accel_v020_signal(payables):
    base = _mean(_log(payables), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log payables
def gm_f58_biotech_f58_days_payables_outstanding_log_63d_accel_v021_signal(payables):
    base = _mean(_log(payables), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log payables
def gm_f58_biotech_f58_days_payables_outstanding_log_126d_accel_v022_signal(payables):
    base = _mean(_log(payables), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log payables
def gm_f58_biotech_f58_days_payables_outstanding_log_126d_accel_v023_signal(payables):
    base = _mean(_log(payables), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log payables
def gm_f58_biotech_f58_days_payables_outstanding_log_126d_accel_v024_signal(payables):
    base = _mean(_log(payables), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log payables
def gm_f58_biotech_f58_days_payables_outstanding_log_252d_accel_v025_signal(payables):
    base = _mean(_log(payables), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log payables
def gm_f58_biotech_f58_days_payables_outstanding_log_252d_accel_v026_signal(payables):
    base = _mean(_log(payables), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log payables
def gm_f58_biotech_f58_days_payables_outstanding_log_252d_accel_v027_signal(payables):
    base = _mean(_log(payables), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log payables
def gm_f58_biotech_f58_days_payables_outstanding_log_504d_accel_v028_signal(payables):
    base = _mean(_log(payables), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log payables
def gm_f58_biotech_f58_days_payables_outstanding_log_504d_accel_v029_signal(payables):
    base = _mean(_log(payables), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log payables
def gm_f58_biotech_f58_days_payables_outstanding_log_504d_accel_v030_signal(payables):
    base = _mean(_log(payables), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z payables
def gm_f58_biotech_f58_days_payables_outstanding_z_21d_accel_v031_signal(payables):
    base = _z(payables, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z payables
def gm_f58_biotech_f58_days_payables_outstanding_z_21d_accel_v032_signal(payables):
    base = _z(payables, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z payables
def gm_f58_biotech_f58_days_payables_outstanding_z_21d_accel_v033_signal(payables):
    base = _z(payables, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z payables
def gm_f58_biotech_f58_days_payables_outstanding_z_63d_accel_v034_signal(payables):
    base = _z(payables, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z payables
def gm_f58_biotech_f58_days_payables_outstanding_z_63d_accel_v035_signal(payables):
    base = _z(payables, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z payables
def gm_f58_biotech_f58_days_payables_outstanding_z_63d_accel_v036_signal(payables):
    base = _z(payables, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z payables
def gm_f58_biotech_f58_days_payables_outstanding_z_126d_accel_v037_signal(payables):
    base = _z(payables, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z payables
def gm_f58_biotech_f58_days_payables_outstanding_z_126d_accel_v038_signal(payables):
    base = _z(payables, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z payables
def gm_f58_biotech_f58_days_payables_outstanding_z_126d_accel_v039_signal(payables):
    base = _z(payables, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z payables
def gm_f58_biotech_f58_days_payables_outstanding_z_252d_accel_v040_signal(payables):
    base = _z(payables, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z payables
def gm_f58_biotech_f58_days_payables_outstanding_z_252d_accel_v041_signal(payables):
    base = _z(payables, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z payables
def gm_f58_biotech_f58_days_payables_outstanding_z_252d_accel_v042_signal(payables):
    base = _z(payables, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z payables
def gm_f58_biotech_f58_days_payables_outstanding_z_504d_accel_v043_signal(payables):
    base = _z(payables, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z payables
def gm_f58_biotech_f58_days_payables_outstanding_z_504d_accel_v044_signal(payables):
    base = _z(payables, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z payables
def gm_f58_biotech_f58_days_payables_outstanding_z_504d_accel_v045_signal(payables):
    base = _z(payables, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps payables
def gm_f58_biotech_f58_days_payables_outstanding_ps_21d_accel_v046_signal(payables, sharesbas):
    base = _safe_div(_mean(payables, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps payables
def gm_f58_biotech_f58_days_payables_outstanding_ps_21d_accel_v047_signal(payables, sharesbas):
    base = _safe_div(_mean(payables, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps payables
def gm_f58_biotech_f58_days_payables_outstanding_ps_21d_accel_v048_signal(payables, sharesbas):
    base = _safe_div(_mean(payables, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps payables
def gm_f58_biotech_f58_days_payables_outstanding_ps_63d_accel_v049_signal(payables, sharesbas):
    base = _safe_div(_mean(payables, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps payables
def gm_f58_biotech_f58_days_payables_outstanding_ps_63d_accel_v050_signal(payables, sharesbas):
    base = _safe_div(_mean(payables, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps payables
def gm_f58_biotech_f58_days_payables_outstanding_ps_63d_accel_v051_signal(payables, sharesbas):
    base = _safe_div(_mean(payables, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps payables
def gm_f58_biotech_f58_days_payables_outstanding_ps_126d_accel_v052_signal(payables, sharesbas):
    base = _safe_div(_mean(payables, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps payables
def gm_f58_biotech_f58_days_payables_outstanding_ps_126d_accel_v053_signal(payables, sharesbas):
    base = _safe_div(_mean(payables, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps payables
def gm_f58_biotech_f58_days_payables_outstanding_ps_126d_accel_v054_signal(payables, sharesbas):
    base = _safe_div(_mean(payables, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps payables
def gm_f58_biotech_f58_days_payables_outstanding_ps_252d_accel_v055_signal(payables, sharesbas):
    base = _safe_div(_mean(payables, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps payables
def gm_f58_biotech_f58_days_payables_outstanding_ps_252d_accel_v056_signal(payables, sharesbas):
    base = _safe_div(_mean(payables, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps payables
def gm_f58_biotech_f58_days_payables_outstanding_ps_252d_accel_v057_signal(payables, sharesbas):
    base = _safe_div(_mean(payables, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps payables
def gm_f58_biotech_f58_days_payables_outstanding_ps_504d_accel_v058_signal(payables, sharesbas):
    base = _safe_div(_mean(payables, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps payables
def gm_f58_biotech_f58_days_payables_outstanding_ps_504d_accel_v059_signal(payables, sharesbas):
    base = _safe_div(_mean(payables, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps payables
def gm_f58_biotech_f58_days_payables_outstanding_ps_504d_accel_v060_signal(payables, sharesbas):
    base = _safe_div(_mean(payables, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_21d_accel_v061_signal(payables, assets):
    base = _safe_div(_mean(payables, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_21d_accel_v062_signal(payables, assets):
    base = _safe_div(_mean(payables, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_21d_accel_v063_signal(payables, assets):
    base = _safe_div(_mean(payables, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_63d_accel_v064_signal(payables, assets):
    base = _safe_div(_mean(payables, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_63d_accel_v065_signal(payables, assets):
    base = _safe_div(_mean(payables, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_63d_accel_v066_signal(payables, assets):
    base = _safe_div(_mean(payables, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_126d_accel_v067_signal(payables, assets):
    base = _safe_div(_mean(payables, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_126d_accel_v068_signal(payables, assets):
    base = _safe_div(_mean(payables, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_126d_accel_v069_signal(payables, assets):
    base = _safe_div(_mean(payables, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_252d_accel_v070_signal(payables, assets):
    base = _safe_div(_mean(payables, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_252d_accel_v071_signal(payables, assets):
    base = _safe_div(_mean(payables, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_252d_accel_v072_signal(payables, assets):
    base = _safe_div(_mean(payables, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_504d_accel_v073_signal(payables, assets):
    base = _safe_div(_mean(payables, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_504d_accel_v074_signal(payables, assets):
    base = _safe_div(_mean(payables, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_asset_scaled_504d_accel_v075_signal(payables, assets):
    base = _safe_div(_mean(payables, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_21d_accel_v076_signal(payables, marketcap):
    base = _safe_div(_mean(payables, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_21d_accel_v077_signal(payables, marketcap):
    base = _safe_div(_mean(payables, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_21d_accel_v078_signal(payables, marketcap):
    base = _safe_div(_mean(payables, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_63d_accel_v079_signal(payables, marketcap):
    base = _safe_div(_mean(payables, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_63d_accel_v080_signal(payables, marketcap):
    base = _safe_div(_mean(payables, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_63d_accel_v081_signal(payables, marketcap):
    base = _safe_div(_mean(payables, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_126d_accel_v082_signal(payables, marketcap):
    base = _safe_div(_mean(payables, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_126d_accel_v083_signal(payables, marketcap):
    base = _safe_div(_mean(payables, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_126d_accel_v084_signal(payables, marketcap):
    base = _safe_div(_mean(payables, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_252d_accel_v085_signal(payables, marketcap):
    base = _safe_div(_mean(payables, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_252d_accel_v086_signal(payables, marketcap):
    base = _safe_div(_mean(payables, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_252d_accel_v087_signal(payables, marketcap):
    base = _safe_div(_mean(payables, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_504d_accel_v088_signal(payables, marketcap):
    base = _safe_div(_mean(payables, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_504d_accel_v089_signal(payables, marketcap):
    base = _safe_div(_mean(payables, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled payables
def gm_f58_biotech_f58_days_payables_outstanding_mcap_scaled_504d_accel_v090_signal(payables, marketcap):
    base = _safe_div(_mean(payables, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_21d_accel_v091_signal(payables):
    base = _safe_div(payables - payables.rolling(21).min(), payables.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_21d_accel_v092_signal(payables):
    base = _safe_div(payables - payables.rolling(21).min(), payables.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_21d_accel_v093_signal(payables):
    base = _safe_div(payables - payables.rolling(21).min(), payables.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_63d_accel_v094_signal(payables):
    base = _safe_div(payables - payables.rolling(63).min(), payables.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_63d_accel_v095_signal(payables):
    base = _safe_div(payables - payables.rolling(63).min(), payables.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_63d_accel_v096_signal(payables):
    base = _safe_div(payables - payables.rolling(63).min(), payables.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_126d_accel_v097_signal(payables):
    base = _safe_div(payables - payables.rolling(126).min(), payables.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_126d_accel_v098_signal(payables):
    base = _safe_div(payables - payables.rolling(126).min(), payables.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_126d_accel_v099_signal(payables):
    base = _safe_div(payables - payables.rolling(126).min(), payables.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_252d_accel_v100_signal(payables):
    base = _safe_div(payables - payables.rolling(252).min(), payables.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_252d_accel_v101_signal(payables):
    base = _safe_div(payables - payables.rolling(252).min(), payables.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_252d_accel_v102_signal(payables):
    base = _safe_div(payables - payables.rolling(252).min(), payables.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_504d_accel_v103_signal(payables):
    base = _safe_div(payables - payables.rolling(504).min(), payables.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_504d_accel_v104_signal(payables):
    base = _safe_div(payables - payables.rolling(504).min(), payables.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_low_504d_accel_v105_signal(payables):
    base = _safe_div(payables - payables.rolling(504).min(), payables.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_21d_accel_v106_signal(payables):
    base = _safe_div(payables.rolling(21).max() - payables, payables.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_21d_accel_v107_signal(payables):
    base = _safe_div(payables.rolling(21).max() - payables, payables.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_21d_accel_v108_signal(payables):
    base = _safe_div(payables.rolling(21).max() - payables, payables.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_63d_accel_v109_signal(payables):
    base = _safe_div(payables.rolling(63).max() - payables, payables.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_63d_accel_v110_signal(payables):
    base = _safe_div(payables.rolling(63).max() - payables, payables.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_63d_accel_v111_signal(payables):
    base = _safe_div(payables.rolling(63).max() - payables, payables.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_126d_accel_v112_signal(payables):
    base = _safe_div(payables.rolling(126).max() - payables, payables.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_126d_accel_v113_signal(payables):
    base = _safe_div(payables.rolling(126).max() - payables, payables.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_126d_accel_v114_signal(payables):
    base = _safe_div(payables.rolling(126).max() - payables, payables.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_252d_accel_v115_signal(payables):
    base = _safe_div(payables.rolling(252).max() - payables, payables.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_252d_accel_v116_signal(payables):
    base = _safe_div(payables.rolling(252).max() - payables, payables.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_252d_accel_v117_signal(payables):
    base = _safe_div(payables.rolling(252).max() - payables, payables.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_504d_accel_v118_signal(payables):
    base = _safe_div(payables.rolling(504).max() - payables, payables.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_504d_accel_v119_signal(payables):
    base = _safe_div(payables.rolling(504).max() - payables, payables.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high payables
def gm_f58_biotech_f58_days_payables_outstanding_dist_high_504d_accel_v120_signal(payables):
    base = _safe_div(payables.rolling(504).max() - payables, payables.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom payables
def gm_f58_biotech_f58_days_payables_outstanding_mom_21d_accel_v121_signal(payables):
    base = _safe_div(_mean(payables, 21) - _mean(payables, 42), _mean(payables, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom payables
def gm_f58_biotech_f58_days_payables_outstanding_mom_21d_accel_v122_signal(payables):
    base = _safe_div(_mean(payables, 21) - _mean(payables, 42), _mean(payables, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom payables
def gm_f58_biotech_f58_days_payables_outstanding_mom_21d_accel_v123_signal(payables):
    base = _safe_div(_mean(payables, 21) - _mean(payables, 42), _mean(payables, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom payables
def gm_f58_biotech_f58_days_payables_outstanding_mom_63d_accel_v124_signal(payables):
    base = _safe_div(_mean(payables, 63) - _mean(payables, 126), _mean(payables, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom payables
def gm_f58_biotech_f58_days_payables_outstanding_mom_63d_accel_v125_signal(payables):
    base = _safe_div(_mean(payables, 63) - _mean(payables, 126), _mean(payables, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom payables
def gm_f58_biotech_f58_days_payables_outstanding_mom_63d_accel_v126_signal(payables):
    base = _safe_div(_mean(payables, 63) - _mean(payables, 126), _mean(payables, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom payables
def gm_f58_biotech_f58_days_payables_outstanding_mom_126d_accel_v127_signal(payables):
    base = _safe_div(_mean(payables, 126) - _mean(payables, 252), _mean(payables, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom payables
def gm_f58_biotech_f58_days_payables_outstanding_mom_126d_accel_v128_signal(payables):
    base = _safe_div(_mean(payables, 126) - _mean(payables, 252), _mean(payables, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom payables
def gm_f58_biotech_f58_days_payables_outstanding_mom_126d_accel_v129_signal(payables):
    base = _safe_div(_mean(payables, 126) - _mean(payables, 252), _mean(payables, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom payables
def gm_f58_biotech_f58_days_payables_outstanding_mom_252d_accel_v130_signal(payables):
    base = _safe_div(_mean(payables, 252) - _mean(payables, 504), _mean(payables, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom payables
def gm_f58_biotech_f58_days_payables_outstanding_mom_252d_accel_v131_signal(payables):
    base = _safe_div(_mean(payables, 252) - _mean(payables, 504), _mean(payables, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom payables
def gm_f58_biotech_f58_days_payables_outstanding_mom_252d_accel_v132_signal(payables):
    base = _safe_div(_mean(payables, 252) - _mean(payables, 504), _mean(payables, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom payables
def gm_f58_biotech_f58_days_payables_outstanding_mom_504d_accel_v133_signal(payables):
    base = _safe_div(_mean(payables, 504) - _mean(payables, 1008), _mean(payables, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom payables
def gm_f58_biotech_f58_days_payables_outstanding_mom_504d_accel_v134_signal(payables):
    base = _safe_div(_mean(payables, 504) - _mean(payables, 1008), _mean(payables, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom payables
def gm_f58_biotech_f58_days_payables_outstanding_mom_504d_accel_v135_signal(payables):
    base = _safe_div(_mean(payables, 504) - _mean(payables, 1008), _mean(payables, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol payables
def gm_f58_biotech_f58_days_payables_outstanding_vol_21d_accel_v136_signal(payables):
    base = _std(payables, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol payables
def gm_f58_biotech_f58_days_payables_outstanding_vol_21d_accel_v137_signal(payables):
    base = _std(payables, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol payables
def gm_f58_biotech_f58_days_payables_outstanding_vol_21d_accel_v138_signal(payables):
    base = _std(payables, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol payables
def gm_f58_biotech_f58_days_payables_outstanding_vol_63d_accel_v139_signal(payables):
    base = _std(payables, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol payables
def gm_f58_biotech_f58_days_payables_outstanding_vol_63d_accel_v140_signal(payables):
    base = _std(payables, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol payables
def gm_f58_biotech_f58_days_payables_outstanding_vol_63d_accel_v141_signal(payables):
    base = _std(payables, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol payables
def gm_f58_biotech_f58_days_payables_outstanding_vol_126d_accel_v142_signal(payables):
    base = _std(payables, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol payables
def gm_f58_biotech_f58_days_payables_outstanding_vol_126d_accel_v143_signal(payables):
    base = _std(payables, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol payables
def gm_f58_biotech_f58_days_payables_outstanding_vol_126d_accel_v144_signal(payables):
    base = _std(payables, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol payables
def gm_f58_biotech_f58_days_payables_outstanding_vol_252d_accel_v145_signal(payables):
    base = _std(payables, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol payables
def gm_f58_biotech_f58_days_payables_outstanding_vol_252d_accel_v146_signal(payables):
    base = _std(payables, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol payables
def gm_f58_biotech_f58_days_payables_outstanding_vol_252d_accel_v147_signal(payables):
    base = _std(payables, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol payables
def gm_f58_biotech_f58_days_payables_outstanding_vol_504d_accel_v148_signal(payables):
    base = _std(payables, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol payables
def gm_f58_biotech_f58_days_payables_outstanding_vol_504d_accel_v149_signal(payables):
    base = _std(payables, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol payables
def gm_f58_biotech_f58_days_payables_outstanding_vol_504d_accel_v150_signal(payables):
    base = _std(payables, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

