import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f068_cash_conversion_cycle_core75_pct_4q_v076_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(inventory, 4))
def cg_f068_cash_conversion_cycle_core76_pct_4q_v077_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(payables, 4))
def cg_f068_cash_conversion_cycle_core77_pct_4q_v078_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(_safe_div(receivables, revenue), 4))
def cg_f068_cash_conversion_cycle_core78_pct_4q_v079_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(_safe_div(inventory, cor), 4))
def cg_f068_cash_conversion_cycle_core79_pct_4q_v080_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_pct_change(_safe_div(payables, cor), 4))

# core80-89: std 8q
def cg_f068_cash_conversion_cycle_core80_std_8q_v081_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_std(_safe_div(receivables, revenue) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core81_std_8q_v082_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_std(_safe_div(inventory, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core82_std_8q_v083_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_std(_safe_div(payables, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core83_std_8q_v084_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_std(_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core84_std_8q_v085_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_std(receivables, 8))
def cg_f068_cash_conversion_cycle_core85_std_8q_v086_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_std(inventory, 8))
def cg_f068_cash_conversion_cycle_core86_std_8q_v087_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_std(payables, 8))
def cg_f068_cash_conversion_cycle_core87_std_8q_v088_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_std(_safe_div(receivables, revenue), 8))
def cg_f068_cash_conversion_cycle_core88_std_8q_v089_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_std(_safe_div(inventory, cor), 8))
def cg_f068_cash_conversion_cycle_core89_std_8q_v090_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_std(_safe_div(payables, cor), 8))

# core90-99: log
def cg_f068_cash_conversion_cycle_core90_log_v091_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_log((_safe_div(receivables, revenue) * 90.0).abs() + 1.0))
def cg_f068_cash_conversion_cycle_core91_log_v092_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_log((_safe_div(inventory, cor) * 90.0).abs() + 1.0))
def cg_f068_cash_conversion_cycle_core92_log_v093_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_log((_safe_div(payables, cor) * 90.0).abs() + 1.0))
def cg_f068_cash_conversion_cycle_core93_log_v094_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_log((_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0).abs() + 1.0))
def cg_f068_cash_conversion_cycle_core94_log_v095_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_log(receivables.abs() + 1.0))
def cg_f068_cash_conversion_cycle_core95_log_v096_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_log(inventory.abs() + 1.0))
def cg_f068_cash_conversion_cycle_core96_log_v097_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_log(payables.abs() + 1.0))
def cg_f068_cash_conversion_cycle_core97_log_v098_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_log(_safe_div(receivables, revenue).abs() + 1.0))
def cg_f068_cash_conversion_cycle_core98_log_v099_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_log(_safe_div(inventory, cor).abs() + 1.0))
def cg_f068_cash_conversion_cycle_core99_log_v100_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_log(_safe_div(payables, cor).abs() + 1.0))

# core100-109: diff 1q
def cg_f068_cash_conversion_cycle_core100_diff_1q_v101_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_safe_div(receivables, revenue) * 90.0, 1))
def cg_f068_cash_conversion_cycle_core101_diff_1q_v102_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_safe_div(inventory, cor) * 90.0, 1))
def cg_f068_cash_conversion_cycle_core102_diff_1q_v103_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_safe_div(payables, cor) * 90.0, 1))
def cg_f068_cash_conversion_cycle_core103_diff_1q_v104_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0, 1))
def cg_f068_cash_conversion_cycle_core104_diff_1q_v105_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(receivables, 1))
def cg_f068_cash_conversion_cycle_core105_diff_1q_v106_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(inventory, 1))
def cg_f068_cash_conversion_cycle_core106_diff_1q_v107_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(payables, 1))
def cg_f068_cash_conversion_cycle_core107_diff_1q_v108_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_safe_div(receivables, revenue), 1))
def cg_f068_cash_conversion_cycle_core108_diff_1q_v109_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_safe_div(inventory, cor), 1))
def cg_f068_cash_conversion_cycle_core109_diff_1q_v110_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_diff(_safe_div(payables, cor), 1))

# core110-119: slope 4q
def cg_f068_cash_conversion_cycle_core110_slope_4q_v111_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_safe_div(receivables, revenue) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core111_slope_4q_v112_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_safe_div(inventory, cor) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core112_slope_4q_v113_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_safe_div(payables, cor) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core113_slope_4q_v114_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0, 4))
def cg_f068_cash_conversion_cycle_core114_slope_4q_v115_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(receivables, 4))
def cg_f068_cash_conversion_cycle_core115_slope_4q_v116_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(inventory, 4))
def cg_f068_cash_conversion_cycle_core116_slope_4q_v117_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(payables, 4))
def cg_f068_cash_conversion_cycle_core117_slope_4q_v118_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_safe_div(receivables, revenue), 4))
def cg_f068_cash_conversion_cycle_core118_slope_4q_v119_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_safe_div(inventory, cor), 4))
def cg_f068_cash_conversion_cycle_core119_slope_4q_v120_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_slope(_safe_div(payables, cor), 4))

