import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f073_earnings_multiples_core75_pct_4q_v076_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(_safe_div(pe, evebitda.abs() + 1.0), 4))
def cg_f073_earnings_multiples_core76_pct_4q_v077_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(pe - evebitda, 4))
def cg_f073_earnings_multiples_core77_pct_4q_v078_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(ebitda - ebit, 4))
def cg_f073_earnings_multiples_core78_pct_4q_v079_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(_safe_div(pe, ebit.abs() + 1.0), 4))
def cg_f073_earnings_multiples_core79_pct_4q_v080_signal(pe, evebitda, ebit, ebitda):
    return _clean(_pct_change(_safe_div(evebitda, ebitda.abs() + 1.0), 4))

# core80-89: std 8q
def cg_f073_earnings_multiples_core80_std_8q_v081_signal(pe, evebitda, ebit, ebitda):
    return _clean(_std(pe, 8))
def cg_f073_earnings_multiples_core81_std_8q_v082_signal(pe, evebitda, ebit, ebitda):
    return _clean(_std(evebitda, 8))
def cg_f073_earnings_multiples_core82_std_8q_v083_signal(pe, evebitda, ebit, ebitda):
    return _clean(_std(ebit, 8))
def cg_f073_earnings_multiples_core83_std_8q_v084_signal(pe, evebitda, ebit, ebitda):
    return _clean(_std(ebitda, 8))
def cg_f073_earnings_multiples_core84_std_8q_v085_signal(pe, evebitda, ebit, ebitda):
    return _clean(_std(_safe_div(ebit, ebitda), 8))
def cg_f073_earnings_multiples_core85_std_8q_v086_signal(pe, evebitda, ebit, ebitda):
    return _clean(_std(_safe_div(pe, evebitda.abs() + 1.0), 8))
def cg_f073_earnings_multiples_core86_std_8q_v087_signal(pe, evebitda, ebit, ebitda):
    return _clean(_std(pe - evebitda, 8))
def cg_f073_earnings_multiples_core87_std_8q_v088_signal(pe, evebitda, ebit, ebitda):
    return _clean(_std(ebitda - ebit, 8))
def cg_f073_earnings_multiples_core88_std_8q_v089_signal(pe, evebitda, ebit, ebitda):
    return _clean(_std(_safe_div(pe, ebit.abs() + 1.0), 8))
def cg_f073_earnings_multiples_core89_std_8q_v090_signal(pe, evebitda, ebit, ebitda):
    return _clean(_std(_safe_div(evebitda, ebitda.abs() + 1.0), 8))

# core90-99: log
def cg_f073_earnings_multiples_core90_log_v091_signal(pe, evebitda, ebit, ebitda):
    return _clean(_log(pe.clip(lower=1.0)))
def cg_f073_earnings_multiples_core91_log_v092_signal(pe, evebitda, ebit, ebitda):
    return _clean(_log(evebitda.clip(lower=1.0)))
def cg_f073_earnings_multiples_core92_log_v093_signal(pe, evebitda, ebit, ebitda):
    return _clean(_log(ebit.clip(lower=1.0)))
def cg_f073_earnings_multiples_core93_log_v094_signal(pe, evebitda, ebit, ebitda):
    return _clean(_log(ebitda.clip(lower=1.0)))
def cg_f073_earnings_multiples_core94_log_v095_signal(pe, evebitda, ebit, ebitda):
    return _clean(_log(_safe_div(ebit, ebitda).clip(lower=0.001)))
def cg_f073_earnings_multiples_core95_log_v096_signal(pe, evebitda, ebit, ebitda):
    return _clean(_log(_safe_div(pe, evebitda.abs() + 1.0).clip(lower=0.001)))
def cg_f073_earnings_multiples_core96_log_v097_signal(pe, evebitda, ebit, ebitda):
    return _clean(_log((pe - evebitda).clip(lower=1.0)))
def cg_f073_earnings_multiples_core97_log_v098_signal(pe, evebitda, ebit, ebitda):
    return _clean(_log((ebitda - ebit).clip(lower=1.0)))
def cg_f073_earnings_multiples_core98_log_v099_signal(pe, evebitda, ebit, ebitda):
    return _clean(_log(_safe_div(pe, ebit.abs() + 1.0).clip(lower=0.001)))
def cg_f073_earnings_multiples_core99_log_v100_signal(pe, evebitda, ebit, ebitda):
    return _clean(_log(_safe_div(evebitda, ebitda.abs() + 1.0).clip(lower=0.001)))

