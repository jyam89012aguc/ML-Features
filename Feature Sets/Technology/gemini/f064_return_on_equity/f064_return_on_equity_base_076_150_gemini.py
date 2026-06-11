import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f064_return_on_equity_core75_pct_4q_v076_signal(netinc, equity):
    return _clean(_pct_change(equity - _mean(equity, 4), 4))
def cg_f064_return_on_equity_core76_pct_4q_v077_signal(netinc, equity):
    return _clean(_pct_change(_safe_div(netinc - _mean(netinc, 4), equity.abs() + 1.0), 4))
def cg_f064_return_on_equity_core77_pct_4q_v078_signal(netinc, equity):
    return _clean(_pct_change(_safe_div(netinc, (equity - _mean(equity, 4)).abs() + 1.0), 4))
def cg_f064_return_on_equity_core78_pct_4q_v079_signal(netinc, equity):
    return _clean(_pct_change(_safe_div(netinc, equity).abs(), 4))
def cg_f064_return_on_equity_core79_pct_4q_v080_signal(netinc, equity):
    return _clean(_pct_change(_safe_div(netinc, equity * 0.5 + 1.0), 4))

# core80-89: std 8q
def cg_f064_return_on_equity_core80_std_8q_v081_signal(netinc, equity):
    return _clean(_std(netinc, 8))
def cg_f064_return_on_equity_core81_std_8q_v082_signal(netinc, equity):
    return _clean(_std(_safe_div(netinc, equity), 8))
def cg_f064_return_on_equity_core82_std_8q_v083_signal(netinc, equity):
    return _clean(_std(equity, 8))
def cg_f064_return_on_equity_core83_std_8q_v084_signal(netinc, equity):
    return _clean(_std(_safe_div(netinc, equity.abs() + 1.0), 8))
def cg_f064_return_on_equity_core84_std_8q_v085_signal(netinc, equity):
    return _clean(_std(netinc - _mean(netinc, 8), 8))
def cg_f064_return_on_equity_core85_std_8q_v086_signal(netinc, equity):
    return _clean(_std(equity - _mean(equity, 8), 8))
def cg_f064_return_on_equity_core86_std_8q_v087_signal(netinc, equity):
    return _clean(_std(_safe_div(netinc - _mean(netinc, 8), equity.abs() + 1.0), 8))
def cg_f064_return_on_equity_core87_std_8q_v088_signal(netinc, equity):
    return _clean(_std(_safe_div(netinc, (equity - _mean(equity, 8)).abs() + 1.0), 8))
def cg_f064_return_on_equity_core88_std_8q_v089_signal(netinc, equity):
    return _clean(_std(_safe_div(netinc, equity).abs(), 8))
def cg_f064_return_on_equity_core89_std_8q_v090_signal(netinc, equity):
    return _clean(_std(_safe_div(netinc, equity * 0.5 + 1.0), 8))

# core90-99: log
def cg_f064_return_on_equity_core90_log_v091_signal(netinc, equity):
    return _clean(_log(netinc.abs() + 1.0))
def cg_f064_return_on_equity_core91_log_v092_signal(netinc, equity):
    return _clean(_log(_safe_div(netinc, equity).abs() + 1.0))
def cg_f064_return_on_equity_core92_log_v093_signal(netinc, equity):
    return _clean(_log(equity.abs() + 1.0))
def cg_f064_return_on_equity_core93_log_v094_signal(netinc, equity):
    return _clean(_log(_safe_div(netinc, equity.abs() + 1.0).abs() + 1.0))
def cg_f064_return_on_equity_core94_log_v095_signal(netinc, equity):
    return _clean(_log((netinc - _mean(netinc, 4)).abs() + 1.0))
def cg_f064_return_on_equity_core95_log_v096_signal(netinc, equity):
    return _clean(_log((equity - _mean(equity, 4)).abs() + 1.0))
def cg_f064_return_on_equity_core96_log_v097_signal(netinc, equity):
    return _clean(_log(_safe_div(netinc - _mean(netinc, 4), equity.abs() + 1.0).abs() + 1.0))
def cg_f064_return_on_equity_core97_log_v098_signal(netinc, equity):
    return _clean(_log(_safe_div(netinc, (equity - _mean(equity, 4)).abs() + 1.0).abs() + 1.0))
def cg_f064_return_on_equity_core98_log_v099_signal(netinc, equity):
    return _clean(_log(_safe_div(netinc, equity).abs() + 1.0))
def cg_f064_return_on_equity_core99_log_v100_signal(netinc, equity):
    return _clean(_log(_safe_div(netinc, equity * 0.5 + 1.0).abs() + 1.0))

