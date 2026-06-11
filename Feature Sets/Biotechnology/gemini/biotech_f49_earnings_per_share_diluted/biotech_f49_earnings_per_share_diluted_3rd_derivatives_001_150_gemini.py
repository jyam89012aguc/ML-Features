
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_21d_accel_v001_signal(epsdil):
    base = _mean(epsdil, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_21d_accel_v002_signal(epsdil):
    base = _mean(epsdil, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_21d_accel_v003_signal(epsdil):
    base = _mean(epsdil, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_63d_accel_v004_signal(epsdil):
    base = _mean(epsdil, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_63d_accel_v005_signal(epsdil):
    base = _mean(epsdil, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_63d_accel_v006_signal(epsdil):
    base = _mean(epsdil, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_126d_accel_v007_signal(epsdil):
    base = _mean(epsdil, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_126d_accel_v008_signal(epsdil):
    base = _mean(epsdil, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_126d_accel_v009_signal(epsdil):
    base = _mean(epsdil, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_252d_accel_v010_signal(epsdil):
    base = _mean(epsdil, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_252d_accel_v011_signal(epsdil):
    base = _mean(epsdil, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_252d_accel_v012_signal(epsdil):
    base = _mean(epsdil, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_504d_accel_v013_signal(epsdil):
    base = _mean(epsdil, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_504d_accel_v014_signal(epsdil):
    base = _mean(epsdil, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_raw_504d_accel_v015_signal(epsdil):
    base = _mean(epsdil, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_21d_accel_v016_signal(epsdil):
    base = _mean(_log(epsdil), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_21d_accel_v017_signal(epsdil):
    base = _mean(_log(epsdil), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_21d_accel_v018_signal(epsdil):
    base = _mean(_log(epsdil), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_63d_accel_v019_signal(epsdil):
    base = _mean(_log(epsdil), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_63d_accel_v020_signal(epsdil):
    base = _mean(_log(epsdil), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_63d_accel_v021_signal(epsdil):
    base = _mean(_log(epsdil), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_126d_accel_v022_signal(epsdil):
    base = _mean(_log(epsdil), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_126d_accel_v023_signal(epsdil):
    base = _mean(_log(epsdil), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_126d_accel_v024_signal(epsdil):
    base = _mean(_log(epsdil), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_252d_accel_v025_signal(epsdil):
    base = _mean(_log(epsdil), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_252d_accel_v026_signal(epsdil):
    base = _mean(_log(epsdil), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_252d_accel_v027_signal(epsdil):
    base = _mean(_log(epsdil), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_504d_accel_v028_signal(epsdil):
    base = _mean(_log(epsdil), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_504d_accel_v029_signal(epsdil):
    base = _mean(_log(epsdil), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_log_504d_accel_v030_signal(epsdil):
    base = _mean(_log(epsdil), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_21d_accel_v031_signal(epsdil):
    base = _z(epsdil, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_21d_accel_v032_signal(epsdil):
    base = _z(epsdil, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_21d_accel_v033_signal(epsdil):
    base = _z(epsdil, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_63d_accel_v034_signal(epsdil):
    base = _z(epsdil, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_63d_accel_v035_signal(epsdil):
    base = _z(epsdil, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_63d_accel_v036_signal(epsdil):
    base = _z(epsdil, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_126d_accel_v037_signal(epsdil):
    base = _z(epsdil, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_126d_accel_v038_signal(epsdil):
    base = _z(epsdil, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_126d_accel_v039_signal(epsdil):
    base = _z(epsdil, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_252d_accel_v040_signal(epsdil):
    base = _z(epsdil, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_252d_accel_v041_signal(epsdil):
    base = _z(epsdil, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_252d_accel_v042_signal(epsdil):
    base = _z(epsdil, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_504d_accel_v043_signal(epsdil):
    base = _z(epsdil, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_504d_accel_v044_signal(epsdil):
    base = _z(epsdil, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_z_504d_accel_v045_signal(epsdil):
    base = _z(epsdil, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_21d_accel_v046_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_21d_accel_v047_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_21d_accel_v048_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_63d_accel_v049_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_63d_accel_v050_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_63d_accel_v051_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_126d_accel_v052_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_126d_accel_v053_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_126d_accel_v054_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_252d_accel_v055_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_252d_accel_v056_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_252d_accel_v057_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_504d_accel_v058_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_504d_accel_v059_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_ps_504d_accel_v060_signal(epsdil, sharesbas):
    base = _safe_div(_mean(epsdil, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_21d_accel_v061_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_21d_accel_v062_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_21d_accel_v063_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_63d_accel_v064_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_63d_accel_v065_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_63d_accel_v066_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_126d_accel_v067_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_126d_accel_v068_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_126d_accel_v069_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_252d_accel_v070_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_252d_accel_v071_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_252d_accel_v072_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_504d_accel_v073_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_504d_accel_v074_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_asset_scaled_504d_accel_v075_signal(epsdil, assets):
    base = _safe_div(_mean(epsdil, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_21d_accel_v076_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_21d_accel_v077_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_21d_accel_v078_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_63d_accel_v079_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_63d_accel_v080_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_63d_accel_v081_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_126d_accel_v082_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_126d_accel_v083_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_126d_accel_v084_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_252d_accel_v085_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_252d_accel_v086_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_252d_accel_v087_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_504d_accel_v088_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_504d_accel_v089_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mcap_scaled_504d_accel_v090_signal(epsdil, marketcap):
    base = _safe_div(_mean(epsdil, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_21d_accel_v091_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(21).min(), epsdil.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_21d_accel_v092_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(21).min(), epsdil.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_21d_accel_v093_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(21).min(), epsdil.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_63d_accel_v094_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(63).min(), epsdil.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_63d_accel_v095_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(63).min(), epsdil.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_63d_accel_v096_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(63).min(), epsdil.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_126d_accel_v097_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(126).min(), epsdil.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_126d_accel_v098_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(126).min(), epsdil.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_126d_accel_v099_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(126).min(), epsdil.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_252d_accel_v100_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(252).min(), epsdil.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_252d_accel_v101_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(252).min(), epsdil.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_252d_accel_v102_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(252).min(), epsdil.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_504d_accel_v103_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(504).min(), epsdil.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_504d_accel_v104_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(504).min(), epsdil.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_low_504d_accel_v105_signal(epsdil):
    base = _safe_div(epsdil - epsdil.rolling(504).min(), epsdil.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_21d_accel_v106_signal(epsdil):
    base = _safe_div(epsdil.rolling(21).max() - epsdil, epsdil.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_21d_accel_v107_signal(epsdil):
    base = _safe_div(epsdil.rolling(21).max() - epsdil, epsdil.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_21d_accel_v108_signal(epsdil):
    base = _safe_div(epsdil.rolling(21).max() - epsdil, epsdil.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_63d_accel_v109_signal(epsdil):
    base = _safe_div(epsdil.rolling(63).max() - epsdil, epsdil.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_63d_accel_v110_signal(epsdil):
    base = _safe_div(epsdil.rolling(63).max() - epsdil, epsdil.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_63d_accel_v111_signal(epsdil):
    base = _safe_div(epsdil.rolling(63).max() - epsdil, epsdil.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_126d_accel_v112_signal(epsdil):
    base = _safe_div(epsdil.rolling(126).max() - epsdil, epsdil.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_126d_accel_v113_signal(epsdil):
    base = _safe_div(epsdil.rolling(126).max() - epsdil, epsdil.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_126d_accel_v114_signal(epsdil):
    base = _safe_div(epsdil.rolling(126).max() - epsdil, epsdil.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_252d_accel_v115_signal(epsdil):
    base = _safe_div(epsdil.rolling(252).max() - epsdil, epsdil.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_252d_accel_v116_signal(epsdil):
    base = _safe_div(epsdil.rolling(252).max() - epsdil, epsdil.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_252d_accel_v117_signal(epsdil):
    base = _safe_div(epsdil.rolling(252).max() - epsdil, epsdil.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_504d_accel_v118_signal(epsdil):
    base = _safe_div(epsdil.rolling(504).max() - epsdil, epsdil.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_504d_accel_v119_signal(epsdil):
    base = _safe_div(epsdil.rolling(504).max() - epsdil, epsdil.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_dist_high_504d_accel_v120_signal(epsdil):
    base = _safe_div(epsdil.rolling(504).max() - epsdil, epsdil.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_21d_accel_v121_signal(epsdil):
    base = _safe_div(_mean(epsdil, 21) - _mean(epsdil, 42), _mean(epsdil, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_21d_accel_v122_signal(epsdil):
    base = _safe_div(_mean(epsdil, 21) - _mean(epsdil, 42), _mean(epsdil, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_21d_accel_v123_signal(epsdil):
    base = _safe_div(_mean(epsdil, 21) - _mean(epsdil, 42), _mean(epsdil, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_63d_accel_v124_signal(epsdil):
    base = _safe_div(_mean(epsdil, 63) - _mean(epsdil, 126), _mean(epsdil, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_63d_accel_v125_signal(epsdil):
    base = _safe_div(_mean(epsdil, 63) - _mean(epsdil, 126), _mean(epsdil, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_63d_accel_v126_signal(epsdil):
    base = _safe_div(_mean(epsdil, 63) - _mean(epsdil, 126), _mean(epsdil, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_126d_accel_v127_signal(epsdil):
    base = _safe_div(_mean(epsdil, 126) - _mean(epsdil, 252), _mean(epsdil, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_126d_accel_v128_signal(epsdil):
    base = _safe_div(_mean(epsdil, 126) - _mean(epsdil, 252), _mean(epsdil, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_126d_accel_v129_signal(epsdil):
    base = _safe_div(_mean(epsdil, 126) - _mean(epsdil, 252), _mean(epsdil, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_252d_accel_v130_signal(epsdil):
    base = _safe_div(_mean(epsdil, 252) - _mean(epsdil, 504), _mean(epsdil, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_252d_accel_v131_signal(epsdil):
    base = _safe_div(_mean(epsdil, 252) - _mean(epsdil, 504), _mean(epsdil, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_252d_accel_v132_signal(epsdil):
    base = _safe_div(_mean(epsdil, 252) - _mean(epsdil, 504), _mean(epsdil, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_504d_accel_v133_signal(epsdil):
    base = _safe_div(_mean(epsdil, 504) - _mean(epsdil, 1008), _mean(epsdil, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_504d_accel_v134_signal(epsdil):
    base = _safe_div(_mean(epsdil, 504) - _mean(epsdil, 1008), _mean(epsdil, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_mom_504d_accel_v135_signal(epsdil):
    base = _safe_div(_mean(epsdil, 504) - _mean(epsdil, 1008), _mean(epsdil, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_21d_accel_v136_signal(epsdil):
    base = _std(epsdil, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_21d_accel_v137_signal(epsdil):
    base = _std(epsdil, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_21d_accel_v138_signal(epsdil):
    base = _std(epsdil, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_63d_accel_v139_signal(epsdil):
    base = _std(epsdil, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_63d_accel_v140_signal(epsdil):
    base = _std(epsdil, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_63d_accel_v141_signal(epsdil):
    base = _std(epsdil, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_126d_accel_v142_signal(epsdil):
    base = _std(epsdil, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_126d_accel_v143_signal(epsdil):
    base = _std(epsdil, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_126d_accel_v144_signal(epsdil):
    base = _std(epsdil, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_252d_accel_v145_signal(epsdil):
    base = _std(epsdil, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_252d_accel_v146_signal(epsdil):
    base = _std(epsdil, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_252d_accel_v147_signal(epsdil):
    base = _std(epsdil, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_504d_accel_v148_signal(epsdil):
    base = _std(epsdil, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_504d_accel_v149_signal(epsdil):
    base = _std(epsdil, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol epsdil
def gm_f49_biotech_f49_earnings_per_share_diluted_vol_504d_accel_v150_signal(epsdil):
    base = _std(epsdil, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

