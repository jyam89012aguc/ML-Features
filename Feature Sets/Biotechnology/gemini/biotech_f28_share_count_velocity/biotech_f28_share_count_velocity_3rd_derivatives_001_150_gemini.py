
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_21d_accel_v001_signal(sharesbas):
    base = _mean(sharesbas, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_21d_accel_v002_signal(sharesbas):
    base = _mean(sharesbas, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_21d_accel_v003_signal(sharesbas):
    base = _mean(sharesbas, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_63d_accel_v004_signal(sharesbas):
    base = _mean(sharesbas, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_63d_accel_v005_signal(sharesbas):
    base = _mean(sharesbas, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_63d_accel_v006_signal(sharesbas):
    base = _mean(sharesbas, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_126d_accel_v007_signal(sharesbas):
    base = _mean(sharesbas, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_126d_accel_v008_signal(sharesbas):
    base = _mean(sharesbas, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_126d_accel_v009_signal(sharesbas):
    base = _mean(sharesbas, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_252d_accel_v010_signal(sharesbas):
    base = _mean(sharesbas, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_252d_accel_v011_signal(sharesbas):
    base = _mean(sharesbas, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_252d_accel_v012_signal(sharesbas):
    base = _mean(sharesbas, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_504d_accel_v013_signal(sharesbas):
    base = _mean(sharesbas, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_504d_accel_v014_signal(sharesbas):
    base = _mean(sharesbas, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw sharesbas
def gm_f28_biotech_f28_share_count_velocity_raw_504d_accel_v015_signal(sharesbas):
    base = _mean(sharesbas, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_21d_accel_v016_signal(sharesbas):
    base = _mean(_log(sharesbas), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_21d_accel_v017_signal(sharesbas):
    base = _mean(_log(sharesbas), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_21d_accel_v018_signal(sharesbas):
    base = _mean(_log(sharesbas), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_63d_accel_v019_signal(sharesbas):
    base = _mean(_log(sharesbas), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_63d_accel_v020_signal(sharesbas):
    base = _mean(_log(sharesbas), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_63d_accel_v021_signal(sharesbas):
    base = _mean(_log(sharesbas), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_126d_accel_v022_signal(sharesbas):
    base = _mean(_log(sharesbas), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_126d_accel_v023_signal(sharesbas):
    base = _mean(_log(sharesbas), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_126d_accel_v024_signal(sharesbas):
    base = _mean(_log(sharesbas), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_252d_accel_v025_signal(sharesbas):
    base = _mean(_log(sharesbas), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_252d_accel_v026_signal(sharesbas):
    base = _mean(_log(sharesbas), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_252d_accel_v027_signal(sharesbas):
    base = _mean(_log(sharesbas), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_504d_accel_v028_signal(sharesbas):
    base = _mean(_log(sharesbas), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_504d_accel_v029_signal(sharesbas):
    base = _mean(_log(sharesbas), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log sharesbas
def gm_f28_biotech_f28_share_count_velocity_log_504d_accel_v030_signal(sharesbas):
    base = _mean(_log(sharesbas), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_21d_accel_v031_signal(sharesbas):
    base = _z(sharesbas, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_21d_accel_v032_signal(sharesbas):
    base = _z(sharesbas, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_21d_accel_v033_signal(sharesbas):
    base = _z(sharesbas, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_63d_accel_v034_signal(sharesbas):
    base = _z(sharesbas, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_63d_accel_v035_signal(sharesbas):
    base = _z(sharesbas, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_63d_accel_v036_signal(sharesbas):
    base = _z(sharesbas, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_126d_accel_v037_signal(sharesbas):
    base = _z(sharesbas, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_126d_accel_v038_signal(sharesbas):
    base = _z(sharesbas, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_126d_accel_v039_signal(sharesbas):
    base = _z(sharesbas, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_252d_accel_v040_signal(sharesbas):
    base = _z(sharesbas, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_252d_accel_v041_signal(sharesbas):
    base = _z(sharesbas, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_252d_accel_v042_signal(sharesbas):
    base = _z(sharesbas, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_504d_accel_v043_signal(sharesbas):
    base = _z(sharesbas, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_504d_accel_v044_signal(sharesbas):
    base = _z(sharesbas, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z sharesbas
def gm_f28_biotech_f28_share_count_velocity_z_504d_accel_v045_signal(sharesbas):
    base = _z(sharesbas, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_21d_accel_v046_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_21d_accel_v047_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_21d_accel_v048_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_63d_accel_v049_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_63d_accel_v050_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_63d_accel_v051_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_126d_accel_v052_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_126d_accel_v053_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_126d_accel_v054_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_252d_accel_v055_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_252d_accel_v056_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_252d_accel_v057_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_504d_accel_v058_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_504d_accel_v059_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps sharesbas
def gm_f28_biotech_f28_share_count_velocity_ps_504d_accel_v060_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_21d_accel_v061_signal(sharesbas, assets):
    base = _safe_div(_mean(sharesbas, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_21d_accel_v062_signal(sharesbas, assets):
    base = _safe_div(_mean(sharesbas, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_21d_accel_v063_signal(sharesbas, assets):
    base = _safe_div(_mean(sharesbas, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_63d_accel_v064_signal(sharesbas, assets):
    base = _safe_div(_mean(sharesbas, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_63d_accel_v065_signal(sharesbas, assets):
    base = _safe_div(_mean(sharesbas, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_63d_accel_v066_signal(sharesbas, assets):
    base = _safe_div(_mean(sharesbas, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_126d_accel_v067_signal(sharesbas, assets):
    base = _safe_div(_mean(sharesbas, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_126d_accel_v068_signal(sharesbas, assets):
    base = _safe_div(_mean(sharesbas, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_126d_accel_v069_signal(sharesbas, assets):
    base = _safe_div(_mean(sharesbas, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_252d_accel_v070_signal(sharesbas, assets):
    base = _safe_div(_mean(sharesbas, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_252d_accel_v071_signal(sharesbas, assets):
    base = _safe_div(_mean(sharesbas, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_252d_accel_v072_signal(sharesbas, assets):
    base = _safe_div(_mean(sharesbas, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_504d_accel_v073_signal(sharesbas, assets):
    base = _safe_div(_mean(sharesbas, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_504d_accel_v074_signal(sharesbas, assets):
    base = _safe_div(_mean(sharesbas, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_asset_scaled_504d_accel_v075_signal(sharesbas, assets):
    base = _safe_div(_mean(sharesbas, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_21d_accel_v076_signal(sharesbas, marketcap):
    base = _safe_div(_mean(sharesbas, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_21d_accel_v077_signal(sharesbas, marketcap):
    base = _safe_div(_mean(sharesbas, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_21d_accel_v078_signal(sharesbas, marketcap):
    base = _safe_div(_mean(sharesbas, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_63d_accel_v079_signal(sharesbas, marketcap):
    base = _safe_div(_mean(sharesbas, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_63d_accel_v080_signal(sharesbas, marketcap):
    base = _safe_div(_mean(sharesbas, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_63d_accel_v081_signal(sharesbas, marketcap):
    base = _safe_div(_mean(sharesbas, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_126d_accel_v082_signal(sharesbas, marketcap):
    base = _safe_div(_mean(sharesbas, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_126d_accel_v083_signal(sharesbas, marketcap):
    base = _safe_div(_mean(sharesbas, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_126d_accel_v084_signal(sharesbas, marketcap):
    base = _safe_div(_mean(sharesbas, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_252d_accel_v085_signal(sharesbas, marketcap):
    base = _safe_div(_mean(sharesbas, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_252d_accel_v086_signal(sharesbas, marketcap):
    base = _safe_div(_mean(sharesbas, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_252d_accel_v087_signal(sharesbas, marketcap):
    base = _safe_div(_mean(sharesbas, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_504d_accel_v088_signal(sharesbas, marketcap):
    base = _safe_div(_mean(sharesbas, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_504d_accel_v089_signal(sharesbas, marketcap):
    base = _safe_div(_mean(sharesbas, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled sharesbas
def gm_f28_biotech_f28_share_count_velocity_mcap_scaled_504d_accel_v090_signal(sharesbas, marketcap):
    base = _safe_div(_mean(sharesbas, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_21d_accel_v091_signal(sharesbas):
    base = _safe_div(sharesbas - sharesbas.rolling(21).min(), sharesbas.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_21d_accel_v092_signal(sharesbas):
    base = _safe_div(sharesbas - sharesbas.rolling(21).min(), sharesbas.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_21d_accel_v093_signal(sharesbas):
    base = _safe_div(sharesbas - sharesbas.rolling(21).min(), sharesbas.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_63d_accel_v094_signal(sharesbas):
    base = _safe_div(sharesbas - sharesbas.rolling(63).min(), sharesbas.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_63d_accel_v095_signal(sharesbas):
    base = _safe_div(sharesbas - sharesbas.rolling(63).min(), sharesbas.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_63d_accel_v096_signal(sharesbas):
    base = _safe_div(sharesbas - sharesbas.rolling(63).min(), sharesbas.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_126d_accel_v097_signal(sharesbas):
    base = _safe_div(sharesbas - sharesbas.rolling(126).min(), sharesbas.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_126d_accel_v098_signal(sharesbas):
    base = _safe_div(sharesbas - sharesbas.rolling(126).min(), sharesbas.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_126d_accel_v099_signal(sharesbas):
    base = _safe_div(sharesbas - sharesbas.rolling(126).min(), sharesbas.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_252d_accel_v100_signal(sharesbas):
    base = _safe_div(sharesbas - sharesbas.rolling(252).min(), sharesbas.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_252d_accel_v101_signal(sharesbas):
    base = _safe_div(sharesbas - sharesbas.rolling(252).min(), sharesbas.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_252d_accel_v102_signal(sharesbas):
    base = _safe_div(sharesbas - sharesbas.rolling(252).min(), sharesbas.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_504d_accel_v103_signal(sharesbas):
    base = _safe_div(sharesbas - sharesbas.rolling(504).min(), sharesbas.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_504d_accel_v104_signal(sharesbas):
    base = _safe_div(sharesbas - sharesbas.rolling(504).min(), sharesbas.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_low_504d_accel_v105_signal(sharesbas):
    base = _safe_div(sharesbas - sharesbas.rolling(504).min(), sharesbas.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_21d_accel_v106_signal(sharesbas):
    base = _safe_div(sharesbas.rolling(21).max() - sharesbas, sharesbas.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_21d_accel_v107_signal(sharesbas):
    base = _safe_div(sharesbas.rolling(21).max() - sharesbas, sharesbas.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_21d_accel_v108_signal(sharesbas):
    base = _safe_div(sharesbas.rolling(21).max() - sharesbas, sharesbas.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_63d_accel_v109_signal(sharesbas):
    base = _safe_div(sharesbas.rolling(63).max() - sharesbas, sharesbas.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_63d_accel_v110_signal(sharesbas):
    base = _safe_div(sharesbas.rolling(63).max() - sharesbas, sharesbas.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_63d_accel_v111_signal(sharesbas):
    base = _safe_div(sharesbas.rolling(63).max() - sharesbas, sharesbas.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_126d_accel_v112_signal(sharesbas):
    base = _safe_div(sharesbas.rolling(126).max() - sharesbas, sharesbas.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_126d_accel_v113_signal(sharesbas):
    base = _safe_div(sharesbas.rolling(126).max() - sharesbas, sharesbas.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_126d_accel_v114_signal(sharesbas):
    base = _safe_div(sharesbas.rolling(126).max() - sharesbas, sharesbas.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_252d_accel_v115_signal(sharesbas):
    base = _safe_div(sharesbas.rolling(252).max() - sharesbas, sharesbas.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_252d_accel_v116_signal(sharesbas):
    base = _safe_div(sharesbas.rolling(252).max() - sharesbas, sharesbas.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_252d_accel_v117_signal(sharesbas):
    base = _safe_div(sharesbas.rolling(252).max() - sharesbas, sharesbas.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_504d_accel_v118_signal(sharesbas):
    base = _safe_div(sharesbas.rolling(504).max() - sharesbas, sharesbas.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_504d_accel_v119_signal(sharesbas):
    base = _safe_div(sharesbas.rolling(504).max() - sharesbas, sharesbas.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high sharesbas
def gm_f28_biotech_f28_share_count_velocity_dist_high_504d_accel_v120_signal(sharesbas):
    base = _safe_div(sharesbas.rolling(504).max() - sharesbas, sharesbas.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_21d_accel_v121_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 21) - _mean(sharesbas, 42), _mean(sharesbas, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_21d_accel_v122_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 21) - _mean(sharesbas, 42), _mean(sharesbas, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_21d_accel_v123_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 21) - _mean(sharesbas, 42), _mean(sharesbas, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_63d_accel_v124_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 63) - _mean(sharesbas, 126), _mean(sharesbas, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_63d_accel_v125_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 63) - _mean(sharesbas, 126), _mean(sharesbas, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_63d_accel_v126_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 63) - _mean(sharesbas, 126), _mean(sharesbas, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_126d_accel_v127_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 126) - _mean(sharesbas, 252), _mean(sharesbas, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_126d_accel_v128_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 126) - _mean(sharesbas, 252), _mean(sharesbas, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_126d_accel_v129_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 126) - _mean(sharesbas, 252), _mean(sharesbas, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_252d_accel_v130_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 252) - _mean(sharesbas, 504), _mean(sharesbas, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_252d_accel_v131_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 252) - _mean(sharesbas, 504), _mean(sharesbas, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_252d_accel_v132_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 252) - _mean(sharesbas, 504), _mean(sharesbas, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_504d_accel_v133_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 504) - _mean(sharesbas, 1008), _mean(sharesbas, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_504d_accel_v134_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 504) - _mean(sharesbas, 1008), _mean(sharesbas, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom sharesbas
def gm_f28_biotech_f28_share_count_velocity_mom_504d_accel_v135_signal(sharesbas):
    base = _safe_div(_mean(sharesbas, 504) - _mean(sharesbas, 1008), _mean(sharesbas, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol sharesbas
def gm_f28_biotech_f28_share_count_velocity_vol_21d_accel_v136_signal(sharesbas):
    base = _std(sharesbas, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol sharesbas
def gm_f28_biotech_f28_share_count_velocity_vol_21d_accel_v137_signal(sharesbas):
    base = _std(sharesbas, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol sharesbas
def gm_f28_biotech_f28_share_count_velocity_vol_21d_accel_v138_signal(sharesbas):
    base = _std(sharesbas, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol sharesbas
def gm_f28_biotech_f28_share_count_velocity_vol_63d_accel_v139_signal(sharesbas):
    base = _std(sharesbas, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol sharesbas
def gm_f28_biotech_f28_share_count_velocity_vol_63d_accel_v140_signal(sharesbas):
    base = _std(sharesbas, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol sharesbas
def gm_f28_biotech_f28_share_count_velocity_vol_63d_accel_v141_signal(sharesbas):
    base = _std(sharesbas, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol sharesbas
def gm_f28_biotech_f28_share_count_velocity_vol_126d_accel_v142_signal(sharesbas):
    base = _std(sharesbas, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol sharesbas
def gm_f28_biotech_f28_share_count_velocity_vol_126d_accel_v143_signal(sharesbas):
    base = _std(sharesbas, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol sharesbas
def gm_f28_biotech_f28_share_count_velocity_vol_126d_accel_v144_signal(sharesbas):
    base = _std(sharesbas, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol sharesbas
def gm_f28_biotech_f28_share_count_velocity_vol_252d_accel_v145_signal(sharesbas):
    base = _std(sharesbas, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol sharesbas
def gm_f28_biotech_f28_share_count_velocity_vol_252d_accel_v146_signal(sharesbas):
    base = _std(sharesbas, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol sharesbas
def gm_f28_biotech_f28_share_count_velocity_vol_252d_accel_v147_signal(sharesbas):
    base = _std(sharesbas, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol sharesbas
def gm_f28_biotech_f28_share_count_velocity_vol_504d_accel_v148_signal(sharesbas):
    base = _std(sharesbas, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol sharesbas
def gm_f28_biotech_f28_share_count_velocity_vol_504d_accel_v149_signal(sharesbas):
    base = _std(sharesbas, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol sharesbas
def gm_f28_biotech_f28_share_count_velocity_vol_504d_accel_v150_signal(sharesbas):
    base = _std(sharesbas, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

