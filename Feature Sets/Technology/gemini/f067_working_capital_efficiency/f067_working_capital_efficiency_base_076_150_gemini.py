import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f067_working_capital_efficiency_core75_pct_4q_v076_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(_safe_div(revenue, assets), 4))
def cg_f067_working_capital_efficiency_core76_pct_4q_v077_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(workingcapital - _mean(workingcapital, 4), 4))
def cg_f067_working_capital_efficiency_core77_pct_4q_v078_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(_safe_div(workingcapital, revenue.abs() + 1.0), 4))
def cg_f067_working_capital_efficiency_core78_pct_4q_v079_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(_safe_div(workingcapital, assets.abs() + 1.0), 4))
def cg_f067_working_capital_efficiency_core79_pct_4q_v080_signal(workingcapital, revenue, assets):
    return _clean(_pct_change(_safe_div(revenue - workingcapital, assets.abs() + 1.0), 4))

# core80-89: std 8q
def cg_f067_working_capital_efficiency_core80_std_8q_v081_signal(workingcapital, revenue, assets):
    return _clean(_std(workingcapital, 8))
def cg_f067_working_capital_efficiency_core81_std_8q_v082_signal(workingcapital, revenue, assets):
    return _clean(_std(_safe_div(workingcapital, revenue), 8))
def cg_f067_working_capital_efficiency_core82_std_8q_v083_signal(workingcapital, revenue, assets):
    return _clean(_std(_safe_div(workingcapital, assets), 8))
def cg_f067_working_capital_efficiency_core84_std_8q_v084_signal(workingcapital, revenue, assets):
    return _clean(_std(revenue, 8))
def cg_f067_working_capital_efficiency_core84_std_8q_v085_signal(workingcapital, revenue, assets):
    return _clean(_std(assets, 8))
def cg_f067_working_capital_efficiency_core85_std_8q_v086_signal(workingcapital, revenue, assets):
    return _clean(_std(_safe_div(revenue, assets), 8))
def cg_f067_working_capital_efficiency_core86_std_8q_v087_signal(workingcapital, revenue, assets):
    return _clean(_std(workingcapital - _mean(workingcapital, 8), 8))
def cg_f067_working_capital_efficiency_core87_std_8q_v088_signal(workingcapital, revenue, assets):
    return _clean(_std(_safe_div(workingcapital, revenue.abs() + 1.0), 8))
def cg_f067_working_capital_efficiency_core88_std_8q_v089_signal(workingcapital, revenue, assets):
    return _clean(_std(_safe_div(workingcapital, assets.abs() + 1.0), 8))
def cg_f067_working_capital_efficiency_core89_std_8q_v090_signal(workingcapital, revenue, assets):
    return _clean(_std(_safe_div(revenue - workingcapital, assets.abs() + 1.0), 8))

# core90-99: log
def cg_f067_working_capital_efficiency_core90_log_v091_signal(workingcapital, revenue, assets):
    return _clean(_log(workingcapital.abs() + 1.0))
def cg_f067_working_capital_efficiency_core91_log_v092_signal(workingcapital, revenue, assets):
    return _clean(_log(_safe_div(workingcapital, revenue).abs() + 1.0))
def cg_f067_working_capital_efficiency_core92_log_v093_signal(workingcapital, revenue, assets):
    return _clean(_log(_safe_div(workingcapital, assets).abs() + 1.0))
def cg_f067_working_capital_efficiency_core93_log_v094_signal(workingcapital, revenue, assets):
    return _clean(_log(revenue.abs() + 1.0))
def cg_f067_working_capital_efficiency_core94_log_v095_signal(workingcapital, revenue, assets):
    return _clean(_log(assets.abs() + 1.0))
def cg_f067_working_capital_efficiency_core95_log_v096_signal(workingcapital, revenue, assets):
    return _clean(_log(_safe_div(revenue, assets).abs() + 1.0))
def cg_f067_working_capital_efficiency_core96_log_v097_signal(workingcapital, revenue, assets):
    return _clean(_log((workingcapital - _mean(workingcapital, 4)).abs() + 1.0))
def cg_f067_working_capital_efficiency_core97_log_v098_signal(workingcapital, revenue, assets):
    return _clean(_log(_safe_div(workingcapital, revenue.abs() + 1.0).abs() + 1.0))
def cg_f067_working_capital_efficiency_core98_log_v099_signal(workingcapital, revenue, assets):
    return _clean(_log(_safe_div(workingcapital, assets.abs() + 1.0).abs() + 1.0))
def cg_f067_working_capital_efficiency_core99_log_v100_signal(workingcapital, revenue, assets):
    return _clean(_log(_safe_div(revenue - workingcapital, assets.abs() + 1.0).abs() + 1.0))

