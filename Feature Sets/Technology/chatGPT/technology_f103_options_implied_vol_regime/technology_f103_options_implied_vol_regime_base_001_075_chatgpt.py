import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_mean_5d_base_v001_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_mean_21d_base_v002_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_mean_63d_base_v003_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_mean_126d_base_v004_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_mean_252d_base_v005_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_mean_5d_base_v006_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv - hv
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_mean_21d_base_v007_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv - hv
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_mean_63d_base_v008_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv - hv
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_mean_126d_base_v009_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv - hv
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_mean_252d_base_v010_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv - hv
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_mean_5d_base_v011_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv, hv.abs()+1e-9)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_mean_21d_base_v012_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv, hv.abs()+1e-9)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_mean_63d_base_v013_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv, hv.abs()+1e-9)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_mean_126d_base_v014_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv, hv.abs()+1e-9)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_mean_252d_base_v015_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv, hv.abs()+1e-9)
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_mean_5d_base_v016_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_skew
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_mean_21d_base_v017_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_skew
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_mean_63d_base_v018_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_skew
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_mean_126d_base_v019_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_skew
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_mean_252d_base_v020_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_skew
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_mean_5d_base_v021_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_mean_21d_base_v022_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_mean_63d_base_v023_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_mean_126d_base_v024_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_mean_252d_base_v025_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_mean_5d_base_v026_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = put_call
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_mean_21d_base_v027_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = put_call
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_mean_63d_base_v028_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = put_call
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_mean_126d_base_v029_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = put_call
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_mean_252d_base_v030_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = put_call
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_mean_5d_base_v031_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_rank
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_mean_21d_base_v032_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_rank
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_mean_63d_base_v033_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_rank
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_mean_126d_base_v034_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_rank
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_mean_252d_base_v035_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_rank
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_mean_5d_base_v036_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv, 21)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_mean_21d_base_v037_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv, 21)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_mean_63d_base_v038_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv, 21)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_mean_126d_base_v039_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv, 21)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_mean_252d_base_v040_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv, 21)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_mean_5d_base_v041_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv_skew, 21)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_mean_21d_base_v042_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv_skew, 21)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_mean_63d_base_v043_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv_skew, 21)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_mean_126d_base_v044_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv_skew, 21)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_mean_252d_base_v045_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(iv_skew, 21)
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_mean_5d_base_v046_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(put_call, 21)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_mean_21d_base_v047_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(put_call, 21)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_mean_63d_base_v048_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(put_call, 21)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_mean_126d_base_v049_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(put_call, 21)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_mean_252d_base_v050_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _diff(put_call, 21)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_mean_5d_base_v051_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv, 252)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_mean_21d_base_v052_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv, 252)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_mean_63d_base_v053_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv, 252)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_mean_126d_base_v054_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv, 252)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_mean_252d_base_v055_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv, 252)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_mean_5d_base_v056_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv_skew, 252)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_mean_21d_base_v057_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv_skew, 252)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_mean_63d_base_v058_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv_skew, 252)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_mean_126d_base_v059_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv_skew, 252)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_mean_252d_base_v060_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(iv_skew, 252)
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_mean_5d_base_v061_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(put_call, 252)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_mean_21d_base_v062_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(put_call, 252)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_mean_63d_base_v063_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(put_call, 252)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_mean_126d_base_v064_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(put_call, 252)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_mean_252d_base_v065_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _z(put_call, 252)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_mean_5d_base_v066_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv, 21)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_mean_21d_base_v067_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv, 21)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_mean_63d_base_v068_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv, 21)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_mean_126d_base_v069_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv, 21)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_mean_252d_base_v070_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv, 21)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_mean_5d_base_v071_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv_rank, 21)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_mean_21d_base_v072_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv_rank, 21)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_mean_63d_base_v073_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv_rank, 21)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_mean_126d_base_v074_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv_rank, 21)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_mean_252d_base_v075_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(iv_rank, 21)
    result = _mean(series, 252)
    return _clean(result)

