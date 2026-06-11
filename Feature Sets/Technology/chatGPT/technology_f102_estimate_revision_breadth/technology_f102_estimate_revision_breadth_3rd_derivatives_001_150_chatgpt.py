import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 accel mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_mean_5d_accel_v001_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 21)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_mean_21d_accel_v002_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 21)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_mean_63d_accel_v003_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 21)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_mean_126d_accel_v004_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 21)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_mean_252d_accel_v005_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 21)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_mean_5d_accel_v006_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 63)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_mean_21d_accel_v007_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 63)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_mean_63d_accel_v008_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 63)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_mean_126d_accel_v009_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 63)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_mean_252d_accel_v010_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 63)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_mean_5d_accel_v011_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 21)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_mean_21d_accel_v012_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 21)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_mean_63d_accel_v013_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 21)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_mean_126d_accel_v014_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 21)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_mean_252d_accel_v015_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 21)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_mean_5d_accel_v016_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 63)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_mean_21d_accel_v017_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 63)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_mean_63d_accel_v018_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 63)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_mean_126d_accel_v019_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 63)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_mean_252d_accel_v020_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 63)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_mean_5d_accel_v021_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up - eps_est_down, (eps_est_up + eps_est_down).abs()+1e-9)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_mean_21d_accel_v022_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up - eps_est_down, (eps_est_up + eps_est_down).abs()+1e-9)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_mean_63d_accel_v023_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up - eps_est_down, (eps_est_up + eps_est_down).abs()+1e-9)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_mean_126d_accel_v024_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up - eps_est_down, (eps_est_up + eps_est_down).abs()+1e-9)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_mean_252d_accel_v025_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up - eps_est_down, (eps_est_up + eps_est_down).abs()+1e-9)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_mean_5d_accel_v026_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up - rev_est_down, (rev_est_up + rev_est_down).abs()+1e-9)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_mean_21d_accel_v027_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up - rev_est_down, (rev_est_up + rev_est_down).abs()+1e-9)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_mean_63d_accel_v028_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up - rev_est_down, (rev_est_up + rev_est_down).abs()+1e-9)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_mean_126d_accel_v029_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up - rev_est_down, (rev_est_up + rev_est_down).abs()+1e-9)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_mean_252d_accel_v030_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up - rev_est_down, (rev_est_up + rev_est_down).abs()+1e-9)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_mean_5d_accel_v031_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(eps_est_up, 21) - _diff(eps_est_down, 21)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_mean_21d_accel_v032_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(eps_est_up, 21) - _diff(eps_est_down, 21)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_mean_63d_accel_v033_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(eps_est_up, 21) - _diff(eps_est_down, 21)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_mean_126d_accel_v034_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(eps_est_up, 21) - _diff(eps_est_down, 21)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_mean_252d_accel_v035_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(eps_est_up, 21) - _diff(eps_est_down, 21)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_mean_5d_accel_v036_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(rev_est_up, 21) - _diff(rev_est_down, 21)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_mean_21d_accel_v037_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(rev_est_up, 21) - _diff(rev_est_down, 21)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_mean_63d_accel_v038_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(rev_est_up, 21) - _diff(rev_est_down, 21)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_mean_126d_accel_v039_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(rev_est_up, 21) - _diff(rev_est_down, 21)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_mean_252d_accel_v040_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(rev_est_up, 21) - _diff(rev_est_down, 21)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_mean_5d_accel_v041_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 21), eps_disp.abs()+1e-9)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_mean_21d_accel_v042_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 21), eps_disp.abs()+1e-9)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_mean_63d_accel_v043_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 21), eps_disp.abs()+1e-9)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_mean_126d_accel_v044_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 21), eps_disp.abs()+1e-9)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_mean_252d_accel_v045_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 21), eps_disp.abs()+1e-9)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_mean_5d_accel_v046_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(rev_est, 21), rev_disp.abs()+1e-9)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_mean_21d_accel_v047_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(rev_est, 21), rev_disp.abs()+1e-9)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_mean_63d_accel_v048_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(rev_est, 21), rev_disp.abs()+1e-9)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_mean_126d_accel_v049_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(rev_est, 21), rev_disp.abs()+1e-9)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_mean_252d_accel_v050_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(rev_est, 21), rev_disp.abs()+1e-9)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_mean_5d_accel_v051_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(eps_est, 21), 252)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_mean_21d_accel_v052_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(eps_est, 21), 252)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_mean_63d_accel_v053_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(eps_est, 21), 252)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_mean_126d_accel_v054_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(eps_est, 21), 252)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_mean_252d_accel_v055_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(eps_est, 21), 252)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_mean_5d_accel_v056_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(rev_est, 21), 252)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_mean_21d_accel_v057_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(rev_est, 21), 252)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_mean_63d_accel_v058_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(rev_est, 21), 252)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_mean_126d_accel_v059_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(rev_est, 21), 252)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_mean_252d_accel_v060_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(rev_est, 21), 252)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_mean_5d_accel_v061_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(eps_est, 21), _pct_change(closeadj, 21), 126)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_mean_21d_accel_v062_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(eps_est, 21), _pct_change(closeadj, 21), 126)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_mean_63d_accel_v063_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(eps_est, 21), _pct_change(closeadj, 21), 126)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_mean_126d_accel_v064_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(eps_est, 21), _pct_change(closeadj, 21), 126)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_mean_252d_accel_v065_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(eps_est, 21), _pct_change(closeadj, 21), 126)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_mean_5d_accel_v066_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(rev_est, 21), _pct_change(closeadj, 21), 126)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_mean_21d_accel_v067_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(rev_est, 21), _pct_change(closeadj, 21), 126)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_mean_63d_accel_v068_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(rev_est, 21), _pct_change(closeadj, 21), 126)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_mean_126d_accel_v069_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(rev_est, 21), _pct_change(closeadj, 21), 126)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_mean_252d_accel_v070_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(rev_est, 21), _pct_change(closeadj, 21), 126)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_mean_5d_accel_v071_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(eps_est, 126)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_mean_21d_accel_v072_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(eps_est, 126)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_mean_63d_accel_v073_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(eps_est, 126)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_mean_126d_accel_v074_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(eps_est, 126)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_mean_252d_accel_v075_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(eps_est, 126)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_ewm_5d_accel_v076_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(rev_est, 126)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_ewm_21d_accel_v077_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(rev_est, 126)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_ewm_63d_accel_v078_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(rev_est, 126)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_ewm_126d_accel_v079_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(rev_est, 126)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_ewm_252d_accel_v080_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(rev_est, 126)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_ewm_5d_accel_v081_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_disp, eps_est.abs()+1e-9)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_ewm_21d_accel_v082_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_disp, eps_est.abs()+1e-9)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_ewm_63d_accel_v083_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_disp, eps_est.abs()+1e-9)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_ewm_126d_accel_v084_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_disp, eps_est.abs()+1e-9)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_ewm_252d_accel_v085_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_disp, eps_est.abs()+1e-9)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_ewm_5d_accel_v086_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_disp, rev_est.abs()+1e-9)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_ewm_21d_accel_v087_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_disp, rev_est.abs()+1e-9)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_ewm_63d_accel_v088_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_disp, rev_est.abs()+1e-9)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_ewm_126d_accel_v089_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_disp, rev_est.abs()+1e-9)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_ewm_252d_accel_v090_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_disp, rev_est.abs()+1e-9)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_ewm_5d_accel_v091_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(eps_disp, 63)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_ewm_21d_accel_v092_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(eps_disp, 63)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_ewm_63d_accel_v093_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(eps_disp, 63)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_ewm_126d_accel_v094_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(eps_disp, 63)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_ewm_252d_accel_v095_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(eps_disp, 63)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_ewm_5d_accel_v096_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(rev_disp, 63)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_ewm_21d_accel_v097_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(rev_disp, 63)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_ewm_63d_accel_v098_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(rev_disp, 63)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_ewm_126d_accel_v099_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(rev_disp, 63)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_ewm_252d_accel_v100_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(rev_disp, 63)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_ewm_5d_accel_v101_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(eps_est, 63), 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_ewm_21d_accel_v102_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(eps_est, 63), 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_ewm_63d_accel_v103_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(eps_est, 63), 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_ewm_126d_accel_v104_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(eps_est, 63), 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_ewm_252d_accel_v105_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(eps_est, 63), 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_ewm_5d_accel_v106_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(rev_est, 63), 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_ewm_21d_accel_v107_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(rev_est, 63), 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_ewm_63d_accel_v108_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(rev_est, 63), 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_ewm_126d_accel_v109_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(rev_est, 63), 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_ewm_252d_accel_v110_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(rev_est, 63), 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_ewm_5d_accel_v111_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up, (eps_est_up + eps_est_down).abs()+1e-9) - 0.5
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_ewm_21d_accel_v112_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up, (eps_est_up + eps_est_down).abs()+1e-9) - 0.5
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_ewm_63d_accel_v113_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up, (eps_est_up + eps_est_down).abs()+1e-9) - 0.5
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_ewm_126d_accel_v114_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up, (eps_est_up + eps_est_down).abs()+1e-9) - 0.5
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_ewm_252d_accel_v115_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up, (eps_est_up + eps_est_down).abs()+1e-9) - 0.5
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_ewm_5d_accel_v116_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up, (rev_est_up + rev_est_down).abs()+1e-9) - 0.5
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_ewm_21d_accel_v117_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up, (rev_est_up + rev_est_down).abs()+1e-9) - 0.5
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_ewm_63d_accel_v118_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up, (rev_est_up + rev_est_down).abs()+1e-9) - 0.5
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_ewm_126d_accel_v119_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up, (rev_est_up + rev_est_down).abs()+1e-9) - 0.5
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_ewm_252d_accel_v120_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up, (rev_est_up + rev_est_down).abs()+1e-9) - 0.5
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_ewm_5d_accel_v121_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(eps_est, 63) > 0, 0)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_ewm_21d_accel_v122_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(eps_est, 63) > 0, 0)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_ewm_63d_accel_v123_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(eps_est, 63) > 0, 0)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_ewm_126d_accel_v124_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(eps_est, 63) > 0, 0)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_ewm_252d_accel_v125_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(eps_est, 63) > 0, 0)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_ewm_5d_accel_v126_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(rev_est, 63) > 0, 0)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_ewm_21d_accel_v127_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(rev_est, 63) > 0, 0)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_ewm_63d_accel_v128_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(rev_est, 63) > 0, 0)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_ewm_126d_accel_v129_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(rev_est, 63) > 0, 0)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_ewm_252d_accel_v130_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(rev_est, 63) > 0, 0)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_ewm_5d_accel_v131_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _autocorr(_pct_change(eps_est, 21), 252, 21)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_ewm_21d_accel_v132_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _autocorr(_pct_change(eps_est, 21), 252, 21)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_ewm_63d_accel_v133_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _autocorr(_pct_change(eps_est, 21), 252, 21)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_ewm_126d_accel_v134_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _autocorr(_pct_change(eps_est, 21), 252, 21)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_ewm_252d_accel_v135_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _autocorr(_pct_change(eps_est, 21), 252, 21)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_ewm_5d_accel_v136_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _std(_pct_change(eps_est, 21), 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_ewm_21d_accel_v137_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _std(_pct_change(eps_est, 21), 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_ewm_63d_accel_v138_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _std(_pct_change(eps_est, 21), 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_ewm_126d_accel_v139_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _std(_pct_change(eps_est, 21), 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_ewm_252d_accel_v140_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _std(_pct_change(eps_est, 21), 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_ewm_5d_accel_v141_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _skew(_pct_change(rev_est, 21), 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_ewm_21d_accel_v142_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _skew(_pct_change(rev_est, 21), 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_ewm_63d_accel_v143_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _skew(_pct_change(rev_est, 21), 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_ewm_126d_accel_v144_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _skew(_pct_change(rev_est, 21), 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_ewm_252d_accel_v145_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _skew(_pct_change(rev_est, 21), 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_ewm_5d_accel_v146_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 63) + _diff(rev_est, 63), (eps_disp + rev_disp).abs()+1e-9)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_ewm_21d_accel_v147_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 63) + _diff(rev_est, 63), (eps_disp + rev_disp).abs()+1e-9)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_ewm_63d_accel_v148_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 63) + _diff(rev_est, 63), (eps_disp + rev_disp).abs()+1e-9)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_ewm_126d_accel_v149_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 63) + _diff(rev_est, 63), (eps_disp + rev_disp).abs()+1e-9)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_ewm_252d_accel_v150_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 63) + _diff(rev_est, 63), (eps_disp + rev_disp).abs()+1e-9)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

