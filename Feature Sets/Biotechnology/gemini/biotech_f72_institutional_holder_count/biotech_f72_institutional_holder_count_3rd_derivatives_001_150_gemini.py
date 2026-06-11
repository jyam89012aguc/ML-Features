
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_21d_accel_v001_signal(investorname):
    base = _mean(investorname, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_21d_accel_v002_signal(investorname):
    base = _mean(investorname, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_21d_accel_v003_signal(investorname):
    base = _mean(investorname, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_63d_accel_v004_signal(investorname):
    base = _mean(investorname, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_63d_accel_v005_signal(investorname):
    base = _mean(investorname, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_63d_accel_v006_signal(investorname):
    base = _mean(investorname, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_126d_accel_v007_signal(investorname):
    base = _mean(investorname, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_126d_accel_v008_signal(investorname):
    base = _mean(investorname, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_126d_accel_v009_signal(investorname):
    base = _mean(investorname, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_252d_accel_v010_signal(investorname):
    base = _mean(investorname, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_252d_accel_v011_signal(investorname):
    base = _mean(investorname, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_252d_accel_v012_signal(investorname):
    base = _mean(investorname, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_504d_accel_v013_signal(investorname):
    base = _mean(investorname, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_504d_accel_v014_signal(investorname):
    base = _mean(investorname, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_504d_accel_v015_signal(investorname):
    base = _mean(investorname, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_21d_accel_v016_signal(investorname):
    base = _mean(_log(investorname), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_21d_accel_v017_signal(investorname):
    base = _mean(_log(investorname), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_21d_accel_v018_signal(investorname):
    base = _mean(_log(investorname), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_63d_accel_v019_signal(investorname):
    base = _mean(_log(investorname), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_63d_accel_v020_signal(investorname):
    base = _mean(_log(investorname), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_63d_accel_v021_signal(investorname):
    base = _mean(_log(investorname), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_126d_accel_v022_signal(investorname):
    base = _mean(_log(investorname), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_126d_accel_v023_signal(investorname):
    base = _mean(_log(investorname), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_126d_accel_v024_signal(investorname):
    base = _mean(_log(investorname), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_252d_accel_v025_signal(investorname):
    base = _mean(_log(investorname), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_252d_accel_v026_signal(investorname):
    base = _mean(_log(investorname), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_252d_accel_v027_signal(investorname):
    base = _mean(_log(investorname), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_504d_accel_v028_signal(investorname):
    base = _mean(_log(investorname), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_504d_accel_v029_signal(investorname):
    base = _mean(_log(investorname), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_504d_accel_v030_signal(investorname):
    base = _mean(_log(investorname), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_21d_accel_v031_signal(investorname):
    base = _z(investorname, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_21d_accel_v032_signal(investorname):
    base = _z(investorname, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_21d_accel_v033_signal(investorname):
    base = _z(investorname, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_63d_accel_v034_signal(investorname):
    base = _z(investorname, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_63d_accel_v035_signal(investorname):
    base = _z(investorname, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_63d_accel_v036_signal(investorname):
    base = _z(investorname, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_126d_accel_v037_signal(investorname):
    base = _z(investorname, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_126d_accel_v038_signal(investorname):
    base = _z(investorname, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_126d_accel_v039_signal(investorname):
    base = _z(investorname, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_252d_accel_v040_signal(investorname):
    base = _z(investorname, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_252d_accel_v041_signal(investorname):
    base = _z(investorname, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_252d_accel_v042_signal(investorname):
    base = _z(investorname, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_504d_accel_v043_signal(investorname):
    base = _z(investorname, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_504d_accel_v044_signal(investorname):
    base = _z(investorname, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_504d_accel_v045_signal(investorname):
    base = _z(investorname, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_21d_accel_v046_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_21d_accel_v047_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_21d_accel_v048_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_63d_accel_v049_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_63d_accel_v050_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_63d_accel_v051_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_126d_accel_v052_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_126d_accel_v053_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_126d_accel_v054_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_252d_accel_v055_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_252d_accel_v056_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_252d_accel_v057_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_504d_accel_v058_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_504d_accel_v059_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_504d_accel_v060_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_21d_accel_v061_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_21d_accel_v062_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_21d_accel_v063_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_63d_accel_v064_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_63d_accel_v065_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_63d_accel_v066_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_126d_accel_v067_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_126d_accel_v068_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_126d_accel_v069_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_252d_accel_v070_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_252d_accel_v071_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_252d_accel_v072_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_504d_accel_v073_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_504d_accel_v074_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_504d_accel_v075_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_21d_accel_v076_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_21d_accel_v077_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_21d_accel_v078_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_63d_accel_v079_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_63d_accel_v080_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_63d_accel_v081_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_126d_accel_v082_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_126d_accel_v083_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_126d_accel_v084_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_252d_accel_v085_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_252d_accel_v086_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_252d_accel_v087_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_504d_accel_v088_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_504d_accel_v089_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_504d_accel_v090_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_21d_accel_v091_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(21).min(), investorname.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_21d_accel_v092_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(21).min(), investorname.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_21d_accel_v093_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(21).min(), investorname.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_63d_accel_v094_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(63).min(), investorname.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_63d_accel_v095_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(63).min(), investorname.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_63d_accel_v096_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(63).min(), investorname.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_126d_accel_v097_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(126).min(), investorname.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_126d_accel_v098_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(126).min(), investorname.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_126d_accel_v099_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(126).min(), investorname.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_252d_accel_v100_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(252).min(), investorname.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_252d_accel_v101_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(252).min(), investorname.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_252d_accel_v102_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(252).min(), investorname.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_504d_accel_v103_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(504).min(), investorname.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_504d_accel_v104_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(504).min(), investorname.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_504d_accel_v105_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(504).min(), investorname.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_21d_accel_v106_signal(investorname):
    base = _safe_div(investorname.rolling(21).max() - investorname, investorname.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_21d_accel_v107_signal(investorname):
    base = _safe_div(investorname.rolling(21).max() - investorname, investorname.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_21d_accel_v108_signal(investorname):
    base = _safe_div(investorname.rolling(21).max() - investorname, investorname.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_63d_accel_v109_signal(investorname):
    base = _safe_div(investorname.rolling(63).max() - investorname, investorname.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_63d_accel_v110_signal(investorname):
    base = _safe_div(investorname.rolling(63).max() - investorname, investorname.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_63d_accel_v111_signal(investorname):
    base = _safe_div(investorname.rolling(63).max() - investorname, investorname.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_126d_accel_v112_signal(investorname):
    base = _safe_div(investorname.rolling(126).max() - investorname, investorname.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_126d_accel_v113_signal(investorname):
    base = _safe_div(investorname.rolling(126).max() - investorname, investorname.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_126d_accel_v114_signal(investorname):
    base = _safe_div(investorname.rolling(126).max() - investorname, investorname.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_252d_accel_v115_signal(investorname):
    base = _safe_div(investorname.rolling(252).max() - investorname, investorname.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_252d_accel_v116_signal(investorname):
    base = _safe_div(investorname.rolling(252).max() - investorname, investorname.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_252d_accel_v117_signal(investorname):
    base = _safe_div(investorname.rolling(252).max() - investorname, investorname.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_504d_accel_v118_signal(investorname):
    base = _safe_div(investorname.rolling(504).max() - investorname, investorname.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_504d_accel_v119_signal(investorname):
    base = _safe_div(investorname.rolling(504).max() - investorname, investorname.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_504d_accel_v120_signal(investorname):
    base = _safe_div(investorname.rolling(504).max() - investorname, investorname.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_21d_accel_v121_signal(investorname):
    base = _safe_div(_mean(investorname, 21) - _mean(investorname, 42), _mean(investorname, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_21d_accel_v122_signal(investorname):
    base = _safe_div(_mean(investorname, 21) - _mean(investorname, 42), _mean(investorname, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_21d_accel_v123_signal(investorname):
    base = _safe_div(_mean(investorname, 21) - _mean(investorname, 42), _mean(investorname, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_63d_accel_v124_signal(investorname):
    base = _safe_div(_mean(investorname, 63) - _mean(investorname, 126), _mean(investorname, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_63d_accel_v125_signal(investorname):
    base = _safe_div(_mean(investorname, 63) - _mean(investorname, 126), _mean(investorname, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_63d_accel_v126_signal(investorname):
    base = _safe_div(_mean(investorname, 63) - _mean(investorname, 126), _mean(investorname, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_126d_accel_v127_signal(investorname):
    base = _safe_div(_mean(investorname, 126) - _mean(investorname, 252), _mean(investorname, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_126d_accel_v128_signal(investorname):
    base = _safe_div(_mean(investorname, 126) - _mean(investorname, 252), _mean(investorname, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_126d_accel_v129_signal(investorname):
    base = _safe_div(_mean(investorname, 126) - _mean(investorname, 252), _mean(investorname, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_252d_accel_v130_signal(investorname):
    base = _safe_div(_mean(investorname, 252) - _mean(investorname, 504), _mean(investorname, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_252d_accel_v131_signal(investorname):
    base = _safe_div(_mean(investorname, 252) - _mean(investorname, 504), _mean(investorname, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_252d_accel_v132_signal(investorname):
    base = _safe_div(_mean(investorname, 252) - _mean(investorname, 504), _mean(investorname, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_504d_accel_v133_signal(investorname):
    base = _safe_div(_mean(investorname, 504) - _mean(investorname, 1008), _mean(investorname, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_504d_accel_v134_signal(investorname):
    base = _safe_div(_mean(investorname, 504) - _mean(investorname, 1008), _mean(investorname, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_504d_accel_v135_signal(investorname):
    base = _safe_div(_mean(investorname, 504) - _mean(investorname, 1008), _mean(investorname, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_21d_accel_v136_signal(investorname):
    base = _std(investorname, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_21d_accel_v137_signal(investorname):
    base = _std(investorname, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_21d_accel_v138_signal(investorname):
    base = _std(investorname, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_63d_accel_v139_signal(investorname):
    base = _std(investorname, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_63d_accel_v140_signal(investorname):
    base = _std(investorname, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_63d_accel_v141_signal(investorname):
    base = _std(investorname, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_126d_accel_v142_signal(investorname):
    base = _std(investorname, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_126d_accel_v143_signal(investorname):
    base = _std(investorname, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_126d_accel_v144_signal(investorname):
    base = _std(investorname, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_252d_accel_v145_signal(investorname):
    base = _std(investorname, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_252d_accel_v146_signal(investorname):
    base = _std(investorname, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_252d_accel_v147_signal(investorname):
    base = _std(investorname, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_504d_accel_v148_signal(investorname):
    base = _std(investorname, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_504d_accel_v149_signal(investorname):
    base = _std(investorname, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_504d_accel_v150_signal(investorname):
    base = _std(investorname, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

