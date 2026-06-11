import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 mean 5d
def cg_f10_technology_f10_technology_price_compression_core00_mean_5d_base_v001_signal(high, low, closeadj, volume):
    result = _mean((_safe_div(high-low,closeadj.abs()+1e-9)), 5)
    return _clean(result)

# core01 mean 21d
def cg_f10_technology_f10_technology_price_compression_core01_mean_21d_base_v002_signal(high, low, closeadj, volume):
    result = _mean((high-low), 21)
    return _clean(result)

# core02 mean 63d
def cg_f10_technology_f10_technology_price_compression_core02_mean_63d_base_v003_signal(high, low, closeadj, volume):
    result = _mean((_std(closeadj,21)), 63)
    return _clean(result)

# core03 mean 126d
def cg_f10_technology_f10_technology_price_compression_core03_mean_126d_base_v004_signal(high, low, closeadj, volume):
    result = _mean((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), 126)
    return _clean(result)

# core04 mean 252d
def cg_f10_technology_f10_technology_price_compression_core04_mean_252d_base_v005_signal(high, low, closeadj, volume):
    result = _mean(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), 252)
    return _clean(result)

# core05 mean 5d
def cg_f10_technology_f10_technology_price_compression_core05_mean_5d_base_v006_signal(high, low, closeadj, volume):
    result = _mean((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), 5)
    return _clean(result)

# core06 mean 21d
def cg_f10_technology_f10_technology_price_compression_core06_mean_21d_base_v007_signal(high, low, closeadj, volume):
    result = _mean((_std(_pct_change(closeadj,1),21)), 21)
    return _clean(result)

# core07 mean 63d
def cg_f10_technology_f10_technology_price_compression_core07_mean_63d_base_v008_signal(high, low, closeadj, volume):
    result = _mean((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), 63)
    return _clean(result)

# core08 mean 126d
def cg_f10_technology_f10_technology_price_compression_core08_mean_126d_base_v009_signal(high, low, closeadj, volume):
    result = _mean(((_rank(high-low,63)<0.25).astype(float)), 126)
    return _clean(result)

# core09 mean 252d
def cg_f10_technology_f10_technology_price_compression_core09_mean_252d_base_v010_signal(high, low, closeadj, volume):
    result = _mean((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), 252)
    return _clean(result)

# core00 z 21d
def cg_f10_technology_f10_technology_price_compression_core00_z_21d_base_v011_signal(high, low, closeadj, volume):
    result = _z((_safe_div(high-low,closeadj.abs()+1e-9)), 21)
    return _clean(result)

# core01 z 63d
def cg_f10_technology_f10_technology_price_compression_core01_z_63d_base_v012_signal(high, low, closeadj, volume):
    result = _z((high-low), 63)
    return _clean(result)

# core02 z 126d
def cg_f10_technology_f10_technology_price_compression_core02_z_126d_base_v013_signal(high, low, closeadj, volume):
    result = _z((_std(closeadj,21)), 126)
    return _clean(result)

# core03 z 252d
def cg_f10_technology_f10_technology_price_compression_core03_z_252d_base_v014_signal(high, low, closeadj, volume):
    result = _z((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), 252)
    return _clean(result)

# core04 z 5d
def cg_f10_technology_f10_technology_price_compression_core04_z_5d_base_v015_signal(high, low, closeadj, volume):
    result = _z(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), 5)
    return _clean(result)

# core05 z 21d
def cg_f10_technology_f10_technology_price_compression_core05_z_21d_base_v016_signal(high, low, closeadj, volume):
    result = _z((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), 21)
    return _clean(result)

# core06 z 63d
def cg_f10_technology_f10_technology_price_compression_core06_z_63d_base_v017_signal(high, low, closeadj, volume):
    result = _z((_std(_pct_change(closeadj,1),21)), 63)
    return _clean(result)

# core07 z 126d
def cg_f10_technology_f10_technology_price_compression_core07_z_126d_base_v018_signal(high, low, closeadj, volume):
    result = _z((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), 126)
    return _clean(result)

# core08 z 252d
def cg_f10_technology_f10_technology_price_compression_core08_z_252d_base_v019_signal(high, low, closeadj, volume):
    result = _z(((_rank(high-low,63)<0.25).astype(float)), 252)
    return _clean(result)

