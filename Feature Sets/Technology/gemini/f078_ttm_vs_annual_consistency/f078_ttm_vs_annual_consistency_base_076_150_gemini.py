import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f078_ttm_vs_annual_consistency_core75_mean_4q_v076_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(dimension, 4))
def cg_f078_ttm_vs_annual_consistency_core76_mean_4q_v077_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(revenue, 4))
def cg_f078_ttm_vs_annual_consistency_core77_mean_4q_v078_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(ncfo, 4))
def cg_f078_ttm_vs_annual_consistency_core78_mean_4q_v079_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(netinc, 4))
def cg_f078_ttm_vs_annual_consistency_core79_mean_4q_v080_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(rnd, 4))
def cg_f078_ttm_vs_annual_consistency_core80_mean_8q_v081_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(dimension, 8))
def cg_f078_ttm_vs_annual_consistency_core81_mean_8q_v082_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(revenue, 8))
def cg_f078_ttm_vs_annual_consistency_core82_mean_8q_v083_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(ncfo, 8))
def cg_f078_ttm_vs_annual_consistency_core83_mean_8q_v084_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(netinc, 8))
def cg_f078_ttm_vs_annual_consistency_core84_mean_8q_v085_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(rnd, 8))
def cg_f078_ttm_vs_annual_consistency_core85_z_8q_v086_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(dimension, 8))
def cg_f078_ttm_vs_annual_consistency_core86_z_8q_v087_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(revenue, 8))
def cg_f078_ttm_vs_annual_consistency_core87_z_8q_v088_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(ncfo, 8))
def cg_f078_ttm_vs_annual_consistency_core88_z_8q_v089_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(netinc, 8))
def cg_f078_ttm_vs_annual_consistency_core89_z_8q_v090_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(rnd, 8))
def cg_f078_ttm_vs_annual_consistency_core90_z_20q_v091_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(dimension, 20))
def cg_f078_ttm_vs_annual_consistency_core91_z_20q_v092_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(revenue, 20))
def cg_f078_ttm_vs_annual_consistency_core92_z_20q_v093_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(ncfo, 20))
def cg_f078_ttm_vs_annual_consistency_core93_z_20q_v094_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(netinc, 20))
def cg_f078_ttm_vs_annual_consistency_core94_z_20q_v095_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(rnd, 20))
def cg_f078_ttm_vs_annual_consistency_core95_rank_12q_v096_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(dimension, 12))
def cg_f078_ttm_vs_annual_consistency_core96_rank_12q_v097_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(revenue, 12))
def cg_f078_ttm_vs_annual_consistency_core97_rank_12q_v098_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(ncfo, 12))
def cg_f078_ttm_vs_annual_consistency_core98_rank_12q_v099_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(netinc, 12))
def cg_f078_ttm_vs_annual_consistency_core99_rank_12q_v100_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(rnd, 12))
def cg_f078_ttm_vs_annual_consistency_core100_rank_20q_v101_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(dimension, 20))
def cg_f078_ttm_vs_annual_consistency_core101_rank_20q_v102_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(revenue, 20))
def cg_f078_ttm_vs_annual_consistency_core102_rank_20q_v103_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(ncfo, 20))
def cg_f078_ttm_vs_annual_consistency_core103_rank_20q_v104_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(netinc, 20))
def cg_f078_ttm_vs_annual_consistency_core104_rank_20q_v105_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(rnd, 20))
def cg_f078_ttm_vs_annual_consistency_core105_pct_1q_v106_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_pct_change(dimension, 1))
def cg_f078_ttm_vs_annual_consistency_core106_pct_1q_v107_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_pct_change(revenue, 1))
def cg_f078_ttm_vs_annual_consistency_core107_pct_1q_v108_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_pct_change(ncfo, 1))
def cg_f078_ttm_vs_annual_consistency_core108_pct_1q_v109_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_pct_change(netinc, 1))
def cg_f078_ttm_vs_annual_consistency_core109_pct_1q_v110_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_pct_change(rnd, 1))
def cg_f078_ttm_vs_annual_consistency_core110_pct_4q_v111_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_pct_change(dimension, 4))
def cg_f078_ttm_vs_annual_consistency_core111_pct_4q_v112_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_pct_change(revenue, 4))
def cg_f078_ttm_vs_annual_consistency_core112_pct_4q_v113_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_pct_change(ncfo, 4))
def cg_f078_ttm_vs_annual_consistency_core113_pct_4q_v114_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_pct_change(netinc, 4))
def cg_f078_ttm_vs_annual_consistency_core114_pct_4q_v115_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_pct_change(rnd, 4))
def cg_f078_ttm_vs_annual_consistency_core115_slope_4q_v116_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(dimension, 4))
def cg_f078_ttm_vs_annual_consistency_core116_slope_4q_v117_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(revenue, 4))
def cg_f078_ttm_vs_annual_consistency_core117_slope_4q_v118_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(ncfo, 4))
def cg_f078_ttm_vs_annual_consistency_core118_slope_4q_v119_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(netinc, 4))
def cg_f078_ttm_vs_annual_consistency_core119_slope_4q_v120_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(rnd, 4))
def cg_f078_ttm_vs_annual_consistency_core120_slope_8q_v121_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(dimension, 8))
def cg_f078_ttm_vs_annual_consistency_core121_slope_8q_v122_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(revenue, 8))
def cg_f078_ttm_vs_annual_consistency_core122_slope_8q_v123_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(ncfo, 8))
def cg_f078_ttm_vs_annual_consistency_core123_slope_8q_v124_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(netinc, 8))
def cg_f078_ttm_vs_annual_consistency_core124_slope_8q_v125_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(rnd, 8))
def cg_f078_ttm_vs_annual_consistency_core125_autocorr_8q_v126_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_autocorr(dimension, 8))
def cg_f078_ttm_vs_annual_consistency_core126_autocorr_8q_v127_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_autocorr(revenue, 8))
def cg_f078_ttm_vs_annual_consistency_core127_autocorr_8q_v128_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_autocorr(ncfo, 8))
def cg_f078_ttm_vs_annual_consistency_core128_autocorr_8q_v129_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_autocorr(netinc, 8))
def cg_f078_ttm_vs_annual_consistency_core129_autocorr_8q_v130_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_autocorr(rnd, 8))
def cg_f078_ttm_vs_annual_consistency_core130_ewm_4q_v131_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_ewm(dimension, 4))
def cg_f078_ttm_vs_annual_consistency_core131_ewm_4q_v132_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_ewm(revenue, 4))
def cg_f078_ttm_vs_annual_consistency_core132_ewm_4q_v133_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_ewm(ncfo, 4))
def cg_f078_ttm_vs_annual_consistency_core133_ewm_4q_v134_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_ewm(netinc, 4))
def cg_f078_ttm_vs_annual_consistency_core134_ewm_4q_v135_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_ewm(rnd, 4))
def cg_f078_ttm_vs_annual_consistency_core135_ewm_8q_v136_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_ewm(dimension, 8))
def cg_f078_ttm_vs_annual_consistency_core136_ewm_8q_v137_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_ewm(revenue, 8))
def cg_f078_ttm_vs_annual_consistency_core137_ewm_8q_v138_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_ewm(ncfo, 8))
def cg_f078_ttm_vs_annual_consistency_core138_ewm_8q_v139_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_ewm(netinc, 8))
def cg_f078_ttm_vs_annual_consistency_core139_ewm_8q_v140_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_ewm(rnd, 8))
def cg_f078_ttm_vs_annual_consistency_core140_std_8q_v141_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_std(dimension, 8))
def cg_f078_ttm_vs_annual_consistency_core141_std_8q_v142_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_std(revenue, 8))
def cg_f078_ttm_vs_annual_consistency_core142_std_8q_v143_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_std(ncfo, 8))
def cg_f078_ttm_vs_annual_consistency_core143_std_8q_v144_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_std(netinc, 8))
def cg_f078_ttm_vs_annual_consistency_core144_std_8q_v145_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_std(rnd, 8))
def cg_f078_ttm_vs_annual_consistency_core145_diff_1q_v146_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(dimension, 1))
def cg_f078_ttm_vs_annual_consistency_core146_diff_1q_v147_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(revenue, 1))
def cg_f078_ttm_vs_annual_consistency_core147_diff_1q_v148_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(ncfo, 1))
def cg_f078_ttm_vs_annual_consistency_core148_diff_1q_v149_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(netinc, 1))
def cg_f078_ttm_vs_annual_consistency_core149_diff_1q_v150_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(rnd, 1))