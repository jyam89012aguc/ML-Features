
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw gp
def gm_f44_biotech_f44_gross_profit_margin_raw_21d_accel_v001_signal(gp):
    base = _mean(gp, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw gp
def gm_f44_biotech_f44_gross_profit_margin_raw_21d_accel_v002_signal(gp):
    base = _mean(gp, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw gp
def gm_f44_biotech_f44_gross_profit_margin_raw_21d_accel_v003_signal(gp):
    base = _mean(gp, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw gp
def gm_f44_biotech_f44_gross_profit_margin_raw_63d_accel_v004_signal(gp):
    base = _mean(gp, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw gp
def gm_f44_biotech_f44_gross_profit_margin_raw_63d_accel_v005_signal(gp):
    base = _mean(gp, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw gp
def gm_f44_biotech_f44_gross_profit_margin_raw_63d_accel_v006_signal(gp):
    base = _mean(gp, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw gp
def gm_f44_biotech_f44_gross_profit_margin_raw_126d_accel_v007_signal(gp):
    base = _mean(gp, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw gp
def gm_f44_biotech_f44_gross_profit_margin_raw_126d_accel_v008_signal(gp):
    base = _mean(gp, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw gp
def gm_f44_biotech_f44_gross_profit_margin_raw_126d_accel_v009_signal(gp):
    base = _mean(gp, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw gp
def gm_f44_biotech_f44_gross_profit_margin_raw_252d_accel_v010_signal(gp):
    base = _mean(gp, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw gp
def gm_f44_biotech_f44_gross_profit_margin_raw_252d_accel_v011_signal(gp):
    base = _mean(gp, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw gp
def gm_f44_biotech_f44_gross_profit_margin_raw_252d_accel_v012_signal(gp):
    base = _mean(gp, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw gp
def gm_f44_biotech_f44_gross_profit_margin_raw_504d_accel_v013_signal(gp):
    base = _mean(gp, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw gp
def gm_f44_biotech_f44_gross_profit_margin_raw_504d_accel_v014_signal(gp):
    base = _mean(gp, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw gp
def gm_f44_biotech_f44_gross_profit_margin_raw_504d_accel_v015_signal(gp):
    base = _mean(gp, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log gp
def gm_f44_biotech_f44_gross_profit_margin_log_21d_accel_v016_signal(gp):
    base = _mean(_log(gp), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log gp
def gm_f44_biotech_f44_gross_profit_margin_log_21d_accel_v017_signal(gp):
    base = _mean(_log(gp), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log gp
def gm_f44_biotech_f44_gross_profit_margin_log_21d_accel_v018_signal(gp):
    base = _mean(_log(gp), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log gp
def gm_f44_biotech_f44_gross_profit_margin_log_63d_accel_v019_signal(gp):
    base = _mean(_log(gp), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log gp
def gm_f44_biotech_f44_gross_profit_margin_log_63d_accel_v020_signal(gp):
    base = _mean(_log(gp), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log gp
def gm_f44_biotech_f44_gross_profit_margin_log_63d_accel_v021_signal(gp):
    base = _mean(_log(gp), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log gp
def gm_f44_biotech_f44_gross_profit_margin_log_126d_accel_v022_signal(gp):
    base = _mean(_log(gp), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log gp
def gm_f44_biotech_f44_gross_profit_margin_log_126d_accel_v023_signal(gp):
    base = _mean(_log(gp), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log gp
def gm_f44_biotech_f44_gross_profit_margin_log_126d_accel_v024_signal(gp):
    base = _mean(_log(gp), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log gp
def gm_f44_biotech_f44_gross_profit_margin_log_252d_accel_v025_signal(gp):
    base = _mean(_log(gp), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log gp
def gm_f44_biotech_f44_gross_profit_margin_log_252d_accel_v026_signal(gp):
    base = _mean(_log(gp), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log gp
def gm_f44_biotech_f44_gross_profit_margin_log_252d_accel_v027_signal(gp):
    base = _mean(_log(gp), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log gp
def gm_f44_biotech_f44_gross_profit_margin_log_504d_accel_v028_signal(gp):
    base = _mean(_log(gp), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log gp
def gm_f44_biotech_f44_gross_profit_margin_log_504d_accel_v029_signal(gp):
    base = _mean(_log(gp), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log gp
def gm_f44_biotech_f44_gross_profit_margin_log_504d_accel_v030_signal(gp):
    base = _mean(_log(gp), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z gp
def gm_f44_biotech_f44_gross_profit_margin_z_21d_accel_v031_signal(gp):
    base = _z(gp, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z gp
def gm_f44_biotech_f44_gross_profit_margin_z_21d_accel_v032_signal(gp):
    base = _z(gp, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z gp
def gm_f44_biotech_f44_gross_profit_margin_z_21d_accel_v033_signal(gp):
    base = _z(gp, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z gp
def gm_f44_biotech_f44_gross_profit_margin_z_63d_accel_v034_signal(gp):
    base = _z(gp, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z gp
def gm_f44_biotech_f44_gross_profit_margin_z_63d_accel_v035_signal(gp):
    base = _z(gp, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z gp
def gm_f44_biotech_f44_gross_profit_margin_z_63d_accel_v036_signal(gp):
    base = _z(gp, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z gp
def gm_f44_biotech_f44_gross_profit_margin_z_126d_accel_v037_signal(gp):
    base = _z(gp, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z gp
def gm_f44_biotech_f44_gross_profit_margin_z_126d_accel_v038_signal(gp):
    base = _z(gp, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z gp
def gm_f44_biotech_f44_gross_profit_margin_z_126d_accel_v039_signal(gp):
    base = _z(gp, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z gp
def gm_f44_biotech_f44_gross_profit_margin_z_252d_accel_v040_signal(gp):
    base = _z(gp, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z gp
def gm_f44_biotech_f44_gross_profit_margin_z_252d_accel_v041_signal(gp):
    base = _z(gp, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z gp
def gm_f44_biotech_f44_gross_profit_margin_z_252d_accel_v042_signal(gp):
    base = _z(gp, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z gp
def gm_f44_biotech_f44_gross_profit_margin_z_504d_accel_v043_signal(gp):
    base = _z(gp, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z gp
def gm_f44_biotech_f44_gross_profit_margin_z_504d_accel_v044_signal(gp):
    base = _z(gp, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z gp
def gm_f44_biotech_f44_gross_profit_margin_z_504d_accel_v045_signal(gp):
    base = _z(gp, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps gp
def gm_f44_biotech_f44_gross_profit_margin_ps_21d_accel_v046_signal(gp, sharesbas):
    base = _safe_div(_mean(gp, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps gp
def gm_f44_biotech_f44_gross_profit_margin_ps_21d_accel_v047_signal(gp, sharesbas):
    base = _safe_div(_mean(gp, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps gp
def gm_f44_biotech_f44_gross_profit_margin_ps_21d_accel_v048_signal(gp, sharesbas):
    base = _safe_div(_mean(gp, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps gp
def gm_f44_biotech_f44_gross_profit_margin_ps_63d_accel_v049_signal(gp, sharesbas):
    base = _safe_div(_mean(gp, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps gp
def gm_f44_biotech_f44_gross_profit_margin_ps_63d_accel_v050_signal(gp, sharesbas):
    base = _safe_div(_mean(gp, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps gp
def gm_f44_biotech_f44_gross_profit_margin_ps_63d_accel_v051_signal(gp, sharesbas):
    base = _safe_div(_mean(gp, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps gp
def gm_f44_biotech_f44_gross_profit_margin_ps_126d_accel_v052_signal(gp, sharesbas):
    base = _safe_div(_mean(gp, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps gp
def gm_f44_biotech_f44_gross_profit_margin_ps_126d_accel_v053_signal(gp, sharesbas):
    base = _safe_div(_mean(gp, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps gp
def gm_f44_biotech_f44_gross_profit_margin_ps_126d_accel_v054_signal(gp, sharesbas):
    base = _safe_div(_mean(gp, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps gp
def gm_f44_biotech_f44_gross_profit_margin_ps_252d_accel_v055_signal(gp, sharesbas):
    base = _safe_div(_mean(gp, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps gp
def gm_f44_biotech_f44_gross_profit_margin_ps_252d_accel_v056_signal(gp, sharesbas):
    base = _safe_div(_mean(gp, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps gp
def gm_f44_biotech_f44_gross_profit_margin_ps_252d_accel_v057_signal(gp, sharesbas):
    base = _safe_div(_mean(gp, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps gp
def gm_f44_biotech_f44_gross_profit_margin_ps_504d_accel_v058_signal(gp, sharesbas):
    base = _safe_div(_mean(gp, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps gp
def gm_f44_biotech_f44_gross_profit_margin_ps_504d_accel_v059_signal(gp, sharesbas):
    base = _safe_div(_mean(gp, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps gp
def gm_f44_biotech_f44_gross_profit_margin_ps_504d_accel_v060_signal(gp, sharesbas):
    base = _safe_div(_mean(gp, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_21d_accel_v061_signal(gp, assets):
    base = _safe_div(_mean(gp, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_21d_accel_v062_signal(gp, assets):
    base = _safe_div(_mean(gp, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_21d_accel_v063_signal(gp, assets):
    base = _safe_div(_mean(gp, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_63d_accel_v064_signal(gp, assets):
    base = _safe_div(_mean(gp, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_63d_accel_v065_signal(gp, assets):
    base = _safe_div(_mean(gp, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_63d_accel_v066_signal(gp, assets):
    base = _safe_div(_mean(gp, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_126d_accel_v067_signal(gp, assets):
    base = _safe_div(_mean(gp, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_126d_accel_v068_signal(gp, assets):
    base = _safe_div(_mean(gp, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_126d_accel_v069_signal(gp, assets):
    base = _safe_div(_mean(gp, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_252d_accel_v070_signal(gp, assets):
    base = _safe_div(_mean(gp, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_252d_accel_v071_signal(gp, assets):
    base = _safe_div(_mean(gp, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_252d_accel_v072_signal(gp, assets):
    base = _safe_div(_mean(gp, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_504d_accel_v073_signal(gp, assets):
    base = _safe_div(_mean(gp, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_504d_accel_v074_signal(gp, assets):
    base = _safe_div(_mean(gp, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_504d_accel_v075_signal(gp, assets):
    base = _safe_div(_mean(gp, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_21d_accel_v076_signal(gp, marketcap):
    base = _safe_div(_mean(gp, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_21d_accel_v077_signal(gp, marketcap):
    base = _safe_div(_mean(gp, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_21d_accel_v078_signal(gp, marketcap):
    base = _safe_div(_mean(gp, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_63d_accel_v079_signal(gp, marketcap):
    base = _safe_div(_mean(gp, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_63d_accel_v080_signal(gp, marketcap):
    base = _safe_div(_mean(gp, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_63d_accel_v081_signal(gp, marketcap):
    base = _safe_div(_mean(gp, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_126d_accel_v082_signal(gp, marketcap):
    base = _safe_div(_mean(gp, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_126d_accel_v083_signal(gp, marketcap):
    base = _safe_div(_mean(gp, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_126d_accel_v084_signal(gp, marketcap):
    base = _safe_div(_mean(gp, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_252d_accel_v085_signal(gp, marketcap):
    base = _safe_div(_mean(gp, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_252d_accel_v086_signal(gp, marketcap):
    base = _safe_div(_mean(gp, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_252d_accel_v087_signal(gp, marketcap):
    base = _safe_div(_mean(gp, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_504d_accel_v088_signal(gp, marketcap):
    base = _safe_div(_mean(gp, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_504d_accel_v089_signal(gp, marketcap):
    base = _safe_div(_mean(gp, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled gp
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_504d_accel_v090_signal(gp, marketcap):
    base = _safe_div(_mean(gp, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low gp
def gm_f44_biotech_f44_gross_profit_margin_dist_low_21d_accel_v091_signal(gp):
    base = _safe_div(gp - gp.rolling(21).min(), gp.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low gp
def gm_f44_biotech_f44_gross_profit_margin_dist_low_21d_accel_v092_signal(gp):
    base = _safe_div(gp - gp.rolling(21).min(), gp.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low gp
def gm_f44_biotech_f44_gross_profit_margin_dist_low_21d_accel_v093_signal(gp):
    base = _safe_div(gp - gp.rolling(21).min(), gp.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low gp
def gm_f44_biotech_f44_gross_profit_margin_dist_low_63d_accel_v094_signal(gp):
    base = _safe_div(gp - gp.rolling(63).min(), gp.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low gp
def gm_f44_biotech_f44_gross_profit_margin_dist_low_63d_accel_v095_signal(gp):
    base = _safe_div(gp - gp.rolling(63).min(), gp.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low gp
def gm_f44_biotech_f44_gross_profit_margin_dist_low_63d_accel_v096_signal(gp):
    base = _safe_div(gp - gp.rolling(63).min(), gp.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low gp
def gm_f44_biotech_f44_gross_profit_margin_dist_low_126d_accel_v097_signal(gp):
    base = _safe_div(gp - gp.rolling(126).min(), gp.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low gp
def gm_f44_biotech_f44_gross_profit_margin_dist_low_126d_accel_v098_signal(gp):
    base = _safe_div(gp - gp.rolling(126).min(), gp.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low gp
def gm_f44_biotech_f44_gross_profit_margin_dist_low_126d_accel_v099_signal(gp):
    base = _safe_div(gp - gp.rolling(126).min(), gp.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low gp
def gm_f44_biotech_f44_gross_profit_margin_dist_low_252d_accel_v100_signal(gp):
    base = _safe_div(gp - gp.rolling(252).min(), gp.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low gp
def gm_f44_biotech_f44_gross_profit_margin_dist_low_252d_accel_v101_signal(gp):
    base = _safe_div(gp - gp.rolling(252).min(), gp.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low gp
def gm_f44_biotech_f44_gross_profit_margin_dist_low_252d_accel_v102_signal(gp):
    base = _safe_div(gp - gp.rolling(252).min(), gp.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low gp
def gm_f44_biotech_f44_gross_profit_margin_dist_low_504d_accel_v103_signal(gp):
    base = _safe_div(gp - gp.rolling(504).min(), gp.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low gp
def gm_f44_biotech_f44_gross_profit_margin_dist_low_504d_accel_v104_signal(gp):
    base = _safe_div(gp - gp.rolling(504).min(), gp.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low gp
def gm_f44_biotech_f44_gross_profit_margin_dist_low_504d_accel_v105_signal(gp):
    base = _safe_div(gp - gp.rolling(504).min(), gp.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high gp
def gm_f44_biotech_f44_gross_profit_margin_dist_high_21d_accel_v106_signal(gp):
    base = _safe_div(gp.rolling(21).max() - gp, gp.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high gp
def gm_f44_biotech_f44_gross_profit_margin_dist_high_21d_accel_v107_signal(gp):
    base = _safe_div(gp.rolling(21).max() - gp, gp.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high gp
def gm_f44_biotech_f44_gross_profit_margin_dist_high_21d_accel_v108_signal(gp):
    base = _safe_div(gp.rolling(21).max() - gp, gp.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high gp
def gm_f44_biotech_f44_gross_profit_margin_dist_high_63d_accel_v109_signal(gp):
    base = _safe_div(gp.rolling(63).max() - gp, gp.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high gp
def gm_f44_biotech_f44_gross_profit_margin_dist_high_63d_accel_v110_signal(gp):
    base = _safe_div(gp.rolling(63).max() - gp, gp.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high gp
def gm_f44_biotech_f44_gross_profit_margin_dist_high_63d_accel_v111_signal(gp):
    base = _safe_div(gp.rolling(63).max() - gp, gp.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high gp
def gm_f44_biotech_f44_gross_profit_margin_dist_high_126d_accel_v112_signal(gp):
    base = _safe_div(gp.rolling(126).max() - gp, gp.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high gp
def gm_f44_biotech_f44_gross_profit_margin_dist_high_126d_accel_v113_signal(gp):
    base = _safe_div(gp.rolling(126).max() - gp, gp.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high gp
def gm_f44_biotech_f44_gross_profit_margin_dist_high_126d_accel_v114_signal(gp):
    base = _safe_div(gp.rolling(126).max() - gp, gp.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high gp
def gm_f44_biotech_f44_gross_profit_margin_dist_high_252d_accel_v115_signal(gp):
    base = _safe_div(gp.rolling(252).max() - gp, gp.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high gp
def gm_f44_biotech_f44_gross_profit_margin_dist_high_252d_accel_v116_signal(gp):
    base = _safe_div(gp.rolling(252).max() - gp, gp.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high gp
def gm_f44_biotech_f44_gross_profit_margin_dist_high_252d_accel_v117_signal(gp):
    base = _safe_div(gp.rolling(252).max() - gp, gp.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high gp
def gm_f44_biotech_f44_gross_profit_margin_dist_high_504d_accel_v118_signal(gp):
    base = _safe_div(gp.rolling(504).max() - gp, gp.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high gp
def gm_f44_biotech_f44_gross_profit_margin_dist_high_504d_accel_v119_signal(gp):
    base = _safe_div(gp.rolling(504).max() - gp, gp.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high gp
def gm_f44_biotech_f44_gross_profit_margin_dist_high_504d_accel_v120_signal(gp):
    base = _safe_div(gp.rolling(504).max() - gp, gp.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom gp
def gm_f44_biotech_f44_gross_profit_margin_mom_21d_accel_v121_signal(gp):
    base = _safe_div(_mean(gp, 21) - _mean(gp, 42), _mean(gp, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom gp
def gm_f44_biotech_f44_gross_profit_margin_mom_21d_accel_v122_signal(gp):
    base = _safe_div(_mean(gp, 21) - _mean(gp, 42), _mean(gp, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom gp
def gm_f44_biotech_f44_gross_profit_margin_mom_21d_accel_v123_signal(gp):
    base = _safe_div(_mean(gp, 21) - _mean(gp, 42), _mean(gp, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom gp
def gm_f44_biotech_f44_gross_profit_margin_mom_63d_accel_v124_signal(gp):
    base = _safe_div(_mean(gp, 63) - _mean(gp, 126), _mean(gp, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom gp
def gm_f44_biotech_f44_gross_profit_margin_mom_63d_accel_v125_signal(gp):
    base = _safe_div(_mean(gp, 63) - _mean(gp, 126), _mean(gp, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom gp
def gm_f44_biotech_f44_gross_profit_margin_mom_63d_accel_v126_signal(gp):
    base = _safe_div(_mean(gp, 63) - _mean(gp, 126), _mean(gp, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom gp
def gm_f44_biotech_f44_gross_profit_margin_mom_126d_accel_v127_signal(gp):
    base = _safe_div(_mean(gp, 126) - _mean(gp, 252), _mean(gp, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom gp
def gm_f44_biotech_f44_gross_profit_margin_mom_126d_accel_v128_signal(gp):
    base = _safe_div(_mean(gp, 126) - _mean(gp, 252), _mean(gp, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom gp
def gm_f44_biotech_f44_gross_profit_margin_mom_126d_accel_v129_signal(gp):
    base = _safe_div(_mean(gp, 126) - _mean(gp, 252), _mean(gp, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom gp
def gm_f44_biotech_f44_gross_profit_margin_mom_252d_accel_v130_signal(gp):
    base = _safe_div(_mean(gp, 252) - _mean(gp, 504), _mean(gp, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom gp
def gm_f44_biotech_f44_gross_profit_margin_mom_252d_accel_v131_signal(gp):
    base = _safe_div(_mean(gp, 252) - _mean(gp, 504), _mean(gp, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom gp
def gm_f44_biotech_f44_gross_profit_margin_mom_252d_accel_v132_signal(gp):
    base = _safe_div(_mean(gp, 252) - _mean(gp, 504), _mean(gp, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom gp
def gm_f44_biotech_f44_gross_profit_margin_mom_504d_accel_v133_signal(gp):
    base = _safe_div(_mean(gp, 504) - _mean(gp, 1008), _mean(gp, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom gp
def gm_f44_biotech_f44_gross_profit_margin_mom_504d_accel_v134_signal(gp):
    base = _safe_div(_mean(gp, 504) - _mean(gp, 1008), _mean(gp, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom gp
def gm_f44_biotech_f44_gross_profit_margin_mom_504d_accel_v135_signal(gp):
    base = _safe_div(_mean(gp, 504) - _mean(gp, 1008), _mean(gp, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol gp
def gm_f44_biotech_f44_gross_profit_margin_vol_21d_accel_v136_signal(gp):
    base = _std(gp, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol gp
def gm_f44_biotech_f44_gross_profit_margin_vol_21d_accel_v137_signal(gp):
    base = _std(gp, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol gp
def gm_f44_biotech_f44_gross_profit_margin_vol_21d_accel_v138_signal(gp):
    base = _std(gp, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol gp
def gm_f44_biotech_f44_gross_profit_margin_vol_63d_accel_v139_signal(gp):
    base = _std(gp, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol gp
def gm_f44_biotech_f44_gross_profit_margin_vol_63d_accel_v140_signal(gp):
    base = _std(gp, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol gp
def gm_f44_biotech_f44_gross_profit_margin_vol_63d_accel_v141_signal(gp):
    base = _std(gp, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol gp
def gm_f44_biotech_f44_gross_profit_margin_vol_126d_accel_v142_signal(gp):
    base = _std(gp, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol gp
def gm_f44_biotech_f44_gross_profit_margin_vol_126d_accel_v143_signal(gp):
    base = _std(gp, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol gp
def gm_f44_biotech_f44_gross_profit_margin_vol_126d_accel_v144_signal(gp):
    base = _std(gp, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol gp
def gm_f44_biotech_f44_gross_profit_margin_vol_252d_accel_v145_signal(gp):
    base = _std(gp, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol gp
def gm_f44_biotech_f44_gross_profit_margin_vol_252d_accel_v146_signal(gp):
    base = _std(gp, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol gp
def gm_f44_biotech_f44_gross_profit_margin_vol_252d_accel_v147_signal(gp):
    base = _std(gp, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol gp
def gm_f44_biotech_f44_gross_profit_margin_vol_504d_accel_v148_signal(gp):
    base = _std(gp, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol gp
def gm_f44_biotech_f44_gross_profit_margin_vol_504d_accel_v149_signal(gp):
    base = _std(gp, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol gp
def gm_f44_biotech_f44_gross_profit_margin_vol_504d_accel_v150_signal(gp):
    base = _std(gp, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

