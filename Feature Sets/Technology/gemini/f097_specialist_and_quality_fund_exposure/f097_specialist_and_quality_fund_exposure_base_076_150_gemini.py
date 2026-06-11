import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f097_specialist_and_quality_fund_exposure_core75_pct_4q_v076_signal(investorname, value, units, securitytype):
    return _clean(_pct_change(_pct_change(value, 1), 4))
def cg_f097_specialist_and_quality_fund_exposure_core76_pct_4q_v077_signal(investorname, value, units, securitytype):
    return _clean(_pct_change(_pct_change(value, 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core77_pct_4q_v078_signal(investorname, value, units, securitytype):
    return _clean(_pct_change(_diff(value, 1), 4))
def cg_f097_specialist_and_quality_fund_exposure_core78_pct_4q_v079_signal(investorname, value, units, securitytype):
    return _clean(_pct_change(_ewm(value, 8), 4))
def cg_f097_specialist_and_quality_fund_exposure_core79_pct_4q_v080_signal(investorname, value, units, securitytype):
    return _clean(_pct_change(_safe_div(value, _std(value, 12) + 1.0), 4))
# core80-89: std_8q
def cg_f097_specialist_and_quality_fund_exposure_core80_std_8q_v081_signal(investorname, value, units, securitytype):
    return _clean(_std(value, 8))
def cg_f097_specialist_and_quality_fund_exposure_core81_std_8q_v082_signal(investorname, value, units, securitytype):
    return _clean(_std(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 8))
def cg_f097_specialist_and_quality_fund_exposure_core82_std_8q_v083_signal(investorname, value, units, securitytype):
    return _clean(_std(_safe_div(value, _mean(value, 20)), 8))
def cg_f097_specialist_and_quality_fund_exposure_core83_std_8q_v084_signal(investorname, value, units, securitytype):
    return _clean(_std(_z(value, 20), 8))
def cg_f097_specialist_and_quality_fund_exposure_core84_std_8q_v085_signal(investorname, value, units, securitytype):
    return _clean(_std(_rank(value, 20), 8))
def cg_f097_specialist_and_quality_fund_exposure_core85_std_8q_v086_signal(investorname, value, units, securitytype):
    return _clean(_std(_pct_change(value, 1), 8))
def cg_f097_specialist_and_quality_fund_exposure_core86_std_8q_v087_signal(investorname, value, units, securitytype):
    return _clean(_std(_pct_change(value, 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core87_std_8q_v088_signal(investorname, value, units, securitytype):
    return _clean(_std(_diff(value, 1), 8))
def cg_f097_specialist_and_quality_fund_exposure_core88_std_8q_v089_signal(investorname, value, units, securitytype):
    return _clean(_std(_ewm(value, 8), 8))
def cg_f097_specialist_and_quality_fund_exposure_core89_std_8q_v090_signal(investorname, value, units, securitytype):
    return _clean(_std(_safe_div(value, _std(value, 12) + 1.0), 8))
# core90-99: log
def cg_f097_specialist_and_quality_fund_exposure_core90_log_v091_signal(investorname, value, units, securitytype):
    return _clean(_log(value.clip(lower=0.001) if hasattr(value, 'clip') else value))
def cg_f097_specialist_and_quality_fund_exposure_core91_log_v092_signal(investorname, value, units, securitytype):
    return _clean(_log(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value).clip(lower=0.001) if hasattr(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 'clip') else _log(value.clip(lower=1.0) if hasattr(value, 'clip') else value)))
def cg_f097_specialist_and_quality_fund_exposure_core92_log_v093_signal(investorname, value, units, securitytype):
    return _clean(_log(_safe_div(value, _mean(value, 20)).clip(lower=0.001) if hasattr(_safe_div(value, _mean(value, 20)), 'clip') else _safe_div(value, _mean(value, 20))))
def cg_f097_specialist_and_quality_fund_exposure_core93_log_v094_signal(investorname, value, units, securitytype):
    return _clean(_log(_z(value, 20).clip(lower=0.001) if hasattr(_z(value, 20), 'clip') else _z(value, 20)))
def cg_f097_specialist_and_quality_fund_exposure_core94_log_v095_signal(investorname, value, units, securitytype):
    return _clean(_log(_rank(value, 20).clip(lower=0.001) if hasattr(_rank(value, 20), 'clip') else _rank(value, 20)))
def cg_f097_specialist_and_quality_fund_exposure_core95_log_v096_signal(investorname, value, units, securitytype):
    return _clean(_log(_pct_change(value, 1).clip(lower=0.001) if hasattr(_pct_change(value, 1), 'clip') else _pct_change(value, 1)))
def cg_f097_specialist_and_quality_fund_exposure_core96_log_v097_signal(investorname, value, units, securitytype):
    return _clean(_log(_pct_change(value, 4).clip(lower=0.001) if hasattr(_pct_change(value, 4), 'clip') else _pct_change(value, 4)))
def cg_f097_specialist_and_quality_fund_exposure_core97_log_v098_signal(investorname, value, units, securitytype):
    return _clean(_log(_diff(value, 1).clip(lower=0.001) if hasattr(_diff(value, 1), 'clip') else _diff(value, 1)))
def cg_f097_specialist_and_quality_fund_exposure_core98_log_v099_signal(investorname, value, units, securitytype):
    return _clean(_log(_ewm(value, 8).clip(lower=0.001) if hasattr(_ewm(value, 8), 'clip') else _ewm(value, 8)))
def cg_f097_specialist_and_quality_fund_exposure_core99_log_v100_signal(investorname, value, units, securitytype):
    return _clean(_log(_safe_div(value, _std(value, 12) + 1.0).clip(lower=0.001) if hasattr(_safe_div(value, _std(value, 12) + 1.0), 'clip') else _safe_div(value, _std(value, 12) + 1.0)))
# core100-109: diff_1q
def cg_f097_specialist_and_quality_fund_exposure_core100_diff_1q_v101_signal(investorname, value, units, securitytype):
    return _clean(_diff(value, 1))
def cg_f097_specialist_and_quality_fund_exposure_core101_diff_1q_v102_signal(investorname, value, units, securitytype):
    return _clean(_diff(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 1))
def cg_f097_specialist_and_quality_fund_exposure_core102_diff_1q_v103_signal(investorname, value, units, securitytype):
    return _clean(_diff(_safe_div(value, _mean(value, 20)), 1))
def cg_f097_specialist_and_quality_fund_exposure_core103_diff_1q_v104_signal(investorname, value, units, securitytype):
    return _clean(_diff(_z(value, 20), 1))
def cg_f097_specialist_and_quality_fund_exposure_core104_diff_1q_v105_signal(investorname, value, units, securitytype):
    return _clean(_diff(_rank(value, 20), 1))
def cg_f097_specialist_and_quality_fund_exposure_core105_diff_1q_v106_signal(investorname, value, units, securitytype):
    return _clean(_diff(_pct_change(value, 1), 1))
def cg_f097_specialist_and_quality_fund_exposure_core106_diff_1q_v107_signal(investorname, value, units, securitytype):
    return _clean(_diff(_pct_change(value, 4), 1))
def cg_f097_specialist_and_quality_fund_exposure_core107_diff_1q_v108_signal(investorname, value, units, securitytype):
    return _clean(_diff(_diff(value, 1), 1))
def cg_f097_specialist_and_quality_fund_exposure_core108_diff_1q_v109_signal(investorname, value, units, securitytype):
    return _clean(_diff(_ewm(value, 8), 1))
def cg_f097_specialist_and_quality_fund_exposure_core109_diff_1q_v110_signal(investorname, value, units, securitytype):
    return _clean(_diff(_safe_div(value, _std(value, 12) + 1.0), 1))
# core110-119: slope_4q
def cg_f097_specialist_and_quality_fund_exposure_core110_slope_4q_v111_signal(investorname, value, units, securitytype):
    return _clean(_slope(value, 4))
def cg_f097_specialist_and_quality_fund_exposure_core111_slope_4q_v112_signal(investorname, value, units, securitytype):
    return _clean(_slope(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 4))
def cg_f097_specialist_and_quality_fund_exposure_core112_slope_4q_v113_signal(investorname, value, units, securitytype):
    return _clean(_slope(_safe_div(value, _mean(value, 20)), 4))
def cg_f097_specialist_and_quality_fund_exposure_core113_slope_4q_v114_signal(investorname, value, units, securitytype):
    return _clean(_slope(_z(value, 20), 4))
def cg_f097_specialist_and_quality_fund_exposure_core114_slope_4q_v115_signal(investorname, value, units, securitytype):
    return _clean(_slope(_rank(value, 20), 4))
def cg_f097_specialist_and_quality_fund_exposure_core115_slope_4q_v116_signal(investorname, value, units, securitytype):
    return _clean(_slope(_pct_change(value, 1), 4))
def cg_f097_specialist_and_quality_fund_exposure_core116_slope_4q_v117_signal(investorname, value, units, securitytype):
    return _clean(_slope(_pct_change(value, 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core117_slope_4q_v118_signal(investorname, value, units, securitytype):
    return _clean(_slope(_diff(value, 1), 4))
def cg_f097_specialist_and_quality_fund_exposure_core118_slope_4q_v119_signal(investorname, value, units, securitytype):
    return _clean(_slope(_ewm(value, 8), 4))
def cg_f097_specialist_and_quality_fund_exposure_core119_slope_4q_v120_signal(investorname, value, units, securitytype):
    return _clean(_slope(_safe_div(value, _std(value, 12) + 1.0), 4))
# core120-129: ewm_8q
def cg_f097_specialist_and_quality_fund_exposure_core120_ewm_8q_v121_signal(investorname, value, units, securitytype):
    return _clean(_ewm(value, 8))
def cg_f097_specialist_and_quality_fund_exposure_core121_ewm_8q_v122_signal(investorname, value, units, securitytype):
    return _clean(_ewm(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 8))
def cg_f097_specialist_and_quality_fund_exposure_core122_ewm_8q_v123_signal(investorname, value, units, securitytype):
    return _clean(_ewm(_safe_div(value, _mean(value, 20)), 8))
def cg_f097_specialist_and_quality_fund_exposure_core123_ewm_8q_v124_signal(investorname, value, units, securitytype):
    return _clean(_ewm(_z(value, 20), 8))
def cg_f097_specialist_and_quality_fund_exposure_core124_ewm_8q_v125_signal(investorname, value, units, securitytype):
    return _clean(_ewm(_rank(value, 20), 8))
def cg_f097_specialist_and_quality_fund_exposure_core125_ewm_8q_v126_signal(investorname, value, units, securitytype):
    return _clean(_ewm(_pct_change(value, 1), 8))
def cg_f097_specialist_and_quality_fund_exposure_core126_ewm_8q_v127_signal(investorname, value, units, securitytype):
    return _clean(_ewm(_pct_change(value, 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core127_ewm_8q_v128_signal(investorname, value, units, securitytype):
    return _clean(_ewm(_diff(value, 1), 8))
def cg_f097_specialist_and_quality_fund_exposure_core128_ewm_8q_v129_signal(investorname, value, units, securitytype):
    return _clean(_ewm(_ewm(value, 8), 8))
def cg_f097_specialist_and_quality_fund_exposure_core129_ewm_8q_v130_signal(investorname, value, units, securitytype):
    return _clean(_ewm(_safe_div(value, _std(value, 12) + 1.0), 8))
# core130-139: stability_12q
def cg_f097_specialist_and_quality_fund_exposure_core130_stability_12q_v131_signal(investorname, value, units, securitytype):
    return _clean(_safe_div(_std(value, 12), _mean(value, 12)))
def cg_f097_specialist_and_quality_fund_exposure_core131_stability_12q_v132_signal(investorname, value, units, securitytype):
    return _clean(_safe_div(_std(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 12), _mean(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value), 12)))
def cg_f097_specialist_and_quality_fund_exposure_core132_stability_12q_v133_signal(investorname, value, units, securitytype):
    return _clean(_safe_div(_std(_safe_div(value, _mean(value, 20)), 12), _mean(_safe_div(value, _mean(value, 20)), 12)))
def cg_f097_specialist_and_quality_fund_exposure_core133_stability_12q_v134_signal(investorname, value, units, securitytype):
    return _clean(_safe_div(_std(_z(value, 20), 12), _mean(_z(value, 20), 12)))
def cg_f097_specialist_and_quality_fund_exposure_core134_stability_12q_v135_signal(investorname, value, units, securitytype):
    return _clean(_safe_div(_std(_rank(value, 20), 12), _mean(_rank(value, 20), 12)))
def cg_f097_specialist_and_quality_fund_exposure_core135_stability_12q_v136_signal(investorname, value, units, securitytype):
    return _clean(_safe_div(_std(_pct_change(value, 1), 12), _mean(_pct_change(value, 1), 12)))
def cg_f097_specialist_and_quality_fund_exposure_core136_stability_12q_v137_signal(investorname, value, units, securitytype):
    return _clean(_safe_div(_std(_pct_change(value, 4), 12), _mean(_pct_change(value, 4), 12)))
def cg_f097_specialist_and_quality_fund_exposure_core137_stability_12q_v138_signal(investorname, value, units, securitytype):
    return _clean(_safe_div(_std(_diff(value, 1), 12), _mean(_diff(value, 1), 12)))
def cg_f097_specialist_and_quality_fund_exposure_core138_stability_12q_v139_signal(investorname, value, units, securitytype):
    return _clean(_safe_div(_std(_ewm(value, 8), 12), _mean(_ewm(value, 8), 12)))
def cg_f097_specialist_and_quality_fund_exposure_core139_stability_12q_v140_signal(investorname, value, units, securitytype):
    return _clean(_safe_div(_std(_safe_div(value, _std(value, 12) + 1.0), 12), _mean(_safe_div(value, _std(value, 12) + 1.0), 12)))
# core140-149: level
def cg_f097_specialist_and_quality_fund_exposure_core140_level_v141_signal(investorname, value, units, securitytype):
    return _clean(value)
def cg_f097_specialist_and_quality_fund_exposure_core141_level_v142_signal(investorname, value, units, securitytype):
    return _clean(_log(value.clip(lower=1.0) if hasattr(value, 'clip') else value))
def cg_f097_specialist_and_quality_fund_exposure_core142_level_v143_signal(investorname, value, units, securitytype):
    return _clean(_safe_div(value, _mean(value, 20)))
def cg_f097_specialist_and_quality_fund_exposure_core143_level_v144_signal(investorname, value, units, securitytype):
    return _clean(_z(value, 20))
def cg_f097_specialist_and_quality_fund_exposure_core144_level_v145_signal(investorname, value, units, securitytype):
    return _clean(_rank(value, 20))
def cg_f097_specialist_and_quality_fund_exposure_core145_level_v146_signal(investorname, value, units, securitytype):
    return _clean(_pct_change(value, 1))
def cg_f097_specialist_and_quality_fund_exposure_core146_level_v147_signal(investorname, value, units, securitytype):
    return _clean(_pct_change(value, 4))
def cg_f097_specialist_and_quality_fund_exposure_core147_level_v148_signal(investorname, value, units, securitytype):
    return _clean(_diff(value, 1))
def cg_f097_specialist_and_quality_fund_exposure_core148_level_v149_signal(investorname, value, units, securitytype):
    return _clean(_ewm(value, 8))
def cg_f097_specialist_and_quality_fund_exposure_core149_level_v150_signal(investorname, value, units, securitytype):
    return _clean(_safe_div(value, _std(value, 12) + 1.0))
