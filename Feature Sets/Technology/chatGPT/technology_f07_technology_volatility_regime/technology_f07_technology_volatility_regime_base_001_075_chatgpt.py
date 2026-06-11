import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 mean 5d
def cg_f07_technology_f07_technology_volatility_regime_core00_mean_5d_base_v001_signal(open, high, low, closeadj):
    result = _mean((_pct_change(closeadj, 1)), 5)
    return _clean(result)

# core01 mean 21d
def cg_f07_technology_f07_technology_volatility_regime_core01_mean_21d_base_v002_signal(open, high, low, closeadj):
    result = _mean((high-low), 21)
    return _clean(result)

# core02 mean 63d
def cg_f07_technology_f07_technology_volatility_regime_core02_mean_63d_base_v003_signal(open, high, low, closeadj):
    result = _mean((_safe_div(high-low, closeadj.abs()+1e-9)), 63)
    return _clean(result)

# core03 mean 126d
def cg_f07_technology_f07_technology_volatility_regime_core03_mean_126d_base_v004_signal(open, high, low, closeadj):
    result = _mean((_std(_pct_change(closeadj, 1),21)), 126)
    return _clean(result)

# core04 mean 252d
def cg_f07_technology_f07_technology_volatility_regime_core04_mean_252d_base_v005_signal(open, high, low, closeadj):
    result = _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 252)
    return _clean(result)

# core05 mean 5d
def cg_f07_technology_f07_technology_volatility_regime_core05_mean_5d_base_v006_signal(open, high, low, closeadj):
    result = _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 5)
    return _clean(result)

# core06 mean 21d
def cg_f07_technology_f07_technology_volatility_regime_core06_mean_21d_base_v007_signal(open, high, low, closeadj):
    result = _mean((-_rank(high-low, 63)), 21)
    return _clean(result)

# core07 mean 63d
def cg_f07_technology_f07_technology_volatility_regime_core07_mean_63d_base_v008_signal(open, high, low, closeadj):
    result = _mean((_std(_pct_change(closeadj,1),252)), 63)
    return _clean(result)

