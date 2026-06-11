import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: ewm 21d (continued)
def cg_f089_volume_liquidity_context_core75_ewm_21d_v076_signal(volume, close, closeadj, sharesbas):
    return _clean(_ewm(_z(volume, 252), 21))
def cg_f089_volume_liquidity_context_core76_ewm_21d_v077_signal(volume, close, closeadj, sharesbas):
    return _clean(_ewm(_rank(volume, 252), 21))
def cg_f089_volume_liquidity_context_core77_ewm_21d_v078_signal(volume, close, closeadj, sharesbas):
    return _clean(_ewm(_safe_div(volume, _max(volume, 252)), 21))
def cg_f089_volume_liquidity_context_core78_ewm_21d_v079_signal(volume, close, closeadj, sharesbas):
    return _clean(_ewm(_safe_div(volume, _min(volume, 252)), 21))
def cg_f089_volume_liquidity_context_core79_ewm_21d_v080_signal(volume, close, closeadj, sharesbas):
    return _clean(_ewm(_safe_div(volume * close, _mean(volume * close, 252)), 21))

# core80-89: skew 63d
def cg_f089_volume_liquidity_context_core80_skew_63d_v081_signal(volume, close, closeadj, sharesbas):
    return _clean(_skew(volume, 63))
def cg_f089_volume_liquidity_context_core81_skew_63d_v082_signal(volume, close, closeadj, sharesbas):
    return _clean(_skew(_safe_div(volume, sharesbas), 63))
def cg_f089_volume_liquidity_context_core82_skew_63d_v083_signal(volume, close, closeadj, sharesbas):
    return _clean(_skew(volume * close, 63))
def cg_f089_volume_liquidity_context_core83_skew_63d_v084_signal(volume, close, closeadj, sharesbas):
    return _clean(_skew(_safe_div(volume, _mean(volume, 252)), 63))
def cg_f089_volume_liquidity_context_core84_skew_63d_v085_signal(volume, close, closeadj, sharesbas):
    return _clean(_skew(_pct_change(volume, 1), 63))
def cg_f089_volume_liquidity_context_core85_skew_63d_v086_signal(volume, close, closeadj, sharesbas):
    return _clean(_skew(_z(volume, 252), 63))
def cg_f089_volume_liquidity_context_core86_skew_63d_v087_signal(volume, close, closeadj, sharesbas):
    return _clean(_skew(_rank(volume, 252), 63))
def cg_f089_volume_liquidity_context_core87_skew_63d_v088_signal(volume, close, closeadj, sharesbas):
    return _clean(_skew(_safe_div(volume, _max(volume, 252)), 63))
def cg_f089_volume_liquidity_context_core88_skew_63d_v089_signal(volume, close, closeadj, sharesbas):
    return _clean(_skew(_safe_div(volume, _min(volume, 252)), 63))
def cg_f089_volume_liquidity_context_core89_skew_63d_v090_signal(volume, close, closeadj, sharesbas):
    return _clean(_skew(_safe_div(volume * close, _mean(volume * close, 252)), 63))

# core90-99: kurt 63d
def cg_f089_volume_liquidity_context_core90_kurt_63d_v091_signal(volume, close, closeadj, sharesbas):
    return _clean(_kurt(volume, 63))
def cg_f089_volume_liquidity_context_core91_kurt_63d_v092_signal(volume, close, closeadj, sharesbas):
    return _clean(_kurt(_safe_div(volume, sharesbas), 63))
def cg_f089_volume_liquidity_context_core92_kurt_63d_v093_signal(volume, close, closeadj, sharesbas):
    return _clean(_kurt(volume * close, 63))
def cg_f089_volume_liquidity_context_core93_kurt_63d_v094_signal(volume, close, closeadj, sharesbas):
    return _clean(_kurt(_safe_div(volume, _mean(volume, 252)), 63))
def cg_f089_volume_liquidity_context_core94_kurt_63d_v095_signal(volume, close, closeadj, sharesbas):
    return _clean(_kurt(_pct_change(volume, 1), 63))
def cg_f089_volume_liquidity_context_core95_kurt_63d_v096_signal(volume, close, closeadj, sharesbas):
    return _clean(_kurt(_z(volume, 252), 63))
def cg_f089_volume_liquidity_context_core96_kurt_63d_v097_signal(volume, close, closeadj, sharesbas):
    return _clean(_kurt(_rank(volume, 252), 63))
def cg_f089_volume_liquidity_context_core97_kurt_63d_v098_signal(volume, close, closeadj, sharesbas):
    return _clean(_kurt(_safe_div(volume, _max(volume, 252)), 63))
def cg_f089_volume_liquidity_context_core98_kurt_63d_v099_signal(volume, close, closeadj, sharesbas):
    return _clean(_kurt(_safe_div(volume, _min(volume, 252)), 63))