# core09 z 5d
def cg_f10_technology_f10_technology_price_compression_core09_z_5d_base_v020_signal(high, low, closeadj, volume):
    result = _z((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), 5)
    return _clean(result)

# core00 rank 63d
def cg_f10_technology_f10_technology_price_compression_core00_rank_63d_base_v021_signal(high, low, closeadj, volume):
    result = _rank((_safe_div(high-low,closeadj.abs()+1e-9)), 63)
    return _clean(result)

# core01 rank 126d
def cg_f10_technology_f10_technology_price_compression_core01_rank_126d_base_v022_signal(high, low, closeadj, volume):
    result = _rank((high-low), 126)
    return _clean(result)

# core02 rank 252d
def cg_f10_technology_f10_technology_price_compression_core02_rank_252d_base_v023_signal(high, low, closeadj, volume):
    result = _rank((_std(closeadj,21)), 252)
    return _clean(result)

# core03 rank 5d
def cg_f10_technology_f10_technology_price_compression_core03_rank_5d_base_v024_signal(high, low, closeadj, volume):
    result = _rank((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), 5)
    return _clean(result)

# core04 rank 21d
def cg_f10_technology_f10_technology_price_compression_core04_rank_21d_base_v025_signal(high, low, closeadj, volume):
    result = _rank(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), 21)
    return _clean(result)

# core05 rank 63d
def cg_f10_technology_f10_technology_price_compression_core05_rank_63d_base_v026_signal(high, low, closeadj, volume):
    result = _rank((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), 63)
    return _clean(result)

# core06 rank 126d
def cg_f10_technology_f10_technology_price_compression_core06_rank_126d_base_v027_signal(high, low, closeadj, volume):
    result = _rank((_std(_pct_change(closeadj,1),21)), 126)
    return _clean(result)

# core07 rank 252d
def cg_f10_technology_f10_technology_price_compression_core07_rank_252d_base_v028_signal(high, low, closeadj, volume):
    result = _rank((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), 252)
    return _clean(result)

# core08 rank 5d
def cg_f10_technology_f10_technology_price_compression_core08_rank_5d_base_v029_signal(high, low, closeadj, volume):
    result = _rank(((_rank(high-low,63)<0.25).astype(float)), 5)
    return _clean(result)

# core09 rank 21d
def cg_f10_technology_f10_technology_price_compression_core09_rank_21d_base_v030_signal(high, low, closeadj, volume):
    result = _rank((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), 21)
    return _clean(result)

# core00 std 126d
def cg_f10_technology_f10_technology_price_compression_core00_std_126d_base_v031_signal(high, low, closeadj, volume):
    result = _std((_safe_div(high-low,closeadj.abs()+1e-9)), 126)
    return _clean(result)

# core01 std 252d
def cg_f10_technology_f10_technology_price_compression_core01_std_252d_base_v032_signal(high, low, closeadj, volume):
    result = _std((high-low), 252)
    return _clean(result)

# core02 std 5d
def cg_f10_technology_f10_technology_price_compression_core02_std_5d_base_v033_signal(high, low, closeadj, volume):
    result = _std((_std(closeadj,21)), 5)
    return _clean(result)

# core03 std 21d
def cg_f10_technology_f10_technology_price_compression_core03_std_21d_base_v034_signal(high, low, closeadj, volume):
    result = _std((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), 21)
    return _clean(result)

# core04 std 63d
def cg_f10_technology_f10_technology_price_compression_core04_std_63d_base_v035_signal(high, low, closeadj, volume):
    result = _std(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), 63)
    return _clean(result)

# core05 std 126d
def cg_f10_technology_f10_technology_price_compression_core05_std_126d_base_v036_signal(high, low, closeadj, volume):
    result = _std((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), 126)
    return _clean(result)

# core06 std 252d
def cg_f10_technology_f10_technology_price_compression_core06_std_252d_base_v037_signal(high, low, closeadj, volume):
    result = _std((_std(_pct_change(closeadj,1),21)), 252)
    return _clean(result)

# core07 std 5d
def cg_f10_technology_f10_technology_price_compression_core07_std_5d_base_v038_signal(high, low, closeadj, volume):
    result = _std((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), 5)
    return _clean(result)

