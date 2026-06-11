import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f061_tax_rate_and_geography_core75_pct_4q_v076_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core76_pct_4q_v077_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(_safe_div(taxassets, ebt.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core77_pct_4q_v078_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(taxliabilities, 4))
def cg_f061_tax_rate_and_geography_core78_pct_4q_v079_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(_safe_div(taxliabilities, ebt.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core79_pct_4q_v080_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_pct_change(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0), 4))

# core80-89: std 8q
def cg_f061_tax_rate_and_geography_core80_std_8q_v081_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_std(taxexp, 8))
def cg_f061_tax_rate_and_geography_core81_std_8q_v082_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_std(_safe_div(taxexp, ebt), 8))
def cg_f061_tax_rate_and_geography_core82_std_8q_v083_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_std(_safe_div(taxexp, taxassets.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core83_std_8q_v084_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_std(_safe_div(taxexp, taxliabilities.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core84_std_8q_v085_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_std(taxassets, 8))
def cg_f061_tax_rate_and_geography_core85_std_8q_v086_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_std(_safe_div(taxassets, taxliabilities.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core86_std_8q_v087_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_std(_safe_div(taxassets, ebt.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core87_std_8q_v088_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_std(taxliabilities, 8))
def cg_f061_tax_rate_and_geography_core88_std_8q_v089_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_std(_safe_div(taxliabilities, ebt.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core89_std_8q_v090_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_std(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0), 8))

# core90-99: log
def cg_f061_tax_rate_and_geography_core90_log_v091_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_log(taxexp.abs() + 1.0))
def cg_f061_tax_rate_and_geography_core91_log_v092_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_log(_safe_div(taxexp, ebt).abs() + 1.0))
def cg_f061_tax_rate_and_geography_core92_log_v093_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_log(_safe_div(taxexp, taxassets.abs() + 1.0).abs() + 1.0))
def cg_f061_tax_rate_and_geography_core93_log_v094_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_log(_safe_div(taxexp, taxliabilities.abs() + 1.0).abs() + 1.0))
def cg_f061_tax_rate_and_geography_core94_log_v095_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_log(taxassets.abs() + 1.0))
def cg_f061_tax_rate_and_geography_core95_log_v096_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_log(_safe_div(taxassets, taxliabilities.abs() + 1.0).abs() + 1.0))
def cg_f061_tax_rate_and_geography_core96_log_v097_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_log(_safe_div(taxassets, ebt.abs() + 1.0).abs() + 1.0))
def cg_f061_tax_rate_and_geography_core97_log_v098_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_log(taxliabilities.abs() + 1.0))
def cg_f061_tax_rate_and_geography_core98_log_v099_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_log(_safe_div(taxliabilities, ebt.abs() + 1.0).abs() + 1.0))
def cg_f061_tax_rate_and_geography_core99_log_v100_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_log(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0).abs() + 1.0))

# core100-109: diff 1q
def cg_f061_tax_rate_and_geography_core100_diff_1q_v101_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(taxexp, 1))
def cg_f061_tax_rate_and_geography_core101_diff_1q_v102_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_safe_div(taxexp, ebt), 1))
def cg_f061_tax_rate_and_geography_core102_diff_1q_v103_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_safe_div(taxexp, taxassets.abs() + 1.0), 1))
def cg_f061_tax_rate_and_geography_core103_diff_1q_v104_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_safe_div(taxexp, taxliabilities.abs() + 1.0), 1))
def cg_f061_tax_rate_and_geography_core104_diff_1q_v105_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(taxassets, 1))
def cg_f061_tax_rate_and_geography_core105_diff_1q_v106_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 1))
def cg_f061_tax_rate_and_geography_core106_diff_1q_v107_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_safe_div(taxassets, ebt.abs() + 1.0), 1))
def cg_f061_tax_rate_and_geography_core107_diff_1q_v108_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(taxliabilities, 1))
def cg_f061_tax_rate_and_geography_core108_diff_1q_v109_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_safe_div(taxliabilities, ebt.abs() + 1.0), 1))
def cg_f061_tax_rate_and_geography_core109_diff_1q_v110_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0), 1))

# core110-119: slope 4q
def cg_f061_tax_rate_and_geography_core110_slope_4q_v111_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(taxexp, 4))
def cg_f061_tax_rate_and_geography_core111_slope_4q_v112_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_safe_div(taxexp, ebt), 4))
def cg_f061_tax_rate_and_geography_core112_slope_4q_v113_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_safe_div(taxexp, taxassets.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core113_slope_4q_v114_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_safe_div(taxexp, taxliabilities.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core114_slope_4q_v115_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(taxassets, 4))
def cg_f061_tax_rate_and_geography_core115_slope_4q_v116_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core116_slope_4q_v117_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_safe_div(taxassets, ebt.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core117_slope_4q_v118_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(taxliabilities, 4))
def cg_f061_tax_rate_and_geography_core118_slope_4q_v119_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_safe_div(taxliabilities, ebt.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core119_slope_4q_v120_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0), 4))

