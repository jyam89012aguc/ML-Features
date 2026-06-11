import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f025_net_debt_leverage_core75_pct_4q_v076_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(debtt - cashneq, 4))
def cg_f025_net_debt_leverage_core76_pct_4q_v077_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt - cashneq, sharesbas), 4))
def cg_f025_net_debt_leverage_core77_pct_4q_v078_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt, cashneq.abs() + 1.0), 4))
def cg_f025_net_debt_leverage_core78_pct_4q_v079_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(cashneq, debtt.abs() + 1.0), 4))
def cg_f025_net_debt_leverage_core79_pct_4q_v080_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_pct_change(_log((debtt - cashneq).clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f025_net_debt_leverage_core80_std_8q_v081_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_std(_safe_div(debtt - cashneq, ebitda.clip(lower=0) + 1.0), 8))
def cg_f025_net_debt_leverage_core81_std_8q_v082_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_std(_safe_div(debtt - cashneq, ncfo.abs() + 1.0), 8))
def cg_f025_net_debt_leverage_core82_std_8q_v083_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_std(_safe_div(debtt - cashneq, revenue), 8))
def cg_f025_net_debt_leverage_core83_std_8q_v084_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_std(_safe_div(debtt - cashneq, assets), 8))
def cg_f025_net_debt_leverage_core84_std_8q_v085_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_std(_safe_div(debtt - cashneq, marketcap), 8))
def cg_f025_net_debt_leverage_core85_std_8q_v086_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_std(debtt - cashneq, 8))
def cg_f025_net_debt_leverage_core86_std_8q_v087_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_std(_safe_div(debtt - cashneq, sharesbas), 8))
def cg_f025_net_debt_leverage_core87_std_8q_v088_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_std(_safe_div(debtt, cashneq.abs() + 1.0), 8))
def cg_f025_net_debt_leverage_core88_std_8q_v089_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_std(_safe_div(cashneq, debtt.abs() + 1.0), 8))
def cg_f025_net_debt_leverage_core89_std_8q_v090_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_std(_log((debtt - cashneq).clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f025_net_debt_leverage_core90_log_v091_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_log((debtt - cashneq).clip(lower=1.0)))
def cg_f025_net_debt_leverage_core91_log_v092_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_log(_safe_div(debtt - cashneq, ebitda.clip(lower=0) + 1.0).abs().clip(lower=0.01)))
def cg_f025_net_debt_leverage_core92_log_v093_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_log(_safe_div(debtt - cashneq, revenue).abs().clip(lower=0.001)))
def cg_f025_net_debt_leverage_core93_log_v094_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_log(_safe_div(debtt - cashneq, assets).abs().clip(lower=0.001)))
def cg_f025_net_debt_leverage_core94_log_v095_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_log(_safe_div(debtt - cashneq, marketcap).abs().clip(lower=0.001)))
def cg_f025_net_debt_leverage_core95_log_v096_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_log(_safe_div(debtt, cashneq.abs() + 1.0).clip(lower=0.01)))
def cg_f025_net_debt_leverage_core96_log_v097_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_log(_safe_div(cashneq, debtt.abs() + 1.0).clip(lower=0.01)))
def cg_f025_net_debt_leverage_core97_log_v098_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_log(_safe_div(debtt - cashneq, sharesbas).abs().clip(lower=0.01)))
def cg_f025_net_debt_leverage_core98_log_v099_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_log(_safe_div(debtt - cashneq, ncfo.abs() + 1.0).abs().clip(lower=0.01)))
def cg_f025_net_debt_leverage_core99_log_v100_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_log(_safe_div(debtt - cashneq, assets).abs().clip(lower=0.001)))

