
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_21d_accel_v001_signal(sgna):
    base = _mean(sgna, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_21d_accel_v002_signal(sgna):
    base = _mean(sgna, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_21d_accel_v003_signal(sgna):
    base = _mean(sgna, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_63d_accel_v004_signal(sgna):
    base = _mean(sgna, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_63d_accel_v005_signal(sgna):
    base = _mean(sgna, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_63d_accel_v006_signal(sgna):
    base = _mean(sgna, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_126d_accel_v007_signal(sgna):
    base = _mean(sgna, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_126d_accel_v008_signal(sgna):
    base = _mean(sgna, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_126d_accel_v009_signal(sgna):
    base = _mean(sgna, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_252d_accel_v010_signal(sgna):
    base = _mean(sgna, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_252d_accel_v011_signal(sgna):
    base = _mean(sgna, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_252d_accel_v012_signal(sgna):
    base = _mean(sgna, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_504d_accel_v013_signal(sgna):
    base = _mean(sgna, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_504d_accel_v014_signal(sgna):
    base = _mean(sgna, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_504d_accel_v015_signal(sgna):
    base = _mean(sgna, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_21d_accel_v016_signal(sgna):
    base = _mean(_log(sgna), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_21d_accel_v017_signal(sgna):
    base = _mean(_log(sgna), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_21d_accel_v018_signal(sgna):
    base = _mean(_log(sgna), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_63d_accel_v019_signal(sgna):
    base = _mean(_log(sgna), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_63d_accel_v020_signal(sgna):
    base = _mean(_log(sgna), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_63d_accel_v021_signal(sgna):
    base = _mean(_log(sgna), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_126d_accel_v022_signal(sgna):
    base = _mean(_log(sgna), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_126d_accel_v023_signal(sgna):
    base = _mean(_log(sgna), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_126d_accel_v024_signal(sgna):
    base = _mean(_log(sgna), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_252d_accel_v025_signal(sgna):
    base = _mean(_log(sgna), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_252d_accel_v026_signal(sgna):
    base = _mean(_log(sgna), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_252d_accel_v027_signal(sgna):
    base = _mean(_log(sgna), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_504d_accel_v028_signal(sgna):
    base = _mean(_log(sgna), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_504d_accel_v029_signal(sgna):
    base = _mean(_log(sgna), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_504d_accel_v030_signal(sgna):
    base = _mean(_log(sgna), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_21d_accel_v031_signal(sgna):
    base = _z(sgna, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_21d_accel_v032_signal(sgna):
    base = _z(sgna, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_21d_accel_v033_signal(sgna):
    base = _z(sgna, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_63d_accel_v034_signal(sgna):
    base = _z(sgna, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_63d_accel_v035_signal(sgna):
    base = _z(sgna, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_63d_accel_v036_signal(sgna):
    base = _z(sgna, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_126d_accel_v037_signal(sgna):
    base = _z(sgna, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_126d_accel_v038_signal(sgna):
    base = _z(sgna, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_126d_accel_v039_signal(sgna):
    base = _z(sgna, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_252d_accel_v040_signal(sgna):
    base = _z(sgna, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_252d_accel_v041_signal(sgna):
    base = _z(sgna, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_252d_accel_v042_signal(sgna):
    base = _z(sgna, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_504d_accel_v043_signal(sgna):
    base = _z(sgna, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_504d_accel_v044_signal(sgna):
    base = _z(sgna, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_504d_accel_v045_signal(sgna):
    base = _z(sgna, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_21d_accel_v046_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_21d_accel_v047_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_21d_accel_v048_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_63d_accel_v049_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_63d_accel_v050_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_63d_accel_v051_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_126d_accel_v052_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_126d_accel_v053_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_126d_accel_v054_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_252d_accel_v055_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_252d_accel_v056_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_252d_accel_v057_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_504d_accel_v058_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_504d_accel_v059_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_504d_accel_v060_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_21d_accel_v061_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_21d_accel_v062_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_21d_accel_v063_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_63d_accel_v064_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_63d_accel_v065_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_63d_accel_v066_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_126d_accel_v067_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_126d_accel_v068_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_126d_accel_v069_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_252d_accel_v070_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_252d_accel_v071_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_252d_accel_v072_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_504d_accel_v073_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_504d_accel_v074_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_504d_accel_v075_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_21d_accel_v076_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_21d_accel_v077_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_21d_accel_v078_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_63d_accel_v079_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_63d_accel_v080_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_63d_accel_v081_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_126d_accel_v082_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_126d_accel_v083_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_126d_accel_v084_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_252d_accel_v085_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_252d_accel_v086_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_252d_accel_v087_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_504d_accel_v088_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_504d_accel_v089_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_504d_accel_v090_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_21d_accel_v091_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(21).min(), sgna.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_21d_accel_v092_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(21).min(), sgna.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_21d_accel_v093_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(21).min(), sgna.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_63d_accel_v094_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(63).min(), sgna.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_63d_accel_v095_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(63).min(), sgna.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_63d_accel_v096_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(63).min(), sgna.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_126d_accel_v097_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(126).min(), sgna.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_126d_accel_v098_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(126).min(), sgna.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_126d_accel_v099_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(126).min(), sgna.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_252d_accel_v100_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(252).min(), sgna.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_252d_accel_v101_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(252).min(), sgna.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_252d_accel_v102_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(252).min(), sgna.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_504d_accel_v103_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(504).min(), sgna.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_504d_accel_v104_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(504).min(), sgna.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_504d_accel_v105_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(504).min(), sgna.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_21d_accel_v106_signal(sgna):
    base = _safe_div(sgna.rolling(21).max() - sgna, sgna.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_21d_accel_v107_signal(sgna):
    base = _safe_div(sgna.rolling(21).max() - sgna, sgna.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_21d_accel_v108_signal(sgna):
    base = _safe_div(sgna.rolling(21).max() - sgna, sgna.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_63d_accel_v109_signal(sgna):
    base = _safe_div(sgna.rolling(63).max() - sgna, sgna.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_63d_accel_v110_signal(sgna):
    base = _safe_div(sgna.rolling(63).max() - sgna, sgna.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_63d_accel_v111_signal(sgna):
    base = _safe_div(sgna.rolling(63).max() - sgna, sgna.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_126d_accel_v112_signal(sgna):
    base = _safe_div(sgna.rolling(126).max() - sgna, sgna.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_126d_accel_v113_signal(sgna):
    base = _safe_div(sgna.rolling(126).max() - sgna, sgna.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_126d_accel_v114_signal(sgna):
    base = _safe_div(sgna.rolling(126).max() - sgna, sgna.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_252d_accel_v115_signal(sgna):
    base = _safe_div(sgna.rolling(252).max() - sgna, sgna.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_252d_accel_v116_signal(sgna):
    base = _safe_div(sgna.rolling(252).max() - sgna, sgna.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_252d_accel_v117_signal(sgna):
    base = _safe_div(sgna.rolling(252).max() - sgna, sgna.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_504d_accel_v118_signal(sgna):
    base = _safe_div(sgna.rolling(504).max() - sgna, sgna.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_504d_accel_v119_signal(sgna):
    base = _safe_div(sgna.rolling(504).max() - sgna, sgna.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_504d_accel_v120_signal(sgna):
    base = _safe_div(sgna.rolling(504).max() - sgna, sgna.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_21d_accel_v121_signal(sgna):
    base = _safe_div(_mean(sgna, 21) - _mean(sgna, 42), _mean(sgna, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_21d_accel_v122_signal(sgna):
    base = _safe_div(_mean(sgna, 21) - _mean(sgna, 42), _mean(sgna, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_21d_accel_v123_signal(sgna):
    base = _safe_div(_mean(sgna, 21) - _mean(sgna, 42), _mean(sgna, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_63d_accel_v124_signal(sgna):
    base = _safe_div(_mean(sgna, 63) - _mean(sgna, 126), _mean(sgna, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_63d_accel_v125_signal(sgna):
    base = _safe_div(_mean(sgna, 63) - _mean(sgna, 126), _mean(sgna, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_63d_accel_v126_signal(sgna):
    base = _safe_div(_mean(sgna, 63) - _mean(sgna, 126), _mean(sgna, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_126d_accel_v127_signal(sgna):
    base = _safe_div(_mean(sgna, 126) - _mean(sgna, 252), _mean(sgna, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_126d_accel_v128_signal(sgna):
    base = _safe_div(_mean(sgna, 126) - _mean(sgna, 252), _mean(sgna, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_126d_accel_v129_signal(sgna):
    base = _safe_div(_mean(sgna, 126) - _mean(sgna, 252), _mean(sgna, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_252d_accel_v130_signal(sgna):
    base = _safe_div(_mean(sgna, 252) - _mean(sgna, 504), _mean(sgna, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_252d_accel_v131_signal(sgna):
    base = _safe_div(_mean(sgna, 252) - _mean(sgna, 504), _mean(sgna, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_252d_accel_v132_signal(sgna):
    base = _safe_div(_mean(sgna, 252) - _mean(sgna, 504), _mean(sgna, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_504d_accel_v133_signal(sgna):
    base = _safe_div(_mean(sgna, 504) - _mean(sgna, 1008), _mean(sgna, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_504d_accel_v134_signal(sgna):
    base = _safe_div(_mean(sgna, 504) - _mean(sgna, 1008), _mean(sgna, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_504d_accel_v135_signal(sgna):
    base = _safe_div(_mean(sgna, 504) - _mean(sgna, 1008), _mean(sgna, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_21d_accel_v136_signal(sgna):
    base = _std(sgna, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_21d_accel_v137_signal(sgna):
    base = _std(sgna, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_21d_accel_v138_signal(sgna):
    base = _std(sgna, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_63d_accel_v139_signal(sgna):
    base = _std(sgna, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_63d_accel_v140_signal(sgna):
    base = _std(sgna, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_63d_accel_v141_signal(sgna):
    base = _std(sgna, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_126d_accel_v142_signal(sgna):
    base = _std(sgna, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_126d_accel_v143_signal(sgna):
    base = _std(sgna, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_126d_accel_v144_signal(sgna):
    base = _std(sgna, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_252d_accel_v145_signal(sgna):
    base = _std(sgna, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_252d_accel_v146_signal(sgna):
    base = _std(sgna, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_252d_accel_v147_signal(sgna):
    base = _std(sgna, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_504d_accel_v148_signal(sgna):
    base = _std(sgna, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_504d_accel_v149_signal(sgna):
    base = _std(sgna, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_504d_accel_v150_signal(sgna):
    base = _std(sgna, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