# core120-129: ewm 8q
def cg_f068_cash_conversion_cycle_core120_ewm_8q_v121_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_ewm(_safe_div(receivables, revenue) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core121_ewm_8q_v122_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_ewm(_safe_div(inventory, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core122_ewm_8q_v123_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_ewm(_safe_div(payables, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core123_ewm_8q_v124_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_ewm(_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0, 8))
def cg_f068_cash_conversion_cycle_core124_ewm_8q_v125_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_ewm(receivables, 8))
def cg_f068_cash_conversion_cycle_core125_ewm_8q_v126_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_ewm(inventory, 8))
def cg_f068_cash_conversion_cycle_core126_ewm_8q_v127_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_ewm(payables, 8))
def cg_f068_cash_conversion_cycle_core127_ewm_8q_v128_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_ewm(_safe_div(receivables, revenue), 8))
def cg_f068_cash_conversion_cycle_core128_ewm_8q_v129_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_ewm(_safe_div(inventory, cor), 8))
def cg_f068_cash_conversion_cycle_core129_ewm_8q_v130_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_ewm(_safe_div(payables, cor), 8))

# core130-139: stability 12q
def cg_f068_cash_conversion_cycle_core130_stability_12q_v131_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(_std(_safe_div(receivables, revenue) * 90.0, 12), _mean(_safe_div(receivables, revenue) * 90.0, 12).abs() + 1.0))
def cg_f068_cash_conversion_cycle_core131_stability_12q_v132_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(_std(_safe_div(inventory, cor) * 90.0, 12), _mean(_safe_div(inventory, cor) * 90.0, 12).abs() + 1.0))
def cg_f068_cash_conversion_cycle_core132_stability_12q_v133_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(_std(_safe_div(payables, cor) * 90.0, 12), _mean(_safe_div(payables, cor) * 90.0, 12).abs() + 1.0))
def cg_f068_cash_conversion_cycle_core133_stability_12q_v134_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(_std(_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0, 12), _mean(_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0, 12).abs() + 1.0))
def cg_f068_cash_conversion_cycle_core134_stability_12q_v135_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(_std(receivables, 12), _mean(receivables, 12).abs() + 1.0))
def cg_f068_cash_conversion_cycle_core135_stability_12q_v136_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(_std(inventory, 12), _mean(inventory, 12).abs() + 1.0))
def cg_f068_cash_conversion_cycle_core136_stability_12q_v137_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(_std(payables, 12), _mean(payables, 12).abs() + 1.0))
def cg_f068_cash_conversion_cycle_core137_stability_12q_v138_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(_std(_safe_div(receivables, revenue), 12), _mean(_safe_div(receivables, revenue), 12).abs() + 1.0))
def cg_f068_cash_conversion_cycle_core138_stability_12q_v139_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(_std(_safe_div(inventory, cor), 12), _mean(_safe_div(inventory, cor), 12).abs() + 1.0))
def cg_f068_cash_conversion_cycle_core139_stability_12q_v140_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(_std(_safe_div(payables, cor), 12), _mean(_safe_div(payables, cor), 12).abs() + 1.0))

# core140-149: raw variations
def cg_f068_cash_conversion_cycle_core140_raw_v141_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(receivables, revenue) * 90.0)
def cg_f068_cash_conversion_cycle_core141_raw_v142_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(inventory, cor) * 90.0)
def cg_f068_cash_conversion_cycle_core142_raw_v143_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(payables, cor) * 90.0)
def cg_f068_cash_conversion_cycle_core143_raw_v144_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(receivables, revenue) * 90.0 + _safe_div(inventory, cor) * 90.0 - _safe_div(payables, cor) * 90.0)
def cg_f068_cash_conversion_cycle_core144_raw_v145_signal(receivables, inventory, payables, revenue, cor):
    return _clean(receivables)
def cg_f068_cash_conversion_cycle_core145_raw_v146_signal(receivables, inventory, payables, revenue, cor):
    return _clean(inventory)
def cg_f068_cash_conversion_cycle_core146_raw_v147_signal(receivables, inventory, payables, revenue, cor):
    return _clean(payables)
def cg_f068_cash_conversion_cycle_core147_raw_v148_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(receivables, revenue))
def cg_f068_cash_conversion_cycle_core148_raw_v149_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(inventory, cor))
def cg_f068_cash_conversion_cycle_core149_raw_v150_signal(receivables, inventory, payables, revenue, cor):
    return _clean(_safe_div(payables, cor))
