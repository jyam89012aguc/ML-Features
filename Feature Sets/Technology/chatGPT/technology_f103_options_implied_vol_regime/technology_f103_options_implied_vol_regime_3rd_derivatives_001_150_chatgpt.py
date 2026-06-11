import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 accel mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_mean_5d_accel_v001_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_mean_21d_accel_v002_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_mean_63d_accel_v003_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_mean_126d_accel_v004_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_mean_252d_accel_v005_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_mean_5d_accel_v006_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv - hv
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_mean_21d_accel_v007_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv - hv
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_mean_63d_accel_v008_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv - hv
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_mean_126d_accel_v009_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv - hv
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_mean_252d_accel_v010_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv - hv
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_mean_5d_accel_v011_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv, hv.abs()+1e-9)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_mean_21d_accel_v012_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv, hv.abs()+1e-9)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_mean_63d_accel_v013_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv, hv.abs()+1e-9)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_mean_126d_accel_v014_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv, hv.abs()+1e-9)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_mean_252d_accel_v015_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv, hv.abs()+1e-9)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_mean_5d_accel_v016_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_skew
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_mean_21d_accel_v017_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_skew
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_mean_63d_accel_v018_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_skew
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_mean_126d_accel_v019_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_skew
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_mean_252d_accel_v020_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_skew
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_mean_5d_accel_v021_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_mean_21d_accel_v022_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_mean_63d_accel_v023_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_mean_126d_accel_v024_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_mean_252d_accel_v025_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_mean_5d_accel_v026_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = put_call
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_mean_21d_accel_v027_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = put_call
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_mean_63d_accel_v028_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = put_call
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_mean_126d_accel_v029_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = put_call
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_mean_252d_accel_v030_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = put_call
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_mean_5d_accel_v031_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_rank
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_mean_21d_accel_v032_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_rank
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_mean_63d_accel_v033_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_rank
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_mean_126d_accel_v034_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_rank
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_mean_252d_accel_v035_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_rank
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_mean_5d_accel_v036_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv, 21)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_mean_21d_accel_v037_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv, 21)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_mean_63d_accel_v038_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv, 21)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_mean_126d_accel_v039_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv, 21)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_mean_252d_accel_v040_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv, 21)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_mean_5d_accel_v041_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv_skew, 21)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_mean_21d_accel_v042_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv_skew, 21)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_mean_63d_accel_v043_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv_skew, 21)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_mean_126d_accel_v044_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv_skew, 21)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_mean_252d_accel_v045_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv_skew, 21)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_mean_5d_accel_v046_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(put_call, 21)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_mean_21d_accel_v047_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(put_call, 21)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_mean_63d_accel_v048_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(put_call, 21)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_mean_126d_accel_v049_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(put_call, 21)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_mean_252d_accel_v050_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(put_call, 21)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_mean_5d_accel_v051_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv, 252)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_mean_21d_accel_v052_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv, 252)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_mean_63d_accel_v053_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv, 252)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_mean_126d_accel_v054_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv, 252)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_mean_252d_accel_v055_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv, 252)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_mean_5d_accel_v056_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv_skew, 252)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_mean_21d_accel_v057_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv_skew, 252)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_mean_63d_accel_v058_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv_skew, 252)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_mean_126d_accel_v059_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv_skew, 252)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_mean_252d_accel_v060_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv_skew, 252)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_mean_5d_accel_v061_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(put_call, 252)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_mean_21d_accel_v062_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(put_call, 252)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_mean_63d_accel_v063_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(put_call, 252)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_mean_126d_accel_v064_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(put_call, 252)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_mean_252d_accel_v065_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(put_call, 252)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_mean_5d_accel_v066_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv, 21)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_mean_21d_accel_v067_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv, 21)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_mean_63d_accel_v068_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv, 21)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_mean_126d_accel_v069_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv, 21)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_mean_252d_accel_v070_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv, 21)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_mean_5d_accel_v071_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv_rank, 21)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_mean_21d_accel_v072_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv_rank, 21)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_mean_63d_accel_v073_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv_rank, 21)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_mean_126d_accel_v074_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv_rank, 21)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_mean_252d_accel_v075_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv_rank, 21)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_ewm_5d_accel_v076_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_ewm_21d_accel_v077_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_ewm_63d_accel_v078_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_ewm_126d_accel_v079_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_ewm_252d_accel_v080_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_ewm_5d_accel_v081_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv_skew, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_ewm_21d_accel_v082_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv_skew, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_ewm_63d_accel_v083_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv_skew, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_ewm_126d_accel_v084_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv_skew, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_ewm_252d_accel_v085_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv_skew, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_ewm_5d_accel_v086_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(put_call, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_ewm_21d_accel_v087_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(put_call, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_ewm_63d_accel_v088_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(put_call, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_ewm_126d_accel_v089_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(put_call, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_ewm_252d_accel_v090_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(put_call, _pct_change(closeadj, 5), 63)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_ewm_5d_accel_v091_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(volume, 5), 63)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_ewm_21d_accel_v092_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(volume, 5), 63)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_ewm_63d_accel_v093_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(volume, 5), 63)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_ewm_126d_accel_v094_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(volume, 5), 63)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_ewm_252d_accel_v095_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(volume, 5), 63)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_ewm_5d_accel_v096_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv, 63)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_ewm_21d_accel_v097_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv, 63)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_ewm_63d_accel_v098_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv, 63)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_ewm_126d_accel_v099_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv, 63)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_ewm_252d_accel_v100_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv, 63)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_ewm_5d_accel_v101_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv_skew, 63)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_ewm_21d_accel_v102_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv_skew, 63)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_ewm_63d_accel_v103_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv_skew, 63)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_ewm_126d_accel_v104_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv_skew, 63)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_ewm_252d_accel_v105_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv_skew, 63)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_ewm_5d_accel_v106_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv, 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_ewm_21d_accel_v107_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv, 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_ewm_63d_accel_v108_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv, 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_ewm_126d_accel_v109_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv, 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_ewm_252d_accel_v110_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv, 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_ewm_5d_accel_v111_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv_skew, 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_ewm_21d_accel_v112_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv_skew, 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_ewm_63d_accel_v113_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv_skew, 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_ewm_126d_accel_v114_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv_skew, 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_ewm_252d_accel_v115_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv_skew, 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_ewm_5d_accel_v116_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(put_call, 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_ewm_21d_accel_v117_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(put_call, 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_ewm_63d_accel_v118_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(put_call, 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_ewm_126d_accel_v119_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(put_call, 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_ewm_252d_accel_v120_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(put_call, 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_ewm_5d_accel_v121_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _std(_diff(iv, 1), 63)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_ewm_21d_accel_v122_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _std(_diff(iv, 1), 63)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_ewm_63d_accel_v123_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _std(_diff(iv, 1), 63)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_ewm_126d_accel_v124_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _std(_diff(iv, 1), 63)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_ewm_252d_accel_v125_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _std(_diff(iv, 1), 63)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_ewm_5d_accel_v126_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _skew(_diff(iv, 1), 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_ewm_21d_accel_v127_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _skew(_diff(iv, 1), 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_ewm_63d_accel_v128_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _skew(_diff(iv, 1), 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_ewm_126d_accel_v129_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _skew(_diff(iv, 1), 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_ewm_252d_accel_v130_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _skew(_diff(iv, 1), 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_ewm_5d_accel_v131_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _autocorr(iv, 63, 5)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_ewm_21d_accel_v132_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _autocorr(iv, 63, 5)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_ewm_63d_accel_v133_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _autocorr(iv, 63, 5)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_ewm_126d_accel_v134_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _autocorr(iv, 63, 5)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_ewm_252d_accel_v135_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _autocorr(iv, 63, 5)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_ewm_5d_accel_v136_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term - iv
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_ewm_21d_accel_v137_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term - iv
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_ewm_63d_accel_v138_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term - iv
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_ewm_126d_accel_v139_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term - iv
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_ewm_252d_accel_v140_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term - iv
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_ewm_5d_accel_v141_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv_term, iv.abs()+1e-9)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_ewm_21d_accel_v142_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv_term, iv.abs()+1e-9)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_ewm_63d_accel_v143_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv_term, iv.abs()+1e-9)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_ewm_126d_accel_v144_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv_term, iv.abs()+1e-9)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_ewm_252d_accel_v145_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv_term, iv.abs()+1e-9)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_ewm_5d_accel_v146_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_ewm_21d_accel_v147_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_ewm_63d_accel_v148_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_ewm_126d_accel_v149_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_ewm_252d_accel_v150_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

