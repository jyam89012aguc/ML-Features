import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f070_ev_gross_profit_valuation_core75_pct_4q_v076_signal(ev, gp, grossmargin):
    return _clean(_pct_change(_safe_div(ev, gp.abs() + 1.0), 4))
def cg_f070_ev_gross_profit_valuation_core76_pct_4q_v077_signal(ev, gp, grossmargin):
    return _clean(_pct_change(ev - gp, 4))
def cg_f070_ev_gross_profit_valuation_core77_pct_4q_v078_signal(ev, gp, grossmargin):
    return _clean(_pct_change(_safe_div(ev - gp, gp.abs() + 1.0), 4))
def cg_f070_ev_gross_profit_valuation_core78_pct_4q_v079_signal(ev, gp, grossmargin):
    return _clean(_pct_change(_safe_div(ev, grossmargin.abs() + 0.01), 4))
def cg_f070_ev_gross_profit_valuation_core79_pct_4q_v080_signal(ev, gp, grossmargin):
    return _clean(_pct_change(_safe_div(gp, grossmargin.abs() + 0.01), 4))

# core80-89: std 8q
def cg_f070_ev_gross_profit_valuation_core80_std_8q_v081_signal(ev, gp, grossmargin):
    return _clean(_std(ev, 8))
def cg_f070_ev_gross_profit_valuation_core81_std_8q_v082_signal(ev, gp, grossmargin):
    return _clean(_std(_safe_div(ev, gp), 8))
def cg_f070_ev_gross_profit_valuation_core82_std_8q_v083_signal(ev, gp, grossmargin):
    return _clean(_std(gp, 8))
def cg_f070_ev_gross_profit_valuation_core83_std_8q_v084_signal(ev, gp, grossmargin):
    return _clean(_std(_safe_div(gp, ev), 8))
def cg_f070_ev_gross_profit_valuation_core84_std_8q_v085_signal(ev, gp, grossmargin):
    return _clean(_std(grossmargin, 8))
def cg_f070_ev_gross_profit_valuation_core85_std_8q_v086_signal(ev, gp, grossmargin):
    return _clean(_std(_safe_div(ev, gp.abs() + 1.0), 8))
def cg_f070_ev_gross_profit_valuation_core86_std_8q_v087_signal(ev, gp, grossmargin):
    return _clean(_std(ev - gp, 8))
def cg_f070_ev_gross_profit_valuation_core87_std_8q_v088_signal(ev, gp, grossmargin):
    return _clean(_std(_safe_div(ev - gp, gp.abs() + 1.0), 8))
def cg_f070_ev_gross_profit_valuation_core88_std_8q_v089_signal(ev, gp, grossmargin):
    return _clean(_std(_safe_div(ev, grossmargin.abs() + 0.01), 8))
def cg_f070_ev_gross_profit_valuation_core89_std_8q_v090_signal(ev, gp, grossmargin):
    return _clean(_std(_safe_div(gp, grossmargin.abs() + 0.01), 8))

# core90-99: log
def cg_f070_ev_gross_profit_valuation_core90_log_v091_signal(ev, gp, grossmargin):
    return _clean(_log(ev.clip(lower=1.0)))
def cg_f070_ev_gross_profit_valuation_core91_log_v092_signal(ev, gp, grossmargin):
    return _clean(_log(_safe_div(ev, gp).clip(lower=0.001)))
def cg_f070_ev_gross_profit_valuation_core92_log_v093_signal(ev, gp, grossmargin):
    return _clean(_log(gp.clip(lower=1.0)))
def cg_f070_ev_gross_profit_valuation_core93_log_v094_signal(ev, gp, grossmargin):
    return _clean(_log(_safe_div(gp, ev).clip(lower=0.001)))
def cg_f070_ev_gross_profit_valuation_core94_log_v095_signal(ev, gp, grossmargin):
    return _clean(_log(grossmargin.clip(lower=0.001)))
def cg_f070_ev_gross_profit_valuation_core95_log_v096_signal(ev, gp, grossmargin):
    return _clean(_log(_safe_div(ev, gp.abs() + 1.0).clip(lower=0.001)))
def cg_f070_ev_gross_profit_valuation_core96_log_v097_signal(ev, gp, grossmargin):
    return _clean(_log((ev - gp).clip(lower=1.0)))
def cg_f070_ev_gross_profit_valuation_core97_log_v098_signal(ev, gp, grossmargin):
    return _clean(_log(_safe_div(ev - gp, gp.abs() + 1.0).clip(lower=0.001)))
def cg_f070_ev_gross_profit_valuation_core98_log_v099_signal(ev, gp, grossmargin):
    return _clean(_log(_safe_div(ev, grossmargin.abs() + 0.01).clip(lower=0.001)))
