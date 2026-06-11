import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 slope mean 5d
def cg_f05_technology_f05_technology_volume_accumulation_core00_mean_5d_slope_v001_signal(volume, closeadj):
    base = _mean((volume), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f05_technology_f05_technology_volume_accumulation_core01_mean_21d_slope_v002_signal(volume, closeadj):
    base = _mean((_safe_div(volume, _mean(volume,21)+1e-9)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f05_technology_f05_technology_volume_accumulation_core02_mean_63d_slope_v003_signal(volume, closeadj):
    base = _mean((_safe_div(volume, _mean(volume,63)+1e-9)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f05_technology_f05_technology_volume_accumulation_core03_mean_126d_slope_v004_signal(volume, closeadj):
    base = _mean((volume.where(_diff(closeadj, 1)>0,0)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f05_technology_f05_technology_volume_accumulation_core04_mean_252d_slope_v005_signal(volume, closeadj):
    base = _mean((volume.where(_diff(closeadj, 1)<0,0)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f05_technology_f05_technology_volume_accumulation_core05_mean_5d_slope_v006_signal(volume, closeadj):
    base = _mean((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f05_technology_f05_technology_volume_accumulation_core06_mean_21d_slope_v007_signal(volume, closeadj):
    base = _mean((_pct_change(volume, 1)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f05_technology_f05_technology_volume_accumulation_core07_mean_63d_slope_v008_signal(volume, closeadj):
    base = _mean((_log((closeadj*volume).abs()+1)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f05_technology_f05_technology_volume_accumulation_core08_mean_126d_slope_v009_signal(volume, closeadj):
    base = _mean(((volume>_mean(volume,21)).astype(float)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f05_technology_f05_technology_volume_accumulation_core09_mean_252d_slope_v010_signal(volume, closeadj):
    base = _mean((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope z 21d
def cg_f05_technology_f05_technology_volume_accumulation_core00_z_21d_slope_v011_signal(volume, closeadj):
    base = _z((volume), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope z 63d
def cg_f05_technology_f05_technology_volume_accumulation_core01_z_63d_slope_v012_signal(volume, closeadj):
    base = _z((_safe_div(volume, _mean(volume,21)+1e-9)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope z 126d
def cg_f05_technology_f05_technology_volume_accumulation_core02_z_126d_slope_v013_signal(volume, closeadj):
    base = _z((_safe_div(volume, _mean(volume,63)+1e-9)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope z 252d
def cg_f05_technology_f05_technology_volume_accumulation_core03_z_252d_slope_v014_signal(volume, closeadj):
    base = _z((volume.where(_diff(closeadj, 1)>0,0)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope z 5d
def cg_f05_technology_f05_technology_volume_accumulation_core04_z_5d_slope_v015_signal(volume, closeadj):
    base = _z((volume.where(_diff(closeadj, 1)<0,0)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope z 21d
def cg_f05_technology_f05_technology_volume_accumulation_core05_z_21d_slope_v016_signal(volume, closeadj):
    base = _z((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope z 63d
def cg_f05_technology_f05_technology_volume_accumulation_core06_z_63d_slope_v017_signal(volume, closeadj):
    base = _z((_pct_change(volume, 1)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope z 126d
def cg_f05_technology_f05_technology_volume_accumulation_core07_z_126d_slope_v018_signal(volume, closeadj):
    base = _z((_log((closeadj*volume).abs()+1)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope z 252d
def cg_f05_technology_f05_technology_volume_accumulation_core08_z_252d_slope_v019_signal(volume, closeadj):
    base = _z(((volume>_mean(volume,21)).astype(float)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope z 5d
def cg_f05_technology_f05_technology_volume_accumulation_core09_z_5d_slope_v020_signal(volume, closeadj):
    base = _z((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope rank 63d
def cg_f05_technology_f05_technology_volume_accumulation_core00_rank_63d_slope_v021_signal(volume, closeadj):
    base = _rank((volume), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope rank 126d
def cg_f05_technology_f05_technology_volume_accumulation_core01_rank_126d_slope_v022_signal(volume, closeadj):
    base = _rank((_safe_div(volume, _mean(volume,21)+1e-9)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope rank 252d
def cg_f05_technology_f05_technology_volume_accumulation_core02_rank_252d_slope_v023_signal(volume, closeadj):
    base = _rank((_safe_div(volume, _mean(volume,63)+1e-9)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope rank 5d
def cg_f05_technology_f05_technology_volume_accumulation_core03_rank_5d_slope_v024_signal(volume, closeadj):
    base = _rank((volume.where(_diff(closeadj, 1)>0,0)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope rank 21d
def cg_f05_technology_f05_technology_volume_accumulation_core04_rank_21d_slope_v025_signal(volume, closeadj):
    base = _rank((volume.where(_diff(closeadj, 1)<0,0)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope rank 63d
def cg_f05_technology_f05_technology_volume_accumulation_core05_rank_63d_slope_v026_signal(volume, closeadj):
    base = _rank((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope rank 126d
def cg_f05_technology_f05_technology_volume_accumulation_core06_rank_126d_slope_v027_signal(volume, closeadj):
    base = _rank((_pct_change(volume, 1)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope rank 252d
def cg_f05_technology_f05_technology_volume_accumulation_core07_rank_252d_slope_v028_signal(volume, closeadj):
    base = _rank((_log((closeadj*volume).abs()+1)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope rank 5d
def cg_f05_technology_f05_technology_volume_accumulation_core08_rank_5d_slope_v029_signal(volume, closeadj):
    base = _rank(((volume>_mean(volume,21)).astype(float)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope rank 21d
def cg_f05_technology_f05_technology_volume_accumulation_core09_rank_21d_slope_v030_signal(volume, closeadj):
    base = _rank((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope std 126d
def cg_f05_technology_f05_technology_volume_accumulation_core00_std_126d_slope_v031_signal(volume, closeadj):
    base = _std((volume), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope std 252d
def cg_f05_technology_f05_technology_volume_accumulation_core01_std_252d_slope_v032_signal(volume, closeadj):
    base = _std((_safe_div(volume, _mean(volume,21)+1e-9)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope std 5d
def cg_f05_technology_f05_technology_volume_accumulation_core02_std_5d_slope_v033_signal(volume, closeadj):
    base = _std((_safe_div(volume, _mean(volume,63)+1e-9)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope std 21d
def cg_f05_technology_f05_technology_volume_accumulation_core03_std_21d_slope_v034_signal(volume, closeadj):
    base = _std((volume.where(_diff(closeadj, 1)>0,0)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope std 63d
def cg_f05_technology_f05_technology_volume_accumulation_core04_std_63d_slope_v035_signal(volume, closeadj):
    base = _std((volume.where(_diff(closeadj, 1)<0,0)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope std 126d
def cg_f05_technology_f05_technology_volume_accumulation_core05_std_126d_slope_v036_signal(volume, closeadj):
    base = _std((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope std 252d
def cg_f05_technology_f05_technology_volume_accumulation_core06_std_252d_slope_v037_signal(volume, closeadj):
    base = _std((_pct_change(volume, 1)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope std 5d
def cg_f05_technology_f05_technology_volume_accumulation_core07_std_5d_slope_v038_signal(volume, closeadj):
    base = _std((_log((closeadj*volume).abs()+1)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope std 21d
def cg_f05_technology_f05_technology_volume_accumulation_core08_std_21d_slope_v039_signal(volume, closeadj):
    base = _std(((volume>_mean(volume,21)).astype(float)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope std 63d
def cg_f05_technology_f05_technology_volume_accumulation_core09_std_63d_slope_v040_signal(volume, closeadj):
    base = _std((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope slope 252d
def cg_f05_technology_f05_technology_volume_accumulation_core00_slope_252d_slope_v041_signal(volume, closeadj):
    base = _slope((volume), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope slope 5d
def cg_f05_technology_f05_technology_volume_accumulation_core01_slope_5d_slope_v042_signal(volume, closeadj):
    base = _slope((_safe_div(volume, _mean(volume,21)+1e-9)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope slope 21d
def cg_f05_technology_f05_technology_volume_accumulation_core02_slope_21d_slope_v043_signal(volume, closeadj):
    base = _slope((_safe_div(volume, _mean(volume,63)+1e-9)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope slope 63d
def cg_f05_technology_f05_technology_volume_accumulation_core03_slope_63d_slope_v044_signal(volume, closeadj):
    base = _slope((volume.where(_diff(closeadj, 1)>0,0)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope slope 126d
def cg_f05_technology_f05_technology_volume_accumulation_core04_slope_126d_slope_v045_signal(volume, closeadj):
    base = _slope((volume.where(_diff(closeadj, 1)<0,0)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope slope 252d
def cg_f05_technology_f05_technology_volume_accumulation_core05_slope_252d_slope_v046_signal(volume, closeadj):
    base = _slope((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope slope 5d
def cg_f05_technology_f05_technology_volume_accumulation_core06_slope_5d_slope_v047_signal(volume, closeadj):
    base = _slope((_pct_change(volume, 1)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope slope 21d
def cg_f05_technology_f05_technology_volume_accumulation_core07_slope_21d_slope_v048_signal(volume, closeadj):
    base = _slope((_log((closeadj*volume).abs()+1)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope slope 63d
def cg_f05_technology_f05_technology_volume_accumulation_core08_slope_63d_slope_v049_signal(volume, closeadj):
    base = _slope(((volume>_mean(volume,21)).astype(float)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope slope 126d
def cg_f05_technology_f05_technology_volume_accumulation_core09_slope_126d_slope_v050_signal(volume, closeadj):
    base = _slope((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope diff 5d
def cg_f05_technology_f05_technology_volume_accumulation_core00_diff_5d_slope_v051_signal(volume, closeadj):
    base = _diff((volume), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope diff 21d
def cg_f05_technology_f05_technology_volume_accumulation_core01_diff_21d_slope_v052_signal(volume, closeadj):
    base = _diff((_safe_div(volume, _mean(volume,21)+1e-9)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope diff 63d
def cg_f05_technology_f05_technology_volume_accumulation_core02_diff_63d_slope_v053_signal(volume, closeadj):
    base = _diff((_safe_div(volume, _mean(volume,63)+1e-9)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope diff 126d
def cg_f05_technology_f05_technology_volume_accumulation_core03_diff_126d_slope_v054_signal(volume, closeadj):
    base = _diff((volume.where(_diff(closeadj, 1)>0,0)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope diff 252d
def cg_f05_technology_f05_technology_volume_accumulation_core04_diff_252d_slope_v055_signal(volume, closeadj):
    base = _diff((volume.where(_diff(closeadj, 1)<0,0)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope diff 5d
def cg_f05_technology_f05_technology_volume_accumulation_core05_diff_5d_slope_v056_signal(volume, closeadj):
    base = _diff((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope diff 21d
def cg_f05_technology_f05_technology_volume_accumulation_core06_diff_21d_slope_v057_signal(volume, closeadj):
    base = _diff((_pct_change(volume, 1)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope diff 63d
def cg_f05_technology_f05_technology_volume_accumulation_core07_diff_63d_slope_v058_signal(volume, closeadj):
    base = _diff((_log((closeadj*volume).abs()+1)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope diff 126d
def cg_f05_technology_f05_technology_volume_accumulation_core08_diff_126d_slope_v059_signal(volume, closeadj):
    base = _diff(((volume>_mean(volume,21)).astype(float)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope diff 252d
def cg_f05_technology_f05_technology_volume_accumulation_core09_diff_252d_slope_v060_signal(volume, closeadj):
    base = _diff((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope pct 21d
def cg_f05_technology_f05_technology_volume_accumulation_core00_pct_21d_slope_v061_signal(volume, closeadj):
    base = _pct_change(((volume).abs()+1.0), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope pct 63d
def cg_f05_technology_f05_technology_volume_accumulation_core01_pct_63d_slope_v062_signal(volume, closeadj):
    base = _pct_change(((_safe_div(volume, _mean(volume,21)+1e-9)).abs()+1.0), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope pct 126d
def cg_f05_technology_f05_technology_volume_accumulation_core02_pct_126d_slope_v063_signal(volume, closeadj):
    base = _pct_change(((_safe_div(volume, _mean(volume,63)+1e-9)).abs()+1.0), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope pct 252d
def cg_f05_technology_f05_technology_volume_accumulation_core03_pct_252d_slope_v064_signal(volume, closeadj):
    base = _pct_change(((volume.where(_diff(closeadj, 1)>0,0)).abs()+1.0), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope pct 5d
def cg_f05_technology_f05_technology_volume_accumulation_core04_pct_5d_slope_v065_signal(volume, closeadj):
    base = _pct_change(((volume.where(_diff(closeadj, 1)<0,0)).abs()+1.0), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope pct 21d
def cg_f05_technology_f05_technology_volume_accumulation_core05_pct_21d_slope_v066_signal(volume, closeadj):
    base = _pct_change(((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)).abs()+1.0), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope pct 63d
def cg_f05_technology_f05_technology_volume_accumulation_core06_pct_63d_slope_v067_signal(volume, closeadj):
    base = _pct_change(((_pct_change(volume, 1)).abs()+1.0), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope pct 126d
def cg_f05_technology_f05_technology_volume_accumulation_core07_pct_126d_slope_v068_signal(volume, closeadj):
    base = _pct_change(((_log((closeadj*volume).abs()+1)).abs()+1.0), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope pct 252d
def cg_f05_technology_f05_technology_volume_accumulation_core08_pct_252d_slope_v069_signal(volume, closeadj):
    base = _pct_change((((volume>_mean(volume,21)).astype(float)).abs()+1.0), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope pct 5d
def cg_f05_technology_f05_technology_volume_accumulation_core09_pct_5d_slope_v070_signal(volume, closeadj):
    base = _pct_change(((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)).abs()+1.0), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 63d
def cg_f05_technology_f05_technology_volume_accumulation_core00_ewm_63d_slope_v071_signal(volume, closeadj):
    base = _ewm((volume), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 126d
def cg_f05_technology_f05_technology_volume_accumulation_core01_ewm_126d_slope_v072_signal(volume, closeadj):
    base = _ewm((_safe_div(volume, _mean(volume,21)+1e-9)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 252d
def cg_f05_technology_f05_technology_volume_accumulation_core02_ewm_252d_slope_v073_signal(volume, closeadj):
    base = _ewm((_safe_div(volume, _mean(volume,63)+1e-9)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 5d
def cg_f05_technology_f05_technology_volume_accumulation_core03_ewm_5d_slope_v074_signal(volume, closeadj):
    base = _ewm((volume.where(_diff(closeadj, 1)>0,0)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 21d
def cg_f05_technology_f05_technology_volume_accumulation_core04_ewm_21d_slope_v075_signal(volume, closeadj):
    base = _ewm((volume.where(_diff(closeadj, 1)<0,0)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 63d
def cg_f05_technology_f05_technology_volume_accumulation_core05_ewm_63d_slope_v076_signal(volume, closeadj):
    base = _ewm((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 126d
def cg_f05_technology_f05_technology_volume_accumulation_core06_ewm_126d_slope_v077_signal(volume, closeadj):
    base = _ewm((_pct_change(volume, 1)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 252d
def cg_f05_technology_f05_technology_volume_accumulation_core07_ewm_252d_slope_v078_signal(volume, closeadj):
    base = _ewm((_log((closeadj*volume).abs()+1)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 5d
def cg_f05_technology_f05_technology_volume_accumulation_core08_ewm_5d_slope_v079_signal(volume, closeadj):
    base = _ewm(((volume>_mean(volume,21)).astype(float)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 21d
def cg_f05_technology_f05_technology_volume_accumulation_core09_ewm_21d_slope_v080_signal(volume, closeadj):
    base = _ewm((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope skew 126d
def cg_f05_technology_f05_technology_volume_accumulation_core00_skew_126d_slope_v081_signal(volume, closeadj):
    base = _skew((volume), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope skew 252d
def cg_f05_technology_f05_technology_volume_accumulation_core01_skew_252d_slope_v082_signal(volume, closeadj):
    base = _skew((_safe_div(volume, _mean(volume,21)+1e-9)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope skew 5d
def cg_f05_technology_f05_technology_volume_accumulation_core02_skew_5d_slope_v083_signal(volume, closeadj):
    base = _skew((_safe_div(volume, _mean(volume,63)+1e-9)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope skew 21d
def cg_f05_technology_f05_technology_volume_accumulation_core03_skew_21d_slope_v084_signal(volume, closeadj):
    base = _skew((volume.where(_diff(closeadj, 1)>0,0)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope skew 63d
def cg_f05_technology_f05_technology_volume_accumulation_core04_skew_63d_slope_v085_signal(volume, closeadj):
    base = _skew((volume.where(_diff(closeadj, 1)<0,0)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope skew 126d
def cg_f05_technology_f05_technology_volume_accumulation_core05_skew_126d_slope_v086_signal(volume, closeadj):
    base = _skew((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope skew 252d
def cg_f05_technology_f05_technology_volume_accumulation_core06_skew_252d_slope_v087_signal(volume, closeadj):
    base = _skew((_pct_change(volume, 1)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope skew 5d
def cg_f05_technology_f05_technology_volume_accumulation_core07_skew_5d_slope_v088_signal(volume, closeadj):
    base = _skew((_log((closeadj*volume).abs()+1)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope skew 21d
def cg_f05_technology_f05_technology_volume_accumulation_core08_skew_21d_slope_v089_signal(volume, closeadj):
    base = _skew(((volume>_mean(volume,21)).astype(float)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope skew 63d
def cg_f05_technology_f05_technology_volume_accumulation_core09_skew_63d_slope_v090_signal(volume, closeadj):
    base = _skew((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope kurt 252d
def cg_f05_technology_f05_technology_volume_accumulation_core00_kurt_252d_slope_v091_signal(volume, closeadj):
    base = _kurt((volume), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope kurt 5d
def cg_f05_technology_f05_technology_volume_accumulation_core01_kurt_5d_slope_v092_signal(volume, closeadj):
    base = _kurt((_safe_div(volume, _mean(volume,21)+1e-9)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope kurt 21d
def cg_f05_technology_f05_technology_volume_accumulation_core02_kurt_21d_slope_v093_signal(volume, closeadj):
    base = _kurt((_safe_div(volume, _mean(volume,63)+1e-9)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope kurt 63d
def cg_f05_technology_f05_technology_volume_accumulation_core03_kurt_63d_slope_v094_signal(volume, closeadj):
    base = _kurt((volume.where(_diff(closeadj, 1)>0,0)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope kurt 126d
def cg_f05_technology_f05_technology_volume_accumulation_core04_kurt_126d_slope_v095_signal(volume, closeadj):
    base = _kurt((volume.where(_diff(closeadj, 1)<0,0)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope kurt 252d
def cg_f05_technology_f05_technology_volume_accumulation_core05_kurt_252d_slope_v096_signal(volume, closeadj):
    base = _kurt((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope kurt 5d
def cg_f05_technology_f05_technology_volume_accumulation_core06_kurt_5d_slope_v097_signal(volume, closeadj):
    base = _kurt((_pct_change(volume, 1)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope kurt 21d
def cg_f05_technology_f05_technology_volume_accumulation_core07_kurt_21d_slope_v098_signal(volume, closeadj):
    base = _kurt((_log((closeadj*volume).abs()+1)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope kurt 63d
def cg_f05_technology_f05_technology_volume_accumulation_core08_kurt_63d_slope_v099_signal(volume, closeadj):
    base = _kurt(((volume>_mean(volume,21)).astype(float)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope kurt 126d
def cg_f05_technology_f05_technology_volume_accumulation_core09_kurt_126d_slope_v100_signal(volume, closeadj):
    base = _kurt((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope autocorr 5d
def cg_f05_technology_f05_technology_volume_accumulation_core00_autocorr_5d_slope_v101_signal(volume, closeadj):
    base = _autocorr((volume), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope autocorr 21d
def cg_f05_technology_f05_technology_volume_accumulation_core01_autocorr_21d_slope_v102_signal(volume, closeadj):
    base = _autocorr((_safe_div(volume, _mean(volume,21)+1e-9)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope autocorr 63d
def cg_f05_technology_f05_technology_volume_accumulation_core02_autocorr_63d_slope_v103_signal(volume, closeadj):
    base = _autocorr((_safe_div(volume, _mean(volume,63)+1e-9)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope autocorr 126d
def cg_f05_technology_f05_technology_volume_accumulation_core03_autocorr_126d_slope_v104_signal(volume, closeadj):
    base = _autocorr((volume.where(_diff(closeadj, 1)>0,0)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope autocorr 252d
def cg_f05_technology_f05_technology_volume_accumulation_core04_autocorr_252d_slope_v105_signal(volume, closeadj):
    base = _autocorr((volume.where(_diff(closeadj, 1)<0,0)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope autocorr 5d
def cg_f05_technology_f05_technology_volume_accumulation_core05_autocorr_5d_slope_v106_signal(volume, closeadj):
    base = _autocorr((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope autocorr 21d
def cg_f05_technology_f05_technology_volume_accumulation_core06_autocorr_21d_slope_v107_signal(volume, closeadj):
    base = _autocorr((_pct_change(volume, 1)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope autocorr 63d
def cg_f05_technology_f05_technology_volume_accumulation_core07_autocorr_63d_slope_v108_signal(volume, closeadj):
    base = _autocorr((_log((closeadj*volume).abs()+1)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope autocorr 126d
def cg_f05_technology_f05_technology_volume_accumulation_core08_autocorr_126d_slope_v109_signal(volume, closeadj):
    base = _autocorr(((volume>_mean(volume,21)).astype(float)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope autocorr 252d
def cg_f05_technology_f05_technology_volume_accumulation_core09_autocorr_252d_slope_v110_signal(volume, closeadj):
    base = _autocorr((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope snr 21d
def cg_f05_technology_f05_technology_volume_accumulation_core00_snr_21d_slope_v111_signal(volume, closeadj):
    base = _safe_div(_diff((volume), max(1, 21//3)).abs(), _std(_diff((volume),1), 21)+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope snr 63d
def cg_f05_technology_f05_technology_volume_accumulation_core01_snr_63d_slope_v112_signal(volume, closeadj):
    base = _safe_div(_diff((_safe_div(volume, _mean(volume,21)+1e-9)), max(1, 63//3)).abs(), _std(_diff((_safe_div(volume, _mean(volume,21)+1e-9)),1), 63)+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope snr 126d
def cg_f05_technology_f05_technology_volume_accumulation_core02_snr_126d_slope_v113_signal(volume, closeadj):
    base = _safe_div(_diff((_safe_div(volume, _mean(volume,63)+1e-9)), max(1, 126//3)).abs(), _std(_diff((_safe_div(volume, _mean(volume,63)+1e-9)),1), 126)+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope snr 252d
def cg_f05_technology_f05_technology_volume_accumulation_core03_snr_252d_slope_v114_signal(volume, closeadj):
    base = _safe_div(_diff((volume.where(_diff(closeadj, 1)>0,0)), max(1, 252//3)).abs(), _std(_diff((volume.where(_diff(closeadj, 1)>0,0)),1), 252)+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope snr 5d
def cg_f05_technology_f05_technology_volume_accumulation_core04_snr_5d_slope_v115_signal(volume, closeadj):
    base = _safe_div(_diff((volume.where(_diff(closeadj, 1)<0,0)), max(1, 5//3)).abs(), _std(_diff((volume.where(_diff(closeadj, 1)<0,0)),1), 5)+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope snr 21d
def cg_f05_technology_f05_technology_volume_accumulation_core05_snr_21d_slope_v116_signal(volume, closeadj):
    base = _safe_div(_diff((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), max(1, 21//3)).abs(), _std(_diff((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)),1), 21)+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope snr 63d
def cg_f05_technology_f05_technology_volume_accumulation_core06_snr_63d_slope_v117_signal(volume, closeadj):
    base = _safe_div(_diff((_pct_change(volume, 1)), max(1, 63//3)).abs(), _std(_diff((_pct_change(volume, 1)),1), 63)+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope snr 126d
def cg_f05_technology_f05_technology_volume_accumulation_core07_snr_126d_slope_v118_signal(volume, closeadj):
    base = _safe_div(_diff((_log((closeadj*volume).abs()+1)), max(1, 126//3)).abs(), _std(_diff((_log((closeadj*volume).abs()+1)),1), 126)+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope snr 252d
def cg_f05_technology_f05_technology_volume_accumulation_core08_snr_252d_slope_v119_signal(volume, closeadj):
    base = _safe_div(_diff(((volume>_mean(volume,21)).astype(float)), max(1, 252//3)).abs(), _std(_diff(((volume>_mean(volume,21)).astype(float)),1), 252)+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope snr 5d
def cg_f05_technology_f05_technology_volume_accumulation_core09_snr_5d_slope_v120_signal(volume, closeadj):
    base = _safe_div(_diff((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), max(1, 5//3)).abs(), _std(_diff((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)),1), 5)+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope ema_gap 63d
def cg_f05_technology_f05_technology_volume_accumulation_core00_ema_gap_63d_slope_v121_signal(volume, closeadj):
    base = _mean((volume), 63) - _ewm((volume), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope ema_gap 126d
def cg_f05_technology_f05_technology_volume_accumulation_core01_ema_gap_126d_slope_v122_signal(volume, closeadj):
    base = _mean((_safe_div(volume, _mean(volume,21)+1e-9)), 126) - _ewm((_safe_div(volume, _mean(volume,21)+1e-9)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope ema_gap 252d
def cg_f05_technology_f05_technology_volume_accumulation_core02_ema_gap_252d_slope_v123_signal(volume, closeadj):
    base = _mean((_safe_div(volume, _mean(volume,63)+1e-9)), 252) - _ewm((_safe_div(volume, _mean(volume,63)+1e-9)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope ema_gap 5d
def cg_f05_technology_f05_technology_volume_accumulation_core03_ema_gap_5d_slope_v124_signal(volume, closeadj):
    base = _mean((volume.where(_diff(closeadj, 1)>0,0)), 5) - _ewm((volume.where(_diff(closeadj, 1)>0,0)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope ema_gap 21d
def cg_f05_technology_f05_technology_volume_accumulation_core04_ema_gap_21d_slope_v125_signal(volume, closeadj):
    base = _mean((volume.where(_diff(closeadj, 1)<0,0)), 21) - _ewm((volume.where(_diff(closeadj, 1)<0,0)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope ema_gap 63d
def cg_f05_technology_f05_technology_volume_accumulation_core05_ema_gap_63d_slope_v126_signal(volume, closeadj):
    base = _mean((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 63) - _ewm((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope ema_gap 126d
def cg_f05_technology_f05_technology_volume_accumulation_core06_ema_gap_126d_slope_v127_signal(volume, closeadj):
    base = _mean((_pct_change(volume, 1)), 126) - _ewm((_pct_change(volume, 1)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope ema_gap 252d
def cg_f05_technology_f05_technology_volume_accumulation_core07_ema_gap_252d_slope_v128_signal(volume, closeadj):
    base = _mean((_log((closeadj*volume).abs()+1)), 252) - _ewm((_log((closeadj*volume).abs()+1)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope ema_gap 5d
def cg_f05_technology_f05_technology_volume_accumulation_core08_ema_gap_5d_slope_v129_signal(volume, closeadj):
    base = _mean(((volume>_mean(volume,21)).astype(float)), 5) - _ewm(((volume>_mean(volume,21)).astype(float)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope ema_gap 21d
def cg_f05_technology_f05_technology_volume_accumulation_core09_ema_gap_21d_slope_v130_signal(volume, closeadj):
    base = _mean((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 21) - _ewm((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope vol_ratio 126d
def cg_f05_technology_f05_technology_volume_accumulation_core00_vol_ratio_126d_slope_v131_signal(volume, closeadj):
    base = _safe_div(_std((volume), max(2, 126//3)), _std((volume), 126).abs()+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope vol_ratio 252d
def cg_f05_technology_f05_technology_volume_accumulation_core01_vol_ratio_252d_slope_v132_signal(volume, closeadj):
    base = _safe_div(_std((_safe_div(volume, _mean(volume,21)+1e-9)), max(2, 252//3)), _std((_safe_div(volume, _mean(volume,21)+1e-9)), 252).abs()+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope vol_ratio 5d
def cg_f05_technology_f05_technology_volume_accumulation_core02_vol_ratio_5d_slope_v133_signal(volume, closeadj):
    base = _safe_div(_std((_safe_div(volume, _mean(volume,63)+1e-9)), max(2, 5//3)), _std((_safe_div(volume, _mean(volume,63)+1e-9)), 5).abs()+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope vol_ratio 21d
def cg_f05_technology_f05_technology_volume_accumulation_core03_vol_ratio_21d_slope_v134_signal(volume, closeadj):
    base = _safe_div(_std((volume.where(_diff(closeadj, 1)>0,0)), max(2, 21//3)), _std((volume.where(_diff(closeadj, 1)>0,0)), 21).abs()+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope vol_ratio 63d
def cg_f05_technology_f05_technology_volume_accumulation_core04_vol_ratio_63d_slope_v135_signal(volume, closeadj):
    base = _safe_div(_std((volume.where(_diff(closeadj, 1)<0,0)), max(2, 63//3)), _std((volume.where(_diff(closeadj, 1)<0,0)), 63).abs()+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope vol_ratio 126d
def cg_f05_technology_f05_technology_volume_accumulation_core05_vol_ratio_126d_slope_v136_signal(volume, closeadj):
    base = _safe_div(_std((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), max(2, 126//3)), _std((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 126).abs()+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope vol_ratio 252d
def cg_f05_technology_f05_technology_volume_accumulation_core06_vol_ratio_252d_slope_v137_signal(volume, closeadj):
    base = _safe_div(_std((_pct_change(volume, 1)), max(2, 252//3)), _std((_pct_change(volume, 1)), 252).abs()+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope vol_ratio 5d
def cg_f05_technology_f05_technology_volume_accumulation_core07_vol_ratio_5d_slope_v138_signal(volume, closeadj):
    base = _safe_div(_std((_log((closeadj*volume).abs()+1)), max(2, 5//3)), _std((_log((closeadj*volume).abs()+1)), 5).abs()+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope vol_ratio 21d
def cg_f05_technology_f05_technology_volume_accumulation_core08_vol_ratio_21d_slope_v139_signal(volume, closeadj):
    base = _safe_div(_std(((volume>_mean(volume,21)).astype(float)), max(2, 21//3)), _std(((volume>_mean(volume,21)).astype(float)), 21).abs()+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope vol_ratio 63d
def cg_f05_technology_f05_technology_volume_accumulation_core09_vol_ratio_63d_slope_v140_signal(volume, closeadj):
    base = _safe_div(_std((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), max(2, 63//3)), _std((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 63).abs()+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope recent_vs_long 252d
def cg_f05_technology_f05_technology_volume_accumulation_core00_recent_vs_long_252d_slope_v141_signal(volume, closeadj):
    base = _mean((volume), max(2, 252//3)) - _mean((volume), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope recent_vs_long 5d
def cg_f05_technology_f05_technology_volume_accumulation_core01_recent_vs_long_5d_slope_v142_signal(volume, closeadj):
    base = _mean((_safe_div(volume, _mean(volume,21)+1e-9)), max(2, 5//3)) - _mean((_safe_div(volume, _mean(volume,21)+1e-9)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope recent_vs_long 21d
def cg_f05_technology_f05_technology_volume_accumulation_core02_recent_vs_long_21d_slope_v143_signal(volume, closeadj):
    base = _mean((_safe_div(volume, _mean(volume,63)+1e-9)), max(2, 21//3)) - _mean((_safe_div(volume, _mean(volume,63)+1e-9)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope recent_vs_long 63d
def cg_f05_technology_f05_technology_volume_accumulation_core03_recent_vs_long_63d_slope_v144_signal(volume, closeadj):
    base = _mean((volume.where(_diff(closeadj, 1)>0,0)), max(2, 63//3)) - _mean((volume.where(_diff(closeadj, 1)>0,0)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope recent_vs_long 126d
def cg_f05_technology_f05_technology_volume_accumulation_core04_recent_vs_long_126d_slope_v145_signal(volume, closeadj):
    base = _mean((volume.where(_diff(closeadj, 1)<0,0)), max(2, 126//3)) - _mean((volume.where(_diff(closeadj, 1)<0,0)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope recent_vs_long 252d
def cg_f05_technology_f05_technology_volume_accumulation_core05_recent_vs_long_252d_slope_v146_signal(volume, closeadj):
    base = _mean((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), max(2, 252//3)) - _mean((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope recent_vs_long 5d
def cg_f05_technology_f05_technology_volume_accumulation_core06_recent_vs_long_5d_slope_v147_signal(volume, closeadj):
    base = _mean((_pct_change(volume, 1)), max(2, 5//3)) - _mean((_pct_change(volume, 1)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope recent_vs_long 21d
def cg_f05_technology_f05_technology_volume_accumulation_core07_recent_vs_long_21d_slope_v148_signal(volume, closeadj):
    base = _mean((_log((closeadj*volume).abs()+1)), max(2, 21//3)) - _mean((_log((closeadj*volume).abs()+1)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope recent_vs_long 63d
def cg_f05_technology_f05_technology_volume_accumulation_core08_recent_vs_long_63d_slope_v149_signal(volume, closeadj):
    base = _mean(((volume>_mean(volume,21)).astype(float)), max(2, 63//3)) - _mean(((volume>_mean(volume,21)).astype(float)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope recent_vs_long 126d
def cg_f05_technology_f05_technology_volume_accumulation_core09_recent_vs_long_126d_slope_v150_signal(volume, closeadj):
    base = _mean((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), max(2, 126//3)) - _mean((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

