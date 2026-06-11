import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f065_return_on_invested_capital_core75_pct_4q_v076_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(_safe_div(invcap, invcapavg), 4))
def cg_f065_return_on_invested_capital_core76_pct_4q_v077_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(_diff(roic, 1), 4))
def cg_f065_return_on_invested_capital_core77_pct_4q_v078_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(_pct_change(invcap, 1), 4))
def cg_f065_return_on_invested_capital_core78_pct_4q_v079_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(_safe_div(roic, invcapavg.abs() + 1.0), 4))
def cg_f065_return_on_invested_capital_core79_pct_4q_v080_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0), 4))

# core80-89: std 8q
def cg_f065_return_on_invested_capital_core80_std_8q_v081_signal(roic, invcap, invcapavg):
    return _clean(_std(roic, 8))
def cg_f065_return_on_invested_capital_core81_std_8q_v082_signal(roic, invcap, invcapavg):
    return _clean(_std(invcap, 8))
def cg_f065_return_on_invested_capital_core82_std_8q_v083_signal(roic, invcap, invcapavg):
    return _clean(_std(invcapavg, 8))
def cg_f065_return_on_invested_capital_core83_std_8q_v084_signal(roic, invcap, invcapavg):
    return _clean(_std(_safe_div(roic * invcap, invcapavg), 8))
def cg_f065_return_on_invested_capital_core84_std_8q_v085_signal(roic, invcap, invcapavg):
    return _clean(_std(roic - _mean(roic, 8), 8))
def cg_f065_return_on_invested_capital_core85_std_8q_v086_signal(roic, invcap, invcapavg):
    return _clean(_std(_safe_div(invcap, invcapavg), 8))
def cg_f065_return_on_invested_capital_core86_std_8q_v087_signal(roic, invcap, invcapavg):
    return _clean(_std(_diff(roic, 1), 8))
def cg_f065_return_on_invested_capital_core87_std_8q_v088_signal(roic, invcap, invcapavg):
    return _clean(_std(_pct_change(invcap, 1), 8))
def cg_f065_return_on_invested_capital_core88_std_8q_v089_signal(roic, invcap, invcapavg):
    return _clean(_std(_safe_div(roic, invcapavg.abs() + 1.0), 8))
def cg_f065_return_on_invested_capital_core89_std_8q_v090_signal(roic, invcap, invcapavg):
    return _clean(_std(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0), 8))

# core90-99: log
def cg_f065_return_on_invested_capital_core90_log_v091_signal(roic, invcap, invcapavg):
    return _clean(_log(roic.abs() + 1.0))
def cg_f065_return_on_invested_capital_core91_log_v092_signal(roic, invcap, invcapavg):
    return _clean(_log(invcap.abs() + 1.0))
def cg_f065_return_on_invested_capital_core92_log_v093_signal(roic, invcap, invcapavg):
    return _clean(_log(invcapavg.abs() + 1.0))
def cg_f065_return_on_invested_capital_core93_log_v094_signal(roic, invcap, invcapavg):
    return _clean(_log(_safe_div(roic * invcap, invcapavg).abs() + 1.0))
def cg_f065_return_on_invested_capital_core94_log_v095_signal(roic, invcap, invcapavg):
    return _clean(_log((roic - _mean(roic, 4)).abs() + 1.0))
def cg_f065_return_on_invested_capital_core95_log_v096_signal(roic, invcap, invcapavg):
    return _clean(_log(_safe_div(invcap, invcapavg).abs() + 1.0))
def cg_f065_return_on_invested_capital_core96_log_v097_signal(roic, invcap, invcapavg):
    return _clean(_log(_diff(roic, 1).abs() + 1.0))
def cg_f065_return_on_invested_capital_core97_log_v098_signal(roic, invcap, invcapavg):
    return _clean(_log(_pct_change(invcap, 1).abs() + 1.0))
def cg_f065_return_on_invested_capital_core98_log_v099_signal(roic, invcap, invcapavg):
    return _clean(_log(_safe_div(roic, invcapavg.abs() + 1.0).abs() + 1.0))
def cg_f065_return_on_invested_capital_core99_log_v100_signal(roic, invcap, invcapavg):
    return _clean(_log(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0).abs() + 1.0))

# core100-109: diff 1q
def cg_f065_return_on_invested_capital_core100_diff_1q_v101_signal(roic, invcap, invcapavg):
    return _clean(_diff(roic, 1))
def cg_f065_return_on_invested_capital_core101_diff_1q_v102_signal(roic, invcap, invcapavg):
    return _clean(_diff(invcap, 1))
