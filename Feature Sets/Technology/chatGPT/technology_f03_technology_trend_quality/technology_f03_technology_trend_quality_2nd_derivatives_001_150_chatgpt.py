import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 slope mean 5d
def cg_f03_technology_f03_technology_trend_quality_core00_mean_5d_slope_v001_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f03_technology_f03_technology_trend_quality_core01_mean_21d_slope_v002_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f03_technology_f03_technology_trend_quality_core02_mean_63d_slope_v003_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f03_technology_f03_technology_trend_quality_core03_mean_126d_slope_v004_signal(closeadj, volume):
    base = _mean((_slope(_log(closeadj),21)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f03_technology_f03_technology_trend_quality_core04_mean_252d_slope_v005_signal(closeadj, volume):
    base = _mean((_slope(_log(_mean(closeadj,50)),21)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f03_technology_f03_technology_trend_quality_core05_mean_5d_slope_v006_signal(closeadj, volume):
    base = _mean((_slope(_log(_mean(closeadj,200)),63)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f03_technology_f03_technology_trend_quality_core06_mean_21d_slope_v007_signal(closeadj, volume):
    base = _mean((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f03_technology_f03_technology_trend_quality_core07_mean_63d_slope_v008_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f03_technology_f03_technology_trend_quality_core08_mean_126d_slope_v009_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f03_technology_f03_technology_trend_quality_core09_mean_252d_slope_v010_signal(closeadj, volume):
    base = _mean((_z(volume, 63)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope z 21d
def cg_f03_technology_f03_technology_trend_quality_core00_z_21d_slope_v011_signal(closeadj, volume):
    base = _z((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope z 63d
def cg_f03_technology_f03_technology_trend_quality_core01_z_63d_slope_v012_signal(closeadj, volume):
    base = _z((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope z 126d
def cg_f03_technology_f03_technology_trend_quality_core02_z_126d_slope_v013_signal(closeadj, volume):
    base = _z((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope z 252d
def cg_f03_technology_f03_technology_trend_quality_core03_z_252d_slope_v014_signal(closeadj, volume):
    base = _z((_slope(_log(closeadj),21)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope z 5d
def cg_f03_technology_f03_technology_trend_quality_core04_z_5d_slope_v015_signal(closeadj, volume):
    base = _z((_slope(_log(_mean(closeadj,50)),21)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope z 21d
def cg_f03_technology_f03_technology_trend_quality_core05_z_21d_slope_v016_signal(closeadj, volume):
    base = _z((_slope(_log(_mean(closeadj,200)),63)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope z 63d
def cg_f03_technology_f03_technology_trend_quality_core06_z_63d_slope_v017_signal(closeadj, volume):
    base = _z((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope z 126d
def cg_f03_technology_f03_technology_trend_quality_core07_z_126d_slope_v018_signal(closeadj, volume):
    base = _z((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope z 252d
def cg_f03_technology_f03_technology_trend_quality_core08_z_252d_slope_v019_signal(closeadj, volume):
    base = _z((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope z 5d
def cg_f03_technology_f03_technology_trend_quality_core09_z_5d_slope_v020_signal(closeadj, volume):
    base = _z((_z(volume, 63)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope rank 63d
def cg_f03_technology_f03_technology_trend_quality_core00_rank_63d_slope_v021_signal(closeadj, volume):
    base = _rank((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope rank 126d
def cg_f03_technology_f03_technology_trend_quality_core01_rank_126d_slope_v022_signal(closeadj, volume):
    base = _rank((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope rank 252d
def cg_f03_technology_f03_technology_trend_quality_core02_rank_252d_slope_v023_signal(closeadj, volume):
    base = _rank((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope rank 5d
def cg_f03_technology_f03_technology_trend_quality_core03_rank_5d_slope_v024_signal(closeadj, volume):
    base = _rank((_slope(_log(closeadj),21)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope rank 21d
def cg_f03_technology_f03_technology_trend_quality_core04_rank_21d_slope_v025_signal(closeadj, volume):
    base = _rank((_slope(_log(_mean(closeadj,50)),21)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope rank 63d
def cg_f03_technology_f03_technology_trend_quality_core05_rank_63d_slope_v026_signal(closeadj, volume):
    base = _rank((_slope(_log(_mean(closeadj,200)),63)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope rank 126d
def cg_f03_technology_f03_technology_trend_quality_core06_rank_126d_slope_v027_signal(closeadj, volume):
    base = _rank((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope rank 252d
def cg_f03_technology_f03_technology_trend_quality_core07_rank_252d_slope_v028_signal(closeadj, volume):
    base = _rank((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope rank 5d
def cg_f03_technology_f03_technology_trend_quality_core08_rank_5d_slope_v029_signal(closeadj, volume):
    base = _rank((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope rank 21d
def cg_f03_technology_f03_technology_trend_quality_core09_rank_21d_slope_v030_signal(closeadj, volume):
    base = _rank((_z(volume, 63)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope std 126d
def cg_f03_technology_f03_technology_trend_quality_core00_std_126d_slope_v031_signal(closeadj, volume):
    base = _std((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope std 252d
def cg_f03_technology_f03_technology_trend_quality_core01_std_252d_slope_v032_signal(closeadj, volume):
    base = _std((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope std 5d
def cg_f03_technology_f03_technology_trend_quality_core02_std_5d_slope_v033_signal(closeadj, volume):
    base = _std((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope std 21d
def cg_f03_technology_f03_technology_trend_quality_core03_std_21d_slope_v034_signal(closeadj, volume):
    base = _std((_slope(_log(closeadj),21)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope std 63d
def cg_f03_technology_f03_technology_trend_quality_core04_std_63d_slope_v035_signal(closeadj, volume):
    base = _std((_slope(_log(_mean(closeadj,50)),21)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope std 126d
def cg_f03_technology_f03_technology_trend_quality_core05_std_126d_slope_v036_signal(closeadj, volume):
    base = _std((_slope(_log(_mean(closeadj,200)),63)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope std 252d
def cg_f03_technology_f03_technology_trend_quality_core06_std_252d_slope_v037_signal(closeadj, volume):
    base = _std((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope std 5d
def cg_f03_technology_f03_technology_trend_quality_core07_std_5d_slope_v038_signal(closeadj, volume):
    base = _std((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope std 21d
def cg_f03_technology_f03_technology_trend_quality_core08_std_21d_slope_v039_signal(closeadj, volume):
    base = _std((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope std 63d
def cg_f03_technology_f03_technology_trend_quality_core09_std_63d_slope_v040_signal(closeadj, volume):
    base = _std((_z(volume, 63)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope slope 252d
def cg_f03_technology_f03_technology_trend_quality_core00_slope_252d_slope_v041_signal(closeadj, volume):
    base = _slope((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope slope 5d
def cg_f03_technology_f03_technology_trend_quality_core01_slope_5d_slope_v042_signal(closeadj, volume):
    base = _slope((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope slope 21d
def cg_f03_technology_f03_technology_trend_quality_core02_slope_21d_slope_v043_signal(closeadj, volume):
    base = _slope((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope slope 63d
def cg_f03_technology_f03_technology_trend_quality_core03_slope_63d_slope_v044_signal(closeadj, volume):
    base = _slope((_slope(_log(closeadj),21)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope slope 126d
def cg_f03_technology_f03_technology_trend_quality_core04_slope_126d_slope_v045_signal(closeadj, volume):
    base = _slope((_slope(_log(_mean(closeadj,50)),21)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope slope 252d
def cg_f03_technology_f03_technology_trend_quality_core05_slope_252d_slope_v046_signal(closeadj, volume):
    base = _slope((_slope(_log(_mean(closeadj,200)),63)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope slope 5d
def cg_f03_technology_f03_technology_trend_quality_core06_slope_5d_slope_v047_signal(closeadj, volume):
    base = _slope((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope slope 21d
def cg_f03_technology_f03_technology_trend_quality_core07_slope_21d_slope_v048_signal(closeadj, volume):
    base = _slope((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope slope 63d
def cg_f03_technology_f03_technology_trend_quality_core08_slope_63d_slope_v049_signal(closeadj, volume):
    base = _slope((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope slope 126d
def cg_f03_technology_f03_technology_trend_quality_core09_slope_126d_slope_v050_signal(closeadj, volume):
    base = _slope((_z(volume, 63)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope diff 5d
def cg_f03_technology_f03_technology_trend_quality_core00_diff_5d_slope_v051_signal(closeadj, volume):
    base = _diff((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope diff 21d
def cg_f03_technology_f03_technology_trend_quality_core01_diff_21d_slope_v052_signal(closeadj, volume):
    base = _diff((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope diff 63d
def cg_f03_technology_f03_technology_trend_quality_core02_diff_63d_slope_v053_signal(closeadj, volume):
    base = _diff((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope diff 126d
def cg_f03_technology_f03_technology_trend_quality_core03_diff_126d_slope_v054_signal(closeadj, volume):
    base = _diff((_slope(_log(closeadj),21)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope diff 252d
def cg_f03_technology_f03_technology_trend_quality_core04_diff_252d_slope_v055_signal(closeadj, volume):
    base = _diff((_slope(_log(_mean(closeadj,50)),21)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope diff 5d
def cg_f03_technology_f03_technology_trend_quality_core05_diff_5d_slope_v056_signal(closeadj, volume):
    base = _diff((_slope(_log(_mean(closeadj,200)),63)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope diff 21d
def cg_f03_technology_f03_technology_trend_quality_core06_diff_21d_slope_v057_signal(closeadj, volume):
    base = _diff((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope diff 63d
def cg_f03_technology_f03_technology_trend_quality_core07_diff_63d_slope_v058_signal(closeadj, volume):
    base = _diff((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope diff 126d
def cg_f03_technology_f03_technology_trend_quality_core08_diff_126d_slope_v059_signal(closeadj, volume):
    base = _diff((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope diff 252d
def cg_f03_technology_f03_technology_trend_quality_core09_diff_252d_slope_v060_signal(closeadj, volume):
    base = _diff((_z(volume, 63)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope pct 21d
def cg_f03_technology_f03_technology_trend_quality_core00_pct_21d_slope_v061_signal(closeadj, volume):
    base = _pct_change(((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)).abs()+1.0), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope pct 63d
def cg_f03_technology_f03_technology_trend_quality_core01_pct_63d_slope_v062_signal(closeadj, volume):
    base = _pct_change(((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)).abs()+1.0), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope pct 126d
def cg_f03_technology_f03_technology_trend_quality_core02_pct_126d_slope_v063_signal(closeadj, volume):
    base = _pct_change(((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0).abs()+1.0), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope pct 252d
def cg_f03_technology_f03_technology_trend_quality_core03_pct_252d_slope_v064_signal(closeadj, volume):
    base = _pct_change(((_slope(_log(closeadj),21)).abs()+1.0), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope pct 5d
def cg_f03_technology_f03_technology_trend_quality_core04_pct_5d_slope_v065_signal(closeadj, volume):
    base = _pct_change(((_slope(_log(_mean(closeadj,50)),21)).abs()+1.0), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope pct 21d
def cg_f03_technology_f03_technology_trend_quality_core05_pct_21d_slope_v066_signal(closeadj, volume):
    base = _pct_change(((_slope(_log(_mean(closeadj,200)),63)).abs()+1.0), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope pct 63d
def cg_f03_technology_f03_technology_trend_quality_core06_pct_63d_slope_v067_signal(closeadj, volume):
    base = _pct_change(((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)).abs()+1.0), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope pct 126d
def cg_f03_technology_f03_technology_trend_quality_core07_pct_126d_slope_v068_signal(closeadj, volume):
    base = _pct_change(((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)).abs()+1.0), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope pct 252d
def cg_f03_technology_f03_technology_trend_quality_core08_pct_252d_slope_v069_signal(closeadj, volume):
    base = _pct_change(((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)).abs()+1.0), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope pct 5d
def cg_f03_technology_f03_technology_trend_quality_core09_pct_5d_slope_v070_signal(closeadj, volume):
    base = _pct_change(((_z(volume, 63)).abs()+1.0), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 63d
def cg_f03_technology_f03_technology_trend_quality_core00_ewm_63d_slope_v071_signal(closeadj, volume):
    base = _ewm((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 126d
def cg_f03_technology_f03_technology_trend_quality_core01_ewm_126d_slope_v072_signal(closeadj, volume):
    base = _ewm((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 252d
def cg_f03_technology_f03_technology_trend_quality_core02_ewm_252d_slope_v073_signal(closeadj, volume):
    base = _ewm((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 5d
def cg_f03_technology_f03_technology_trend_quality_core03_ewm_5d_slope_v074_signal(closeadj, volume):
    base = _ewm((_slope(_log(closeadj),21)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 21d
def cg_f03_technology_f03_technology_trend_quality_core04_ewm_21d_slope_v075_signal(closeadj, volume):
    base = _ewm((_slope(_log(_mean(closeadj,50)),21)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 63d
def cg_f03_technology_f03_technology_trend_quality_core05_ewm_63d_slope_v076_signal(closeadj, volume):
    base = _ewm((_slope(_log(_mean(closeadj,200)),63)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 126d
def cg_f03_technology_f03_technology_trend_quality_core06_ewm_126d_slope_v077_signal(closeadj, volume):
    base = _ewm((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 252d
def cg_f03_technology_f03_technology_trend_quality_core07_ewm_252d_slope_v078_signal(closeadj, volume):
    base = _ewm((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 5d
def cg_f03_technology_f03_technology_trend_quality_core08_ewm_5d_slope_v079_signal(closeadj, volume):
    base = _ewm((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 21d
def cg_f03_technology_f03_technology_trend_quality_core09_ewm_21d_slope_v080_signal(closeadj, volume):
    base = _ewm((_z(volume, 63)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope skew 126d
def cg_f03_technology_f03_technology_trend_quality_core00_skew_126d_slope_v081_signal(closeadj, volume):
    base = _skew((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope skew 252d
def cg_f03_technology_f03_technology_trend_quality_core01_skew_252d_slope_v082_signal(closeadj, volume):
    base = _skew((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope skew 5d
def cg_f03_technology_f03_technology_trend_quality_core02_skew_5d_slope_v083_signal(closeadj, volume):
    base = _skew((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope skew 21d
def cg_f03_technology_f03_technology_trend_quality_core03_skew_21d_slope_v084_signal(closeadj, volume):
    base = _skew((_slope(_log(closeadj),21)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope skew 63d
def cg_f03_technology_f03_technology_trend_quality_core04_skew_63d_slope_v085_signal(closeadj, volume):
    base = _skew((_slope(_log(_mean(closeadj,50)),21)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope skew 126d
def cg_f03_technology_f03_technology_trend_quality_core05_skew_126d_slope_v086_signal(closeadj, volume):
    base = _skew((_slope(_log(_mean(closeadj,200)),63)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope skew 252d
def cg_f03_technology_f03_technology_trend_quality_core06_skew_252d_slope_v087_signal(closeadj, volume):
    base = _skew((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope skew 5d
def cg_f03_technology_f03_technology_trend_quality_core07_skew_5d_slope_v088_signal(closeadj, volume):
    base = _skew((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope skew 21d
def cg_f03_technology_f03_technology_trend_quality_core08_skew_21d_slope_v089_signal(closeadj, volume):
    base = _skew((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope skew 63d
def cg_f03_technology_f03_technology_trend_quality_core09_skew_63d_slope_v090_signal(closeadj, volume):
    base = _skew((_z(volume, 63)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope kurt 252d
def cg_f03_technology_f03_technology_trend_quality_core00_kurt_252d_slope_v091_signal(closeadj, volume):
    base = _kurt((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope kurt 5d
def cg_f03_technology_f03_technology_trend_quality_core01_kurt_5d_slope_v092_signal(closeadj, volume):
    base = _kurt((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope kurt 21d
def cg_f03_technology_f03_technology_trend_quality_core02_kurt_21d_slope_v093_signal(closeadj, volume):
    base = _kurt((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope kurt 63d
def cg_f03_technology_f03_technology_trend_quality_core03_kurt_63d_slope_v094_signal(closeadj, volume):
    base = _kurt((_slope(_log(closeadj),21)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope kurt 126d
def cg_f03_technology_f03_technology_trend_quality_core04_kurt_126d_slope_v095_signal(closeadj, volume):
    base = _kurt((_slope(_log(_mean(closeadj,50)),21)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope kurt 252d
def cg_f03_technology_f03_technology_trend_quality_core05_kurt_252d_slope_v096_signal(closeadj, volume):
    base = _kurt((_slope(_log(_mean(closeadj,200)),63)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope kurt 5d
def cg_f03_technology_f03_technology_trend_quality_core06_kurt_5d_slope_v097_signal(closeadj, volume):
    base = _kurt((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope kurt 21d
def cg_f03_technology_f03_technology_trend_quality_core07_kurt_21d_slope_v098_signal(closeadj, volume):
    base = _kurt((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope kurt 63d
def cg_f03_technology_f03_technology_trend_quality_core08_kurt_63d_slope_v099_signal(closeadj, volume):
    base = _kurt((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope kurt 126d
def cg_f03_technology_f03_technology_trend_quality_core09_kurt_126d_slope_v100_signal(closeadj, volume):
    base = _kurt((_z(volume, 63)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope autocorr 5d
def cg_f03_technology_f03_technology_trend_quality_core00_autocorr_5d_slope_v101_signal(closeadj, volume):
    base = _autocorr((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope autocorr 21d
def cg_f03_technology_f03_technology_trend_quality_core01_autocorr_21d_slope_v102_signal(closeadj, volume):
    base = _autocorr((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope autocorr 63d
def cg_f03_technology_f03_technology_trend_quality_core02_autocorr_63d_slope_v103_signal(closeadj, volume):
    base = _autocorr((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope autocorr 126d
def cg_f03_technology_f03_technology_trend_quality_core03_autocorr_126d_slope_v104_signal(closeadj, volume):
    base = _autocorr((_slope(_log(closeadj),21)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope autocorr 252d
def cg_f03_technology_f03_technology_trend_quality_core04_autocorr_252d_slope_v105_signal(closeadj, volume):
    base = _autocorr((_slope(_log(_mean(closeadj,50)),21)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope autocorr 5d
def cg_f03_technology_f03_technology_trend_quality_core05_autocorr_5d_slope_v106_signal(closeadj, volume):
    base = _autocorr((_slope(_log(_mean(closeadj,200)),63)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope autocorr 21d
def cg_f03_technology_f03_technology_trend_quality_core06_autocorr_21d_slope_v107_signal(closeadj, volume):
    base = _autocorr((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope autocorr 63d
def cg_f03_technology_f03_technology_trend_quality_core07_autocorr_63d_slope_v108_signal(closeadj, volume):
    base = _autocorr((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope autocorr 126d
def cg_f03_technology_f03_technology_trend_quality_core08_autocorr_126d_slope_v109_signal(closeadj, volume):
    base = _autocorr((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope autocorr 252d
def cg_f03_technology_f03_technology_trend_quality_core09_autocorr_252d_slope_v110_signal(closeadj, volume):
    base = _autocorr((_z(volume, 63)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope snr 21d
def cg_f03_technology_f03_technology_trend_quality_core00_snr_21d_slope_v111_signal(closeadj, volume):
    base = _safe_div(_diff((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), max(1, 21//3)).abs(), _std(_diff((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)),1), 21)+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope snr 63d
def cg_f03_technology_f03_technology_trend_quality_core01_snr_63d_slope_v112_signal(closeadj, volume):
    base = _safe_div(_diff((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), max(1, 63//3)).abs(), _std(_diff((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)),1), 63)+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope snr 126d
def cg_f03_technology_f03_technology_trend_quality_core02_snr_126d_slope_v113_signal(closeadj, volume):
    base = _safe_div(_diff((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), max(1, 126//3)).abs(), _std(_diff((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0),1), 126)+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope snr 252d
def cg_f03_technology_f03_technology_trend_quality_core03_snr_252d_slope_v114_signal(closeadj, volume):
    base = _safe_div(_diff((_slope(_log(closeadj),21)), max(1, 252//3)).abs(), _std(_diff((_slope(_log(closeadj),21)),1), 252)+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope snr 5d
def cg_f03_technology_f03_technology_trend_quality_core04_snr_5d_slope_v115_signal(closeadj, volume):
    base = _safe_div(_diff((_slope(_log(_mean(closeadj,50)),21)), max(1, 5//3)).abs(), _std(_diff((_slope(_log(_mean(closeadj,50)),21)),1), 5)+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope snr 21d
def cg_f03_technology_f03_technology_trend_quality_core05_snr_21d_slope_v116_signal(closeadj, volume):
    base = _safe_div(_diff((_slope(_log(_mean(closeadj,200)),63)), max(1, 21//3)).abs(), _std(_diff((_slope(_log(_mean(closeadj,200)),63)),1), 21)+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope snr 63d
def cg_f03_technology_f03_technology_trend_quality_core06_snr_63d_slope_v117_signal(closeadj, volume):
    base = _safe_div(_diff((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), max(1, 63//3)).abs(), _std(_diff((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)),1), 63)+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope snr 126d
def cg_f03_technology_f03_technology_trend_quality_core07_snr_126d_slope_v118_signal(closeadj, volume):
    base = _safe_div(_diff((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), max(1, 126//3)).abs(), _std(_diff((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)),1), 126)+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope snr 252d
def cg_f03_technology_f03_technology_trend_quality_core08_snr_252d_slope_v119_signal(closeadj, volume):
    base = _safe_div(_diff((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), max(1, 252//3)).abs(), _std(_diff((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)),1), 252)+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope snr 5d
def cg_f03_technology_f03_technology_trend_quality_core09_snr_5d_slope_v120_signal(closeadj, volume):
    base = _safe_div(_diff((_z(volume, 63)), max(1, 5//3)).abs(), _std(_diff((_z(volume, 63)),1), 5)+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope ema_gap 63d
def cg_f03_technology_f03_technology_trend_quality_core00_ema_gap_63d_slope_v121_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 63) - _ewm((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope ema_gap 126d
def cg_f03_technology_f03_technology_trend_quality_core01_ema_gap_126d_slope_v122_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 126) - _ewm((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope ema_gap 252d
def cg_f03_technology_f03_technology_trend_quality_core02_ema_gap_252d_slope_v123_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 252) - _ewm((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope ema_gap 5d
def cg_f03_technology_f03_technology_trend_quality_core03_ema_gap_5d_slope_v124_signal(closeadj, volume):
    base = _mean((_slope(_log(closeadj),21)), 5) - _ewm((_slope(_log(closeadj),21)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope ema_gap 21d
def cg_f03_technology_f03_technology_trend_quality_core04_ema_gap_21d_slope_v125_signal(closeadj, volume):
    base = _mean((_slope(_log(_mean(closeadj,50)),21)), 21) - _ewm((_slope(_log(_mean(closeadj,50)),21)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope ema_gap 63d
def cg_f03_technology_f03_technology_trend_quality_core05_ema_gap_63d_slope_v126_signal(closeadj, volume):
    base = _mean((_slope(_log(_mean(closeadj,200)),63)), 63) - _ewm((_slope(_log(_mean(closeadj,200)),63)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope ema_gap 126d
def cg_f03_technology_f03_technology_trend_quality_core06_ema_gap_126d_slope_v127_signal(closeadj, volume):
    base = _mean((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 126) - _ewm((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope ema_gap 252d
def cg_f03_technology_f03_technology_trend_quality_core07_ema_gap_252d_slope_v128_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 252) - _ewm((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope ema_gap 5d
def cg_f03_technology_f03_technology_trend_quality_core08_ema_gap_5d_slope_v129_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 5) - _ewm((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope ema_gap 21d
def cg_f03_technology_f03_technology_trend_quality_core09_ema_gap_21d_slope_v130_signal(closeadj, volume):
    base = _mean((_z(volume, 63)), 21) - _ewm((_z(volume, 63)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope vol_ratio 126d
def cg_f03_technology_f03_technology_trend_quality_core00_vol_ratio_126d_slope_v131_signal(closeadj, volume):
    base = _safe_div(_std((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), max(2, 126//3)), _std((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 126).abs()+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope vol_ratio 252d
def cg_f03_technology_f03_technology_trend_quality_core01_vol_ratio_252d_slope_v132_signal(closeadj, volume):
    base = _safe_div(_std((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), max(2, 252//3)), _std((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 252).abs()+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope vol_ratio 5d
def cg_f03_technology_f03_technology_trend_quality_core02_vol_ratio_5d_slope_v133_signal(closeadj, volume):
    base = _safe_div(_std((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), max(2, 5//3)), _std((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 5).abs()+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope vol_ratio 21d
def cg_f03_technology_f03_technology_trend_quality_core03_vol_ratio_21d_slope_v134_signal(closeadj, volume):
    base = _safe_div(_std((_slope(_log(closeadj),21)), max(2, 21//3)), _std((_slope(_log(closeadj),21)), 21).abs()+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope vol_ratio 63d
def cg_f03_technology_f03_technology_trend_quality_core04_vol_ratio_63d_slope_v135_signal(closeadj, volume):
    base = _safe_div(_std((_slope(_log(_mean(closeadj,50)),21)), max(2, 63//3)), _std((_slope(_log(_mean(closeadj,50)),21)), 63).abs()+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope vol_ratio 126d
def cg_f03_technology_f03_technology_trend_quality_core05_vol_ratio_126d_slope_v136_signal(closeadj, volume):
    base = _safe_div(_std((_slope(_log(_mean(closeadj,200)),63)), max(2, 126//3)), _std((_slope(_log(_mean(closeadj,200)),63)), 126).abs()+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope vol_ratio 252d
def cg_f03_technology_f03_technology_trend_quality_core06_vol_ratio_252d_slope_v137_signal(closeadj, volume):
    base = _safe_div(_std((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), max(2, 252//3)), _std((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 252).abs()+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope vol_ratio 5d
def cg_f03_technology_f03_technology_trend_quality_core07_vol_ratio_5d_slope_v138_signal(closeadj, volume):
    base = _safe_div(_std((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), max(2, 5//3)), _std((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 5).abs()+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope vol_ratio 21d
def cg_f03_technology_f03_technology_trend_quality_core08_vol_ratio_21d_slope_v139_signal(closeadj, volume):
    base = _safe_div(_std((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), max(2, 21//3)), _std((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 21).abs()+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope vol_ratio 63d
def cg_f03_technology_f03_technology_trend_quality_core09_vol_ratio_63d_slope_v140_signal(closeadj, volume):
    base = _safe_div(_std((_z(volume, 63)), max(2, 63//3)), _std((_z(volume, 63)), 63).abs()+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope recent_vs_long 252d
def cg_f03_technology_f03_technology_trend_quality_core00_recent_vs_long_252d_slope_v141_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), max(2, 252//3)) - _mean((_safe_div(closeadj-_mean(closeadj,50), _mean(closeadj,50).abs()+1e-9)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope recent_vs_long 5d
def cg_f03_technology_f03_technology_trend_quality_core01_recent_vs_long_5d_slope_v142_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), max(2, 5//3)) - _mean((_safe_div(closeadj-_mean(closeadj,200), _mean(closeadj,200).abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope recent_vs_long 21d
def cg_f03_technology_f03_technology_trend_quality_core02_recent_vs_long_21d_slope_v143_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), max(2, 21//3)) - _mean((_safe_div(closeadj, _mean(closeadj,50).abs()+1e-9)+_safe_div(closeadj, _mean(closeadj,200).abs()+1e-9)-2.0), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope recent_vs_long 63d
def cg_f03_technology_f03_technology_trend_quality_core03_recent_vs_long_63d_slope_v144_signal(closeadj, volume):
    base = _mean((_slope(_log(closeadj),21)), max(2, 63//3)) - _mean((_slope(_log(closeadj),21)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope recent_vs_long 126d
def cg_f03_technology_f03_technology_trend_quality_core04_recent_vs_long_126d_slope_v145_signal(closeadj, volume):
    base = _mean((_slope(_log(_mean(closeadj,50)),21)), max(2, 126//3)) - _mean((_slope(_log(_mean(closeadj,50)),21)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope recent_vs_long 252d
def cg_f03_technology_f03_technology_trend_quality_core05_recent_vs_long_252d_slope_v146_signal(closeadj, volume):
    base = _mean((_slope(_log(_mean(closeadj,200)),63)), max(2, 252//3)) - _mean((_slope(_log(_mean(closeadj,200)),63)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope recent_vs_long 5d
def cg_f03_technology_f03_technology_trend_quality_core06_recent_vs_long_5d_slope_v147_signal(closeadj, volume):
    base = _mean((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), max(2, 5//3)) - _mean((_safe_div(_diff(closeadj, 21).abs(),_sum(_diff(closeadj, 1).abs(),21)+1e-9)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope recent_vs_long 21d
def cg_f03_technology_f03_technology_trend_quality_core07_recent_vs_long_21d_slope_v148_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), max(2, 21//3)) - _mean((_safe_div(closeadj-_mean(closeadj,50), closeadj.abs()+1e-9)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope recent_vs_long 63d
def cg_f03_technology_f03_technology_trend_quality_core08_recent_vs_long_63d_slope_v149_signal(closeadj, volume):
    base = _mean((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), max(2, 63//3)) - _mean((_safe_div(closeadj-_mean(closeadj,200), closeadj.abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope recent_vs_long 126d
def cg_f03_technology_f03_technology_trend_quality_core09_recent_vs_long_126d_slope_v150_signal(closeadj, volume):
    base = _mean((_z(volume, 63)), max(2, 126//3)) - _mean((_z(volume, 63)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

