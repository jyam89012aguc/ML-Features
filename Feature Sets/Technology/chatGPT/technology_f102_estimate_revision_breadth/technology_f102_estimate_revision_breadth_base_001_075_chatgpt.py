import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_mean_5d_base_v001_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 21)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_mean_21d_base_v002_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 21)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_mean_63d_base_v003_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 21)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_mean_126d_base_v004_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 21)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_mean_252d_base_v005_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 21)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_mean_5d_base_v006_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 63)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_mean_21d_base_v007_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 63)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_mean_63d_base_v008_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 63)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_mean_126d_base_v009_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 63)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_mean_252d_base_v010_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(eps_est, 63)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_mean_5d_base_v011_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 21)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_mean_21d_base_v012_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 21)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_mean_63d_base_v013_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 21)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_mean_126d_base_v014_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 21)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_mean_252d_base_v015_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 21)
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_mean_5d_base_v016_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 63)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_mean_21d_base_v017_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 63)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_mean_63d_base_v018_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 63)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_mean_126d_base_v019_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 63)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_mean_252d_base_v020_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(rev_est, 63)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_mean_5d_base_v021_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up - eps_est_down, (eps_est_up + eps_est_down).abs()+1e-9)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_mean_21d_base_v022_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up - eps_est_down, (eps_est_up + eps_est_down).abs()+1e-9)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_mean_63d_base_v023_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up - eps_est_down, (eps_est_up + eps_est_down).abs()+1e-9)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_mean_126d_base_v024_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up - eps_est_down, (eps_est_up + eps_est_down).abs()+1e-9)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_mean_252d_base_v025_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up - eps_est_down, (eps_est_up + eps_est_down).abs()+1e-9)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_mean_5d_base_v026_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up - rev_est_down, (rev_est_up + rev_est_down).abs()+1e-9)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_mean_21d_base_v027_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up - rev_est_down, (rev_est_up + rev_est_down).abs()+1e-9)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_mean_63d_base_v028_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up - rev_est_down, (rev_est_up + rev_est_down).abs()+1e-9)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_mean_126d_base_v029_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up - rev_est_down, (rev_est_up + rev_est_down).abs()+1e-9)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_mean_252d_base_v030_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up - rev_est_down, (rev_est_up + rev_est_down).abs()+1e-9)
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_mean_5d_base_v031_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(eps_est_up, 21) - _diff(eps_est_down, 21)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_mean_21d_base_v032_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(eps_est_up, 21) - _diff(eps_est_down, 21)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_mean_63d_base_v033_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(eps_est_up, 21) - _diff(eps_est_down, 21)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_mean_126d_base_v034_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(eps_est_up, 21) - _diff(eps_est_down, 21)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_mean_252d_base_v035_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(eps_est_up, 21) - _diff(eps_est_down, 21)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_mean_5d_base_v036_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(rev_est_up, 21) - _diff(rev_est_down, 21)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_mean_21d_base_v037_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(rev_est_up, 21) - _diff(rev_est_down, 21)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_mean_63d_base_v038_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(rev_est_up, 21) - _diff(rev_est_down, 21)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_mean_126d_base_v039_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(rev_est_up, 21) - _diff(rev_est_down, 21)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_mean_252d_base_v040_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _diff(rev_est_up, 21) - _diff(rev_est_down, 21)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_mean_5d_base_v041_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 21), eps_disp.abs()+1e-9)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_mean_21d_base_v042_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 21), eps_disp.abs()+1e-9)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_mean_63d_base_v043_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 21), eps_disp.abs()+1e-9)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_mean_126d_base_v044_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 21), eps_disp.abs()+1e-9)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_mean_252d_base_v045_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 21), eps_disp.abs()+1e-9)
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_mean_5d_base_v046_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(rev_est, 21), rev_disp.abs()+1e-9)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_mean_21d_base_v047_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(rev_est, 21), rev_disp.abs()+1e-9)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_mean_63d_base_v048_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(rev_est, 21), rev_disp.abs()+1e-9)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_mean_126d_base_v049_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(rev_est, 21), rev_disp.abs()+1e-9)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_mean_252d_base_v050_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(rev_est, 21), rev_disp.abs()+1e-9)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_mean_5d_base_v051_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(eps_est, 21), 252)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_mean_21d_base_v052_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(eps_est, 21), 252)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_mean_63d_base_v053_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(eps_est, 21), 252)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_mean_126d_base_v054_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(eps_est, 21), 252)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_mean_252d_base_v055_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(eps_est, 21), 252)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_mean_5d_base_v056_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(rev_est, 21), 252)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_mean_21d_base_v057_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(rev_est, 21), 252)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_mean_63d_base_v058_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(rev_est, 21), 252)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_mean_126d_base_v059_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(rev_est, 21), 252)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_mean_252d_base_v060_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _z(_pct_change(rev_est, 21), 252)
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_mean_5d_base_v061_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(eps_est, 21), _pct_change(closeadj, 21), 126)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_mean_21d_base_v062_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(eps_est, 21), _pct_change(closeadj, 21), 126)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_mean_63d_base_v063_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(eps_est, 21), _pct_change(closeadj, 21), 126)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_mean_126d_base_v064_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(eps_est, 21), _pct_change(closeadj, 21), 126)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_mean_252d_base_v065_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(eps_est, 21), _pct_change(closeadj, 21), 126)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_mean_5d_base_v066_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(rev_est, 21), _pct_change(closeadj, 21), 126)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_mean_21d_base_v067_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(rev_est, 21), _pct_change(closeadj, 21), 126)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_mean_63d_base_v068_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(rev_est, 21), _pct_change(closeadj, 21), 126)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_mean_126d_base_v069_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(rev_est, 21), _pct_change(closeadj, 21), 126)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_mean_252d_base_v070_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _corr(_pct_change(rev_est, 21), _pct_change(closeadj, 21), 126)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_mean_5d_base_v071_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(eps_est, 126)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_mean_21d_base_v072_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(eps_est, 126)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_mean_63d_base_v073_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(eps_est, 126)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_mean_126d_base_v074_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(eps_est, 126)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_mean_252d_base_v075_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(eps_est, 126)
    result = _mean(series, 252)
    return _clean(result)