# core100-109: diff 1q
def cg_f073_earnings_multiples_core100_diff_1q_v101_signal(pe, evebitda, ebit, ebitda):
    return _clean(_diff(pe, 1))
def cg_f073_earnings_multiples_core101_diff_1q_v102_signal(pe, evebitda, ebit, ebitda):
    return _clean(_diff(evebitda, 1))
def cg_f073_earnings_multiples_core102_diff_1q_v103_signal(pe, evebitda, ebit, ebitda):
    return _clean(_diff(ebit, 1))
def cg_f073_earnings_multiples_core103_diff_1q_v104_signal(pe, evebitda, ebit, ebitda):
    return _clean(_diff(ebitda, 1))
def cg_f073_earnings_multiples_core104_diff_1q_v105_signal(pe, evebitda, ebit, ebitda):
    return _clean(_diff(_safe_div(ebit, ebitda), 1))
def cg_f073_earnings_multiples_core105_diff_1q_v106_signal(pe, evebitda, ebit, ebitda):
    return _clean(_diff(_safe_div(pe, evebitda.abs() + 1.0), 1))
def cg_f073_earnings_multiples_core106_diff_1q_v107_signal(pe, evebitda, ebit, ebitda):
    return _clean(_diff(pe - evebitda, 1))
def cg_f073_earnings_multiples_core107_diff_1q_v108_signal(pe, evebitda, ebit, ebitda):
    return _clean(_diff(ebitda - ebit, 1))
def cg_f073_earnings_multiples_core108_diff_1q_v109_signal(pe, evebitda, ebit, ebitda):
    return _clean(_diff(_safe_div(pe, ebit.abs() + 1.0), 1))
def cg_f073_earnings_multiples_core109_diff_1q_v110_signal(pe, evebitda, ebit, ebitda):
    return _clean(_diff(_safe_div(evebitda, ebitda.abs() + 1.0), 1))

# core110-119: slope 4q
def cg_f073_earnings_multiples_core110_slope_4q_v111_signal(pe, evebitda, ebit, ebitda):
    return _clean(_slope(pe, 4))
def cg_f073_earnings_multiples_core111_slope_4q_v112_signal(pe, evebitda, ebit, ebitda):
    return _clean(_slope(evebitda, 4))
def cg_f073_earnings_multiples_core112_slope_4q_v113_signal(pe, evebitda, ebit, ebitda):
    return _clean(_slope(ebit, 4))
def cg_f073_earnings_multiples_core113_slope_4q_v114_signal(pe, evebitda, ebit, ebitda):
    return _clean(_slope(ebitda, 4))
def cg_f073_earnings_multiples_core114_slope_4q_v115_signal(pe, evebitda, ebit, ebitda):
    return _clean(_slope(_safe_div(ebit, ebitda), 4))
def cg_f073_earnings_multiples_core115_slope_4q_v116_signal(pe, evebitda, ebit, ebitda):
    return _clean(_slope(_safe_div(pe, evebitda.abs() + 1.0), 4))
def cg_f073_earnings_multiples_core116_slope_4q_v117_signal(pe, evebitda, ebit, ebitda):
    return _clean(_slope(pe - evebitda, 4))
def cg_f073_earnings_multiples_core117_slope_4q_v118_signal(pe, evebitda, ebit, ebitda):
    return _clean(_slope(ebitda - ebit, 4))
def cg_f073_earnings_multiples_core118_slope_4q_v119_signal(pe, evebitda, ebit, ebitda):
    return _clean(_slope(_safe_div(pe, ebit.abs() + 1.0), 4))
def cg_f073_earnings_multiples_core119_slope_4q_v120_signal(pe, evebitda, ebit, ebitda):
    return _clean(_slope(_safe_div(evebitda, ebitda.abs() + 1.0), 4))

# core120-129: ewm 8q
def cg_f073_earnings_multiples_core120_ewm_8q_v121_signal(pe, evebitda, ebit, ebitda):
    return _clean(_ewm(pe, 8))
def cg_f073_earnings_multiples_core121_ewm_8q_v122_signal(pe, evebitda, ebit, ebitda):
    return _clean(_ewm(evebitda, 8))
def cg_f073_earnings_multiples_core122_ewm_8q_v123_signal(pe, evebitda, ebit, ebitda):
    return _clean(_ewm(ebit, 8))
def cg_f073_earnings_multiples_core123_ewm_8q_v124_signal(pe, evebitda, ebit, ebitda):
    return _clean(_ewm(ebitda, 8))
