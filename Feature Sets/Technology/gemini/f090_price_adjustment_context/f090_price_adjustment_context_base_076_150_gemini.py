import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: ewm 21d (continued)
def cg_f090_price_adjustment_context_core75_ewm_21d_v076_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_ewm(_safe_div(closeadj, closeunadj), 21))
def cg_f090_price_adjustment_context_core76_ewm_21d_v077_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_ewm(_z(closeadj, 252), 21))
def cg_f090_price_adjustment_context_core77_ewm_21d_v078_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_ewm(_rank(closeadj, 252), 21))
def cg_f090_price_adjustment_context_core78_ewm_21d_v079_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_ewm(_safe_div(high, low), 21))
def cg_f090_price_adjustment_context_core79_ewm_21d_v080_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_ewm(_safe_div(close, open), 21))

# core80-89: skew 63d
def cg_f090_price_adjustment_context_core80_skew_63d_v081_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_skew(_safe_div(closeadj, close), 63))
def cg_f090_price_adjustment_context_core81_skew_63d_v082_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_skew(_safe_div(closeunadj, close), 63))
def cg_f090_price_adjustment_context_core82_skew_63d_v083_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_skew(_safe_div(closeadj, closeunadj), 63))
def cg_f090_price_adjustment_context_core83_skew_63d_v084_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_skew(_pct_change(closeadj, 1), 63))
def cg_f090_price_adjustment_context_core84_skew_63d_v085_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_skew(_pct_change(close, 1), 63))
def cg_f090_price_adjustment_context_core85_skew_63d_v086_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_skew(_z(closeadj, 252), 63))
def cg_f090_price_adjustment_context_core86_skew_63d_v087_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_skew(_rank(closeadj, 252), 63))
def cg_f090_price_adjustment_context_core87_skew_63d_v088_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_skew(_safe_div(high, low), 63))
def cg_f090_price_adjustment_context_core88_skew_63d_v089_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_skew(_safe_div(close, open), 63))
def cg_f090_price_adjustment_context_core89_skew_63d_v090_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_skew(closeadj, 63))

# core90-99: kurt 63d
def cg_f090_price_adjustment_context_core90_kurt_63d_v091_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_kurt(_safe_div(closeadj, close), 63))
def cg_f090_price_adjustment_context_core91_kurt_63d_v092_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_kurt(_safe_div(closeunadj, close), 63))
def cg_f090_price_adjustment_context_core92_kurt_63d_v093_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_kurt(_safe_div(closeadj, closeunadj), 63))
def cg_f090_price_adjustment_context_core93_kurt_63d_v094_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_kurt(_pct_change(closeadj, 1), 63))
def cg_f090_price_adjustment_context_core94_kurt_63d_v095_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_kurt(_pct_change(close, 1), 63))
def cg_f090_price_adjustment_context_core95_kurt_63d_v096_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_kurt(_z(closeadj, 252), 63))
def cg_f090_price_adjustment_context_core96_kurt_63d_v097_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_kurt(_rank(closeadj, 252), 63))
def cg_f090_price_adjustment_context_core97_kurt_63d_v098_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_kurt(_safe_div(high, low), 63))
def cg_f090_price_adjustment_context_core98_kurt_63d_v099_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_kurt(_safe_div(close, open), 63))
def cg_f090_price_adjustment_context_core99_kurt_63d_v100_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_kurt(closeadj, 63))

# core100-109: autocorr 21d
def cg_f090_price_adjustment_context_core100_autocorr_21d_v101_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_autocorr(_safe_div(closeadj, close), 21))
def cg_f090_price_adjustment_context_core101_autocorr_21d_v102_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_autocorr(_safe_div(closeunadj, close), 21))
def cg_f090_price_adjustment_context_core102_autocorr_21d_v103_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_autocorr(_safe_div(closeadj, closeunadj), 21))
def cg_f090_price_adjustment_context_core103_autocorr_21d_v104_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_autocorr(_pct_change(closeadj, 1), 21))
def cg_f090_price_adjustment_context_core104_autocorr_21d_v105_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_autocorr(_pct_change(close, 1), 21))
def cg_f090_price_adjustment_context_core105_autocorr_21d_v106_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_autocorr(_z(closeadj, 252), 21))
def cg_f090_price_adjustment_context_core106_autocorr_21d_v107_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_autocorr(_rank(closeadj, 252), 21))
def cg_f090_price_adjustment_context_core107_autocorr_21d_v108_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_autocorr(_safe_div(high, low), 21))
def cg_f090_price_adjustment_context_core108_autocorr_21d_v109_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_autocorr(_safe_div(close, open), 21))
def cg_f090_price_adjustment_context_core109_autocorr_21d_v110_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_autocorr(closeadj, 21))

