
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_21d_accel_v001_signal(debtc):
    base = _mean(debtc, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_21d_accel_v002_signal(debtc):
    base = _mean(debtc, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_21d_accel_v003_signal(debtc):
    base = _mean(debtc, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_63d_accel_v004_signal(debtc):
    base = _mean(debtc, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_63d_accel_v005_signal(debtc):
    base = _mean(debtc, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_63d_accel_v006_signal(debtc):
    base = _mean(debtc, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_126d_accel_v007_signal(debtc):
    base = _mean(debtc, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_126d_accel_v008_signal(debtc):
    base = _mean(debtc, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_126d_accel_v009_signal(debtc):
    base = _mean(debtc, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_252d_accel_v010_signal(debtc):
    base = _mean(debtc, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_252d_accel_v011_signal(debtc):
    base = _mean(debtc, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_252d_accel_v012_signal(debtc):
    base = _mean(debtc, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_504d_accel_v013_signal(debtc):
    base = _mean(debtc, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_504d_accel_v014_signal(debtc):
    base = _mean(debtc, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_504d_accel_v015_signal(debtc):
    base = _mean(debtc, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_21d_accel_v016_signal(debtc):
    base = _mean(_log(debtc), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_21d_accel_v017_signal(debtc):
    base = _mean(_log(debtc), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_21d_accel_v018_signal(debtc):
    base = _mean(_log(debtc), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_63d_accel_v019_signal(debtc):
    base = _mean(_log(debtc), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_63d_accel_v020_signal(debtc):
    base = _mean(_log(debtc), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_63d_accel_v021_signal(debtc):
    base = _mean(_log(debtc), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_126d_accel_v022_signal(debtc):
    base = _mean(_log(debtc), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_126d_accel_v023_signal(debtc):
    base = _mean(_log(debtc), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_126d_accel_v024_signal(debtc):
    base = _mean(_log(debtc), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_252d_accel_v025_signal(debtc):
    base = _mean(_log(debtc), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_252d_accel_v026_signal(debtc):
    base = _mean(_log(debtc), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_252d_accel_v027_signal(debtc):
    base = _mean(_log(debtc), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_504d_accel_v028_signal(debtc):
    base = _mean(_log(debtc), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_504d_accel_v029_signal(debtc):
    base = _mean(_log(debtc), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_504d_accel_v030_signal(debtc):
    base = _mean(_log(debtc), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_21d_accel_v031_signal(debtc):
    base = _z(debtc, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_21d_accel_v032_signal(debtc):
    base = _z(debtc, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_21d_accel_v033_signal(debtc):
    base = _z(debtc, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_63d_accel_v034_signal(debtc):
    base = _z(debtc, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_63d_accel_v035_signal(debtc):
    base = _z(debtc, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_63d_accel_v036_signal(debtc):
    base = _z(debtc, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_126d_accel_v037_signal(debtc):
    base = _z(debtc, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_126d_accel_v038_signal(debtc):
    base = _z(debtc, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_126d_accel_v039_signal(debtc):
    base = _z(debtc, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_252d_accel_v040_signal(debtc):
    base = _z(debtc, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_252d_accel_v041_signal(debtc):
    base = _z(debtc, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_252d_accel_v042_signal(debtc):
    base = _z(debtc, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_504d_accel_v043_signal(debtc):
    base = _z(debtc, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_504d_accel_v044_signal(debtc):
    base = _z(debtc, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_504d_accel_v045_signal(debtc):
    base = _z(debtc, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_21d_accel_v046_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_21d_accel_v047_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_21d_accel_v048_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_63d_accel_v049_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_63d_accel_v050_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_63d_accel_v051_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_126d_accel_v052_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_126d_accel_v053_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_126d_accel_v054_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_252d_accel_v055_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_252d_accel_v056_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_252d_accel_v057_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_504d_accel_v058_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_504d_accel_v059_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_504d_accel_v060_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_21d_accel_v061_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_21d_accel_v062_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_21d_accel_v063_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_63d_accel_v064_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_63d_accel_v065_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_63d_accel_v066_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_126d_accel_v067_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_126d_accel_v068_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_126d_accel_v069_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_252d_accel_v070_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_252d_accel_v071_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_252d_accel_v072_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_504d_accel_v073_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_504d_accel_v074_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_504d_accel_v075_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_21d_accel_v076_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_21d_accel_v077_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_21d_accel_v078_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_63d_accel_v079_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_63d_accel_v080_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_63d_accel_v081_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_126d_accel_v082_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_126d_accel_v083_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_126d_accel_v084_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_252d_accel_v085_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_252d_accel_v086_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_252d_accel_v087_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_504d_accel_v088_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_504d_accel_v089_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_504d_accel_v090_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_21d_accel_v091_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(21).min(), debtc.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_21d_accel_v092_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(21).min(), debtc.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_21d_accel_v093_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(21).min(), debtc.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_63d_accel_v094_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(63).min(), debtc.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_63d_accel_v095_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(63).min(), debtc.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_63d_accel_v096_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(63).min(), debtc.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_126d_accel_v097_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(126).min(), debtc.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_126d_accel_v098_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(126).min(), debtc.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_126d_accel_v099_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(126).min(), debtc.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_252d_accel_v100_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(252).min(), debtc.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_252d_accel_v101_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(252).min(), debtc.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_252d_accel_v102_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(252).min(), debtc.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_504d_accel_v103_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(504).min(), debtc.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_504d_accel_v104_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(504).min(), debtc.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_504d_accel_v105_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(504).min(), debtc.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_21d_accel_v106_signal(debtc):
    base = _safe_div(debtc.rolling(21).max() - debtc, debtc.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_21d_accel_v107_signal(debtc):
    base = _safe_div(debtc.rolling(21).max() - debtc, debtc.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_21d_accel_v108_signal(debtc):
    base = _safe_div(debtc.rolling(21).max() - debtc, debtc.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_63d_accel_v109_signal(debtc):
    base = _safe_div(debtc.rolling(63).max() - debtc, debtc.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_63d_accel_v110_signal(debtc):
    base = _safe_div(debtc.rolling(63).max() - debtc, debtc.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_63d_accel_v111_signal(debtc):
    base = _safe_div(debtc.rolling(63).max() - debtc, debtc.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_126d_accel_v112_signal(debtc):
    base = _safe_div(debtc.rolling(126).max() - debtc, debtc.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_126d_accel_v113_signal(debtc):
    base = _safe_div(debtc.rolling(126).max() - debtc, debtc.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_126d_accel_v114_signal(debtc):
    base = _safe_div(debtc.rolling(126).max() - debtc, debtc.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_252d_accel_v115_signal(debtc):
    base = _safe_div(debtc.rolling(252).max() - debtc, debtc.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_252d_accel_v116_signal(debtc):
    base = _safe_div(debtc.rolling(252).max() - debtc, debtc.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_252d_accel_v117_signal(debtc):
    base = _safe_div(debtc.rolling(252).max() - debtc, debtc.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_504d_accel_v118_signal(debtc):
    base = _safe_div(debtc.rolling(504).max() - debtc, debtc.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_504d_accel_v119_signal(debtc):
    base = _safe_div(debtc.rolling(504).max() - debtc, debtc.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_504d_accel_v120_signal(debtc):
    base = _safe_div(debtc.rolling(504).max() - debtc, debtc.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_21d_accel_v121_signal(debtc):
    base = _safe_div(_mean(debtc, 21) - _mean(debtc, 42), _mean(debtc, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_21d_accel_v122_signal(debtc):
    base = _safe_div(_mean(debtc, 21) - _mean(debtc, 42), _mean(debtc, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_21d_accel_v123_signal(debtc):
    base = _safe_div(_mean(debtc, 21) - _mean(debtc, 42), _mean(debtc, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_63d_accel_v124_signal(debtc):
    base = _safe_div(_mean(debtc, 63) - _mean(debtc, 126), _mean(debtc, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_63d_accel_v125_signal(debtc):
    base = _safe_div(_mean(debtc, 63) - _mean(debtc, 126), _mean(debtc, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_63d_accel_v126_signal(debtc):
    base = _safe_div(_mean(debtc, 63) - _mean(debtc, 126), _mean(debtc, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_126d_accel_v127_signal(debtc):
    base = _safe_div(_mean(debtc, 126) - _mean(debtc, 252), _mean(debtc, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_126d_accel_v128_signal(debtc):
    base = _safe_div(_mean(debtc, 126) - _mean(debtc, 252), _mean(debtc, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_126d_accel_v129_signal(debtc):
    base = _safe_div(_mean(debtc, 126) - _mean(debtc, 252), _mean(debtc, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_252d_accel_v130_signal(debtc):
    base = _safe_div(_mean(debtc, 252) - _mean(debtc, 504), _mean(debtc, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_252d_accel_v131_signal(debtc):
    base = _safe_div(_mean(debtc, 252) - _mean(debtc, 504), _mean(debtc, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_252d_accel_v132_signal(debtc):
    base = _safe_div(_mean(debtc, 252) - _mean(debtc, 504), _mean(debtc, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_504d_accel_v133_signal(debtc):
    base = _safe_div(_mean(debtc, 504) - _mean(debtc, 1008), _mean(debtc, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_504d_accel_v134_signal(debtc):
    base = _safe_div(_mean(debtc, 504) - _mean(debtc, 1008), _mean(debtc, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_504d_accel_v135_signal(debtc):
    base = _safe_div(_mean(debtc, 504) - _mean(debtc, 1008), _mean(debtc, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_21d_accel_v136_signal(debtc):
    base = _std(debtc, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_21d_accel_v137_signal(debtc):
    base = _std(debtc, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_21d_accel_v138_signal(debtc):
    base = _std(debtc, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_63d_accel_v139_signal(debtc):
    base = _std(debtc, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_63d_accel_v140_signal(debtc):
    base = _std(debtc, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_63d_accel_v141_signal(debtc):
    base = _std(debtc, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_126d_accel_v142_signal(debtc):
    base = _std(debtc, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_126d_accel_v143_signal(debtc):
    base = _std(debtc, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_126d_accel_v144_signal(debtc):
    base = _std(debtc, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_252d_accel_v145_signal(debtc):
    base = _std(debtc, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_252d_accel_v146_signal(debtc):
    base = _std(debtc, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_252d_accel_v147_signal(debtc):
    base = _std(debtc, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_504d_accel_v148_signal(debtc):
    base = _std(debtc, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_504d_accel_v149_signal(debtc):
    base = _std(debtc, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_504d_accel_v150_signal(debtc):
    base = _std(debtc, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