def cg_f089_volume_liquidity_context_core99_kurt_63d_v100_signal(volume, close, closeadj, sharesbas):
    return _clean(_kurt(_safe_div(volume * close, _mean(volume * close, 252)), 63))

# core100-109: autocorr 21d
def cg_f089_volume_liquidity_context_core100_autocorr_21d_v101_signal(volume, close, closeadj, sharesbas):
    return _clean(_autocorr(volume, 21))
def cg_f089_volume_liquidity_context_core101_autocorr_21d_v102_signal(volume, close, closeadj, sharesbas):
    return _clean(_autocorr(_safe_div(volume, sharesbas), 21))
def cg_f089_volume_liquidity_context_core102_autocorr_21d_v103_signal(volume, close, closeadj, sharesbas):
    return _clean(_autocorr(volume * close, 21))
def cg_f089_volume_liquidity_context_core103_autocorr_21d_v104_signal(volume, close, closeadj, sharesbas):
    return _clean(_autocorr(_safe_div(volume, _mean(volume, 252)), 21))
def cg_f089_volume_liquidity_context_core104_autocorr_21d_v105_signal(volume, close, closeadj, sharesbas):
    return _clean(_autocorr(_pct_change(volume, 1), 21))
def cg_f089_volume_liquidity_context_core105_autocorr_21d_v106_signal(volume, close, closeadj, sharesbas):
    return _clean(_autocorr(_z(volume, 252), 21))
def cg_f089_volume_liquidity_context_core106_autocorr_21d_v107_signal(volume, close, closeadj, sharesbas):
    return _clean(_autocorr(_rank(volume, 252), 21))
def cg_f089_volume_liquidity_context_core107_autocorr_21d_v108_signal(volume, close, closeadj, sharesbas):
    return _clean(_autocorr(_safe_div(volume, _max(volume, 252)), 21))
def cg_f089_volume_liquidity_context_core108_autocorr_21d_v109_signal(volume, close, closeadj, sharesbas):
    return _clean(_autocorr(_safe_div(volume, _min(volume, 252)), 21))
def cg_f089_volume_liquidity_context_core109_autocorr_21d_v110_signal(volume, close, closeadj, sharesbas):
    return _clean(_autocorr(_safe_div(volume * close, _mean(volume * close, 252)), 21))

# core110-119: corr with close 21d
def cg_f089_volume_liquidity_context_core110_corr_close_21d_v111_signal(volume, close, closeadj, sharesbas):
    return _clean(_corr(volume, close, 21))
def cg_f089_volume_liquidity_context_core111_corr_close_21d_v112_signal(volume, close, closeadj, sharesbas):
    return _clean(_corr(_safe_div(volume, sharesbas), close, 21))
def cg_f089_volume_liquidity_context_core112_corr_close_21d_v113_signal(volume, close, closeadj, sharesbas):
    return _clean(_corr(volume * close, close, 21))
def cg_f089_volume_liquidity_context_core113_corr_close_21d_v114_signal(volume, close, closeadj, sharesbas):
    return _clean(_corr(_safe_div(volume, _mean(volume, 252)), close, 21))
def cg_f089_volume_liquidity_context_core114_corr_close_21d_v115_signal(volume, close, closeadj, sharesbas):
    return _clean(_corr(_pct_change(volume, 1), close, 21))
def cg_f089_volume_liquidity_context_core115_corr_close_21d_v116_signal(volume, close, closeadj, sharesbas):
    return _clean(_corr(_z(volume, 252), close, 21))
def cg_f089_volume_liquidity_context_core116_corr_close_21d_v117_signal(volume, close, closeadj, sharesbas):
    return _clean(_corr(_rank(volume, 252), close, 21))
def cg_f089_volume_liquidity_context_core117_corr_close_21d_v118_signal(volume, close, closeadj, sharesbas):
    return _clean(_corr(_safe_div(volume, _max(volume, 252)), close, 21))
def cg_f089_volume_liquidity_context_core118_corr_close_21d_v119_signal(volume, close, closeadj, sharesbas):
    return _clean(_corr(_safe_div(volume, _min(volume, 252)), close, 21))
def cg_f089_volume_liquidity_context_core119_corr_close_21d_v120_signal(volume, close, closeadj, sharesbas):
    return _clean(_corr(_safe_div(volume * close, _mean(volume * close, 252)), close, 21))

# core120-129: stability 21d
def cg_f089_volume_liquidity_context_core120_stability_21d_v121_signal(volume, close, closeadj, sharesbas):
    return _clean(_safe_div(_std(volume, 21), _mean(volume, 21)))
