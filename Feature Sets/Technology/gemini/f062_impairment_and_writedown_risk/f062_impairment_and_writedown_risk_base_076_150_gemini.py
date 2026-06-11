import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f062_impairment_and_writedown_risk_core75_pct_4q_v076_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(opex, 4))
def cg_f062_impairment_and_writedown_risk_core76_pct_4q_v077_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(_safe_div(opex, assets), 4))
def cg_f062_impairment_and_writedown_risk_core77_pct_4q_v078_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(_safe_div(intangibles + depamor, assets), 4))
def cg_f062_impairment_and_writedown_risk_core78_pct_4q_v079_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(_safe_div(intangibles, opex.abs() + 1.0), 4))
def cg_f062_impairment_and_writedown_risk_core79_pct_4q_v080_signal(intangibles, depamor, assets, opex):
    return _clean(_pct_change(_safe_div(depamor, intangibles.abs() + 1.0), 4))

# core80-89: std 8q
def cg_f062_impairment_and_writedown_risk_core80_std_8q_v081_signal(intangibles, depamor, assets, opex):
    return _clean(_std(intangibles, 8))
def cg_f062_impairment_and_writedown_risk_core81_std_8q_v082_signal(intangibles, depamor, assets, opex):
    return _clean(_std(_safe_div(intangibles, assets), 8))
def cg_f062_impairment_and_writedown_risk_core82_std_8q_v083_signal(intangibles, depamor, assets, opex):
    return _clean(_std(depamor, 8))
def cg_f062_impairment_and_writedown_risk_core83_std_8q_v084_signal(intangibles, depamor, assets, opex):
    return _clean(_std(_safe_div(depamor, opex.abs() + 1.0), 8))
def cg_f062_impairment_and_writedown_risk_core84_std_8q_v085_signal(intangibles, depamor, assets, opex):
    return _clean(_std(_safe_div(depamor, assets), 8))
def cg_f062_impairment_and_writedown_risk_core85_std_8q_v086_signal(intangibles, depamor, assets, opex):
    return _clean(_std(opex, 8))
def cg_f062_impairment_and_writedown_risk_core86_std_8q_v087_signal(intangibles, depamor, assets, opex):
    return _clean(_std(_safe_div(opex, assets), 8))
def cg_f062_impairment_and_writedown_risk_core87_std_8q_v088_signal(intangibles, depamor, assets, opex):
    return _clean(_std(_safe_div(intangibles + depamor, assets), 8))
def cg_f062_impairment_and_writedown_risk_core88_std_8q_v089_signal(intangibles, depamor, assets, opex):
    return _clean(_std(_safe_div(intangibles, opex.abs() + 1.0), 8))
def cg_f062_impairment_and_writedown_risk_core89_std_8q_v090_signal(intangibles, depamor, assets, opex):
    return _clean(_std(_safe_div(depamor, intangibles.abs() + 1.0), 8))

# core90-99: log
def cg_f062_impairment_and_writedown_risk_core90_log_v091_signal(intangibles, depamor, assets, opex):
    return _clean(_log(intangibles.abs() + 1.0))
def cg_f062_impairment_and_writedown_risk_core91_log_v092_signal(intangibles, depamor, assets, opex):
    return _clean(_log(_safe_div(intangibles, assets).abs() + 1.0))
def cg_f062_impairment_and_writedown_risk_core92_log_v093_signal(intangibles, depamor, assets, opex):
    return _clean(_log(depamor.abs() + 1.0))
def cg_f062_impairment_and_writedown_risk_core93_log_v094_signal(intangibles, depamor, assets, opex):
    return _clean(_log(_safe_div(depamor, opex.abs() + 1.0).abs() + 1.0))
def cg_f062_impairment_and_writedown_risk_core94_log_v095_signal(intangibles, depamor, assets, opex):
    return _clean(_log(_safe_div(depamor, assets).abs() + 1.0))
def cg_f062_impairment_and_writedown_risk_core95_log_v096_signal(intangibles, depamor, assets, opex):
    return _clean(_log(opex.abs() + 1.0))
def cg_f062_impairment_and_writedown_risk_core96_log_v097_signal(intangibles, depamor, assets, opex):
    return _clean(_log(_safe_div(opex, assets).abs() + 1.0))
