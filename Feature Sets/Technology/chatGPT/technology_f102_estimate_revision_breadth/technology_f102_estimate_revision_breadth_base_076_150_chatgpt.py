import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_ewm_5d_base_v076_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(rev_est, 126)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_ewm_21d_base_v077_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(rev_est, 126)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_ewm_63d_base_v078_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(rev_est, 126)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_ewm_126d_base_v079_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(rev_est, 126)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_ewm_252d_base_v080_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _slope(rev_est, 126)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_ewm_5d_base_v081_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_disp, eps_est.abs()+1e-9)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_ewm_21d_base_v082_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_disp, eps_est.abs()+1e-9)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_ewm_63d_base_v083_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_disp, eps_est.abs()+1e-9)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_ewm_126d_base_v084_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_disp, eps_est.abs()+1e-9)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_ewm_252d_base_v085_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_disp, eps_est.abs()+1e-9)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_ewm_5d_base_v086_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_disp, rev_est.abs()+1e-9)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_ewm_21d_base_v087_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_disp, rev_est.abs()+1e-9)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_ewm_63d_base_v088_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_disp, rev_est.abs()+1e-9)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_ewm_126d_base_v089_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_disp, rev_est.abs()+1e-9)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_ewm_252d_base_v090_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_disp, rev_est.abs()+1e-9)
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_ewm_5d_base_v091_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(eps_disp, 63)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_ewm_21d_base_v092_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(eps_disp, 63)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_ewm_63d_base_v093_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(eps_disp, 63)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_ewm_126d_base_v094_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(eps_disp, 63)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_ewm_252d_base_v095_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(eps_disp, 63)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_ewm_5d_base_v096_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(rev_disp, 63)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_ewm_21d_base_v097_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(rev_disp, 63)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_ewm_63d_base_v098_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(rev_disp, 63)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_ewm_126d_base_v099_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(rev_disp, 63)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_ewm_252d_base_v100_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = -_diff(rev_disp, 63)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_ewm_5d_base_v101_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(eps_est, 63), 252)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_ewm_21d_base_v102_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(eps_est, 63), 252)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_ewm_63d_base_v103_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(eps_est, 63), 252)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_ewm_126d_base_v104_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(eps_est, 63), 252)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_ewm_252d_base_v105_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(eps_est, 63), 252)
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_ewm_5d_base_v106_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(rev_est, 63), 252)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_ewm_21d_base_v107_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(rev_est, 63), 252)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_ewm_63d_base_v108_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(rev_est, 63), 252)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_ewm_126d_base_v109_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(rev_est, 63), 252)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_ewm_252d_base_v110_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _rank(_pct_change(rev_est, 63), 252)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_ewm_5d_base_v111_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up, (eps_est_up + eps_est_down).abs()+1e-9) - 0.5
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_ewm_21d_base_v112_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up, (eps_est_up + eps_est_down).abs()+1e-9) - 0.5
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_ewm_63d_base_v113_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up, (eps_est_up + eps_est_down).abs()+1e-9) - 0.5
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_ewm_126d_base_v114_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up, (eps_est_up + eps_est_down).abs()+1e-9) - 0.5
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_ewm_252d_base_v115_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(eps_est_up, (eps_est_up + eps_est_down).abs()+1e-9) - 0.5
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_ewm_5d_base_v116_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up, (rev_est_up + rev_est_down).abs()+1e-9) - 0.5
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_ewm_21d_base_v117_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up, (rev_est_up + rev_est_down).abs()+1e-9) - 0.5
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_ewm_63d_base_v118_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up, (rev_est_up + rev_est_down).abs()+1e-9) - 0.5
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_ewm_126d_base_v119_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up, (rev_est_up + rev_est_down).abs()+1e-9) - 0.5
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_ewm_252d_base_v120_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(rev_est_up, (rev_est_up + rev_est_down).abs()+1e-9) - 0.5
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_ewm_5d_base_v121_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(eps_est, 63) > 0, 0)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_ewm_21d_base_v122_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(eps_est, 63) > 0, 0)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_ewm_63d_base_v123_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(eps_est, 63) > 0, 0)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_ewm_126d_base_v124_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(eps_est, 63) > 0, 0)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_ewm_252d_base_v125_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(eps_est, 63) > 0, 0)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_ewm_5d_base_v126_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(rev_est, 63) > 0, 0)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_ewm_21d_base_v127_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(rev_est, 63) > 0, 0)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_ewm_63d_base_v128_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(rev_est, 63) > 0, 0)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_ewm_126d_base_v129_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(rev_est, 63) > 0, 0)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_ewm_252d_base_v130_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _pct_change(closeadj, 63).where(_diff(rev_est, 63) > 0, 0)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_ewm_5d_base_v131_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _autocorr(_pct_change(eps_est, 21), 252, 21)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_ewm_21d_base_v132_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _autocorr(_pct_change(eps_est, 21), 252, 21)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_ewm_63d_base_v133_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _autocorr(_pct_change(eps_est, 21), 252, 21)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_ewm_126d_base_v134_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _autocorr(_pct_change(eps_est, 21), 252, 21)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_ewm_252d_base_v135_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _autocorr(_pct_change(eps_est, 21), 252, 21)
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core00_ewm_5d_base_v136_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _std(_pct_change(eps_est, 21), 252)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core01_ewm_21d_base_v137_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _std(_pct_change(eps_est, 21), 252)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core02_ewm_63d_base_v138_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _std(_pct_change(eps_est, 21), 252)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core03_ewm_126d_base_v139_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _std(_pct_change(eps_est, 21), 252)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core04_ewm_252d_base_v140_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _std(_pct_change(eps_est, 21), 252)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core05_ewm_5d_base_v141_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _skew(_pct_change(rev_est, 21), 252)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core06_ewm_21d_base_v142_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _skew(_pct_change(rev_est, 21), 252)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core07_ewm_63d_base_v143_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _skew(_pct_change(rev_est, 21), 252)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core08_ewm_126d_base_v144_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _skew(_pct_change(rev_est, 21), 252)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core09_ewm_252d_base_v145_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _skew(_pct_change(rev_est, 21), 252)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f102_technology_f102_estimate_revision_breadth_core10_ewm_5d_base_v146_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 63) + _diff(rev_est, 63), (eps_disp + rev_disp).abs()+1e-9)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f102_technology_f102_estimate_revision_breadth_core11_ewm_21d_base_v147_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 63) + _diff(rev_est, 63), (eps_disp + rev_disp).abs()+1e-9)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f102_technology_f102_estimate_revision_breadth_core12_ewm_63d_base_v148_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 63) + _diff(rev_est, 63), (eps_disp + rev_disp).abs()+1e-9)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f102_technology_f102_estimate_revision_breadth_core13_ewm_126d_base_v149_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 63) + _diff(rev_est, 63), (eps_disp + rev_disp).abs()+1e-9)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f102_technology_f102_estimate_revision_breadth_core14_ewm_252d_base_v150_signal(eps_est, rev_est, eps_est_up, eps_est_down, rev_est_up, rev_est_down, eps_disp, rev_disp, closeadj):
    series = _safe_div(_diff(eps_est, 63) + _diff(rev_est, 63), (eps_disp + rev_disp).abs()+1e-9)
    result = _ewm(series, 252)
    return _clean(result)

