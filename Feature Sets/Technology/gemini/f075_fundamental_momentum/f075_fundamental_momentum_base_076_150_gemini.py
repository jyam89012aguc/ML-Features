import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f075_fundamental_momentum_core75_pct_4q_v076_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_pct_change(_safe_div(revenue, rnd.abs() + 1.0), 4))
def cg_f075_fundamental_momentum_core76_pct_4q_v077_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_pct_change(_safe_div(ncfo, revenue.abs() + 1.0), 4))
def cg_f075_fundamental_momentum_core77_pct_4q_v078_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_pct_change(_safe_div(fcf, ncfo.abs() + 1.0), 4))
def cg_f075_fundamental_momentum_core78_pct_4q_v079_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_pct_change(_safe_div(netinc, revenue.abs() + 1.0), 4))
def cg_f075_fundamental_momentum_core79_pct_4q_v080_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_pct_change(_safe_div(opinc, revenue.abs() + 1.0), 4))

# core80-89: std 8q
def cg_f075_fundamental_momentum_core80_std_8q_v081_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_std(revenue, 8))
def cg_f075_fundamental_momentum_core81_std_8q_v082_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_std(ncfo, 8))
def cg_f075_fundamental_momentum_core82_std_8q_v083_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_std(fcf, 8))
def cg_f075_fundamental_momentum_core83_std_8q_v084_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_std(netinc, 8))
def cg_f075_fundamental_momentum_core84_std_8q_v085_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_std(opinc, 8))
def cg_f075_fundamental_momentum_core85_std_8q_v086_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_std(_safe_div(revenue, rnd.abs() + 1.0), 8))
def cg_f075_fundamental_momentum_core86_std_8q_v087_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_std(_safe_div(ncfo, revenue.abs() + 1.0), 8))
def cg_f075_fundamental_momentum_core87_std_8q_v088_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_std(_safe_div(fcf, ncfo.abs() + 1.0), 8))
def cg_f075_fundamental_momentum_core88_std_8q_v089_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_std(_safe_div(netinc, revenue.abs() + 1.0), 8))
def cg_f075_fundamental_momentum_core89_std_8q_v090_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_std(_safe_div(opinc, revenue.abs() + 1.0), 8))

# core90-99: log
def cg_f075_fundamental_momentum_core90_log_v091_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_log(revenue.clip(lower=1.0)))
def cg_f075_fundamental_momentum_core91_log_v092_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_log(ncfo.clip(lower=1.0)))
def cg_f075_fundamental_momentum_core92_log_v093_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_log(fcf.clip(lower=1.0)))
def cg_f075_fundamental_momentum_core93_log_v094_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_log(netinc.clip(lower=1.0)))
def cg_f075_fundamental_momentum_core94_log_v095_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_log(opinc.clip(lower=1.0)))
def cg_f075_fundamental_momentum_core95_log_v096_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_log(_safe_div(revenue, rnd.abs() + 1.0).clip(lower=0.001)))
def cg_f075_fundamental_momentum_core96_log_v097_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_log(_safe_div(ncfo, revenue.abs() + 1.0).clip(lower=0.001)))
def cg_f075_fundamental_momentum_core97_log_v098_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_log(_safe_div(fcf, ncfo.abs() + 1.0).clip(lower=0.001)))
def cg_f075_fundamental_momentum_core98_log_v099_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_log(_safe_div(netinc, revenue.abs() + 1.0).clip(lower=0.001)))
def cg_f075_fundamental_momentum_core99_log_v100_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_log(_safe_div(opinc, revenue.abs() + 1.0).clip(lower=0.001)))

# core100-109: diff 1q
def cg_f075_fundamental_momentum_core100_diff_1q_v101_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(revenue, 1))
def cg_f075_fundamental_momentum_core101_diff_1q_v102_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(ncfo, 1))
def cg_f075_fundamental_momentum_core102_diff_1q_v103_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(fcf, 1))
def cg_f075_fundamental_momentum_core103_diff_1q_v104_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(netinc, 1))
def cg_f075_fundamental_momentum_core104_diff_1q_v105_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(opinc, 1))
def cg_f075_fundamental_momentum_core105_diff_1q_v106_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_safe_div(revenue, rnd.abs() + 1.0), 1))
def cg_f075_fundamental_momentum_core106_diff_1q_v107_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_safe_div(ncfo, revenue.abs() + 1.0), 1))
def cg_f075_fundamental_momentum_core107_diff_1q_v108_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_safe_div(fcf, ncfo.abs() + 1.0), 1))
def cg_f075_fundamental_momentum_core108_diff_1q_v109_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_safe_div(netinc, revenue.abs() + 1.0), 1))
def cg_f075_fundamental_momentum_core109_diff_1q_v110_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_safe_div(opinc, revenue.abs() + 1.0), 1))