# core100-109: diff 1q
def cg_f067_working_capital_efficiency_core100_diff_1q_v101_signal(workingcapital, revenue, assets):
    return _clean(_diff(workingcapital, 1))
def cg_f067_working_capital_efficiency_core101_diff_1q_v102_signal(workingcapital, revenue, assets):
    return _clean(_diff(_safe_div(workingcapital, revenue), 1))
def cg_f067_working_capital_efficiency_core102_diff_1q_v103_signal(workingcapital, revenue, assets):
    return _clean(_diff(_safe_div(workingcapital, assets), 1))
def cg_f067_working_capital_efficiency_core103_diff_1q_v104_signal(workingcapital, revenue, assets):
    return _clean(_diff(revenue, 1))
def cg_f067_working_capital_efficiency_core104_diff_1q_v105_signal(workingcapital, revenue, assets):
    return _clean(_diff(assets, 1))
def cg_f067_working_capital_efficiency_core105_diff_1q_v106_signal(workingcapital, revenue, assets):
    return _clean(_diff(_safe_div(revenue, assets), 1))
def cg_f067_working_capital_efficiency_core106_diff_1q_v107_signal(workingcapital, revenue, assets):
    return _clean(_diff(workingcapital - _mean(workingcapital, 4), 1))
def cg_f067_working_capital_efficiency_core107_diff_1q_v108_signal(workingcapital, revenue, assets):
    return _clean(_diff(_safe_div(workingcapital, revenue.abs() + 1.0), 1))
def cg_f067_working_capital_efficiency_core108_diff_1q_v109_signal(workingcapital, revenue, assets):
    return _clean(_diff(_safe_div(workingcapital, assets.abs() + 1.0), 1))
def cg_f067_working_capital_efficiency_core109_diff_1q_v110_signal(workingcapital, revenue, assets):
    return _clean(_diff(_safe_div(revenue - workingcapital, assets.abs() + 1.0), 1))

# core110-119: slope 4q
def cg_f067_working_capital_efficiency_core110_slope_4q_v111_signal(workingcapital, revenue, assets):
    return _clean(_slope(workingcapital, 4))
def cg_f067_working_capital_efficiency_core111_slope_4q_v112_signal(workingcapital, revenue, assets):
    return _clean(_slope(_safe_div(workingcapital, revenue), 4))
def cg_f067_working_capital_efficiency_core112_slope_4q_v113_signal(workingcapital, revenue, assets):
    return _clean(_slope(_safe_div(workingcapital, assets), 4))
def cg_f067_working_capital_efficiency_core113_slope_4q_v114_signal(workingcapital, revenue, assets):
    return _clean(_slope(revenue, 4))
def cg_f067_working_capital_efficiency_core114_slope_4q_v115_signal(workingcapital, revenue, assets):
    return _clean(_slope(assets, 4))
def cg_f067_working_capital_efficiency_core115_slope_4q_v116_signal(workingcapital, revenue, assets):
    return _clean(_slope(_safe_div(revenue, assets), 4))
def cg_f067_working_capital_efficiency_core116_slope_4q_v117_signal(workingcapital, revenue, assets):
    return _clean(_slope(workingcapital - _mean(workingcapital, 4), 4))
def cg_f067_working_capital_efficiency_core117_slope_4q_v118_signal(workingcapital, revenue, assets):
    return _clean(_slope(_safe_div(workingcapital, revenue.abs() + 1.0), 4))
def cg_f067_working_capital_efficiency_core118_slope_4q_v119_signal(workingcapital, revenue, assets):
    return _clean(_slope(_safe_div(workingcapital, assets.abs() + 1.0), 4))
def cg_f067_working_capital_efficiency_core119_slope_4q_v120_signal(workingcapital, revenue, assets):
    return _clean(_slope(_safe_div(revenue - workingcapital, assets.abs() + 1.0), 4))

# core120-129: ewm 8q
def cg_f067_working_capital_efficiency_core120_ewm_8q_v121_signal(workingcapital, revenue, assets):
    return _clean(_ewm(workingcapital, 8))
def cg_f067_working_capital_efficiency_core121_ewm_8q_v122_signal(workingcapital, revenue, assets):
    return _clean(_ewm(_safe_div(workingcapital, revenue), 8))
def cg_f067_working_capital_efficiency_core122_ewm_8q_v123_signal(workingcapital, revenue, assets):
    return _clean(_ewm(_safe_div(workingcapital, assets), 8))
def cg_f067_working_capital_efficiency_core123_ewm_8q_v124_signal(workingcapital, revenue, assets):
    return _clean(_ewm(revenue, 8))