def cg_f070_ev_gross_profit_valuation_core99_log_v100_signal(ev, gp, grossmargin):
    return _clean(_log(_safe_div(gp, grossmargin.abs() + 0.01).clip(lower=0.001)))

# core100-109: diff 1q
def cg_f070_ev_gross_profit_valuation_core100_diff_1q_v101_signal(ev, gp, grossmargin):
    return _clean(_diff(ev, 1))
def cg_f070_ev_gross_profit_valuation_core101_diff_1q_v102_signal(ev, gp, grossmargin):
    return _clean(_diff(_safe_div(ev, gp), 1))
def cg_f070_ev_gross_profit_valuation_core102_diff_1q_v103_signal(ev, gp, grossmargin):
    return _clean(_diff(gp, 1))
def cg_f070_ev_gross_profit_valuation_core103_diff_1q_v104_signal(ev, gp, grossmargin):
    return _clean(_diff(_safe_div(gp, ev), 1))
def cg_f070_ev_gross_profit_valuation_core104_diff_1q_v105_signal(ev, gp, grossmargin):
    return _clean(_diff(grossmargin, 1))
def cg_f070_ev_gross_profit_valuation_core105_diff_1q_v106_signal(ev, gp, grossmargin):
    return _clean(_diff(_safe_div(ev, gp.abs() + 1.0), 1))
def cg_f070_ev_gross_profit_valuation_core106_diff_1q_v107_signal(ev, gp, grossmargin):
    return _clean(_diff(ev - gp, 1))
def cg_f070_ev_gross_profit_valuation_core107_diff_1q_v108_signal(ev, gp, grossmargin):
    return _clean(_diff(_safe_div(ev - gp, gp.abs() + 1.0), 1))
def cg_f070_ev_gross_profit_valuation_core108_diff_1q_v109_signal(ev, gp, grossmargin):
    return _clean(_diff(_safe_div(ev, grossmargin.abs() + 0.01), 1))
def cg_f070_ev_gross_profit_valuation_core109_diff_1q_v110_signal(ev, gp, grossmargin):
    return _clean(_diff(_safe_div(gp, grossmargin.abs() + 0.01), 1))

# core110-119: slope 4q
def cg_f070_ev_gross_profit_valuation_core110_slope_4q_v111_signal(ev, gp, grossmargin):
    return _clean(_slope(ev, 4))
def cg_f070_ev_gross_profit_valuation_core111_slope_4q_v112_signal(ev, gp, grossmargin):
    return _clean(_slope(_safe_div(ev, gp), 4))
def cg_f070_ev_gross_profit_valuation_core112_slope_4q_v113_signal(ev, gp, grossmargin):
    return _clean(_slope(gp, 4))
def cg_f070_ev_gross_profit_valuation_core113_slope_4q_v114_signal(ev, gp, grossmargin):
    return _clean(_slope(_safe_div(gp, ev), 4))
def cg_f070_ev_gross_profit_valuation_core114_slope_4q_v115_signal(ev, gp, grossmargin):
    return _clean(_slope(grossmargin, 4))
def cg_f070_ev_gross_profit_valuation_core115_slope_4q_v116_signal(ev, gp, grossmargin):
    return _clean(_slope(_safe_div(ev, gp.abs() + 1.0), 4))
def cg_f070_ev_gross_profit_valuation_core116_slope_4q_v117_signal(ev, gp, grossmargin):
    return _clean(_slope(ev - gp, 4))
def cg_f070_ev_gross_profit_valuation_core117_slope_4q_v118_signal(ev, gp, grossmargin):
    return _clean(_slope(_safe_div(ev - gp, gp.abs() + 1.0), 4))
def cg_f070_ev_gross_profit_valuation_core118_slope_4q_v119_signal(ev, gp, grossmargin):
    return _clean(_slope(_safe_div(ev, grossmargin.abs() + 0.01), 4))
def cg_f070_ev_gross_profit_valuation_core119_slope_4q_v120_signal(ev, gp, grossmargin):
    return _clean(_slope(_safe_div(gp, grossmargin.abs() + 0.01), 4))

# core120-129: ewm 8q
def cg_f070_ev_gross_profit_valuation_core120_ewm_8q_v121_signal(ev, gp, grossmargin):
    return _clean(_ewm(ev, 8))
def cg_f070_ev_gross_profit_valuation_core121_ewm_8q_v122_signal(ev, gp, grossmargin):
    return _clean(_ewm(_safe_div(ev, gp), 8))
def cg_f070_ev_gross_profit_valuation_core122_ewm_8q_v123_signal(ev, gp, grossmargin):
    return _clean(_ewm(gp, 8))
