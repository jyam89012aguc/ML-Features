import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 accel mean 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core00_mean_5d_accel_v001_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel mean 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core01_mean_21d_accel_v002_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel mean 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core02_mean_63d_accel_v003_signal(closeadj, volume):
    base = _mean(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel mean 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core03_mean_126d_accel_v004_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel mean 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core04_mean_252d_accel_v005_signal(closeadj, volume):
    base = _mean((_min(closeadj,252)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core05 accel mean 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core05_mean_5d_accel_v006_signal(closeadj, volume):
    base = _mean((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core06 accel mean 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core06_mean_21d_accel_v007_signal(closeadj, volume):
    base = _mean((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core07 accel mean 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core07_mean_63d_accel_v008_signal(closeadj, volume):
    base = _mean((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core08 accel mean 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core08_mean_126d_accel_v009_signal(closeadj, volume):
    base = _mean((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core09 accel mean 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core09_mean_252d_accel_v010_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core00 accel z 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core00_z_21d_accel_v011_signal(closeadj, volume):
    base = _z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core01 accel z 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core01_z_63d_accel_v012_signal(closeadj, volume):
    base = _z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core02 accel z 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core02_z_126d_accel_v013_signal(closeadj, volume):
    base = _z(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core03 accel z 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core03_z_252d_accel_v014_signal(closeadj, volume):
    base = _z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core04 accel z 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core04_z_5d_accel_v015_signal(closeadj, volume):
    base = _z((_min(closeadj,252)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core05 accel z 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core05_z_21d_accel_v016_signal(closeadj, volume):
    base = _z((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel z 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core06_z_63d_accel_v017_signal(closeadj, volume):
    base = _z((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel z 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core07_z_126d_accel_v018_signal(closeadj, volume):
    base = _z((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel z 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core08_z_252d_accel_v019_signal(closeadj, volume):
    base = _z((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel z 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core09_z_5d_accel_v020_signal(closeadj, volume):
    base = _z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core00 accel rank 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core00_rank_63d_accel_v021_signal(closeadj, volume):
    base = _rank((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel rank 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core01_rank_126d_accel_v022_signal(closeadj, volume):
    base = _rank((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel rank 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core02_rank_252d_accel_v023_signal(closeadj, volume):
    base = _rank(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel rank 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core03_rank_5d_accel_v024_signal(closeadj, volume):
    base = _rank((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel rank 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core04_rank_21d_accel_v025_signal(closeadj, volume):
    base = _rank((_min(closeadj,252)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core05 accel rank 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core05_rank_63d_accel_v026_signal(closeadj, volume):
    base = _rank((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel rank 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core06_rank_126d_accel_v027_signal(closeadj, volume):
    base = _rank((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel rank 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core07_rank_252d_accel_v028_signal(closeadj, volume):
    base = _rank((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel rank 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core08_rank_5d_accel_v029_signal(closeadj, volume):
    base = _rank((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel rank 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core09_rank_21d_accel_v030_signal(closeadj, volume):
    base = _rank((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core00 accel std 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core00_std_126d_accel_v031_signal(closeadj, volume):
    base = _std((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel std 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core01_std_252d_accel_v032_signal(closeadj, volume):
    base = _std((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel std 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core02_std_5d_accel_v033_signal(closeadj, volume):
    base = _std(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel std 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core03_std_21d_accel_v034_signal(closeadj, volume):
    base = _std((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel std 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core04_std_63d_accel_v035_signal(closeadj, volume):
    base = _std((_min(closeadj,252)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core05 accel std 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core05_std_126d_accel_v036_signal(closeadj, volume):
    base = _std((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core06 accel std 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core06_std_252d_accel_v037_signal(closeadj, volume):
    base = _std((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core07 accel std 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core07_std_5d_accel_v038_signal(closeadj, volume):
    base = _std((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core08 accel std 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core08_std_21d_accel_v039_signal(closeadj, volume):
    base = _std((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core09 accel std 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core09_std_63d_accel_v040_signal(closeadj, volume):
    base = _std((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core00 accel slope 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core00_slope_252d_accel_v041_signal(closeadj, volume):
    base = _slope((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core01 accel slope 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core01_slope_5d_accel_v042_signal(closeadj, volume):
    base = _slope((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core02 accel slope 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core02_slope_21d_accel_v043_signal(closeadj, volume):
    base = _slope(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core03 accel slope 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core03_slope_63d_accel_v044_signal(closeadj, volume):
    base = _slope((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core04 accel slope 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core04_slope_126d_accel_v045_signal(closeadj, volume):
    base = _slope((_min(closeadj,252)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core05 accel slope 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core05_slope_252d_accel_v046_signal(closeadj, volume):
    base = _slope((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel slope 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core06_slope_5d_accel_v047_signal(closeadj, volume):
    base = _slope((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel slope 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core07_slope_21d_accel_v048_signal(closeadj, volume):
    base = _slope((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel slope 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core08_slope_63d_accel_v049_signal(closeadj, volume):
    base = _slope((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel slope 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core09_slope_126d_accel_v050_signal(closeadj, volume):
    base = _slope((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core00 accel diff 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core00_diff_5d_accel_v051_signal(closeadj, volume):
    base = _diff((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel diff 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core01_diff_21d_accel_v052_signal(closeadj, volume):
    base = _diff((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel diff 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core02_diff_63d_accel_v053_signal(closeadj, volume):
    base = _diff(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel diff 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core03_diff_126d_accel_v054_signal(closeadj, volume):
    base = _diff((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel diff 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core04_diff_252d_accel_v055_signal(closeadj, volume):
    base = _diff((_min(closeadj,252)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core05 accel diff 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core05_diff_5d_accel_v056_signal(closeadj, volume):
    base = _diff((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel diff 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core06_diff_21d_accel_v057_signal(closeadj, volume):
    base = _diff((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel diff 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core07_diff_63d_accel_v058_signal(closeadj, volume):
    base = _diff((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel diff 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core08_diff_126d_accel_v059_signal(closeadj, volume):
    base = _diff((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel diff 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core09_diff_252d_accel_v060_signal(closeadj, volume):
    base = _diff((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core00 accel pct 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core00_pct_21d_accel_v061_signal(closeadj, volume):
    base = _pct_change(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()+1.0), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel pct 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core01_pct_63d_accel_v062_signal(closeadj, volume):
    base = _pct_change(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()+1.0), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel pct 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core02_pct_126d_accel_v063_signal(closeadj, volume):
    base = _pct_change((((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()).abs()+1.0), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel pct 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core03_pct_252d_accel_v064_signal(closeadj, volume):
    base = _pct_change(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)).abs()+1.0), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel pct 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core04_pct_5d_accel_v065_signal(closeadj, volume):
    base = _pct_change(((_min(closeadj,252)).abs()+1.0), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core05 accel pct 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core05_pct_21d_accel_v066_signal(closeadj, volume):
    base = _pct_change(((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)).abs()+1.0), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core06 accel pct 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core06_pct_63d_accel_v067_signal(closeadj, volume):
    base = _pct_change(((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)).abs()+1.0), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core07 accel pct 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core07_pct_126d_accel_v068_signal(closeadj, volume):
    base = _pct_change(((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)).abs()+1.0), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core08 accel pct 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core08_pct_252d_accel_v069_signal(closeadj, volume):
    base = _pct_change(((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()).abs()+1.0), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core09 accel pct 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core09_pct_5d_accel_v070_signal(closeadj, volume):
    base = _pct_change(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)).abs()+1.0), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core00 accel ewm 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core00_ewm_63d_accel_v071_signal(closeadj, volume):
    base = _ewm((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core01 accel ewm 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core01_ewm_126d_accel_v072_signal(closeadj, volume):
    base = _ewm((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core02 accel ewm 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core02_ewm_252d_accel_v073_signal(closeadj, volume):
    base = _ewm(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core03 accel ewm 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core03_ewm_5d_accel_v074_signal(closeadj, volume):
    base = _ewm((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core04 accel ewm 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core04_ewm_21d_accel_v075_signal(closeadj, volume):
    base = _ewm((_min(closeadj,252)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core05 accel ewm 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core05_ewm_63d_accel_v076_signal(closeadj, volume):
    base = _ewm((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel ewm 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core06_ewm_126d_accel_v077_signal(closeadj, volume):
    base = _ewm((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel ewm 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core07_ewm_252d_accel_v078_signal(closeadj, volume):
    base = _ewm((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel ewm 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core08_ewm_5d_accel_v079_signal(closeadj, volume):
    base = _ewm((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel ewm 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core09_ewm_21d_accel_v080_signal(closeadj, volume):
    base = _ewm((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core00 accel skew 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core00_skew_126d_accel_v081_signal(closeadj, volume):
    base = _skew((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel skew 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core01_skew_252d_accel_v082_signal(closeadj, volume):
    base = _skew((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel skew 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core02_skew_5d_accel_v083_signal(closeadj, volume):
    base = _skew(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel skew 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core03_skew_21d_accel_v084_signal(closeadj, volume):
    base = _skew((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel skew 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core04_skew_63d_accel_v085_signal(closeadj, volume):
    base = _skew((_min(closeadj,252)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core05 accel skew 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core05_skew_126d_accel_v086_signal(closeadj, volume):
    base = _skew((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel skew 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core06_skew_252d_accel_v087_signal(closeadj, volume):
    base = _skew((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel skew 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core07_skew_5d_accel_v088_signal(closeadj, volume):
    base = _skew((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel skew 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core08_skew_21d_accel_v089_signal(closeadj, volume):
    base = _skew((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel skew 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core09_skew_63d_accel_v090_signal(closeadj, volume):
    base = _skew((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core00 accel kurt 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core00_kurt_252d_accel_v091_signal(closeadj, volume):
    base = _kurt((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel kurt 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core01_kurt_5d_accel_v092_signal(closeadj, volume):
    base = _kurt((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel kurt 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core02_kurt_21d_accel_v093_signal(closeadj, volume):
    base = _kurt(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel kurt 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core03_kurt_63d_accel_v094_signal(closeadj, volume):
    base = _kurt((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel kurt 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core04_kurt_126d_accel_v095_signal(closeadj, volume):
    base = _kurt((_min(closeadj,252)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core05 accel kurt 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core05_kurt_252d_accel_v096_signal(closeadj, volume):
    base = _kurt((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core06 accel kurt 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core06_kurt_5d_accel_v097_signal(closeadj, volume):
    base = _kurt((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core07 accel kurt 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core07_kurt_21d_accel_v098_signal(closeadj, volume):
    base = _kurt((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core08 accel kurt 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core08_kurt_63d_accel_v099_signal(closeadj, volume):
    base = _kurt((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core09 accel kurt 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core09_kurt_126d_accel_v100_signal(closeadj, volume):
    base = _kurt((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core00 accel autocorr 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core00_autocorr_5d_accel_v101_signal(closeadj, volume):
    base = _autocorr((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core01 accel autocorr 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core01_autocorr_21d_accel_v102_signal(closeadj, volume):
    base = _autocorr((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core02 accel autocorr 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core02_autocorr_63d_accel_v103_signal(closeadj, volume):
    base = _autocorr(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core03 accel autocorr 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core03_autocorr_126d_accel_v104_signal(closeadj, volume):
    base = _autocorr((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core04 accel autocorr 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core04_autocorr_252d_accel_v105_signal(closeadj, volume):
    base = _autocorr((_min(closeadj,252)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core05 accel autocorr 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core05_autocorr_5d_accel_v106_signal(closeadj, volume):
    base = _autocorr((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel autocorr 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core06_autocorr_21d_accel_v107_signal(closeadj, volume):
    base = _autocorr((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel autocorr 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core07_autocorr_63d_accel_v108_signal(closeadj, volume):
    base = _autocorr((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel autocorr 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core08_autocorr_126d_accel_v109_signal(closeadj, volume):
    base = _autocorr((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel autocorr 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core09_autocorr_252d_accel_v110_signal(closeadj, volume):
    base = _autocorr((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core00 accel snr 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core00_snr_21d_accel_v111_signal(closeadj, volume):
    base = _safe_div(_diff((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), max(1, 21//3)).abs(), _std(_diff((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0),1), 21)+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel snr 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core01_snr_63d_accel_v112_signal(closeadj, volume):
    base = _safe_div(_diff((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), max(1, 63//3)).abs(), _std(_diff((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0),1), 63)+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel snr 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core02_snr_126d_accel_v113_signal(closeadj, volume):
    base = _safe_div(_diff(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), max(1, 126//3)).abs(), _std(_diff(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()),1), 126)+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel snr 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core03_snr_252d_accel_v114_signal(closeadj, volume):
    base = _safe_div(_diff((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), max(1, 252//3)).abs(), _std(_diff((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)),1), 252)+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel snr 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core04_snr_5d_accel_v115_signal(closeadj, volume):
    base = _safe_div(_diff((_min(closeadj,252)), max(1, 5//3)).abs(), _std(_diff((_min(closeadj,252)),1), 5)+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core05 accel snr 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core05_snr_21d_accel_v116_signal(closeadj, volume):
    base = _safe_div(_diff((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), max(1, 21//3)).abs(), _std(_diff((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)),1), 21)+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel snr 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core06_snr_63d_accel_v117_signal(closeadj, volume):
    base = _safe_div(_diff((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), max(1, 63//3)).abs(), _std(_diff((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)),1), 63)+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel snr 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core07_snr_126d_accel_v118_signal(closeadj, volume):
    base = _safe_div(_diff((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), max(1, 126//3)).abs(), _std(_diff((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)),1), 126)+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel snr 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core08_snr_252d_accel_v119_signal(closeadj, volume):
    base = _safe_div(_diff((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), max(1, 252//3)).abs(), _std(_diff((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()),1), 252)+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel snr 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core09_snr_5d_accel_v120_signal(closeadj, volume):
    base = _safe_div(_diff((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), max(1, 5//3)).abs(), _std(_diff((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)),1), 5)+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core00 accel ema_gap 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core00_ema_gap_63d_accel_v121_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 63) - _ewm((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel ema_gap 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core01_ema_gap_126d_accel_v122_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 126) - _ewm((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel ema_gap 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core02_ema_gap_252d_accel_v123_signal(closeadj, volume):
    base = _mean(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 252) - _ewm(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel ema_gap 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core03_ema_gap_5d_accel_v124_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 5) - _ewm((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel ema_gap 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core04_ema_gap_21d_accel_v125_signal(closeadj, volume):
    base = _mean((_min(closeadj,252)), 21) - _ewm((_min(closeadj,252)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core05 accel ema_gap 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core05_ema_gap_63d_accel_v126_signal(closeadj, volume):
    base = _mean((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), 63) - _ewm((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core06 accel ema_gap 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core06_ema_gap_126d_accel_v127_signal(closeadj, volume):
    base = _mean((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), 126) - _ewm((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core07 accel ema_gap 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core07_ema_gap_252d_accel_v128_signal(closeadj, volume):
    base = _mean((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), 252) - _ewm((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core08 accel ema_gap 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core08_ema_gap_5d_accel_v129_signal(closeadj, volume):
    base = _mean((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 5) - _ewm((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core09 accel ema_gap 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core09_ema_gap_21d_accel_v130_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 21) - _ewm((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core00 accel vol_ratio 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core00_vol_ratio_126d_accel_v131_signal(closeadj, volume):
    base = _safe_div(_std((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), max(2, 126//3)), _std((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 126).abs()+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core01 accel vol_ratio 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core01_vol_ratio_252d_accel_v132_signal(closeadj, volume):
    base = _safe_div(_std((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), max(2, 252//3)), _std((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 252).abs()+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core02 accel vol_ratio 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core02_vol_ratio_5d_accel_v133_signal(closeadj, volume):
    base = _safe_div(_std(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), max(2, 5//3)), _std(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 5).abs()+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core03 accel vol_ratio 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core03_vol_ratio_21d_accel_v134_signal(closeadj, volume):
    base = _safe_div(_std((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), max(2, 21//3)), _std((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 21).abs()+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core04 accel vol_ratio 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core04_vol_ratio_63d_accel_v135_signal(closeadj, volume):
    base = _safe_div(_std((_min(closeadj,252)), max(2, 63//3)), _std((_min(closeadj,252)), 63).abs()+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core05 accel vol_ratio 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core05_vol_ratio_126d_accel_v136_signal(closeadj, volume):
    base = _safe_div(_std((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), max(2, 126//3)), _std((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), 126).abs()+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel vol_ratio 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core06_vol_ratio_252d_accel_v137_signal(closeadj, volume):
    base = _safe_div(_std((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), max(2, 252//3)), _std((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), 252).abs()+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel vol_ratio 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core07_vol_ratio_5d_accel_v138_signal(closeadj, volume):
    base = _safe_div(_std((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), max(2, 5//3)), _std((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), 5).abs()+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel vol_ratio 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core08_vol_ratio_21d_accel_v139_signal(closeadj, volume):
    base = _safe_div(_std((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), max(2, 21//3)), _std((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 21).abs()+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel vol_ratio 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core09_vol_ratio_63d_accel_v140_signal(closeadj, volume):
    base = _safe_div(_std((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), max(2, 63//3)), _std((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 63).abs()+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core00 accel recent_vs_long 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core00_recent_vs_long_252d_accel_v141_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), max(2, 252//3)) - _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel recent_vs_long 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core01_recent_vs_long_5d_accel_v142_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), max(2, 5//3)) - _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel recent_vs_long 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core02_recent_vs_long_21d_accel_v143_signal(closeadj, volume):
    base = _mean(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), max(2, 21//3)) - _mean(((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel recent_vs_long 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core03_recent_vs_long_63d_accel_v144_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), max(2, 63//3)) - _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel recent_vs_long 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core04_recent_vs_long_126d_accel_v145_signal(closeadj, volume):
    base = _mean((_min(closeadj,252)), max(2, 126//3)) - _mean((_min(closeadj,252)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core05 accel recent_vs_long 252d
def cg_f09_technology_f09_technology_drawdown_resilience_core05_recent_vs_long_252d_accel_v146_signal(closeadj, volume):
    base = _mean((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), max(2, 252//3)) - _mean((_std(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0,21)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel recent_vs_long 5d
def cg_f09_technology_f09_technology_drawdown_resilience_core06_recent_vs_long_5d_accel_v147_signal(closeadj, volume):
    base = _mean((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), max(2, 5//3)) - _mean((_z(volume, 63)-_z((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs(),63)), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel recent_vs_long 21d
def cg_f09_technology_f09_technology_drawdown_resilience_core07_recent_vs_long_21d_accel_v148_signal(closeadj, volume):
    base = _mean((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), max(2, 21//3)) - _mean((((closeadj<_max(closeadj,252)*0.9)&(_pct_change(closeadj, 21)<0)).astype(float)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel recent_vs_long 63d
def cg_f09_technology_f09_technology_drawdown_resilience_core08_recent_vs_long_63d_accel_v149_signal(closeadj, volume):
    base = _mean((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), max(2, 63//3)) - _mean((_pct_change(closeadj, 63)-(_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)-1.0).abs()), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel recent_vs_long 126d
def cg_f09_technology_f09_technology_drawdown_resilience_core09_recent_vs_long_126d_accel_v150_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), max(2, 126//3)) - _mean((_safe_div(closeadj, _max(closeadj,252).abs()+1e-9)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