def cg_f067_working_capital_efficiency_core124_ewm_8q_v125_signal(workingcapital, revenue, assets):
    return _clean(_ewm(assets, 8))
def cg_f067_working_capital_efficiency_core125_ewm_8q_v126_signal(workingcapital, revenue, assets):
    return _clean(_ewm(_safe_div(revenue, assets), 8))
def cg_f067_working_capital_efficiency_core126_ewm_8q_v127_signal(workingcapital, revenue, assets):
    return _clean(_ewm(workingcapital - _mean(workingcapital, 4), 8))
def cg_f067_working_capital_efficiency_core127_ewm_8q_v128_signal(workingcapital, revenue, assets):
    return _clean(_ewm(_safe_div(workingcapital, revenue.abs() + 1.0), 8))
def cg_f067_working_capital_efficiency_core128_ewm_8q_v129_signal(workingcapital, revenue, assets):
    return _clean(_ewm(_safe_div(workingcapital, assets.abs() + 1.0), 8))
def cg_f067_working_capital_efficiency_core129_ewm_8q_v130_signal(workingcapital, revenue, assets):
    return _clean(_ewm(_safe_div(revenue - workingcapital, assets.abs() + 1.0), 8))

# core130-139: stability 12q
def cg_f067_working_capital_efficiency_core130_stability_12q_v131_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(_std(workingcapital, 12), _mean(workingcapital, 12).abs() + 1.0))
def cg_f067_working_capital_efficiency_core131_stability_12q_v132_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(_std(_safe_div(workingcapital, revenue), 12), _mean(_safe_div(workingcapital, revenue), 12).abs() + 1.0))
def cg_f067_working_capital_efficiency_core132_stability_12q_v133_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(_std(_safe_div(workingcapital, assets), 12), _mean(_safe_div(workingcapital, assets), 12).abs() + 1.0))
def cg_f067_working_capital_efficiency_core133_stability_12q_v134_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(_std(revenue, 12), _mean(revenue, 12).abs() + 1.0))
def cg_f067_working_capital_efficiency_core134_stability_12q_v135_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(_std(assets, 12), _mean(assets, 12).abs() + 1.0))
def cg_f067_working_capital_efficiency_core135_stability_12q_v136_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(_std(_safe_div(revenue, assets), 12), _mean(_safe_div(revenue, assets), 12).abs() + 1.0))
def cg_f067_working_capital_efficiency_core136_stability_12q_v137_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(_std(workingcapital - _mean(workingcapital, 4), 12), _mean(workingcapital - _mean(workingcapital, 4), 12).abs() + 1.0))
def cg_f067_working_capital_efficiency_core137_stability_12q_v138_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(_std(_safe_div(workingcapital, revenue.abs() + 1.0), 12), _mean(_safe_div(workingcapital, revenue.abs() + 1.0), 12).abs() + 1.0))
def cg_f067_working_capital_efficiency_core138_stability_12q_v139_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(_std(_safe_div(workingcapital, assets.abs() + 1.0), 12), _mean(_safe_div(workingcapital, assets.abs() + 1.0), 12).abs() + 1.0))
def cg_f067_working_capital_efficiency_core139_stability_12q_v140_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(_std(_safe_div(revenue - workingcapital, assets.abs() + 1.0), 12), _mean(_safe_div(revenue - workingcapital, assets.abs() + 1.0), 12).abs() + 1.0))

# core140-149: raw variations
def cg_f067_working_capital_efficiency_core140_raw_v141_signal(workingcapital, revenue, assets):
    return _clean(workingcapital)
def cg_f067_working_capital_efficiency_core141_raw_v142_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(workingcapital, revenue))
def cg_f067_working_capital_efficiency_core142_raw_v143_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(workingcapital, assets))
def cg_f067_working_capital_efficiency_core143_raw_v144_signal(workingcapital, revenue, assets):
    return _clean(revenue)
def cg_f067_working_capital_efficiency_core144_raw_v145_signal(workingcapital, revenue, assets):
    return _clean(assets)
def cg_f067_working_capital_efficiency_core145_raw_v146_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(revenue, assets))
def cg_f067_working_capital_efficiency_core146_raw_v147_signal(workingcapital, revenue, assets):
    return _clean(workingcapital - _mean(workingcapital, 4))
def cg_f067_working_capital_efficiency_core147_raw_v148_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(workingcapital, revenue.abs() + 1.0))
def cg_f067_working_capital_efficiency_core148_raw_v149_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(workingcapital, assets.abs() + 1.0))
def cg_f067_working_capital_efficiency_core149_raw_v150_signal(workingcapital, revenue, assets):
    return _clean(_safe_div(revenue - workingcapital, assets.abs() + 1.0))
