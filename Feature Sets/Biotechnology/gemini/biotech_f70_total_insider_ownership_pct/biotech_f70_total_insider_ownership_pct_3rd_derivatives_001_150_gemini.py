
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_21d_accel_v001_signal(sharesownedfollowingtransaction):
    base = _mean(sharesownedfollowingtransaction, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_21d_accel_v002_signal(sharesownedfollowingtransaction):
    base = _mean(sharesownedfollowingtransaction, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_21d_accel_v003_signal(sharesownedfollowingtransaction):
    base = _mean(sharesownedfollowingtransaction, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_63d_accel_v004_signal(sharesownedfollowingtransaction):
    base = _mean(sharesownedfollowingtransaction, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_63d_accel_v005_signal(sharesownedfollowingtransaction):
    base = _mean(sharesownedfollowingtransaction, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_63d_accel_v006_signal(sharesownedfollowingtransaction):
    base = _mean(sharesownedfollowingtransaction, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_126d_accel_v007_signal(sharesownedfollowingtransaction):
    base = _mean(sharesownedfollowingtransaction, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_126d_accel_v008_signal(sharesownedfollowingtransaction):
    base = _mean(sharesownedfollowingtransaction, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_126d_accel_v009_signal(sharesownedfollowingtransaction):
    base = _mean(sharesownedfollowingtransaction, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_252d_accel_v010_signal(sharesownedfollowingtransaction):
    base = _mean(sharesownedfollowingtransaction, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_252d_accel_v011_signal(sharesownedfollowingtransaction):
    base = _mean(sharesownedfollowingtransaction, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_252d_accel_v012_signal(sharesownedfollowingtransaction):
    base = _mean(sharesownedfollowingtransaction, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_504d_accel_v013_signal(sharesownedfollowingtransaction):
    base = _mean(sharesownedfollowingtransaction, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_504d_accel_v014_signal(sharesownedfollowingtransaction):
    base = _mean(sharesownedfollowingtransaction, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_raw_504d_accel_v015_signal(sharesownedfollowingtransaction):
    base = _mean(sharesownedfollowingtransaction, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_21d_accel_v016_signal(sharesownedfollowingtransaction):
    base = _mean(_log(sharesownedfollowingtransaction), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_21d_accel_v017_signal(sharesownedfollowingtransaction):
    base = _mean(_log(sharesownedfollowingtransaction), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_21d_accel_v018_signal(sharesownedfollowingtransaction):
    base = _mean(_log(sharesownedfollowingtransaction), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_63d_accel_v019_signal(sharesownedfollowingtransaction):
    base = _mean(_log(sharesownedfollowingtransaction), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_63d_accel_v020_signal(sharesownedfollowingtransaction):
    base = _mean(_log(sharesownedfollowingtransaction), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_63d_accel_v021_signal(sharesownedfollowingtransaction):
    base = _mean(_log(sharesownedfollowingtransaction), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_126d_accel_v022_signal(sharesownedfollowingtransaction):
    base = _mean(_log(sharesownedfollowingtransaction), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_126d_accel_v023_signal(sharesownedfollowingtransaction):
    base = _mean(_log(sharesownedfollowingtransaction), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_126d_accel_v024_signal(sharesownedfollowingtransaction):
    base = _mean(_log(sharesownedfollowingtransaction), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_252d_accel_v025_signal(sharesownedfollowingtransaction):
    base = _mean(_log(sharesownedfollowingtransaction), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_252d_accel_v026_signal(sharesownedfollowingtransaction):
    base = _mean(_log(sharesownedfollowingtransaction), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_252d_accel_v027_signal(sharesownedfollowingtransaction):
    base = _mean(_log(sharesownedfollowingtransaction), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_504d_accel_v028_signal(sharesownedfollowingtransaction):
    base = _mean(_log(sharesownedfollowingtransaction), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_504d_accel_v029_signal(sharesownedfollowingtransaction):
    base = _mean(_log(sharesownedfollowingtransaction), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_log_504d_accel_v030_signal(sharesownedfollowingtransaction):
    base = _mean(_log(sharesownedfollowingtransaction), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_21d_accel_v031_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_21d_accel_v032_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_21d_accel_v033_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_63d_accel_v034_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_63d_accel_v035_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_63d_accel_v036_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_126d_accel_v037_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_126d_accel_v038_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_126d_accel_v039_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_252d_accel_v040_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_252d_accel_v041_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_252d_accel_v042_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_504d_accel_v043_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_504d_accel_v044_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_z_504d_accel_v045_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_21d_accel_v046_signal(sharesownedfollowingtransaction, sharesbas):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_21d_accel_v047_signal(sharesownedfollowingtransaction, sharesbas):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_21d_accel_v048_signal(sharesownedfollowingtransaction, sharesbas):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_63d_accel_v049_signal(sharesownedfollowingtransaction, sharesbas):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_63d_accel_v050_signal(sharesownedfollowingtransaction, sharesbas):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_63d_accel_v051_signal(sharesownedfollowingtransaction, sharesbas):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_126d_accel_v052_signal(sharesownedfollowingtransaction, sharesbas):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_126d_accel_v053_signal(sharesownedfollowingtransaction, sharesbas):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_126d_accel_v054_signal(sharesownedfollowingtransaction, sharesbas):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_252d_accel_v055_signal(sharesownedfollowingtransaction, sharesbas):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_252d_accel_v056_signal(sharesownedfollowingtransaction, sharesbas):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_252d_accel_v057_signal(sharesownedfollowingtransaction, sharesbas):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_504d_accel_v058_signal(sharesownedfollowingtransaction, sharesbas):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_504d_accel_v059_signal(sharesownedfollowingtransaction, sharesbas):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ps_504d_accel_v060_signal(sharesownedfollowingtransaction, sharesbas):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_21d_accel_v061_signal(sharesownedfollowingtransaction, assets):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_21d_accel_v062_signal(sharesownedfollowingtransaction, assets):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_21d_accel_v063_signal(sharesownedfollowingtransaction, assets):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_63d_accel_v064_signal(sharesownedfollowingtransaction, assets):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_63d_accel_v065_signal(sharesownedfollowingtransaction, assets):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_63d_accel_v066_signal(sharesownedfollowingtransaction, assets):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_126d_accel_v067_signal(sharesownedfollowingtransaction, assets):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_126d_accel_v068_signal(sharesownedfollowingtransaction, assets):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_126d_accel_v069_signal(sharesownedfollowingtransaction, assets):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_252d_accel_v070_signal(sharesownedfollowingtransaction, assets):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_252d_accel_v071_signal(sharesownedfollowingtransaction, assets):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_252d_accel_v072_signal(sharesownedfollowingtransaction, assets):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_504d_accel_v073_signal(sharesownedfollowingtransaction, assets):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_504d_accel_v074_signal(sharesownedfollowingtransaction, assets):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_asset_scaled_504d_accel_v075_signal(sharesownedfollowingtransaction, assets):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_21d_accel_v076_signal(sharesownedfollowingtransaction, marketcap):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_21d_accel_v077_signal(sharesownedfollowingtransaction, marketcap):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_21d_accel_v078_signal(sharesownedfollowingtransaction, marketcap):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_63d_accel_v079_signal(sharesownedfollowingtransaction, marketcap):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_63d_accel_v080_signal(sharesownedfollowingtransaction, marketcap):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_63d_accel_v081_signal(sharesownedfollowingtransaction, marketcap):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_126d_accel_v082_signal(sharesownedfollowingtransaction, marketcap):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_126d_accel_v083_signal(sharesownedfollowingtransaction, marketcap):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_126d_accel_v084_signal(sharesownedfollowingtransaction, marketcap):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_252d_accel_v085_signal(sharesownedfollowingtransaction, marketcap):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_252d_accel_v086_signal(sharesownedfollowingtransaction, marketcap):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_252d_accel_v087_signal(sharesownedfollowingtransaction, marketcap):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_504d_accel_v088_signal(sharesownedfollowingtransaction, marketcap):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_504d_accel_v089_signal(sharesownedfollowingtransaction, marketcap):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mcap_scaled_504d_accel_v090_signal(sharesownedfollowingtransaction, marketcap):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_21d_accel_v091_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction - sharesownedfollowingtransaction.rolling(21).min(), sharesownedfollowingtransaction.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_21d_accel_v092_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction - sharesownedfollowingtransaction.rolling(21).min(), sharesownedfollowingtransaction.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_21d_accel_v093_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction - sharesownedfollowingtransaction.rolling(21).min(), sharesownedfollowingtransaction.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_63d_accel_v094_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction - sharesownedfollowingtransaction.rolling(63).min(), sharesownedfollowingtransaction.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_63d_accel_v095_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction - sharesownedfollowingtransaction.rolling(63).min(), sharesownedfollowingtransaction.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_63d_accel_v096_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction - sharesownedfollowingtransaction.rolling(63).min(), sharesownedfollowingtransaction.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_126d_accel_v097_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction - sharesownedfollowingtransaction.rolling(126).min(), sharesownedfollowingtransaction.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_126d_accel_v098_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction - sharesownedfollowingtransaction.rolling(126).min(), sharesownedfollowingtransaction.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_126d_accel_v099_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction - sharesownedfollowingtransaction.rolling(126).min(), sharesownedfollowingtransaction.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_252d_accel_v100_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction - sharesownedfollowingtransaction.rolling(252).min(), sharesownedfollowingtransaction.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_252d_accel_v101_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction - sharesownedfollowingtransaction.rolling(252).min(), sharesownedfollowingtransaction.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_252d_accel_v102_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction - sharesownedfollowingtransaction.rolling(252).min(), sharesownedfollowingtransaction.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_504d_accel_v103_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction - sharesownedfollowingtransaction.rolling(504).min(), sharesownedfollowingtransaction.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_504d_accel_v104_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction - sharesownedfollowingtransaction.rolling(504).min(), sharesownedfollowingtransaction.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_low_504d_accel_v105_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction - sharesownedfollowingtransaction.rolling(504).min(), sharesownedfollowingtransaction.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_21d_accel_v106_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction.rolling(21).max() - sharesownedfollowingtransaction, sharesownedfollowingtransaction.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_21d_accel_v107_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction.rolling(21).max() - sharesownedfollowingtransaction, sharesownedfollowingtransaction.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_21d_accel_v108_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction.rolling(21).max() - sharesownedfollowingtransaction, sharesownedfollowingtransaction.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_63d_accel_v109_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction.rolling(63).max() - sharesownedfollowingtransaction, sharesownedfollowingtransaction.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_63d_accel_v110_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction.rolling(63).max() - sharesownedfollowingtransaction, sharesownedfollowingtransaction.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_63d_accel_v111_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction.rolling(63).max() - sharesownedfollowingtransaction, sharesownedfollowingtransaction.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_126d_accel_v112_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction.rolling(126).max() - sharesownedfollowingtransaction, sharesownedfollowingtransaction.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_126d_accel_v113_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction.rolling(126).max() - sharesownedfollowingtransaction, sharesownedfollowingtransaction.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_126d_accel_v114_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction.rolling(126).max() - sharesownedfollowingtransaction, sharesownedfollowingtransaction.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_252d_accel_v115_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction.rolling(252).max() - sharesownedfollowingtransaction, sharesownedfollowingtransaction.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_252d_accel_v116_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction.rolling(252).max() - sharesownedfollowingtransaction, sharesownedfollowingtransaction.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_252d_accel_v117_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction.rolling(252).max() - sharesownedfollowingtransaction, sharesownedfollowingtransaction.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_504d_accel_v118_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction.rolling(504).max() - sharesownedfollowingtransaction, sharesownedfollowingtransaction.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_504d_accel_v119_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction.rolling(504).max() - sharesownedfollowingtransaction, sharesownedfollowingtransaction.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_dist_high_504d_accel_v120_signal(sharesownedfollowingtransaction):
    base = _safe_div(sharesownedfollowingtransaction.rolling(504).max() - sharesownedfollowingtransaction, sharesownedfollowingtransaction.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_21d_accel_v121_signal(sharesownedfollowingtransaction):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 21) - _mean(sharesownedfollowingtransaction, 42), _mean(sharesownedfollowingtransaction, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_21d_accel_v122_signal(sharesownedfollowingtransaction):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 21) - _mean(sharesownedfollowingtransaction, 42), _mean(sharesownedfollowingtransaction, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_21d_accel_v123_signal(sharesownedfollowingtransaction):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 21) - _mean(sharesownedfollowingtransaction, 42), _mean(sharesownedfollowingtransaction, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_63d_accel_v124_signal(sharesownedfollowingtransaction):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 63) - _mean(sharesownedfollowingtransaction, 126), _mean(sharesownedfollowingtransaction, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_63d_accel_v125_signal(sharesownedfollowingtransaction):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 63) - _mean(sharesownedfollowingtransaction, 126), _mean(sharesownedfollowingtransaction, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_63d_accel_v126_signal(sharesownedfollowingtransaction):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 63) - _mean(sharesownedfollowingtransaction, 126), _mean(sharesownedfollowingtransaction, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_126d_accel_v127_signal(sharesownedfollowingtransaction):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 126) - _mean(sharesownedfollowingtransaction, 252), _mean(sharesownedfollowingtransaction, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_126d_accel_v128_signal(sharesownedfollowingtransaction):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 126) - _mean(sharesownedfollowingtransaction, 252), _mean(sharesownedfollowingtransaction, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_126d_accel_v129_signal(sharesownedfollowingtransaction):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 126) - _mean(sharesownedfollowingtransaction, 252), _mean(sharesownedfollowingtransaction, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_252d_accel_v130_signal(sharesownedfollowingtransaction):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 252) - _mean(sharesownedfollowingtransaction, 504), _mean(sharesownedfollowingtransaction, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_252d_accel_v131_signal(sharesownedfollowingtransaction):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 252) - _mean(sharesownedfollowingtransaction, 504), _mean(sharesownedfollowingtransaction, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_252d_accel_v132_signal(sharesownedfollowingtransaction):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 252) - _mean(sharesownedfollowingtransaction, 504), _mean(sharesownedfollowingtransaction, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_504d_accel_v133_signal(sharesownedfollowingtransaction):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 504) - _mean(sharesownedfollowingtransaction, 1008), _mean(sharesownedfollowingtransaction, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_504d_accel_v134_signal(sharesownedfollowingtransaction):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 504) - _mean(sharesownedfollowingtransaction, 1008), _mean(sharesownedfollowingtransaction, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mom_504d_accel_v135_signal(sharesownedfollowingtransaction):
    base = _safe_div(_mean(sharesownedfollowingtransaction, 504) - _mean(sharesownedfollowingtransaction, 1008), _mean(sharesownedfollowingtransaction, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_vol_21d_accel_v136_signal(sharesownedfollowingtransaction):
    base = _std(sharesownedfollowingtransaction, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_vol_21d_accel_v137_signal(sharesownedfollowingtransaction):
    base = _std(sharesownedfollowingtransaction, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_vol_21d_accel_v138_signal(sharesownedfollowingtransaction):
    base = _std(sharesownedfollowingtransaction, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_vol_63d_accel_v139_signal(sharesownedfollowingtransaction):
    base = _std(sharesownedfollowingtransaction, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_vol_63d_accel_v140_signal(sharesownedfollowingtransaction):
    base = _std(sharesownedfollowingtransaction, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_vol_63d_accel_v141_signal(sharesownedfollowingtransaction):
    base = _std(sharesownedfollowingtransaction, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_vol_126d_accel_v142_signal(sharesownedfollowingtransaction):
    base = _std(sharesownedfollowingtransaction, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_vol_126d_accel_v143_signal(sharesownedfollowingtransaction):
    base = _std(sharesownedfollowingtransaction, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_vol_126d_accel_v144_signal(sharesownedfollowingtransaction):
    base = _std(sharesownedfollowingtransaction, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_vol_252d_accel_v145_signal(sharesownedfollowingtransaction):
    base = _std(sharesownedfollowingtransaction, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_vol_252d_accel_v146_signal(sharesownedfollowingtransaction):
    base = _std(sharesownedfollowingtransaction, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_vol_252d_accel_v147_signal(sharesownedfollowingtransaction):
    base = _std(sharesownedfollowingtransaction, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_vol_504d_accel_v148_signal(sharesownedfollowingtransaction):
    base = _std(sharesownedfollowingtransaction, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_vol_504d_accel_v149_signal(sharesownedfollowingtransaction):
    base = _std(sharesownedfollowingtransaction, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_vol_504d_accel_v150_signal(sharesownedfollowingtransaction):
    base = _std(sharesownedfollowingtransaction, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