def cg_f062_impairment_and_writedown_risk_core97_log_v098_signal(intangibles, depamor, assets, opex):
    return _clean(_log(_safe_div(intangibles + depamor, assets).abs() + 1.0))
def cg_f062_impairment_and_writedown_risk_core98_log_v099_signal(intangibles, depamor, assets, opex):
    return _clean(_log(_safe_div(intangibles, opex.abs() + 1.0).abs() + 1.0))
def cg_f062_impairment_and_writedown_risk_core99_log_v100_signal(intangibles, depamor, assets, opex):
    return _clean(_log(_safe_div(depamor, intangibles.abs() + 1.0).abs() + 1.0))

# core100-109: diff 1q
def cg_f062_impairment_and_writedown_risk_core100_diff_1q_v101_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(intangibles, 1))
def cg_f062_impairment_and_writedown_risk_core101_diff_1q_v102_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_safe_div(intangibles, assets), 1))
def cg_f062_impairment_and_writedown_risk_core102_diff_1q_v103_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(depamor, 1))
def cg_f062_impairment_and_writedown_risk_core103_diff_1q_v104_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_safe_div(depamor, opex.abs() + 1.0), 1))
def cg_f062_impairment_and_writedown_risk_core104_diff_1q_v105_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_safe_div(depamor, assets), 1))
def cg_f062_impairment_and_writedown_risk_core105_diff_1q_v106_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(opex, 1))
def cg_f062_impairment_and_writedown_risk_core106_diff_1q_v107_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_safe_div(opex, assets), 1))
def cg_f062_impairment_and_writedown_risk_core107_diff_1q_v108_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_safe_div(intangibles + depamor, assets), 1))
def cg_f062_impairment_and_writedown_risk_core108_diff_1q_v109_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_safe_div(intangibles, opex.abs() + 1.0), 1))
def cg_f062_impairment_and_writedown_risk_core109_diff_1q_v110_signal(intangibles, depamor, assets, opex):
    return _clean(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 1))

# core110-119: slope 4q
def cg_f062_impairment_and_writedown_risk_core110_slope_4q_v111_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(intangibles, 4))
def cg_f062_impairment_and_writedown_risk_core111_slope_4q_v112_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_safe_div(intangibles, assets), 4))
def cg_f062_impairment_and_writedown_risk_core112_slope_4q_v113_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(depamor, 4))
def cg_f062_impairment_and_writedown_risk_core113_slope_4q_v114_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_safe_div(depamor, opex.abs() + 1.0), 4))
def cg_f062_impairment_and_writedown_risk_core114_slope_4q_v115_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_safe_div(depamor, assets), 4))
def cg_f062_impairment_and_writedown_risk_core115_slope_4q_v116_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(opex, 4))
def cg_f062_impairment_and_writedown_risk_core116_slope_4q_v117_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_safe_div(opex, assets), 4))
def cg_f062_impairment_and_writedown_risk_core117_slope_4q_v118_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_safe_div(intangibles + depamor, assets), 4))
def cg_f062_impairment_and_writedown_risk_core118_slope_4q_v119_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_safe_div(intangibles, opex.abs() + 1.0), 4))
def cg_f062_impairment_and_writedown_risk_core119_slope_4q_v120_signal(intangibles, depamor, assets, opex):
    return _clean(_slope(_safe_div(depamor, intangibles.abs() + 1.0), 4))

# core120-129: ewm 8q
def cg_f062_impairment_and_writedown_risk_core120_ewm_8q_v121_signal(intangibles, depamor, assets, opex):
    return _clean(_ewm(intangibles, 8))
def cg_f062_impairment_and_writedown_risk_core121_ewm_8q_v122_signal(intangibles, depamor, assets, opex):
    return _clean(_ewm(_safe_div(intangibles, assets), 8))
def cg_f062_impairment_and_writedown_risk_core122_ewm_8q_v123_signal(intangibles, depamor, assets, opex):
    return _clean(_ewm(depamor, 8))
def cg_f062_impairment_and_writedown_risk_core123_ewm_8q_v124_signal(intangibles, depamor, assets, opex):
    return _clean(_ewm(_safe_div(depamor, opex.abs() + 1.0), 8))
def cg_f062_impairment_and_writedown_risk_core124_ewm_8q_v125_signal(intangibles, depamor, assets, opex):
    return _clean(_ewm(_safe_div(depamor, assets), 8))