# core08 std 21d
def cg_f10_technology_f10_technology_price_compression_core08_std_21d_base_v039_signal(high, low, closeadj, volume):
    result = _std(((_rank(high-low,63)<0.25).astype(float)), 21)
    return _clean(result)

# core09 std 63d
def cg_f10_technology_f10_technology_price_compression_core09_std_63d_base_v040_signal(high, low, closeadj, volume):
    result = _std((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), 63)
    return _clean(result)

# core00 slope 252d
def cg_f10_technology_f10_technology_price_compression_core00_slope_252d_base_v041_signal(high, low, closeadj, volume):
    result = _slope((_safe_div(high-low,closeadj.abs()+1e-9)), 252)
    return _clean(result)

# core01 slope 5d
def cg_f10_technology_f10_technology_price_compression_core01_slope_5d_base_v042_signal(high, low, closeadj, volume):
    result = _slope((high-low), 5)
    return _clean(result)

# core02 slope 21d
def cg_f10_technology_f10_technology_price_compression_core02_slope_21d_base_v043_signal(high, low, closeadj, volume):
    result = _slope((_std(closeadj,21)), 21)
    return _clean(result)

# core03 slope 63d
def cg_f10_technology_f10_technology_price_compression_core03_slope_63d_base_v044_signal(high, low, closeadj, volume):
    result = _slope((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), 63)
    return _clean(result)

# core04 slope 126d
def cg_f10_technology_f10_technology_price_compression_core04_slope_126d_base_v045_signal(high, low, closeadj, volume):
    result = _slope(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), 126)
    return _clean(result)

# core05 slope 252d
def cg_f10_technology_f10_technology_price_compression_core05_slope_252d_base_v046_signal(high, low, closeadj, volume):
    result = _slope((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), 252)
    return _clean(result)

# core06 slope 5d
def cg_f10_technology_f10_technology_price_compression_core06_slope_5d_base_v047_signal(high, low, closeadj, volume):
    result = _slope((_std(_pct_change(closeadj,1),21)), 5)
    return _clean(result)

# core07 slope 21d
def cg_f10_technology_f10_technology_price_compression_core07_slope_21d_base_v048_signal(high, low, closeadj, volume):
    result = _slope((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), 21)
    return _clean(result)

# core08 slope 63d
def cg_f10_technology_f10_technology_price_compression_core08_slope_63d_base_v049_signal(high, low, closeadj, volume):
    result = _slope(((_rank(high-low,63)<0.25).astype(float)), 63)
    return _clean(result)

# core09 slope 126d
def cg_f10_technology_f10_technology_price_compression_core09_slope_126d_base_v050_signal(high, low, closeadj, volume):
    result = _slope((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), 126)
    return _clean(result)

# core00 diff 5d
def cg_f10_technology_f10_technology_price_compression_core00_diff_5d_base_v051_signal(high, low, closeadj, volume):
    result = _diff((_safe_div(high-low,closeadj.abs()+1e-9)), 5)
    return _clean(result)

# core01 diff 21d
def cg_f10_technology_f10_technology_price_compression_core01_diff_21d_base_v052_signal(high, low, closeadj, volume):
    result = _diff((high-low), 21)
    return _clean(result)

# core02 diff 63d
def cg_f10_technology_f10_technology_price_compression_core02_diff_63d_base_v053_signal(high, low, closeadj, volume):
    result = _diff((_std(closeadj,21)), 63)
    return _clean(result)

# core03 diff 126d
def cg_f10_technology_f10_technology_price_compression_core03_diff_126d_base_v054_signal(high, low, closeadj, volume):
    result = _diff((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), 126)
    return _clean(result)

# core04 diff 252d
def cg_f10_technology_f10_technology_price_compression_core04_diff_252d_base_v055_signal(high, low, closeadj, volume):
    result = _diff(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), 252)
    return _clean(result)

# core05 diff 5d
def cg_f10_technology_f10_technology_price_compression_core05_diff_5d_base_v056_signal(high, low, closeadj, volume):
    result = _diff((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), 5)
    return _clean(result)

# core06 diff 21d
def cg_f10_technology_f10_technology_price_compression_core06_diff_21d_base_v057_signal(high, low, closeadj, volume):
    result = _diff((_std(_pct_change(closeadj,1),21)), 21)
    return _clean(result)

