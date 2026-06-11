import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f098_corporate_action_events_core75_pct_4q_v076_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_pct_change(value, 1), 4))
def cg_f098_corporate_action_events_core76_pct_4q_v077_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_pct_change(value, 4), 4))
def cg_f098_corporate_action_events_core77_pct_4q_v078_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_diff(value, 1), 4))
def cg_f098_corporate_action_events_core78_pct_4q_v079_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_ewm(value, 8), 4))
def cg_f098_corporate_action_events_core79_pct_4q_v080_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(_event_count(value, 12), 4))
# core80-89: std_8q
def cg_f098_corporate_action_events_core80_std_8q_v081_signal(date, action, value, name, contraticker, contraname):
    return _clean(_std(value, 8))
def cg_f098_corporate_action_events_core81_std_8q_v082_signal(date, action, value, name, contraticker, contraname):
    return _clean(_std(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 8))
def cg_f098_corporate_action_events_core82_std_8q_v083_signal(date, action, value, name, contraticker, contraname):
    return _clean(_std(_safe_div(value, _mean(value, 20)), 8))
def cg_f098_corporate_action_events_core83_std_8q_v084_signal(date, action, value, name, contraticker, contraname):
    return _clean(_std(_z(value, 20), 8))
def cg_f098_corporate_action_events_core84_std_8q_v085_signal(date, action, value, name, contraticker, contraname):
    return _clean(_std(_rank(value, 20), 8))
def cg_f098_corporate_action_events_core85_std_8q_v086_signal(date, action, value, name, contraticker, contraname):
    return _clean(_std(_pct_change(value, 1), 8))
def cg_f098_corporate_action_events_core86_std_8q_v087_signal(date, action, value, name, contraticker, contraname):
    return _clean(_std(_pct_change(value, 4), 8))
def cg_f098_corporate_action_events_core87_std_8q_v088_signal(date, action, value, name, contraticker, contraname):
    return _clean(_std(_diff(value, 1), 8))
def cg_f098_corporate_action_events_core88_std_8q_v089_signal(date, action, value, name, contraticker, contraname):
    return _clean(_std(_ewm(value, 8), 8))
def cg_f098_corporate_action_events_core89_std_8q_v090_signal(date, action, value, name, contraticker, contraname):
    return _clean(_std(_event_count(value, 12), 8))
# core90-99: log
def cg_f098_corporate_action_events_core90_log_v091_signal(date, action, value, name, contraticker, contraname):
    return _clean(_log(value.clip(lower=0.001) if hasattr(value, 'clip') else value))
def cg_f098_corporate_action_events_core91_log_v092_signal(date, action, value, name, contraticker, contraname):
    return _clean(_log(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value).clip(lower=0.001) if hasattr(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 'clip') else _log(value.clip(lower=1.0) if hasattr(value, 'clip') else value)))
def cg_f098_corporate_action_events_core92_log_v093_signal(date, action, value, name, contraticker, contraname):
    return _clean(_log(_safe_div(value, _mean(value, 20)).clip(lower=0.001) if hasattr(_safe_div(value, _mean(value, 20)), 'clip') else _safe_div(value, _mean(value, 20))))
def cg_f098_corporate_action_events_core93_log_v094_signal(date, action, value, name, contraticker, contraname):
    return _clean(_log(_z(value, 20).clip(lower=0.001) if hasattr(_z(value, 20), 'clip') else _z(value, 20)))
def cg_f098_corporate_action_events_core94_log_v095_signal(date, action, value, name, contraticker, contraname):
    return _clean(_log(_rank(value, 20).clip(lower=0.001) if hasattr(_rank(value, 20), 'clip') else _rank(value, 20)))
def cg_f098_corporate_action_events_core95_log_v096_signal(date, action, value, name, contraticker, contraname):
    return _clean(_log(_pct_change(value, 1).clip(lower=0.001) if hasattr(_pct_change(value, 1), 'clip') else _pct_change(value, 1)))
def cg_f098_corporate_action_events_core96_log_v097_signal(date, action, value, name, contraticker, contraname):
    return _clean(_log(_pct_change(value, 4).clip(lower=0.001) if hasattr(_pct_change(value, 4), 'clip') else _pct_change(value, 4)))