def cg_f062_impairment_and_writedown_risk_core125_ewm_8q_v126_signal(intangibles, depamor, assets, opex):
    return _clean(_ewm(opex, 8))
def cg_f062_impairment_and_writedown_risk_core126_ewm_8q_v127_signal(intangibles, depamor, assets, opex):
    return _clean(_ewm(_safe_div(opex, assets), 8))
def cg_f062_impairment_and_writedown_risk_core127_ewm_8q_v128_signal(intangibles, depamor, assets, opex):
    return _clean(_ewm(_safe_div(intangibles + depamor, assets), 8))
def cg_f062_impairment_and_writedown_risk_core128_ewm_8q_v129_signal(intangibles, depamor, assets, opex):
    return _clean(_ewm(_safe_div(intangibles, opex.abs() + 1.0), 8))
def cg_f062_impairment_and_writedown_risk_core129_ewm_8q_v130_signal(intangibles, depamor, assets, opex):
    return _clean(_ewm(_safe_div(depamor, intangibles.abs() + 1.0), 8))

# core130-139: stability 12q
def cg_f062_impairment_and_writedown_risk_core130_stability_12q_v131_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(_std(intangibles, 12), _mean(intangibles, 12)))
def cg_f062_impairment_and_writedown_risk_core131_stability_12q_v132_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(_std(_safe_div(intangibles, assets), 12), _mean(_safe_div(intangibles, assets), 12)))
def cg_f062_impairment_and_writedown_risk_core132_stability_12q_v133_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(_std(depamor, 12), _mean(depamor, 12)))
def cg_f062_impairment_and_writedown_risk_core133_stability_12q_v134_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(_std(_safe_div(depamor, opex.abs() + 1.0), 12), _mean(_safe_div(depamor, opex.abs() + 1.0), 12)))
def cg_f062_impairment_and_writedown_risk_core134_stability_12q_v135_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(_std(_safe_div(depamor, assets), 12), _mean(_safe_div(depamor, assets), 12)))
def cg_f062_impairment_and_writedown_risk_core135_stability_12q_v136_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(_std(opex, 12), _mean(opex, 12)))
def cg_f062_impairment_and_writedown_risk_core136_stability_12q_v137_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(_std(_safe_div(opex, assets), 12), _mean(_safe_div(opex, assets), 12)))
def cg_f062_impairment_and_writedown_risk_core137_stability_12q_v138_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(_std(_safe_div(intangibles + depamor, assets), 12), _mean(_safe_div(intangibles + depamor, assets), 12)))
def cg_f062_impairment_and_writedown_risk_core138_stability_12q_v139_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(_std(_safe_div(intangibles, opex.abs() + 1.0), 12), _mean(_safe_div(intangibles, opex.abs() + 1.0), 12)))
def cg_f062_impairment_and_writedown_risk_core139_stability_12q_v140_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(_std(_safe_div(depamor, intangibles.abs() + 1.0), 12), _mean(_safe_div(depamor, intangibles.abs() + 1.0), 12)))

# core140-149: raw variations
def cg_f062_impairment_and_writedown_risk_core140_raw_v141_signal(intangibles, depamor, assets, opex):
    return _clean(intangibles)
def cg_f062_impairment_and_writedown_risk_core141_raw_v142_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(intangibles, assets))
def cg_f062_impairment_and_writedown_risk_core142_raw_v143_signal(intangibles, depamor, assets, opex):
    return _clean(depamor)
def cg_f062_impairment_and_writedown_risk_core143_raw_v144_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(depamor, opex.abs() + 1.0))
def cg_f062_impairment_and_writedown_risk_core144_raw_v145_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(depamor, assets))
def cg_f062_impairment_and_writedown_risk_core145_raw_v146_signal(intangibles, depamor, assets, opex):
    return _clean(opex)
def cg_f062_impairment_and_writedown_risk_core146_raw_v147_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(opex, assets))
def cg_f062_impairment_and_writedown_risk_core147_raw_v148_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(intangibles + depamor, assets))
def cg_f062_impairment_and_writedown_risk_core148_raw_v149_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(intangibles, opex.abs() + 1.0))
def cg_f062_impairment_and_writedown_risk_core149_raw_v150_signal(intangibles, depamor, assets, opex):
    return _clean(_safe_div(depamor, intangibles.abs() + 1.0))