# core07 diff 63d
def cg_f10_technology_f10_technology_price_compression_core07_diff_63d_base_v058_signal(high, low, closeadj, volume):
    result = _diff((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), 63)
    return _clean(result)

# core08 diff 126d
def cg_f10_technology_f10_technology_price_compression_core08_diff_126d_base_v059_signal(high, low, closeadj, volume):
    result = _diff(((_rank(high-low,63)<0.25).astype(float)), 126)
    return _clean(result)

# core09 diff 252d
def cg_f10_technology_f10_technology_price_compression_core09_diff_252d_base_v060_signal(high, low, closeadj, volume):
    result = _diff((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), 252)
    return _clean(result)

# core00 pct 21d
def cg_f10_technology_f10_technology_price_compression_core00_pct_21d_base_v061_signal(high, low, closeadj, volume):
    result = _pct_change(((_safe_div(high-low,closeadj.abs()+1e-9)).abs()+1.0), 21)
    return _clean(result)

# core01 pct 63d
def cg_f10_technology_f10_technology_price_compression_core01_pct_63d_base_v062_signal(high, low, closeadj, volume):
    result = _pct_change(((high-low).abs()+1.0), 63)
    return _clean(result)

# core02 pct 126d
def cg_f10_technology_f10_technology_price_compression_core02_pct_126d_base_v063_signal(high, low, closeadj, volume):
    result = _pct_change(((_std(closeadj,21)).abs()+1.0), 126)
    return _clean(result)

# core03 pct 252d
def cg_f10_technology_f10_technology_price_compression_core03_pct_252d_base_v064_signal(high, low, closeadj, volume):
    result = _pct_change(((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)).abs()+1.0), 252)
    return _clean(result)

# core04 pct 5d
def cg_f10_technology_f10_technology_price_compression_core04_pct_5d_base_v065_signal(high, low, closeadj, volume):
    result = _pct_change((((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))).abs()+1.0), 5)
    return _clean(result)

# core05 pct 21d
def cg_f10_technology_f10_technology_price_compression_core05_pct_21d_base_v066_signal(high, low, closeadj, volume):
    result = _pct_change(((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)).abs()+1.0), 21)
    return _clean(result)

# core06 pct 63d
def cg_f10_technology_f10_technology_price_compression_core06_pct_63d_base_v067_signal(high, low, closeadj, volume):
    result = _pct_change(((_std(_pct_change(closeadj,1),21)).abs()+1.0), 63)
    return _clean(result)

# core07 pct 126d
def cg_f10_technology_f10_technology_price_compression_core07_pct_126d_base_v068_signal(high, low, closeadj, volume):
    result = _pct_change(((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)).abs()+1.0), 126)
    return _clean(result)

# core08 pct 252d
def cg_f10_technology_f10_technology_price_compression_core08_pct_252d_base_v069_signal(high, low, closeadj, volume):
    result = _pct_change((((_rank(high-low,63)<0.25).astype(float)).abs()+1.0), 252)
    return _clean(result)

# core09 pct 5d
def cg_f10_technology_f10_technology_price_compression_core09_pct_5d_base_v070_signal(high, low, closeadj, volume):
    result = _pct_change(((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)).abs()+1.0), 5)
    return _clean(result)

# core00 ewm 63d
def cg_f10_technology_f10_technology_price_compression_core00_ewm_63d_base_v071_signal(high, low, closeadj, volume):
    result = _ewm((_safe_div(high-low,closeadj.abs()+1e-9)), 63)
    return _clean(result)

# core01 ewm 126d
def cg_f10_technology_f10_technology_price_compression_core01_ewm_126d_base_v072_signal(high, low, closeadj, volume):
    result = _ewm((high-low), 126)
    return _clean(result)

# core02 ewm 252d
def cg_f10_technology_f10_technology_price_compression_core02_ewm_252d_base_v073_signal(high, low, closeadj, volume):
    result = _ewm((_std(closeadj,21)), 252)
    return _clean(result)

# core03 ewm 5d
def cg_f10_technology_f10_technology_price_compression_core03_ewm_5d_base_v074_signal(high, low, closeadj, volume):
    result = _ewm((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), 5)
    return _clean(result)

# core04 ewm 21d
def cg_f10_technology_f10_technology_price_compression_core04_ewm_21d_base_v075_signal(high, low, closeadj, volume):
    result = _ewm(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), 21)
    return _clean(result)

