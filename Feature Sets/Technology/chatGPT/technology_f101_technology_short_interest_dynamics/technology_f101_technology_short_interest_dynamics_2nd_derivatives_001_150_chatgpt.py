import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 slope mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_mean_5d_slope_v001_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, sharesbas.abs()+1e-9)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_mean_21d_slope_v002_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, sharesbas.abs()+1e-9)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_mean_63d_slope_v003_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, sharesbas.abs()+1e-9)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_mean_126d_slope_v004_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, sharesbas.abs()+1e-9)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_mean_252d_slope_v005_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, sharesbas.abs()+1e-9)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_mean_5d_slope_v006_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_float
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_mean_21d_slope_v007_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_float
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_mean_63d_slope_v008_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_float
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_mean_126d_slope_v009_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_float
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_mean_252d_slope_v010_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_float
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_mean_5d_slope_v011_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_shares
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core11 slope mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_mean_21d_slope_v012_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_shares
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_mean_63d_slope_v013_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_shares
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core13 slope mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_mean_126d_slope_v014_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_shares
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core14 slope mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_mean_252d_slope_v015_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_shares
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_mean_5d_slope_v016_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = days_to_cover
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_mean_21d_slope_v017_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = days_to_cover
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_mean_63d_slope_v018_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = days_to_cover
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_mean_126d_slope_v019_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = days_to_cover
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_mean_252d_slope_v020_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = days_to_cover
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_mean_5d_slope_v021_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 21)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_mean_21d_slope_v022_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 21)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_mean_63d_slope_v023_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 21)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_mean_126d_slope_v024_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 21)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_mean_252d_slope_v025_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 21)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_mean_5d_slope_v026_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 63)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core11 slope mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_mean_21d_slope_v027_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 63)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_mean_63d_slope_v028_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 63)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core13 slope mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_mean_126d_slope_v029_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 63)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core14 slope mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_mean_252d_slope_v030_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 63)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_mean_5d_slope_v031_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 21)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_mean_21d_slope_v032_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 21)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_mean_63d_slope_v033_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 21)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_mean_126d_slope_v034_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 21)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_mean_252d_slope_v035_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 21)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_mean_5d_slope_v036_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 63)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_mean_21d_slope_v037_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 63)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_mean_63d_slope_v038_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 63)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_mean_126d_slope_v039_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 63)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_mean_252d_slope_v040_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 63)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_mean_5d_slope_v041_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(short_pct_shares, 21)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core11 slope mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_mean_21d_slope_v042_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(short_pct_shares, 21)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_mean_63d_slope_v043_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(short_pct_shares, 21)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core13 slope mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_mean_126d_slope_v044_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(short_pct_shares, 21)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core14 slope mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_mean_252d_slope_v045_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(short_pct_shares, 21)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_mean_5d_slope_v046_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(days_to_cover, 21)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_mean_21d_slope_v047_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(days_to_cover, 21)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_mean_63d_slope_v048_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(days_to_cover, 21)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_mean_126d_slope_v049_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(days_to_cover, 21)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_mean_252d_slope_v050_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(days_to_cover, 21)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_mean_5d_slope_v051_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, volume.abs()+1e-9)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_mean_21d_slope_v052_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, volume.abs()+1e-9)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_mean_63d_slope_v053_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, volume.abs()+1e-9)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_mean_126d_slope_v054_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, volume.abs()+1e-9)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_mean_252d_slope_v055_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, volume.abs()+1e-9)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_mean_5d_slope_v056_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(shortint, 252)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core11 slope mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_mean_21d_slope_v057_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(shortint, 252)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_mean_63d_slope_v058_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(shortint, 252)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core13 slope mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_mean_126d_slope_v059_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(shortint, 252)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core14 slope mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_mean_252d_slope_v060_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(shortint, 252)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_mean_5d_slope_v061_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(short_pct_float, 252)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_mean_21d_slope_v062_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(short_pct_float, 252)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_mean_63d_slope_v063_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(short_pct_float, 252)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_mean_126d_slope_v064_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(short_pct_float, 252)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_mean_252d_slope_v065_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(short_pct_float, 252)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_mean_5d_slope_v066_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(short_pct_float, _pct_change(closeadj, 21), 63)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_mean_21d_slope_v067_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(short_pct_float, _pct_change(closeadj, 21), 63)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_mean_63d_slope_v068_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(short_pct_float, _pct_change(closeadj, 21), 63)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_mean_126d_slope_v069_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(short_pct_float, _pct_change(closeadj, 21), 63)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_mean_252d_slope_v070_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(short_pct_float, _pct_change(closeadj, 21), 63)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_mean_5d_slope_v071_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(days_to_cover, _pct_change(closeadj, 5), 63)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core11 slope mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_mean_21d_slope_v072_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(days_to_cover, _pct_change(closeadj, 5), 63)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_mean_63d_slope_v073_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(days_to_cover, _pct_change(closeadj, 5), 63)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core13 slope mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_mean_126d_slope_v074_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(days_to_cover, _pct_change(closeadj, 5), 63)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core14 slope mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_mean_252d_slope_v075_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(days_to_cover, _pct_change(closeadj, 5), 63)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_ewm_5d_slope_v076_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(shortint, 21), shortint.abs()+1e-9)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_ewm_21d_slope_v077_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(shortint, 21), shortint.abs()+1e-9)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_ewm_63d_slope_v078_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(shortint, 21), shortint.abs()+1e-9)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_ewm_126d_slope_v079_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(shortint, 21), shortint.abs()+1e-9)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_ewm_252d_slope_v080_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(shortint, 21), shortint.abs()+1e-9)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_ewm_5d_slope_v081_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_ewm_21d_slope_v082_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_ewm_63d_slope_v083_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_ewm_126d_slope_v084_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_ewm_252d_slope_v085_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_ewm_5d_slope_v086_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core11 slope ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_ewm_21d_slope_v087_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_ewm_63d_slope_v088_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core13 slope ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_ewm_126d_slope_v089_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core14 slope ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_ewm_252d_slope_v090_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_ewm_5d_slope_v091_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_ewm_21d_slope_v092_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_ewm_63d_slope_v093_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_ewm_126d_slope_v094_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_ewm_252d_slope_v095_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_ewm_5d_slope_v096_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(shortint, 252)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_ewm_21d_slope_v097_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(shortint, 252)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_ewm_63d_slope_v098_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(shortint, 252)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_ewm_126d_slope_v099_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(shortint, 252)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_ewm_252d_slope_v100_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(shortint, 252)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_ewm_5d_slope_v101_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(short_pct_float, 252)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core11 slope ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_ewm_21d_slope_v102_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(short_pct_float, 252)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_ewm_63d_slope_v103_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(short_pct_float, 252)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core13 slope ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_ewm_126d_slope_v104_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(short_pct_float, 252)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core14 slope ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_ewm_252d_slope_v105_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(short_pct_float, 252)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_ewm_5d_slope_v106_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(days_to_cover, 252)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_ewm_21d_slope_v107_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(days_to_cover, 252)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_ewm_63d_slope_v108_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(days_to_cover, 252)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_ewm_126d_slope_v109_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(days_to_cover, 252)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_ewm_252d_slope_v110_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(days_to_cover, 252)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_ewm_5d_slope_v111_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_ewm_21d_slope_v112_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_ewm_63d_slope_v113_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_ewm_126d_slope_v114_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_ewm_252d_slope_v115_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_ewm_5d_slope_v116_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core11 slope ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_ewm_21d_slope_v117_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_ewm_63d_slope_v118_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core13 slope ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_ewm_126d_slope_v119_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core14 slope ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_ewm_252d_slope_v120_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_ewm_5d_slope_v121_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_ewm_21d_slope_v122_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_ewm_63d_slope_v123_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_ewm_126d_slope_v124_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_ewm_252d_slope_v125_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_ewm_5d_slope_v126_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _slope(_z(short_pct_float, 252), 63)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_ewm_21d_slope_v127_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _slope(_z(short_pct_float, 252), 63)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_ewm_63d_slope_v128_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _slope(_z(short_pct_float, 252), 63)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_ewm_126d_slope_v129_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _slope(_z(short_pct_float, 252), 63)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_ewm_252d_slope_v130_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _slope(_z(short_pct_float, 252), 63)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_ewm_5d_slope_v131_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _std(_diff(short_pct_float, 1), 63)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core11 slope ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_ewm_21d_slope_v132_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _std(_diff(short_pct_float, 1), 63)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_ewm_63d_slope_v133_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _std(_diff(short_pct_float, 1), 63)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core13 slope ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_ewm_126d_slope_v134_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _std(_diff(short_pct_float, 1), 63)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core14 slope ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_ewm_252d_slope_v135_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _std(_diff(short_pct_float, 1), 63)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_ewm_5d_slope_v136_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _autocorr(short_pct_float, 63, 5)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_ewm_21d_slope_v137_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _autocorr(short_pct_float, 63, 5)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_ewm_63d_slope_v138_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _autocorr(short_pct_float, 63, 5)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_ewm_126d_slope_v139_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _autocorr(short_pct_float, 63, 5)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_ewm_252d_slope_v140_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _autocorr(short_pct_float, 63, 5)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_ewm_5d_slope_v141_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _skew(_diff(short_pct_float, 1), 252)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_ewm_21d_slope_v142_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _skew(_diff(short_pct_float, 1), 252)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_ewm_63d_slope_v143_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _skew(_diff(short_pct_float, 1), 252)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_ewm_126d_slope_v144_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _skew(_diff(short_pct_float, 1), 252)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_ewm_252d_slope_v145_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _skew(_diff(short_pct_float, 1), 252)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_ewm_5d_slope_v146_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = -_safe_div(shortint, (closeadj*sharesbas).abs()+1e-9)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core11 slope ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_ewm_21d_slope_v147_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = -_safe_div(shortint, (closeadj*sharesbas).abs()+1e-9)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_ewm_63d_slope_v148_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = -_safe_div(shortint, (closeadj*sharesbas).abs()+1e-9)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core13 slope ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_ewm_126d_slope_v149_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = -_safe_div(shortint, (closeadj*sharesbas).abs()+1e-9)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core14 slope ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_ewm_252d_slope_v150_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = -_safe_div(shortint, (closeadj*sharesbas).abs()+1e-9)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