def cg_f065_return_on_invested_capital_core102_diff_1q_v103_signal(roic, invcap, invcapavg):
    return _clean(_diff(invcapavg, 1))
def cg_f065_return_on_invested_capital_core103_diff_1q_v104_signal(roic, invcap, invcapavg):
    return _clean(_diff(_safe_div(roic * invcap, invcapavg), 1))
def cg_f065_return_on_invested_capital_core104_diff_1q_v105_signal(roic, invcap, invcapavg):
    return _clean(_diff(roic - _mean(roic, 4), 1))
def cg_f065_return_on_invested_capital_core105_diff_1q_v106_signal(roic, invcap, invcapavg):
    return _clean(_diff(_safe_div(invcap, invcapavg), 1))
def cg_f065_return_on_invested_capital_core106_diff_1q_v107_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(roic, 1), 1))
def cg_f065_return_on_invested_capital_core107_diff_1q_v108_signal(roic, invcap, invcapavg):
    return _clean(_diff(_pct_change(invcap, 1), 1))
def cg_f065_return_on_invested_capital_core108_diff_1q_v109_signal(roic, invcap, invcapavg):
    return _clean(_diff(_safe_div(roic, invcapavg.abs() + 1.0), 1))
def cg_f065_return_on_invested_capital_core109_diff_1q_v110_signal(roic, invcap, invcapavg):
    return _clean(_diff(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0), 1))

# core110-119: slope 4q
def cg_f065_return_on_invested_capital_core110_slope_4q_v111_signal(roic, invcap, invcapavg):
    return _clean(_slope(roic, 4))
def cg_f065_return_on_invested_capital_core111_slope_4q_v112_signal(roic, invcap, invcapavg):
    return _clean(_slope(invcap, 4))
def cg_f065_return_on_invested_capital_core112_slope_4q_v113_signal(roic, invcap, invcapavg):
    return _clean(_slope(invcapavg, 4))
def cg_f065_return_on_invested_capital_core113_slope_4q_v114_signal(roic, invcap, invcapavg):
    return _clean(_slope(_safe_div(roic * invcap, invcapavg), 4))
def cg_f065_return_on_invested_capital_core114_slope_4q_v115_signal(roic, invcap, invcapavg):
    return _clean(_slope(roic - _mean(roic, 4), 4))
def cg_f065_return_on_invested_capital_core115_slope_4q_v116_signal(roic, invcap, invcapavg):
    return _clean(_slope(_safe_div(invcap, invcapavg), 4))
def cg_f065_return_on_invested_capital_core116_slope_4q_v117_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(roic, 1), 4))
def cg_f065_return_on_invested_capital_core117_slope_4q_v118_signal(roic, invcap, invcapavg):
    return _clean(_slope(_pct_change(invcap, 1), 4))
def cg_f065_return_on_invested_capital_core118_slope_4q_v119_signal(roic, invcap, invcapavg):
    return _clean(_slope(_safe_div(roic, invcapavg.abs() + 1.0), 4))
def cg_f065_return_on_invested_capital_core119_slope_4q_v120_signal(roic, invcap, invcapavg):
    return _clean(_slope(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0), 4))

# core120-129: ewm 8q
def cg_f065_return_on_invested_capital_core120_ewm_8q_v121_signal(roic, invcap, invcapavg):
    return _clean(_ewm(roic, 8))
def cg_f065_return_on_invested_capital_core121_ewm_8q_v122_signal(roic, invcap, invcapavg):
    return _clean(_ewm(invcap, 8))
def cg_f065_return_on_invested_capital_core122_ewm_8q_v123_signal(roic, invcap, invcapavg):
    return _clean(_ewm(invcapavg, 8))
def cg_f065_return_on_invested_capital_core123_ewm_8q_v124_signal(roic, invcap, invcapavg):
    return _clean(_ewm(_safe_div(roic * invcap, invcapavg), 8))
def cg_f065_return_on_invested_capital_core124_ewm_8q_v125_signal(roic, invcap, invcapavg):
    return _clean(_ewm(roic - _mean(roic, 4), 8))
def cg_f065_return_on_invested_capital_core125_ewm_8q_v126_signal(roic, invcap, invcapavg):
    return _clean(_ewm(_safe_div(invcap, invcapavg), 8))
def cg_f065_return_on_invested_capital_core126_ewm_8q_v127_signal(roic, invcap, invcapavg):
    return _clean(_ewm(_diff(roic, 1), 8))
def cg_f065_return_on_invested_capital_core127_ewm_8q_v128_signal(roic, invcap, invcapavg):
    return _clean(_ewm(_pct_change(invcap, 1), 8))
