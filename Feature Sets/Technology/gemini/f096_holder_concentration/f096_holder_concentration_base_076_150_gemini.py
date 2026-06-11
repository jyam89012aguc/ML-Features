import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f096_holder_concentration_core75_pct_4q_v076_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(_safe_div(value, shrholders), 4))
def cg_f096_holder_concentration_core76_pct_4q_v077_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(_safe_div(totalvalue, shrholders), 4))
def cg_f096_holder_concentration_core77_pct_4q_v078_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(_safe_div(value, percentoftotal + 1e-9), 4))
def cg_f096_holder_concentration_core78_pct_4q_v079_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(_safe_div(totalvalue, percentoftotal + 1e-9), 4))
def cg_f096_holder_concentration_core79_pct_4q_v080_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_pct_change(_safe_div(shrholders, percentoftotal + 1e-9), 4))
# core80-89: std_8q
def cg_f096_holder_concentration_core80_std_8q_v081_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_std(value, 8))
def cg_f096_holder_concentration_core81_std_8q_v082_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_std(shrholders, 8))
def cg_f096_holder_concentration_core82_std_8q_v083_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_std(totalvalue, 8))
def cg_f096_holder_concentration_core83_std_8q_v084_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_std(percentoftotal, 8))
def cg_f096_holder_concentration_core84_std_8q_v085_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_std(_safe_div(value, totalvalue), 8))
def cg_f096_holder_concentration_core85_std_8q_v086_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_std(_safe_div(value, shrholders), 8))
def cg_f096_holder_concentration_core86_std_8q_v087_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_std(_safe_div(totalvalue, shrholders), 8))
def cg_f096_holder_concentration_core87_std_8q_v088_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_std(_safe_div(value, percentoftotal + 1e-9), 8))
def cg_f096_holder_concentration_core88_std_8q_v089_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_std(_safe_div(totalvalue, percentoftotal + 1e-9), 8))
def cg_f096_holder_concentration_core89_std_8q_v090_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_std(_safe_div(shrholders, percentoftotal + 1e-9), 8))
# core90-99: log
def cg_f096_holder_concentration_core90_log_v091_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_log(value.clip(lower=0.001) if hasattr(value, 'clip') else value))
def cg_f096_holder_concentration_core91_log_v092_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_log(shrholders.clip(lower=0.001) if hasattr(shrholders, 'clip') else shrholders))
def cg_f096_holder_concentration_core92_log_v093_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_log(totalvalue.clip(lower=0.001) if hasattr(totalvalue, 'clip') else totalvalue))
def cg_f096_holder_concentration_core93_log_v094_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_log(percentoftotal.clip(lower=0.001) if hasattr(percentoftotal, 'clip') else percentoftotal))
def cg_f096_holder_concentration_core94_log_v095_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_log(_safe_div(value, totalvalue).clip(lower=0.001) if hasattr(_safe_div(value, totalvalue), 'clip') else _safe_div(value, totalvalue)))
def cg_f096_holder_concentration_core95_log_v096_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_log(_safe_div(value, shrholders).clip(lower=0.001) if hasattr(_safe_div(value, shrholders), 'clip') else _safe_div(value, shrholders)))
def cg_f096_holder_concentration_core96_log_v097_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_log(_safe_div(totalvalue, shrholders).clip(lower=0.001) if hasattr(_safe_div(totalvalue, shrholders), 'clip') else _safe_div(totalvalue, shrholders)))
def cg_f096_holder_concentration_core97_log_v098_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_log(_safe_div(value, percentoftotal + 1e-9).clip(lower=0.001) if hasattr(_safe_div(value, percentoftotal + 1e-9), 'clip') else _safe_div(value, percentoftotal + 1e-9)))
def cg_f096_holder_concentration_core98_log_v099_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_log(_safe_div(totalvalue, percentoftotal + 1e-9).clip(lower=0.001) if hasattr(_safe_div(totalvalue, percentoftotal + 1e-9), 'clip') else _safe_div(totalvalue, percentoftotal + 1e-9)))
def cg_f096_holder_concentration_core99_log_v100_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_log(_safe_div(shrholders, percentoftotal + 1e-9).clip(lower=0.001) if hasattr(_safe_div(shrholders, percentoftotal + 1e-9), 'clip') else _safe_div(shrholders, percentoftotal + 1e-9)))
# core100-109: diff_1q
def cg_f096_holder_concentration_core100_diff_1q_v101_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(value, 1))
def cg_f096_holder_concentration_core101_diff_1q_v102_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(shrholders, 1))
def cg_f096_holder_concentration_core102_diff_1q_v103_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(totalvalue, 1))
def cg_f096_holder_concentration_core103_diff_1q_v104_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(percentoftotal, 1))
def cg_f096_holder_concentration_core104_diff_1q_v105_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_safe_div(value, totalvalue), 1))
def cg_f096_holder_concentration_core105_diff_1q_v106_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_safe_div(value, shrholders), 1))
def cg_f096_holder_concentration_core106_diff_1q_v107_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_safe_div(totalvalue, shrholders), 1))
def cg_f096_holder_concentration_core107_diff_1q_v108_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_safe_div(value, percentoftotal + 1e-9), 1))
def cg_f096_holder_concentration_core108_diff_1q_v109_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_safe_div(totalvalue, percentoftotal + 1e-9), 1))
def cg_f096_holder_concentration_core109_diff_1q_v110_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_diff(_safe_div(shrholders, percentoftotal + 1e-9), 1))
# core110-119: slope_4q
def cg_f096_holder_concentration_core110_slope_4q_v111_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(value, 4))
def cg_f096_holder_concentration_core111_slope_4q_v112_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(shrholders, 4))
def cg_f096_holder_concentration_core112_slope_4q_v113_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(totalvalue, 4))
def cg_f096_holder_concentration_core113_slope_4q_v114_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(percentoftotal, 4))
def cg_f096_holder_concentration_core114_slope_4q_v115_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_safe_div(value, totalvalue), 4))
def cg_f096_holder_concentration_core115_slope_4q_v116_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_safe_div(value, shrholders), 4))
def cg_f096_holder_concentration_core116_slope_4q_v117_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_safe_div(totalvalue, shrholders), 4))
def cg_f096_holder_concentration_core117_slope_4q_v118_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_safe_div(value, percentoftotal + 1e-9), 4))
def cg_f096_holder_concentration_core118_slope_4q_v119_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_safe_div(totalvalue, percentoftotal + 1e-9), 4))
def cg_f096_holder_concentration_core119_slope_4q_v120_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_slope(_safe_div(shrholders, percentoftotal + 1e-9), 4))
# core120-129: ewm_8q
def cg_f096_holder_concentration_core120_ewm_8q_v121_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_ewm(value, 8))
def cg_f096_holder_concentration_core121_ewm_8q_v122_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_ewm(shrholders, 8))
def cg_f096_holder_concentration_core122_ewm_8q_v123_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_ewm(totalvalue, 8))
def cg_f096_holder_concentration_core123_ewm_8q_v124_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_ewm(percentoftotal, 8))
def cg_f096_holder_concentration_core124_ewm_8q_v125_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_ewm(_safe_div(value, totalvalue), 8))
def cg_f096_holder_concentration_core125_ewm_8q_v126_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_ewm(_safe_div(value, shrholders), 8))
def cg_f096_holder_concentration_core126_ewm_8q_v127_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_ewm(_safe_div(totalvalue, shrholders), 8))
def cg_f096_holder_concentration_core127_ewm_8q_v128_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_ewm(_safe_div(value, percentoftotal + 1e-9), 8))
def cg_f096_holder_concentration_core128_ewm_8q_v129_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_ewm(_safe_div(totalvalue, percentoftotal + 1e-9), 8))
def cg_f096_holder_concentration_core129_ewm_8q_v130_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_ewm(_safe_div(shrholders, percentoftotal + 1e-9), 8))
# core130-139: stability_12q
def cg_f096_holder_concentration_core130_stability_12q_v131_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(_std(value, 12), _mean(value, 12)))
def cg_f096_holder_concentration_core131_stability_12q_v132_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(_std(shrholders, 12), _mean(shrholders, 12)))
def cg_f096_holder_concentration_core132_stability_12q_v133_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(_std(totalvalue, 12), _mean(totalvalue, 12)))
def cg_f096_holder_concentration_core133_stability_12q_v134_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(_std(percentoftotal, 12), _mean(percentoftotal, 12)))
def cg_f096_holder_concentration_core134_stability_12q_v135_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(_std(_safe_div(value, totalvalue), 12), _mean(_safe_div(value, totalvalue), 12)))
def cg_f096_holder_concentration_core135_stability_12q_v136_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(_std(_safe_div(value, shrholders), 12), _mean(_safe_div(value, shrholders), 12)))
def cg_f096_holder_concentration_core136_stability_12q_v137_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(_std(_safe_div(totalvalue, shrholders), 12), _mean(_safe_div(totalvalue, shrholders), 12)))
def cg_f096_holder_concentration_core137_stability_12q_v138_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(_std(_safe_div(value, percentoftotal + 1e-9), 12), _mean(_safe_div(value, percentoftotal + 1e-9), 12)))
def cg_f096_holder_concentration_core138_stability_12q_v139_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(_std(_safe_div(totalvalue, percentoftotal + 1e-9), 12), _mean(_safe_div(totalvalue, percentoftotal + 1e-9), 12)))
def cg_f096_holder_concentration_core139_stability_12q_v140_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(_std(_safe_div(shrholders, percentoftotal + 1e-9), 12), _mean(_safe_div(shrholders, percentoftotal + 1e-9), 12)))
# core140-149: level
def cg_f096_holder_concentration_core140_level_v141_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(value)
def cg_f096_holder_concentration_core141_level_v142_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(shrholders)
def cg_f096_holder_concentration_core142_level_v143_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(totalvalue)
def cg_f096_holder_concentration_core143_level_v144_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(percentoftotal)
def cg_f096_holder_concentration_core144_level_v145_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(value, totalvalue))
def cg_f096_holder_concentration_core145_level_v146_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(value, shrholders))
def cg_f096_holder_concentration_core146_level_v147_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(totalvalue, shrholders))
def cg_f096_holder_concentration_core147_level_v148_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(value, percentoftotal + 1e-9))
def cg_f096_holder_concentration_core148_level_v149_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(totalvalue, percentoftotal + 1e-9))
def cg_f096_holder_concentration_core149_level_v150_signal(investorname, value, units, calendardate, shrholders, totalvalue, percentoftotal):
    return _clean(_safe_div(shrholders, percentoftotal + 1e-9))