def cg_f073_earnings_multiples_core124_ewm_8q_v125_signal(pe, evebitda, ebit, ebitda):
    return _clean(_ewm(_safe_div(ebit, ebitda), 8))
def cg_f073_earnings_multiples_core125_ewm_8q_v126_signal(pe, evebitda, ebit, ebitda):
    return _clean(_ewm(_safe_div(pe, evebitda.abs() + 1.0), 8))
def cg_f073_earnings_multiples_core126_ewm_8q_v127_signal(pe, evebitda, ebit, ebitda):
    return _clean(_ewm(pe - evebitda, 8))
def cg_f073_earnings_multiples_core127_ewm_8q_v128_signal(pe, evebitda, ebit, ebitda):
    return _clean(_ewm(ebitda - ebit, 8))
def cg_f073_earnings_multiples_core128_ewm_8q_v129_signal(pe, evebitda, ebit, ebitda):
    return _clean(_ewm(_safe_div(pe, ebit.abs() + 1.0), 8))
def cg_f073_earnings_multiples_core129_ewm_8q_v130_signal(pe, evebitda, ebit, ebitda):
    return _clean(_ewm(_safe_div(evebitda, ebitda.abs() + 1.0), 8))

# core130-139: stability 12q
def cg_f073_earnings_multiples_core130_stability_12q_v131_signal(pe, evebitda, ebit, ebitda):
    return _clean(_safe_div(_std(pe, 12), _mean(pe, 12)))
def cg_f073_earnings_multiples_core131_stability_12q_v132_signal(pe, evebitda, ebit, ebitda):
    base = evebitda
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f073_earnings_multiples_core132_stability_12q_v133_signal(pe, evebitda, ebit, ebitda):
    base = ebit
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f073_earnings_multiples_core133_stability_12q_v134_signal(pe, evebitda, ebit, ebitda):
    base = ebitda
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f073_earnings_multiples_core134_stability_12q_v135_signal(pe, evebitda, ebit, ebitda):
    base = _safe_div(ebit, ebitda)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f073_earnings_multiples_core135_stability_12q_v136_signal(pe, evebitda, ebit, ebitda):
    base = _safe_div(pe, evebitda.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f073_earnings_multiples_core136_stability_12q_v137_signal(pe, evebitda, ebit, ebitda):
    base = pe - evebitda
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f073_earnings_multiples_core137_stability_12q_v138_signal(pe, evebitda, ebit, ebitda):
    base = ebitda - ebit
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f073_earnings_multiples_core138_stability_12q_v139_signal(pe, evebitda, ebit, ebitda):
    base = _safe_div(pe, ebit.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f073_earnings_multiples_core139_stability_12q_v140_signal(pe, evebitda, ebit, ebitda):
    base = _safe_div(evebitda, ebitda.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))

# core140-149: level
def cg_f073_earnings_multiples_core140_pe_v141_signal(pe, evebitda, ebit, ebitda):
    return _clean(pe)
def cg_f073_earnings_multiples_core141_evebitda_v142_signal(pe, evebitda, ebit, ebitda):
    return _clean(evebitda)
def cg_f073_earnings_multiples_core142_ebit_v143_signal(pe, evebitda, ebit, ebitda):
    return _clean(ebit)
def cg_f073_earnings_multiples_core143_ebitda_v144_signal(pe, evebitda, ebit, ebitda):
    return _clean(ebitda)
def cg_f073_earnings_multiples_core144_ebit_ebitda_v145_signal(pe, evebitda, ebit, ebitda):
    return _clean(_safe_div(ebit, ebitda))
def cg_f073_earnings_multiples_core145_pe_evebitda_v146_signal(pe, evebitda, ebit, ebitda):
    return _clean(_safe_div(pe, evebitda.abs() + 1.0))
def cg_f073_earnings_multiples_core146_pe_minus_evebitda_v147_signal(pe, evebitda, ebit, ebitda):
    return _clean(pe - evebitda)
def cg_f073_earnings_multiples_core147_ebitda_minus_ebit_v148_signal(pe, evebitda, ebit, ebitda):
    return _clean(ebitda - ebit)
def cg_f073_earnings_multiples_core148_pe_to_ebit_v149_signal(pe, evebitda, ebit, ebitda):
    return _clean(_safe_div(pe, ebit.abs() + 1.0))
def cg_f073_earnings_multiples_core149_evebitda_to_ebitda_v150_signal(pe, evebitda, ebit, ebitda):
    return _clean(_safe_div(evebitda, ebitda.abs() + 1.0))
