import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f099_sec_8k_event_density_core75_pct_4q_v076_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_event_rate(eventcodes, 20), 4))
def cg_f099_sec_8k_event_density_core76_pct_4q_v077_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_z(_event_count(eventcodes, 12), 20), 4))
def cg_f099_sec_8k_event_density_core77_pct_4q_v078_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_rank(_event_count(eventcodes, 12), 20), 4))
def cg_f099_sec_8k_event_density_core78_pct_4q_v079_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_diff(_event_count(eventcodes, 4), 1), 4))
def cg_f099_sec_8k_event_density_core79_pct_4q_v080_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_pct_change(_event_count(eventcodes, 12) + 1, 4), 4))
# core80-89: std_8q
def cg_f099_sec_8k_event_density_core80_std_8q_v081_signal(ticker, date, eventcodes):
    return _clean(_std(_event_count(eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core81_std_8q_v082_signal(ticker, date, eventcodes):
    return _clean(_std(_event_count(eventcodes, 12), 8))
def cg_f099_sec_8k_event_density_core82_std_8q_v083_signal(ticker, date, eventcodes):
    return _clean(_std(_event_count(eventcodes, 20), 8))
def cg_f099_sec_8k_event_density_core83_std_8q_v084_signal(ticker, date, eventcodes):
    return _clean(_std(_event_rate(eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core84_std_8q_v085_signal(ticker, date, eventcodes):
    return _clean(_std(_event_rate(eventcodes, 12), 8))
def cg_f099_sec_8k_event_density_core85_std_8q_v086_signal(ticker, date, eventcodes):
    return _clean(_std(_event_rate(eventcodes, 20), 8))
def cg_f099_sec_8k_event_density_core86_std_8q_v087_signal(ticker, date, eventcodes):
    return _clean(_std(_z(_event_count(eventcodes, 12), 20), 8))
def cg_f099_sec_8k_event_density_core87_std_8q_v088_signal(ticker, date, eventcodes):
    return _clean(_std(_rank(_event_count(eventcodes, 12), 20), 8))
def cg_f099_sec_8k_event_density_core88_std_8q_v089_signal(ticker, date, eventcodes):
    return _clean(_std(_diff(_event_count(eventcodes, 4), 1), 8))
def cg_f099_sec_8k_event_density_core89_std_8q_v090_signal(ticker, date, eventcodes):
    return _clean(_std(_pct_change(_event_count(eventcodes, 12) + 1, 4), 8))
# core90-99: log
def cg_f099_sec_8k_event_density_core90_log_v091_signal(ticker, date, eventcodes):
    return _clean(_log(_event_count(eventcodes, 4).clip(lower=0.001) if hasattr(_event_count(eventcodes, 4), 'clip') else _event_count(eventcodes, 4)))
def cg_f099_sec_8k_event_density_core91_log_v092_signal(ticker, date, eventcodes):
    return _clean(_log(_event_count(eventcodes, 12).clip(lower=0.001) if hasattr(_event_count(eventcodes, 12), 'clip') else _event_count(eventcodes, 12)))
def cg_f099_sec_8k_event_density_core92_log_v093_signal(ticker, date, eventcodes):
    return _clean(_log(_event_count(eventcodes, 20).clip(lower=0.001) if hasattr(_event_count(eventcodes, 20), 'clip') else _event_count(eventcodes, 20)))
def cg_f099_sec_8k_event_density_core93_log_v094_signal(ticker, date, eventcodes):
    return _clean(_log(_event_rate(eventcodes, 4).clip(lower=0.001) if hasattr(_event_rate(eventcodes, 4), 'clip') else _event_rate(eventcodes, 4)))
def cg_f099_sec_8k_event_density_core94_log_v095_signal(ticker, date, eventcodes):
    return _clean(_log(_event_rate(eventcodes, 12).clip(lower=0.001) if hasattr(_event_rate(eventcodes, 12), 'clip') else _event_rate(eventcodes, 12)))
def cg_f099_sec_8k_event_density_core95_log_v096_signal(ticker, date, eventcodes):
    return _clean(_log(_event_rate(eventcodes, 20).clip(lower=0.001) if hasattr(_event_rate(eventcodes, 20), 'clip') else _event_rate(eventcodes, 20)))
def cg_f099_sec_8k_event_density_core96_log_v097_signal(ticker, date, eventcodes):
    return _clean(_log(_z(_event_count(eventcodes, 12), 20).clip(lower=0.001) if hasattr(_z(_event_count(eventcodes, 12), 20), 'clip') else _z(_event_count(eventcodes, 12), 20)))
def cg_f099_sec_8k_event_density_core97_log_v098_signal(ticker, date, eventcodes):
    return _clean(_log(_rank(_event_count(eventcodes, 12), 20).clip(lower=0.001) if hasattr(_rank(_event_count(eventcodes, 12), 20), 'clip') else _rank(_event_count(eventcodes, 12), 20)))
def cg_f099_sec_8k_event_density_core98_log_v099_signal(ticker, date, eventcodes):
    return _clean(_log(_diff(_event_count(eventcodes, 4), 1).clip(lower=0.001) if hasattr(_diff(_event_count(eventcodes, 4), 1), 'clip') else _diff(_event_count(eventcodes, 4), 1)))
def cg_f099_sec_8k_event_density_core99_log_v100_signal(ticker, date, eventcodes):
    return _clean(_log(_pct_change(_event_count(eventcodes, 12) + 1, 4).clip(lower=0.001) if hasattr(_pct_change(_event_count(eventcodes, 12) + 1, 4), 'clip') else _pct_change(_event_count(eventcodes, 12) + 1, 4)))
# core100-109: diff_1q
def cg_f099_sec_8k_event_density_core100_diff_1q_v101_signal(ticker, date, eventcodes):
    return _clean(_diff(_event_count(eventcodes, 4), 1))
def cg_f099_sec_8k_event_density_core101_diff_1q_v102_signal(ticker, date, eventcodes):
    return _clean(_diff(_event_count(eventcodes, 12), 1))
def cg_f099_sec_8k_event_density_core102_diff_1q_v103_signal(ticker, date, eventcodes):
    return _clean(_diff(_event_count(eventcodes, 20), 1))
def cg_f099_sec_8k_event_density_core103_diff_1q_v104_signal(ticker, date, eventcodes):
    return _clean(_diff(_event_rate(eventcodes, 4), 1))
def cg_f099_sec_8k_event_density_core104_diff_1q_v105_signal(ticker, date, eventcodes):
    return _clean(_diff(_event_rate(eventcodes, 12), 1))
def cg_f099_sec_8k_event_density_core105_diff_1q_v106_signal(ticker, date, eventcodes):
    return _clean(_diff(_event_rate(eventcodes, 20), 1))
def cg_f099_sec_8k_event_density_core106_diff_1q_v107_signal(ticker, date, eventcodes):
    return _clean(_diff(_z(_event_count(eventcodes, 12), 20), 1))
def cg_f099_sec_8k_event_density_core107_diff_1q_v108_signal(ticker, date, eventcodes):
    return _clean(_diff(_rank(_event_count(eventcodes, 12), 20), 1))
def cg_f099_sec_8k_event_density_core108_diff_1q_v109_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_event_count(eventcodes, 4), 1), 1))
def cg_f099_sec_8k_event_density_core109_diff_1q_v110_signal(ticker, date, eventcodes):
    return _clean(_diff(_pct_change(_event_count(eventcodes, 12) + 1, 4), 1))
# core110-119: slope_4q
def cg_f099_sec_8k_event_density_core110_slope_4q_v111_signal(ticker, date, eventcodes):
    return _clean(_slope(_event_count(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core111_slope_4q_v112_signal(ticker, date, eventcodes):
    return _clean(_slope(_event_count(eventcodes, 12), 4))
def cg_f099_sec_8k_event_density_core112_slope_4q_v113_signal(ticker, date, eventcodes):
    return _clean(_slope(_event_count(eventcodes, 20), 4))
def cg_f099_sec_8k_event_density_core113_slope_4q_v114_signal(ticker, date, eventcodes):
    return _clean(_slope(_event_rate(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core114_slope_4q_v115_signal(ticker, date, eventcodes):
    return _clean(_slope(_event_rate(eventcodes, 12), 4))
def cg_f099_sec_8k_event_density_core115_slope_4q_v116_signal(ticker, date, eventcodes):
    return _clean(_slope(_event_rate(eventcodes, 20), 4))
def cg_f099_sec_8k_event_density_core116_slope_4q_v117_signal(ticker, date, eventcodes):
    return _clean(_slope(_z(_event_count(eventcodes, 12), 20), 4))
def cg_f099_sec_8k_event_density_core117_slope_4q_v118_signal(ticker, date, eventcodes):
    return _clean(_slope(_rank(_event_count(eventcodes, 12), 20), 4))
def cg_f099_sec_8k_event_density_core118_slope_4q_v119_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_event_count(eventcodes, 4), 1), 4))
def cg_f099_sec_8k_event_density_core119_slope_4q_v120_signal(ticker, date, eventcodes):
    return _clean(_slope(_pct_change(_event_count(eventcodes, 12) + 1, 4), 4))
# core120-129: ewm_8q
def cg_f099_sec_8k_event_density_core120_ewm_8q_v121_signal(ticker, date, eventcodes):
    return _clean(_ewm(_event_count(eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core121_ewm_8q_v122_signal(ticker, date, eventcodes):
    return _clean(_ewm(_event_count(eventcodes, 12), 8))
def cg_f099_sec_8k_event_density_core122_ewm_8q_v123_signal(ticker, date, eventcodes):
    return _clean(_ewm(_event_count(eventcodes, 20), 8))
def cg_f099_sec_8k_event_density_core123_ewm_8q_v124_signal(ticker, date, eventcodes):
    return _clean(_ewm(_event_rate(eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core124_ewm_8q_v125_signal(ticker, date, eventcodes):
    return _clean(_ewm(_event_rate(eventcodes, 12), 8))
def cg_f099_sec_8k_event_density_core125_ewm_8q_v126_signal(ticker, date, eventcodes):
    return _clean(_ewm(_event_rate(eventcodes, 20), 8))
def cg_f099_sec_8k_event_density_core126_ewm_8q_v127_signal(ticker, date, eventcodes):
    return _clean(_ewm(_z(_event_count(eventcodes, 12), 20), 8))
def cg_f099_sec_8k_event_density_core127_ewm_8q_v128_signal(ticker, date, eventcodes):
    return _clean(_ewm(_rank(_event_count(eventcodes, 12), 20), 8))
def cg_f099_sec_8k_event_density_core128_ewm_8q_v129_signal(ticker, date, eventcodes):
    return _clean(_ewm(_diff(_event_count(eventcodes, 4), 1), 8))
def cg_f099_sec_8k_event_density_core129_ewm_8q_v130_signal(ticker, date, eventcodes):
    return _clean(_ewm(_pct_change(_event_count(eventcodes, 12) + 1, 4), 8))
# core130-139: stability_12q
def cg_f099_sec_8k_event_density_core130_stability_12q_v131_signal(ticker, date, eventcodes):
    return _clean(_safe_div(_std(_event_count(eventcodes, 4), 12), _mean(_event_count(eventcodes, 4), 12)))
def cg_f099_sec_8k_event_density_core131_stability_12q_v132_signal(ticker, date, eventcodes):
    return _clean(_safe_div(_std(_event_count(eventcodes, 12), 12), _mean(_event_count(eventcodes, 12), 12)))
def cg_f099_sec_8k_event_density_core132_stability_12q_v133_signal(ticker, date, eventcodes):
    return _clean(_safe_div(_std(_event_count(eventcodes, 20), 12), _mean(_event_count(eventcodes, 20), 12)))
def cg_f099_sec_8k_event_density_core133_stability_12q_v134_signal(ticker, date, eventcodes):
    return _clean(_safe_div(_std(_event_rate(eventcodes, 4), 12), _mean(_event_rate(eventcodes, 4), 12)))
def cg_f099_sec_8k_event_density_core134_stability_12q_v135_signal(ticker, date, eventcodes):
    return _clean(_safe_div(_std(_event_rate(eventcodes, 12), 12), _mean(_event_rate(eventcodes, 12), 12)))
def cg_f099_sec_8k_event_density_core135_stability_12q_v136_signal(ticker, date, eventcodes):
    return _clean(_safe_div(_std(_event_rate(eventcodes, 20), 12), _mean(_event_rate(eventcodes, 20), 12)))
def cg_f099_sec_8k_event_density_core136_stability_12q_v137_signal(ticker, date, eventcodes):
    return _clean(_safe_div(_std(_z(_event_count(eventcodes, 12), 20), 12), _mean(_z(_event_count(eventcodes, 12), 20), 12)))
def cg_f099_sec_8k_event_density_core137_stability_12q_v138_signal(ticker, date, eventcodes):
    return _clean(_safe_div(_std(_rank(_event_count(eventcodes, 12), 20), 12), _mean(_rank(_event_count(eventcodes, 12), 20), 12)))
def cg_f099_sec_8k_event_density_core138_stability_12q_v139_signal(ticker, date, eventcodes):
    return _clean(_safe_div(_std(_diff(_event_count(eventcodes, 4), 1), 12), _mean(_diff(_event_count(eventcodes, 4), 1), 12)))
def cg_f099_sec_8k_event_density_core139_stability_12q_v140_signal(ticker, date, eventcodes):
    return _clean(_safe_div(_std(_pct_change(_event_count(eventcodes, 12) + 1, 4), 12), _mean(_pct_change(_event_count(eventcodes, 12) + 1, 4), 12)))
# core140-149: level
def cg_f099_sec_8k_event_density_core140_level_v141_signal(ticker, date, eventcodes):
    return _clean(_event_count(eventcodes, 4))
def cg_f099_sec_8k_event_density_core141_level_v142_signal(ticker, date, eventcodes):
    return _clean(_event_count(eventcodes, 12))
def cg_f099_sec_8k_event_density_core142_level_v143_signal(ticker, date, eventcodes):
    return _clean(_event_count(eventcodes, 20))
def cg_f099_sec_8k_event_density_core143_level_v144_signal(ticker, date, eventcodes):
    return _clean(_event_rate(eventcodes, 4))
def cg_f099_sec_8k_event_density_core144_level_v145_signal(ticker, date, eventcodes):
    return _clean(_event_rate(eventcodes, 12))
def cg_f099_sec_8k_event_density_core145_level_v146_signal(ticker, date, eventcodes):
    return _clean(_event_rate(eventcodes, 20))
def cg_f099_sec_8k_event_density_core146_level_v147_signal(ticker, date, eventcodes):
    return _clean(_z(_event_count(eventcodes, 12), 20))
def cg_f099_sec_8k_event_density_core147_level_v148_signal(ticker, date, eventcodes):
    return _clean(_rank(_event_count(eventcodes, 12), 20))
def cg_f099_sec_8k_event_density_core148_level_v149_signal(ticker, date, eventcodes):
    return _clean(_diff(_event_count(eventcodes, 4), 1))
def cg_f099_sec_8k_event_density_core149_level_v150_signal(ticker, date, eventcodes):
    return _clean(_pct_change(_event_count(eventcodes, 12) + 1, 4))
