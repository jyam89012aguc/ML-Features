import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_mean_5d_base_v001_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, sharesbas.abs()+1e-9)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_mean_21d_base_v002_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, sharesbas.abs()+1e-9)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_mean_63d_base_v003_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, sharesbas.abs()+1e-9)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_mean_126d_base_v004_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, sharesbas.abs()+1e-9)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_mean_252d_base_v005_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, sharesbas.abs()+1e-9)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_mean_5d_base_v006_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_float
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_mean_21d_base_v007_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_float
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_mean_63d_base_v008_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_float
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_mean_126d_base_v009_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_float
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_mean_252d_base_v010_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_float
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_mean_5d_base_v011_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_shares
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_mean_21d_base_v012_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_shares
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_mean_63d_base_v013_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_shares
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_mean_126d_base_v014_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_shares
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_mean_252d_base_v015_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = short_pct_shares
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_mean_5d_base_v016_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = days_to_cover
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_mean_21d_base_v017_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = days_to_cover
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_mean_63d_base_v018_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = days_to_cover
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_mean_126d_base_v019_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = days_to_cover
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_mean_252d_base_v020_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = days_to_cover
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_mean_5d_base_v021_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 21)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_mean_21d_base_v022_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 21)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_mean_63d_base_v023_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 21)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_mean_126d_base_v024_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 21)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_mean_252d_base_v025_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 21)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_mean_5d_base_v026_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 63)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_mean_21d_base_v027_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 63)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_mean_63d_base_v028_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 63)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_mean_126d_base_v029_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 63)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_mean_252d_base_v030_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(shortint, 63)
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_mean_5d_base_v031_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 21)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_mean_21d_base_v032_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 21)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_mean_63d_base_v033_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 21)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_mean_126d_base_v034_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 21)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_mean_252d_base_v035_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 21)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_mean_5d_base_v036_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 63)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_mean_21d_base_v037_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 63)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_mean_63d_base_v038_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 63)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_mean_126d_base_v039_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 63)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_mean_252d_base_v040_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(short_pct_float, 63)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_mean_5d_base_v041_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(short_pct_shares, 21)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_mean_21d_base_v042_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(short_pct_shares, 21)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_mean_63d_base_v043_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(short_pct_shares, 21)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_mean_126d_base_v044_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(short_pct_shares, 21)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_mean_252d_base_v045_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(short_pct_shares, 21)
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_mean_5d_base_v046_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(days_to_cover, 21)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_mean_21d_base_v047_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(days_to_cover, 21)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_mean_63d_base_v048_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(days_to_cover, 21)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_mean_126d_base_v049_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(days_to_cover, 21)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_mean_252d_base_v050_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _diff(days_to_cover, 21)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_mean_5d_base_v051_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, volume.abs()+1e-9)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_mean_21d_base_v052_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, volume.abs()+1e-9)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_mean_63d_base_v053_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, volume.abs()+1e-9)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_mean_126d_base_v054_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, volume.abs()+1e-9)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_mean_252d_base_v055_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(shortint, volume.abs()+1e-9)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_mean_5d_base_v056_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(shortint, 252)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_mean_21d_base_v057_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(shortint, 252)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_mean_63d_base_v058_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(shortint, 252)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_mean_126d_base_v059_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(shortint, 252)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_mean_252d_base_v060_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(shortint, 252)
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_mean_5d_base_v061_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(short_pct_float, 252)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_mean_21d_base_v062_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(short_pct_float, 252)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_mean_63d_base_v063_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(short_pct_float, 252)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_mean_126d_base_v064_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(short_pct_float, 252)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_mean_252d_base_v065_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _z(short_pct_float, 252)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_mean_5d_base_v066_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(short_pct_float, _pct_change(closeadj, 21), 63)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_mean_21d_base_v067_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(short_pct_float, _pct_change(closeadj, 21), 63)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_mean_63d_base_v068_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(short_pct_float, _pct_change(closeadj, 21), 63)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_mean_126d_base_v069_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(short_pct_float, _pct_change(closeadj, 21), 63)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_mean_252d_base_v070_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(short_pct_float, _pct_change(closeadj, 21), 63)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_mean_5d_base_v071_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(days_to_cover, _pct_change(closeadj, 5), 63)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_mean_21d_base_v072_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(days_to_cover, _pct_change(closeadj, 5), 63)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_mean_63d_base_v073_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(days_to_cover, _pct_change(closeadj, 5), 63)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_mean_126d_base_v074_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(days_to_cover, _pct_change(closeadj, 5), 63)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_mean_252d_base_v075_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _corr(days_to_cover, _pct_change(closeadj, 5), 63)
    result = _mean(series, 252)
    return _clean(result)