# core100-109: diff 1q
def cg_f064_return_on_equity_core100_diff_1q_v101_signal(netinc, equity):
    return _clean(_diff(netinc, 1))
def cg_f064_return_on_equity_core101_diff_1q_v102_signal(netinc, equity):
    return _clean(_diff(_safe_div(netinc, equity), 1))
def cg_f064_return_on_equity_core102_diff_1q_v103_signal(netinc, equity):
    return _clean(_diff(equity, 1))
def cg_f064_return_on_equity_core103_diff_1q_v104_signal(netinc, equity):
    return _clean(_diff(_safe_div(netinc, equity.abs() + 1.0), 1))
def cg_f064_return_on_equity_core104_diff_1q_v105_signal(netinc, equity):
    return _clean(_diff(netinc - _mean(netinc, 4), 1))
def cg_f064_return_on_equity_core105_diff_1q_v106_signal(netinc, equity):
    return _clean(_diff(equity - _mean(equity, 4), 1))
def cg_f064_return_on_equity_core106_diff_1q_v107_signal(netinc, equity):
    return _clean(_diff(_safe_div(netinc - _mean(netinc, 4), equity.abs() + 1.0), 1))
def cg_f064_return_on_equity_core107_diff_1q_v108_signal(netinc, equity):
    return _clean(_diff(_safe_div(netinc, (equity - _mean(equity, 4)).abs() + 1.0), 1))
def cg_f064_return_on_equity_core108_diff_1q_v109_signal(netinc, equity):
    return _clean(_diff(_safe_div(netinc, equity).abs(), 1))
def cg_f064_return_on_equity_core109_diff_1q_v110_signal(netinc, equity):
    return _clean(_diff(_safe_div(netinc, equity * 0.5 + 1.0), 1))

# core110-119: slope 4q
def cg_f064_return_on_equity_core110_slope_4q_v111_signal(netinc, equity):
    return _clean(_slope(netinc, 4))
def cg_f064_return_on_equity_core111_slope_4q_v112_signal(netinc, equity):
    return _clean(_slope(_safe_div(netinc, equity), 4))
def cg_f064_return_on_equity_core112_slope_4q_v113_signal(netinc, equity):
    return _clean(_slope(equity, 4))
def cg_f064_return_on_equity_core113_slope_4q_v114_signal(netinc, equity):
    return _clean(_slope(_safe_div(netinc, equity.abs() + 1.0), 4))
def cg_f064_return_on_equity_core114_slope_4q_v115_signal(netinc, equity):
    return _clean(_slope(netinc - _mean(netinc, 4), 4))
def cg_f064_return_on_equity_core115_slope_4q_v116_signal(netinc, equity):
    return _clean(_slope(equity - _mean(equity, 4), 4))
def cg_f064_return_on_equity_core116_slope_4q_v117_signal(netinc, equity):
    return _clean(_slope(_safe_div(netinc - _mean(netinc, 4), equity.abs() + 1.0), 4))
def cg_f064_return_on_equity_core117_slope_4q_v118_signal(netinc, equity):
    return _clean(_slope(_safe_div(netinc, (equity - _mean(equity, 4)).abs() + 1.0), 4))
def cg_f064_return_on_equity_core118_slope_4q_v119_signal(netinc, equity):
    return _clean(_slope(_safe_div(netinc, equity).abs(), 4))
def cg_f064_return_on_equity_core119_slope_4q_v120_signal(netinc, equity):
    return _clean(_slope(_safe_div(netinc, equity * 0.5 + 1.0), 4))

# core120-129: ewm 8q
def cg_f064_return_on_equity_core120_ewm_8q_v121_signal(netinc, equity):
    return _clean(_ewm(netinc, 8))
def cg_f064_return_on_equity_core121_ewm_8q_v122_signal(netinc, equity):
    return _clean(_ewm(_safe_div(netinc, equity), 8))
def cg_f064_return_on_equity_core122_ewm_8q_v123_signal(netinc, equity):
    return _clean(_ewm(equity, 8))
def cg_f064_return_on_equity_core122_ewm_8q_v124_signal(netinc, equity):
    return _clean(_ewm(_safe_div(netinc, equity.abs() + 1.0), 8))
def cg_f064_return_on_equity_core124_ewm_8q_v125_signal(netinc, equity):
    return _clean(_ewm(netinc - _mean(netinc, 4), 8))
def cg_f064_return_on_equity_core125_ewm_8q_v126_signal(netinc, equity):
    return _clean(_ewm(equity - _mean(equity, 4), 8))
def cg_f064_return_on_equity_core126_ewm_8q_v127_signal(netinc, equity):
    return _clean(_ewm(_safe_div(netinc - _mean(netinc, 4), equity.abs() + 1.0), 8))