# Block 100-109: diff 1q
def cg_f025_net_debt_leverage_core100_diff_1q_v101_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debtt - cashneq, ebitda.clip(lower=0) + 1.0), 1))
def cg_f025_net_debt_leverage_core101_diff_1q_v102_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debtt - cashneq, ncfo.abs() + 1.0), 1))
def cg_f025_net_debt_leverage_core102_diff_1q_v103_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debtt - cashneq, revenue), 1))
def cg_f025_net_debt_leverage_core103_diff_1q_v104_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debtt - cashneq, assets), 1))
def cg_f025_net_debt_leverage_core104_diff_1q_v105_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debtt - cashneq, marketcap), 1))
def cg_f025_net_debt_leverage_core105_diff_1q_v106_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_diff(debtt - cashneq, 1))
def cg_f025_net_debt_leverage_core106_diff_1q_v107_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debtt - cashneq, sharesbas), 1))
def cg_f025_net_debt_leverage_core107_diff_1q_v108_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debtt, cashneq.abs() + 1.0), 1))
def cg_f025_net_debt_leverage_core108_diff_1q_v109_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_diff(_safe_div(cashneq, debtt.abs() + 1.0), 1))
def cg_f025_net_debt_leverage_core109_diff_1q_v110_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_diff(_log((debtt - cashneq).clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f025_net_debt_leverage_core110_slope_4q_v111_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debtt - cashneq, ebitda.clip(lower=0) + 1.0), 4))
def cg_f025_net_debt_leverage_core111_slope_4q_v112_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debtt - cashneq, ncfo.abs() + 1.0), 4))
def cg_f025_net_debt_leverage_core112_slope_4q_v113_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debtt - cashneq, revenue), 4))
def cg_f025_net_debt_leverage_core113_slope_4q_v114_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debtt - cashneq, assets), 4))
def cg_f025_net_debt_leverage_core114_slope_4q_v115_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debtt - cashneq, marketcap), 4))
def cg_f025_net_debt_leverage_core115_slope_4q_v116_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_slope(debtt - cashneq, 4))
def cg_f025_net_debt_leverage_core116_slope_4q_v117_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debtt - cashneq, sharesbas), 4))
def cg_f025_net_debt_leverage_core117_slope_4q_v118_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debtt, cashneq.abs() + 1.0), 4))
def cg_f025_net_debt_leverage_core118_slope_4q_v119_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_slope(_safe_div(cashneq, debtt.abs() + 1.0), 4))
def cg_f025_net_debt_leverage_core119_slope_4q_v120_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_slope(_log((debtt - cashneq).clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f025_net_debt_leverage_core120_ewm_8q_v121_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debtt - cashneq, ebitda.clip(lower=0) + 1.0), 8))
def cg_f025_net_debt_leverage_core121_ewm_8q_v122_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debtt - cashneq, ncfo.abs() + 1.0), 8))
def cg_f025_net_debt_leverage_core122_ewm_8q_v123_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debtt - cashneq, revenue), 8))
def cg_f025_net_debt_leverage_core123_ewm_8q_v124_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debtt - cashneq, assets), 8))
def cg_f025_net_debt_leverage_core124_ewm_8q_v125_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debtt - cashneq, marketcap), 8))
def cg_f025_net_debt_leverage_core125_ewm_8q_v126_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_ewm(debtt - cashneq, 8))
def cg_f025_net_debt_leverage_core126_ewm_8q_v127_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debtt - cashneq, sharesbas), 8))
def cg_f025_net_debt_leverage_core127_ewm_8q_v128_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debtt, cashneq.abs() + 1.0), 8))
def cg_f025_net_debt_leverage_core128_ewm_8q_v129_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(cashneq, debtt.abs() + 1.0), 8))
def cg_f025_net_debt_leverage_core129_ewm_8q_v130_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_ewm(_log((debtt - cashneq).clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f025_net_debt_leverage_core130_stability_12q_v131_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    base = _safe_div(debtt - cashneq, ebitda.clip(lower=0) + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f025_net_debt_leverage_core131_stability_12q_v132_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    base = _safe_div(debtt - cashneq, ncfo.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f025_net_debt_leverage_core132_stability_12q_v133_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    base = _safe_div(debtt - cashneq, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f025_net_debt_leverage_core133_stability_12q_v134_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    base = _safe_div(debtt - cashneq, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f025_net_debt_leverage_core134_stability_12q_v135_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    base = _safe_div(debtt - cashneq, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f025_net_debt_leverage_core135_stability_12q_v136_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    base = debtt - cashneq
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f025_net_debt_leverage_core136_stability_12q_v137_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    base = _safe_div(debtt - cashneq, sharesbas)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f025_net_debt_leverage_core137_stability_12q_v138_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    base = _safe_div(debtt, cashneq.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f025_net_debt_leverage_core138_stability_12q_v139_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    base = _safe_div(cashneq, debtt.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f025_net_debt_leverage_core139_stability_12q_v140_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    base = _log((debtt - cashneq).clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f025_net_debt_leverage_core140_net_debt_v141_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(debtt - cashneq)
def cg_f025_net_debt_leverage_core141_nd_ebitda_v142_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_safe_div(debtt - cashneq, ebitda.clip(lower=0) + 1.0))
def cg_f025_net_debt_leverage_core142_nd_ncfo_v143_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_safe_div(debtt - cashneq, ncfo.abs() + 1.0))
def cg_f025_net_debt_leverage_core143_nd_rev_v144_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_safe_div(debtt - cashneq, revenue))
def cg_f025_net_debt_leverage_core144_nd_assets_v145_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_safe_div(debtt - cashneq, assets))
def cg_f025_net_debt_leverage_core145_nd_mcap_v146_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_safe_div(debtt - cashneq, marketcap))
def cg_f025_net_debt_leverage_core146_nd_shares_v147_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_safe_div(debtt - cashneq, sharesbas))
def cg_f025_net_debt_leverage_core147_d_c_ratio_v148_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_safe_div(debtt, cashneq.abs() + 1.0))
def cg_f025_net_debt_leverage_core148_c_d_ratio_v149_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_safe_div(cashneq, debtt.abs() + 1.0))
def cg_f025_net_debt_leverage_core149_nd_log_v150_signal(debtt, cashneq, ebitda, ncfo, revenue, assets, marketcap, sharesbas):
    return _clean(_log((debtt - cashneq).clip(lower=1.0)))
