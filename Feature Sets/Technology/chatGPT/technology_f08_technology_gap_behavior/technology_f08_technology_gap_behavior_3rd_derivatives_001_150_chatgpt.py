import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 accel mean 5d
def cg_f08_technology_f08_technology_gap_behavior_core00_mean_5d_accel_v001_signal(open, high, low, close, closeadj, volume):
    base = _mean((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel mean 21d
def cg_f08_technology_f08_technology_gap_behavior_core01_mean_21d_accel_v002_signal(open, high, low, close, closeadj, volume):
    base = _mean((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel mean 63d
def cg_f08_technology_f08_technology_gap_behavior_core02_mean_63d_accel_v003_signal(open, high, low, close, closeadj, volume):
    base = _mean(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel mean 126d
def cg_f08_technology_f08_technology_gap_behavior_core03_mean_126d_accel_v004_signal(open, high, low, close, closeadj, volume):
    base = _mean((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel mean 252d
def cg_f08_technology_f08_technology_gap_behavior_core04_mean_252d_accel_v005_signal(open, high, low, close, closeadj, volume):
    base = _mean((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core05 accel mean 5d
def cg_f08_technology_f08_technology_gap_behavior_core05_mean_5d_accel_v006_signal(open, high, low, close, closeadj, volume):
    base = _mean((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core06 accel mean 21d
def cg_f08_technology_f08_technology_gap_behavior_core06_mean_21d_accel_v007_signal(open, high, low, close, closeadj, volume):
    base = _mean((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core07 accel mean 63d
def cg_f08_technology_f08_technology_gap_behavior_core07_mean_63d_accel_v008_signal(open, high, low, close, closeadj, volume):
    base = _mean((_safe_div(close-open,open.abs()+1e-9)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core08 accel mean 126d
def cg_f08_technology_f08_technology_gap_behavior_core08_mean_126d_accel_v009_signal(open, high, low, close, closeadj, volume):
    base = _mean((volume), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core09 accel mean 252d
def cg_f08_technology_f08_technology_gap_behavior_core09_mean_252d_accel_v010_signal(open, high, low, close, closeadj, volume):
    base = _mean((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core00 accel z 21d
def cg_f08_technology_f08_technology_gap_behavior_core00_z_21d_accel_v011_signal(open, high, low, close, closeadj, volume):
    base = _z((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core01 accel z 63d
def cg_f08_technology_f08_technology_gap_behavior_core01_z_63d_accel_v012_signal(open, high, low, close, closeadj, volume):
    base = _z((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core02 accel z 126d
def cg_f08_technology_f08_technology_gap_behavior_core02_z_126d_accel_v013_signal(open, high, low, close, closeadj, volume):
    base = _z(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core03 accel z 252d
def cg_f08_technology_f08_technology_gap_behavior_core03_z_252d_accel_v014_signal(open, high, low, close, closeadj, volume):
    base = _z((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core04 accel z 5d
def cg_f08_technology_f08_technology_gap_behavior_core04_z_5d_accel_v015_signal(open, high, low, close, closeadj, volume):
    base = _z((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core05 accel z 21d
def cg_f08_technology_f08_technology_gap_behavior_core05_z_21d_accel_v016_signal(open, high, low, close, closeadj, volume):
    base = _z((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel z 63d
def cg_f08_technology_f08_technology_gap_behavior_core06_z_63d_accel_v017_signal(open, high, low, close, closeadj, volume):
    base = _z((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel z 126d
def cg_f08_technology_f08_technology_gap_behavior_core07_z_126d_accel_v018_signal(open, high, low, close, closeadj, volume):
    base = _z((_safe_div(close-open,open.abs()+1e-9)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel z 252d
def cg_f08_technology_f08_technology_gap_behavior_core08_z_252d_accel_v019_signal(open, high, low, close, closeadj, volume):
    base = _z((volume), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel z 5d
def cg_f08_technology_f08_technology_gap_behavior_core09_z_5d_accel_v020_signal(open, high, low, close, closeadj, volume):
    base = _z((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core00 accel rank 63d
def cg_f08_technology_f08_technology_gap_behavior_core00_rank_63d_accel_v021_signal(open, high, low, close, closeadj, volume):
    base = _rank((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel rank 126d
def cg_f08_technology_f08_technology_gap_behavior_core01_rank_126d_accel_v022_signal(open, high, low, close, closeadj, volume):
    base = _rank((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel rank 252d
def cg_f08_technology_f08_technology_gap_behavior_core02_rank_252d_accel_v023_signal(open, high, low, close, closeadj, volume):
    base = _rank(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel rank 5d
def cg_f08_technology_f08_technology_gap_behavior_core03_rank_5d_accel_v024_signal(open, high, low, close, closeadj, volume):
    base = _rank((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel rank 21d
def cg_f08_technology_f08_technology_gap_behavior_core04_rank_21d_accel_v025_signal(open, high, low, close, closeadj, volume):
    base = _rank((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core05 accel rank 63d
def cg_f08_technology_f08_technology_gap_behavior_core05_rank_63d_accel_v026_signal(open, high, low, close, closeadj, volume):
    base = _rank((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel rank 126d
def cg_f08_technology_f08_technology_gap_behavior_core06_rank_126d_accel_v027_signal(open, high, low, close, closeadj, volume):
    base = _rank((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel rank 252d
def cg_f08_technology_f08_technology_gap_behavior_core07_rank_252d_accel_v028_signal(open, high, low, close, closeadj, volume):
    base = _rank((_safe_div(close-open,open.abs()+1e-9)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel rank 5d
def cg_f08_technology_f08_technology_gap_behavior_core08_rank_5d_accel_v029_signal(open, high, low, close, closeadj, volume):
    base = _rank((volume), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel rank 21d
def cg_f08_technology_f08_technology_gap_behavior_core09_rank_21d_accel_v030_signal(open, high, low, close, closeadj, volume):
    base = _rank((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core00 accel std 126d
def cg_f08_technology_f08_technology_gap_behavior_core00_std_126d_accel_v031_signal(open, high, low, close, closeadj, volume):
    base = _std((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel std 252d
def cg_f08_technology_f08_technology_gap_behavior_core01_std_252d_accel_v032_signal(open, high, low, close, closeadj, volume):
    base = _std((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel std 5d
def cg_f08_technology_f08_technology_gap_behavior_core02_std_5d_accel_v033_signal(open, high, low, close, closeadj, volume):
    base = _std(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel std 21d
def cg_f08_technology_f08_technology_gap_behavior_core03_std_21d_accel_v034_signal(open, high, low, close, closeadj, volume):
    base = _std((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel std 63d
def cg_f08_technology_f08_technology_gap_behavior_core04_std_63d_accel_v035_signal(open, high, low, close, closeadj, volume):
    base = _std((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core05 accel std 126d
def cg_f08_technology_f08_technology_gap_behavior_core05_std_126d_accel_v036_signal(open, high, low, close, closeadj, volume):
    base = _std((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core06 accel std 252d
def cg_f08_technology_f08_technology_gap_behavior_core06_std_252d_accel_v037_signal(open, high, low, close, closeadj, volume):
    base = _std((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core07 accel std 5d
def cg_f08_technology_f08_technology_gap_behavior_core07_std_5d_accel_v038_signal(open, high, low, close, closeadj, volume):
    base = _std((_safe_div(close-open,open.abs()+1e-9)), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core08 accel std 21d
def cg_f08_technology_f08_technology_gap_behavior_core08_std_21d_accel_v039_signal(open, high, low, close, closeadj, volume):
    base = _std((volume), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core09 accel std 63d
def cg_f08_technology_f08_technology_gap_behavior_core09_std_63d_accel_v040_signal(open, high, low, close, closeadj, volume):
    base = _std((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core00 accel slope 252d
def cg_f08_technology_f08_technology_gap_behavior_core00_slope_252d_accel_v041_signal(open, high, low, close, closeadj, volume):
    base = _slope((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core01 accel slope 5d
def cg_f08_technology_f08_technology_gap_behavior_core01_slope_5d_accel_v042_signal(open, high, low, close, closeadj, volume):
    base = _slope((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core02 accel slope 21d
def cg_f08_technology_f08_technology_gap_behavior_core02_slope_21d_accel_v043_signal(open, high, low, close, closeadj, volume):
    base = _slope(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core03 accel slope 63d
def cg_f08_technology_f08_technology_gap_behavior_core03_slope_63d_accel_v044_signal(open, high, low, close, closeadj, volume):
    base = _slope((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core04 accel slope 126d
def cg_f08_technology_f08_technology_gap_behavior_core04_slope_126d_accel_v045_signal(open, high, low, close, closeadj, volume):
    base = _slope((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core05 accel slope 252d
def cg_f08_technology_f08_technology_gap_behavior_core05_slope_252d_accel_v046_signal(open, high, low, close, closeadj, volume):
    base = _slope((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel slope 5d
def cg_f08_technology_f08_technology_gap_behavior_core06_slope_5d_accel_v047_signal(open, high, low, close, closeadj, volume):
    base = _slope((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel slope 21d
def cg_f08_technology_f08_technology_gap_behavior_core07_slope_21d_accel_v048_signal(open, high, low, close, closeadj, volume):
    base = _slope((_safe_div(close-open,open.abs()+1e-9)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel slope 63d
def cg_f08_technology_f08_technology_gap_behavior_core08_slope_63d_accel_v049_signal(open, high, low, close, closeadj, volume):
    base = _slope((volume), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel slope 126d
def cg_f08_technology_f08_technology_gap_behavior_core09_slope_126d_accel_v050_signal(open, high, low, close, closeadj, volume):
    base = _slope((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core00 accel diff 5d
def cg_f08_technology_f08_technology_gap_behavior_core00_diff_5d_accel_v051_signal(open, high, low, close, closeadj, volume):
    base = _diff((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel diff 21d
def cg_f08_technology_f08_technology_gap_behavior_core01_diff_21d_accel_v052_signal(open, high, low, close, closeadj, volume):
    base = _diff((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel diff 63d
def cg_f08_technology_f08_technology_gap_behavior_core02_diff_63d_accel_v053_signal(open, high, low, close, closeadj, volume):
    base = _diff(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel diff 126d
def cg_f08_technology_f08_technology_gap_behavior_core03_diff_126d_accel_v054_signal(open, high, low, close, closeadj, volume):
    base = _diff((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel diff 252d
def cg_f08_technology_f08_technology_gap_behavior_core04_diff_252d_accel_v055_signal(open, high, low, close, closeadj, volume):
    base = _diff((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core05 accel diff 5d
def cg_f08_technology_f08_technology_gap_behavior_core05_diff_5d_accel_v056_signal(open, high, low, close, closeadj, volume):
    base = _diff((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel diff 21d
def cg_f08_technology_f08_technology_gap_behavior_core06_diff_21d_accel_v057_signal(open, high, low, close, closeadj, volume):
    base = _diff((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel diff 63d
def cg_f08_technology_f08_technology_gap_behavior_core07_diff_63d_accel_v058_signal(open, high, low, close, closeadj, volume):
    base = _diff((_safe_div(close-open,open.abs()+1e-9)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel diff 126d
def cg_f08_technology_f08_technology_gap_behavior_core08_diff_126d_accel_v059_signal(open, high, low, close, closeadj, volume):
    base = _diff((volume), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel diff 252d
def cg_f08_technology_f08_technology_gap_behavior_core09_diff_252d_accel_v060_signal(open, high, low, close, closeadj, volume):
    base = _diff((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core00 accel pct 21d
def cg_f08_technology_f08_technology_gap_behavior_core00_pct_21d_accel_v061_signal(open, high, low, close, closeadj, volume):
    base = _pct_change(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)).abs()+1.0), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel pct 63d
def cg_f08_technology_f08_technology_gap_behavior_core01_pct_63d_accel_v062_signal(open, high, low, close, closeadj, volume):
    base = _pct_change(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()).abs()+1.0), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel pct 126d
def cg_f08_technology_f08_technology_gap_behavior_core02_pct_126d_accel_v063_signal(open, high, low, close, closeadj, volume):
    base = _pct_change((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)).abs()+1.0), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel pct 252d
def cg_f08_technology_f08_technology_gap_behavior_core03_pct_252d_accel_v064_signal(open, high, low, close, closeadj, volume):
    base = _pct_change(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)).abs()+1.0), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel pct 5d
def cg_f08_technology_f08_technology_gap_behavior_core04_pct_5d_accel_v065_signal(open, high, low, close, closeadj, volume):
    base = _pct_change(((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)).abs()+1.0), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core05 accel pct 21d
def cg_f08_technology_f08_technology_gap_behavior_core05_pct_21d_accel_v066_signal(open, high, low, close, closeadj, volume):
    base = _pct_change(((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)).abs()+1.0), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core06 accel pct 63d
def cg_f08_technology_f08_technology_gap_behavior_core06_pct_63d_accel_v067_signal(open, high, low, close, closeadj, volume):
    base = _pct_change(((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)).abs()+1.0), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core07 accel pct 126d
def cg_f08_technology_f08_technology_gap_behavior_core07_pct_126d_accel_v068_signal(open, high, low, close, closeadj, volume):
    base = _pct_change(((_safe_div(close-open,open.abs()+1e-9)).abs()+1.0), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core08 accel pct 252d
def cg_f08_technology_f08_technology_gap_behavior_core08_pct_252d_accel_v069_signal(open, high, low, close, closeadj, volume):
    base = _pct_change(((volume).abs()+1.0), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core09 accel pct 5d
def cg_f08_technology_f08_technology_gap_behavior_core09_pct_5d_accel_v070_signal(open, high, low, close, closeadj, volume):
    base = _pct_change(((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)).abs()+1.0), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core00 accel ewm 63d
def cg_f08_technology_f08_technology_gap_behavior_core00_ewm_63d_accel_v071_signal(open, high, low, close, closeadj, volume):
    base = _ewm((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core01 accel ewm 126d
def cg_f08_technology_f08_technology_gap_behavior_core01_ewm_126d_accel_v072_signal(open, high, low, close, closeadj, volume):
    base = _ewm((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core02 accel ewm 252d
def cg_f08_technology_f08_technology_gap_behavior_core02_ewm_252d_accel_v073_signal(open, high, low, close, closeadj, volume):
    base = _ewm(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core03 accel ewm 5d
def cg_f08_technology_f08_technology_gap_behavior_core03_ewm_5d_accel_v074_signal(open, high, low, close, closeadj, volume):
    base = _ewm((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core04 accel ewm 21d
def cg_f08_technology_f08_technology_gap_behavior_core04_ewm_21d_accel_v075_signal(open, high, low, close, closeadj, volume):
    base = _ewm((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core05 accel ewm 63d
def cg_f08_technology_f08_technology_gap_behavior_core05_ewm_63d_accel_v076_signal(open, high, low, close, closeadj, volume):
    base = _ewm((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel ewm 126d
def cg_f08_technology_f08_technology_gap_behavior_core06_ewm_126d_accel_v077_signal(open, high, low, close, closeadj, volume):
    base = _ewm((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel ewm 252d
def cg_f08_technology_f08_technology_gap_behavior_core07_ewm_252d_accel_v078_signal(open, high, low, close, closeadj, volume):
    base = _ewm((_safe_div(close-open,open.abs()+1e-9)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel ewm 5d
def cg_f08_technology_f08_technology_gap_behavior_core08_ewm_5d_accel_v079_signal(open, high, low, close, closeadj, volume):
    base = _ewm((volume), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel ewm 21d
def cg_f08_technology_f08_technology_gap_behavior_core09_ewm_21d_accel_v080_signal(open, high, low, close, closeadj, volume):
    base = _ewm((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core00 accel skew 126d
def cg_f08_technology_f08_technology_gap_behavior_core00_skew_126d_accel_v081_signal(open, high, low, close, closeadj, volume):
    base = _skew((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel skew 252d
def cg_f08_technology_f08_technology_gap_behavior_core01_skew_252d_accel_v082_signal(open, high, low, close, closeadj, volume):
    base = _skew((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel skew 5d
def cg_f08_technology_f08_technology_gap_behavior_core02_skew_5d_accel_v083_signal(open, high, low, close, closeadj, volume):
    base = _skew(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel skew 21d
def cg_f08_technology_f08_technology_gap_behavior_core03_skew_21d_accel_v084_signal(open, high, low, close, closeadj, volume):
    base = _skew((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel skew 63d
def cg_f08_technology_f08_technology_gap_behavior_core04_skew_63d_accel_v085_signal(open, high, low, close, closeadj, volume):
    base = _skew((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core05 accel skew 126d
def cg_f08_technology_f08_technology_gap_behavior_core05_skew_126d_accel_v086_signal(open, high, low, close, closeadj, volume):
    base = _skew((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel skew 252d
def cg_f08_technology_f08_technology_gap_behavior_core06_skew_252d_accel_v087_signal(open, high, low, close, closeadj, volume):
    base = _skew((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel skew 5d
def cg_f08_technology_f08_technology_gap_behavior_core07_skew_5d_accel_v088_signal(open, high, low, close, closeadj, volume):
    base = _skew((_safe_div(close-open,open.abs()+1e-9)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel skew 21d
def cg_f08_technology_f08_technology_gap_behavior_core08_skew_21d_accel_v089_signal(open, high, low, close, closeadj, volume):
    base = _skew((volume), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel skew 63d
def cg_f08_technology_f08_technology_gap_behavior_core09_skew_63d_accel_v090_signal(open, high, low, close, closeadj, volume):
    base = _skew((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core00 accel kurt 252d
def cg_f08_technology_f08_technology_gap_behavior_core00_kurt_252d_accel_v091_signal(open, high, low, close, closeadj, volume):
    base = _kurt((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel kurt 5d
def cg_f08_technology_f08_technology_gap_behavior_core01_kurt_5d_accel_v092_signal(open, high, low, close, closeadj, volume):
    base = _kurt((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel kurt 21d
def cg_f08_technology_f08_technology_gap_behavior_core02_kurt_21d_accel_v093_signal(open, high, low, close, closeadj, volume):
    base = _kurt(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel kurt 63d
def cg_f08_technology_f08_technology_gap_behavior_core03_kurt_63d_accel_v094_signal(open, high, low, close, closeadj, volume):
    base = _kurt((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel kurt 126d
def cg_f08_technology_f08_technology_gap_behavior_core04_kurt_126d_accel_v095_signal(open, high, low, close, closeadj, volume):
    base = _kurt((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core05 accel kurt 252d
def cg_f08_technology_f08_technology_gap_behavior_core05_kurt_252d_accel_v096_signal(open, high, low, close, closeadj, volume):
    base = _kurt((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core06 accel kurt 5d
def cg_f08_technology_f08_technology_gap_behavior_core06_kurt_5d_accel_v097_signal(open, high, low, close, closeadj, volume):
    base = _kurt((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core07 accel kurt 21d
def cg_f08_technology_f08_technology_gap_behavior_core07_kurt_21d_accel_v098_signal(open, high, low, close, closeadj, volume):
    base = _kurt((_safe_div(close-open,open.abs()+1e-9)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core08 accel kurt 63d
def cg_f08_technology_f08_technology_gap_behavior_core08_kurt_63d_accel_v099_signal(open, high, low, close, closeadj, volume):
    base = _kurt((volume), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core09 accel kurt 126d
def cg_f08_technology_f08_technology_gap_behavior_core09_kurt_126d_accel_v100_signal(open, high, low, close, closeadj, volume):
    base = _kurt((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core00 accel autocorr 5d
def cg_f08_technology_f08_technology_gap_behavior_core00_autocorr_5d_accel_v101_signal(open, high, low, close, closeadj, volume):
    base = _autocorr((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core01 accel autocorr 21d
def cg_f08_technology_f08_technology_gap_behavior_core01_autocorr_21d_accel_v102_signal(open, high, low, close, closeadj, volume):
    base = _autocorr((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core02 accel autocorr 63d
def cg_f08_technology_f08_technology_gap_behavior_core02_autocorr_63d_accel_v103_signal(open, high, low, close, closeadj, volume):
    base = _autocorr(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core03 accel autocorr 126d
def cg_f08_technology_f08_technology_gap_behavior_core03_autocorr_126d_accel_v104_signal(open, high, low, close, closeadj, volume):
    base = _autocorr((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core04 accel autocorr 252d
def cg_f08_technology_f08_technology_gap_behavior_core04_autocorr_252d_accel_v105_signal(open, high, low, close, closeadj, volume):
    base = _autocorr((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core05 accel autocorr 5d
def cg_f08_technology_f08_technology_gap_behavior_core05_autocorr_5d_accel_v106_signal(open, high, low, close, closeadj, volume):
    base = _autocorr((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel autocorr 21d
def cg_f08_technology_f08_technology_gap_behavior_core06_autocorr_21d_accel_v107_signal(open, high, low, close, closeadj, volume):
    base = _autocorr((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel autocorr 63d
def cg_f08_technology_f08_technology_gap_behavior_core07_autocorr_63d_accel_v108_signal(open, high, low, close, closeadj, volume):
    base = _autocorr((_safe_div(close-open,open.abs()+1e-9)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel autocorr 126d
def cg_f08_technology_f08_technology_gap_behavior_core08_autocorr_126d_accel_v109_signal(open, high, low, close, closeadj, volume):
    base = _autocorr((volume), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel autocorr 252d
def cg_f08_technology_f08_technology_gap_behavior_core09_autocorr_252d_accel_v110_signal(open, high, low, close, closeadj, volume):
    base = _autocorr((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core00 accel snr 21d
def cg_f08_technology_f08_technology_gap_behavior_core00_snr_21d_accel_v111_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_diff((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), max(1,21//3)).abs(), _std(_diff((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)),1), 21)+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel snr 63d
def cg_f08_technology_f08_technology_gap_behavior_core01_snr_63d_accel_v112_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_diff((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), max(1,63//3)).abs(), _std(_diff((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()),1), 63)+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel snr 126d
def cg_f08_technology_f08_technology_gap_behavior_core02_snr_126d_accel_v113_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_diff(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), max(1,126//3)).abs(), _std(_diff(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)),1), 126)+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel snr 252d
def cg_f08_technology_f08_technology_gap_behavior_core03_snr_252d_accel_v114_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_diff((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), max(1,252//3)).abs(), _std(_diff((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)),1), 252)+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel snr 5d
def cg_f08_technology_f08_technology_gap_behavior_core04_snr_5d_accel_v115_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_diff((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), max(1,5//3)).abs(), _std(_diff((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)),1), 5)+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core05 accel snr 21d
def cg_f08_technology_f08_technology_gap_behavior_core05_snr_21d_accel_v116_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_diff((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), max(1,21//3)).abs(), _std(_diff((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)),1), 21)+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel snr 63d
def cg_f08_technology_f08_technology_gap_behavior_core06_snr_63d_accel_v117_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_diff((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), max(1,63//3)).abs(), _std(_diff((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)),1), 63)+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel snr 126d
def cg_f08_technology_f08_technology_gap_behavior_core07_snr_126d_accel_v118_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_diff((_safe_div(close-open,open.abs()+1e-9)), max(1,126//3)).abs(), _std(_diff((_safe_div(close-open,open.abs()+1e-9)),1), 126)+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel snr 252d
def cg_f08_technology_f08_technology_gap_behavior_core08_snr_252d_accel_v119_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_diff((volume), max(1,252//3)).abs(), _std(_diff((volume),1), 252)+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel snr 5d
def cg_f08_technology_f08_technology_gap_behavior_core09_snr_5d_accel_v120_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_diff((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), max(1,5//3)).abs(), _std(_diff((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)),1), 5)+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core00 accel ema_gap 63d
def cg_f08_technology_f08_technology_gap_behavior_core00_ema_gap_63d_accel_v121_signal(open, high, low, close, closeadj, volume):
    base = _mean((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), 63) - _ewm((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel ema_gap 126d
def cg_f08_technology_f08_technology_gap_behavior_core01_ema_gap_126d_accel_v122_signal(open, high, low, close, closeadj, volume):
    base = _mean((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), 126) - _ewm((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel ema_gap 252d
def cg_f08_technology_f08_technology_gap_behavior_core02_ema_gap_252d_accel_v123_signal(open, high, low, close, closeadj, volume):
    base = _mean(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), 252) - _ewm(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel ema_gap 5d
def cg_f08_technology_f08_technology_gap_behavior_core03_ema_gap_5d_accel_v124_signal(open, high, low, close, closeadj, volume):
    base = _mean((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), 5) - _ewm((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel ema_gap 21d
def cg_f08_technology_f08_technology_gap_behavior_core04_ema_gap_21d_accel_v125_signal(open, high, low, close, closeadj, volume):
    base = _mean((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), 21) - _ewm((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core05 accel ema_gap 63d
def cg_f08_technology_f08_technology_gap_behavior_core05_ema_gap_63d_accel_v126_signal(open, high, low, close, closeadj, volume):
    base = _mean((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), 63) - _ewm((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core06 accel ema_gap 126d
def cg_f08_technology_f08_technology_gap_behavior_core06_ema_gap_126d_accel_v127_signal(open, high, low, close, closeadj, volume):
    base = _mean((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), 126) - _ewm((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core07 accel ema_gap 252d
def cg_f08_technology_f08_technology_gap_behavior_core07_ema_gap_252d_accel_v128_signal(open, high, low, close, closeadj, volume):
    base = _mean((_safe_div(close-open,open.abs()+1e-9)), 252) - _ewm((_safe_div(close-open,open.abs()+1e-9)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core08 accel ema_gap 5d
def cg_f08_technology_f08_technology_gap_behavior_core08_ema_gap_5d_accel_v129_signal(open, high, low, close, closeadj, volume):
    base = _mean((volume), 5) - _ewm((volume), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core09 accel ema_gap 21d
def cg_f08_technology_f08_technology_gap_behavior_core09_ema_gap_21d_accel_v130_signal(open, high, low, close, closeadj, volume):
    base = _mean((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), 21) - _ewm((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core00 accel vol_ratio 126d
def cg_f08_technology_f08_technology_gap_behavior_core00_vol_ratio_126d_accel_v131_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_std((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), max(2,126//3)), _std((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), 126).abs()+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core01 accel vol_ratio 252d
def cg_f08_technology_f08_technology_gap_behavior_core01_vol_ratio_252d_accel_v132_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_std((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), max(2,252//3)), _std((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), 252).abs()+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core02 accel vol_ratio 5d
def cg_f08_technology_f08_technology_gap_behavior_core02_vol_ratio_5d_accel_v133_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_std(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), max(2,5//3)), _std(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), 5).abs()+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core03 accel vol_ratio 21d
def cg_f08_technology_f08_technology_gap_behavior_core03_vol_ratio_21d_accel_v134_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_std((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), max(2,21//3)), _std((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), 21).abs()+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core04 accel vol_ratio 63d
def cg_f08_technology_f08_technology_gap_behavior_core04_vol_ratio_63d_accel_v135_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_std((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), max(2,63//3)), _std((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), 63).abs()+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core05 accel vol_ratio 126d
def cg_f08_technology_f08_technology_gap_behavior_core05_vol_ratio_126d_accel_v136_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_std((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), max(2,126//3)), _std((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), 126).abs()+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel vol_ratio 252d
def cg_f08_technology_f08_technology_gap_behavior_core06_vol_ratio_252d_accel_v137_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_std((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), max(2,252//3)), _std((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), 252).abs()+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel vol_ratio 5d
def cg_f08_technology_f08_technology_gap_behavior_core07_vol_ratio_5d_accel_v138_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_std((_safe_div(close-open,open.abs()+1e-9)), max(2,5//3)), _std((_safe_div(close-open,open.abs()+1e-9)), 5).abs()+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel vol_ratio 21d
def cg_f08_technology_f08_technology_gap_behavior_core08_vol_ratio_21d_accel_v139_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_std((volume), max(2,21//3)), _std((volume), 21).abs()+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel vol_ratio 63d
def cg_f08_technology_f08_technology_gap_behavior_core09_vol_ratio_63d_accel_v140_signal(open, high, low, close, closeadj, volume):
    base = _safe_div(_std((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), max(2,63//3)), _std((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), 63).abs()+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core00 accel recent_vs_long 252d
def cg_f08_technology_f08_technology_gap_behavior_core00_recent_vs_long_252d_accel_v141_signal(open, high, low, close, closeadj, volume):
    base = _mean((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), max(2,252//3)) - _mean((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel recent_vs_long 5d
def cg_f08_technology_f08_technology_gap_behavior_core01_recent_vs_long_5d_accel_v142_signal(open, high, low, close, closeadj, volume):
    base = _mean((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), max(2,5//3)) - _mean((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).abs()), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel recent_vs_long 21d
def cg_f08_technology_f08_technology_gap_behavior_core02_recent_vs_long_21d_accel_v143_signal(open, high, low, close, closeadj, volume):
    base = _mean(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), max(2,21//3)) - _mean(((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0).astype(float)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel recent_vs_long 63d
def cg_f08_technology_f08_technology_gap_behavior_core03_recent_vs_long_63d_accel_v144_signal(open, high, low, close, closeadj, volume):
    base = _mean((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), max(2,63//3)) - _mean((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9).where(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0,0)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel recent_vs_long 126d
def cg_f08_technology_f08_technology_gap_behavior_core04_recent_vs_long_126d_accel_v145_signal(open, high, low, close, closeadj, volume):
    base = _mean((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), max(2,126//3)) - _mean((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)<0)&(close>open)).astype(float)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core05 accel recent_vs_long 252d
def cg_f08_technology_f08_technology_gap_behavior_core05_recent_vs_long_252d_accel_v146_signal(open, high, low, close, closeadj, volume):
    base = _mean((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), max(2,252//3)) - _mean((((_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)>0)&(close<open)).astype(float)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel recent_vs_long 5d
def cg_f08_technology_f08_technology_gap_behavior_core06_recent_vs_long_5d_accel_v147_signal(open, high, low, close, closeadj, volume):
    base = _mean((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), max(2,5//3)) - _mean((-_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9)*_safe_div(close-open,open.abs()+1e-9)), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel recent_vs_long 21d
def cg_f08_technology_f08_technology_gap_behavior_core07_recent_vs_long_21d_accel_v148_signal(open, high, low, close, closeadj, volume):
    base = _mean((_safe_div(close-open,open.abs()+1e-9)), max(2,21//3)) - _mean((_safe_div(close-open,open.abs()+1e-9)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel recent_vs_long 63d
def cg_f08_technology_f08_technology_gap_behavior_core08_recent_vs_long_63d_accel_v149_signal(open, high, low, close, closeadj, volume):
    base = _mean((volume), max(2,63//3)) - _mean((volume), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel recent_vs_long 126d
def cg_f08_technology_f08_technology_gap_behavior_core09_recent_vs_long_126d_accel_v150_signal(open, high, low, close, closeadj, volume):
    base = _mean((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), max(2,126//3)) - _mean((_z(_safe_div(open-close.shift(1),close.shift(1).abs()+1e-9),63)*_z(volume,63)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

