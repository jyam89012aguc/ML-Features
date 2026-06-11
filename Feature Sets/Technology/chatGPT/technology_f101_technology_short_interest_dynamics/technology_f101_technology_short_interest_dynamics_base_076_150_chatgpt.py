import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_ewm_5d_base_v076_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(shortint, 21), shortint.abs()+1e-9)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_ewm_21d_base_v077_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(shortint, 21), shortint.abs()+1e-9)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_ewm_63d_base_v078_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(shortint, 21), shortint.abs()+1e-9)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_ewm_126d_base_v079_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(shortint, 21), shortint.abs()+1e-9)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_ewm_252d_base_v080_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(shortint, 21), shortint.abs()+1e-9)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_ewm_5d_base_v081_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_ewm_21d_base_v082_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_ewm_63d_base_v083_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_ewm_126d_base_v084_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_ewm_252d_base_v085_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_float, 21), short_pct_float.abs()+1e-9)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_ewm_5d_base_v086_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_ewm_21d_base_v087_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_ewm_63d_base_v088_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_ewm_126d_base_v089_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_ewm_252d_base_v090_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(short_pct_shares, 21), short_pct_shares.abs()+1e-9)
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_ewm_5d_base_v091_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_ewm_21d_base_v092_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_ewm_63d_base_v093_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_ewm_126d_base_v094_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_ewm_252d_base_v095_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(_diff(days_to_cover, 21), days_to_cover.abs()+1e-9)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_ewm_5d_base_v096_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(shortint, 252)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_ewm_21d_base_v097_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(shortint, 252)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_ewm_63d_base_v098_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(shortint, 252)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_ewm_126d_base_v099_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(shortint, 252)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_ewm_252d_base_v100_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(shortint, 252)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_ewm_5d_base_v101_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(short_pct_float, 252)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_ewm_21d_base_v102_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(short_pct_float, 252)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_ewm_63d_base_v103_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(short_pct_float, 252)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_ewm_126d_base_v104_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(short_pct_float, 252)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_ewm_252d_base_v105_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(short_pct_float, 252)
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_ewm_5d_base_v106_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(days_to_cover, 252)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_ewm_21d_base_v107_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(days_to_cover, 252)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_ewm_63d_base_v108_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(days_to_cover, 252)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_ewm_126d_base_v109_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(days_to_cover, 252)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_ewm_252d_base_v110_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _rank(days_to_cover, 252)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_ewm_5d_base_v111_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_ewm_21d_base_v112_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_ewm_63d_base_v113_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_ewm_126d_base_v114_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_ewm_252d_base_v115_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 5).where(short_pct_float > _mean(short_pct_float, 252), 0)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_ewm_5d_base_v116_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_ewm_21d_base_v117_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_ewm_63d_base_v118_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_ewm_126d_base_v119_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_ewm_252d_base_v120_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _pct_change(closeadj, 21).where(_diff(short_pct_float, 21) < 0, 0)
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_ewm_5d_base_v121_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_ewm_21d_base_v122_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_ewm_63d_base_v123_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_ewm_126d_base_v124_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_ewm_252d_base_v125_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _safe_div(volume, _mean(volume, 63)+1e-9).where(short_pct_float > _mean(short_pct_float, 252), 0)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_ewm_5d_base_v126_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _slope(_z(short_pct_float, 252), 63)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_ewm_21d_base_v127_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _slope(_z(short_pct_float, 252), 63)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_ewm_63d_base_v128_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _slope(_z(short_pct_float, 252), 63)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_ewm_126d_base_v129_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _slope(_z(short_pct_float, 252), 63)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_ewm_252d_base_v130_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _slope(_z(short_pct_float, 252), 63)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_ewm_5d_base_v131_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _std(_diff(short_pct_float, 1), 63)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_ewm_21d_base_v132_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _std(_diff(short_pct_float, 1), 63)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_ewm_63d_base_v133_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _std(_diff(short_pct_float, 1), 63)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_ewm_126d_base_v134_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _std(_diff(short_pct_float, 1), 63)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_ewm_252d_base_v135_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _std(_diff(short_pct_float, 1), 63)
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core00_ewm_5d_base_v136_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _autocorr(short_pct_float, 63, 5)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core01_ewm_21d_base_v137_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _autocorr(short_pct_float, 63, 5)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core02_ewm_63d_base_v138_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _autocorr(short_pct_float, 63, 5)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core03_ewm_126d_base_v139_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _autocorr(short_pct_float, 63, 5)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core04_ewm_252d_base_v140_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _autocorr(short_pct_float, 63, 5)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core05_ewm_5d_base_v141_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _skew(_diff(short_pct_float, 1), 252)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core06_ewm_21d_base_v142_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _skew(_diff(short_pct_float, 1), 252)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core07_ewm_63d_base_v143_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _skew(_diff(short_pct_float, 1), 252)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core08_ewm_126d_base_v144_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _skew(_diff(short_pct_float, 1), 252)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core09_ewm_252d_base_v145_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = _skew(_diff(short_pct_float, 1), 252)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f101_technology_f101_technology_short_interest_dynamics_core10_ewm_5d_base_v146_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = -_safe_div(shortint, (closeadj*sharesbas).abs()+1e-9)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f101_technology_f101_technology_short_interest_dynamics_core11_ewm_21d_base_v147_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = -_safe_div(shortint, (closeadj*sharesbas).abs()+1e-9)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f101_technology_f101_technology_short_interest_dynamics_core12_ewm_63d_base_v148_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = -_safe_div(shortint, (closeadj*sharesbas).abs()+1e-9)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f101_technology_f101_technology_short_interest_dynamics_core13_ewm_126d_base_v149_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = -_safe_div(shortint, (closeadj*sharesbas).abs()+1e-9)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f101_technology_f101_technology_short_interest_dynamics_core14_ewm_252d_base_v150_signal(shortint, short_pct_float, short_pct_shares, days_to_cover, sharesbas, volume, closeadj):
    series = -_safe_div(shortint, (closeadj*sharesbas).abs()+1e-9)
    result = _ewm(series, 252)
    return _clean(result)

