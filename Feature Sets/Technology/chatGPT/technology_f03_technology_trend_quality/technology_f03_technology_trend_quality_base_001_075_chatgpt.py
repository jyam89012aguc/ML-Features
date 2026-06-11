import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 mean 5d
def cg_f03_technology_f03_technology_trend_quality_core00_mean_5d_base_v001_signal(closeadj, volume):
    result = _mean((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 5)
    return _clean(result)

# core01 mean 21d
def cg_f03_technology_f03_technology_trend_quality_core01_mean_21d_base_v002_signal(closeadj, volume):
    result = _mean((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 21)
    return _clean(result)

# core02 mean 63d
def cg_f03_technology_f03_technology_trend_quality_core02_mean_63d_base_v003_signal(closeadj, volume):
    result = _mean((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 63)
    return _clean(result)

# core03 mean 126d
def cg_f03_technology_f03_technology_trend_quality_core03_mean_126d_base_v004_signal(closeadj, volume):
    result = _mean((_slope(_log(closeadj),21)), 126)
    return _clean(result)

# core04 mean 252d
def cg_f03_technology_f03_technology_trend_quality_core04_mean_252d_base_v005_signal(closeadj, volume):
    result = _mean((_slope(_log(_mean(closeadj,50)),21)), 252)
    return _clean(result)

# core05 mean 5d
def cg_f03_technology_f03_technology_trend_quality_core05_mean_5d_base_v006_signal(closeadj, volume):
    result = _mean((_slope(_log(_mean(closeadj,200)),63)), 5)
    return _clean(result)

# core06 mean 21d
def cg_f03_technology_f03_technology_trend_quality_core06_mean_21d_base_v007_signal(closeadj, volume):
    result = _mean((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 21)
    return _clean(result)

# core07 mean 63d
def cg_f03_technology_f03_technology_trend_quality_core07_mean_63d_base_v008_signal(closeadj, volume):
    result = _mean((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 63)
    return _clean(result)

# core08 mean 126d
def cg_f03_technology_f03_technology_trend_quality_core08_mean_126d_base_v009_signal(closeadj, volume):
    result = _mean((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 126)
    return _clean(result)

# core09 mean 252d
def cg_f03_technology_f03_technology_trend_quality_core09_mean_252d_base_v010_signal(closeadj, volume):
    result = _mean((_z(volume, 63)), 252)
    return _clean(result)

# core00 z 21d
def cg_f03_technology_f03_technology_trend_quality_core00_z_21d_base_v011_signal(closeadj, volume):
    result = _z((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 21)
    return _clean(result)

# core01 z 63d
def cg_f03_technology_f03_technology_trend_quality_core01_z_63d_base_v012_signal(closeadj, volume):
    result = _z((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 63)
    return _clean(result)

# core02 z 126d
def cg_f03_technology_f03_technology_trend_quality_core02_z_126d_base_v013_signal(closeadj, volume):
    result = _z((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 126)
    return _clean(result)

# core03 z 252d
def cg_f03_technology_f03_technology_trend_quality_core03_z_252d_base_v014_signal(closeadj, volume):
    result = _z((_slope(_log(closeadj),21)), 252)
    return _clean(result)

# core04 z 5d
def cg_f03_technology_f03_technology_trend_quality_core04_z_5d_base_v015_signal(closeadj, volume):
    result = _z((_slope(_log(_mean(closeadj,50)),21)), 5)
    return _clean(result)

# core05 z 21d
def cg_f03_technology_f03_technology_trend_quality_core05_z_21d_base_v016_signal(closeadj, volume):
    result = _z((_slope(_log(_mean(closeadj,200)),63)), 21)
    return _clean(result)

# core06 z 63d
def cg_f03_technology_f03_technology_trend_quality_core06_z_63d_base_v017_signal(closeadj, volume):
    result = _z((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 63)
    return _clean(result)

# core07 z 126d
def cg_f03_technology_f03_technology_trend_quality_core07_z_126d_base_v018_signal(closeadj, volume):
    result = _z((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 126)
    return _clean(result)

# core08 z 252d
def cg_f03_technology_f03_technology_trend_quality_core08_z_252d_base_v019_signal(closeadj, volume):
    result = _z((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 252)
    return _clean(result)

# core09 z 5d
def cg_f03_technology_f03_technology_trend_quality_core09_z_5d_base_v020_signal(closeadj, volume):
    result = _z((_z(volume, 63)), 5)
    return _clean(result)

# core00 rank 63d
def cg_f03_technology_f03_technology_trend_quality_core00_rank_63d_base_v021_signal(closeadj, volume):
    result = _rank((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 63)
    return _clean(result)

# core01 rank 126d
def cg_f03_technology_f03_technology_trend_quality_core01_rank_126d_base_v022_signal(closeadj, volume):
    result = _rank((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 126)
    return _clean(result)

# core02 rank 252d
def cg_f03_technology_f03_technology_trend_quality_core02_rank_252d_base_v023_signal(closeadj, volume):
    result = _rank((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 252)
    return _clean(result)

# core03 rank 5d
def cg_f03_technology_f03_technology_trend_quality_core03_rank_5d_base_v024_signal(closeadj, volume):
    result = _rank((_slope(_log(closeadj),21)), 5)
    return _clean(result)

# core04 rank 21d
def cg_f03_technology_f03_technology_trend_quality_core04_rank_21d_base_v025_signal(closeadj, volume):
    result = _rank((_slope(_log(_mean(closeadj,50)),21)), 21)
    return _clean(result)

# core05 rank 63d
def cg_f03_technology_f03_technology_trend_quality_core05_rank_63d_base_v026_signal(closeadj, volume):
    result = _rank((_slope(_log(_mean(closeadj,200)),63)), 63)
    return _clean(result)

# core06 rank 126d
def cg_f03_technology_f03_technology_trend_quality_core06_rank_126d_base_v027_signal(closeadj, volume):
    result = _rank((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 126)
    return _clean(result)

# core07 rank 252d
def cg_f03_technology_f03_technology_trend_quality_core07_rank_252d_base_v028_signal(closeadj, volume):
    result = _rank((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 252)
    return _clean(result)

# core08 rank 5d
def cg_f03_technology_f03_technology_trend_quality_core08_rank_5d_base_v029_signal(closeadj, volume):
    result = _rank((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 5)
    return _clean(result)

# core09 rank 21d
def cg_f03_technology_f03_technology_trend_quality_core09_rank_21d_base_v030_signal(closeadj, volume):
    result = _rank((_z(volume, 63)), 21)
    return _clean(result)

# core00 std 126d
def cg_f03_technology_f03_technology_trend_quality_core00_std_126d_base_v031_signal(closeadj, volume):
    result = _std((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 126)
    return _clean(result)

# core01 std 252d
def cg_f03_technology_f03_technology_trend_quality_core01_std_252d_base_v032_signal(closeadj, volume):
    result = _std((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 252)
    return _clean(result)

# core02 std 5d
def cg_f03_technology_f03_technology_trend_quality_core02_std_5d_base_v033_signal(closeadj, volume):
    result = _std((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 5)
    return _clean(result)

# core03 std 21d
def cg_f03_technology_f03_technology_trend_quality_core03_std_21d_base_v034_signal(closeadj, volume):
    result = _std((_slope(_log(closeadj),21)), 21)
    return _clean(result)

# core04 std 63d
def cg_f03_technology_f03_technology_trend_quality_core04_std_63d_base_v035_signal(closeadj, volume):
    result = _std((_slope(_log(_mean(closeadj,50)),21)), 63)
    return _clean(result)

# core05 std 126d
def cg_f03_technology_f03_technology_trend_quality_core05_std_126d_base_v036_signal(closeadj, volume):
    result = _std((_slope(_log(_mean(closeadj,200)),63)), 126)
    return _clean(result)

# core06 std 252d
def cg_f03_technology_f03_technology_trend_quality_core06_std_252d_base_v037_signal(closeadj, volume):
    result = _std((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 252)
    return _clean(result)

# core07 std 5d
def cg_f03_technology_f03_technology_trend_quality_core07_std_5d_base_v038_signal(closeadj, volume):
    result = _std((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 5)
    return _clean(result)

# core08 std 21d
def cg_f03_technology_f03_technology_trend_quality_core08_std_21d_base_v039_signal(closeadj, volume):
    result = _std((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 21)
    return _clean(result)

# core09 std 63d
def cg_f03_technology_f03_technology_trend_quality_core09_std_63d_base_v040_signal(closeadj, volume):
    result = _std((_z(volume, 63)), 63)
    return _clean(result)

# core00 slope 252d
def cg_f03_technology_f03_technology_trend_quality_core00_slope_252d_base_v041_signal(closeadj, volume):
    result = _slope((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 252)
    return _clean(result)

# core01 slope 5d
def cg_f03_technology_f03_technology_trend_quality_core01_slope_5d_base_v042_signal(closeadj, volume):
    result = _slope((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 5)
    return _clean(result)

# core02 slope 21d
def cg_f03_technology_f03_technology_trend_quality_core02_slope_21d_base_v043_signal(closeadj, volume):
    result = _slope((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 21)
    return _clean(result)

# core03 slope 63d
def cg_f03_technology_f03_technology_trend_quality_core03_slope_63d_base_v044_signal(closeadj, volume):
    result = _slope((_slope(_log(closeadj),21)), 63)
    return _clean(result)

# core04 slope 126d
def cg_f03_technology_f03_technology_trend_quality_core04_slope_126d_base_v045_signal(closeadj, volume):
    result = _slope((_slope(_log(_mean(closeadj,50)),21)), 126)
    return _clean(result)

# core05 slope 252d
def cg_f03_technology_f03_technology_trend_quality_core05_slope_252d_base_v046_signal(closeadj, volume):
    result = _slope((_slope(_log(_mean(closeadj,200)),63)), 252)
    return _clean(result)

# core06 slope 5d
def cg_f03_technology_f03_technology_trend_quality_core06_slope_5d_base_v047_signal(closeadj, volume):
    result = _slope((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 5)
    return _clean(result)

# core07 slope 21d
def cg_f03_technology_f03_technology_trend_quality_core07_slope_21d_base_v048_signal(closeadj, volume):
    result = _slope((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 21)
    return _clean(result)

# core08 slope 63d
def cg_f03_technology_f03_technology_trend_quality_core08_slope_63d_base_v049_signal(closeadj, volume):
    result = _slope((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 63)
    return _clean(result)

# core09 slope 126d
def cg_f03_technology_f03_technology_trend_quality_core09_slope_126d_base_v050_signal(closeadj, volume):
    result = _slope((_z(volume, 63)), 126)
    return _clean(result)

# core00 diff 5d
def cg_f03_technology_f03_technology_trend_quality_core00_diff_5d_base_v051_signal(closeadj, volume):
    result = _diff((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 5)
    return _clean(result)

# core01 diff 21d
def cg_f03_technology_f03_technology_trend_quality_core01_diff_21d_base_v052_signal(closeadj, volume):
    result = _diff((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 21)
    return _clean(result)

# core02 diff 63d
def cg_f03_technology_f03_technology_trend_quality_core02_diff_63d_base_v053_signal(closeadj, volume):
    result = _diff((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 63)
    return _clean(result)

# core03 diff 126d
def cg_f03_technology_f03_technology_trend_quality_core03_diff_126d_base_v054_signal(closeadj, volume):
    result = _diff((_slope(_log(closeadj),21)), 126)
    return _clean(result)

# core04 diff 252d
def cg_f03_technology_f03_technology_trend_quality_core04_diff_252d_base_v055_signal(closeadj, volume):
    result = _diff((_slope(_log(_mean(closeadj,50)),21)), 252)
    return _clean(result)

# core05 diff 5d
def cg_f03_technology_f03_technology_trend_quality_core05_diff_5d_base_v056_signal(closeadj, volume):
    result = _diff((_slope(_log(_mean(closeadj,200)),63)), 5)
    return _clean(result)

# core06 diff 21d
def cg_f03_technology_f03_technology_trend_quality_core06_diff_21d_base_v057_signal(closeadj, volume):
    result = _diff((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 21)
    return _clean(result)

# core07 diff 63d
def cg_f03_technology_f03_technology_trend_quality_core07_diff_63d_base_v058_signal(closeadj, volume):
    result = _diff((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 63)
    return _clean(result)

# core08 diff 126d
def cg_f03_technology_f03_technology_trend_quality_core08_diff_126d_base_v059_signal(closeadj, volume):
    result = _diff((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 126)
    return _clean(result)

# core09 diff 252d
def cg_f03_technology_f03_technology_trend_quality_core09_diff_252d_base_v060_signal(closeadj, volume):
    result = _diff((_z(volume, 63)), 252)
    return _clean(result)

# core00 pct 21d
def cg_f03_technology_f03_technology_trend_quality_core00_pct_21d_base_v061_signal(closeadj, volume):
    result = _pct_change(((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)).abs()+1.0), 21)
    return _clean(result)

# core01 pct 63d
def cg_f03_technology_f03_technology_trend_quality_core01_pct_63d_base_v062_signal(closeadj, volume):
    result = _pct_change(((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)).abs()+1.0), 63)
    return _clean(result)

# core02 pct 126d
def cg_f03_technology_f03_technology_trend_quality_core02_pct_126d_base_v063_signal(closeadj, volume):
    result = _pct_change(((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0).abs()+1.0), 126)
    return _clean(result)

# core03 pct 252d
def cg_f03_technology_f03_technology_trend_quality_core03_pct_252d_base_v064_signal(closeadj, volume):
    result = _pct_change(((_slope(_log(closeadj),21)).abs()+1.0), 252)
    return _clean(result)

# core04 pct 5d
def cg_f03_technology_f03_technology_trend_quality_core04_pct_5d_base_v065_signal(closeadj, volume):
    result = _pct_change(((_slope(_log(_mean(closeadj,50)),21)).abs()+1.0), 5)
    return _clean(result)

# core05 pct 21d
def cg_f03_technology_f03_technology_trend_quality_core05_pct_21d_base_v066_signal(closeadj, volume):
    result = _pct_change(((_slope(_log(_mean(closeadj,200)),63)).abs()+1.0), 21)
    return _clean(result)

# core06 pct 63d
def cg_f03_technology_f03_technology_trend_quality_core06_pct_63d_base_v067_signal(closeadj, volume):
    result = _pct_change(((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)).abs()+1.0), 63)
    return _clean(result)

# core07 pct 126d
def cg_f03_technology_f03_technology_trend_quality_core07_pct_126d_base_v068_signal(closeadj, volume):
    result = _pct_change(((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)).abs()+1.0), 126)
    return _clean(result)

# core08 pct 252d
def cg_f03_technology_f03_technology_trend_quality_core08_pct_252d_base_v069_signal(closeadj, volume):
    result = _pct_change(((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)).abs()+1.0), 252)
    return _clean(result)

# core09 pct 5d
def cg_f03_technology_f03_technology_trend_quality_core09_pct_5d_base_v070_signal(closeadj, volume):
    result = _pct_change(((_z(volume, 63)).abs()+1.0), 5)
    return _clean(result)

# core00 ewm 63d
def cg_f03_technology_f03_technology_trend_quality_core00_ewm_63d_base_v071_signal(closeadj, volume):
    result = _ewm((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 63)
    return _clean(result)

# core01 ewm 126d
def cg_f03_technology_f03_technology_trend_quality_core01_ewm_126d_base_v072_signal(closeadj, volume):
    result = _ewm((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 126)
    return _clean(result)

# core02 ewm 252d
def cg_f03_technology_f03_technology_trend_quality_core02_ewm_252d_base_v073_signal(closeadj, volume):
    result = _ewm((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 252)
    return _clean(result)

# core03 ewm 5d
def cg_f03_technology_f03_technology_trend_quality_core03_ewm_5d_base_v074_signal(closeadj, volume):
    result = _ewm((_slope(_log(closeadj),21)), 5)
    return _clean(result)

# core04 ewm 21d
def cg_f03_technology_f03_technology_trend_quality_core04_ewm_21d_base_v075_signal(closeadj, volume):
    result = _ewm((_slope(_log(_mean(closeadj,50)),21)), 21)
    return _clean(result)

