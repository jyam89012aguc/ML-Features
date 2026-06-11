import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: ewm 21d (continued)
def cg_f088_ohlcv_multi_year_highs_core75_ewm_21d_v076_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(_z(closeadj, 252), 21))
def cg_f088_ohlcv_multi_year_highs_core76_ewm_21d_v077_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(_rank(closeadj, 252), 21))
def cg_f088_ohlcv_multi_year_highs_core77_ewm_21d_v078_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(_safe_div(closeadj, _max(closeadj, 252)), 21))
def cg_f088_ohlcv_multi_year_highs_core78_ewm_21d_v079_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(_safe_div(closeadj, _min(closeadj, 252)), 21))
def cg_f088_ohlcv_multi_year_highs_core79_ewm_21d_v080_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(_safe_div(volume, _max(volume, 252)), 21))

# core80-89: skew 63d
def cg_f088_ohlcv_multi_year_highs_core80_skew_63d_v081_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_skew(closeadj, 63))
def cg_f088_ohlcv_multi_year_highs_core81_skew_63d_v082_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_skew(_safe_div(closeadj, open), 63))
def cg_f088_ohlcv_multi_year_highs_core82_skew_63d_v083_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_skew(_safe_div(high, low), 63))
def cg_f088_ohlcv_multi_year_highs_core83_skew_63d_v084_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_skew(volume, 63))
def cg_f088_ohlcv_multi_year_highs_core84_skew_63d_v085_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_skew(_pct_change(closeadj, 1), 63))
def cg_f088_ohlcv_multi_year_highs_core85_skew_63d_v086_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_skew(_z(closeadj, 252), 63))
def cg_f088_ohlcv_multi_year_highs_core86_skew_63d_v087_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_skew(_rank(closeadj, 252), 63))
def cg_f088_ohlcv_multi_year_highs_core87_skew_63d_v088_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_skew(_safe_div(closeadj, _max(closeadj, 252)), 63))
def cg_f088_ohlcv_multi_year_highs_core88_skew_63d_v089_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_skew(_safe_div(closeadj, _min(closeadj, 252)), 63))
def cg_f088_ohlcv_multi_year_highs_core89_skew_63d_v090_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_skew(_safe_div(volume, _max(volume, 252)), 63))

# core90-99: kurt 63d
def cg_f088_ohlcv_multi_year_highs_core90_kurt_63d_v091_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_kurt(closeadj, 63))
def cg_f088_ohlcv_multi_year_highs_core91_kurt_63d_v092_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_kurt(_safe_div(closeadj, open), 63))
def cg_f088_ohlcv_multi_year_highs_core92_kurt_63d_v093_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_kurt(_safe_div(high, low), 63))
def cg_f088_ohlcv_multi_year_highs_core93_kurt_63d_v094_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_kurt(volume, 63))
def cg_f088_ohlcv_multi_year_highs_core94_kurt_63d_v095_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_kurt(_pct_change(closeadj, 1), 63))
def cg_f088_ohlcv_multi_year_highs_core95_kurt_63d_v096_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_kurt(_z(closeadj, 252), 63))
def cg_f088_ohlcv_multi_year_highs_core96_kurt_63d_v097_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_kurt(_rank(closeadj, 252), 63))
def cg_f088_ohlcv_multi_year_highs_core97_kurt_63d_v098_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_kurt(_safe_div(closeadj, _max(closeadj, 252)), 63))
def cg_f088_ohlcv_multi_year_highs_core98_kurt_63d_v099_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_kurt(_safe_div(closeadj, _min(closeadj, 252)), 63))
def cg_f088_ohlcv_multi_year_highs_core99_kurt_63d_v100_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_kurt(_safe_div(volume, _max(volume, 252)), 63))

# core100-109: autocorr 21d
def cg_f088_ohlcv_multi_year_highs_core100_autocorr_21d_v101_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(closeadj, 21))
def cg_f088_ohlcv_multi_year_highs_core101_autocorr_21d_v102_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(_safe_div(closeadj, open), 21))
def cg_f088_ohlcv_multi_year_highs_core102_autocorr_21d_v103_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(_safe_div(high, low), 21))
def cg_f088_ohlcv_multi_year_highs_core103_autocorr_21d_v104_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(volume, 21))
def cg_f088_ohlcv_multi_year_highs_core104_autocorr_21d_v105_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(_pct_change(closeadj, 1), 21))
def cg_f088_ohlcv_multi_year_highs_core105_autocorr_21d_v106_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(_z(closeadj, 252), 21))
def cg_f088_ohlcv_multi_year_highs_core106_autocorr_21d_v107_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(_rank(closeadj, 252), 21))
def cg_f088_ohlcv_multi_year_highs_core107_autocorr_21d_v108_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(_safe_div(closeadj, _max(closeadj, 252)), 21))
def cg_f088_ohlcv_multi_year_highs_core108_autocorr_21d_v109_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(_safe_div(closeadj, _min(closeadj, 252)), 21))
def cg_f088_ohlcv_multi_year_highs_core109_autocorr_21d_v110_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(_safe_div(volume, _max(volume, 252)), 21))

