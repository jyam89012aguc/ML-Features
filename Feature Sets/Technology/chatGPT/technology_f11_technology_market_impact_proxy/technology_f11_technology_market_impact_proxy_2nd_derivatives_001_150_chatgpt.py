import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 slope mean 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core00_mean_5d_slope_v001_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 1).abs(), _safe_div(volume * closeadj, marketcap.abs() + 1e-9) + 1e-9)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core01_mean_21d_slope_v002_signal(closeadj, volume, marketcap):
    series = _safe_div(_std(_pct_change(closeadj, 1),21), _mean(volume * closeadj, 21) + 1e-9) * 1e9
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core02_mean_63d_slope_v003_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,1260).abs()
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core03_mean_126d_slope_v004_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj,252) - _pct_change(closeadj,1260), _std(_pct_change(closeadj,252) - _pct_change(closeadj,1260), 252).abs() + 1e-9)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core04_mean_252d_slope_v005_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core05_mean_5d_slope_v006_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core06_mean_21d_slope_v007_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 63), _std(_pct_change(closeadj,1),252).abs() + 1e-9)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core07_mean_63d_slope_v008_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(marketcap, 63), _pct_change(closeadj,63).abs() + 1e-9)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core08_mean_126d_slope_v009_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 21), _safe_div(volume, _mean(volume, 63) + 1e-9) + 1e-9)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core09_mean_252d_slope_v010_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 21), _diff(_pct_change(closeadj,252),21).abs() + 1e-9)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope z 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core00_z_21d_slope_v011_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 1).abs(), _safe_div(volume * closeadj, marketcap.abs() + 1e-9) + 1e-9)
    base = _z(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope z 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core01_z_63d_slope_v012_signal(closeadj, volume, marketcap):
    series = _safe_div(_std(_pct_change(closeadj, 1),21), _mean(volume * closeadj, 21) + 1e-9) * 1e9
    base = _z(series, 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope z 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core02_z_126d_slope_v013_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,1260).abs()
    base = _z(series, 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope z 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core03_z_252d_slope_v014_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj,252) - _pct_change(closeadj,1260), _std(_pct_change(closeadj,252) - _pct_change(closeadj,1260), 252).abs() + 1e-9)
    base = _z(series, 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope z 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core04_z_5d_slope_v015_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _z(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope z 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core05_z_21d_slope_v016_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _z(series, 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope z 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core06_z_63d_slope_v017_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 63), _std(_pct_change(closeadj,1),252).abs() + 1e-9)
    base = _z(series, 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope z 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core07_z_126d_slope_v018_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(marketcap, 63), _pct_change(closeadj,63).abs() + 1e-9)
    base = _z(series, 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope z 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core08_z_252d_slope_v019_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 21), _safe_div(volume, _mean(volume, 63) + 1e-9) + 1e-9)
    base = _z(series, 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope z 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core09_z_5d_slope_v020_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 21), _diff(_pct_change(closeadj,252),21).abs() + 1e-9)
    base = _z(series, 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope rank 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core00_rank_63d_slope_v021_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 1).abs(), _safe_div(volume * closeadj, marketcap.abs() + 1e-9) + 1e-9)
    base = _rank(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope rank 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core01_rank_126d_slope_v022_signal(closeadj, volume, marketcap):
    series = _safe_div(_std(_pct_change(closeadj, 1),21), _mean(volume * closeadj, 21) + 1e-9) * 1e9
    base = _rank(series, 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope rank 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core02_rank_252d_slope_v023_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,1260).abs()
    base = _rank(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope rank 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core03_rank_5d_slope_v024_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj,252) - _pct_change(closeadj,1260), _std(_pct_change(closeadj,252) - _pct_change(closeadj,1260), 252).abs() + 1e-9)
    base = _rank(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope rank 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core04_rank_21d_slope_v025_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _rank(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope rank 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core05_rank_63d_slope_v026_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _rank(series, 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope rank 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core06_rank_126d_slope_v027_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 63), _std(_pct_change(closeadj,1),252).abs() + 1e-9)
    base = _rank(series, 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope rank 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core07_rank_252d_slope_v028_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(marketcap, 63), _pct_change(closeadj,63).abs() + 1e-9)
    base = _rank(series, 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope rank 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core08_rank_5d_slope_v029_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 21), _safe_div(volume, _mean(volume, 63) + 1e-9) + 1e-9)
    base = _rank(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope rank 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core09_rank_21d_slope_v030_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 21), _diff(_pct_change(closeadj,252),21).abs() + 1e-9)
    base = _rank(series, 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope std 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core00_std_126d_slope_v031_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 1).abs(), _safe_div(volume * closeadj, marketcap.abs() + 1e-9) + 1e-9)
    base = _std(series, 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope std 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core01_std_252d_slope_v032_signal(closeadj, volume, marketcap):
    series = _safe_div(_std(_pct_change(closeadj, 1),21), _mean(volume * closeadj, 21) + 1e-9) * 1e9
    base = _std(series, 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope std 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core02_std_5d_slope_v033_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,1260).abs()
    base = _std(series, 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope std 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core03_std_21d_slope_v034_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj,252) - _pct_change(closeadj,1260), _std(_pct_change(closeadj,252) - _pct_change(closeadj,1260), 252).abs() + 1e-9)
    base = _std(series, 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope std 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core04_std_63d_slope_v035_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _std(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope std 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core05_std_126d_slope_v036_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _std(series, 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope std 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core06_std_252d_slope_v037_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 63), _std(_pct_change(closeadj,1),252).abs() + 1e-9)
    base = _std(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope std 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core07_std_5d_slope_v038_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(marketcap, 63), _pct_change(closeadj,63).abs() + 1e-9)
    base = _std(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope std 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core08_std_21d_slope_v039_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 21), _safe_div(volume, _mean(volume, 63) + 1e-9) + 1e-9)
    base = _std(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope std 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core09_std_63d_slope_v040_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 21), _diff(_pct_change(closeadj,252),21).abs() + 1e-9)
    base = _std(series, 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope delta 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core00_delta_252d_slope_v041_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 1).abs(), _safe_div(volume * closeadj, marketcap.abs() + 1e-9) + 1e-9)
    base = _diff(series, 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope delta 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core01_delta_5d_slope_v042_signal(closeadj, volume, marketcap):
    series = _safe_div(_std(_pct_change(closeadj, 1),21), _mean(volume * closeadj, 21) + 1e-9) * 1e9
    base = _diff(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope delta 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core02_delta_21d_slope_v043_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,1260).abs()
    base = _diff(series, 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope delta 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core03_delta_63d_slope_v044_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj,252) - _pct_change(closeadj,1260), _std(_pct_change(closeadj,252) - _pct_change(closeadj,1260), 252).abs() + 1e-9)
    base = _diff(series, 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope delta 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core04_delta_126d_slope_v045_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _diff(series, 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope delta 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core05_delta_252d_slope_v046_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _diff(series, 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope delta 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core06_delta_5d_slope_v047_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 63), _std(_pct_change(closeadj,1),252).abs() + 1e-9)
    base = _diff(series, 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope delta 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core07_delta_21d_slope_v048_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(marketcap, 63), _pct_change(closeadj,63).abs() + 1e-9)
    base = _diff(series, 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope delta 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core08_delta_63d_slope_v049_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 21), _safe_div(volume, _mean(volume, 63) + 1e-9) + 1e-9)
    base = _diff(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope delta 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core09_delta_126d_slope_v050_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 21), _diff(_pct_change(closeadj,252),21).abs() + 1e-9)
    base = _diff(series, 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope pct 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core00_pct_5d_slope_v051_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 1).abs(), _safe_div(volume * closeadj, marketcap.abs() + 1e-9) + 1e-9)
    base = _pct_change(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope pct 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core01_pct_21d_slope_v052_signal(closeadj, volume, marketcap):
    series = _safe_div(_std(_pct_change(closeadj, 1),21), _mean(volume * closeadj, 21) + 1e-9) * 1e9
    base = _pct_change(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope pct 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core02_pct_63d_slope_v053_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,1260).abs()
    base = _pct_change(series, 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope pct 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core03_pct_126d_slope_v054_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj,252) - _pct_change(closeadj,1260), _std(_pct_change(closeadj,252) - _pct_change(closeadj,1260), 252).abs() + 1e-9)
    base = _pct_change(series, 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope pct 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core04_pct_252d_slope_v055_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _pct_change(series, 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope pct 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core05_pct_5d_slope_v056_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _pct_change(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope pct 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core06_pct_21d_slope_v057_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 63), _std(_pct_change(closeadj,1),252).abs() + 1e-9)
    base = _pct_change(series, 21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope pct 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core07_pct_63d_slope_v058_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(marketcap, 63), _pct_change(closeadj,63).abs() + 1e-9)
    base = _pct_change(series, 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope pct 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core08_pct_126d_slope_v059_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 21), _safe_div(volume, _mean(volume, 63) + 1e-9) + 1e-9)
    base = _pct_change(series, 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope pct 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core09_pct_252d_slope_v060_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 21), _diff(_pct_change(closeadj,252),21).abs() + 1e-9)
    base = _pct_change(series, 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core00_ewm_21d_slope_v061_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 1).abs(), _safe_div(volume * closeadj, marketcap.abs() + 1e-9) + 1e-9)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core01_ewm_63d_slope_v062_signal(closeadj, volume, marketcap):
    series = _safe_div(_std(_pct_change(closeadj, 1),21), _mean(volume * closeadj, 21) + 1e-9) * 1e9
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core02_ewm_126d_slope_v063_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,1260).abs()
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core03_ewm_252d_slope_v064_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj,252) - _pct_change(closeadj,1260), _std(_pct_change(closeadj,252) - _pct_change(closeadj,1260), 252).abs() + 1e-9)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core04_ewm_5d_slope_v065_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core05_ewm_21d_slope_v066_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core06_ewm_63d_slope_v067_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 63), _std(_pct_change(closeadj,1),252).abs() + 1e-9)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core07_ewm_126d_slope_v068_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(marketcap, 63), _pct_change(closeadj,63).abs() + 1e-9)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core08_ewm_252d_slope_v069_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 21), _safe_div(volume, _mean(volume, 63) + 1e-9) + 1e-9)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core09_ewm_5d_slope_v070_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 21), _diff(_pct_change(closeadj,252),21).abs() + 1e-9)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope slope 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core00_slope_63d_slope_v071_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 1).abs(), _safe_div(volume * closeadj, marketcap.abs() + 1e-9) + 1e-9)
    base = _slope(series, 63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope slope 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core01_slope_126d_slope_v072_signal(closeadj, volume, marketcap):
    series = _safe_div(_std(_pct_change(closeadj, 1),21), _mean(volume * closeadj, 21) + 1e-9) * 1e9
    base = _slope(series, 126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope slope 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core02_slope_252d_slope_v073_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,1260).abs()
    base = _slope(series, 252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope slope 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core03_slope_5d_slope_v074_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj,252) - _pct_change(closeadj,1260), _std(_pct_change(closeadj,252) - _pct_change(closeadj,1260), 252).abs() + 1e-9)
    base = _slope(series, 5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope slope 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core04_slope_21d_slope_v075_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _slope(series, 21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope slope 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core05_slope_63d_slope_v076_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _slope(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope slope 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core06_slope_126d_slope_v077_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 63), _std(_pct_change(closeadj,1),252).abs() + 1e-9)
    base = _slope(series, 126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope slope 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core07_slope_252d_slope_v078_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(marketcap, 63), _pct_change(closeadj,63).abs() + 1e-9)
    base = _slope(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope slope 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core08_slope_5d_slope_v079_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 21), _safe_div(volume, _mean(volume, 63) + 1e-9) + 1e-9)
    base = _slope(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope slope 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core09_slope_21d_slope_v080_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 21), _diff(_pct_change(closeadj,252),21).abs() + 1e-9)
    base = _slope(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope abs_mean 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core00_abs_mean_126d_slope_v081_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 1).abs(), _safe_div(volume * closeadj, marketcap.abs() + 1e-9) + 1e-9)
    base = _mean(series.abs(),126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope abs_mean 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core01_abs_mean_252d_slope_v082_signal(closeadj, volume, marketcap):
    series = _safe_div(_std(_pct_change(closeadj, 1),21), _mean(volume * closeadj, 21) + 1e-9) * 1e9
    base = _mean(series.abs(),252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope abs_mean 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core02_abs_mean_5d_slope_v083_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,1260).abs()
    base = _mean(series.abs(),5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope abs_mean 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core03_abs_mean_21d_slope_v084_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj,252) - _pct_change(closeadj,1260), _std(_pct_change(closeadj,252) - _pct_change(closeadj,1260), 252).abs() + 1e-9)
    base = _mean(series.abs(),21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope abs_mean 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core04_abs_mean_63d_slope_v085_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _mean(series.abs(),63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope abs_mean 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core05_abs_mean_126d_slope_v086_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _mean(series.abs(),126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope abs_mean 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core06_abs_mean_252d_slope_v087_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 63), _std(_pct_change(closeadj,1),252).abs() + 1e-9)
    base = _mean(series.abs(),252)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope abs_mean 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core07_abs_mean_5d_slope_v088_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(marketcap, 63), _pct_change(closeadj,63).abs() + 1e-9)
    base = _mean(series.abs(),5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope abs_mean 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core08_abs_mean_21d_slope_v089_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 21), _safe_div(volume, _mean(volume, 63) + 1e-9) + 1e-9)
    base = _mean(series.abs(),21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope abs_mean 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core09_abs_mean_63d_slope_v090_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 21), _diff(_pct_change(closeadj,252),21).abs() + 1e-9)
    base = _mean(series.abs(),63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope pos_mag 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core00_pos_mag_252d_slope_v091_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 1).abs(), _safe_div(volume * closeadj, marketcap.abs() + 1e-9) + 1e-9)
    base = _mean(series.where(series>0, 0),252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope pos_mag 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core01_pos_mag_5d_slope_v092_signal(closeadj, volume, marketcap):
    series = _safe_div(_std(_pct_change(closeadj, 1),21), _mean(volume * closeadj, 21) + 1e-9) * 1e9
    base = _mean(series.where(series>0, 0),5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope pos_mag 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core02_pos_mag_21d_slope_v093_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,1260).abs()
    base = _mean(series.where(series>0, 0),21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope pos_mag 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core03_pos_mag_63d_slope_v094_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj,252) - _pct_change(closeadj,1260), _std(_pct_change(closeadj,252) - _pct_change(closeadj,1260), 252).abs() + 1e-9)
    base = _mean(series.where(series>0, 0),63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope pos_mag 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core04_pos_mag_126d_slope_v095_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _mean(series.where(series>0, 0),126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope pos_mag 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core05_pos_mag_252d_slope_v096_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _mean(series.where(series>0, 0),252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope pos_mag 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core06_pos_mag_5d_slope_v097_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 63), _std(_pct_change(closeadj,1),252).abs() + 1e-9)
    base = _mean(series.where(series>0, 0),5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope pos_mag 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core07_pos_mag_21d_slope_v098_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(marketcap, 63), _pct_change(closeadj,63).abs() + 1e-9)
    base = _mean(series.where(series>0, 0),21)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope pos_mag 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core08_pos_mag_63d_slope_v099_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 21), _safe_div(volume, _mean(volume, 63) + 1e-9) + 1e-9)
    base = _mean(series.where(series>0, 0),63)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope pos_mag 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core09_pos_mag_126d_slope_v100_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 21), _diff(_pct_change(closeadj,252),21).abs() + 1e-9)
    base = _mean(series.where(series>0, 0),126)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope neg_mag 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core00_neg_mag_5d_slope_v101_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 1).abs(), _safe_div(volume * closeadj, marketcap.abs() + 1e-9) + 1e-9)
    base = _mean((series.where(series<0, 0).abs() ** 2),5)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope neg_mag 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core01_neg_mag_21d_slope_v102_signal(closeadj, volume, marketcap):
    series = _safe_div(_std(_pct_change(closeadj, 1),21), _mean(volume * closeadj, 21) + 1e-9) * 1e9
    base = _mean((series.where(series<0, 0).abs() ** 2),21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope neg_mag 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core02_neg_mag_63d_slope_v103_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,1260).abs()
    base = _mean((series.where(series<0, 0).abs() ** 2),63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope neg_mag 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core03_neg_mag_126d_slope_v104_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj,252) - _pct_change(closeadj,1260), _std(_pct_change(closeadj,252) - _pct_change(closeadj,1260), 252).abs() + 1e-9)
    base = _mean((series.where(series<0, 0).abs() ** 2),126)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope neg_mag 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core04_neg_mag_252d_slope_v105_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _mean((series.where(series<0, 0).abs() ** 2),252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope neg_mag 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core05_neg_mag_5d_slope_v106_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _mean((series.where(series<0, 0).abs() ** 2),5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope neg_mag 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core06_neg_mag_21d_slope_v107_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 63), _std(_pct_change(closeadj,1),252).abs() + 1e-9)
    base = _mean((series.where(series<0, 0).abs() ** 2),21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope neg_mag 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core07_neg_mag_63d_slope_v108_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(marketcap, 63), _pct_change(closeadj,63).abs() + 1e-9)
    base = _mean((series.where(series<0, 0).abs() ** 2),63)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope neg_mag 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core08_neg_mag_126d_slope_v109_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 21), _safe_div(volume, _mean(volume, 63) + 1e-9) + 1e-9)
    base = _mean((series.where(series<0, 0).abs() ** 2),126)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope neg_mag 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core09_neg_mag_252d_slope_v110_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 21), _diff(_pct_change(closeadj,252),21).abs() + 1e-9)
    base = _mean((series.where(series<0, 0).abs() ** 2),252)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope vol_ratio 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core00_vol_ratio_21d_slope_v111_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 1).abs(), _safe_div(volume * closeadj, marketcap.abs() + 1e-9) + 1e-9)
    base = _safe_div(_std(series, 21), _mean(series.abs(),21) + 1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope vol_ratio 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core01_vol_ratio_63d_slope_v112_signal(closeadj, volume, marketcap):
    series = _safe_div(_std(_pct_change(closeadj, 1),21), _mean(volume * closeadj, 21) + 1e-9) * 1e9
    base = _safe_div(_std(series, 63), _mean(series.abs(),63) + 1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope vol_ratio 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core02_vol_ratio_126d_slope_v113_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,1260).abs()
    base = _safe_div(_std(series, 126), _mean(series.abs(),126) + 1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope vol_ratio 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core03_vol_ratio_252d_slope_v114_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj,252) - _pct_change(closeadj,1260), _std(_pct_change(closeadj,252) - _pct_change(closeadj,1260), 252).abs() + 1e-9)
    base = _safe_div(_std(series, 252), _mean(series.abs(),252) + 1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope vol_ratio 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core04_vol_ratio_5d_slope_v115_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _safe_div(_std(series, 5), _mean(series.abs(),5) + 1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope vol_ratio 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core05_vol_ratio_21d_slope_v116_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _safe_div(_std(series, 21), _mean(series.abs(),21) + 1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope vol_ratio 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core06_vol_ratio_63d_slope_v117_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 63), _std(_pct_change(closeadj,1),252).abs() + 1e-9)
    base = _safe_div(_std(series, 63), _mean(series.abs(),63) + 1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope vol_ratio 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core07_vol_ratio_126d_slope_v118_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(marketcap, 63), _pct_change(closeadj,63).abs() + 1e-9)
    base = _safe_div(_std(series, 126), _mean(series.abs(),126) + 1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope vol_ratio 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core08_vol_ratio_252d_slope_v119_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 21), _safe_div(volume, _mean(volume, 63) + 1e-9) + 1e-9)
    base = _safe_div(_std(series, 252), _mean(series.abs(),252) + 1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope vol_ratio 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core09_vol_ratio_5d_slope_v120_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 21), _diff(_pct_change(closeadj,252),21).abs() + 1e-9)
    base = _safe_div(_std(series, 5), _mean(series.abs(),5) + 1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core00 slope recent_vs_long 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core00_recent_vs_long_63d_slope_v121_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 1).abs(), _safe_div(volume * closeadj, marketcap.abs() + 1e-9) + 1e-9)
    base = _safe_div(_mean(series, 63), _mean(series, 126) + 1e-9) - 1.0
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope recent_vs_long 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core01_recent_vs_long_126d_slope_v122_signal(closeadj, volume, marketcap):
    series = _safe_div(_std(_pct_change(closeadj, 1),21), _mean(volume * closeadj, 21) + 1e-9) * 1e9
    base = _safe_div(_mean(series, 126), _mean(series, 252) + 1e-9) - 1.0
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core02 slope recent_vs_long 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core02_recent_vs_long_252d_slope_v123_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,1260).abs()
    base = _safe_div(_mean(series, 252), _mean(series, 504) + 1e-9) - 1.0
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core03 slope recent_vs_long 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core03_recent_vs_long_5d_slope_v124_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj,252) - _pct_change(closeadj,1260), _std(_pct_change(closeadj,252) - _pct_change(closeadj,1260), 252).abs() + 1e-9)
    base = _safe_div(_mean(series, 5), _mean(series, 10) + 1e-9) - 1.0
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core04 slope recent_vs_long 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core04_recent_vs_long_21d_slope_v125_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _safe_div(_mean(series, 21), _mean(series, 42) + 1e-9) - 1.0
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core05 slope recent_vs_long 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core05_recent_vs_long_63d_slope_v126_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _safe_div(_mean(series, 63), _mean(series, 126) + 1e-9) - 1.0
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core06 slope recent_vs_long 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core06_recent_vs_long_126d_slope_v127_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 63), _std(_pct_change(closeadj,1),252).abs() + 1e-9)
    base = _safe_div(_mean(series, 126), _mean(series, 252) + 1e-9) - 1.0
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core07 slope recent_vs_long 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core07_recent_vs_long_252d_slope_v128_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(marketcap, 63), _pct_change(closeadj,63).abs() + 1e-9)
    base = _safe_div(_mean(series, 252), _mean(series, 504) + 1e-9) - 1.0
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope recent_vs_long 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core08_recent_vs_long_5d_slope_v129_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 21), _safe_div(volume, _mean(volume, 63) + 1e-9) + 1e-9)
    base = _safe_div(_mean(series, 5), _mean(series, 10) + 1e-9) - 1.0
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core09 slope recent_vs_long 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core09_recent_vs_long_21d_slope_v130_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 21), _diff(_pct_change(closeadj,252),21).abs() + 1e-9)
    base = _safe_div(_mean(series, 21), _mean(series, 42) + 1e-9) - 1.0
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope accel 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core00_accel_126d_slope_v131_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 1).abs(), _safe_div(volume * closeadj, marketcap.abs() + 1e-9) + 1e-9)
    base = _diff(_diff(series, 42),42)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core01 slope accel 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core01_accel_252d_slope_v132_signal(closeadj, volume, marketcap):
    series = _safe_div(_std(_pct_change(closeadj, 1),21), _mean(volume * closeadj, 21) + 1e-9) * 1e9
    base = _diff(_diff(series, 84),84)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core02 slope accel 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core02_accel_5d_slope_v133_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,1260).abs()
    base = _diff(_diff(series, 1),1)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope accel 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core03_accel_21d_slope_v134_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj,252) - _pct_change(closeadj,1260), _std(_pct_change(closeadj,252) - _pct_change(closeadj,1260), 252).abs() + 1e-9)
    base = _diff(_diff(series, 7),7)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core04 slope accel 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core04_accel_63d_slope_v135_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _diff(_diff(series, 21),21)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope accel 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core05_accel_126d_slope_v136_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _diff(_diff(series, 42),42)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope accel 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core06_accel_252d_slope_v137_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 63), _std(_pct_change(closeadj,1),252).abs() + 1e-9)
    base = _diff(_diff(series, 84),84)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope accel 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core07_accel_5d_slope_v138_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(marketcap, 63), _pct_change(closeadj,63).abs() + 1e-9)
    base = _diff(_diff(series, 1),1)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core08 slope accel 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core08_accel_21d_slope_v139_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 21), _safe_div(volume, _mean(volume, 63) + 1e-9) + 1e-9)
    base = _diff(_diff(series, 7),7)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core09 slope accel 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core09_accel_63d_slope_v140_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 21), _diff(_pct_change(closeadj,252),21).abs() + 1e-9)
    base = _diff(_diff(series, 21),21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core00 slope range_norm 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core00_range_norm_252d_slope_v141_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 1).abs(), _safe_div(volume * closeadj, marketcap.abs() + 1e-9) + 1e-9)
    base = _safe_div(series - _mean(series, 252), (_max(series, 252) - _min(series, 252)).abs() + 1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope range_norm 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core01_range_norm_5d_slope_v142_signal(closeadj, volume, marketcap):
    series = _safe_div(_std(_pct_change(closeadj, 1),21), _mean(volume * closeadj, 21) + 1e-9) * 1e9
    base = _safe_div(series - _mean(series, 5), (_max(series, 5) - _min(series, 5)).abs() + 1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope range_norm 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core02_range_norm_21d_slope_v143_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,1260).abs()
    base = _safe_div(series - _mean(series, 21), (_max(series, 21) - _min(series, 21)).abs() + 1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core03 slope range_norm 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core03_range_norm_63d_slope_v144_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj,252) - _pct_change(closeadj,1260), _std(_pct_change(closeadj,252) - _pct_change(closeadj,1260), 252).abs() + 1e-9)
    base = _safe_div(series - _mean(series, 63), (_max(series, 63) - _min(series, 63)).abs() + 1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core04 slope range_norm 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core04_range_norm_126d_slope_v145_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _safe_div(series - _mean(series, 126), (_max(series, 126) - _min(series, 126)).abs() + 1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core05 slope range_norm 252d
def cg_f11_technology_f11_technology_market_impact_proxy_core05_range_norm_252d_slope_v146_signal(closeadj, volume, marketcap):
    series = _pct_change(closeadj,63)
    base = _safe_div(series - _mean(series, 252), (_max(series, 252) - _min(series, 252)).abs() + 1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope range_norm 5d
def cg_f11_technology_f11_technology_market_impact_proxy_core06_range_norm_5d_slope_v147_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 63), _std(_pct_change(closeadj,1),252).abs() + 1e-9)
    base = _safe_div(series - _mean(series, 5), (_max(series, 5) - _min(series, 5)).abs() + 1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core07 slope range_norm 21d
def cg_f11_technology_f11_technology_market_impact_proxy_core07_range_norm_21d_slope_v148_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(marketcap, 63), _pct_change(closeadj,63).abs() + 1e-9)
    base = _safe_div(series - _mean(series, 21), (_max(series, 21) - _min(series, 21)).abs() + 1e-9)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core08 slope range_norm 63d
def cg_f11_technology_f11_technology_market_impact_proxy_core08_range_norm_63d_slope_v149_signal(closeadj, volume, marketcap):
    series = _safe_div(_pct_change(closeadj, 21), _safe_div(volume, _mean(volume, 63) + 1e-9) + 1e-9)
    base = _safe_div(series - _mean(series, 63), (_max(series, 63) - _min(series, 63)).abs() + 1e-9)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core09 slope range_norm 126d
def cg_f11_technology_f11_technology_market_impact_proxy_core09_range_norm_126d_slope_v150_signal(closeadj, volume, marketcap):
    series = _safe_div(_diff(_pct_change(closeadj,252), 21), _diff(_pct_change(closeadj,252),21).abs() + 1e-9)
    base = _safe_div(series - _mean(series, 126), (_max(series, 126) - _min(series, 126)).abs() + 1e-9)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

