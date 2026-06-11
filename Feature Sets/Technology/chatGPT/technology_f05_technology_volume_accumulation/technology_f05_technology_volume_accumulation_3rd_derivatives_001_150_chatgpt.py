import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 accel mean 5d
def cg_f05_technology_f05_technology_volume_accumulation_core00_mean_5d_accel_v001_signal(volume, closeadj):
    base = _mean((volume), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel mean 21d
def cg_f05_technology_f05_technology_volume_accumulation_core01_mean_21d_accel_v002_signal(volume, closeadj):
    base = _mean((_safe_div(volume, _mean(volume,21)+1e-9)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel mean 63d
def cg_f05_technology_f05_technology_volume_accumulation_core02_mean_63d_accel_v003_signal(volume, closeadj):
    base = _mean((_safe_div(volume, _mean(volume,63)+1e-9)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel mean 126d
def cg_f05_technology_f05_technology_volume_accumulation_core03_mean_126d_accel_v004_signal(volume, closeadj):
    base = _mean((volume.where(_diff(closeadj, 1)>0,0)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel mean 252d
def cg_f05_technology_f05_technology_volume_accumulation_core04_mean_252d_accel_v005_signal(volume, closeadj):
    base = _mean((volume.where(_diff(closeadj, 1)<0,0)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core05 accel mean 5d
def cg_f05_technology_f05_technology_volume_accumulation_core05_mean_5d_accel_v006_signal(volume, closeadj):
    base = _mean((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core06 accel mean 21d
def cg_f05_technology_f05_technology_volume_accumulation_core06_mean_21d_accel_v007_signal(volume, closeadj):
    base = _mean((_pct_change(volume, 1)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core07 accel mean 63d
def cg_f05_technology_f05_technology_volume_accumulation_core07_mean_63d_accel_v008_signal(volume, closeadj):
    base = _mean((_log((closeadj*volume).abs()+1)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core08 accel mean 126d
def cg_f05_technology_f05_technology_volume_accumulation_core08_mean_126d_accel_v009_signal(volume, closeadj):
    base = _mean(((volume>_mean(volume,21)).astype(float)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core09 accel mean 252d
def cg_f05_technology_f05_technology_volume_accumulation_core09_mean_252d_accel_v010_signal(volume, closeadj):
    base = _mean((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core00 accel z 21d
def cg_f05_technology_f05_technology_volume_accumulation_core00_z_21d_accel_v011_signal(volume, closeadj):
    base = _z((volume), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core01 accel z 63d
def cg_f05_technology_f05_technology_volume_accumulation_core01_z_63d_accel_v012_signal(volume, closeadj):
    base = _z((_safe_div(volume, _mean(volume,21)+1e-9)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core02 accel z 126d
def cg_f05_technology_f05_technology_volume_accumulation_core02_z_126d_accel_v013_signal(volume, closeadj):
    base = _z((_safe_div(volume, _mean(volume,63)+1e-9)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core03 accel z 252d
def cg_f05_technology_f05_technology_volume_accumulation_core03_z_252d_accel_v014_signal(volume, closeadj):
    base = _z((volume.where(_diff(closeadj, 1)>0,0)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core04 accel z 5d
def cg_f05_technology_f05_technology_volume_accumulation_core04_z_5d_accel_v015_signal(volume, closeadj):
    base = _z((volume.where(_diff(closeadj, 1)<0,0)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core05 accel z 21d
def cg_f05_technology_f05_technology_volume_accumulation_core05_z_21d_accel_v016_signal(volume, closeadj):
    base = _z((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel z 63d
def cg_f05_technology_f05_technology_volume_accumulation_core06_z_63d_accel_v017_signal(volume, closeadj):
    base = _z((_pct_change(volume, 1)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel z 126d
def cg_f05_technology_f05_technology_volume_accumulation_core07_z_126d_accel_v018_signal(volume, closeadj):
    base = _z((_log((closeadj*volume).abs()+1)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel z 252d
def cg_f05_technology_f05_technology_volume_accumulation_core08_z_252d_accel_v019_signal(volume, closeadj):
    base = _z(((volume>_mean(volume,21)).astype(float)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel z 5d
def cg_f05_technology_f05_technology_volume_accumulation_core09_z_5d_accel_v020_signal(volume, closeadj):
    base = _z((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core00 accel rank 63d
def cg_f05_technology_f05_technology_volume_accumulation_core00_rank_63d_accel_v021_signal(volume, closeadj):
    base = _rank((volume), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel rank 126d
def cg_f05_technology_f05_technology_volume_accumulation_core01_rank_126d_accel_v022_signal(volume, closeadj):
    base = _rank((_safe_div(volume, _mean(volume,21)+1e-9)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel rank 252d
def cg_f05_technology_f05_technology_volume_accumulation_core02_rank_252d_accel_v023_signal(volume, closeadj):
    base = _rank((_safe_div(volume, _mean(volume,63)+1e-9)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel rank 5d
def cg_f05_technology_f05_technology_volume_accumulation_core03_rank_5d_accel_v024_signal(volume, closeadj):
    base = _rank((volume.where(_diff(closeadj, 1)>0,0)), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel rank 21d
def cg_f05_technology_f05_technology_volume_accumulation_core04_rank_21d_accel_v025_signal(volume, closeadj):
    base = _rank((volume.where(_diff(closeadj, 1)<0,0)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core05 accel rank 63d
def cg_f05_technology_f05_technology_volume_accumulation_core05_rank_63d_accel_v026_signal(volume, closeadj):
    base = _rank((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel rank 126d
def cg_f05_technology_f05_technology_volume_accumulation_core06_rank_126d_accel_v027_signal(volume, closeadj):
    base = _rank((_pct_change(volume, 1)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel rank 252d
def cg_f05_technology_f05_technology_volume_accumulation_core07_rank_252d_accel_v028_signal(volume, closeadj):
    base = _rank((_log((closeadj*volume).abs()+1)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel rank 5d
def cg_f05_technology_f05_technology_volume_accumulation_core08_rank_5d_accel_v029_signal(volume, closeadj):
    base = _rank(((volume>_mean(volume,21)).astype(float)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel rank 21d
def cg_f05_technology_f05_technology_volume_accumulation_core09_rank_21d_accel_v030_signal(volume, closeadj):
    base = _rank((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core00 accel std 126d
def cg_f05_technology_f05_technology_volume_accumulation_core00_std_126d_accel_v031_signal(volume, closeadj):
    base = _std((volume), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel std 252d
def cg_f05_technology_f05_technology_volume_accumulation_core01_std_252d_accel_v032_signal(volume, closeadj):
    base = _std((_safe_div(volume, _mean(volume,21)+1e-9)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel std 5d
def cg_f05_technology_f05_technology_volume_accumulation_core02_std_5d_accel_v033_signal(volume, closeadj):
    base = _std((_safe_div(volume, _mean(volume,63)+1e-9)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel std 21d
def cg_f05_technology_f05_technology_volume_accumulation_core03_std_21d_accel_v034_signal(volume, closeadj):
    base = _std((volume.where(_diff(closeadj, 1)>0,0)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel std 63d
def cg_f05_technology_f05_technology_volume_accumulation_core04_std_63d_accel_v035_signal(volume, closeadj):
    base = _std((volume.where(_diff(closeadj, 1)<0,0)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core05 accel std 126d
def cg_f05_technology_f05_technology_volume_accumulation_core05_std_126d_accel_v036_signal(volume, closeadj):
    base = _std((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core06 accel std 252d
def cg_f05_technology_f05_technology_volume_accumulation_core06_std_252d_accel_v037_signal(volume, closeadj):
    base = _std((_pct_change(volume, 1)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core07 accel std 5d
def cg_f05_technology_f05_technology_volume_accumulation_core07_std_5d_accel_v038_signal(volume, closeadj):
    base = _std((_log((closeadj*volume).abs()+1)), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core08 accel std 21d
def cg_f05_technology_f05_technology_volume_accumulation_core08_std_21d_accel_v039_signal(volume, closeadj):
    base = _std(((volume>_mean(volume,21)).astype(float)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core09 accel std 63d
def cg_f05_technology_f05_technology_volume_accumulation_core09_std_63d_accel_v040_signal(volume, closeadj):
    base = _std((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core00 accel slope 252d
def cg_f05_technology_f05_technology_volume_accumulation_core00_slope_252d_accel_v041_signal(volume, closeadj):
    base = _slope((volume), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core01 accel slope 5d
def cg_f05_technology_f05_technology_volume_accumulation_core01_slope_5d_accel_v042_signal(volume, closeadj):
    base = _slope((_safe_div(volume, _mean(volume,21)+1e-9)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core02 accel slope 21d
def cg_f05_technology_f05_technology_volume_accumulation_core02_slope_21d_accel_v043_signal(volume, closeadj):
    base = _slope((_safe_div(volume, _mean(volume,63)+1e-9)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core03 accel slope 63d
def cg_f05_technology_f05_technology_volume_accumulation_core03_slope_63d_accel_v044_signal(volume, closeadj):
    base = _slope((volume.where(_diff(closeadj, 1)>0,0)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core04 accel slope 126d
def cg_f05_technology_f05_technology_volume_accumulation_core04_slope_126d_accel_v045_signal(volume, closeadj):
    base = _slope((volume.where(_diff(closeadj, 1)<0,0)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core05 accel slope 252d
def cg_f05_technology_f05_technology_volume_accumulation_core05_slope_252d_accel_v046_signal(volume, closeadj):
    base = _slope((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel slope 5d
def cg_f05_technology_f05_technology_volume_accumulation_core06_slope_5d_accel_v047_signal(volume, closeadj):
    base = _slope((_pct_change(volume, 1)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel slope 21d
def cg_f05_technology_f05_technology_volume_accumulation_core07_slope_21d_accel_v048_signal(volume, closeadj):
    base = _slope((_log((closeadj*volume).abs()+1)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel slope 63d
def cg_f05_technology_f05_technology_volume_accumulation_core08_slope_63d_accel_v049_signal(volume, closeadj):
    base = _slope(((volume>_mean(volume,21)).astype(float)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel slope 126d
def cg_f05_technology_f05_technology_volume_accumulation_core09_slope_126d_accel_v050_signal(volume, closeadj):
    base = _slope((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core00 accel diff 5d
def cg_f05_technology_f05_technology_volume_accumulation_core00_diff_5d_accel_v051_signal(volume, closeadj):
    base = _diff((volume), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel diff 21d
def cg_f05_technology_f05_technology_volume_accumulation_core01_diff_21d_accel_v052_signal(volume, closeadj):
    base = _diff((_safe_div(volume, _mean(volume,21)+1e-9)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel diff 63d
def cg_f05_technology_f05_technology_volume_accumulation_core02_diff_63d_accel_v053_signal(volume, closeadj):
    base = _diff((_safe_div(volume, _mean(volume,63)+1e-9)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel diff 126d
def cg_f05_technology_f05_technology_volume_accumulation_core03_diff_126d_accel_v054_signal(volume, closeadj):
    base = _diff((volume.where(_diff(closeadj, 1)>0,0)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel diff 252d
def cg_f05_technology_f05_technology_volume_accumulation_core04_diff_252d_accel_v055_signal(volume, closeadj):
    base = _diff((volume.where(_diff(closeadj, 1)<0,0)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core05 accel diff 5d
def cg_f05_technology_f05_technology_volume_accumulation_core05_diff_5d_accel_v056_signal(volume, closeadj):
    base = _diff((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel diff 21d
def cg_f05_technology_f05_technology_volume_accumulation_core06_diff_21d_accel_v057_signal(volume, closeadj):
    base = _diff((_pct_change(volume, 1)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel diff 63d
def cg_f05_technology_f05_technology_volume_accumulation_core07_diff_63d_accel_v058_signal(volume, closeadj):
    base = _diff((_log((closeadj*volume).abs()+1)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel diff 126d
def cg_f05_technology_f05_technology_volume_accumulation_core08_diff_126d_accel_v059_signal(volume, closeadj):
    base = _diff(((volume>_mean(volume,21)).astype(float)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel diff 252d
def cg_f05_technology_f05_technology_volume_accumulation_core09_diff_252d_accel_v060_signal(volume, closeadj):
    base = _diff((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core00 accel pct 21d
def cg_f05_technology_f05_technology_volume_accumulation_core00_pct_21d_accel_v061_signal(volume, closeadj):
    base = _pct_change(((volume).abs()+1.0), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel pct 63d
def cg_f05_technology_f05_technology_volume_accumulation_core01_pct_63d_accel_v062_signal(volume, closeadj):
    base = _pct_change(((_safe_div(volume, _mean(volume,21)+1e-9)).abs()+1.0), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel pct 126d
def cg_f05_technology_f05_technology_volume_accumulation_core02_pct_126d_accel_v063_signal(volume, closeadj):
    base = _pct_change(((_safe_div(volume, _mean(volume,63)+1e-9)).abs()+1.0), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel pct 252d
def cg_f05_technology_f05_technology_volume_accumulation_core03_pct_252d_accel_v064_signal(volume, closeadj):
    base = _pct_change(((volume.where(_diff(closeadj, 1)>0,0)).abs()+1.0), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel pct 5d
def cg_f05_technology_f05_technology_volume_accumulation_core04_pct_5d_accel_v065_signal(volume, closeadj):
    base = _pct_change(((volume.where(_diff(closeadj, 1)<0,0)).abs()+1.0), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core05 accel pct 21d
def cg_f05_technology_f05_technology_volume_accumulation_core05_pct_21d_accel_v066_signal(volume, closeadj):
    base = _pct_change(((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)).abs()+1.0), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core06 accel pct 63d
def cg_f05_technology_f05_technology_volume_accumulation_core06_pct_63d_accel_v067_signal(volume, closeadj):
    base = _pct_change(((_pct_change(volume, 1)).abs()+1.0), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core07 accel pct 126d
def cg_f05_technology_f05_technology_volume_accumulation_core07_pct_126d_accel_v068_signal(volume, closeadj):
    base = _pct_change(((_log((closeadj*volume).abs()+1)).abs()+1.0), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core08 accel pct 252d
def cg_f05_technology_f05_technology_volume_accumulation_core08_pct_252d_accel_v069_signal(volume, closeadj):
    base = _pct_change((((volume>_mean(volume,21)).astype(float)).abs()+1.0), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core09 accel pct 5d
def cg_f05_technology_f05_technology_volume_accumulation_core09_pct_5d_accel_v070_signal(volume, closeadj):
    base = _pct_change(((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)).abs()+1.0), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core00 accel ewm 63d
def cg_f05_technology_f05_technology_volume_accumulation_core00_ewm_63d_accel_v071_signal(volume, closeadj):
    base = _ewm((volume), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core01 accel ewm 126d
def cg_f05_technology_f05_technology_volume_accumulation_core01_ewm_126d_accel_v072_signal(volume, closeadj):
    base = _ewm((_safe_div(volume, _mean(volume,21)+1e-9)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core02 accel ewm 252d
def cg_f05_technology_f05_technology_volume_accumulation_core02_ewm_252d_accel_v073_signal(volume, closeadj):
    base = _ewm((_safe_div(volume, _mean(volume,63)+1e-9)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core03 accel ewm 5d
def cg_f05_technology_f05_technology_volume_accumulation_core03_ewm_5d_accel_v074_signal(volume, closeadj):
    base = _ewm((volume.where(_diff(closeadj, 1)>0,0)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core04 accel ewm 21d
def cg_f05_technology_f05_technology_volume_accumulation_core04_ewm_21d_accel_v075_signal(volume, closeadj):
    base = _ewm((volume.where(_diff(closeadj, 1)<0,0)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core05 accel ewm 63d
def cg_f05_technology_f05_technology_volume_accumulation_core05_ewm_63d_accel_v076_signal(volume, closeadj):
    base = _ewm((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel ewm 126d
def cg_f05_technology_f05_technology_volume_accumulation_core06_ewm_126d_accel_v077_signal(volume, closeadj):
    base = _ewm((_pct_change(volume, 1)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel ewm 252d
def cg_f05_technology_f05_technology_volume_accumulation_core07_ewm_252d_accel_v078_signal(volume, closeadj):
    base = _ewm((_log((closeadj*volume).abs()+1)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel ewm 5d
def cg_f05_technology_f05_technology_volume_accumulation_core08_ewm_5d_accel_v079_signal(volume, closeadj):
    base = _ewm(((volume>_mean(volume,21)).astype(float)), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel ewm 21d
def cg_f05_technology_f05_technology_volume_accumulation_core09_ewm_21d_accel_v080_signal(volume, closeadj):
    base = _ewm((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core00 accel skew 126d
def cg_f05_technology_f05_technology_volume_accumulation_core00_skew_126d_accel_v081_signal(volume, closeadj):
    base = _skew((volume), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel skew 252d
def cg_f05_technology_f05_technology_volume_accumulation_core01_skew_252d_accel_v082_signal(volume, closeadj):
    base = _skew((_safe_div(volume, _mean(volume,21)+1e-9)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel skew 5d
def cg_f05_technology_f05_technology_volume_accumulation_core02_skew_5d_accel_v083_signal(volume, closeadj):
    base = _skew((_safe_div(volume, _mean(volume,63)+1e-9)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel skew 21d
def cg_f05_technology_f05_technology_volume_accumulation_core03_skew_21d_accel_v084_signal(volume, closeadj):
    base = _skew((volume.where(_diff(closeadj, 1)>0,0)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel skew 63d
def cg_f05_technology_f05_technology_volume_accumulation_core04_skew_63d_accel_v085_signal(volume, closeadj):
    base = _skew((volume.where(_diff(closeadj, 1)<0,0)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core05 accel skew 126d
def cg_f05_technology_f05_technology_volume_accumulation_core05_skew_126d_accel_v086_signal(volume, closeadj):
    base = _skew((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel skew 252d
def cg_f05_technology_f05_technology_volume_accumulation_core06_skew_252d_accel_v087_signal(volume, closeadj):
    base = _skew((_pct_change(volume, 1)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel skew 5d
def cg_f05_technology_f05_technology_volume_accumulation_core07_skew_5d_accel_v088_signal(volume, closeadj):
    base = _skew((_log((closeadj*volume).abs()+1)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel skew 21d
def cg_f05_technology_f05_technology_volume_accumulation_core08_skew_21d_accel_v089_signal(volume, closeadj):
    base = _skew(((volume>_mean(volume,21)).astype(float)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel skew 63d
def cg_f05_technology_f05_technology_volume_accumulation_core09_skew_63d_accel_v090_signal(volume, closeadj):
    base = _skew((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core00 accel kurt 252d
def cg_f05_technology_f05_technology_volume_accumulation_core00_kurt_252d_accel_v091_signal(volume, closeadj):
    base = _kurt((volume), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel kurt 5d
def cg_f05_technology_f05_technology_volume_accumulation_core01_kurt_5d_accel_v092_signal(volume, closeadj):
    base = _kurt((_safe_div(volume, _mean(volume,21)+1e-9)), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel kurt 21d
def cg_f05_technology_f05_technology_volume_accumulation_core02_kurt_21d_accel_v093_signal(volume, closeadj):
    base = _kurt((_safe_div(volume, _mean(volume,63)+1e-9)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel kurt 63d
def cg_f05_technology_f05_technology_volume_accumulation_core03_kurt_63d_accel_v094_signal(volume, closeadj):
    base = _kurt((volume.where(_diff(closeadj, 1)>0,0)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel kurt 126d
def cg_f05_technology_f05_technology_volume_accumulation_core04_kurt_126d_accel_v095_signal(volume, closeadj):
    base = _kurt((volume.where(_diff(closeadj, 1)<0,0)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core05 accel kurt 252d
def cg_f05_technology_f05_technology_volume_accumulation_core05_kurt_252d_accel_v096_signal(volume, closeadj):
    base = _kurt((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core06 accel kurt 5d
def cg_f05_technology_f05_technology_volume_accumulation_core06_kurt_5d_accel_v097_signal(volume, closeadj):
    base = _kurt((_pct_change(volume, 1)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core07 accel kurt 21d
def cg_f05_technology_f05_technology_volume_accumulation_core07_kurt_21d_accel_v098_signal(volume, closeadj):
    base = _kurt((_log((closeadj*volume).abs()+1)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core08 accel kurt 63d
def cg_f05_technology_f05_technology_volume_accumulation_core08_kurt_63d_accel_v099_signal(volume, closeadj):
    base = _kurt(((volume>_mean(volume,21)).astype(float)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core09 accel kurt 126d
def cg_f05_technology_f05_technology_volume_accumulation_core09_kurt_126d_accel_v100_signal(volume, closeadj):
    base = _kurt((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core00 accel autocorr 5d
def cg_f05_technology_f05_technology_volume_accumulation_core00_autocorr_5d_accel_v101_signal(volume, closeadj):
    base = _autocorr((volume), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core01 accel autocorr 21d
def cg_f05_technology_f05_technology_volume_accumulation_core01_autocorr_21d_accel_v102_signal(volume, closeadj):
    base = _autocorr((_safe_div(volume, _mean(volume,21)+1e-9)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core02 accel autocorr 63d
def cg_f05_technology_f05_technology_volume_accumulation_core02_autocorr_63d_accel_v103_signal(volume, closeadj):
    base = _autocorr((_safe_div(volume, _mean(volume,63)+1e-9)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core03 accel autocorr 126d
def cg_f05_technology_f05_technology_volume_accumulation_core03_autocorr_126d_accel_v104_signal(volume, closeadj):
    base = _autocorr((volume.where(_diff(closeadj, 1)>0,0)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core04 accel autocorr 252d
def cg_f05_technology_f05_technology_volume_accumulation_core04_autocorr_252d_accel_v105_signal(volume, closeadj):
    base = _autocorr((volume.where(_diff(closeadj, 1)<0,0)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core05 accel autocorr 5d
def cg_f05_technology_f05_technology_volume_accumulation_core05_autocorr_5d_accel_v106_signal(volume, closeadj):
    base = _autocorr((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel autocorr 21d
def cg_f05_technology_f05_technology_volume_accumulation_core06_autocorr_21d_accel_v107_signal(volume, closeadj):
    base = _autocorr((_pct_change(volume, 1)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel autocorr 63d
def cg_f05_technology_f05_technology_volume_accumulation_core07_autocorr_63d_accel_v108_signal(volume, closeadj):
    base = _autocorr((_log((closeadj*volume).abs()+1)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel autocorr 126d
def cg_f05_technology_f05_technology_volume_accumulation_core08_autocorr_126d_accel_v109_signal(volume, closeadj):
    base = _autocorr(((volume>_mean(volume,21)).astype(float)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel autocorr 252d
def cg_f05_technology_f05_technology_volume_accumulation_core09_autocorr_252d_accel_v110_signal(volume, closeadj):
    base = _autocorr((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core00 accel snr 21d
def cg_f05_technology_f05_technology_volume_accumulation_core00_snr_21d_accel_v111_signal(volume, closeadj):
    base = _safe_div(_diff((volume), max(1, 21//3)).abs(), _std(_diff((volume),1), 21)+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel snr 63d
def cg_f05_technology_f05_technology_volume_accumulation_core01_snr_63d_accel_v112_signal(volume, closeadj):
    base = _safe_div(_diff((_safe_div(volume, _mean(volume,21)+1e-9)), max(1, 63//3)).abs(), _std(_diff((_safe_div(volume, _mean(volume,21)+1e-9)),1), 63)+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel snr 126d
def cg_f05_technology_f05_technology_volume_accumulation_core02_snr_126d_accel_v113_signal(volume, closeadj):
    base = _safe_div(_diff((_safe_div(volume, _mean(volume,63)+1e-9)), max(1, 126//3)).abs(), _std(_diff((_safe_div(volume, _mean(volume,63)+1e-9)),1), 126)+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel snr 252d
def cg_f05_technology_f05_technology_volume_accumulation_core03_snr_252d_accel_v114_signal(volume, closeadj):
    base = _safe_div(_diff((volume.where(_diff(closeadj, 1)>0,0)), max(1, 252//3)).abs(), _std(_diff((volume.where(_diff(closeadj, 1)>0,0)),1), 252)+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel snr 5d
def cg_f05_technology_f05_technology_volume_accumulation_core04_snr_5d_accel_v115_signal(volume, closeadj):
    base = _safe_div(_diff((volume.where(_diff(closeadj, 1)<0,0)), max(1, 5//3)).abs(), _std(_diff((volume.where(_diff(closeadj, 1)<0,0)),1), 5)+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core05 accel snr 21d
def cg_f05_technology_f05_technology_volume_accumulation_core05_snr_21d_accel_v116_signal(volume, closeadj):
    base = _safe_div(_diff((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), max(1, 21//3)).abs(), _std(_diff((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)),1), 21)+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel snr 63d
def cg_f05_technology_f05_technology_volume_accumulation_core06_snr_63d_accel_v117_signal(volume, closeadj):
    base = _safe_div(_diff((_pct_change(volume, 1)), max(1, 63//3)).abs(), _std(_diff((_pct_change(volume, 1)),1), 63)+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel snr 126d
def cg_f05_technology_f05_technology_volume_accumulation_core07_snr_126d_accel_v118_signal(volume, closeadj):
    base = _safe_div(_diff((_log((closeadj*volume).abs()+1)), max(1, 126//3)).abs(), _std(_diff((_log((closeadj*volume).abs()+1)),1), 126)+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel snr 252d
def cg_f05_technology_f05_technology_volume_accumulation_core08_snr_252d_accel_v119_signal(volume, closeadj):
    base = _safe_div(_diff(((volume>_mean(volume,21)).astype(float)), max(1, 252//3)).abs(), _std(_diff(((volume>_mean(volume,21)).astype(float)),1), 252)+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel snr 5d
def cg_f05_technology_f05_technology_volume_accumulation_core09_snr_5d_accel_v120_signal(volume, closeadj):
    base = _safe_div(_diff((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), max(1, 5//3)).abs(), _std(_diff((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)),1), 5)+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core00 accel ema_gap 63d
def cg_f05_technology_f05_technology_volume_accumulation_core00_ema_gap_63d_accel_v121_signal(volume, closeadj):
    base = _mean((volume), 63) - _ewm((volume), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel ema_gap 126d
def cg_f05_technology_f05_technology_volume_accumulation_core01_ema_gap_126d_accel_v122_signal(volume, closeadj):
    base = _mean((_safe_div(volume, _mean(volume,21)+1e-9)), 126) - _ewm((_safe_div(volume, _mean(volume,21)+1e-9)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel ema_gap 252d
def cg_f05_technology_f05_technology_volume_accumulation_core02_ema_gap_252d_accel_v123_signal(volume, closeadj):
    base = _mean((_safe_div(volume, _mean(volume,63)+1e-9)), 252) - _ewm((_safe_div(volume, _mean(volume,63)+1e-9)), 252)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel ema_gap 5d
def cg_f05_technology_f05_technology_volume_accumulation_core03_ema_gap_5d_accel_v124_signal(volume, closeadj):
    base = _mean((volume.where(_diff(closeadj, 1)>0,0)), 5) - _ewm((volume.where(_diff(closeadj, 1)>0,0)), 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel ema_gap 21d
def cg_f05_technology_f05_technology_volume_accumulation_core04_ema_gap_21d_accel_v125_signal(volume, closeadj):
    base = _mean((volume.where(_diff(closeadj, 1)<0,0)), 21) - _ewm((volume.where(_diff(closeadj, 1)<0,0)), 21)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core05 accel ema_gap 63d
def cg_f05_technology_f05_technology_volume_accumulation_core05_ema_gap_63d_accel_v126_signal(volume, closeadj):
    base = _mean((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 63) - _ewm((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 63)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core06 accel ema_gap 126d
def cg_f05_technology_f05_technology_volume_accumulation_core06_ema_gap_126d_accel_v127_signal(volume, closeadj):
    base = _mean((_pct_change(volume, 1)), 126) - _ewm((_pct_change(volume, 1)), 126)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core07 accel ema_gap 252d
def cg_f05_technology_f05_technology_volume_accumulation_core07_ema_gap_252d_accel_v128_signal(volume, closeadj):
    base = _mean((_log((closeadj*volume).abs()+1)), 252) - _ewm((_log((closeadj*volume).abs()+1)), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core08 accel ema_gap 5d
def cg_f05_technology_f05_technology_volume_accumulation_core08_ema_gap_5d_accel_v129_signal(volume, closeadj):
    base = _mean(((volume>_mean(volume,21)).astype(float)), 5) - _ewm(((volume>_mean(volume,21)).astype(float)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core09 accel ema_gap 21d
def cg_f05_technology_f05_technology_volume_accumulation_core09_ema_gap_21d_accel_v130_signal(volume, closeadj):
    base = _mean((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 21) - _ewm((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core00 accel vol_ratio 126d
def cg_f05_technology_f05_technology_volume_accumulation_core00_vol_ratio_126d_accel_v131_signal(volume, closeadj):
    base = _safe_div(_std((volume), max(2, 126//3)), _std((volume), 126).abs()+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core01 accel vol_ratio 252d
def cg_f05_technology_f05_technology_volume_accumulation_core01_vol_ratio_252d_accel_v132_signal(volume, closeadj):
    base = _safe_div(_std((_safe_div(volume, _mean(volume,21)+1e-9)), max(2, 252//3)), _std((_safe_div(volume, _mean(volume,21)+1e-9)), 252).abs()+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core02 accel vol_ratio 5d
def cg_f05_technology_f05_technology_volume_accumulation_core02_vol_ratio_5d_accel_v133_signal(volume, closeadj):
    base = _safe_div(_std((_safe_div(volume, _mean(volume,63)+1e-9)), max(2, 5//3)), _std((_safe_div(volume, _mean(volume,63)+1e-9)), 5).abs()+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core03 accel vol_ratio 21d
def cg_f05_technology_f05_technology_volume_accumulation_core03_vol_ratio_21d_accel_v134_signal(volume, closeadj):
    base = _safe_div(_std((volume.where(_diff(closeadj, 1)>0,0)), max(2, 21//3)), _std((volume.where(_diff(closeadj, 1)>0,0)), 21).abs()+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core04 accel vol_ratio 63d
def cg_f05_technology_f05_technology_volume_accumulation_core04_vol_ratio_63d_accel_v135_signal(volume, closeadj):
    base = _safe_div(_std((volume.where(_diff(closeadj, 1)<0,0)), max(2, 63//3)), _std((volume.where(_diff(closeadj, 1)<0,0)), 63).abs()+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core05 accel vol_ratio 126d
def cg_f05_technology_f05_technology_volume_accumulation_core05_vol_ratio_126d_accel_v136_signal(volume, closeadj):
    base = _safe_div(_std((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), max(2, 126//3)), _std((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 126).abs()+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel vol_ratio 252d
def cg_f05_technology_f05_technology_volume_accumulation_core06_vol_ratio_252d_accel_v137_signal(volume, closeadj):
    base = _safe_div(_std((_pct_change(volume, 1)), max(2, 252//3)), _std((_pct_change(volume, 1)), 252).abs()+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel vol_ratio 5d
def cg_f05_technology_f05_technology_volume_accumulation_core07_vol_ratio_5d_accel_v138_signal(volume, closeadj):
    base = _safe_div(_std((_log((closeadj*volume).abs()+1)), max(2, 5//3)), _std((_log((closeadj*volume).abs()+1)), 5).abs()+1e-9)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel vol_ratio 21d
def cg_f05_technology_f05_technology_volume_accumulation_core08_vol_ratio_21d_accel_v139_signal(volume, closeadj):
    base = _safe_div(_std(((volume>_mean(volume,21)).astype(float)), max(2, 21//3)), _std(((volume>_mean(volume,21)).astype(float)), 21).abs()+1e-9)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel vol_ratio 63d
def cg_f05_technology_f05_technology_volume_accumulation_core09_vol_ratio_63d_accel_v140_signal(volume, closeadj):
    base = _safe_div(_std((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), max(2, 63//3)), _std((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 63).abs()+1e-9)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core00 accel recent_vs_long 252d
def cg_f05_technology_f05_technology_volume_accumulation_core00_recent_vs_long_252d_accel_v141_signal(volume, closeadj):
    base = _mean((volume), max(2, 252//3)) - _mean((volume), 252)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel recent_vs_long 5d
def cg_f05_technology_f05_technology_volume_accumulation_core01_recent_vs_long_5d_accel_v142_signal(volume, closeadj):
    base = _mean((_safe_div(volume, _mean(volume,21)+1e-9)), max(2, 5//3)) - _mean((_safe_div(volume, _mean(volume,21)+1e-9)), 5)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel recent_vs_long 21d
def cg_f05_technology_f05_technology_volume_accumulation_core02_recent_vs_long_21d_accel_v143_signal(volume, closeadj):
    base = _mean((_safe_div(volume, _mean(volume,63)+1e-9)), max(2, 21//3)) - _mean((_safe_div(volume, _mean(volume,63)+1e-9)), 21)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel recent_vs_long 63d
def cg_f05_technology_f05_technology_volume_accumulation_core03_recent_vs_long_63d_accel_v144_signal(volume, closeadj):
    base = _mean((volume.where(_diff(closeadj, 1)>0,0)), max(2, 63//3)) - _mean((volume.where(_diff(closeadj, 1)>0,0)), 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel recent_vs_long 126d
def cg_f05_technology_f05_technology_volume_accumulation_core04_recent_vs_long_126d_accel_v145_signal(volume, closeadj):
    base = _mean((volume.where(_diff(closeadj, 1)<0,0)), max(2, 126//3)) - _mean((volume.where(_diff(closeadj, 1)<0,0)), 126)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core05 accel recent_vs_long 252d
def cg_f05_technology_f05_technology_volume_accumulation_core05_recent_vs_long_252d_accel_v146_signal(volume, closeadj):
    base = _mean((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), max(2, 252//3)) - _mean((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel recent_vs_long 5d
def cg_f05_technology_f05_technology_volume_accumulation_core06_recent_vs_long_5d_accel_v147_signal(volume, closeadj):
    base = _mean((_pct_change(volume, 1)), max(2, 5//3)) - _mean((_pct_change(volume, 1)), 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel recent_vs_long 21d
def cg_f05_technology_f05_technology_volume_accumulation_core07_recent_vs_long_21d_accel_v148_signal(volume, closeadj):
    base = _mean((_log((closeadj*volume).abs()+1)), max(2, 21//3)) - _mean((_log((closeadj*volume).abs()+1)), 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel recent_vs_long 63d
def cg_f05_technology_f05_technology_volume_accumulation_core08_recent_vs_long_63d_accel_v149_signal(volume, closeadj):
    base = _mean(((volume>_mean(volume,21)).astype(float)), max(2, 63//3)) - _mean(((volume>_mean(volume,21)).astype(float)), 63)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel recent_vs_long 126d
def cg_f05_technology_f05_technology_volume_accumulation_core09_recent_vs_long_126d_accel_v150_signal(volume, closeadj):
    base = _mean((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), max(2, 126//3)) - _mean((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 126)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

