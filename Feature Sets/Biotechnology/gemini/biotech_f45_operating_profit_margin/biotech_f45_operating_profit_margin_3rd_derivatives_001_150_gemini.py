
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_21d_accel_v001_signal(opinc):
    base = _mean(opinc, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_21d_accel_v002_signal(opinc):
    base = _mean(opinc, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_21d_accel_v003_signal(opinc):
    base = _mean(opinc, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_63d_accel_v004_signal(opinc):
    base = _mean(opinc, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_63d_accel_v005_signal(opinc):
    base = _mean(opinc, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_63d_accel_v006_signal(opinc):
    base = _mean(opinc, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_126d_accel_v007_signal(opinc):
    base = _mean(opinc, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_126d_accel_v008_signal(opinc):
    base = _mean(opinc, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_126d_accel_v009_signal(opinc):
    base = _mean(opinc, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_252d_accel_v010_signal(opinc):
    base = _mean(opinc, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_252d_accel_v011_signal(opinc):
    base = _mean(opinc, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_252d_accel_v012_signal(opinc):
    base = _mean(opinc, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_504d_accel_v013_signal(opinc):
    base = _mean(opinc, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_504d_accel_v014_signal(opinc):
    base = _mean(opinc, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw opinc
def gm_f45_biotech_f45_operating_profit_margin_raw_504d_accel_v015_signal(opinc):
    base = _mean(opinc, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_21d_accel_v016_signal(opinc):
    base = _mean(_log(opinc), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_21d_accel_v017_signal(opinc):
    base = _mean(_log(opinc), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_21d_accel_v018_signal(opinc):
    base = _mean(_log(opinc), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_63d_accel_v019_signal(opinc):
    base = _mean(_log(opinc), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_63d_accel_v020_signal(opinc):
    base = _mean(_log(opinc), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_63d_accel_v021_signal(opinc):
    base = _mean(_log(opinc), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_126d_accel_v022_signal(opinc):
    base = _mean(_log(opinc), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_126d_accel_v023_signal(opinc):
    base = _mean(_log(opinc), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_126d_accel_v024_signal(opinc):
    base = _mean(_log(opinc), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_252d_accel_v025_signal(opinc):
    base = _mean(_log(opinc), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_252d_accel_v026_signal(opinc):
    base = _mean(_log(opinc), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_252d_accel_v027_signal(opinc):
    base = _mean(_log(opinc), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_504d_accel_v028_signal(opinc):
    base = _mean(_log(opinc), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_504d_accel_v029_signal(opinc):
    base = _mean(_log(opinc), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log opinc
def gm_f45_biotech_f45_operating_profit_margin_log_504d_accel_v030_signal(opinc):
    base = _mean(_log(opinc), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_21d_accel_v031_signal(opinc):
    base = _z(opinc, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_21d_accel_v032_signal(opinc):
    base = _z(opinc, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_21d_accel_v033_signal(opinc):
    base = _z(opinc, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_63d_accel_v034_signal(opinc):
    base = _z(opinc, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_63d_accel_v035_signal(opinc):
    base = _z(opinc, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_63d_accel_v036_signal(opinc):
    base = _z(opinc, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_126d_accel_v037_signal(opinc):
    base = _z(opinc, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_126d_accel_v038_signal(opinc):
    base = _z(opinc, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_126d_accel_v039_signal(opinc):
    base = _z(opinc, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_252d_accel_v040_signal(opinc):
    base = _z(opinc, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_252d_accel_v041_signal(opinc):
    base = _z(opinc, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_252d_accel_v042_signal(opinc):
    base = _z(opinc, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_504d_accel_v043_signal(opinc):
    base = _z(opinc, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_504d_accel_v044_signal(opinc):
    base = _z(opinc, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z opinc
def gm_f45_biotech_f45_operating_profit_margin_z_504d_accel_v045_signal(opinc):
    base = _z(opinc, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_21d_accel_v046_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_21d_accel_v047_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_21d_accel_v048_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_63d_accel_v049_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_63d_accel_v050_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_63d_accel_v051_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_126d_accel_v052_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_126d_accel_v053_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_126d_accel_v054_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_252d_accel_v055_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_252d_accel_v056_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_252d_accel_v057_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_504d_accel_v058_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_504d_accel_v059_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps opinc
def gm_f45_biotech_f45_operating_profit_margin_ps_504d_accel_v060_signal(opinc, sharesbas):
    base = _safe_div(_mean(opinc, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_21d_accel_v061_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_21d_accel_v062_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_21d_accel_v063_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_63d_accel_v064_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_63d_accel_v065_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_63d_accel_v066_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_126d_accel_v067_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_126d_accel_v068_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_126d_accel_v069_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_252d_accel_v070_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_252d_accel_v071_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_252d_accel_v072_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_504d_accel_v073_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_504d_accel_v074_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_504d_accel_v075_signal(opinc, assets):
    base = _safe_div(_mean(opinc, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_21d_accel_v076_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_21d_accel_v077_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_21d_accel_v078_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_63d_accel_v079_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_63d_accel_v080_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_63d_accel_v081_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_126d_accel_v082_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_126d_accel_v083_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_126d_accel_v084_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_252d_accel_v085_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_252d_accel_v086_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_252d_accel_v087_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_504d_accel_v088_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_504d_accel_v089_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled opinc
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_504d_accel_v090_signal(opinc, marketcap):
    base = _safe_div(_mean(opinc, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_21d_accel_v091_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(21).min(), opinc.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_21d_accel_v092_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(21).min(), opinc.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_21d_accel_v093_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(21).min(), opinc.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_63d_accel_v094_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(63).min(), opinc.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_63d_accel_v095_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(63).min(), opinc.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_63d_accel_v096_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(63).min(), opinc.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_126d_accel_v097_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(126).min(), opinc.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_126d_accel_v098_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(126).min(), opinc.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_126d_accel_v099_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(126).min(), opinc.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_252d_accel_v100_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(252).min(), opinc.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_252d_accel_v101_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(252).min(), opinc.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_252d_accel_v102_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(252).min(), opinc.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_504d_accel_v103_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(504).min(), opinc.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_504d_accel_v104_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(504).min(), opinc.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_low_504d_accel_v105_signal(opinc):
    base = _safe_div(opinc - opinc.rolling(504).min(), opinc.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_21d_accel_v106_signal(opinc):
    base = _safe_div(opinc.rolling(21).max() - opinc, opinc.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_21d_accel_v107_signal(opinc):
    base = _safe_div(opinc.rolling(21).max() - opinc, opinc.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_21d_accel_v108_signal(opinc):
    base = _safe_div(opinc.rolling(21).max() - opinc, opinc.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_63d_accel_v109_signal(opinc):
    base = _safe_div(opinc.rolling(63).max() - opinc, opinc.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_63d_accel_v110_signal(opinc):
    base = _safe_div(opinc.rolling(63).max() - opinc, opinc.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_63d_accel_v111_signal(opinc):
    base = _safe_div(opinc.rolling(63).max() - opinc, opinc.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_126d_accel_v112_signal(opinc):
    base = _safe_div(opinc.rolling(126).max() - opinc, opinc.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_126d_accel_v113_signal(opinc):
    base = _safe_div(opinc.rolling(126).max() - opinc, opinc.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_126d_accel_v114_signal(opinc):
    base = _safe_div(opinc.rolling(126).max() - opinc, opinc.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_252d_accel_v115_signal(opinc):
    base = _safe_div(opinc.rolling(252).max() - opinc, opinc.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_252d_accel_v116_signal(opinc):
    base = _safe_div(opinc.rolling(252).max() - opinc, opinc.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_252d_accel_v117_signal(opinc):
    base = _safe_div(opinc.rolling(252).max() - opinc, opinc.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_504d_accel_v118_signal(opinc):
    base = _safe_div(opinc.rolling(504).max() - opinc, opinc.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_504d_accel_v119_signal(opinc):
    base = _safe_div(opinc.rolling(504).max() - opinc, opinc.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high opinc
def gm_f45_biotech_f45_operating_profit_margin_dist_high_504d_accel_v120_signal(opinc):
    base = _safe_div(opinc.rolling(504).max() - opinc, opinc.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_21d_accel_v121_signal(opinc):
    base = _safe_div(_mean(opinc, 21) - _mean(opinc, 42), _mean(opinc, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_21d_accel_v122_signal(opinc):
    base = _safe_div(_mean(opinc, 21) - _mean(opinc, 42), _mean(opinc, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_21d_accel_v123_signal(opinc):
    base = _safe_div(_mean(opinc, 21) - _mean(opinc, 42), _mean(opinc, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_63d_accel_v124_signal(opinc):
    base = _safe_div(_mean(opinc, 63) - _mean(opinc, 126), _mean(opinc, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_63d_accel_v125_signal(opinc):
    base = _safe_div(_mean(opinc, 63) - _mean(opinc, 126), _mean(opinc, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_63d_accel_v126_signal(opinc):
    base = _safe_div(_mean(opinc, 63) - _mean(opinc, 126), _mean(opinc, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_126d_accel_v127_signal(opinc):
    base = _safe_div(_mean(opinc, 126) - _mean(opinc, 252), _mean(opinc, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_126d_accel_v128_signal(opinc):
    base = _safe_div(_mean(opinc, 126) - _mean(opinc, 252), _mean(opinc, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_126d_accel_v129_signal(opinc):
    base = _safe_div(_mean(opinc, 126) - _mean(opinc, 252), _mean(opinc, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_252d_accel_v130_signal(opinc):
    base = _safe_div(_mean(opinc, 252) - _mean(opinc, 504), _mean(opinc, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_252d_accel_v131_signal(opinc):
    base = _safe_div(_mean(opinc, 252) - _mean(opinc, 504), _mean(opinc, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_252d_accel_v132_signal(opinc):
    base = _safe_div(_mean(opinc, 252) - _mean(opinc, 504), _mean(opinc, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_504d_accel_v133_signal(opinc):
    base = _safe_div(_mean(opinc, 504) - _mean(opinc, 1008), _mean(opinc, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_504d_accel_v134_signal(opinc):
    base = _safe_div(_mean(opinc, 504) - _mean(opinc, 1008), _mean(opinc, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom opinc
def gm_f45_biotech_f45_operating_profit_margin_mom_504d_accel_v135_signal(opinc):
    base = _safe_div(_mean(opinc, 504) - _mean(opinc, 1008), _mean(opinc, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_21d_accel_v136_signal(opinc):
    base = _std(opinc, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_21d_accel_v137_signal(opinc):
    base = _std(opinc, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_21d_accel_v138_signal(opinc):
    base = _std(opinc, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_63d_accel_v139_signal(opinc):
    base = _std(opinc, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_63d_accel_v140_signal(opinc):
    base = _std(opinc, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_63d_accel_v141_signal(opinc):
    base = _std(opinc, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_126d_accel_v142_signal(opinc):
    base = _std(opinc, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_126d_accel_v143_signal(opinc):
    base = _std(opinc, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_126d_accel_v144_signal(opinc):
    base = _std(opinc, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_252d_accel_v145_signal(opinc):
    base = _std(opinc, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_252d_accel_v146_signal(opinc):
    base = _std(opinc, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_252d_accel_v147_signal(opinc):
    base = _std(opinc, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_504d_accel_v148_signal(opinc):
    base = _std(opinc, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_504d_accel_v149_signal(opinc):
    base = _std(opinc, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol opinc
def gm_f45_biotech_f45_operating_profit_margin_vol_504d_accel_v150_signal(opinc):
    base = _std(opinc, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

