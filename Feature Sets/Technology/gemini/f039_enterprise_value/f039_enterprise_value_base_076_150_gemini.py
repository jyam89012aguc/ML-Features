import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f039_enterprise_value_core75_pct_4q_v076_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_pct_change(_safe_div(debt - cashneq, ev.abs() + 1.0), 4))
def cg_f039_enterprise_value_core76_pct_4q_v077_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_pct_change(_safe_div(ev, marketcap), 4))
def cg_f039_enterprise_value_core77_pct_4q_v078_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_pct_change(_safe_div(ev, ncfo.abs() + 1.0), 4))
def cg_f039_enterprise_value_core78_pct_4q_v079_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_pct_change(_pct_change(ev, 4), 4))
def cg_f039_enterprise_value_core79_pct_4q_v080_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_pct_change(_log(ev.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f039_enterprise_value_core80_std_8q_v081_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_std(ev, 8))
def cg_f039_enterprise_value_core81_std_8q_v082_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_std(_safe_div(ev, revenue), 8))
def cg_f039_enterprise_value_core82_std_8q_v083_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_std(_safe_div(ev, ebitda.clip(lower=0) + 1.0), 8))
def cg_f039_enterprise_value_core83_std_8q_v084_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_std(_safe_div(ev, ncfo.abs() + 1.0), 8))
def cg_f039_enterprise_value_core84_std_8q_v085_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_std(_safe_div(ev, assets), 8))
def cg_f039_enterprise_value_core85_std_8q_v086_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_std(_safe_div(debt - cashneq, ev.abs() + 1.0), 8))
def cg_f039_enterprise_value_core86_std_8q_v087_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_std(_safe_div(ev, sharesbas), 8))
def cg_f039_enterprise_value_core87_std_8q_v088_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_std(_pct_change(ev, 4), 8))
def cg_f039_enterprise_value_core88_std_8q_v089_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_std(_safe_div(ev, marketcap), 8))
def cg_f039_enterprise_value_core89_std_8q_v090_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_std(_log(ev.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f039_enterprise_value_core90_log_v091_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_log(ev.clip(lower=1.0)))
def cg_f039_enterprise_value_core91_log_v092_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_log(_safe_div(ev, revenue).abs().clip(lower=0.0001)))
def cg_f039_enterprise_value_core92_log_v093_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_log(_safe_div(ev, ebitda.clip(lower=0) + 1.0).abs().clip(lower=0.001)))
def cg_f039_enterprise_value_core93_log_v094_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_log(_safe_div(ev, ncfo.abs() + 1.0).abs().clip(lower=0.001)))
def cg_f039_enterprise_value_core94_log_v095_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_log(_safe_div(ev, assets).clip(lower=0.0001)))
def cg_f039_enterprise_value_core95_log_v096_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_log(_safe_div(debt - cashneq, ev.abs() + 1.0).abs().clip(lower=0.001)))
def cg_f039_enterprise_value_core96_log_v097_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_log(_safe_div(ev, sharesbas).clip(lower=0.1)))
def cg_f039_enterprise_value_core97_log_v098_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_log(_pct_change(ev, 4).clip(lower=-0.9) + 1.1))
def cg_f039_enterprise_value_core98_log_v099_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_log(_safe_div(ev, marketcap).clip(lower=0.1)))
def cg_f039_enterprise_value_core99_log_v100_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    return _clean(_log(marketcap.clip(lower=1.0)))