# core110-119: slope 4q
def cg_f075_fundamental_momentum_core110_slope_4q_v111_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(revenue, 4))
def cg_f075_fundamental_momentum_core111_slope_4q_v112_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(ncfo, 4))
def cg_f075_fundamental_momentum_core112_slope_4q_v113_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(fcf, 4))
def cg_f075_fundamental_momentum_core113_slope_4q_v114_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(netinc, 4))
def cg_f075_fundamental_momentum_core114_slope_4q_v115_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(opinc, 4))
def cg_f075_fundamental_momentum_core115_slope_4q_v116_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_safe_div(revenue, rnd.abs() + 1.0), 4))
def cg_f075_fundamental_momentum_core116_slope_4q_v117_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_safe_div(ncfo, revenue.abs() + 1.0), 4))
def cg_f075_fundamental_momentum_core117_slope_4q_v118_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_safe_div(fcf, ncfo.abs() + 1.0), 4))
def cg_f075_fundamental_momentum_core118_slope_4q_v119_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_safe_div(netinc, revenue.abs() + 1.0), 4))
def cg_f075_fundamental_momentum_core119_slope_4q_v120_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_safe_div(opinc, revenue.abs() + 1.0), 4))

# core120-129: ewm 8q
def cg_f075_fundamental_momentum_core120_ewm_8q_v121_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_ewm(revenue, 8))
def cg_f075_fundamental_momentum_core121_ewm_8q_v122_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_ewm(ncfo, 8))
def cg_f075_fundamental_momentum_core122_ewm_8q_v123_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_ewm(fcf, 8))
def cg_f075_fundamental_momentum_core123_ewm_8q_v124_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_ewm(netinc, 8))
def cg_f075_fundamental_momentum_core124_ewm_8q_v125_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_ewm(opinc, 8))
def cg_f075_fundamental_momentum_core125_ewm_8q_v126_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_ewm(_safe_div(revenue, rnd.abs() + 1.0), 8))
def cg_f075_fundamental_momentum_core126_ewm_8q_v127_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_ewm(_safe_div(ncfo, revenue.abs() + 1.0), 8))
def cg_f075_fundamental_momentum_core127_ewm_8q_v128_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_ewm(_safe_div(fcf, ncfo.abs() + 1.0), 8))
def cg_f075_fundamental_momentum_core128_ewm_8q_v129_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_ewm(_safe_div(netinc, revenue.abs() + 1.0), 8))
def cg_f075_fundamental_momentum_core129_ewm_8q_v130_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_ewm(_safe_div(opinc, revenue.abs() + 1.0), 8))

# core130-139: stability 12q
def cg_f075_fundamental_momentum_core130_stability_12q_v131_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_safe_div(_std(revenue, 12), _mean(revenue, 12)))
def cg_f075_fundamental_momentum_core131_stability_12q_v132_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    base = ncfo
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f075_fundamental_momentum_core132_stability_12q_v133_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    base = fcf
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f075_fundamental_momentum_core133_stability_12q_v134_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    base = netinc
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f075_fundamental_momentum_core134_stability_12q_v135_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    base = opinc
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f075_fundamental_momentum_core135_stability_12q_v136_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    base = _safe_div(revenue, rnd.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f075_fundamental_momentum_core136_stability_12q_v137_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    base = _safe_div(ncfo, revenue.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f075_fundamental_momentum_core137_stability_12q_v138_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    base = _safe_div(fcf, ncfo.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f075_fundamental_momentum_core138_stability_12q_v139_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    base = _safe_div(netinc, revenue.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f075_fundamental_momentum_core139_stability_12q_v140_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    base = _safe_div(opinc, revenue.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))

# core140-149: level
def cg_f075_fundamental_momentum_core140_revenue_v141_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(revenue)
def cg_f075_fundamental_momentum_core141_ncfo_v142_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(ncfo)
def cg_f075_fundamental_momentum_core142_fcf_v143_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(fcf)
def cg_f075_fundamental_momentum_core143_netinc_v144_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(netinc)
def cg_f075_fundamental_momentum_core144_opinc_v145_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(opinc)
def cg_f075_fundamental_momentum_core145_rev_to_rnd_v146_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_safe_div(revenue, rnd.abs() + 1.0))
def cg_f075_fundamental_momentum_core146_ncfo_to_rev_v147_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_safe_div(ncfo, revenue.abs() + 1.0))
def cg_f075_fundamental_momentum_core147_fcf_to_ncfo_v148_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_safe_div(fcf, ncfo.abs() + 1.0))
def cg_f075_fundamental_momentum_core148_netinc_to_rev_v149_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_safe_div(netinc, revenue.abs() + 1.0))
def cg_f075_fundamental_momentum_core149_opinc_to_rev_v150_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_safe_div(opinc, revenue.abs() + 1.0))
