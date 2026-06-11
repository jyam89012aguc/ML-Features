import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 slope mean 5d
def cg_f07_technology_f07_technology_volatility_regime_core00_mean_5d_slope_v001_signal(open, high, low, closeadj):
    base = _mean((_pct_change(closeadj, 1)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f07_technology_f07_technology_volatility_regime_core01_mean_21d_slope_v002_signal(open, high, low, closeadj):
    base = _mean((high-low), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f07_technology_f07_technology_volatility_regime_core02_mean_63d_slope_v003_signal(open, high, low, closeadj):
    base = _mean((_safe_div(high-low, closeadj.abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f07_technology_f07_technology_volatility_regime_core03_mean_126d_slope_v004_signal(open, high, low, closeadj):
    base = _mean((_std(_pct_change(closeadj, 1),21)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f07_technology_f07_technology_volatility_regime_core04_mean_252d_slope_v005_signal(open, high, low, closeadj):
    base = _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f07_technology_f07_technology_volatility_regime_core05_mean_5d_slope_v006_signal(open, high, low, closeadj):
    base = _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f07_technology_f07_technology_volatility_regime_core06_mean_21d_slope_v007_signal(open, high, low, closeadj):
    base = _mean((-_rank(high-low, 63)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f07_technology_f07_technology_volatility_regime_core07_mean_63d_slope_v008_signal(open, high, low, closeadj):
    base = _mean((_std(_pct_change(closeadj,1),252)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f07_technology_f07_technology_volatility_regime_core08_mean_126d_slope_v009_signal(open, high, low, closeadj):
    base = _mean((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f07_technology_f07_technology_volatility_regime_core09_mean_252d_slope_v010_signal(open, high, low, closeadj):
    base = _mean((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope z 21d
def cg_f07_technology_f07_technology_volatility_regime_core00_z_21d_slope_v011_signal(open, high, low, closeadj):
    base = _z((_pct_change(closeadj, 1)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope z 63d
def cg_f07_technology_f07_technology_volatility_regime_core01_z_63d_slope_v012_signal(open, high, low, closeadj):
    base = _z((high-low), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope z 126d
def cg_f07_technology_f07_technology_volatility_regime_core02_z_126d_slope_v013_signal(open, high, low, closeadj):
    base = _z((_safe_div(high-low, closeadj.abs()+1e-9)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope z 252d
def cg_f07_technology_f07_technology_volatility_regime_core03_z_252d_slope_v014_signal(open, high, low, closeadj):
    base = _z((_std(_pct_change(closeadj, 1),21)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope z 5d
def cg_f07_technology_f07_technology_volatility_regime_core04_z_5d_slope_v015_signal(open, high, low, closeadj):
    base = _z((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope z 21d
def cg_f07_technology_f07_technology_volatility_regime_core05_z_21d_slope_v016_signal(open, high, low, closeadj):
    base = _z((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope z 63d
def cg_f07_technology_f07_technology_volatility_regime_core06_z_63d_slope_v017_signal(open, high, low, closeadj):
    base = _z((-_rank(high-low, 63)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope z 126d
def cg_f07_technology_f07_technology_volatility_regime_core07_z_126d_slope_v018_signal(open, high, low, closeadj):
    base = _z((_std(_pct_change(closeadj,1),252)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope z 252d
def cg_f07_technology_f07_technology_volatility_regime_core08_z_252d_slope_v019_signal(open, high, low, closeadj):
    base = _z((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope z 5d
def cg_f07_technology_f07_technology_volatility_regime_core09_z_5d_slope_v020_signal(open, high, low, closeadj):
    base = _z((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope rank 63d
def cg_f07_technology_f07_technology_volatility_regime_core00_rank_63d_slope_v021_signal(open, high, low, closeadj):
    base = _rank((_pct_change(closeadj, 1)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope rank 126d
def cg_f07_technology_f07_technology_volatility_regime_core01_rank_126d_slope_v022_signal(open, high, low, closeadj):
    base = _rank((high-low), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope rank 252d
def cg_f07_technology_f07_technology_volatility_regime_core02_rank_252d_slope_v023_signal(open, high, low, closeadj):
    base = _rank((_safe_div(high-low, closeadj.abs()+1e-9)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope rank 5d
def cg_f07_technology_f07_technology_volatility_regime_core03_rank_5d_slope_v024_signal(open, high, low, closeadj):
    base = _rank((_std(_pct_change(closeadj, 1),21)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope rank 21d
def cg_f07_technology_f07_technology_volatility_regime_core04_rank_21d_slope_v025_signal(open, high, low, closeadj):
    base = _rank((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope rank 63d
def cg_f07_technology_f07_technology_volatility_regime_core05_rank_63d_slope_v026_signal(open, high, low, closeadj):
    base = _rank((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope rank 126d
def cg_f07_technology_f07_technology_volatility_regime_core06_rank_126d_slope_v027_signal(open, high, low, closeadj):
    base = _rank((-_rank(high-low, 63)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope rank 252d
def cg_f07_technology_f07_technology_volatility_regime_core07_rank_252d_slope_v028_signal(open, high, low, closeadj):
    base = _rank((_std(_pct_change(closeadj,1),252)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope rank 5d
def cg_f07_technology_f07_technology_volatility_regime_core08_rank_5d_slope_v029_signal(open, high, low, closeadj):
    base = _rank((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope rank 21d
def cg_f07_technology_f07_technology_volatility_regime_core09_rank_21d_slope_v030_signal(open, high, low, closeadj):
    base = _rank((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope std 126d
def cg_f07_technology_f07_technology_volatility_regime_core00_std_126d_slope_v031_signal(open, high, low, closeadj):
    base = _std((_pct_change(closeadj, 1)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope std 252d
def cg_f07_technology_f07_technology_volatility_regime_core01_std_252d_slope_v032_signal(open, high, low, closeadj):
    base = _std((high-low), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope std 5d
def cg_f07_technology_f07_technology_volatility_regime_core02_std_5d_slope_v033_signal(open, high, low, closeadj):
    base = _std((_safe_div(high-low, closeadj.abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope std 21d
def cg_f07_technology_f07_technology_volatility_regime_core03_std_21d_slope_v034_signal(open, high, low, closeadj):
    base = _std((_std(_pct_change(closeadj, 1),21)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope std 63d
def cg_f07_technology_f07_technology_volatility_regime_core04_std_63d_slope_v035_signal(open, high, low, closeadj):
    base = _std((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope std 126d
def cg_f07_technology_f07_technology_volatility_regime_core05_std_126d_slope_v036_signal(open, high, low, closeadj):
    base = _std((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope std 252d
def cg_f07_technology_f07_technology_volatility_regime_core06_std_252d_slope_v037_signal(open, high, low, closeadj):
    base = _std((-_rank(high-low, 63)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope std 5d
def cg_f07_technology_f07_technology_volatility_regime_core07_std_5d_slope_v038_signal(open, high, low, closeadj):
    base = _std((_std(_pct_change(closeadj,1),252)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope std 21d
def cg_f07_technology_f07_technology_volatility_regime_core08_std_21d_slope_v039_signal(open, high, low, closeadj):
    base = _std((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope std 63d
def cg_f07_technology_f07_technology_volatility_regime_core09_std_63d_slope_v040_signal(open, high, low, closeadj):
    base = _std((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope slope 252d
def cg_f07_technology_f07_technology_volatility_regime_core00_slope_252d_slope_v041_signal(open, high, low, closeadj):
    base = _slope((_pct_change(closeadj, 1)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope slope 5d
def cg_f07_technology_f07_technology_volatility_regime_core01_slope_5d_slope_v042_signal(open, high, low, closeadj):
    base = _slope((high-low), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope slope 21d
def cg_f07_technology_f07_technology_volatility_regime_core02_slope_21d_slope_v043_signal(open, high, low, closeadj):
    base = _slope((_safe_div(high-low, closeadj.abs()+1e-9)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope slope 63d
def cg_f07_technology_f07_technology_volatility_regime_core03_slope_63d_slope_v044_signal(open, high, low, closeadj):
    base = _slope((_std(_pct_change(closeadj, 1),21)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope slope 126d
def cg_f07_technology_f07_technology_volatility_regime_core04_slope_126d_slope_v045_signal(open, high, low, closeadj):
    base = _slope((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope slope 252d
def cg_f07_technology_f07_technology_volatility_regime_core05_slope_252d_slope_v046_signal(open, high, low, closeadj):
    base = _slope((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope slope 5d
def cg_f07_technology_f07_technology_volatility_regime_core06_slope_5d_slope_v047_signal(open, high, low, closeadj):
    base = _slope((-_rank(high-low, 63)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope slope 21d
def cg_f07_technology_f07_technology_volatility_regime_core07_slope_21d_slope_v048_signal(open, high, low, closeadj):
    base = _slope((_std(_pct_change(closeadj,1),252)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope slope 63d
def cg_f07_technology_f07_technology_volatility_regime_core08_slope_63d_slope_v049_signal(open, high, low, closeadj):
    base = _slope((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope slope 126d
def cg_f07_technology_f07_technology_volatility_regime_core09_slope_126d_slope_v050_signal(open, high, low, closeadj):
    base = _slope((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope diff 5d
def cg_f07_technology_f07_technology_volatility_regime_core00_diff_5d_slope_v051_signal(open, high, low, closeadj):
    base = _diff((_pct_change(closeadj, 1)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope diff 21d
def cg_f07_technology_f07_technology_volatility_regime_core01_diff_21d_slope_v052_signal(open, high, low, closeadj):
    base = _diff((high-low), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope diff 63d
def cg_f07_technology_f07_technology_volatility_regime_core02_diff_63d_slope_v053_signal(open, high, low, closeadj):
    base = _diff((_safe_div(high-low, closeadj.abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope diff 126d
def cg_f07_technology_f07_technology_volatility_regime_core03_diff_126d_slope_v054_signal(open, high, low, closeadj):
    base = _diff((_std(_pct_change(closeadj, 1),21)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope diff 252d
def cg_f07_technology_f07_technology_volatility_regime_core04_diff_252d_slope_v055_signal(open, high, low, closeadj):
    base = _diff((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope diff 5d
def cg_f07_technology_f07_technology_volatility_regime_core05_diff_5d_slope_v056_signal(open, high, low, closeadj):
    base = _diff((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope diff 21d
def cg_f07_technology_f07_technology_volatility_regime_core06_diff_21d_slope_v057_signal(open, high, low, closeadj):
    base = _diff((-_rank(high-low, 63)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope diff 63d
def cg_f07_technology_f07_technology_volatility_regime_core07_diff_63d_slope_v058_signal(open, high, low, closeadj):
    base = _diff((_std(_pct_change(closeadj,1),252)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope diff 126d
def cg_f07_technology_f07_technology_volatility_regime_core08_diff_126d_slope_v059_signal(open, high, low, closeadj):
    base = _diff((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope diff 252d
def cg_f07_technology_f07_technology_volatility_regime_core09_diff_252d_slope_v060_signal(open, high, low, closeadj):
    base = _diff((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope pct 21d
def cg_f07_technology_f07_technology_volatility_regime_core00_pct_21d_slope_v061_signal(open, high, low, closeadj):
    base = _pct_change(((_pct_change(closeadj, 1)).abs()+1.0), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope pct 63d
def cg_f07_technology_f07_technology_volatility_regime_core01_pct_63d_slope_v062_signal(open, high, low, closeadj):
    base = _pct_change(((high-low).abs()+1.0), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope pct 126d
def cg_f07_technology_f07_technology_volatility_regime_core02_pct_126d_slope_v063_signal(open, high, low, closeadj):
    base = _pct_change(((_safe_div(high-low, closeadj.abs()+1e-9)).abs()+1.0), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope pct 252d
def cg_f07_technology_f07_technology_volatility_regime_core03_pct_252d_slope_v064_signal(open, high, low, closeadj):
    base = _pct_change(((_std(_pct_change(closeadj, 1),21)).abs()+1.0), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope pct 5d
def cg_f07_technology_f07_technology_volatility_regime_core04_pct_5d_slope_v065_signal(open, high, low, closeadj):
    base = _pct_change(((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)).abs()+1.0), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope pct 21d
def cg_f07_technology_f07_technology_volatility_regime_core05_pct_21d_slope_v066_signal(open, high, low, closeadj):
    base = _pct_change(((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)).abs()+1.0), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope pct 63d
def cg_f07_technology_f07_technology_volatility_regime_core06_pct_63d_slope_v067_signal(open, high, low, closeadj):
    base = _pct_change(((-_rank(high-low, 63)).abs()+1.0), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope pct 126d
def cg_f07_technology_f07_technology_volatility_regime_core07_pct_126d_slope_v068_signal(open, high, low, closeadj):
    base = _pct_change(((_std(_pct_change(closeadj,1),252)).abs()+1.0), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope pct 252d
def cg_f07_technology_f07_technology_volatility_regime_core08_pct_252d_slope_v069_signal(open, high, low, closeadj):
    base = _pct_change(((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)).abs()+1.0), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope pct 5d
def cg_f07_technology_f07_technology_volatility_regime_core09_pct_5d_slope_v070_signal(open, high, low, closeadj):
    base = _pct_change(((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)).abs()+1.0), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 63d
def cg_f07_technology_f07_technology_volatility_regime_core00_ewm_63d_slope_v071_signal(open, high, low, closeadj):
    base = _ewm((_pct_change(closeadj, 1)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 126d
def cg_f07_technology_f07_technology_volatility_regime_core01_ewm_126d_slope_v072_signal(open, high, low, closeadj):
    base = _ewm((high-low), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 252d
def cg_f07_technology_f07_technology_volatility_regime_core02_ewm_252d_slope_v073_signal(open, high, low, closeadj):
    base = _ewm((_safe_div(high-low, closeadj.abs()+1e-9)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 5d
def cg_f07_technology_f07_technology_volatility_regime_core03_ewm_5d_slope_v074_signal(open, high, low, closeadj):
    base = _ewm((_std(_pct_change(closeadj, 1),21)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 21d
def cg_f07_technology_f07_technology_volatility_regime_core04_ewm_21d_slope_v075_signal(open, high, low, closeadj):
    base = _ewm((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 63d
def cg_f07_technology_f07_technology_volatility_regime_core05_ewm_63d_slope_v076_signal(open, high, low, closeadj):
    base = _ewm((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 126d
def cg_f07_technology_f07_technology_volatility_regime_core06_ewm_126d_slope_v077_signal(open, high, low, closeadj):
    base = _ewm((-_rank(high-low, 63)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 252d
def cg_f07_technology_f07_technology_volatility_regime_core07_ewm_252d_slope_v078_signal(open, high, low, closeadj):
    base = _ewm((_std(_pct_change(closeadj,1),252)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 5d
def cg_f07_technology_f07_technology_volatility_regime_core08_ewm_5d_slope_v079_signal(open, high, low, closeadj):
    base = _ewm((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 21d
def cg_f07_technology_f07_technology_volatility_regime_core09_ewm_21d_slope_v080_signal(open, high, low, closeadj):
    base = _ewm((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope skew 126d
def cg_f07_technology_f07_technology_volatility_regime_core00_skew_126d_slope_v081_signal(open, high, low, closeadj):
    base = _skew((_pct_change(closeadj, 1)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope skew 252d
def cg_f07_technology_f07_technology_volatility_regime_core01_skew_252d_slope_v082_signal(open, high, low, closeadj):
    base = _skew((high-low), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope skew 5d
def cg_f07_technology_f07_technology_volatility_regime_core02_skew_5d_slope_v083_signal(open, high, low, closeadj):
    base = _skew((_safe_div(high-low, closeadj.abs()+1e-9)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope skew 21d
def cg_f07_technology_f07_technology_volatility_regime_core03_skew_21d_slope_v084_signal(open, high, low, closeadj):
    base = _skew((_std(_pct_change(closeadj, 1),21)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope skew 63d
def cg_f07_technology_f07_technology_volatility_regime_core04_skew_63d_slope_v085_signal(open, high, low, closeadj):
    base = _skew((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope skew 126d
def cg_f07_technology_f07_technology_volatility_regime_core05_skew_126d_slope_v086_signal(open, high, low, closeadj):
    base = _skew((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope skew 252d
def cg_f07_technology_f07_technology_volatility_regime_core06_skew_252d_slope_v087_signal(open, high, low, closeadj):
    base = _skew((-_rank(high-low, 63)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope skew 5d
def cg_f07_technology_f07_technology_volatility_regime_core07_skew_5d_slope_v088_signal(open, high, low, closeadj):
    base = _skew((_std(_pct_change(closeadj,1),252)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope skew 21d
def cg_f07_technology_f07_technology_volatility_regime_core08_skew_21d_slope_v089_signal(open, high, low, closeadj):
    base = _skew((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope skew 63d
def cg_f07_technology_f07_technology_volatility_regime_core09_skew_63d_slope_v090_signal(open, high, low, closeadj):
    base = _skew((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope kurt 252d
def cg_f07_technology_f07_technology_volatility_regime_core00_kurt_252d_slope_v091_signal(open, high, low, closeadj):
    base = _kurt((_pct_change(closeadj, 1)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope kurt 5d
def cg_f07_technology_f07_technology_volatility_regime_core01_kurt_5d_slope_v092_signal(open, high, low, closeadj):
    base = _kurt((high-low), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope kurt 21d
def cg_f07_technology_f07_technology_volatility_regime_core02_kurt_21d_slope_v093_signal(open, high, low, closeadj):
    base = _kurt((_safe_div(high-low, closeadj.abs()+1e-9)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope kurt 63d
def cg_f07_technology_f07_technology_volatility_regime_core03_kurt_63d_slope_v094_signal(open, high, low, closeadj):
    base = _kurt((_std(_pct_change(closeadj, 1),21)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope kurt 126d
def cg_f07_technology_f07_technology_volatility_regime_core04_kurt_126d_slope_v095_signal(open, high, low, closeadj):
    base = _kurt((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope kurt 252d
def cg_f07_technology_f07_technology_volatility_regime_core05_kurt_252d_slope_v096_signal(open, high, low, closeadj):
    base = _kurt((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope kurt 5d
def cg_f07_technology_f07_technology_volatility_regime_core06_kurt_5d_slope_v097_signal(open, high, low, closeadj):
    base = _kurt((-_rank(high-low, 63)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope kurt 21d
def cg_f07_technology_f07_technology_volatility_regime_core07_kurt_21d_slope_v098_signal(open, high, low, closeadj):
    base = _kurt((_std(_pct_change(closeadj,1),252)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope kurt 63d
def cg_f07_technology_f07_technology_volatility_regime_core08_kurt_63d_slope_v099_signal(open, high, low, closeadj):
    base = _kurt((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope kurt 126d
def cg_f07_technology_f07_technology_volatility_regime_core09_kurt_126d_slope_v100_signal(open, high, low, closeadj):
    base = _kurt((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope autocorr 5d
def cg_f07_technology_f07_technology_volatility_regime_core00_autocorr_5d_slope_v101_signal(open, high, low, closeadj):
    base = _autocorr((_pct_change(closeadj, 1)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope autocorr 21d
def cg_f07_technology_f07_technology_volatility_regime_core01_autocorr_21d_slope_v102_signal(open, high, low, closeadj):
    base = _autocorr((high-low), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope autocorr 63d
def cg_f07_technology_f07_technology_volatility_regime_core02_autocorr_63d_slope_v103_signal(open, high, low, closeadj):
    base = _autocorr((_safe_div(high-low, closeadj.abs()+1e-9)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope autocorr 126d
def cg_f07_technology_f07_technology_volatility_regime_core03_autocorr_126d_slope_v104_signal(open, high, low, closeadj):
    base = _autocorr((_std(_pct_change(closeadj, 1),21)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope autocorr 252d
def cg_f07_technology_f07_technology_volatility_regime_core04_autocorr_252d_slope_v105_signal(open, high, low, closeadj):
    base = _autocorr((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope autocorr 5d
def cg_f07_technology_f07_technology_volatility_regime_core05_autocorr_5d_slope_v106_signal(open, high, low, closeadj):
    base = _autocorr((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope autocorr 21d
def cg_f07_technology_f07_technology_volatility_regime_core06_autocorr_21d_slope_v107_signal(open, high, low, closeadj):
    base = _autocorr((-_rank(high-low, 63)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope autocorr 63d
def cg_f07_technology_f07_technology_volatility_regime_core07_autocorr_63d_slope_v108_signal(open, high, low, closeadj):
    base = _autocorr((_std(_pct_change(closeadj,1),252)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope autocorr 126d
def cg_f07_technology_f07_technology_volatility_regime_core08_autocorr_126d_slope_v109_signal(open, high, low, closeadj):
    base = _autocorr((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope autocorr 252d
def cg_f07_technology_f07_technology_volatility_regime_core09_autocorr_252d_slope_v110_signal(open, high, low, closeadj):
    base = _autocorr((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope snr 21d
def cg_f07_technology_f07_technology_volatility_regime_core00_snr_21d_slope_v111_signal(open, high, low, closeadj):
    base = _safe_div(_diff((_pct_change(closeadj, 1)), max(1, 21//3)).abs(), _std(_diff((_pct_change(closeadj, 1)),1), 21)+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope snr 63d
def cg_f07_technology_f07_technology_volatility_regime_core01_snr_63d_slope_v112_signal(open, high, low, closeadj):
    base = _safe_div(_diff((high-low), max(1, 63//3)).abs(), _std(_diff((high-low),1), 63)+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope snr 126d
def cg_f07_technology_f07_technology_volatility_regime_core02_snr_126d_slope_v113_signal(open, high, low, closeadj):
    base = _safe_div(_diff((_safe_div(high-low, closeadj.abs()+1e-9)), max(1, 126//3)).abs(), _std(_diff((_safe_div(high-low, closeadj.abs()+1e-9)),1), 126)+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope snr 252d
def cg_f07_technology_f07_technology_volatility_regime_core03_snr_252d_slope_v114_signal(open, high, low, closeadj):
    base = _safe_div(_diff((_std(_pct_change(closeadj, 1),21)), max(1, 252//3)).abs(), _std(_diff((_std(_pct_change(closeadj, 1),21)),1), 252)+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope snr 5d
def cg_f07_technology_f07_technology_volatility_regime_core04_snr_5d_slope_v115_signal(open, high, low, closeadj):
    base = _safe_div(_diff((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), max(1, 5//3)).abs(), _std(_diff((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)),1), 5)+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope snr 21d
def cg_f07_technology_f07_technology_volatility_regime_core05_snr_21d_slope_v116_signal(open, high, low, closeadj):
    base = _safe_div(_diff((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), max(1, 21//3)).abs(), _std(_diff((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)),1), 21)+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope snr 63d
def cg_f07_technology_f07_technology_volatility_regime_core06_snr_63d_slope_v117_signal(open, high, low, closeadj):
    base = _safe_div(_diff((-_rank(high-low, 63)), max(1, 63//3)).abs(), _std(_diff((-_rank(high-low, 63)),1), 63)+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope snr 126d
def cg_f07_technology_f07_technology_volatility_regime_core07_snr_126d_slope_v118_signal(open, high, low, closeadj):
    base = _safe_div(_diff((_std(_pct_change(closeadj,1),252)), max(1, 126//3)).abs(), _std(_diff((_std(_pct_change(closeadj,1),252)),1), 126)+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope snr 252d
def cg_f07_technology_f07_technology_volatility_regime_core08_snr_252d_slope_v119_signal(open, high, low, closeadj):
    base = _safe_div(_diff((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), max(1, 252//3)).abs(), _std(_diff((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)),1), 252)+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope snr 5d
def cg_f07_technology_f07_technology_volatility_regime_core09_snr_5d_slope_v120_signal(open, high, low, closeadj):
    base = _safe_div(_diff((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), max(1, 5//3)).abs(), _std(_diff((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)),1), 5)+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope ema_gap 63d
def cg_f07_technology_f07_technology_volatility_regime_core00_ema_gap_63d_slope_v121_signal(open, high, low, closeadj):
    base = _mean((_pct_change(closeadj, 1)), 63) - _ewm((_pct_change(closeadj, 1)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope ema_gap 126d
def cg_f07_technology_f07_technology_volatility_regime_core01_ema_gap_126d_slope_v122_signal(open, high, low, closeadj):
    base = _mean((high-low), 126) - _ewm((high-low), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope ema_gap 252d
def cg_f07_technology_f07_technology_volatility_regime_core02_ema_gap_252d_slope_v123_signal(open, high, low, closeadj):
    base = _mean((_safe_div(high-low, closeadj.abs()+1e-9)), 252) - _ewm((_safe_div(high-low, closeadj.abs()+1e-9)), 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope ema_gap 5d
def cg_f07_technology_f07_technology_volatility_regime_core03_ema_gap_5d_slope_v124_signal(open, high, low, closeadj):
    base = _mean((_std(_pct_change(closeadj, 1),21)), 5) - _ewm((_std(_pct_change(closeadj, 1),21)), 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope ema_gap 21d
def cg_f07_technology_f07_technology_volatility_regime_core04_ema_gap_21d_slope_v125_signal(open, high, low, closeadj):
    base = _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 21) - _ewm((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope ema_gap 63d
def cg_f07_technology_f07_technology_volatility_regime_core05_ema_gap_63d_slope_v126_signal(open, high, low, closeadj):
    base = _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 63) - _ewm((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope ema_gap 126d
def cg_f07_technology_f07_technology_volatility_regime_core06_ema_gap_126d_slope_v127_signal(open, high, low, closeadj):
    base = _mean((-_rank(high-low, 63)), 126) - _ewm((-_rank(high-low, 63)), 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope ema_gap 252d
def cg_f07_technology_f07_technology_volatility_regime_core07_ema_gap_252d_slope_v128_signal(open, high, low, closeadj):
    base = _mean((_std(_pct_change(closeadj,1),252)), 252) - _ewm((_std(_pct_change(closeadj,1),252)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope ema_gap 5d
def cg_f07_technology_f07_technology_volatility_regime_core08_ema_gap_5d_slope_v129_signal(open, high, low, closeadj):
    base = _mean((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 5) - _ewm((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope ema_gap 21d
def cg_f07_technology_f07_technology_volatility_regime_core09_ema_gap_21d_slope_v130_signal(open, high, low, closeadj):
    base = _mean((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 21) - _ewm((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope vol_ratio 126d
def cg_f07_technology_f07_technology_volatility_regime_core00_vol_ratio_126d_slope_v131_signal(open, high, low, closeadj):
    base = _safe_div(_std((_pct_change(closeadj, 1)), max(2, 126//3)), _std((_pct_change(closeadj, 1)), 126).abs()+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope vol_ratio 252d
def cg_f07_technology_f07_technology_volatility_regime_core01_vol_ratio_252d_slope_v132_signal(open, high, low, closeadj):
    base = _safe_div(_std((high-low), max(2, 252//3)), _std((high-low), 252).abs()+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope vol_ratio 5d
def cg_f07_technology_f07_technology_volatility_regime_core02_vol_ratio_5d_slope_v133_signal(open, high, low, closeadj):
    base = _safe_div(_std((_safe_div(high-low, closeadj.abs()+1e-9)), max(2, 5//3)), _std((_safe_div(high-low, closeadj.abs()+1e-9)), 5).abs()+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope vol_ratio 21d
def cg_f07_technology_f07_technology_volatility_regime_core03_vol_ratio_21d_slope_v134_signal(open, high, low, closeadj):
    base = _safe_div(_std((_std(_pct_change(closeadj, 1),21)), max(2, 21//3)), _std((_std(_pct_change(closeadj, 1),21)), 21).abs()+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope vol_ratio 63d
def cg_f07_technology_f07_technology_volatility_regime_core04_vol_ratio_63d_slope_v135_signal(open, high, low, closeadj):
    base = _safe_div(_std((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), max(2, 63//3)), _std((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 63).abs()+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope vol_ratio 126d
def cg_f07_technology_f07_technology_volatility_regime_core05_vol_ratio_126d_slope_v136_signal(open, high, low, closeadj):
    base = _safe_div(_std((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), max(2, 126//3)), _std((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 126).abs()+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope vol_ratio 252d
def cg_f07_technology_f07_technology_volatility_regime_core06_vol_ratio_252d_slope_v137_signal(open, high, low, closeadj):
    base = _safe_div(_std((-_rank(high-low, 63)), max(2, 252//3)), _std((-_rank(high-low, 63)), 252).abs()+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope vol_ratio 5d
def cg_f07_technology_f07_technology_volatility_regime_core07_vol_ratio_5d_slope_v138_signal(open, high, low, closeadj):
    base = _safe_div(_std((_std(_pct_change(closeadj,1),252)), max(2, 5//3)), _std((_std(_pct_change(closeadj,1),252)), 5).abs()+1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope vol_ratio 21d
def cg_f07_technology_f07_technology_volatility_regime_core08_vol_ratio_21d_slope_v139_signal(open, high, low, closeadj):
    base = _safe_div(_std((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), max(2, 21//3)), _std((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 21).abs()+1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope vol_ratio 63d
def cg_f07_technology_f07_technology_volatility_regime_core09_vol_ratio_63d_slope_v140_signal(open, high, low, closeadj):
    base = _safe_div(_std((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), max(2, 63//3)), _std((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 63).abs()+1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope recent_vs_long 252d
def cg_f07_technology_f07_technology_volatility_regime_core00_recent_vs_long_252d_slope_v141_signal(open, high, low, closeadj):
    base = _mean((_pct_change(closeadj, 1)), max(2, 252//3)) - _mean((_pct_change(closeadj, 1)), 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope recent_vs_long 5d
def cg_f07_technology_f07_technology_volatility_regime_core01_recent_vs_long_5d_slope_v142_signal(open, high, low, closeadj):
    base = _mean((high-low), max(2, 5//3)) - _mean((high-low), 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope recent_vs_long 21d
def cg_f07_technology_f07_technology_volatility_regime_core02_recent_vs_long_21d_slope_v143_signal(open, high, low, closeadj):
    base = _mean((_safe_div(high-low, closeadj.abs()+1e-9)), max(2, 21//3)) - _mean((_safe_div(high-low, closeadj.abs()+1e-9)), 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope recent_vs_long 63d
def cg_f07_technology_f07_technology_volatility_regime_core03_recent_vs_long_63d_slope_v144_signal(open, high, low, closeadj):
    base = _mean((_std(_pct_change(closeadj, 1),21)), max(2, 63//3)) - _mean((_std(_pct_change(closeadj, 1),21)), 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope recent_vs_long 126d
def cg_f07_technology_f07_technology_volatility_regime_core04_recent_vs_long_126d_slope_v145_signal(open, high, low, closeadj):
    base = _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), max(2, 126//3)) - _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope recent_vs_long 252d
def cg_f07_technology_f07_technology_volatility_regime_core05_recent_vs_long_252d_slope_v146_signal(open, high, low, closeadj):
    base = _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), max(2, 252//3)) - _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope recent_vs_long 5d
def cg_f07_technology_f07_technology_volatility_regime_core06_recent_vs_long_5d_slope_v147_signal(open, high, low, closeadj):
    base = _mean((-_rank(high-low, 63)), max(2, 5//3)) - _mean((-_rank(high-low, 63)), 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope recent_vs_long 21d
def cg_f07_technology_f07_technology_volatility_regime_core07_recent_vs_long_21d_slope_v148_signal(open, high, low, closeadj):
    base = _mean((_std(_pct_change(closeadj,1),252)), max(2, 21//3)) - _mean((_std(_pct_change(closeadj,1),252)), 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope recent_vs_long 63d
def cg_f07_technology_f07_technology_volatility_regime_core08_recent_vs_long_63d_slope_v149_signal(open, high, low, closeadj):
    base = _mean((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), max(2, 63//3)) - _mean((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope recent_vs_long 126d
def cg_f07_technology_f07_technology_volatility_regime_core09_recent_vs_long_126d_slope_v150_signal(open, high, low, closeadj):
    base = _mean((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), max(2, 126//3)) - _mean((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