# core08 mean 126d
def cg_f07_technology_f07_technology_volatility_regime_core08_mean_126d_base_v009_signal(open, high, low, closeadj):
    result = _mean((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 126)
    return _clean(result)

# core09 mean 252d
def cg_f07_technology_f07_technology_volatility_regime_core09_mean_252d_base_v010_signal(open, high, low, closeadj):
    result = _mean((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 252)
    return _clean(result)

# core00 z 21d
def cg_f07_technology_f07_technology_volatility_regime_core00_z_21d_base_v011_signal(open, high, low, closeadj):
    result = _z((_pct_change(closeadj, 1)), 21)
    return _clean(result)

# core01 z 63d
def cg_f07_technology_f07_technology_volatility_regime_core01_z_63d_base_v012_signal(open, high, low, closeadj):
    result = _z((high-low), 63)
    return _clean(result)

# core02 z 126d
def cg_f07_technology_f07_technology_volatility_regime_core02_z_126d_base_v013_signal(open, high, low, closeadj):
    result = _z((_safe_div(high-low, closeadj.abs()+1e-9)), 126)
    return _clean(result)

# core03 z 252d
def cg_f07_technology_f07_technology_volatility_regime_core03_z_252d_base_v014_signal(open, high, low, closeadj):
    result = _z((_std(_pct_change(closeadj, 1),21)), 252)
    return _clean(result)

# core04 z 5d
def cg_f07_technology_f07_technology_volatility_regime_core04_z_5d_base_v015_signal(open, high, low, closeadj):
    result = _z((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 5)
    return _clean(result)

# core05 z 21d
def cg_f07_technology_f07_technology_volatility_regime_core05_z_21d_base_v016_signal(open, high, low, closeadj):
    result = _z((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 21)
    return _clean(result)

# core06 z 63d
def cg_f07_technology_f07_technology_volatility_regime_core06_z_63d_base_v017_signal(open, high, low, closeadj):
    result = _z((-_rank(high-low, 63)), 63)
    return _clean(result)

# core07 z 126d
def cg_f07_technology_f07_technology_volatility_regime_core07_z_126d_base_v018_signal(open, high, low, closeadj):
    result = _z((_std(_pct_change(closeadj,1),252)), 126)
    return _clean(result)

# core08 z 252d
def cg_f07_technology_f07_technology_volatility_regime_core08_z_252d_base_v019_signal(open, high, low, closeadj):
    result = _z((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 252)
    return _clean(result)

# core09 z 5d
def cg_f07_technology_f07_technology_volatility_regime_core09_z_5d_base_v020_signal(open, high, low, closeadj):
    result = _z((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 5)
    return _clean(result)

# core00 rank 63d
def cg_f07_technology_f07_technology_volatility_regime_core00_rank_63d_base_v021_signal(open, high, low, closeadj):
    result = _rank((_pct_change(closeadj, 1)), 63)
    return _clean(result)

# core01 rank 126d
def cg_f07_technology_f07_technology_volatility_regime_core01_rank_126d_base_v022_signal(open, high, low, closeadj):
    result = _rank((high-low), 126)
    return _clean(result)

# core02 rank 252d
def cg_f07_technology_f07_technology_volatility_regime_core02_rank_252d_base_v023_signal(open, high, low, closeadj):
    result = _rank((_safe_div(high-low, closeadj.abs()+1e-9)), 252)
    return _clean(result)

# core03 rank 5d
def cg_f07_technology_f07_technology_volatility_regime_core03_rank_5d_base_v024_signal(open, high, low, closeadj):
    result = _rank((_std(_pct_change(closeadj, 1),21)), 5)
    return _clean(result)

# core04 rank 21d
def cg_f07_technology_f07_technology_volatility_regime_core04_rank_21d_base_v025_signal(open, high, low, closeadj):
    result = _rank((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 21)
    return _clean(result)

# core05 rank 63d
def cg_f07_technology_f07_technology_volatility_regime_core05_rank_63d_base_v026_signal(open, high, low, closeadj):
    result = _rank((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 63)
    return _clean(result)

# core06 rank 126d
def cg_f07_technology_f07_technology_volatility_regime_core06_rank_126d_base_v027_signal(open, high, low, closeadj):
    result = _rank((-_rank(high-low, 63)), 126)
    return _clean(result)

# core07 rank 252d
def cg_f07_technology_f07_technology_volatility_regime_core07_rank_252d_base_v028_signal(open, high, low, closeadj):
    result = _rank((_std(_pct_change(closeadj,1),252)), 252)
    return _clean(result)

# core08 rank 5d
def cg_f07_technology_f07_technology_volatility_regime_core08_rank_5d_base_v029_signal(open, high, low, closeadj):
    result = _rank((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 5)
    return _clean(result)

# core09 rank 21d
def cg_f07_technology_f07_technology_volatility_regime_core09_rank_21d_base_v030_signal(open, high, low, closeadj):
    result = _rank((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 21)
    return _clean(result)

# core00 std 126d
def cg_f07_technology_f07_technology_volatility_regime_core00_std_126d_base_v031_signal(open, high, low, closeadj):
    result = _std((_pct_change(closeadj, 1)), 126)
    return _clean(result)

# core01 std 252d
def cg_f07_technology_f07_technology_volatility_regime_core01_std_252d_base_v032_signal(open, high, low, closeadj):
    result = _std((high-low), 252)
    return _clean(result)

# core02 std 5d
def cg_f07_technology_f07_technology_volatility_regime_core02_std_5d_base_v033_signal(open, high, low, closeadj):
    result = _std((_safe_div(high-low, closeadj.abs()+1e-9)), 5)
    return _clean(result)

# core03 std 21d
def cg_f07_technology_f07_technology_volatility_regime_core03_std_21d_base_v034_signal(open, high, low, closeadj):
    result = _std((_std(_pct_change(closeadj, 1),21)), 21)
    return _clean(result)

# core04 std 63d
def cg_f07_technology_f07_technology_volatility_regime_core04_std_63d_base_v035_signal(open, high, low, closeadj):
    result = _std((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 63)
    return _clean(result)

# core05 std 126d
def cg_f07_technology_f07_technology_volatility_regime_core05_std_126d_base_v036_signal(open, high, low, closeadj):
    result = _std((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 126)
    return _clean(result)

# core06 std 252d
def cg_f07_technology_f07_technology_volatility_regime_core06_std_252d_base_v037_signal(open, high, low, closeadj):
    result = _std((-_rank(high-low, 63)), 252)
    return _clean(result)

# core07 std 5d
def cg_f07_technology_f07_technology_volatility_regime_core07_std_5d_base_v038_signal(open, high, low, closeadj):
    result = _std((_std(_pct_change(closeadj,1),252)), 5)
    return _clean(result)

# core08 std 21d
def cg_f07_technology_f07_technology_volatility_regime_core08_std_21d_base_v039_signal(open, high, low, closeadj):
    result = _std((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 21)
    return _clean(result)

# core09 std 63d
def cg_f07_technology_f07_technology_volatility_regime_core09_std_63d_base_v040_signal(open, high, low, closeadj):
    result = _std((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 63)
    return _clean(result)

# core00 slope 252d
def cg_f07_technology_f07_technology_volatility_regime_core00_slope_252d_base_v041_signal(open, high, low, closeadj):
    result = _slope((_pct_change(closeadj, 1)), 252)
    return _clean(result)

# core01 slope 5d
def cg_f07_technology_f07_technology_volatility_regime_core01_slope_5d_base_v042_signal(open, high, low, closeadj):
    result = _slope((high-low), 5)
    return _clean(result)

# core02 slope 21d
def cg_f07_technology_f07_technology_volatility_regime_core02_slope_21d_base_v043_signal(open, high, low, closeadj):
    result = _slope((_safe_div(high-low, closeadj.abs()+1e-9)), 21)
    return _clean(result)

# core03 slope 63d
def cg_f07_technology_f07_technology_volatility_regime_core03_slope_63d_base_v044_signal(open, high, low, closeadj):
    result = _slope((_std(_pct_change(closeadj, 1),21)), 63)
    return _clean(result)

# core04 slope 126d
def cg_f07_technology_f07_technology_volatility_regime_core04_slope_126d_base_v045_signal(open, high, low, closeadj):
    result = _slope((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 126)
    return _clean(result)

# core05 slope 252d
def cg_f07_technology_f07_technology_volatility_regime_core05_slope_252d_base_v046_signal(open, high, low, closeadj):
    result = _slope((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 252)
    return _clean(result)

# core06 slope 5d
def cg_f07_technology_f07_technology_volatility_regime_core06_slope_5d_base_v047_signal(open, high, low, closeadj):
    result = _slope((-_rank(high-low, 63)), 5)
    return _clean(result)

# core07 slope 21d
def cg_f07_technology_f07_technology_volatility_regime_core07_slope_21d_base_v048_signal(open, high, low, closeadj):
    result = _slope((_std(_pct_change(closeadj,1),252)), 21)
    return _clean(result)

# core08 slope 63d
def cg_f07_technology_f07_technology_volatility_regime_core08_slope_63d_base_v049_signal(open, high, low, closeadj):
    result = _slope((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 63)
    return _clean(result)

# core09 slope 126d
def cg_f07_technology_f07_technology_volatility_regime_core09_slope_126d_base_v050_signal(open, high, low, closeadj):
    result = _slope((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 126)
    return _clean(result)

# core00 diff 5d
def cg_f07_technology_f07_technology_volatility_regime_core00_diff_5d_base_v051_signal(open, high, low, closeadj):
    result = _diff((_pct_change(closeadj, 1)), 5)
    return _clean(result)

# core01 diff 21d
def cg_f07_technology_f07_technology_volatility_regime_core01_diff_21d_base_v052_signal(open, high, low, closeadj):
    result = _diff((high-low), 21)
    return _clean(result)

# core02 diff 63d
def cg_f07_technology_f07_technology_volatility_regime_core02_diff_63d_base_v053_signal(open, high, low, closeadj):
    result = _diff((_safe_div(high-low, closeadj.abs()+1e-9)), 63)
    return _clean(result)

# core03 diff 126d
def cg_f07_technology_f07_technology_volatility_regime_core03_diff_126d_base_v054_signal(open, high, low, closeadj):
    result = _diff((_std(_pct_change(closeadj, 1),21)), 126)
    return _clean(result)

# core04 diff 252d
def cg_f07_technology_f07_technology_volatility_regime_core04_diff_252d_base_v055_signal(open, high, low, closeadj):
    result = _diff((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 252)
    return _clean(result)

# core05 diff 5d
def cg_f07_technology_f07_technology_volatility_regime_core05_diff_5d_base_v056_signal(open, high, low, closeadj):
    result = _diff((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 5)
    return _clean(result)

# core06 diff 21d
def cg_f07_technology_f07_technology_volatility_regime_core06_diff_21d_base_v057_signal(open, high, low, closeadj):
    result = _diff((-_rank(high-low, 63)), 21)
    return _clean(result)

# core07 diff 63d
def cg_f07_technology_f07_technology_volatility_regime_core07_diff_63d_base_v058_signal(open, high, low, closeadj):
    result = _diff((_std(_pct_change(closeadj,1),252)), 63)
    return _clean(result)

# core08 diff 126d
def cg_f07_technology_f07_technology_volatility_regime_core08_diff_126d_base_v059_signal(open, high, low, closeadj):
    result = _diff((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)), 126)
    return _clean(result)

# core09 diff 252d
def cg_f07_technology_f07_technology_volatility_regime_core09_diff_252d_base_v060_signal(open, high, low, closeadj):
    result = _diff((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)), 252)
    return _clean(result)

# core00 pct 21d
def cg_f07_technology_f07_technology_volatility_regime_core00_pct_21d_base_v061_signal(open, high, low, closeadj):
    result = _pct_change(((_pct_change(closeadj, 1)).abs()+1.0), 21)
    return _clean(result)

# core01 pct 63d
def cg_f07_technology_f07_technology_volatility_regime_core01_pct_63d_base_v062_signal(open, high, low, closeadj):
    result = _pct_change(((high-low).abs()+1.0), 63)
    return _clean(result)

# core02 pct 126d
def cg_f07_technology_f07_technology_volatility_regime_core02_pct_126d_base_v063_signal(open, high, low, closeadj):
    result = _pct_change(((_safe_div(high-low, closeadj.abs()+1e-9)).abs()+1.0), 126)
    return _clean(result)

# core03 pct 252d
def cg_f07_technology_f07_technology_volatility_regime_core03_pct_252d_base_v064_signal(open, high, low, closeadj):
    result = _pct_change(((_std(_pct_change(closeadj, 1),21)).abs()+1.0), 252)
    return _clean(result)

# core04 pct 5d
def cg_f07_technology_f07_technology_volatility_regime_core04_pct_5d_base_v065_signal(open, high, low, closeadj):
    result = _pct_change(((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)).abs()+1.0), 5)
    return _clean(result)

# core05 pct 21d
def cg_f07_technology_f07_technology_volatility_regime_core05_pct_21d_base_v066_signal(open, high, low, closeadj):
    result = _pct_change(((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)).abs()+1.0), 21)
    return _clean(result)

# core06 pct 63d
def cg_f07_technology_f07_technology_volatility_regime_core06_pct_63d_base_v067_signal(open, high, low, closeadj):
    result = _pct_change(((-_rank(high-low, 63)).abs()+1.0), 63)
    return _clean(result)

# core07 pct 126d
def cg_f07_technology_f07_technology_volatility_regime_core07_pct_126d_base_v068_signal(open, high, low, closeadj):
    result = _pct_change(((_std(_pct_change(closeadj,1),252)).abs()+1.0), 126)
    return _clean(result)

# core08 pct 252d
def cg_f07_technology_f07_technology_volatility_regime_core08_pct_252d_base_v069_signal(open, high, low, closeadj):
    result = _pct_change(((_z(_std(_pct_change(closeadj,1),252), 63)*_z(_std(_pct_change(closeadj, 1),21),63)).abs()+1.0), 252)
    return _clean(result)

# core09 pct 5d
def cg_f07_technology_f07_technology_volatility_regime_core09_pct_5d_base_v070_signal(open, high, low, closeadj):
    result = _pct_change(((pd.concat([(high-low).abs(),(high-closeadj.shift(1)).abs(),(low-closeadj.shift(1)).abs()],axis=1).max(axis=1)).abs()+1.0), 5)
    return _clean(result)

# core00 ewm 63d
def cg_f07_technology_f07_technology_volatility_regime_core00_ewm_63d_base_v071_signal(open, high, low, closeadj):
    result = _ewm((_pct_change(closeadj, 1)), 63)
    return _clean(result)

# core01 ewm 126d
def cg_f07_technology_f07_technology_volatility_regime_core01_ewm_126d_base_v072_signal(open, high, low, closeadj):
    result = _ewm((high-low), 126)
    return _clean(result)

# core02 ewm 252d
def cg_f07_technology_f07_technology_volatility_regime_core02_ewm_252d_base_v073_signal(open, high, low, closeadj):
    result = _ewm((_safe_div(high-low, closeadj.abs()+1e-9)), 252)
    return _clean(result)

# core03 ewm 5d
def cg_f07_technology_f07_technology_volatility_regime_core03_ewm_5d_base_v074_signal(open, high, low, closeadj):
    result = _ewm((_std(_pct_change(closeadj, 1),21)), 5)
    return _clean(result)

# core04 ewm 21d
def cg_f07_technology_f07_technology_volatility_regime_core04_ewm_21d_base_v075_signal(open, high, low, closeadj):
    result = _ewm((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0)), 21)
    return _clean(result)