def cg_f098_corporate_action_events_core97_log_v098_signal(date, action, value, name, contraticker, contraname):
    return _clean(_log(_diff(value, 1).clip(lower=0.001) if hasattr(_diff(value, 1), 'clip') else _diff(value, 1)))
def cg_f098_corporate_action_events_core98_log_v099_signal(date, action, value, name, contraticker, contraname):
    return _clean(_log(_ewm(value, 8).clip(lower=0.001) if hasattr(_ewm(value, 8), 'clip') else _ewm(value, 8)))
def cg_f098_corporate_action_events_core99_log_v100_signal(date, action, value, name, contraticker, contraname):
    return _clean(_log(_event_count(value, 12).clip(lower=0.001) if hasattr(_event_count(value, 12), 'clip') else _event_count(value, 12)))
# core100-109: diff_1q
def cg_f098_corporate_action_events_core100_diff_1q_v101_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(value, 1))
def cg_f098_corporate_action_events_core101_diff_1q_v102_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 1))
def cg_f098_corporate_action_events_core102_diff_1q_v103_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_safe_div(value, _mean(value, 20)), 1))
def cg_f098_corporate_action_events_core103_diff_1q_v104_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_z(value, 20), 1))
def cg_f098_corporate_action_events_core104_diff_1q_v105_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_rank(value, 20), 1))
def cg_f098_corporate_action_events_core105_diff_1q_v106_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_pct_change(value, 1), 1))
def cg_f098_corporate_action_events_core106_diff_1q_v107_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_pct_change(value, 4), 1))
def cg_f098_corporate_action_events_core107_diff_1q_v108_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_diff(value, 1), 1))
def cg_f098_corporate_action_events_core108_diff_1q_v109_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_ewm(value, 8), 1))
def cg_f098_corporate_action_events_core109_diff_1q_v110_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(_event_count(value, 12), 1))
# core110-119: slope_4q
def cg_f098_corporate_action_events_core110_slope_4q_v111_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(value, 4))
def cg_f098_corporate_action_events_core111_slope_4q_v112_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 4))
def cg_f098_corporate_action_events_core112_slope_4q_v113_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_safe_div(value, _mean(value, 20)), 4))
def cg_f098_corporate_action_events_core113_slope_4q_v114_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_z(value, 20), 4))
def cg_f098_corporate_action_events_core114_slope_4q_v115_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_rank(value, 20), 4))
def cg_f098_corporate_action_events_core115_slope_4q_v116_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_pct_change(value, 1), 4))
def cg_f098_corporate_action_events_core116_slope_4q_v117_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_pct_change(value, 4), 4))
def cg_f098_corporate_action_events_core117_slope_4q_v118_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_diff(value, 1), 4))
def cg_f098_corporate_action_events_core118_slope_4q_v119_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_ewm(value, 8), 4))
def cg_f098_corporate_action_events_core119_slope_4q_v120_signal(date, action, value, name, contraticker, contraname):
    return _clean(_slope(_event_count(value, 12), 4))
# core120-129: ewm_8q
def cg_f098_corporate_action_events_core120_ewm_8q_v121_signal(date, action, value, name, contraticker, contraname):
    return _clean(_ewm(value, 8))
def cg_f098_corporate_action_events_core121_ewm_8q_v122_signal(date, action, value, name, contraticker, contraname):
    return _clean(_ewm(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 8))
def cg_f098_corporate_action_events_core122_ewm_8q_v123_signal(date, action, value, name, contraticker, contraname):
    return _clean(_ewm(_safe_div(value, _mean(value, 20)), 8))
def cg_f098_corporate_action_events_core123_ewm_8q_v124_signal(date, action, value, name, contraticker, contraname):
    return _clean(_ewm(_z(value, 20), 8))
def cg_f098_corporate_action_events_core124_ewm_8q_v125_signal(date, action, value, name, contraticker, contraname):
    return _clean(_ewm(_rank(value, 20), 8))
def cg_f098_corporate_action_events_core125_ewm_8q_v126_signal(date, action, value, name, contraticker, contraname):
    return _clean(_ewm(_pct_change(value, 1), 8))
def cg_f098_corporate_action_events_core126_ewm_8q_v127_signal(date, action, value, name, contraticker, contraname):
    return _clean(_ewm(_pct_change(value, 4), 8))
