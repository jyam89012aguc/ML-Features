import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 accel mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_mean_5d_accel_v001_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, sharesbas.abs()+1e-9)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_mean_21d_accel_v002_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, sharesbas.abs()+1e-9)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_mean_63d_accel_v003_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, sharesbas.abs()+1e-9)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_mean_126d_accel_v004_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, sharesbas.abs()+1e-9)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_mean_252d_accel_v005_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, sharesbas.abs()+1e-9)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_mean_5d_accel_v006_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_float
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_mean_21d_accel_v007_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_float
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_mean_63d_accel_v008_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_float
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_mean_126d_accel_v009_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_float
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_mean_252d_accel_v010_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_float
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_mean_5d_accel_v011_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_shares
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_mean_21d_accel_v012_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_shares
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_mean_63d_accel_v013_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_shares
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_mean_126d_accel_v014_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_shares
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_mean_252d_accel_v015_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_shares
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_mean_5d_accel_v016_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = days_to_cover
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_mean_21d_accel_v017_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = days_to_cover
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_mean_63d_accel_v018_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = days_to_cover
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_mean_126d_accel_v019_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = days_to_cover
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_mean_252d_accel_v020_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = days_to_cover
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_mean_5d_accel_v021_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 21)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_mean_21d_accel_v022_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 21)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_mean_63d_accel_v023_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 21)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_mean_126d_accel_v024_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 21)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_mean_252d_accel_v025_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 21)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_mean_5d_accel_v026_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 63)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_mean_21d_accel_v027_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 63)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_mean_63d_accel_v028_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 63)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_mean_126d_accel_v029_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 63)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_mean_252d_accel_v030_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 63)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_mean_5d_accel_v031_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 21)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_mean_21d_accel_v032_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 21)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_mean_63d_accel_v033_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 21)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_mean_126d_accel_v034_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 21)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_mean_252d_accel_v035_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 21)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_mean_5d_accel_v036_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 63)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_mean_21d_accel_v037_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 63)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_mean_63d_accel_v038_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 63)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_mean_126d_accel_v039_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 63)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_mean_252d_accel_v040_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 63)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_mean_5d_accel_v041_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(short_pct_shares, 21)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_mean_21d_accel_v042_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(short_pct_shares, 21)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_mean_63d_accel_v043_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(short_pct_shares, 21)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_mean_126d_accel_v044_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(short_pct_shares, 21)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_mean_252d_accel_v045_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(short_pct_shares, 21)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_mean_5d_accel_v046_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(days_to_cover, 21)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_mean_21d_accel_v047_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(days_to_cover, 21)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_mean_63d_accel_v048_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(days_to_cover, 21)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_mean_126d_accel_v049_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(days_to_cover, 21)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_mean_252d_accel_v050_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(days_to_cover, 21)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_mean_5d_accel_v051_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, volume.abs()+1e-9)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_mean_21d_accel_v052_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, volume.abs()+1e-9)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_mean_63d_accel_v053_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, volume.abs()+1e-9)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_mean_126d_accel_v054_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, volume.abs()+1e-9)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_mean_252d_accel_v055_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, volume.abs()+1e-9)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_mean_5d_accel_v056_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(shortint, 252)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_mean_21d_accel_v057_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(shortint, 252)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_mean_63d_accel_v058_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(shortint, 252)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_mean_126d_accel_v059_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(shortint, 252)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_mean_252d_accel_v060_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(shortint, 252)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_mean_5d_accel_v061_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(short_pct_float, 252)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_mean_21d_accel_v062_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(short_pct_float, 252)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_mean_63d_accel_v063_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(short_pct_float, 252)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_mean_126d_accel_v064_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(short_pct_float, 252)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_mean_252d_accel_v065_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(short_pct_float, 252)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_mean_5d_accel_v066_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(short_pct_float, _pct_change(closeadj, 21), 63)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_mean_21d_accel_v067_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(short_pct_float, _pct_change(closeadj, 21), 63)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_mean_63d_accel_v068_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(short_pct_float, _pct_change(closeadj, 21), 63)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_mean_126d_accel_v069_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(short_pct_float, _pct_change(closeadj, 21), 63)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_mean_252d_accel_v070_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(short_pct_float, _pct_change(closeadj, 21), 63)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_mean_5d_accel_v071_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(days_to_cover, _pct_change(closeadj, 5), 63)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_mean_21d_accel_v072_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(days_to_cover, _pct_change(closeadj, 5), 63)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_mean_63d_accel_v073_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(days_to_cover, _pct_change(closeadj, 5), 63)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_mean_126d_accel_v074_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(days_to_cover, _pct_change(closeadj, 5), 63)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_mean_252d_accel_v075_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(days_to_cover, _pct_change(closeadj, 5), 63)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_ewm_5d_accel_v076_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(shortint, 21), shortint.abs()+1e-9)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_ewm_21d_accel_v077_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(shortint, 21), shortint.abs()+1e-9)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_ewm_63d_accel_v078_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(shortint, 21), shortint.abs()+1e-9)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_ewm_126d_accel_v079_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(shortint, 21), shortint.abs()+1e-9)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_ewm_252d_accel_v080_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(shortint, 21), shortint.abs()+1e-9)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_ewm_5d_accel_v081_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_ewm_21d_accel_v082_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_ewm_63d_accel_v083_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_ewm_126d_accel_v084_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_ewm_252d_accel_v085_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_ewm_5d_accel_v086_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_ewm_21d_accel_v087_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_ewm_63d_accel_v088_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_ewm_126d_accel_v089_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_ewm_252d_accel_v090_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_ewm_5d_accel_v091_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_ewm_21d_accel_v092_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_ewm_63d_accel_v093_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_ewm_126d_accel_v094_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_ewm_252d_accel_v095_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_ewm_5d_accel_v096_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(shortint, 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_ewm_21d_accel_v097_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(shortint, 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_ewm_63d_accel_v098_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(shortint, 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_ewm_126d_accel_v099_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(shortint, 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_ewm_252d_accel_v100_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(shortint, 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_ewm_5d_accel_v101_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(short_pct_float, 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_ewm_21d_accel_v102_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(short_pct_float, 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_ewm_63d_accel_v103_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(short_pct_float, 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_ewm_126d_accel_v104_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(short_pct_float, 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_ewm_252d_accel_v105_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(short_pct_float, 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_ewm_5d_accel_v106_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(days_to_cover, 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_ewm_21d_accel_v107_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(days_to_cover, 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_ewm_63d_accel_v108_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(days_to_cover, 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_ewm_126d_accel_v109_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(days_to_cover, 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_ewm_252d_accel_v110_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(days_to_cover, 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_ewm_5d_accel_v111_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_ewm_21d_accel_v112_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_ewm_63d_accel_v113_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_ewm_126d_accel_v114_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_ewm_252d_accel_v115_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_ewm_5d_accel_v116_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_ewm_21d_accel_v117_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_ewm_63d_accel_v118_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_ewm_126d_accel_v119_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_ewm_252d_accel_v120_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_ewm_5d_accel_v121_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_ewm_21d_accel_v122_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_ewm_63d_accel_v123_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_ewm_126d_accel_v124_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_ewm_252d_accel_v125_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_ewm_5d_accel_v126_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _slope(_z(short_pct_float, 252), 63)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_ewm_21d_accel_v127_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _slope(_z(short_pct_float, 252), 63)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_ewm_63d_accel_v128_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _slope(_z(short_pct_float, 252), 63)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_ewm_126d_accel_v129_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _slope(_z(short_pct_float, 252), 63)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_ewm_252d_accel_v130_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _slope(_z(short_pct_float, 252), 63)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_ewm_5d_accel_v131_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _std(_diff(short_pct_float, 1), 63)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_ewm_21d_accel_v132_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _std(_diff(short_pct_float, 1), 63)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_ewm_63d_accel_v133_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _std(_diff(short_pct_float, 1), 63)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_ewm_126d_accel_v134_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _std(_diff(short_pct_float, 1), 63)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_ewm_252d_accel_v135_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _std(_diff(short_pct_float, 1), 63)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_ewm_5d_accel_v136_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _autocorr(short_pct_float, 63, 5)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_ewm_21d_accel_v137_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _autocorr(short_pct_float, 63, 5)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_ewm_63d_accel_v138_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _autocorr(short_pct_float, 63, 5)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_ewm_126d_accel_v139_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _autocorr(short_pct_float, 63, 5)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_ewm_252d_accel_v140_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _autocorr(short_pct_float, 63, 5)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_ewm_5d_accel_v141_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _skew(_diff(short_pct_float, 1), 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_ewm_21d_accel_v142_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _skew(_diff(short_pct_float, 1), 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_ewm_63d_accel_v143_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _skew(_diff(short_pct_float, 1), 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_ewm_126d_accel_v144_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _skew(_diff(short_pct_float, 1), 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_ewm_252d_accel_v145_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _skew(_diff(short_pct_float, 1), 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_ewm_5d_accel_v146_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = -_safe_div(shortint, (closeadj*sharesbas).abs()+1e-9)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_ewm_21d_accel_v147_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = -_safe_div(shortint, (closeadj*sharesbas).abs()+1e-9)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_ewm_63d_accel_v148_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = -_safe_div(shortint, (closeadj*sharesbas).abs()+1e-9)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_ewm_126d_accel_v149_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = -_safe_div(shortint, (closeadj*sharesbas).abs()+1e-9)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_ewm_252d_accel_v150_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = -_safe_div(shortint, (closeadj*sharesbas).abs()+1e-9)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