def cg_f064_return_on_equity_core127_ewm_8q_v128_signal(netinc, equity):
    return _clean(_ewm(_safe_div(netinc, (equity - _mean(equity, 4)).abs() + 1.0), 8))
def cg_f064_return_on_equity_core128_ewm_8q_v129_signal(netinc, equity):
    return _clean(_ewm(_safe_div(netinc, equity).abs(), 8))
def cg_f064_return_on_equity_core129_ewm_8q_v130_signal(netinc, equity):
    return _clean(_ewm(_safe_div(netinc, equity * 0.5 + 1.0), 8))

# core130-139: stability 12q
def cg_f064_return_on_equity_core130_stability_12q_v131_signal(netinc, equity):
    return _clean(_safe_div(_std(netinc, 12), _mean(netinc, 12)))
def cg_f064_return_on_equity_core131_stability_12q_v132_signal(netinc, equity):
    return _clean(_safe_div(_std(_safe_div(netinc, equity), 12), _mean(_safe_div(netinc, equity), 12)))
def cg_f064_return_on_equity_core132_stability_12q_v133_signal(netinc, equity):
    return _clean(_safe_div(_std(equity, 12), _mean(equity, 12)))
def cg_f064_return_on_equity_core133_stability_12q_v134_signal(netinc, equity):
    return _clean(_safe_div(_std(_safe_div(netinc, equity.abs() + 1.0), 12), _mean(_safe_div(netinc, equity.abs() + 1.0), 12)))
def cg_f064_return_on_equity_core134_stability_12q_v135_signal(netinc, equity):
    return _clean(_safe_div(_std(netinc - _mean(netinc, 4), 12), _mean(netinc - _mean(netinc, 4), 12).abs() + 1.0))
def cg_f064_return_on_equity_core135_stability_12q_v136_signal(netinc, equity):
    return _clean(_safe_div(_std(equity - _mean(equity, 4), 12), _mean(equity - _mean(equity, 4), 12).abs() + 1.0))
def cg_f064_return_on_equity_core136_stability_12q_v137_signal(netinc, equity):
    return _clean(_safe_div(_std(_safe_div(netinc - _mean(netinc, 4), equity.abs() + 1.0), 12), _mean(_safe_div(netinc - _mean(netinc, 4), equity.abs() + 1.0), 12).abs() + 1.0))
def cg_f064_return_on_equity_core137_stability_12q_v138_signal(netinc, equity):
    return _clean(_safe_div(_std(_safe_div(netinc, (equity - _mean(equity, 4)).abs() + 1.0), 12), _mean(_safe_div(netinc, (equity - _mean(equity, 4)).abs() + 1.0), 12).abs() + 1.0))
def cg_f064_return_on_equity_core138_stability_12q_v139_signal(netinc, equity):
    return _clean(_safe_div(_std(_safe_div(netinc, equity).abs(), 12), _mean(_safe_div(netinc, equity).abs(), 12).abs() + 1.0))
def cg_f064_return_on_equity_core139_stability_12q_v140_signal(netinc, equity):
    return _clean(_safe_div(_std(_safe_div(netinc, equity * 0.5 + 1.0), 12), _mean(_safe_div(netinc, equity * 0.5 + 1.0), 12).abs() + 1.0))

# core140-149: raw variations
def cg_f064_return_on_equity_core140_raw_v141_signal(netinc, equity):
    return _clean(netinc)
def cg_f064_return_on_equity_core141_raw_v142_signal(netinc, equity):
    return _clean(_safe_div(netinc, equity))
def cg_f064_return_on_equity_core142_raw_v143_signal(netinc, equity):
    return _clean(equity)
def cg_f064_return_on_equity_core143_raw_v144_signal(netinc, equity):
    return _clean(_safe_div(netinc, equity.abs() + 1.0))
def cg_f064_return_on_equity_core144_raw_v145_signal(netinc, equity):
    return _clean(netinc - _mean(netinc, 4))
def cg_f064_return_on_equity_core145_raw_v146_signal(netinc, equity):
    return _clean(equity - _mean(equity, 4))
def cg_f064_return_on_equity_core146_raw_v147_signal(netinc, equity):
    return _clean(_safe_div(netinc - _mean(netinc, 4), equity.abs() + 1.0))
def cg_f064_return_on_equity_core147_raw_v148_signal(netinc, equity):
    return _clean(_safe_div(netinc, (equity - _mean(equity, 4)).abs() + 1.0))
def cg_f064_return_on_equity_core148_raw_v149_signal(netinc, equity):
    return _clean(_safe_div(netinc, equity).abs())
def cg_f064_return_on_equity_core149_raw_v150_signal(netinc, equity):
    return _clean(_safe_div(netinc, equity * 0.5 + 1.0))