# core110-119: corr with closeadj 21d
def cg_f090_price_adjustment_context_core110_corr_closeadj_21d_v111_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_corr(_safe_div(closeadj, close), closeadj, 21))
def cg_f090_price_adjustment_context_core111_corr_closeadj_21d_v112_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_corr(_safe_div(closeunadj, close), closeadj, 21))
def cg_f090_price_adjustment_context_core112_corr_closeadj_21d_v113_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_corr(_safe_div(closeadj, closeunadj), closeadj, 21))
def cg_f090_price_adjustment_context_core113_corr_closeadj_21d_v114_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_corr(_pct_change(closeadj, 1), closeadj, 21))
def cg_f090_price_adjustment_context_core114_corr_closeadj_21d_v115_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_corr(_pct_change(close, 1), closeadj, 21))
def cg_f090_price_adjustment_context_core115_corr_closeadj_21d_v116_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_corr(_z(closeadj, 252), closeadj, 21))
def cg_f090_price_adjustment_context_core116_corr_closeadj_21d_v117_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_corr(_rank(closeadj, 252), closeadj, 21))
def cg_f090_price_adjustment_context_core117_corr_closeadj_21d_v118_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_corr(_safe_div(high, low), closeadj, 21))
def cg_f090_price_adjustment_context_core118_corr_closeadj_21d_v119_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_corr(_safe_div(close, open), closeadj, 21))
def cg_f090_price_adjustment_context_core119_corr_closeadj_21d_v120_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_corr(closeunadj, closeadj, 21))

# core120-129: stability 21d
def cg_f090_price_adjustment_context_core120_stability_21d_v121_signal(close, closeadj, closeunadj, open, high, low):
    base = _safe_div(closeadj, close)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f090_price_adjustment_context_core121_stability_21d_v122_signal(close, closeadj, closeunadj, open, high, low):
    base = _safe_div(closeunadj, close)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f090_price_adjustment_context_core122_stability_21d_v123_signal(close, closeadj, closeunadj, open, high, low):
    base = _safe_div(closeadj, closeunadj)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f090_price_adjustment_context_core123_stability_21d_v124_signal(close, closeadj, closeunadj, open, high, low):
    base = _pct_change(closeadj, 1)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f090_price_adjustment_context_core124_stability_21d_v125_signal(close, closeadj, closeunadj, open, high, low):
    base = _pct_change(close, 1)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f090_price_adjustment_context_core125_stability_21d_v126_signal(close, closeadj, closeunadj, open, high, low):
    base = _z(closeadj, 252)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f090_price_adjustment_context_core126_stability_21d_v127_signal(close, closeadj, closeunadj, open, high, low):
    base = _rank(closeadj, 252)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f090_price_adjustment_context_core127_stability_21d_v128_signal(close, closeadj, closeunadj, open, high, low):
    base = _safe_div(high, low)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f090_price_adjustment_context_core128_stability_21d_v129_signal(close, closeadj, closeunadj, open, high, low):
    base = _safe_div(close, open)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f090_price_adjustment_context_core129_stability_21d_v130_signal(close, closeadj, closeunadj, open, high, low):
    base = closeadj
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))

# core130-139: diff 5d
def cg_f090_price_adjustment_context_core130_diff_5d_v131_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_safe_div(closeadj, close), 5))
def cg_f090_price_adjustment_context_core131_diff_5d_v132_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_safe_div(closeunadj, close), 5))
def cg_f090_price_adjustment_context_core132_diff_5d_v133_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_safe_div(closeadj, closeunadj), 5))
def cg_f090_price_adjustment_context_core133_diff_5d_v134_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_pct_change(closeadj, 1), 5))
def cg_f090_price_adjustment_context_core134_diff_5d_v135_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_pct_change(close, 1), 5))
def cg_f090_price_adjustment_context_core135_diff_5d_v136_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_z(closeadj, 252), 5))
def cg_f090_price_adjustment_context_core136_diff_5d_v137_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_rank(closeadj, 252), 5))
def cg_f090_price_adjustment_context_core137_diff_5d_v138_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_safe_div(high, low), 5))
def cg_f090_price_adjustment_context_core138_diff_5d_v139_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_safe_div(close, open), 5))
def cg_f090_price_adjustment_context_core139_diff_5d_v140_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(closeadj, 5))

# core140-149: levels
def cg_f090_price_adjustment_context_core140_level_v141_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(closeadj)
def cg_f090_price_adjustment_context_core141_close_v142_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(close)
def cg_f090_price_adjustment_context_core142_closeunadj_v143_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(closeunadj)
def cg_f090_price_adjustment_context_core143_adj_factor_v144_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_safe_div(closeadj, close))
def cg_f090_price_adjustment_context_core144_unadj_ratio_v145_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_safe_div(closeunadj, close))
def cg_f090_price_adjustment_context_core145_adj_diff_v146_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(closeadj - close)
def cg_f090_price_adjustment_context_core146_open_v147_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(open)
def cg_f090_price_adjustment_context_core147_high_v148_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(high)
def cg_f090_price_adjustment_context_core148_low_v149_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(low)
def cg_f090_price_adjustment_context_core149_hl_range_v150_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_safe_div(high - low, low))