# core120-129: ewm 8q
def cg_f061_tax_rate_and_geography_core120_ewm_8q_v121_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_ewm(taxexp, 8))
def cg_f061_tax_rate_and_geography_core121_ewm_8q_v122_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_ewm(_safe_div(taxexp, ebt), 8))
def cg_f061_tax_rate_and_geography_core122_ewm_8q_v123_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_ewm(_safe_div(taxexp, taxassets.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core123_ewm_8q_v124_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_ewm(_safe_div(taxexp, taxliabilities.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core124_ewm_8q_v125_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_ewm(taxassets, 8))
def cg_f061_tax_rate_and_geography_core125_ewm_8q_v126_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_ewm(_safe_div(taxassets, taxliabilities.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core126_ewm_8q_v127_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_ewm(_safe_div(taxassets, ebt.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core127_ewm_8q_v128_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_ewm(taxliabilities, 8))
def cg_f061_tax_rate_and_geography_core128_ewm_8q_v129_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_ewm(_safe_div(taxliabilities, ebt.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core129_ewm_8q_v130_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_ewm(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0), 8))

# core130-139: stability 12q
def cg_f061_tax_rate_and_geography_core130_stability_12q_v131_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(_std(taxexp, 12), _mean(taxexp, 12)))
def cg_f061_tax_rate_and_geography_core131_stability_12q_v132_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(_std(_safe_div(taxexp, ebt), 12), _mean(_safe_div(taxexp, ebt), 12)))
def cg_f061_tax_rate_and_geography_core132_stability_12q_v133_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(_std(_safe_div(taxexp, taxassets.abs() + 1.0), 12), _mean(_safe_div(taxexp, taxassets.abs() + 1.0), 12)))
def cg_f061_tax_rate_and_geography_core133_stability_12q_v134_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(_std(_safe_div(taxexp, taxliabilities.abs() + 1.0), 12), _mean(_safe_div(taxexp, taxliabilities.abs() + 1.0), 12)))
def cg_f061_tax_rate_and_geography_core134_stability_12q_v135_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(_std(taxassets, 12), _mean(taxassets, 12)))
def cg_f061_tax_rate_and_geography_core135_stability_12q_v136_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(_std(_safe_div(taxassets, taxliabilities.abs() + 1.0), 12), _mean(_safe_div(taxassets, taxliabilities.abs() + 1.0), 12)))
def cg_f061_tax_rate_and_geography_core136_stability_12q_v137_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(_std(_safe_div(taxassets, ebt.abs() + 1.0), 12), _mean(_safe_div(taxassets, ebt.abs() + 1.0), 12)))
def cg_f061_tax_rate_and_geography_core137_stability_12q_v138_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(_std(taxliabilities, 12), _mean(taxliabilities, 12)))
def cg_f061_tax_rate_and_geography_core138_stability_12q_v139_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(_std(_safe_div(taxliabilities, ebt.abs() + 1.0), 12), _mean(_safe_div(taxliabilities, ebt.abs() + 1.0), 12)))
def cg_f061_tax_rate_and_geography_core139_stability_12q_v140_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(_std(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0), 12), _mean(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0), 12)))

# core140-149: raw variations
def cg_f061_tax_rate_and_geography_core140_raw_v141_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(taxexp)
def cg_f061_tax_rate_and_geography_core141_raw_v142_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(taxexp, ebt))
def cg_f061_tax_rate_and_geography_core142_raw_v143_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(taxexp, taxassets.abs() + 1.0))
def cg_f061_tax_rate_and_geography_core143_raw_v144_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(taxexp, taxliabilities.abs() + 1.0))
def cg_f061_tax_rate_and_geography_core144_raw_v145_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(taxassets)
def cg_f061_tax_rate_and_geography_core145_raw_v146_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(taxassets, taxliabilities.abs() + 1.0))
def cg_f061_tax_rate_and_geography_core146_raw_v147_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(taxassets, ebt.abs() + 1.0))
def cg_f061_tax_rate_and_geography_core147_raw_v148_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(taxliabilities)
def cg_f061_tax_rate_and_geography_core148_raw_v149_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(taxliabilities, ebt.abs() + 1.0))
def cg_f061_tax_rate_and_geography_core149_raw_v150_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_safe_div(taxexp, (taxassets + taxliabilities).abs() + 1.0))
