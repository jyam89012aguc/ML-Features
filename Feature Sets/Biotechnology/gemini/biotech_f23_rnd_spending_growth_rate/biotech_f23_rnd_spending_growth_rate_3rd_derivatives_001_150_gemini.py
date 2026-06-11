
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_raw_21d_accel_v001_signal(rnd):
    base = _mean(rnd, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_raw_21d_accel_v002_signal(rnd):
    base = _mean(rnd, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_raw_21d_accel_v003_signal(rnd):
    base = _mean(rnd, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_raw_63d_accel_v004_signal(rnd):
    base = _mean(rnd, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_raw_63d_accel_v005_signal(rnd):
    base = _mean(rnd, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_raw_63d_accel_v006_signal(rnd):
    base = _mean(rnd, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_raw_126d_accel_v007_signal(rnd):
    base = _mean(rnd, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_raw_126d_accel_v008_signal(rnd):
    base = _mean(rnd, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_raw_126d_accel_v009_signal(rnd):
    base = _mean(rnd, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_raw_252d_accel_v010_signal(rnd):
    base = _mean(rnd, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_raw_252d_accel_v011_signal(rnd):
    base = _mean(rnd, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_raw_252d_accel_v012_signal(rnd):
    base = _mean(rnd, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_raw_504d_accel_v013_signal(rnd):
    base = _mean(rnd, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_raw_504d_accel_v014_signal(rnd):
    base = _mean(rnd, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_raw_504d_accel_v015_signal(rnd):
    base = _mean(rnd, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_log_21d_accel_v016_signal(rnd):
    base = _mean(_log(rnd), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_log_21d_accel_v017_signal(rnd):
    base = _mean(_log(rnd), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_log_21d_accel_v018_signal(rnd):
    base = _mean(_log(rnd), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_log_63d_accel_v019_signal(rnd):
    base = _mean(_log(rnd), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_log_63d_accel_v020_signal(rnd):
    base = _mean(_log(rnd), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_log_63d_accel_v021_signal(rnd):
    base = _mean(_log(rnd), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_log_126d_accel_v022_signal(rnd):
    base = _mean(_log(rnd), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_log_126d_accel_v023_signal(rnd):
    base = _mean(_log(rnd), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_log_126d_accel_v024_signal(rnd):
    base = _mean(_log(rnd), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_log_252d_accel_v025_signal(rnd):
    base = _mean(_log(rnd), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_log_252d_accel_v026_signal(rnd):
    base = _mean(_log(rnd), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_log_252d_accel_v027_signal(rnd):
    base = _mean(_log(rnd), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_log_504d_accel_v028_signal(rnd):
    base = _mean(_log(rnd), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_log_504d_accel_v029_signal(rnd):
    base = _mean(_log(rnd), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_log_504d_accel_v030_signal(rnd):
    base = _mean(_log(rnd), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_z_21d_accel_v031_signal(rnd):
    base = _z(rnd, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_z_21d_accel_v032_signal(rnd):
    base = _z(rnd, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_z_21d_accel_v033_signal(rnd):
    base = _z(rnd, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_z_63d_accel_v034_signal(rnd):
    base = _z(rnd, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_z_63d_accel_v035_signal(rnd):
    base = _z(rnd, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_z_63d_accel_v036_signal(rnd):
    base = _z(rnd, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_z_126d_accel_v037_signal(rnd):
    base = _z(rnd, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_z_126d_accel_v038_signal(rnd):
    base = _z(rnd, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_z_126d_accel_v039_signal(rnd):
    base = _z(rnd, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_z_252d_accel_v040_signal(rnd):
    base = _z(rnd, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_z_252d_accel_v041_signal(rnd):
    base = _z(rnd, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_z_252d_accel_v042_signal(rnd):
    base = _z(rnd, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_z_504d_accel_v043_signal(rnd):
    base = _z(rnd, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_z_504d_accel_v044_signal(rnd):
    base = _z(rnd, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_z_504d_accel_v045_signal(rnd):
    base = _z(rnd, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_ps_21d_accel_v046_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_ps_21d_accel_v047_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_ps_21d_accel_v048_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_ps_63d_accel_v049_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_ps_63d_accel_v050_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_ps_63d_accel_v051_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_ps_126d_accel_v052_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_ps_126d_accel_v053_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_ps_126d_accel_v054_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_ps_252d_accel_v055_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_ps_252d_accel_v056_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_ps_252d_accel_v057_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_ps_504d_accel_v058_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_ps_504d_accel_v059_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_ps_504d_accel_v060_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_asset_scaled_21d_accel_v061_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_asset_scaled_21d_accel_v062_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_asset_scaled_21d_accel_v063_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_asset_scaled_63d_accel_v064_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_asset_scaled_63d_accel_v065_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_asset_scaled_63d_accel_v066_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_asset_scaled_126d_accel_v067_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_asset_scaled_126d_accel_v068_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_asset_scaled_126d_accel_v069_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_asset_scaled_252d_accel_v070_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_asset_scaled_252d_accel_v071_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_asset_scaled_252d_accel_v072_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_asset_scaled_504d_accel_v073_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_asset_scaled_504d_accel_v074_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_asset_scaled_504d_accel_v075_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mcap_scaled_21d_accel_v076_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mcap_scaled_21d_accel_v077_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mcap_scaled_21d_accel_v078_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mcap_scaled_63d_accel_v079_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mcap_scaled_63d_accel_v080_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mcap_scaled_63d_accel_v081_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mcap_scaled_126d_accel_v082_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mcap_scaled_126d_accel_v083_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mcap_scaled_126d_accel_v084_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mcap_scaled_252d_accel_v085_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mcap_scaled_252d_accel_v086_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mcap_scaled_252d_accel_v087_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mcap_scaled_504d_accel_v088_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mcap_scaled_504d_accel_v089_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mcap_scaled_504d_accel_v090_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_low_21d_accel_v091_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(21).min(), rnd.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_low_21d_accel_v092_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(21).min(), rnd.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_low_21d_accel_v093_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(21).min(), rnd.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_low_63d_accel_v094_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(63).min(), rnd.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_low_63d_accel_v095_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(63).min(), rnd.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_low_63d_accel_v096_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(63).min(), rnd.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_low_126d_accel_v097_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(126).min(), rnd.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_low_126d_accel_v098_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(126).min(), rnd.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_low_126d_accel_v099_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(126).min(), rnd.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_low_252d_accel_v100_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(252).min(), rnd.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_low_252d_accel_v101_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(252).min(), rnd.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_low_252d_accel_v102_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(252).min(), rnd.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_low_504d_accel_v103_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(504).min(), rnd.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_low_504d_accel_v104_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(504).min(), rnd.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_low_504d_accel_v105_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(504).min(), rnd.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_high_21d_accel_v106_signal(rnd):
    base = _safe_div(rnd.rolling(21).max() - rnd, rnd.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_high_21d_accel_v107_signal(rnd):
    base = _safe_div(rnd.rolling(21).max() - rnd, rnd.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_high_21d_accel_v108_signal(rnd):
    base = _safe_div(rnd.rolling(21).max() - rnd, rnd.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_high_63d_accel_v109_signal(rnd):
    base = _safe_div(rnd.rolling(63).max() - rnd, rnd.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_high_63d_accel_v110_signal(rnd):
    base = _safe_div(rnd.rolling(63).max() - rnd, rnd.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_high_63d_accel_v111_signal(rnd):
    base = _safe_div(rnd.rolling(63).max() - rnd, rnd.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_high_126d_accel_v112_signal(rnd):
    base = _safe_div(rnd.rolling(126).max() - rnd, rnd.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_high_126d_accel_v113_signal(rnd):
    base = _safe_div(rnd.rolling(126).max() - rnd, rnd.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_high_126d_accel_v114_signal(rnd):
    base = _safe_div(rnd.rolling(126).max() - rnd, rnd.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_high_252d_accel_v115_signal(rnd):
    base = _safe_div(rnd.rolling(252).max() - rnd, rnd.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_high_252d_accel_v116_signal(rnd):
    base = _safe_div(rnd.rolling(252).max() - rnd, rnd.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_high_252d_accel_v117_signal(rnd):
    base = _safe_div(rnd.rolling(252).max() - rnd, rnd.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_high_504d_accel_v118_signal(rnd):
    base = _safe_div(rnd.rolling(504).max() - rnd, rnd.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_high_504d_accel_v119_signal(rnd):
    base = _safe_div(rnd.rolling(504).max() - rnd, rnd.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_dist_high_504d_accel_v120_signal(rnd):
    base = _safe_div(rnd.rolling(504).max() - rnd, rnd.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mom_21d_accel_v121_signal(rnd):
    base = _safe_div(_mean(rnd, 21) - _mean(rnd, 42), _mean(rnd, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mom_21d_accel_v122_signal(rnd):
    base = _safe_div(_mean(rnd, 21) - _mean(rnd, 42), _mean(rnd, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mom_21d_accel_v123_signal(rnd):
    base = _safe_div(_mean(rnd, 21) - _mean(rnd, 42), _mean(rnd, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mom_63d_accel_v124_signal(rnd):
    base = _safe_div(_mean(rnd, 63) - _mean(rnd, 126), _mean(rnd, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mom_63d_accel_v125_signal(rnd):
    base = _safe_div(_mean(rnd, 63) - _mean(rnd, 126), _mean(rnd, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mom_63d_accel_v126_signal(rnd):
    base = _safe_div(_mean(rnd, 63) - _mean(rnd, 126), _mean(rnd, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mom_126d_accel_v127_signal(rnd):
    base = _safe_div(_mean(rnd, 126) - _mean(rnd, 252), _mean(rnd, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mom_126d_accel_v128_signal(rnd):
    base = _safe_div(_mean(rnd, 126) - _mean(rnd, 252), _mean(rnd, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mom_126d_accel_v129_signal(rnd):
    base = _safe_div(_mean(rnd, 126) - _mean(rnd, 252), _mean(rnd, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mom_252d_accel_v130_signal(rnd):
    base = _safe_div(_mean(rnd, 252) - _mean(rnd, 504), _mean(rnd, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mom_252d_accel_v131_signal(rnd):
    base = _safe_div(_mean(rnd, 252) - _mean(rnd, 504), _mean(rnd, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mom_252d_accel_v132_signal(rnd):
    base = _safe_div(_mean(rnd, 252) - _mean(rnd, 504), _mean(rnd, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mom_504d_accel_v133_signal(rnd):
    base = _safe_div(_mean(rnd, 504) - _mean(rnd, 1008), _mean(rnd, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mom_504d_accel_v134_signal(rnd):
    base = _safe_div(_mean(rnd, 504) - _mean(rnd, 1008), _mean(rnd, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_mom_504d_accel_v135_signal(rnd):
    base = _safe_div(_mean(rnd, 504) - _mean(rnd, 1008), _mean(rnd, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_vol_21d_accel_v136_signal(rnd):
    base = _std(rnd, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_vol_21d_accel_v137_signal(rnd):
    base = _std(rnd, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_vol_21d_accel_v138_signal(rnd):
    base = _std(rnd, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_vol_63d_accel_v139_signal(rnd):
    base = _std(rnd, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_vol_63d_accel_v140_signal(rnd):
    base = _std(rnd, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_vol_63d_accel_v141_signal(rnd):
    base = _std(rnd, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_vol_126d_accel_v142_signal(rnd):
    base = _std(rnd, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_vol_126d_accel_v143_signal(rnd):
    base = _std(rnd, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_vol_126d_accel_v144_signal(rnd):
    base = _std(rnd, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_vol_252d_accel_v145_signal(rnd):
    base = _std(rnd, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_vol_252d_accel_v146_signal(rnd):
    base = _std(rnd, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_vol_252d_accel_v147_signal(rnd):
    base = _std(rnd, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_vol_504d_accel_v148_signal(rnd):
    base = _std(rnd, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_vol_504d_accel_v149_signal(rnd):
    base = _std(rnd, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol rnd
def gm_f23_biotech_f23_rnd_spending_growth_rate_vol_504d_accel_v150_signal(rnd):
    base = _std(rnd, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