# Block 100-109: diff 1q
def cg_f039_enterprise_value_core100_diff_1q_v101_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_diff(ev, 1))
def cg_f039_enterprise_value_core101_diff_1q_v102_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_diff(_safe_div(ev, revenue), 1))
def cg_f039_enterprise_value_core102_diff_1q_v103_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_diff(_safe_div(ev, ebitda.clip(lower=0) + 1.0), 1))
def cg_f039_enterprise_value_core103_diff_1q_v104_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_diff(_safe_div(ev, ncfo.abs() + 1.0), 1))
def cg_f039_enterprise_value_core104_diff_1q_v105_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_diff(_safe_div(ev, assets), 1))
def cg_f039_enterprise_value_core105_diff_1q_v106_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_diff(_safe_div(debt - cashneq, ev.abs() + 1.0), 1))
def cg_f039_enterprise_value_core106_diff_1q_v107_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_diff(_safe_div(ev, sharesbas), 1))
def cg_f039_enterprise_value_core107_diff_1q_v108_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_diff(_pct_change(ev, 4), 1))
def cg_f039_enterprise_value_core108_diff_1q_v109_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_diff(_safe_div(ev, marketcap), 1))
def cg_f039_enterprise_value_core109_diff_1q_v110_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_diff(_log(ev.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f039_enterprise_value_core110_slope_4q_v111_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_slope(ev, 4))
def cg_f039_enterprise_value_core111_slope_4q_v112_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_slope(_safe_div(ev, revenue), 4))
def cg_f039_enterprise_value_core112_slope_4q_v113_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_slope(_safe_div(ev, ebitda.clip(lower=0) + 1.0), 4))
def cg_f039_enterprise_value_core113_slope_4q_v114_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_slope(_safe_div(ev, ncfo.abs() + 1.0), 4))
def cg_f039_enterprise_value_core114_slope_4q_v115_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_slope(_safe_div(ev, assets), 4))
def cg_f039_enterprise_value_core115_slope_4q_v116_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_slope(_safe_div(debt - cashneq, ev.abs() + 1.0), 4))
def cg_f039_enterprise_value_core116_slope_4q_v117_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_slope(_safe_div(ev, sharesbas), 4))
def cg_f039_enterprise_value_core117_slope_4q_v118_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_slope(_pct_change(ev, 4), 4))
def cg_f039_enterprise_value_core118_slope_4q_v119_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_slope(_safe_div(ev, marketcap), 4))
def cg_f039_enterprise_value_core119_slope_4q_v120_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_slope(_log(ev.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f039_enterprise_value_core120_ewm_8q_v121_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_ewm(ev, 8))
def cg_f039_enterprise_value_core121_ewm_8q_v122_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_ewm(_safe_div(ev, revenue), 8))
def cg_f039_enterprise_value_core122_ewm_8q_v123_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_ewm(_safe_div(ev, ebitda.clip(lower=0) + 1.0), 8))
def cg_f039_enterprise_value_core123_ewm_8q_v124_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_ewm(_safe_div(ev, ncfo.abs() + 1.0), 8))
def cg_f039_enterprise_value_core124_ewm_8q_v125_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_ewm(_safe_div(ev, assets), 8))
def cg_f039_enterprise_value_core125_ewm_8q_v126_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_ewm(_safe_div(debt - cashneq, ev.abs() + 1.0), 8))
def cg_f039_enterprise_value_core126_ewm_8q_v127_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_ewm(_safe_div(ev, sharesbas), 8))
def cg_f039_enterprise_value_core127_ewm_8q_v128_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_ewm(_pct_change(ev, 4), 8))
def cg_f039_enterprise_value_core128_ewm_8q_v129_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_ewm(_safe_div(ev, marketcap), 8))
def cg_f039_enterprise_value_core129_ewm_8q_v130_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_ewm(_log(ev.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f039_enterprise_value_core130_stability_12q_v131_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_safe_div(_std(ev, 12), _mean(ev, 12).abs() + 1.0))
def cg_f039_enterprise_value_core131_stability_12q_v132_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    base = _safe_div(ev, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f039_enterprise_value_core132_stability_12q_v133_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    base = _safe_div(ev, ebitda.clip(lower=0) + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f039_enterprise_value_core133_stability_12q_v134_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    base = _safe_div(ev, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f039_enterprise_value_core134_stability_12q_v135_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    base = _safe_div(debt - cashneq, ev.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f039_enterprise_value_core135_stability_12q_v136_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    base = _safe_div(ev, sharesbas)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f039_enterprise_value_core136_stability_12q_v137_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    base = _pct_change(ev, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f039_enterprise_value_core137_stability_12q_v138_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    base = _safe_div(ev, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f039_enterprise_value_core138_stability_12q_v139_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    base = ev
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f039_enterprise_value_core139_stability_12q_v140_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    base = _log(ev.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f039_enterprise_value_core140_level_v141_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    return _clean(marketcap + debt - cashneq)
def cg_f039_enterprise_value_core141_ratio_rev_v142_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_safe_div(ev, revenue))
def cg_f039_enterprise_value_core142_ratio_ebitda_v143_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_safe_div(ev, ebitda.clip(lower=0) + 1.0))
def cg_f039_enterprise_value_core143_ratio_ncfo_v144_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_safe_div(ev, ncfo.abs() + 1.0))
def cg_f039_enterprise_value_core144_ratio_assets_v145_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_safe_div(ev, assets))
def cg_f039_enterprise_value_core145_ratio_nd_ev_v146_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_safe_div(debt - cashneq, ev.abs() + 1.0))
def cg_f039_enterprise_value_core146_ratio_shares_v147_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_safe_div(ev, sharesbas))
def cg_f039_enterprise_value_core147_growth_yoy_v148_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_pct_change(ev, 4))
def cg_f039_enterprise_value_core148_ratio_mcap_v149_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_safe_div(ev, marketcap))
def cg_f039_enterprise_value_core149_log_level_v150_signal(marketcap, debt, cashneq, revenue, ebitda, ncfo, assets, sharesbas):
    ev = marketcap + debt - cashneq
    return _clean(_log(ev.clip(lower=1.0)))
