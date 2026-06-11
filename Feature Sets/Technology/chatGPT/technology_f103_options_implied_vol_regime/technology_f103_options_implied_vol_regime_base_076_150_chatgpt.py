import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_ewm_5d_base_v076_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(closeadj, 5), 63)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_ewm_21d_base_v077_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(closeadj, 5), 63)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_ewm_63d_base_v078_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(closeadj, 5), 63)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_ewm_126d_base_v079_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(closeadj, 5), 63)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_ewm_252d_base_v080_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(closeadj, 5), 63)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_ewm_5d_base_v081_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv_skew, _pct_change(closeadj, 5), 63)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_ewm_21d_base_v082_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv_skew, _pct_change(closeadj, 5), 63)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_ewm_63d_base_v083_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv_skew, _pct_change(closeadj, 5), 63)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_ewm_126d_base_v084_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv_skew, _pct_change(closeadj, 5), 63)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_ewm_252d_base_v085_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv_skew, _pct_change(closeadj, 5), 63)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_ewm_5d_base_v086_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(put_call, _pct_change(closeadj, 5), 63)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_ewm_21d_base_v087_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(put_call, _pct_change(closeadj, 5), 63)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_ewm_63d_base_v088_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(put_call, _pct_change(closeadj, 5), 63)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_ewm_126d_base_v089_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(put_call, _pct_change(closeadj, 5), 63)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_ewm_252d_base_v090_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(put_call, _pct_change(closeadj, 5), 63)
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_ewm_5d_base_v091_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(volume, 5), 63)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_ewm_21d_base_v092_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(volume, 5), 63)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_ewm_63d_base_v093_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(volume, 5), 63)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_ewm_126d_base_v094_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(volume, 5), 63)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_ewm_252d_base_v095_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _corr(iv, _pct_change(volume, 5), 63)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_ewm_5d_base_v096_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv, 63)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_ewm_21d_base_v097_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv, 63)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_ewm_63d_base_v098_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv, 63)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_ewm_126d_base_v099_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv, 63)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_ewm_252d_base_v100_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv, 63)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_ewm_5d_base_v101_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv_skew, 63)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_ewm_21d_base_v102_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv_skew, 63)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_ewm_63d_base_v103_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv_skew, 63)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_ewm_126d_base_v104_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv_skew, 63)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_ewm_252d_base_v105_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _slope(iv_skew, 63)
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_ewm_5d_base_v106_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv, 252)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_ewm_21d_base_v107_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv, 252)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_ewm_63d_base_v108_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv, 252)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_ewm_126d_base_v109_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv, 252)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_ewm_252d_base_v110_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv, 252)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_ewm_5d_base_v111_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv_skew, 252)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_ewm_21d_base_v112_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv_skew, 252)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_ewm_63d_base_v113_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv_skew, 252)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_ewm_126d_base_v114_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv_skew, 252)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_ewm_252d_base_v115_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(iv_skew, 252)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_ewm_5d_base_v116_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(put_call, 252)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_ewm_21d_base_v117_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(put_call, 252)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_ewm_63d_base_v118_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(put_call, 252)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_ewm_126d_base_v119_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(put_call, 252)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_ewm_252d_base_v120_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _rank(put_call, 252)
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_ewm_5d_base_v121_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _std(_diff(iv, 1), 63)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_ewm_21d_base_v122_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _std(_diff(iv, 1), 63)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_ewm_63d_base_v123_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _std(_diff(iv, 1), 63)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_ewm_126d_base_v124_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _std(_diff(iv, 1), 63)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_ewm_252d_base_v125_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _std(_diff(iv, 1), 63)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_ewm_5d_base_v126_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _skew(_diff(iv, 1), 252)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_ewm_21d_base_v127_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _skew(_diff(iv, 1), 252)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_ewm_63d_base_v128_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _skew(_diff(iv, 1), 252)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_ewm_126d_base_v129_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _skew(_diff(iv, 1), 252)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_ewm_252d_base_v130_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _skew(_diff(iv, 1), 252)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_ewm_5d_base_v131_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _autocorr(iv, 63, 5)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_ewm_21d_base_v132_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _autocorr(iv, 63, 5)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_ewm_63d_base_v133_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _autocorr(iv, 63, 5)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_ewm_126d_base_v134_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _autocorr(iv, 63, 5)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_ewm_252d_base_v135_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _autocorr(iv, 63, 5)
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core00_ewm_5d_base_v136_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term - iv
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core01_ewm_21d_base_v137_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term - iv
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core02_ewm_63d_base_v138_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term - iv
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core03_ewm_126d_base_v139_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term - iv
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core04_ewm_252d_base_v140_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = iv_term - iv
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core05_ewm_5d_base_v141_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv_term, iv.abs()+1e-9)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core06_ewm_21d_base_v142_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv_term, iv.abs()+1e-9)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core07_ewm_63d_base_v143_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv_term, iv.abs()+1e-9)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core08_ewm_126d_base_v144_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv_term, iv.abs()+1e-9)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core09_ewm_252d_base_v145_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _safe_div(iv_term, iv.abs()+1e-9)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f103_technology_f103_options_implied_vol_regime_core10_ewm_5d_base_v146_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f103_technology_f103_options_implied_vol_regime_core11_ewm_21d_base_v147_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f103_technology_f103_options_implied_vol_regime_core12_ewm_63d_base_v148_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f103_technology_f103_options_implied_vol_regime_core13_ewm_126d_base_v149_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f103_technology_f103_options_implied_vol_regime_core14_ewm_252d_base_v150_signal(iv, iv_skew, iv_term, put_call, iv_rank, hv, closeadj, volume):
    series = _pct_change(closeadj, 5).where(iv > _mean(iv, 252), 0)
    result = _ewm(series, 252)
    return _clean(result)

