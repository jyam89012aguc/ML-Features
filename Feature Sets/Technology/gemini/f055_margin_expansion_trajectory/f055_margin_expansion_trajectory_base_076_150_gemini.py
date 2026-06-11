import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f055_margin_expansion_trajectory_core75_pct_4q_v076_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_pct_change(_diff(netmargin, 4) - _diff(grossmargin, 4), 4))
def cg_f055_margin_expansion_trajectory_core76_pct_4q_v077_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_pct_change(_diff(_diff(grossmargin, 4), 1), 4))
def cg_f055_margin_expansion_trajectory_core77_pct_4q_v078_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_pct_change(_diff(_diff(opmargin, 4), 1), 4))
def cg_f055_margin_expansion_trajectory_core78_pct_4q_v079_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_pct_change(_diff(grossmargin, 1), 4))
def cg_f055_margin_expansion_trajectory_core79_pct_4q_v080_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_pct_change(_diff(opmargin, 1), 4))

# Block 80-89: std 8q
def cg_f055_margin_expansion_trajectory_core80_std_8q_v081_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_std(_diff(grossmargin, 4), 8))
def cg_f055_margin_expansion_trajectory_core81_std_8q_v082_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_std(_diff(opmargin, 4), 8))
def cg_f055_margin_expansion_trajectory_core82_std_8q_v083_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_std(_diff(ebitdamargin, 4), 8))
def cg_f055_margin_expansion_trajectory_core83_std_8q_v084_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_std(_diff(netmargin, 4), 8))
def cg_f055_margin_expansion_trajectory_core84_std_8q_v085_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_std(_diff(grossmargin, 1), 8))
def cg_f055_margin_expansion_trajectory_core85_std_8q_v086_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_std(_diff(opmargin, 1), 8))
def cg_f055_margin_expansion_trajectory_core86_std_8q_v087_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_std(_diff(opmargin, 4) - _diff(grossmargin, 4), 8))
def cg_f055_margin_expansion_trajectory_core87_std_8q_v088_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_std(_diff(netmargin, 4) - _diff(grossmargin, 4), 8))
def cg_f055_margin_expansion_trajectory_core88_std_8q_v089_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_std(_diff(_diff(grossmargin, 4), 1), 8))
def cg_f055_margin_expansion_trajectory_core89_std_8q_v090_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_std(_diff(_diff(opmargin, 4), 1), 8))

# Block 90-99: log
def cg_f055_margin_expansion_trajectory_core90_log_v091_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_log(_diff(grossmargin, 4).clip(lower=-0.9) + 1.1))
def cg_f055_margin_expansion_trajectory_core91_log_v092_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_log(_diff(opmargin, 4).clip(lower=-0.9) + 1.1))
def cg_f055_margin_expansion_trajectory_core92_log_v093_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_log(_diff(ebitdamargin, 4).clip(lower=-0.9) + 1.1))
def cg_f055_margin_expansion_trajectory_core93_log_v094_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_log(_diff(netmargin, 4).clip(lower=-0.9) + 1.1))
def cg_f055_margin_expansion_trajectory_core94_log_v095_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_log(_diff(grossmargin, 1).clip(lower=-0.9) + 1.1))
def cg_f055_margin_expansion_trajectory_core95_log_v096_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_log(_diff(opmargin, 1).clip(lower=-0.9) + 1.1))
def cg_f055_margin_expansion_trajectory_core96_log_v097_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_log((_diff(opmargin, 4) - _diff(grossmargin, 4)).clip(lower=-0.9) + 1.1))
def cg_f055_margin_expansion_trajectory_core97_log_v098_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_log((_diff(netmargin, 4) - _diff(grossmargin, 4)).clip(lower=-0.9) + 1.1))
def cg_f055_margin_expansion_trajectory_core98_log_v099_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_log(_diff(_diff(grossmargin, 4), 1).clip(lower=-0.9) + 1.1))
def cg_f055_margin_expansion_trajectory_core99_log_v100_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_log(_diff(_diff(opmargin, 4), 1).clip(lower=-0.9) + 1.1))

# Block 100-109: diff 1q
def cg_f055_margin_expansion_trajectory_core100_diff_1q_v101_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(_diff(grossmargin, 4), 1))
def cg_f055_margin_expansion_trajectory_core101_diff_1q_v102_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(_diff(opmargin, 4), 1))
def cg_f055_margin_expansion_trajectory_core102_diff_1q_v103_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(_diff(ebitdamargin, 4), 1))
def cg_f055_margin_expansion_trajectory_core103_diff_1q_v104_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(_diff(netmargin, 4), 1))
def cg_f055_margin_expansion_trajectory_core104_diff_1q_v105_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(_diff(grossmargin, 1), 1))
def cg_f055_margin_expansion_trajectory_core105_diff_1q_v106_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(_diff(opmargin, 1), 1))
def cg_f055_margin_expansion_trajectory_core106_diff_1q_v107_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(_diff(opmargin, 4) - _diff(grossmargin, 4), 1))
def cg_f055_margin_expansion_trajectory_core107_diff_1q_v108_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(_diff(netmargin, 4) - _diff(grossmargin, 4), 1))
def cg_f055_margin_expansion_trajectory_core108_diff_1q_v109_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(_diff(_diff(grossmargin, 4), 1), 1))
def cg_f055_margin_expansion_trajectory_core109_diff_1q_v110_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(_diff(_diff(opmargin, 4), 1), 1))

