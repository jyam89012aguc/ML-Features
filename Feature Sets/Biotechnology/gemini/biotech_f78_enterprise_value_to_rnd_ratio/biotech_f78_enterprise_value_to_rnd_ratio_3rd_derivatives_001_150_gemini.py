
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_21d_accel_v001_signal(ev):
    base = _mean(ev, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_21d_accel_v002_signal(ev):
    base = _mean(ev, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_21d_accel_v003_signal(ev):
    base = _mean(ev, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_63d_accel_v004_signal(ev):
    base = _mean(ev, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_63d_accel_v005_signal(ev):
    base = _mean(ev, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_63d_accel_v006_signal(ev):
    base = _mean(ev, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_126d_accel_v007_signal(ev):
    base = _mean(ev, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_126d_accel_v008_signal(ev):
    base = _mean(ev, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_126d_accel_v009_signal(ev):
    base = _mean(ev, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_252d_accel_v010_signal(ev):
    base = _mean(ev, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_252d_accel_v011_signal(ev):
    base = _mean(ev, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_252d_accel_v012_signal(ev):
    base = _mean(ev, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_504d_accel_v013_signal(ev):
    base = _mean(ev, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_504d_accel_v014_signal(ev):
    base = _mean(ev, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_504d_accel_v015_signal(ev):
    base = _mean(ev, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_21d_accel_v016_signal(ev):
    base = _mean(_log(ev), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_21d_accel_v017_signal(ev):
    base = _mean(_log(ev), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_21d_accel_v018_signal(ev):
    base = _mean(_log(ev), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_63d_accel_v019_signal(ev):
    base = _mean(_log(ev), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_63d_accel_v020_signal(ev):
    base = _mean(_log(ev), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_63d_accel_v021_signal(ev):
    base = _mean(_log(ev), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_126d_accel_v022_signal(ev):
    base = _mean(_log(ev), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_126d_accel_v023_signal(ev):
    base = _mean(_log(ev), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_126d_accel_v024_signal(ev):
    base = _mean(_log(ev), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_252d_accel_v025_signal(ev):
    base = _mean(_log(ev), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_252d_accel_v026_signal(ev):
    base = _mean(_log(ev), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_252d_accel_v027_signal(ev):
    base = _mean(_log(ev), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_504d_accel_v028_signal(ev):
    base = _mean(_log(ev), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_504d_accel_v029_signal(ev):
    base = _mean(_log(ev), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_504d_accel_v030_signal(ev):
    base = _mean(_log(ev), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_21d_accel_v031_signal(ev):
    base = _z(ev, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_21d_accel_v032_signal(ev):
    base = _z(ev, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_21d_accel_v033_signal(ev):
    base = _z(ev, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_63d_accel_v034_signal(ev):
    base = _z(ev, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_63d_accel_v035_signal(ev):
    base = _z(ev, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_63d_accel_v036_signal(ev):
    base = _z(ev, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_126d_accel_v037_signal(ev):
    base = _z(ev, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_126d_accel_v038_signal(ev):
    base = _z(ev, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_126d_accel_v039_signal(ev):
    base = _z(ev, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_252d_accel_v040_signal(ev):
    base = _z(ev, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_252d_accel_v041_signal(ev):
    base = _z(ev, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_252d_accel_v042_signal(ev):
    base = _z(ev, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_504d_accel_v043_signal(ev):
    base = _z(ev, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_504d_accel_v044_signal(ev):
    base = _z(ev, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_504d_accel_v045_signal(ev):
    base = _z(ev, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_21d_accel_v046_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_21d_accel_v047_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_21d_accel_v048_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_63d_accel_v049_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_63d_accel_v050_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_63d_accel_v051_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_126d_accel_v052_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_126d_accel_v053_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_126d_accel_v054_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_252d_accel_v055_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_252d_accel_v056_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_252d_accel_v057_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_504d_accel_v058_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_504d_accel_v059_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_504d_accel_v060_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_21d_accel_v061_signal(ev, assets):
    base = _safe_div(_mean(ev, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_21d_accel_v062_signal(ev, assets):
    base = _safe_div(_mean(ev, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_21d_accel_v063_signal(ev, assets):
    base = _safe_div(_mean(ev, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_63d_accel_v064_signal(ev, assets):
    base = _safe_div(_mean(ev, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_63d_accel_v065_signal(ev, assets):
    base = _safe_div(_mean(ev, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_63d_accel_v066_signal(ev, assets):
    base = _safe_div(_mean(ev, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_126d_accel_v067_signal(ev, assets):
    base = _safe_div(_mean(ev, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_126d_accel_v068_signal(ev, assets):
    base = _safe_div(_mean(ev, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_126d_accel_v069_signal(ev, assets):
    base = _safe_div(_mean(ev, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_252d_accel_v070_signal(ev, assets):
    base = _safe_div(_mean(ev, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_252d_accel_v071_signal(ev, assets):
    base = _safe_div(_mean(ev, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_252d_accel_v072_signal(ev, assets):
    base = _safe_div(_mean(ev, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_504d_accel_v073_signal(ev, assets):
    base = _safe_div(_mean(ev, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_504d_accel_v074_signal(ev, assets):
    base = _safe_div(_mean(ev, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_504d_accel_v075_signal(ev, assets):
    base = _safe_div(_mean(ev, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_21d_accel_v076_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_21d_accel_v077_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_21d_accel_v078_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_63d_accel_v079_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_63d_accel_v080_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_63d_accel_v081_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_126d_accel_v082_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_126d_accel_v083_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_126d_accel_v084_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_252d_accel_v085_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_252d_accel_v086_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_252d_accel_v087_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_504d_accel_v088_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_504d_accel_v089_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_504d_accel_v090_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_21d_accel_v091_signal(ev):
    base = _safe_div(ev - ev.rolling(21).min(), ev.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_21d_accel_v092_signal(ev):
    base = _safe_div(ev - ev.rolling(21).min(), ev.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_21d_accel_v093_signal(ev):
    base = _safe_div(ev - ev.rolling(21).min(), ev.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_63d_accel_v094_signal(ev):
    base = _safe_div(ev - ev.rolling(63).min(), ev.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_63d_accel_v095_signal(ev):
    base = _safe_div(ev - ev.rolling(63).min(), ev.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_63d_accel_v096_signal(ev):
    base = _safe_div(ev - ev.rolling(63).min(), ev.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_126d_accel_v097_signal(ev):
    base = _safe_div(ev - ev.rolling(126).min(), ev.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_126d_accel_v098_signal(ev):
    base = _safe_div(ev - ev.rolling(126).min(), ev.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_126d_accel_v099_signal(ev):
    base = _safe_div(ev - ev.rolling(126).min(), ev.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_252d_accel_v100_signal(ev):
    base = _safe_div(ev - ev.rolling(252).min(), ev.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_252d_accel_v101_signal(ev):
    base = _safe_div(ev - ev.rolling(252).min(), ev.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_252d_accel_v102_signal(ev):
    base = _safe_div(ev - ev.rolling(252).min(), ev.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_504d_accel_v103_signal(ev):
    base = _safe_div(ev - ev.rolling(504).min(), ev.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_504d_accel_v104_signal(ev):
    base = _safe_div(ev - ev.rolling(504).min(), ev.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_504d_accel_v105_signal(ev):
    base = _safe_div(ev - ev.rolling(504).min(), ev.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_21d_accel_v106_signal(ev):
    base = _safe_div(ev.rolling(21).max() - ev, ev.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_21d_accel_v107_signal(ev):
    base = _safe_div(ev.rolling(21).max() - ev, ev.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_21d_accel_v108_signal(ev):
    base = _safe_div(ev.rolling(21).max() - ev, ev.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_63d_accel_v109_signal(ev):
    base = _safe_div(ev.rolling(63).max() - ev, ev.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_63d_accel_v110_signal(ev):
    base = _safe_div(ev.rolling(63).max() - ev, ev.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_63d_accel_v111_signal(ev):
    base = _safe_div(ev.rolling(63).max() - ev, ev.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_126d_accel_v112_signal(ev):
    base = _safe_div(ev.rolling(126).max() - ev, ev.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_126d_accel_v113_signal(ev):
    base = _safe_div(ev.rolling(126).max() - ev, ev.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_126d_accel_v114_signal(ev):
    base = _safe_div(ev.rolling(126).max() - ev, ev.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_252d_accel_v115_signal(ev):
    base = _safe_div(ev.rolling(252).max() - ev, ev.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_252d_accel_v116_signal(ev):
    base = _safe_div(ev.rolling(252).max() - ev, ev.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_252d_accel_v117_signal(ev):
    base = _safe_div(ev.rolling(252).max() - ev, ev.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_504d_accel_v118_signal(ev):
    base = _safe_div(ev.rolling(504).max() - ev, ev.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_504d_accel_v119_signal(ev):
    base = _safe_div(ev.rolling(504).max() - ev, ev.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_504d_accel_v120_signal(ev):
    base = _safe_div(ev.rolling(504).max() - ev, ev.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_21d_accel_v121_signal(ev):
    base = _safe_div(_mean(ev, 21) - _mean(ev, 42), _mean(ev, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_21d_accel_v122_signal(ev):
    base = _safe_div(_mean(ev, 21) - _mean(ev, 42), _mean(ev, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_21d_accel_v123_signal(ev):
    base = _safe_div(_mean(ev, 21) - _mean(ev, 42), _mean(ev, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_63d_accel_v124_signal(ev):
    base = _safe_div(_mean(ev, 63) - _mean(ev, 126), _mean(ev, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_63d_accel_v125_signal(ev):
    base = _safe_div(_mean(ev, 63) - _mean(ev, 126), _mean(ev, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_63d_accel_v126_signal(ev):
    base = _safe_div(_mean(ev, 63) - _mean(ev, 126), _mean(ev, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_126d_accel_v127_signal(ev):
    base = _safe_div(_mean(ev, 126) - _mean(ev, 252), _mean(ev, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_126d_accel_v128_signal(ev):
    base = _safe_div(_mean(ev, 126) - _mean(ev, 252), _mean(ev, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_126d_accel_v129_signal(ev):
    base = _safe_div(_mean(ev, 126) - _mean(ev, 252), _mean(ev, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_252d_accel_v130_signal(ev):
    base = _safe_div(_mean(ev, 252) - _mean(ev, 504), _mean(ev, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_252d_accel_v131_signal(ev):
    base = _safe_div(_mean(ev, 252) - _mean(ev, 504), _mean(ev, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_252d_accel_v132_signal(ev):
    base = _safe_div(_mean(ev, 252) - _mean(ev, 504), _mean(ev, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_504d_accel_v133_signal(ev):
    base = _safe_div(_mean(ev, 504) - _mean(ev, 1008), _mean(ev, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_504d_accel_v134_signal(ev):
    base = _safe_div(_mean(ev, 504) - _mean(ev, 1008), _mean(ev, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_504d_accel_v135_signal(ev):
    base = _safe_div(_mean(ev, 504) - _mean(ev, 1008), _mean(ev, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_21d_accel_v136_signal(ev):
    base = _std(ev, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_21d_accel_v137_signal(ev):
    base = _std(ev, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_21d_accel_v138_signal(ev):
    base = _std(ev, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_63d_accel_v139_signal(ev):
    base = _std(ev, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_63d_accel_v140_signal(ev):
    base = _std(ev, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_63d_accel_v141_signal(ev):
    base = _std(ev, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_126d_accel_v142_signal(ev):
    base = _std(ev, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_126d_accel_v143_signal(ev):
    base = _std(ev, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_126d_accel_v144_signal(ev):
    base = _std(ev, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_252d_accel_v145_signal(ev):
    base = _std(ev, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_252d_accel_v146_signal(ev):
    base = _std(ev, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_252d_accel_v147_signal(ev):
    base = _std(ev, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_504d_accel_v148_signal(ev):
    base = _std(ev, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_504d_accel_v149_signal(ev):
    base = _std(ev, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_504d_accel_v150_signal(ev):
    base = _std(ev, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