def cg_f070_ev_gross_profit_valuation_core123_ewm_8q_v124_signal(ev, gp, grossmargin):
    return _clean(_ewm(_safe_div(gp, ev), 8))
def cg_f070_ev_gross_profit_valuation_core124_ewm_8q_v125_signal(ev, gp, grossmargin):
    return _clean(_ewm(grossmargin, 8))
def cg_f070_ev_gross_profit_valuation_core125_ewm_8q_v126_signal(ev, gp, grossmargin):
    return _clean(_ewm(_safe_div(ev, gp.abs() + 1.0), 8))
def cg_f070_ev_gross_profit_valuation_core126_ewm_8q_v127_signal(ev, gp, grossmargin):
    return _clean(_ewm(ev - gp, 8))
def cg_f070_ev_gross_profit_valuation_core127_ewm_8q_v128_signal(ev, gp, grossmargin):
    return _clean(_ewm(_safe_div(ev - gp, gp.abs() + 1.0), 8))
def cg_f070_ev_gross_profit_valuation_core128_ewm_8q_v129_signal(ev, gp, grossmargin):
    return _clean(_ewm(_safe_div(ev, grossmargin.abs() + 0.01), 8))
def cg_f070_ev_gross_profit_valuation_core129_ewm_8q_v130_signal(ev, gp, grossmargin):
    return _clean(_ewm(_safe_div(gp, grossmargin.abs() + 0.01), 8))

# core130-139: stability 12q
def cg_f070_ev_gross_profit_valuation_core130_stability_12q_v131_signal(ev, gp, grossmargin):
    return _clean(_safe_div(_std(ev, 12), _mean(ev, 12)))
def cg_f070_ev_gross_profit_valuation_core131_stability_12q_v132_signal(ev, gp, grossmargin):
    base = _safe_div(ev, gp)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f070_ev_gross_profit_valuation_core132_stability_12q_v133_signal(ev, gp, grossmargin):
    base = gp
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f070_ev_gross_profit_valuation_core133_stability_12q_v134_signal(ev, gp, grossmargin):
    base = _safe_div(gp, ev)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f070_ev_gross_profit_valuation_core134_stability_12q_v135_signal(ev, gp, grossmargin):
    base = grossmargin
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f070_ev_gross_profit_valuation_core135_stability_12q_v136_signal(ev, gp, grossmargin):
    base = _safe_div(ev, gp.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f070_ev_gross_profit_valuation_core136_stability_12q_v137_signal(ev, gp, grossmargin):
    base = ev - gp
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f070_ev_gross_profit_valuation_core137_stability_12q_v138_signal(ev, gp, grossmargin):
    base = _safe_div(ev - gp, gp.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f070_ev_gross_profit_valuation_core138_stability_12q_v139_signal(ev, gp, grossmargin):
    base = _safe_div(ev, grossmargin.abs() + 0.01)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f070_ev_gross_profit_valuation_core139_stability_12q_v140_signal(ev, gp, grossmargin):
    base = _safe_div(gp, grossmargin.abs() + 0.01)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))

# core140-149: level
def cg_f070_ev_gross_profit_valuation_core140_level_v141_signal(ev, gp, grossmargin):
    return _clean(ev)
def cg_f070_ev_gross_profit_valuation_core141_to_gp_v142_signal(ev, gp, grossmargin):
    return _clean(_safe_div(ev, gp))
def cg_f070_ev_gross_profit_valuation_core142_gp_level_v143_signal(ev, gp, grossmargin):
    return _clean(gp)
def cg_f070_ev_gross_profit_valuation_core143_gp_to_ev_v144_signal(ev, gp, grossmargin):
    return _clean(_safe_div(gp, ev))
def cg_f070_ev_gross_profit_valuation_core144_grossmargin_v145_signal(ev, gp, grossmargin):
    return _clean(grossmargin)
def cg_f070_ev_gross_profit_valuation_core145_to_gp_abs_v146_signal(ev, gp, grossmargin):
    return _clean(_safe_div(ev, gp.abs() + 1.0))
def cg_f070_ev_gross_profit_valuation_core146_ev_minus_gp_v147_signal(ev, gp, grossmargin):
    return _clean(ev - gp)
def cg_f070_ev_gross_profit_valuation_core147_ev_minus_gp_to_gp_v148_signal(ev, gp, grossmargin):
    return _clean(_safe_div(ev - gp, gp.abs() + 1.0))
def cg_f070_ev_gross_profit_valuation_core148_ev_to_margin_v149_signal(ev, gp, grossmargin):
    return _clean(_safe_div(ev, grossmargin.abs() + 0.01))
def cg_f070_ev_gross_profit_valuation_core149_gp_to_margin_v150_signal(ev, gp, grossmargin):
    return _clean(_safe_div(gp, grossmargin.abs() + 0.01))