# core110-119: corr with volume 21d
def cg_f088_ohlcv_multi_year_highs_core110_corr_vol_21d_v111_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_corr(closeadj, volume, 21))
def cg_f088_ohlcv_multi_year_highs_core111_corr_vol_21d_v112_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_corr(_safe_div(closeadj, open), volume, 21))
def cg_f088_ohlcv_multi_year_highs_core112_corr_vol_21d_v113_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_corr(_safe_div(high, low), volume, 21))
def cg_f088_ohlcv_multi_year_highs_core113_corr_vol_21d_v114_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_corr(volume, _mean(volume, 252), 21))
def cg_f088_ohlcv_multi_year_highs_core114_corr_vol_21d_v115_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_corr(_pct_change(closeadj, 1), volume, 21))
def cg_f088_ohlcv_multi_year_highs_core115_corr_vol_21d_v116_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_corr(_z(closeadj, 252), volume, 21))
def cg_f088_ohlcv_multi_year_highs_core116_corr_vol_21d_v117_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_corr(_rank(closeadj, 252), volume, 21))
def cg_f088_ohlcv_multi_year_highs_core117_corr_vol_21d_v118_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_corr(_safe_div(closeadj, _max(closeadj, 252)), volume, 21))
def cg_f088_ohlcv_multi_year_highs_core118_corr_vol_21d_v119_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_corr(_safe_div(closeadj, _min(closeadj, 252)), volume, 21))
def cg_f088_ohlcv_multi_year_highs_core119_corr_vol_21d_v120_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_corr(_safe_div(volume, _max(volume, 252)), volume, 21))

# core120-129: stability 21d
def cg_f088_ohlcv_multi_year_highs_core120_stability_21d_v121_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_safe_div(_std(closeadj, 21), _mean(closeadj, 21)))
def cg_f088_ohlcv_multi_year_highs_core121_stability_21d_v122_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    base = _safe_div(closeadj, open)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f088_ohlcv_multi_year_highs_core122_stability_21d_v123_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    base = _safe_div(high, low)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f088_ohlcv_multi_year_highs_core123_stability_21d_v124_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    base = volume
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f088_ohlcv_multi_year_highs_core124_stability_21d_v125_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    base = _pct_change(closeadj, 1)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f088_ohlcv_multi_year_highs_core125_stability_21d_v126_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    base = _z(closeadj, 252)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f088_ohlcv_multi_year_highs_core126_stability_21d_v127_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    base = _rank(closeadj, 252)
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f088_ohlcv_multi_year_highs_core127_stability_21d_v128_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    base = _safe_div(closeadj, _max(closeadj, 252))
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f088_ohlcv_multi_year_highs_core128_stability_21d_v129_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    base = _safe_div(closeadj, _min(closeadj, 252))
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))
def cg_f088_ohlcv_multi_year_highs_core129_stability_21d_v130_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    base = _safe_div(volume, _max(volume, 252))
    return _clean(_safe_div(_std(base, 21), _mean(base, 21)))

# core130-139: diff 5d
def cg_f088_ohlcv_multi_year_highs_core130_diff_5d_v131_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(closeadj, 5))
def cg_f088_ohlcv_multi_year_highs_core131_diff_5d_v132_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_safe_div(closeadj, open), 5))
def cg_f088_ohlcv_multi_year_highs_core132_diff_5d_v133_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_safe_div(high, low), 5))
def cg_f088_ohlcv_multi_year_highs_core133_diff_5d_v134_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(volume, 5))
def cg_f088_ohlcv_multi_year_highs_core134_diff_5d_v135_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_pct_change(closeadj, 1), 5))
def cg_f088_ohlcv_multi_year_highs_core135_diff_5d_v136_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_z(closeadj, 252), 5))
def cg_f088_ohlcv_multi_year_highs_core136_diff_5d_v137_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_rank(closeadj, 252), 5))
def cg_f088_ohlcv_multi_year_highs_core137_diff_5d_v138_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_safe_div(closeadj, _max(closeadj, 252)), 5))
def cg_f088_ohlcv_multi_year_highs_core138_diff_5d_v139_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_safe_div(closeadj, _min(closeadj, 252)), 5))
def cg_f088_ohlcv_multi_year_highs_core139_diff_5d_v140_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(_safe_div(volume, _max(volume, 252)), 5))

# core140-149: levels
def cg_f088_ohlcv_multi_year_highs_core140_level_v141_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(closeadj)
def cg_f088_ohlcv_multi_year_highs_core141_open_v142_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(open)
def cg_f088_ohlcv_multi_year_highs_core142_high_v143_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(high)
def cg_f088_ohlcv_multi_year_highs_core143_low_v144_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(low)
def cg_f088_ohlcv_multi_year_highs_core144_volume_v145_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(volume)
def cg_f088_ohlcv_multi_year_highs_core145_closeunadj_v146_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(closeunadj)
def cg_f088_ohlcv_multi_year_highs_core146_co_range_v147_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_safe_div(close - open, open))
def cg_f088_ohlcv_multi_year_highs_core147_hl_range_v148_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_safe_div(high - low, low))
def cg_f088_ohlcv_multi_year_highs_core148_cl_range_v149_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_safe_div(close - low, high - low))
def cg_f088_ohlcv_multi_year_highs_core149_vol_norm_v150_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_safe_div(volume, _mean(volume, 252)))