# Block 110-119: slope 4q
def cg_f055_margin_expansion_trajectory_core110_slope_4q_v111_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_slope(_diff(grossmargin, 4), 4))
def cg_f055_margin_expansion_trajectory_core111_slope_4q_v112_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_slope(_diff(opmargin, 4), 4))
def cg_f055_margin_expansion_trajectory_core112_slope_4q_v113_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_slope(_diff(ebitdamargin, 4), 4))
def cg_f055_margin_expansion_trajectory_core113_slope_4q_v114_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_slope(_diff(netmargin, 4), 4))
def cg_f055_margin_expansion_trajectory_core114_slope_4q_v115_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_slope(_diff(grossmargin, 1), 4))
def cg_f055_margin_expansion_trajectory_core115_slope_4q_v116_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_slope(_diff(opmargin, 1), 4))
def cg_f055_margin_expansion_trajectory_core116_slope_4q_v117_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_slope(_diff(opmargin, 4) - _diff(grossmargin, 4), 4))
def cg_f055_margin_expansion_trajectory_core117_slope_4q_v118_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_slope(_diff(netmargin, 4) - _diff(grossmargin, 4), 4))
def cg_f055_margin_expansion_trajectory_core118_slope_4q_v119_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_slope(_diff(_diff(grossmargin, 4), 1), 4))
def cg_f055_margin_expansion_trajectory_core119_slope_4q_v120_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_slope(_diff(_diff(opmargin, 4), 1), 4))

# Block 120-129: ewm 8q
def cg_f055_margin_expansion_trajectory_core120_ewm_8q_v121_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_ewm(_diff(grossmargin, 4), 8))
def cg_f055_margin_expansion_trajectory_core121_ewm_8q_v122_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_ewm(_diff(opmargin, 4), 8))
def cg_f055_margin_expansion_trajectory_core122_ewm_8q_v123_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_ewm(_diff(ebitdamargin, 4), 8))
def cg_f055_margin_expansion_trajectory_core123_ewm_8q_v124_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_ewm(_diff(netmargin, 4), 8))
def cg_f055_margin_expansion_trajectory_core124_ewm_8q_v125_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_ewm(_diff(grossmargin, 1), 8))
def cg_f055_margin_expansion_trajectory_core125_ewm_8q_v126_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_ewm(_diff(opmargin, 1), 8))
def cg_f055_margin_expansion_trajectory_core126_ewm_8q_v127_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_ewm(_diff(opmargin, 4) - _diff(grossmargin, 4), 8))
def cg_f055_margin_expansion_trajectory_core127_ewm_8q_v128_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_ewm(_diff(netmargin, 4) - _diff(grossmargin, 4), 8))
def cg_f055_margin_expansion_trajectory_core128_ewm_8q_v129_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_ewm(_diff(_diff(grossmargin, 4), 1), 8))
def cg_f055_margin_expansion_trajectory_core129_ewm_8q_v130_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_ewm(_diff(_diff(opmargin, 4), 1), 8))

# Block 130-139: stability 12q
def cg_f055_margin_expansion_trajectory_core130_stability_12q_v131_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    base = _diff(grossmargin, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f055_margin_expansion_trajectory_core131_stability_12q_v132_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    base = _diff(opmargin, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f055_margin_expansion_trajectory_core132_stability_12q_v133_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    base = _diff(ebitdamargin, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f055_margin_expansion_trajectory_core133_stability_12q_v134_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    base = _diff(netmargin, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f055_margin_expansion_trajectory_core134_stability_12q_v135_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    base = _diff(grossmargin, 1)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f055_margin_expansion_trajectory_core135_stability_12q_v136_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    base = _diff(opmargin, 1)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f055_margin_expansion_trajectory_core136_stability_12q_v137_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    base = _diff(opmargin, 4) - _diff(grossmargin, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f055_margin_expansion_trajectory_core137_stability_12q_v138_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    base = _diff(netmargin, 4) - _diff(grossmargin, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f055_margin_expansion_trajectory_core138_stability_12q_v139_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    base = _diff(_diff(grossmargin, 4), 1)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f055_margin_expansion_trajectory_core139_stability_12q_v140_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    base = _diff(_diff(opmargin, 4), 1)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f055_margin_expansion_trajectory_core140_gm_diff_v141_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(grossmargin, 4))
def cg_f055_margin_expansion_trajectory_core141_om_diff_v142_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(opmargin, 4))
def cg_f055_margin_expansion_trajectory_core142_ebitdam_diff_v143_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(ebitdamargin, 4))
def cg_f055_margin_expansion_trajectory_core143_nm_diff_v144_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(netmargin, 4))
def cg_f055_margin_expansion_trajectory_core144_gm_accel_v145_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(_diff(grossmargin, 4), 1))
def cg_f055_margin_expansion_trajectory_core145_om_accel_v146_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(_diff(opmargin, 4), 1))
def cg_f055_margin_expansion_trajectory_core146_op_leverage_v147_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(opmargin, 4) - _diff(grossmargin, 4))
def cg_f055_margin_expansion_trajectory_core147_net_leverage_v148_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_diff(netmargin, 4) - _diff(grossmargin, 4))
def cg_f055_margin_expansion_trajectory_core148_om_to_gm_v149_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_safe_div(opmargin, grossmargin.abs() + 1e-9))
def cg_f055_margin_expansion_trajectory_core149_nm_to_om_v150_signal(grossmargin, opmargin, netmargin, ebitdamargin, revenue, assets, opex, equity):
    return _clean(_safe_div(netmargin, opmargin.abs() + 1e-9))
