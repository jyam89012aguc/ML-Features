
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_21d_accel_v001_signal(ebitda):
    base = _mean(ebitda, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_21d_accel_v002_signal(ebitda):
    base = _mean(ebitda, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_21d_accel_v003_signal(ebitda):
    base = _mean(ebitda, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_63d_accel_v004_signal(ebitda):
    base = _mean(ebitda, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_63d_accel_v005_signal(ebitda):
    base = _mean(ebitda, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_63d_accel_v006_signal(ebitda):
    base = _mean(ebitda, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_126d_accel_v007_signal(ebitda):
    base = _mean(ebitda, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_126d_accel_v008_signal(ebitda):
    base = _mean(ebitda, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_126d_accel_v009_signal(ebitda):
    base = _mean(ebitda, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_252d_accel_v010_signal(ebitda):
    base = _mean(ebitda, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_252d_accel_v011_signal(ebitda):
    base = _mean(ebitda, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_252d_accel_v012_signal(ebitda):
    base = _mean(ebitda, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_504d_accel_v013_signal(ebitda):
    base = _mean(ebitda, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_504d_accel_v014_signal(ebitda):
    base = _mean(ebitda, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_504d_accel_v015_signal(ebitda):
    base = _mean(ebitda, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_21d_accel_v016_signal(ebitda):
    base = _mean(_log(ebitda), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_21d_accel_v017_signal(ebitda):
    base = _mean(_log(ebitda), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_21d_accel_v018_signal(ebitda):
    base = _mean(_log(ebitda), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_63d_accel_v019_signal(ebitda):
    base = _mean(_log(ebitda), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_63d_accel_v020_signal(ebitda):
    base = _mean(_log(ebitda), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_63d_accel_v021_signal(ebitda):
    base = _mean(_log(ebitda), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_126d_accel_v022_signal(ebitda):
    base = _mean(_log(ebitda), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_126d_accel_v023_signal(ebitda):
    base = _mean(_log(ebitda), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_126d_accel_v024_signal(ebitda):
    base = _mean(_log(ebitda), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_252d_accel_v025_signal(ebitda):
    base = _mean(_log(ebitda), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_252d_accel_v026_signal(ebitda):
    base = _mean(_log(ebitda), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_252d_accel_v027_signal(ebitda):
    base = _mean(_log(ebitda), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_504d_accel_v028_signal(ebitda):
    base = _mean(_log(ebitda), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_504d_accel_v029_signal(ebitda):
    base = _mean(_log(ebitda), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_504d_accel_v030_signal(ebitda):
    base = _mean(_log(ebitda), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_21d_accel_v031_signal(ebitda):
    base = _z(ebitda, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_21d_accel_v032_signal(ebitda):
    base = _z(ebitda, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_21d_accel_v033_signal(ebitda):
    base = _z(ebitda, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_63d_accel_v034_signal(ebitda):
    base = _z(ebitda, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_63d_accel_v035_signal(ebitda):
    base = _z(ebitda, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_63d_accel_v036_signal(ebitda):
    base = _z(ebitda, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_126d_accel_v037_signal(ebitda):
    base = _z(ebitda, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_126d_accel_v038_signal(ebitda):
    base = _z(ebitda, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_126d_accel_v039_signal(ebitda):
    base = _z(ebitda, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_252d_accel_v040_signal(ebitda):
    base = _z(ebitda, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_252d_accel_v041_signal(ebitda):
    base = _z(ebitda, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_252d_accel_v042_signal(ebitda):
    base = _z(ebitda, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_504d_accel_v043_signal(ebitda):
    base = _z(ebitda, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_504d_accel_v044_signal(ebitda):
    base = _z(ebitda, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_504d_accel_v045_signal(ebitda):
    base = _z(ebitda, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_21d_accel_v046_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_21d_accel_v047_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_21d_accel_v048_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_63d_accel_v049_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_63d_accel_v050_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_63d_accel_v051_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_126d_accel_v052_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_126d_accel_v053_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_126d_accel_v054_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_252d_accel_v055_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_252d_accel_v056_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_252d_accel_v057_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_504d_accel_v058_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_504d_accel_v059_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_504d_accel_v060_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_21d_accel_v061_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_21d_accel_v062_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_21d_accel_v063_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_63d_accel_v064_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_63d_accel_v065_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_63d_accel_v066_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_126d_accel_v067_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_126d_accel_v068_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_126d_accel_v069_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_252d_accel_v070_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_252d_accel_v071_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_252d_accel_v072_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_504d_accel_v073_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_504d_accel_v074_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_504d_accel_v075_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_21d_accel_v076_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_21d_accel_v077_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_21d_accel_v078_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_63d_accel_v079_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_63d_accel_v080_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_63d_accel_v081_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_126d_accel_v082_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_126d_accel_v083_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_126d_accel_v084_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_252d_accel_v085_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_252d_accel_v086_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_252d_accel_v087_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_504d_accel_v088_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_504d_accel_v089_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_504d_accel_v090_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_21d_accel_v091_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(21).min(), ebitda.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_21d_accel_v092_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(21).min(), ebitda.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_21d_accel_v093_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(21).min(), ebitda.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_63d_accel_v094_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(63).min(), ebitda.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_63d_accel_v095_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(63).min(), ebitda.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_63d_accel_v096_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(63).min(), ebitda.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_126d_accel_v097_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(126).min(), ebitda.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_126d_accel_v098_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(126).min(), ebitda.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_126d_accel_v099_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(126).min(), ebitda.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_252d_accel_v100_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(252).min(), ebitda.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_252d_accel_v101_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(252).min(), ebitda.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_252d_accel_v102_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(252).min(), ebitda.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_504d_accel_v103_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(504).min(), ebitda.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_504d_accel_v104_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(504).min(), ebitda.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_504d_accel_v105_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(504).min(), ebitda.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_21d_accel_v106_signal(ebitda):
    base = _safe_div(ebitda.rolling(21).max() - ebitda, ebitda.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_21d_accel_v107_signal(ebitda):
    base = _safe_div(ebitda.rolling(21).max() - ebitda, ebitda.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_21d_accel_v108_signal(ebitda):
    base = _safe_div(ebitda.rolling(21).max() - ebitda, ebitda.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_63d_accel_v109_signal(ebitda):
    base = _safe_div(ebitda.rolling(63).max() - ebitda, ebitda.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_63d_accel_v110_signal(ebitda):
    base = _safe_div(ebitda.rolling(63).max() - ebitda, ebitda.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_63d_accel_v111_signal(ebitda):
    base = _safe_div(ebitda.rolling(63).max() - ebitda, ebitda.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_126d_accel_v112_signal(ebitda):
    base = _safe_div(ebitda.rolling(126).max() - ebitda, ebitda.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_126d_accel_v113_signal(ebitda):
    base = _safe_div(ebitda.rolling(126).max() - ebitda, ebitda.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_126d_accel_v114_signal(ebitda):
    base = _safe_div(ebitda.rolling(126).max() - ebitda, ebitda.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_252d_accel_v115_signal(ebitda):
    base = _safe_div(ebitda.rolling(252).max() - ebitda, ebitda.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_252d_accel_v116_signal(ebitda):
    base = _safe_div(ebitda.rolling(252).max() - ebitda, ebitda.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_252d_accel_v117_signal(ebitda):
    base = _safe_div(ebitda.rolling(252).max() - ebitda, ebitda.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_504d_accel_v118_signal(ebitda):
    base = _safe_div(ebitda.rolling(504).max() - ebitda, ebitda.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_504d_accel_v119_signal(ebitda):
    base = _safe_div(ebitda.rolling(504).max() - ebitda, ebitda.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_504d_accel_v120_signal(ebitda):
    base = _safe_div(ebitda.rolling(504).max() - ebitda, ebitda.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_21d_accel_v121_signal(ebitda):
    base = _safe_div(_mean(ebitda, 21) - _mean(ebitda, 42), _mean(ebitda, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_21d_accel_v122_signal(ebitda):
    base = _safe_div(_mean(ebitda, 21) - _mean(ebitda, 42), _mean(ebitda, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_21d_accel_v123_signal(ebitda):
    base = _safe_div(_mean(ebitda, 21) - _mean(ebitda, 42), _mean(ebitda, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_63d_accel_v124_signal(ebitda):
    base = _safe_div(_mean(ebitda, 63) - _mean(ebitda, 126), _mean(ebitda, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_63d_accel_v125_signal(ebitda):
    base = _safe_div(_mean(ebitda, 63) - _mean(ebitda, 126), _mean(ebitda, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_63d_accel_v126_signal(ebitda):
    base = _safe_div(_mean(ebitda, 63) - _mean(ebitda, 126), _mean(ebitda, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_126d_accel_v127_signal(ebitda):
    base = _safe_div(_mean(ebitda, 126) - _mean(ebitda, 252), _mean(ebitda, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_126d_accel_v128_signal(ebitda):
    base = _safe_div(_mean(ebitda, 126) - _mean(ebitda, 252), _mean(ebitda, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_126d_accel_v129_signal(ebitda):
    base = _safe_div(_mean(ebitda, 126) - _mean(ebitda, 252), _mean(ebitda, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_252d_accel_v130_signal(ebitda):
    base = _safe_div(_mean(ebitda, 252) - _mean(ebitda, 504), _mean(ebitda, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_252d_accel_v131_signal(ebitda):
    base = _safe_div(_mean(ebitda, 252) - _mean(ebitda, 504), _mean(ebitda, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_252d_accel_v132_signal(ebitda):
    base = _safe_div(_mean(ebitda, 252) - _mean(ebitda, 504), _mean(ebitda, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_504d_accel_v133_signal(ebitda):
    base = _safe_div(_mean(ebitda, 504) - _mean(ebitda, 1008), _mean(ebitda, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_504d_accel_v134_signal(ebitda):
    base = _safe_div(_mean(ebitda, 504) - _mean(ebitda, 1008), _mean(ebitda, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_504d_accel_v135_signal(ebitda):
    base = _safe_div(_mean(ebitda, 504) - _mean(ebitda, 1008), _mean(ebitda, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_21d_accel_v136_signal(ebitda):
    base = _std(ebitda, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_21d_accel_v137_signal(ebitda):
    base = _std(ebitda, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_21d_accel_v138_signal(ebitda):
    base = _std(ebitda, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_63d_accel_v139_signal(ebitda):
    base = _std(ebitda, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_63d_accel_v140_signal(ebitda):
    base = _std(ebitda, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_63d_accel_v141_signal(ebitda):
    base = _std(ebitda, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_126d_accel_v142_signal(ebitda):
    base = _std(ebitda, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_126d_accel_v143_signal(ebitda):
    base = _std(ebitda, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_126d_accel_v144_signal(ebitda):
    base = _std(ebitda, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_252d_accel_v145_signal(ebitda):
    base = _std(ebitda, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_252d_accel_v146_signal(ebitda):
    base = _std(ebitda, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_252d_accel_v147_signal(ebitda):
    base = _std(ebitda, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_504d_accel_v148_signal(ebitda):
    base = _std(ebitda, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_504d_accel_v149_signal(ebitda):
    base = _std(ebitda, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_504d_accel_v150_signal(ebitda):
    base = _std(ebitda, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

