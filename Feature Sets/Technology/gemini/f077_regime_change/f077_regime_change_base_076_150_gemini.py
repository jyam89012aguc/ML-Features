import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f077_regime_change_core75_ewm_8q_v076_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_ewm(opex, 8))
def cg_f077_regime_change_core76_ewm_8q_v077_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_ewm(cashneq, 8))
def cg_f077_regime_change_core77_ewm_8q_v078_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_ewm(fcf, 8))
def cg_f077_regime_change_core78_std_8q_v079_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_std(revenue, 8))
def cg_f077_regime_change_core79_std_8q_v080_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_std(rnd, 8))
def cg_f077_regime_change_core80_std_8q_v081_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_std(ncfo, 8))
def cg_f077_regime_change_core81_std_8q_v082_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_std(opex, 8))
def cg_f077_regime_change_core82_std_8q_v083_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_std(cashneq, 8))
def cg_f077_regime_change_core83_std_8q_v084_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_std(fcf, 8))
def cg_f077_regime_change_core84_diff_1q_v085_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(revenue, 1))
def cg_f077_regime_change_core85_diff_1q_v086_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(rnd, 1))
def cg_f077_regime_change_core86_diff_1q_v087_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(ncfo, 1))
def cg_f077_regime_change_core87_diff_1q_v088_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(opex, 1))
def cg_f077_regime_change_core88_diff_1q_v089_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(cashneq, 1))
def cg_f077_regime_change_core89_diff_1q_v090_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_diff(fcf, 1))
def cg_f077_regime_change_core90_mean_4q_v091_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(revenue, 4))
def cg_f077_regime_change_core91_mean_4q_v092_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(rnd, 4))
def cg_f077_regime_change_core92_mean_4q_v093_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(ncfo, 4))
def cg_f077_regime_change_core93_mean_4q_v094_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(opex, 4))
def cg_f077_regime_change_core94_mean_4q_v095_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(cashneq, 4))
def cg_f077_regime_change_core95_mean_4q_v096_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(fcf, 4))
def cg_f077_regime_change_core96_mean_8q_v097_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(revenue, 8))
def cg_f077_regime_change_core97_mean_8q_v098_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(rnd, 8))
def cg_f077_regime_change_core98_mean_8q_v099_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(ncfo, 8))
def cg_f077_regime_change_core99_mean_8q_v100_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(opex, 8))
def cg_f077_regime_change_core100_mean_8q_v101_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(cashneq, 8))
def cg_f077_regime_change_core101_mean_8q_v102_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_mean(fcf, 8))
def cg_f077_regime_change_core102_z_8q_v103_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(revenue, 8))
def cg_f077_regime_change_core103_z_8q_v104_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(rnd, 8))
def cg_f077_regime_change_core104_z_8q_v105_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(ncfo, 8))
def cg_f077_regime_change_core105_z_8q_v106_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(opex, 8))
def cg_f077_regime_change_core106_z_8q_v107_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(cashneq, 8))
def cg_f077_regime_change_core107_z_8q_v108_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(fcf, 8))
def cg_f077_regime_change_core108_z_20q_v109_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(revenue, 20))
def cg_f077_regime_change_core109_z_20q_v110_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(rnd, 20))
def cg_f077_regime_change_core110_z_20q_v111_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(ncfo, 20))
def cg_f077_regime_change_core111_z_20q_v112_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(opex, 20))
def cg_f077_regime_change_core112_z_20q_v113_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(cashneq, 20))
def cg_f077_regime_change_core113_z_20q_v114_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_z(fcf, 20))
def cg_f077_regime_change_core114_rank_12q_v115_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(revenue, 12))
def cg_f077_regime_change_core115_rank_12q_v116_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(rnd, 12))
def cg_f077_regime_change_core116_rank_12q_v117_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(ncfo, 12))
def cg_f077_regime_change_core117_rank_12q_v118_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(opex, 12))
def cg_f077_regime_change_core118_rank_12q_v119_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(cashneq, 12))
def cg_f077_regime_change_core119_rank_12q_v120_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(fcf, 12))
def cg_f077_regime_change_core120_rank_20q_v121_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(revenue, 20))
def cg_f077_regime_change_core121_rank_20q_v122_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(rnd, 20))
def cg_f077_regime_change_core122_rank_20q_v123_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(ncfo, 20))
def cg_f077_regime_change_core123_rank_20q_v124_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(opex, 20))
def cg_f077_regime_change_core124_rank_20q_v125_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(cashneq, 20))
def cg_f077_regime_change_core125_rank_20q_v126_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_rank(fcf, 20))
def cg_f077_regime_change_core126_pct_1q_v127_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(revenue, 1))
def cg_f077_regime_change_core127_pct_1q_v128_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(rnd, 1))
def cg_f077_regime_change_core128_pct_1q_v129_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(ncfo, 1))
def cg_f077_regime_change_core129_pct_1q_v130_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(opex, 1))
def cg_f077_regime_change_core130_pct_1q_v131_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(cashneq, 1))
def cg_f077_regime_change_core131_pct_1q_v132_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(fcf, 1))
def cg_f077_regime_change_core132_pct_4q_v133_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(revenue, 4))
def cg_f077_regime_change_core133_pct_4q_v134_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(rnd, 4))
def cg_f077_regime_change_core134_pct_4q_v135_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(ncfo, 4))
def cg_f077_regime_change_core135_pct_4q_v136_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(opex, 4))
def cg_f077_regime_change_core136_pct_4q_v137_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(cashneq, 4))
def cg_f077_regime_change_core137_pct_4q_v138_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_pct_change(fcf, 4))
def cg_f077_regime_change_core138_slope_4q_v139_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(revenue, 4))
def cg_f077_regime_change_core139_slope_4q_v140_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(rnd, 4))
def cg_f077_regime_change_core140_slope_4q_v141_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(ncfo, 4))
def cg_f077_regime_change_core141_slope_4q_v142_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(opex, 4))
def cg_f077_regime_change_core142_slope_4q_v143_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(cashneq, 4))
def cg_f077_regime_change_core143_slope_4q_v144_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(fcf, 4))
def cg_f077_regime_change_core144_slope_8q_v145_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(revenue, 8))
def cg_f077_regime_change_core145_slope_8q_v146_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(rnd, 8))
def cg_f077_regime_change_core146_slope_8q_v147_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(ncfo, 8))
def cg_f077_regime_change_core147_slope_8q_v148_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(opex, 8))
def cg_f077_regime_change_core148_slope_8q_v149_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(cashneq, 8))
def cg_f077_regime_change_core149_slope_8q_v150_signal(revenue, rnd, ncfo, opex, cashneq, fcf):
    return _clean(_slope(fcf, 8))