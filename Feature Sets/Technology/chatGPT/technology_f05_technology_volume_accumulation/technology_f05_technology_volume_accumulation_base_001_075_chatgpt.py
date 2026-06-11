import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 mean 5d
def cg_f05_technology_f05_technology_volume_accumulation_core00_mean_5d_base_v001_signal(volume, closeadj):
    result = _mean((volume), 5)
    return _clean(result)

# core01 mean 21d
def cg_f05_technology_f05_technology_volume_accumulation_core01_mean_21d_base_v002_signal(volume, closeadj):
    result = _mean((_safe_div(volume, _mean(volume,21)+1e-9)), 21)
    return _clean(result)

# core02 mean 63d
def cg_f05_technology_f05_technology_volume_accumulation_core02_mean_63d_base_v003_signal(volume, closeadj):
    result = _mean((_safe_div(volume, _mean(volume,63)+1e-9)), 63)
    return _clean(result)

# core03 mean 126d
def cg_f05_technology_f05_technology_volume_accumulation_core03_mean_126d_base_v004_signal(volume, closeadj):
    result = _mean((volume.where(_diff(closeadj, 1)>0,0)), 126)
    return _clean(result)

# core04 mean 252d
def cg_f05_technology_f05_technology_volume_accumulation_core04_mean_252d_base_v005_signal(volume, closeadj):
    result = _mean((volume.where(_diff(closeadj, 1)<0,0)), 252)
    return _clean(result)