def cg_f098_corporate_action_events_core127_ewm_8q_v128_signal(date, action, value, name, contraticker, contraname):
    return _clean(_ewm(_diff(value, 1), 8))
def cg_f098_corporate_action_events_core128_ewm_8q_v129_signal(date, action, value, name, contraticker, contraname):
    return _clean(_ewm(_ewm(value, 8), 8))
def cg_f098_corporate_action_events_core129_ewm_8q_v130_signal(date, action, value, name, contraticker, contraname):
    return _clean(_ewm(_event_count(value, 12), 8))
# core130-139: stability_12q
def cg_f098_corporate_action_events_core130_stability_12q_v131_signal(date, action, value, name, contraticker, contraname):
    return _clean(_safe_div(_std(value, 12), _mean(value, 12)))
def cg_f098_corporate_action_events_core131_stability_12q_v132_signal(date, action, value, name, contraticker, contraname):
    return _clean(_safe_div(_std(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 12), _mean(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 12)))
def cg_f098_corporate_action_events_core132_stability_12q_v133_signal(date, action, value, name, contraticker, contraname):
    return _clean(_safe_div(_std(_safe_div(value, _mean(value, 20)), 12), _mean(_safe_div(value, _mean(value, 20)), 12)))
def cg_f098_corporate_action_events_core133_stability_12q_v134_signal(date, action, value, name, contraticker, contraname):
    return _clean(_safe_div(_std(_z(value, 20), 12), _mean(_z(value, 20), 12)))
def cg_f098_corporate_action_events_core134_stability_12q_v135_signal(date, action, value, name, contraticker, contraname):
    return _clean(_safe_div(_std(_rank(value, 20), 12), _mean(_rank(value, 20), 12)))
def cg_f098_corporate_action_events_core135_stability_12q_v136_signal(date, action, value, name, contraticker, contraname):
    return _clean(_safe_div(_std(_pct_change(value, 1), 12), _mean(_pct_change(value, 1), 12)))
def cg_f098_corporate_action_events_core136_stability_12q_v137_signal(date, action, value, name, contraticker, contraname):
    return _clean(_safe_div(_std(_pct_change(value, 4), 12), _mean(_pct_change(value, 4), 12)))
def cg_f098_corporate_action_events_core137_stability_12q_v138_signal(date, action, value, name, contraticker, contraname):
    return _clean(_safe_div(_std(_diff(value, 1), 12), _mean(_diff(value, 1), 12)))
def cg_f098_corporate_action_events_core138_stability_12q_v139_signal(date, action, value, name, contraticker, contraname):
    return _clean(_safe_div(_std(_ewm(value, 8), 12), _mean(_ewm(value, 8), 12)))
def cg_f098_corporate_action_events_core139_stability_12q_v140_signal(date, action, value, name, contraticker, contraname):
    return _clean(_safe_div(_std(_event_count(value, 12), 12), _mean(_event_count(value, 12), 12)))
# core140-149: level
def cg_f098_corporate_action_events_core140_level_v141_signal(date, action, value, name, contraticker, contraname):
    return _clean(value)
def cg_f098_corporate_action_events_core141_level_v142_signal(date, action, value, name, contraticker, contraname):
    return _clean(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value))
def cg_f098_corporate_action_events_core142_level_v143_signal(date, action, value, name, contraticker, contraname):
    return _clean(_safe_div(value, _mean(value, 20)))
def cg_f098_corporate_action_events_core143_level_v144_signal(date, action, value, name, contraticker, contraname):
    return _clean(_z(value, 20))
def cg_f098_corporate_action_events_core144_level_v145_signal(date, action, value, name, contraticker, contraname):
    return _clean(_rank(value, 20))
def cg_f098_corporate_action_events_core145_level_v146_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(value, 1))
def cg_f098_corporate_action_events_core146_level_v147_signal(date, action, value, name, contraticker, contraname):
    return _clean(_pct_change(value, 4))
def cg_f098_corporate_action_events_core147_level_v148_signal(date, action, value, name, contraticker, contraname):
    return _clean(_diff(value, 1))
def cg_f098_corporate_action_events_core148_level_v149_signal(date, action, value, name, contraticker, contraname):
    return _clean(_ewm(value, 8))
def cg_f098_corporate_action_events_core149_level_v150_signal(date, action, value, name, contraticker, contraname):
    return _clean(_event_count(value, 12))
