import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 slope mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_mean_5d_slope_v001_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_mean_21d_slope_v002_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_mean_63d_slope_v003_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_mean_126d_slope_v004_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_mean_252d_slope_v005_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_mean_5d_slope_v006_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv - hv
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_mean_21d_slope_v007_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv - hv
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_mean_63d_slope_v008_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv - hv
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_mean_126d_slope_v009_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv - hv
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_mean_252d_slope_v010_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv - hv
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_mean_5d_slope_v011_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv, hv.abs()+1e-9)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core11 slope mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_mean_21d_slope_v012_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv, hv.abs()+1e-9)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_mean_63d_slope_v013_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv, hv.abs()+1e-9)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core13 slope mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_mean_126d_slope_v014_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv, hv.abs()+1e-9)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core14 slope mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_mean_252d_slope_v015_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv, hv.abs()+1e-9)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_mean_5d_slope_v016_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_skew
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_mean_21d_slope_v017_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_skew
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_mean_63d_slope_v018_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_skew
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_mean_126d_slope_v019_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_skew
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_mean_252d_slope_v020_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_skew
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_mean_5d_slope_v021_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_mean_21d_slope_v022_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_mean_63d_slope_v023_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_mean_126d_slope_v024_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_mean_252d_slope_v025_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_mean_5d_slope_v026_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = put_call
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core11 slope mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_mean_21d_slope_v027_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = put_call
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_mean_63d_slope_v028_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = put_call
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core13 slope mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_mean_126d_slope_v029_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = put_call
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core14 slope mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_mean_252d_slope_v030_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = put_call
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_mean_5d_slope_v031_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_rank
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_mean_21d_slope_v032_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_rank
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_mean_63d_slope_v033_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_rank
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_mean_126d_slope_v034_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_rank
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_mean_252d_slope_v035_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_rank
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_mean_5d_slope_v036_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv, 21)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_mean_21d_slope_v037_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv, 21)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_mean_63d_slope_v038_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv, 21)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_mean_126d_slope_v039_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv, 21)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_mean_252d_slope_v040_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv, 21)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_mean_5d_slope_v041_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv_skew, 21)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core11 slope mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_mean_21d_slope_v042_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv_skew, 21)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_mean_63d_slope_v043_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv_skew, 21)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core13 slope mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_mean_126d_slope_v044_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv_skew, 21)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core14 slope mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_mean_252d_slope_v045_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv_skew, 21)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_mean_5d_slope_v046_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(put_call, 21)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_mean_21d_slope_v047_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(put_call, 21)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_mean_63d_slope_v048_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(put_call, 21)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_mean_126d_slope_v049_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(put_call, 21)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_mean_252d_slope_v050_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(put_call, 21)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_mean_5d_slope_v051_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv, 252)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_mean_21d_slope_v052_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv, 252)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_mean_63d_slope_v053_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv, 252)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_mean_126d_slope_v054_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv, 252)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_mean_252d_slope_v055_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv, 252)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_mean_5d_slope_v056_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv_skew, 252)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core11 slope mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_mean_21d_slope_v057_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv_skew, 252)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_mean_63d_slope_v058_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv_skew, 252)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core13 slope mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_mean_126d_slope_v059_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv_skew, 252)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core14 slope mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_mean_252d_slope_v060_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv_skew, 252)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_mean_5d_slope_v061_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(put_call, 252)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_mean_21d_slope_v062_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(put_call, 252)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_mean_63d_slope_v063_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(put_call, 252)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_mean_126d_slope_v064_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(put_call, 252)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_mean_252d_slope_v065_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(put_call, 252)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_mean_5d_slope_v066_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv, 21)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_mean_21d_slope_v067_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv, 21)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_mean_63d_slope_v068_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv, 21)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_mean_126d_slope_v069_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv, 21)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_mean_252d_slope_v070_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv, 21)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_mean_5d_slope_v071_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv_rank, 21)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core11 slope mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_mean_21d_slope_v072_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv_rank, 21)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_mean_63d_slope_v073_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv_rank, 21)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core13 slope mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_mean_126d_slope_v074_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv_rank, 21)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core14 slope mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_mean_252d_slope_v075_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv_rank, 21)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_ewm_5d_slope_v076_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_ewm_21d_slope_v077_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_ewm_63d_slope_v078_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_ewm_126d_slope_v079_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_ewm_252d_slope_v080_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_ewm_5d_slope_v081_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv_skew, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_ewm_21d_slope_v082_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv_skew, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_ewm_63d_slope_v083_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv_skew, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_ewm_126d_slope_v084_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv_skew, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_ewm_252d_slope_v085_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv_skew, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_ewm_5d_slope_v086_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(put_call, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core11 slope ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_ewm_21d_slope_v087_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(put_call, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_ewm_63d_slope_v088_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(put_call, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core13 slope ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_ewm_126d_slope_v089_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(put_call, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core14 slope ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_ewm_252d_slope_v090_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(put_call, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_ewm_5d_slope_v091_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(volume, 5), 63)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_ewm_21d_slope_v092_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(volume, 5), 63)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_ewm_63d_slope_v093_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(volume, 5), 63)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_ewm_126d_slope_v094_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(volume, 5), 63)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_ewm_252d_slope_v095_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(volume, 5), 63)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_ewm_5d_slope_v096_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv, 63)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_ewm_21d_slope_v097_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv, 63)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_ewm_63d_slope_v098_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv, 63)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_ewm_126d_slope_v099_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv, 63)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_ewm_252d_slope_v100_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv, 63)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_ewm_5d_slope_v101_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv_skew, 63)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core11 slope ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_ewm_21d_slope_v102_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv_skew, 63)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_ewm_63d_slope_v103_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv_skew, 63)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core13 slope ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_ewm_126d_slope_v104_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv_skew, 63)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core14 slope ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_ewm_252d_slope_v105_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv_skew, 63)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_ewm_5d_slope_v106_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv, 252)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_ewm_21d_slope_v107_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv, 252)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_ewm_63d_slope_v108_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv, 252)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_ewm_126d_slope_v109_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv, 252)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_ewm_252d_slope_v110_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv, 252)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_ewm_5d_slope_v111_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv_skew, 252)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_ewm_21d_slope_v112_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv_skew, 252)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_ewm_63d_slope_v113_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv_skew, 252)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_ewm_126d_slope_v114_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv_skew, 252)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_ewm_252d_slope_v115_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv_skew, 252)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_ewm_5d_slope_v116_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(put_call, 252)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core11 slope ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_ewm_21d_slope_v117_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(put_call, 252)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_ewm_63d_slope_v118_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(put_call, 252)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core13 slope ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_ewm_126d_slope_v119_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(put_call, 252)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core14 slope ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_ewm_252d_slope_v120_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(put_call, 252)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_ewm_5d_slope_v121_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _std(_diff(iv, 1), 63)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_ewm_21d_slope_v122_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _std(_diff(iv, 1), 63)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_ewm_63d_slope_v123_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _std(_diff(iv, 1), 63)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_ewm_126d_slope_v124_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _std(_diff(iv, 1), 63)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_ewm_252d_slope_v125_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _std(_diff(iv, 1), 63)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_ewm_5d_slope_v126_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _skew(_diff(iv, 1), 252)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_ewm_21d_slope_v127_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _skew(_diff(iv, 1), 252)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_ewm_63d_slope_v128_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _skew(_diff(iv, 1), 252)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_ewm_126d_slope_v129_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _skew(_diff(iv, 1), 252)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_ewm_252d_slope_v130_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _skew(_diff(iv, 1), 252)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_ewm_5d_slope_v131_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _autocorr(iv, 63, 5)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core11 slope ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_ewm_21d_slope_v132_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _autocorr(iv, 63, 5)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_ewm_63d_slope_v133_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _autocorr(iv, 63, 5)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core13 slope ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_ewm_126d_slope_v134_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _autocorr(iv, 63, 5)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core14 slope ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_ewm_252d_slope_v135_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _autocorr(iv, 63, 5)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_ewm_5d_slope_v136_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term - iv
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_ewm_21d_slope_v137_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term - iv
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_ewm_63d_slope_v138_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term - iv
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_ewm_126d_slope_v139_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term - iv
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_ewm_252d_slope_v140_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term - iv
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_ewm_5d_slope_v141_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv_term, iv.abs()+1e-9)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_ewm_21d_slope_v142_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv_term, iv.abs()+1e-9)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_ewm_63d_slope_v143_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv_term, iv.abs()+1e-9)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_ewm_126d_slope_v144_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv_term, iv.abs()+1e-9)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_ewm_252d_slope_v145_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv_term, iv.abs()+1e-9)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_ewm_5d_slope_v146_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core11 slope ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_ewm_21d_slope_v147_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_ewm_63d_slope_v148_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core13 slope ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_ewm_126d_slope_v149_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core14 slope ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_ewm_252d_slope_v150_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

