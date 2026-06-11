
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw ebit
def gm_f54_biotech_f54_return_on_invested_capital_raw_21d_accel_v001_signal(ebit):
    base = _mean(ebit, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw ebit
def gm_f54_biotech_f54_return_on_invested_capital_raw_21d_accel_v002_signal(ebit):
    base = _mean(ebit, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw ebit
def gm_f54_biotech_f54_return_on_invested_capital_raw_21d_accel_v003_signal(ebit):
    base = _mean(ebit, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw ebit
def gm_f54_biotech_f54_return_on_invested_capital_raw_63d_accel_v004_signal(ebit):
    base = _mean(ebit, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw ebit
def gm_f54_biotech_f54_return_on_invested_capital_raw_63d_accel_v005_signal(ebit):
    base = _mean(ebit, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw ebit
def gm_f54_biotech_f54_return_on_invested_capital_raw_63d_accel_v006_signal(ebit):
    base = _mean(ebit, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw ebit
def gm_f54_biotech_f54_return_on_invested_capital_raw_126d_accel_v007_signal(ebit):
    base = _mean(ebit, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw ebit
def gm_f54_biotech_f54_return_on_invested_capital_raw_126d_accel_v008_signal(ebit):
    base = _mean(ebit, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw ebit
def gm_f54_biotech_f54_return_on_invested_capital_raw_126d_accel_v009_signal(ebit):
    base = _mean(ebit, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw ebit
def gm_f54_biotech_f54_return_on_invested_capital_raw_252d_accel_v010_signal(ebit):
    base = _mean(ebit, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw ebit
def gm_f54_biotech_f54_return_on_invested_capital_raw_252d_accel_v011_signal(ebit):
    base = _mean(ebit, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw ebit
def gm_f54_biotech_f54_return_on_invested_capital_raw_252d_accel_v012_signal(ebit):
    base = _mean(ebit, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw ebit
def gm_f54_biotech_f54_return_on_invested_capital_raw_504d_accel_v013_signal(ebit):
    base = _mean(ebit, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw ebit
def gm_f54_biotech_f54_return_on_invested_capital_raw_504d_accel_v014_signal(ebit):
    base = _mean(ebit, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw ebit
def gm_f54_biotech_f54_return_on_invested_capital_raw_504d_accel_v015_signal(ebit):
    base = _mean(ebit, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log ebit
def gm_f54_biotech_f54_return_on_invested_capital_log_21d_accel_v016_signal(ebit):
    base = _mean(_log(ebit), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log ebit
def gm_f54_biotech_f54_return_on_invested_capital_log_21d_accel_v017_signal(ebit):
    base = _mean(_log(ebit), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log ebit
def gm_f54_biotech_f54_return_on_invested_capital_log_21d_accel_v018_signal(ebit):
    base = _mean(_log(ebit), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log ebit
def gm_f54_biotech_f54_return_on_invested_capital_log_63d_accel_v019_signal(ebit):
    base = _mean(_log(ebit), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log ebit
def gm_f54_biotech_f54_return_on_invested_capital_log_63d_accel_v020_signal(ebit):
    base = _mean(_log(ebit), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log ebit
def gm_f54_biotech_f54_return_on_invested_capital_log_63d_accel_v021_signal(ebit):
    base = _mean(_log(ebit), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log ebit
def gm_f54_biotech_f54_return_on_invested_capital_log_126d_accel_v022_signal(ebit):
    base = _mean(_log(ebit), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log ebit
def gm_f54_biotech_f54_return_on_invested_capital_log_126d_accel_v023_signal(ebit):
    base = _mean(_log(ebit), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log ebit
def gm_f54_biotech_f54_return_on_invested_capital_log_126d_accel_v024_signal(ebit):
    base = _mean(_log(ebit), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log ebit
def gm_f54_biotech_f54_return_on_invested_capital_log_252d_accel_v025_signal(ebit):
    base = _mean(_log(ebit), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log ebit
def gm_f54_biotech_f54_return_on_invested_capital_log_252d_accel_v026_signal(ebit):
    base = _mean(_log(ebit), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log ebit
def gm_f54_biotech_f54_return_on_invested_capital_log_252d_accel_v027_signal(ebit):
    base = _mean(_log(ebit), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log ebit
def gm_f54_biotech_f54_return_on_invested_capital_log_504d_accel_v028_signal(ebit):
    base = _mean(_log(ebit), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log ebit
def gm_f54_biotech_f54_return_on_invested_capital_log_504d_accel_v029_signal(ebit):
    base = _mean(_log(ebit), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log ebit
def gm_f54_biotech_f54_return_on_invested_capital_log_504d_accel_v030_signal(ebit):
    base = _mean(_log(ebit), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z ebit
def gm_f54_biotech_f54_return_on_invested_capital_z_21d_accel_v031_signal(ebit):
    base = _z(ebit, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z ebit
def gm_f54_biotech_f54_return_on_invested_capital_z_21d_accel_v032_signal(ebit):
    base = _z(ebit, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z ebit
def gm_f54_biotech_f54_return_on_invested_capital_z_21d_accel_v033_signal(ebit):
    base = _z(ebit, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z ebit
def gm_f54_biotech_f54_return_on_invested_capital_z_63d_accel_v034_signal(ebit):
    base = _z(ebit, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z ebit
def gm_f54_biotech_f54_return_on_invested_capital_z_63d_accel_v035_signal(ebit):
    base = _z(ebit, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z ebit
def gm_f54_biotech_f54_return_on_invested_capital_z_63d_accel_v036_signal(ebit):
    base = _z(ebit, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z ebit
def gm_f54_biotech_f54_return_on_invested_capital_z_126d_accel_v037_signal(ebit):
    base = _z(ebit, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z ebit
def gm_f54_biotech_f54_return_on_invested_capital_z_126d_accel_v038_signal(ebit):
    base = _z(ebit, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z ebit
def gm_f54_biotech_f54_return_on_invested_capital_z_126d_accel_v039_signal(ebit):
    base = _z(ebit, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z ebit
def gm_f54_biotech_f54_return_on_invested_capital_z_252d_accel_v040_signal(ebit):
    base = _z(ebit, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z ebit
def gm_f54_biotech_f54_return_on_invested_capital_z_252d_accel_v041_signal(ebit):
    base = _z(ebit, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z ebit
def gm_f54_biotech_f54_return_on_invested_capital_z_252d_accel_v042_signal(ebit):
    base = _z(ebit, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z ebit
def gm_f54_biotech_f54_return_on_invested_capital_z_504d_accel_v043_signal(ebit):
    base = _z(ebit, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z ebit
def gm_f54_biotech_f54_return_on_invested_capital_z_504d_accel_v044_signal(ebit):
    base = _z(ebit, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z ebit
def gm_f54_biotech_f54_return_on_invested_capital_z_504d_accel_v045_signal(ebit):
    base = _z(ebit, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps ebit
def gm_f54_biotech_f54_return_on_invested_capital_ps_21d_accel_v046_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps ebit
def gm_f54_biotech_f54_return_on_invested_capital_ps_21d_accel_v047_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps ebit
def gm_f54_biotech_f54_return_on_invested_capital_ps_21d_accel_v048_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps ebit
def gm_f54_biotech_f54_return_on_invested_capital_ps_63d_accel_v049_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps ebit
def gm_f54_biotech_f54_return_on_invested_capital_ps_63d_accel_v050_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps ebit
def gm_f54_biotech_f54_return_on_invested_capital_ps_63d_accel_v051_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps ebit
def gm_f54_biotech_f54_return_on_invested_capital_ps_126d_accel_v052_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps ebit
def gm_f54_biotech_f54_return_on_invested_capital_ps_126d_accel_v053_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps ebit
def gm_f54_biotech_f54_return_on_invested_capital_ps_126d_accel_v054_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps ebit
def gm_f54_biotech_f54_return_on_invested_capital_ps_252d_accel_v055_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps ebit
def gm_f54_biotech_f54_return_on_invested_capital_ps_252d_accel_v056_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps ebit
def gm_f54_biotech_f54_return_on_invested_capital_ps_252d_accel_v057_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps ebit
def gm_f54_biotech_f54_return_on_invested_capital_ps_504d_accel_v058_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps ebit
def gm_f54_biotech_f54_return_on_invested_capital_ps_504d_accel_v059_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps ebit
def gm_f54_biotech_f54_return_on_invested_capital_ps_504d_accel_v060_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_21d_accel_v061_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_21d_accel_v062_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_21d_accel_v063_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_63d_accel_v064_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_63d_accel_v065_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_63d_accel_v066_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_126d_accel_v067_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_126d_accel_v068_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_126d_accel_v069_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_252d_accel_v070_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_252d_accel_v071_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_252d_accel_v072_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_504d_accel_v073_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_504d_accel_v074_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_asset_scaled_504d_accel_v075_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_21d_accel_v076_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_21d_accel_v077_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_21d_accel_v078_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_63d_accel_v079_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_63d_accel_v080_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_63d_accel_v081_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_126d_accel_v082_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_126d_accel_v083_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_126d_accel_v084_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_252d_accel_v085_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_252d_accel_v086_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_252d_accel_v087_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_504d_accel_v088_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_504d_accel_v089_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled ebit
def gm_f54_biotech_f54_return_on_invested_capital_mcap_scaled_504d_accel_v090_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_21d_accel_v091_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(21).min(), ebit.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_21d_accel_v092_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(21).min(), ebit.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_21d_accel_v093_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(21).min(), ebit.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_63d_accel_v094_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(63).min(), ebit.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_63d_accel_v095_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(63).min(), ebit.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_63d_accel_v096_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(63).min(), ebit.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_126d_accel_v097_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(126).min(), ebit.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_126d_accel_v098_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(126).min(), ebit.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_126d_accel_v099_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(126).min(), ebit.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_252d_accel_v100_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(252).min(), ebit.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_252d_accel_v101_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(252).min(), ebit.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_252d_accel_v102_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(252).min(), ebit.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_504d_accel_v103_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(504).min(), ebit.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_504d_accel_v104_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(504).min(), ebit.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_low_504d_accel_v105_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(504).min(), ebit.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_21d_accel_v106_signal(ebit):
    base = _safe_div(ebit.rolling(21).max() - ebit, ebit.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_21d_accel_v107_signal(ebit):
    base = _safe_div(ebit.rolling(21).max() - ebit, ebit.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_21d_accel_v108_signal(ebit):
    base = _safe_div(ebit.rolling(21).max() - ebit, ebit.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_63d_accel_v109_signal(ebit):
    base = _safe_div(ebit.rolling(63).max() - ebit, ebit.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_63d_accel_v110_signal(ebit):
    base = _safe_div(ebit.rolling(63).max() - ebit, ebit.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_63d_accel_v111_signal(ebit):
    base = _safe_div(ebit.rolling(63).max() - ebit, ebit.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_126d_accel_v112_signal(ebit):
    base = _safe_div(ebit.rolling(126).max() - ebit, ebit.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_126d_accel_v113_signal(ebit):
    base = _safe_div(ebit.rolling(126).max() - ebit, ebit.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_126d_accel_v114_signal(ebit):
    base = _safe_div(ebit.rolling(126).max() - ebit, ebit.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_252d_accel_v115_signal(ebit):
    base = _safe_div(ebit.rolling(252).max() - ebit, ebit.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_252d_accel_v116_signal(ebit):
    base = _safe_div(ebit.rolling(252).max() - ebit, ebit.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_252d_accel_v117_signal(ebit):
    base = _safe_div(ebit.rolling(252).max() - ebit, ebit.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_504d_accel_v118_signal(ebit):
    base = _safe_div(ebit.rolling(504).max() - ebit, ebit.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_504d_accel_v119_signal(ebit):
    base = _safe_div(ebit.rolling(504).max() - ebit, ebit.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high ebit
def gm_f54_biotech_f54_return_on_invested_capital_dist_high_504d_accel_v120_signal(ebit):
    base = _safe_div(ebit.rolling(504).max() - ebit, ebit.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom ebit
def gm_f54_biotech_f54_return_on_invested_capital_mom_21d_accel_v121_signal(ebit):
    base = _safe_div(_mean(ebit, 21) - _mean(ebit, 42), _mean(ebit, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom ebit
def gm_f54_biotech_f54_return_on_invested_capital_mom_21d_accel_v122_signal(ebit):
    base = _safe_div(_mean(ebit, 21) - _mean(ebit, 42), _mean(ebit, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom ebit
def gm_f54_biotech_f54_return_on_invested_capital_mom_21d_accel_v123_signal(ebit):
    base = _safe_div(_mean(ebit, 21) - _mean(ebit, 42), _mean(ebit, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom ebit
def gm_f54_biotech_f54_return_on_invested_capital_mom_63d_accel_v124_signal(ebit):
    base = _safe_div(_mean(ebit, 63) - _mean(ebit, 126), _mean(ebit, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom ebit
def gm_f54_biotech_f54_return_on_invested_capital_mom_63d_accel_v125_signal(ebit):
    base = _safe_div(_mean(ebit, 63) - _mean(ebit, 126), _mean(ebit, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom ebit
def gm_f54_biotech_f54_return_on_invested_capital_mom_63d_accel_v126_signal(ebit):
    base = _safe_div(_mean(ebit, 63) - _mean(ebit, 126), _mean(ebit, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom ebit
def gm_f54_biotech_f54_return_on_invested_capital_mom_126d_accel_v127_signal(ebit):
    base = _safe_div(_mean(ebit, 126) - _mean(ebit, 252), _mean(ebit, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom ebit
def gm_f54_biotech_f54_return_on_invested_capital_mom_126d_accel_v128_signal(ebit):
    base = _safe_div(_mean(ebit, 126) - _mean(ebit, 252), _mean(ebit, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom ebit
def gm_f54_biotech_f54_return_on_invested_capital_mom_126d_accel_v129_signal(ebit):
    base = _safe_div(_mean(ebit, 126) - _mean(ebit, 252), _mean(ebit, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom ebit
def gm_f54_biotech_f54_return_on_invested_capital_mom_252d_accel_v130_signal(ebit):
    base = _safe_div(_mean(ebit, 252) - _mean(ebit, 504), _mean(ebit, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom ebit
def gm_f54_biotech_f54_return_on_invested_capital_mom_252d_accel_v131_signal(ebit):
    base = _safe_div(_mean(ebit, 252) - _mean(ebit, 504), _mean(ebit, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom ebit
def gm_f54_biotech_f54_return_on_invested_capital_mom_252d_accel_v132_signal(ebit):
    base = _safe_div(_mean(ebit, 252) - _mean(ebit, 504), _mean(ebit, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom ebit
def gm_f54_biotech_f54_return_on_invested_capital_mom_504d_accel_v133_signal(ebit):
    base = _safe_div(_mean(ebit, 504) - _mean(ebit, 1008), _mean(ebit, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom ebit
def gm_f54_biotech_f54_return_on_invested_capital_mom_504d_accel_v134_signal(ebit):
    base = _safe_div(_mean(ebit, 504) - _mean(ebit, 1008), _mean(ebit, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom ebit
def gm_f54_biotech_f54_return_on_invested_capital_mom_504d_accel_v135_signal(ebit):
    base = _safe_div(_mean(ebit, 504) - _mean(ebit, 1008), _mean(ebit, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol ebit
def gm_f54_biotech_f54_return_on_invested_capital_vol_21d_accel_v136_signal(ebit):
    base = _std(ebit, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol ebit
def gm_f54_biotech_f54_return_on_invested_capital_vol_21d_accel_v137_signal(ebit):
    base = _std(ebit, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol ebit
def gm_f54_biotech_f54_return_on_invested_capital_vol_21d_accel_v138_signal(ebit):
    base = _std(ebit, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol ebit
def gm_f54_biotech_f54_return_on_invested_capital_vol_63d_accel_v139_signal(ebit):
    base = _std(ebit, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol ebit
def gm_f54_biotech_f54_return_on_invested_capital_vol_63d_accel_v140_signal(ebit):
    base = _std(ebit, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol ebit
def gm_f54_biotech_f54_return_on_invested_capital_vol_63d_accel_v141_signal(ebit):
    base = _std(ebit, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol ebit
def gm_f54_biotech_f54_return_on_invested_capital_vol_126d_accel_v142_signal(ebit):
    base = _std(ebit, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol ebit
def gm_f54_biotech_f54_return_on_invested_capital_vol_126d_accel_v143_signal(ebit):
    base = _std(ebit, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol ebit
def gm_f54_biotech_f54_return_on_invested_capital_vol_126d_accel_v144_signal(ebit):
    base = _std(ebit, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol ebit
def gm_f54_biotech_f54_return_on_invested_capital_vol_252d_accel_v145_signal(ebit):
    base = _std(ebit, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol ebit
def gm_f54_biotech_f54_return_on_invested_capital_vol_252d_accel_v146_signal(ebit):
    base = _std(ebit, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol ebit
def gm_f54_biotech_f54_return_on_invested_capital_vol_252d_accel_v147_signal(ebit):
    base = _std(ebit, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol ebit
def gm_f54_biotech_f54_return_on_invested_capital_vol_504d_accel_v148_signal(ebit):
    base = _std(ebit, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol ebit
def gm_f54_biotech_f54_return_on_invested_capital_vol_504d_accel_v149_signal(ebit):
    base = _std(ebit, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol ebit
def gm_f54_biotech_f54_return_on_invested_capital_vol_504d_accel_v150_signal(ebit):
    base = _std(ebit, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

