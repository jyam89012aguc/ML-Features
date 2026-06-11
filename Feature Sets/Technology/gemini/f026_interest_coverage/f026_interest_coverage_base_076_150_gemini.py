import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f026_interest_coverage_core75_pct_4q_v076_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(netinc, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core76_pct_4q_v077_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(revenue, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core77_pct_4q_v078_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(ebitda - capex.abs(), intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core78_pct_4q_v079_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(debtt.abs(), intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core79_pct_4q_v080_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_log(_safe_div(ebitda, intexp.abs() + 1.0).clip(lower=0.1)), 4))

# Block 80-89: std 8q
def cg_f026_interest_coverage_core80_std_8q_v081_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_std(_safe_div(opinc, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core81_std_8q_v082_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_std(_safe_div(ebitda, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core82_std_8q_v083_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_std(_safe_div(ncfo, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core83_std_8q_v084_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_std(_safe_div(fcf, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core84_std_8q_v085_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_std(_safe_div(opinc + sbc, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core85_std_8q_v086_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_std(_safe_div(netinc, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core86_std_8q_v087_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_std(_safe_div(revenue, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core87_std_8q_v088_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_std(_safe_div(ebitda - capex.abs(), intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core88_std_8q_v089_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_std(_safe_div(debtt.abs(), intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core89_std_8q_v090_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_std(_log(_safe_div(ebitda, intexp.abs() + 1.0).clip(lower=0.1)), 8))

# Block 90-99: log
def cg_f026_interest_coverage_core90_log_v091_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_log(_safe_div(opinc, intexp.abs() + 1.0).clip(lower=0.1)))
def cg_f026_interest_coverage_core91_log_v092_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_log(_safe_div(ebitda, intexp.abs() + 1.0).clip(lower=0.1)))
def cg_f026_interest_coverage_core92_log_v093_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_log(_safe_div(ncfo, intexp.abs() + 1.0).clip(lower=0.1)))
def cg_f026_interest_coverage_core93_log_v094_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_log(_safe_div(fcf, intexp.abs() + 1.0).clip(lower=0.1)))
def cg_f026_interest_coverage_core94_log_v095_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_log(_safe_div(opinc + sbc, intexp.abs() + 1.0).clip(lower=0.1)))
def cg_f026_interest_coverage_core95_log_v096_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_log(_safe_div(netinc, intexp.abs() + 1.0).clip(lower=0.1)))
def cg_f026_interest_coverage_core96_log_v097_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_log(_safe_div(revenue, intexp.abs() + 1.0).clip(lower=0.1)))
def cg_f026_interest_coverage_core97_log_v098_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_log(_safe_div(ebitda - capex.abs(), intexp.abs() + 1.0).clip(lower=0.1)))
def cg_f026_interest_coverage_core98_log_v099_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_log(_safe_div(debtt.abs(), intexp.abs() + 1.0).clip(lower=0.1)))
def cg_f026_interest_coverage_core99_log_v100_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_log(_safe_div(ncfo + sbc, intexp.abs() + 1.0).clip(lower=0.1)))

# Block 100-109: diff 1q
def cg_f026_interest_coverage_core100_diff_1q_v101_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_diff(_safe_div(opinc, intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core101_diff_1q_v102_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core102_diff_1q_v103_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core103_diff_1q_v104_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_diff(_safe_div(fcf, intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core104_diff_1q_v105_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_diff(_safe_div(opinc + sbc, intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core105_diff_1q_v106_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_diff(_safe_div(netinc, intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core106_diff_1q_v107_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_diff(_safe_div(revenue, intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core107_diff_1q_v108_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_diff(_safe_div(ebitda - capex.abs(), intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core108_diff_1q_v109_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_diff(_safe_div(debtt.abs(), intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core109_diff_1q_v110_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_diff(_log(_safe_div(ebitda, intexp.abs() + 1.0).clip(lower=0.1)), 1))

# Block 110-119: slope 4q
def cg_f026_interest_coverage_core110_slope_4q_v111_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_slope(_safe_div(opinc, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core111_slope_4q_v112_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_slope(_safe_div(ebitda, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core112_slope_4q_v113_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_slope(_safe_div(ncfo, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core113_slope_4q_v114_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_slope(_safe_div(fcf, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core114_slope_4q_v115_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_slope(_safe_div(opinc + sbc, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core115_slope_4q_v116_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_slope(_safe_div(netinc, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core116_slope_4q_v117_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_slope(_safe_div(revenue, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core117_slope_4q_v118_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_slope(_safe_div(ebitda - capex.abs(), intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core118_slope_4q_v119_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_slope(_safe_div(debtt.abs(), intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core119_slope_4q_v120_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_slope(_log(_safe_div(ebitda, intexp.abs() + 1.0).clip(lower=0.1)), 4))

# Block 120-129: ewm 8q
def cg_f026_interest_coverage_core120_ewm_8q_v121_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_ewm(_safe_div(opinc, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core121_ewm_8q_v122_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_ewm(_safe_div(ebitda, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core122_ewm_8q_v123_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_ewm(_safe_div(ncfo, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core123_ewm_8q_v124_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_ewm(_safe_div(fcf, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core124_ewm_8q_v125_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_ewm(_safe_div(opinc + sbc, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core125_ewm_8q_v126_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_ewm(_safe_div(netinc, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core126_ewm_8q_v127_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_ewm(_safe_div(revenue, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core127_ewm_8q_v128_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_ewm(_safe_div(ebitda - capex.abs(), intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core128_ewm_8q_v129_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_ewm(_safe_div(debtt.abs(), intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core129_ewm_8q_v130_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_ewm(_log(_safe_div(ebitda, intexp.abs() + 1.0).clip(lower=0.1)), 8))

# Block 130-139: stability 12q
def cg_f026_interest_coverage_core130_stability_12q_v131_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    base = _safe_div(opinc, intexp.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f026_interest_coverage_core131_stability_12q_v132_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    base = _safe_div(ebitda, intexp.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f026_interest_coverage_core132_stability_12q_v133_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    base = _safe_div(ncfo, intexp.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f026_interest_coverage_core133_stability_12q_v134_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    base = _safe_div(fcf, intexp.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f026_interest_coverage_core134_stability_12q_v135_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    base = _safe_div(opinc + sbc, intexp.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f026_interest_coverage_core135_stability_12q_v136_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    base = _safe_div(netinc, intexp.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f026_interest_coverage_core136_stability_12q_v137_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    base = _safe_div(revenue, intexp.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f026_interest_coverage_core137_stability_12q_v138_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    base = _safe_div(ebitda - capex.abs(), intexp.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f026_interest_coverage_core138_stability_12q_v139_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    base = _safe_div(debtt.abs(), intexp.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f026_interest_coverage_core139_stability_12q_v140_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    base = _log(_safe_div(ebitda, intexp.abs() + 1.0).clip(lower=0.1))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f026_interest_coverage_core140_ic_v141_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_safe_div(opinc, intexp.abs() + 1.0))
def cg_f026_interest_coverage_core141_ebitda_ic_v142_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_safe_div(ebitda, intexp.abs() + 1.0))
def cg_f026_interest_coverage_core142_cash_ic_v143_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_safe_div(ncfo, intexp.abs() + 1.0))
def cg_f026_interest_coverage_core143_fcf_ic_v144_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_safe_div(fcf, intexp.abs() + 1.0))
def cg_f026_interest_coverage_core144_adj_ic_v145_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_safe_div(opinc + sbc, intexp.abs() + 1.0))
def cg_f026_interest_coverage_core145_net_ic_v146_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_safe_div(netinc, intexp.abs() + 1.0))
def cg_f026_interest_coverage_core146_rev_ic_v147_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_safe_div(revenue, intexp.abs() + 1.0))
def cg_f026_interest_coverage_core147_debt_int_v148_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_safe_div(debtt.abs(), intexp.abs() + 1.0))
def cg_f026_interest_coverage_core148_free_ic_v149_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_safe_div(ebitda - capex.abs(), intexp.abs() + 1.0))
def cg_f026_interest_coverage_core149_ic_log_v150_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_log(_safe_div(ebitda, intexp.abs() + 1.0).clip(lower=0.1)))