def cg_f065_return_on_invested_capital_core128_ewm_8q_v129_signal(roic, invcap, invcapavg):
    return _clean(_ewm(_safe_div(roic, invcapavg.abs() + 1.0), 8))
def cg_f065_return_on_invested_capital_core129_ewm_8q_v130_signal(roic, invcap, invcapavg):
    return _clean(_ewm(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0), 8))

# core130-139: stability 12q
def cg_f065_return_on_invested_capital_core130_stability_12q_v131_signal(roic, invcap, invcapavg):
    return _clean(_safe_div(_std(roic, 12), _mean(roic, 12).abs() + 1.0))
def cg_f065_return_on_invested_capital_core131_stability_12q_v132_signal(roic, invcap, invcapavg):
    return _clean(_safe_div(_std(invcap, 12), _mean(invcap, 12).abs() + 1.0))
def cg_f065_return_on_invested_capital_core132_stability_12q_v133_signal(roic, invcap, invcapavg):
    return _clean(_safe_div(_std(invcapavg, 12), _mean(invcapavg, 12).abs() + 1.0))
def cg_f065_return_on_invested_capital_core133_stability_12q_v134_signal(roic, invcap, invcapavg):
    return _clean(_safe_div(_std(_safe_div(roic * invcap, invcapavg), 12), _mean(_safe_div(roic * invcap, invcapavg), 12).abs() + 1.0))
def cg_f065_return_on_invested_capital_core134_stability_12q_v135_signal(roic, invcap, invcapavg):
    return _clean(_safe_div(_std(roic - _mean(roic, 4), 12), _mean(roic - _mean(roic, 4), 12).abs() + 1.0))
def cg_f065_return_on_invested_capital_core135_stability_12q_v136_signal(roic, invcap, invcapavg):
    return _clean(_safe_div(_std(_safe_div(invcap, invcapavg), 12), _mean(_safe_div(invcap, invcapavg), 12).abs() + 1.0))
def cg_f065_return_on_invested_capital_core136_stability_12q_v137_signal(roic, invcap, invcapavg):
    return _clean(_safe_div(_std(_diff(roic, 1), 12), _mean(_diff(roic, 1), 12).abs() + 1.0))
def cg_f065_return_on_invested_capital_core137_stability_12q_v138_signal(roic, invcap, invcapavg):
    return _clean(_safe_div(_std(_pct_change(invcap, 1), 12), _mean(_pct_change(invcap, 1), 12).abs() + 1.0))
def cg_f065_return_on_invested_capital_core138_stability_12q_v139_signal(roic, invcap, invcapavg):
    return _clean(_safe_div(_std(_safe_div(roic, invcapavg.abs() + 1.0), 12), _mean(_safe_div(roic, invcapavg.abs() + 1.0), 12).abs() + 1.0))
def cg_f065_return_on_invested_capital_core139_stability_12q_v140_signal(roic, invcap, invcapavg):
    return _clean(_safe_div(_std(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0), 12), _mean(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0), 12).abs() + 1.0))

# core140-149: raw variations
def cg_f065_return_on_invested_capital_core140_raw_v141_signal(roic, invcap, invcapavg):
    return _clean(roic)
def cg_f065_return_on_invested_capital_core141_raw_v142_signal(roic, invcap, invcapavg):
    return _clean(invcap)
def cg_f065_return_on_invested_capital_core142_raw_v143_signal(roic, invcap, invcapavg):
    return _clean(invcapavg)
def cg_f065_return_on_invested_capital_core143_raw_v144_signal(roic, invcap, invcapavg):
    return _clean(_safe_div(roic * invcap, invcapavg))
def cg_f065_return_on_invested_capital_core144_raw_v145_signal(roic, invcap, invcapavg):
    return _clean(roic - _mean(roic, 4))
def cg_f065_return_on_invested_capital_core145_raw_v146_signal(roic, invcap, invcapavg):
    return _clean(_safe_div(invcap, invcapavg))
def cg_f065_return_on_invested_capital_core146_raw_v147_signal(roic, invcap, invcapavg):
    return _clean(_diff(roic, 1))
def cg_f065_return_on_invested_capital_core147_raw_v148_signal(roic, invcap, invcapavg):
    return _clean(_pct_change(invcap, 1))
def cg_f065_return_on_invested_capital_core148_raw_v149_signal(roic, invcap, invcapavg):
    return _clean(_safe_div(roic, invcapavg.abs() + 1.0))
def cg_f065_return_on_invested_capital_core149_raw_v150_signal(roic, invcap, invcapavg):
    return _clean(_safe_div(invcap - invcapavg, invcapavg.abs() + 1.0))