def cg_f089_volume_liquidity_context_core121_stability_21d_v122_signal(volume, close, closeadj, sharesbas):
    base = _safe_div(volume, sharesbas)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f089_volume_liquidity_context_core122_stability_21d_v123_signal(volume, close, closeadj, sharesbas):
    base = volume * close
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f089_volume_liquidity_context_core123_stability_21d_v124_signal(volume, close, closeadj, sharesbas):
    base = _safe_div(volume, _mean(volume, 252))
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f089_volume_liquidity_context_core124_stability_21d_v125_signal(volume, close, closeadj, sharesbas):
    base = _pct_change(volume, 1)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f089_volume_liquidity_context_core125_stability_21d_v126_signal(volume, close, closeadj, sharesbas):
    base = _z(volume, 252)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f089_volume_liquidity_context_core126_stability_21d_v127_signal(volume, close, closeadj, sharesbas):
    base = _rank(volume, 252)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f089_volume_liquidity_context_core127_stability_21d_v128_signal(volume, close, closeadj, sharesbas):
    base = _safe_div(volume, _max(volume, 252))
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f089_volume_liquidity_context_core128_stability_21d_v129_signal(volume, close, closeadj, sharesbas):
    base = _safe_div(volume, _min(volume, 252))
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f089_volume_liquidity_context_core129_stability_21d_v130_signal(volume, close, closeadj, sharesbas):
    base = _safe_div(volume * close, _mean(volume * close, 252))
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))

# core130-139: diff 5d
def cg_f089_volume_liquidity_context_core130_diff_5d_v131_signal(volume, close, closeadj, sharesbas):
    return _clean(_diff(volume, 5))
def cg_f089_volume_liquidity_context_core131_diff_5d_v132_signal(volume, close, closeadj, sharesbas):
    return _clean(_diff(_safe_div(volume, sharesbas), 5))
def cg_f089_volume_liquidity_context_core132_diff_5d_v133_signal(volume, close, closeadj, sharesbas):
    return _clean(_diff(volume * close, 5))
def cg_f089_volume_liquidity_context_core133_diff_5d_v134_signal(volume, close, closeadj, sharesbas):
    return _clean(_diff(_safe_div(volume, _mean(volume, 252)), 5))
def cg_f089_volume_liquidity_context_core134_diff_5d_v135_signal(volume, close, closeadj, sharesbas):
    return _clean(_diff(_pct_change(volume, 1), 5))
def cg_f089_volume_liquidity_context_core135_diff_5d_v136_signal(volume, close, closeadj, sharesbas):
    return _clean(_diff(_z(volume, 252), 5))
def cg_f089_volume_liquidity_context_core136_diff_5d_v137_signal(volume, close, closeadj, sharesbas):
    return _clean(_diff(_rank(volume, 252), 5))
def cg_f089_volume_liquidity_context_core137_diff_5d_v138_signal(volume, close, closeadj, sharesbas):
    return _clean(_diff(_safe_div(volume, _max(volume, 252)), 5))
def cg_f089_volume_liquidity_context_core138_diff_5d_v139_signal(volume, close, closeadj, sharesbas):
    return _clean(_diff(_safe_div(volume, _min(volume, 252)), 5))
def cg_f089_volume_liquidity_context_core139_diff_5d_v140_signal(volume, close, closeadj, sharesbas):
    return _clean(_diff(_safe_div(volume * close, _mean(volume * close, 252)), 5))

# core140-149: levels
def cg_f089_volume_liquidity_context_core140_level_v141_signal(volume, close, closeadj, sharesbas):
    return _clean(volume)
def cg_f089_volume_liquidity_context_core141_turnover_v142_signal(volume, close, closeadj, sharesbas):
    return _clean(_safe_div(volume, sharesbas))
def cg_f089_volume_liquidity_context_core142_dollar_vol_v143_signal(volume, close, closeadj, sharesbas):
    return _clean(volume * close)
def cg_f089_volume_liquidity_context_core143_vol_z_252d_v144_signal(volume, close, closeadj, sharesbas):
    return _clean(_z(volume, 252))
def cg_f089_volume_liquidity_context_core144_turnover_z_252d_v145_signal(volume, close, closeadj, sharesbas):
    return _clean(_z(_safe_div(volume, sharesbas), 252))
def cg_f089_volume_liquidity_context_core145_dollar_vol_z_252d_v146_signal(volume, close, closeadj, sharesbas):
    return _clean(_z(volume * close, 252))
def cg_f089_volume_liquidity_context_core146_vol_rank_252d_v147_signal(volume, close, closeadj, sharesbas):
    return _clean(_rank(volume, 252))
def cg_f089_volume_liquidity_context_core147_turnover_rank_252d_v148_signal(volume, close, closeadj, sharesbas):
    return _clean(_rank(_safe_div(volume, sharesbas), 252))
def cg_f089_volume_liquidity_context_core148_dollar_vol_rank_252d_v149_signal(volume, close, closeadj, sharesbas):
    return _clean(_rank(volume * close, 252))
def cg_f089_volume_liquidity_context_core149_sharesbas_v150_signal(volume, close, closeadj, sharesbas):
    return _clean(sharesbas)