# core05 mean 5d
def cg_f05_technology_f05_technology_volume_accumulation_core05_mean_5d_base_v006_signal(volume, closeadj):
    result = _mean((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 5)
    return _clean(result)

# core06 mean 21d
def cg_f05_technology_f05_technology_volume_accumulation_core06_mean_21d_base_v007_signal(volume, closeadj):
    result = _mean((_pct_change(volume, 1)), 21)
    return _clean(result)

# core07 mean 63d
def cg_f05_technology_f05_technology_volume_accumulation_core07_mean_63d_base_v008_signal(volume, closeadj):
    result = _mean((_log((closeadj*volume).abs()+1)), 63)
    return _clean(result)

# core08 mean 126d
def cg_f05_technology_f05_technology_volume_accumulation_core08_mean_126d_base_v009_signal(volume, closeadj):
    result = _mean(((volume>_mean(volume,21)).astype(float)), 126)
    return _clean(result)

# core09 mean 252d
def cg_f05_technology_f05_technology_volume_accumulation_core09_mean_252d_base_v010_signal(volume, closeadj):
    result = _mean((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 252)
    return _clean(result)

# core00 z 21d
def cg_f05_technology_f05_technology_volume_accumulation_core00_z_21d_base_v011_signal(volume, closeadj):
    result = _z((volume), 21)
    return _clean(result)

# core01 z 63d
def cg_f05_technology_f05_technology_volume_accumulation_core01_z_63d_base_v012_signal(volume, closeadj):
    result = _z((_safe_div(volume, _mean(volume,21)+1e-9)), 63)
    return _clean(result)

# core02 z 126d
def cg_f05_technology_f05_technology_volume_accumulation_core02_z_126d_base_v013_signal(volume, closeadj):
    result = _z((_safe_div(volume, _mean(volume,63)+1e-9)), 126)
    return _clean(result)

# core03 z 252d
def cg_f05_technology_f05_technology_volume_accumulation_core03_z_252d_base_v014_signal(volume, closeadj):
    result = _z((volume.where(_diff(closeadj, 1)>0,0)), 252)
    return _clean(result)

# core04 z 5d
def cg_f05_technology_f05_technology_volume_accumulation_core04_z_5d_base_v015_signal(volume, closeadj):
    result = _z((volume.where(_diff(closeadj, 1)<0,0)), 5)
    return _clean(result)

# core05 z 21d
def cg_f05_technology_f05_technology_volume_accumulation_core05_z_21d_base_v016_signal(volume, closeadj):
    result = _z((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 21)
    return _clean(result)

# core06 z 63d
def cg_f05_technology_f05_technology_volume_accumulation_core06_z_63d_base_v017_signal(volume, closeadj):
    result = _z((_pct_change(volume, 1)), 63)
    return _clean(result)

# core07 z 126d
def cg_f05_technology_f05_technology_volume_accumulation_core07_z_126d_base_v018_signal(volume, closeadj):
    result = _z((_log((closeadj*volume).abs()+1)), 126)
    return _clean(result)

# core08 z 252d
def cg_f05_technology_f05_technology_volume_accumulation_core08_z_252d_base_v019_signal(volume, closeadj):
    result = _z(((volume>_mean(volume,21)).astype(float)), 252)
    return _clean(result)

# core09 z 5d
def cg_f05_technology_f05_technology_volume_accumulation_core09_z_5d_base_v020_signal(volume, closeadj):
    result = _z((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 5)
    return _clean(result)

# core00 rank 63d
def cg_f05_technology_f05_technology_volume_accumulation_core00_rank_63d_base_v021_signal(volume, closeadj):
    result = _rank((volume), 63)
    return _clean(result)

# core01 rank 126d
def cg_f05_technology_f05_technology_volume_accumulation_core01_rank_126d_base_v022_signal(volume, closeadj):
    result = _rank((_safe_div(volume, _mean(volume,21)+1e-9)), 126)
    return _clean(result)

# core02 rank 252d
def cg_f05_technology_f05_technology_volume_accumulation_core02_rank_252d_base_v023_signal(volume, closeadj):
    result = _rank((_safe_div(volume, _mean(volume,63)+1e-9)), 252)
    return _clean(result)

# core03 rank 5d
def cg_f05_technology_f05_technology_volume_accumulation_core03_rank_5d_base_v024_signal(volume, closeadj):
    result = _rank((volume.where(_diff(closeadj, 1)>0,0)), 5)
    return _clean(result)

# core04 rank 21d
def cg_f05_technology_f05_technology_volume_accumulation_core04_rank_21d_base_v025_signal(volume, closeadj):
    result = _rank((volume.where(_diff(closeadj, 1)<0,0)), 21)
    return _clean(result)

# core05 rank 63d
def cg_f05_technology_f05_technology_volume_accumulation_core05_rank_63d_base_v026_signal(volume, closeadj):
    result = _rank((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 63)
    return _clean(result)

# core06 rank 126d
def cg_f05_technology_f05_technology_volume_accumulation_core06_rank_126d_base_v027_signal(volume, closeadj):
    result = _rank((_pct_change(volume, 1)), 126)
    return _clean(result)

# core07 rank 252d
def cg_f05_technology_f05_technology_volume_accumulation_core07_rank_252d_base_v028_signal(volume, closeadj):
    result = _rank((_log((closeadj*volume).abs()+1)), 252)
    return _clean(result)

# core08 rank 5d
def cg_f05_technology_f05_technology_volume_accumulation_core08_rank_5d_base_v029_signal(volume, closeadj):
    result = _rank(((volume>_mean(volume,21)).astype(float)), 5)
    return _clean(result)

# core09 rank 21d
def cg_f05_technology_f05_technology_volume_accumulation_core09_rank_21d_base_v030_signal(volume, closeadj):
    result = _rank((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 21)
    return _clean(result)

# core00 std 126d
def cg_f05_technology_f05_technology_volume_accumulation_core00_std_126d_base_v031_signal(volume, closeadj):
    result = _std((volume), 126)
    return _clean(result)

# core01 std 252d
def cg_f05_technology_f05_technology_volume_accumulation_core01_std_252d_base_v032_signal(volume, closeadj):
    result = _std((_safe_div(volume, _mean(volume,21)+1e-9)), 252)
    return _clean(result)

# core02 std 5d
def cg_f05_technology_f05_technology_volume_accumulation_core02_std_5d_base_v033_signal(volume, closeadj):
    result = _std((_safe_div(volume, _mean(volume,63)+1e-9)), 5)
    return _clean(result)

# core03 std 21d
def cg_f05_technology_f05_technology_volume_accumulation_core03_std_21d_base_v034_signal(volume, closeadj):
    result = _std((volume.where(_diff(closeadj, 1)>0,0)), 21)
    return _clean(result)

# core04 std 63d
def cg_f05_technology_f05_technology_volume_accumulation_core04_std_63d_base_v035_signal(volume, closeadj):
    result = _std((volume.where(_diff(closeadj, 1)<0,0)), 63)
    return _clean(result)

# core05 std 126d
def cg_f05_technology_f05_technology_volume_accumulation_core05_std_126d_base_v036_signal(volume, closeadj):
    result = _std((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 126)
    return _clean(result)

# core06 std 252d
def cg_f05_technology_f05_technology_volume_accumulation_core06_std_252d_base_v037_signal(volume, closeadj):
    result = _std((_pct_change(volume, 1)), 252)
    return _clean(result)

# core07 std 5d
def cg_f05_technology_f05_technology_volume_accumulation_core07_std_5d_base_v038_signal(volume, closeadj):
    result = _std((_log((closeadj*volume).abs()+1)), 5)
    return _clean(result)

# core08 std 21d
def cg_f05_technology_f05_technology_volume_accumulation_core08_std_21d_base_v039_signal(volume, closeadj):
    result = _std(((volume>_mean(volume,21)).astype(float)), 21)
    return _clean(result)

# core09 std 63d
def cg_f05_technology_f05_technology_volume_accumulation_core09_std_63d_base_v040_signal(volume, closeadj):
    result = _std((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 63)
    return _clean(result)

# core00 slope 252d
def cg_f05_technology_f05_technology_volume_accumulation_core00_slope_252d_base_v041_signal(volume, closeadj):
    result = _slope((volume), 252)
    return _clean(result)

# core01 slope 5d
def cg_f05_technology_f05_technology_volume_accumulation_core01_slope_5d_base_v042_signal(volume, closeadj):
    result = _slope((_safe_div(volume, _mean(volume,21)+1e-9)), 5)
    return _clean(result)

# core02 slope 21d
def cg_f05_technology_f05_technology_volume_accumulation_core02_slope_21d_base_v043_signal(volume, closeadj):
    result = _slope((_safe_div(volume, _mean(volume,63)+1e-9)), 21)
    return _clean(result)

# core03 slope 63d
def cg_f05_technology_f05_technology_volume_accumulation_core03_slope_63d_base_v044_signal(volume, closeadj):
    result = _slope((volume.where(_diff(closeadj, 1)>0,0)), 63)
    return _clean(result)

# core04 slope 126d
def cg_f05_technology_f05_technology_volume_accumulation_core04_slope_126d_base_v045_signal(volume, closeadj):
    result = _slope((volume.where(_diff(closeadj, 1)<0,0)), 126)
    return _clean(result)

# core05 slope 252d
def cg_f05_technology_f05_technology_volume_accumulation_core05_slope_252d_base_v046_signal(volume, closeadj):
    result = _slope((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 252)
    return _clean(result)

# core06 slope 5d
def cg_f05_technology_f05_technology_volume_accumulation_core06_slope_5d_base_v047_signal(volume, closeadj):
    result = _slope((_pct_change(volume, 1)), 5)
    return _clean(result)

# core07 slope 21d
def cg_f05_technology_f05_technology_volume_accumulation_core07_slope_21d_base_v048_signal(volume, closeadj):
    result = _slope((_log((closeadj*volume).abs()+1)), 21)
    return _clean(result)

# core08 slope 63d
def cg_f05_technology_f05_technology_volume_accumulation_core08_slope_63d_base_v049_signal(volume, closeadj):
    result = _slope(((volume>_mean(volume,21)).astype(float)), 63)
    return _clean(result)

# core09 slope 126d
def cg_f05_technology_f05_technology_volume_accumulation_core09_slope_126d_base_v050_signal(volume, closeadj):
    result = _slope((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 126)
    return _clean(result)

# core00 diff 5d
def cg_f05_technology_f05_technology_volume_accumulation_core00_diff_5d_base_v051_signal(volume, closeadj):
    result = _diff((volume), 5)
    return _clean(result)

# core01 diff 21d
def cg_f05_technology_f05_technology_volume_accumulation_core01_diff_21d_base_v052_signal(volume, closeadj):
    result = _diff((_safe_div(volume, _mean(volume,21)+1e-9)), 21)
    return _clean(result)

# core02 diff 63d
def cg_f05_technology_f05_technology_volume_accumulation_core02_diff_63d_base_v053_signal(volume, closeadj):
    result = _diff((_safe_div(volume, _mean(volume,63)+1e-9)), 63)
    return _clean(result)

# core03 diff 126d
def cg_f05_technology_f05_technology_volume_accumulation_core03_diff_126d_base_v054_signal(volume, closeadj):
    result = _diff((volume.where(_diff(closeadj, 1)>0,0)), 126)
    return _clean(result)

# core04 diff 252d
def cg_f05_technology_f05_technology_volume_accumulation_core04_diff_252d_base_v055_signal(volume, closeadj):
    result = _diff((volume.where(_diff(closeadj, 1)<0,0)), 252)
    return _clean(result)

# core05 diff 5d
def cg_f05_technology_f05_technology_volume_accumulation_core05_diff_5d_base_v056_signal(volume, closeadj):
    result = _diff((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)), 5)
    return _clean(result)

# core06 diff 21d
def cg_f05_technology_f05_technology_volume_accumulation_core06_diff_21d_base_v057_signal(volume, closeadj):
    result = _diff((_pct_change(volume, 1)), 21)
    return _clean(result)

# core07 diff 63d
def cg_f05_technology_f05_technology_volume_accumulation_core07_diff_63d_base_v058_signal(volume, closeadj):
    result = _diff((_log((closeadj*volume).abs()+1)), 63)
    return _clean(result)

# core08 diff 126d
def cg_f05_technology_f05_technology_volume_accumulation_core08_diff_126d_base_v059_signal(volume, closeadj):
    result = _diff(((volume>_mean(volume,21)).astype(float)), 126)
    return _clean(result)

# core09 diff 252d
def cg_f05_technology_f05_technology_volume_accumulation_core09_diff_252d_base_v060_signal(volume, closeadj):
    result = _diff((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)), 252)
    return _clean(result)

# core00 pct 21d
def cg_f05_technology_f05_technology_volume_accumulation_core00_pct_21d_base_v061_signal(volume, closeadj):
    result = _pct_change(((volume).abs()+1.0), 21)
    return _clean(result)

# core01 pct 63d
def cg_f05_technology_f05_technology_volume_accumulation_core01_pct_63d_base_v062_signal(volume, closeadj):
    result = _pct_change(((_safe_div(volume, _mean(volume,21)+1e-9)).abs()+1.0), 63)
    return _clean(result)

# core02 pct 126d
def cg_f05_technology_f05_technology_volume_accumulation_core02_pct_126d_base_v063_signal(volume, closeadj):
    result = _pct_change(((_safe_div(volume, _mean(volume,63)+1e-9)).abs()+1.0), 126)
    return _clean(result)

# core03 pct 252d
def cg_f05_technology_f05_technology_volume_accumulation_core03_pct_252d_base_v064_signal(volume, closeadj):
    result = _pct_change(((volume.where(_diff(closeadj, 1)>0,0)).abs()+1.0), 252)
    return _clean(result)

# core04 pct 5d
def cg_f05_technology_f05_technology_volume_accumulation_core04_pct_5d_base_v065_signal(volume, closeadj):
    result = _pct_change(((volume.where(_diff(closeadj, 1)<0,0)).abs()+1.0), 5)
    return _clean(result)

# core05 pct 21d
def cg_f05_technology_f05_technology_volume_accumulation_core05_pct_21d_base_v066_signal(volume, closeadj):
    result = _pct_change(((_safe_div(volume.where(_diff(closeadj, 1)>0,0)-volume.where(_diff(closeadj, 1)<0,0),volume.abs()+1e-9)).abs()+1.0), 21)
    return _clean(result)

# core06 pct 63d
def cg_f05_technology_f05_technology_volume_accumulation_core06_pct_63d_base_v067_signal(volume, closeadj):
    result = _pct_change(((_pct_change(volume, 1)).abs()+1.0), 63)
    return _clean(result)

# core07 pct 126d
def cg_f05_technology_f05_technology_volume_accumulation_core07_pct_126d_base_v068_signal(volume, closeadj):
    result = _pct_change(((_log((closeadj*volume).abs()+1)).abs()+1.0), 126)
    return _clean(result)

# core08 pct 252d
def cg_f05_technology_f05_technology_volume_accumulation_core08_pct_252d_base_v069_signal(volume, closeadj):
    result = _pct_change((((volume>_mean(volume,21)).astype(float)).abs()+1.0), 252)
    return _clean(result)

# core09 pct 5d
def cg_f05_technology_f05_technology_volume_accumulation_core09_pct_5d_base_v070_signal(volume, closeadj):
    result = _pct_change(((((volume>_mean(volume,21))&(_pct_change(closeadj, 1).abs()<_std(_pct_change(closeadj, 1),63))).astype(float)).abs()+1.0), 5)
    return _clean(result)

# core00 ewm 63d
def cg_f05_technology_f05_technology_volume_accumulation_core00_ewm_63d_base_v071_signal(volume, closeadj):
    result = _ewm((volume), 63)
    return _clean(result)

# core01 ewm 126d
def cg_f05_technology_f05_technology_volume_accumulation_core01_ewm_126d_base_v072_signal(volume, closeadj):
    result = _ewm((_safe_div(volume, _mean(volume,21)+1e-9)), 126)
    return _clean(result)

# core02 ewm 252d
def cg_f05_technology_f05_technology_volume_accumulation_core02_ewm_252d_base_v073_signal(volume, closeadj):
    result = _ewm((_safe_div(volume, _mean(volume,63)+1e-9)), 252)
    return _clean(result)

# core03 ewm 5d
def cg_f05_technology_f05_technology_volume_accumulation_core03_ewm_5d_base_v074_signal(volume, closeadj):
    result = _ewm((volume.where(_diff(closeadj, 1)>0,0)), 5)
    return _clean(result)

# core04 ewm 21d
def cg_f05_technology_f05_technology_volume_accumulation_core04_ewm_21d_base_v075_signal(volume, closeadj):
    result = _ewm((volume.where(_diff(closeadj, 1)<0,0)), 21)
    return _clean(result)

