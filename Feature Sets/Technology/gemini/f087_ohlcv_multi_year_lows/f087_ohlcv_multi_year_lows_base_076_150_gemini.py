import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f087_ohlcv_multi_year_lows_core75_slope_8q_v076_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(low, 8))
def cg_f087_ohlcv_multi_year_lows_core76_slope_8q_v077_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(close, 8))
def cg_f087_ohlcv_multi_year_lows_core77_slope_8q_v078_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(volume, 8))
def cg_f087_ohlcv_multi_year_lows_core78_slope_8q_v079_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(closeadj, 8))
def cg_f087_ohlcv_multi_year_lows_core79_slope_8q_v080_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(closeunadj, 8))
def cg_f087_ohlcv_multi_year_lows_core80_autocorr_8q_v081_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(date, 8))
def cg_f087_ohlcv_multi_year_lows_core81_autocorr_8q_v082_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(open, 8))
def cg_f087_ohlcv_multi_year_lows_core82_autocorr_8q_v083_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(high, 8))
def cg_f087_ohlcv_multi_year_lows_core83_autocorr_8q_v084_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(low, 8))
def cg_f087_ohlcv_multi_year_lows_core84_autocorr_8q_v085_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(close, 8))
def cg_f087_ohlcv_multi_year_lows_core85_autocorr_8q_v086_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(volume, 8))
def cg_f087_ohlcv_multi_year_lows_core86_autocorr_8q_v087_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(closeadj, 8))
def cg_f087_ohlcv_multi_year_lows_core87_autocorr_8q_v088_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_autocorr(closeunadj, 8))
def cg_f087_ohlcv_multi_year_lows_core88_ewm_4q_v089_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(date, 4))
def cg_f087_ohlcv_multi_year_lows_core89_ewm_4q_v090_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(open, 4))
def cg_f087_ohlcv_multi_year_lows_core90_ewm_4q_v091_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(high, 4))
def cg_f087_ohlcv_multi_year_lows_core91_ewm_4q_v092_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(low, 4))
def cg_f087_ohlcv_multi_year_lows_core92_ewm_4q_v093_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(close, 4))
def cg_f087_ohlcv_multi_year_lows_core93_ewm_4q_v094_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(volume, 4))
def cg_f087_ohlcv_multi_year_lows_core94_ewm_4q_v095_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(closeadj, 4))
def cg_f087_ohlcv_multi_year_lows_core95_ewm_4q_v096_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(closeunadj, 4))
def cg_f087_ohlcv_multi_year_lows_core96_ewm_8q_v097_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(date, 8))
def cg_f087_ohlcv_multi_year_lows_core97_ewm_8q_v098_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(open, 8))
def cg_f087_ohlcv_multi_year_lows_core98_ewm_8q_v099_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(high, 8))
def cg_f087_ohlcv_multi_year_lows_core99_ewm_8q_v100_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(low, 8))
def cg_f087_ohlcv_multi_year_lows_core100_ewm_8q_v101_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(close, 8))
def cg_f087_ohlcv_multi_year_lows_core101_ewm_8q_v102_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(volume, 8))
def cg_f087_ohlcv_multi_year_lows_core102_ewm_8q_v103_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(closeadj, 8))
def cg_f087_ohlcv_multi_year_lows_core103_ewm_8q_v104_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(closeunadj, 8))
def cg_f087_ohlcv_multi_year_lows_core104_std_8q_v105_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(date, 8))
def cg_f087_ohlcv_multi_year_lows_core105_std_8q_v106_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(open, 8))
def cg_f087_ohlcv_multi_year_lows_core106_std_8q_v107_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(high, 8))
def cg_f087_ohlcv_multi_year_lows_core107_std_8q_v108_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(low, 8))
def cg_f087_ohlcv_multi_year_lows_core108_std_8q_v109_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(close, 8))
def cg_f087_ohlcv_multi_year_lows_core109_std_8q_v110_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(volume, 8))
def cg_f087_ohlcv_multi_year_lows_core110_std_8q_v111_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(closeadj, 8))
def cg_f087_ohlcv_multi_year_lows_core111_std_8q_v112_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(closeunadj, 8))
def cg_f087_ohlcv_multi_year_lows_core112_diff_1q_v113_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(date, 1))
def cg_f087_ohlcv_multi_year_lows_core113_diff_1q_v114_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(open, 1))
def cg_f087_ohlcv_multi_year_lows_core114_diff_1q_v115_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(high, 1))
def cg_f087_ohlcv_multi_year_lows_core115_diff_1q_v116_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(low, 1))
def cg_f087_ohlcv_multi_year_lows_core116_diff_1q_v117_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(close, 1))
def cg_f087_ohlcv_multi_year_lows_core117_diff_1q_v118_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(volume, 1))
def cg_f087_ohlcv_multi_year_lows_core118_diff_1q_v119_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(closeadj, 1))
def cg_f087_ohlcv_multi_year_lows_core119_diff_1q_v120_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_diff(closeunadj, 1))
def cg_f087_ohlcv_multi_year_lows_core120_mean_4q_v121_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(date, 4))
def cg_f087_ohlcv_multi_year_lows_core121_mean_4q_v122_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(open, 4))
def cg_f087_ohlcv_multi_year_lows_core122_mean_4q_v123_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(high, 4))
def cg_f087_ohlcv_multi_year_lows_core123_mean_4q_v124_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(low, 4))
def cg_f087_ohlcv_multi_year_lows_core124_mean_4q_v125_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(close, 4))
def cg_f087_ohlcv_multi_year_lows_core125_mean_4q_v126_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(volume, 4))
def cg_f087_ohlcv_multi_year_lows_core126_mean_4q_v127_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(closeadj, 4))
def cg_f087_ohlcv_multi_year_lows_core127_mean_4q_v128_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(closeunadj, 4))
def cg_f087_ohlcv_multi_year_lows_core128_mean_8q_v129_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(date, 8))
def cg_f087_ohlcv_multi_year_lows_core129_mean_8q_v130_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(open, 8))
def cg_f087_ohlcv_multi_year_lows_core130_mean_8q_v131_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(high, 8))
def cg_f087_ohlcv_multi_year_lows_core131_mean_8q_v132_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(low, 8))
def cg_f087_ohlcv_multi_year_lows_core132_mean_8q_v133_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(close, 8))
def cg_f087_ohlcv_multi_year_lows_core133_mean_8q_v134_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(volume, 8))
def cg_f087_ohlcv_multi_year_lows_core134_mean_8q_v135_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(closeadj, 8))
def cg_f087_ohlcv_multi_year_lows_core135_mean_8q_v136_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(closeunadj, 8))
def cg_f087_ohlcv_multi_year_lows_core136_z_8q_v137_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(date, 8))
def cg_f087_ohlcv_multi_year_lows_core137_z_8q_v138_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(open, 8))
def cg_f087_ohlcv_multi_year_lows_core138_z_8q_v139_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(high, 8))
def cg_f087_ohlcv_multi_year_lows_core139_z_8q_v140_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(low, 8))
def cg_f087_ohlcv_multi_year_lows_core140_z_8q_v141_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(close, 8))
def cg_f087_ohlcv_multi_year_lows_core141_z_8q_v142_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(volume, 8))
def cg_f087_ohlcv_multi_year_lows_core142_z_8q_v143_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(closeadj, 8))
def cg_f087_ohlcv_multi_year_lows_core143_z_8q_v144_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(closeunadj, 8))
def cg_f087_ohlcv_multi_year_lows_core144_z_20q_v145_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(date, 20))
def cg_f087_ohlcv_multi_year_lows_core145_z_20q_v146_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(open, 20))
def cg_f087_ohlcv_multi_year_lows_core146_z_20q_v147_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(high, 20))
def cg_f087_ohlcv_multi_year_lows_core147_z_20q_v148_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(low, 20))
def cg_f087_ohlcv_multi_year_lows_core148_z_20q_v149_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(close, 20))
def cg_f087_ohlcv_multi_year_lows_core149_z_20q_v150_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(volume, 20))