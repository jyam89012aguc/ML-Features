import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f045_receivables_payables_core75_pct_4q_v076_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_pct_change(_safe_div(payables, cor), 4))
def cg_f045_receivables_payables_core76_pct_4q_v077_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    net_working = receivables - payables
    return _clean(_pct_change(_safe_div(net_working, assets), 4))
def cg_f045_receivables_payables_core77_pct_4q_v078_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_pct_change(_pct_change(receivables, 4), 4))
def cg_f045_receivables_payables_core78_pct_4q_v079_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_pct_change(_pct_change(payables, 4), 4))
def cg_f045_receivables_payables_core79_pct_4q_v080_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    net_working = receivables - payables
    return _clean(_pct_change(_log(net_working.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f045_receivables_payables_core80_std_8q_v081_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_std(receivables, 8))
def cg_f045_receivables_payables_core81_std_8q_v082_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_std(payables, 8))
def cg_f045_receivables_payables_core82_std_8q_v083_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_std(_safe_div(receivables, assets), 8))
def cg_f045_receivables_payables_core83_std_8q_v084_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_std(_safe_div(payables, assets), 8))
def cg_f045_receivables_payables_core84_std_8q_v085_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_std(_safe_div(receivables, revenue), 8))
def cg_f045_receivables_payables_core85_std_8q_v086_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_std(_safe_div(payables, cor), 8))
def cg_f045_receivables_payables_core86_std_8q_v087_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    net_working = receivables - payables
    return _clean(_std(_safe_div(net_working, assets), 8))
def cg_f045_receivables_payables_core87_std_8q_v088_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_std(_pct_change(receivables, 4), 8))
def cg_f045_receivables_payables_core88_std_8q_v089_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_std(_pct_change(payables, 4), 8))
def cg_f045_receivables_payables_core89_std_8q_v090_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    net_working = receivables - payables
    return _clean(_std(_log(net_working.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f045_receivables_payables_core90_log_v091_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_log(receivables.clip(lower=1.0)))
def cg_f045_receivables_payables_core91_log_v092_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_log(payables.clip(lower=1.0)))
def cg_f045_receivables_payables_core92_log_v093_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_log(_safe_div(receivables, assets).clip(lower=0.0001)))
def cg_f045_receivables_payables_core93_log_v094_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_log(_safe_div(payables, assets).clip(lower=0.0001)))
def cg_f045_receivables_payables_core94_log_v095_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_log(_safe_div(receivables, revenue).clip(lower=0.0001)))
def cg_f045_receivables_payables_core95_log_v096_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_log(_safe_div(payables, cor).clip(lower=0.001)))
def cg_f045_receivables_payables_core96_log_v097_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    net_working = receivables - payables
    return _clean(_log(_safe_div(net_working, assets).abs().clip(lower=0.001)))
def cg_f045_receivables_payables_core97_log_v098_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_log(_pct_change(receivables, 4).clip(lower=-0.9) + 1.1))
def cg_f045_receivables_payables_core98_log_v099_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_log(_pct_change(payables, 4).clip(lower=-0.9) + 1.1))
def cg_f045_receivables_payables_core99_log_v100_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_log(assets.clip(lower=1.0)))

# Block 100-109: diff 1q
def cg_f045_receivables_payables_core100_diff_1q_v101_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_diff(receivables, 1))
def cg_f045_receivables_payables_core101_diff_1q_v102_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_diff(payables, 1))
def cg_f045_receivables_payables_core102_diff_1q_v103_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_diff(_safe_div(receivables, assets), 1))
def cg_f045_receivables_payables_core103_diff_1q_v104_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_diff(_safe_div(payables, assets), 1))
def cg_f045_receivables_payables_core104_diff_1q_v105_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_diff(_safe_div(receivables, revenue), 1))
def cg_f045_receivables_payables_core105_diff_1q_v106_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_diff(_safe_div(payables, cor), 1))
def cg_f045_receivables_payables_core106_diff_1q_v107_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    net_working = receivables - payables
    return _clean(_diff(_safe_div(net_working, assets), 1))
def cg_f045_receivables_payables_core107_diff_1q_v108_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_diff(_pct_change(receivables, 4), 1))
def cg_f045_receivables_payables_core108_diff_1q_v109_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_diff(_pct_change(payables, 4), 1))
def cg_f045_receivables_payables_core109_diff_1q_v110_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    net_working = receivables - payables
    return _clean(_diff(_log(net_working.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f045_receivables_payables_core110_slope_4q_v111_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_slope(receivables, 4))
def cg_f045_receivables_payables_core111_slope_4q_v112_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_slope(payables, 4))
def cg_f045_receivables_payables_core112_slope_4q_v113_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_slope(_safe_div(receivables, assets), 4))
def cg_f045_receivables_payables_core113_slope_4q_v114_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_slope(_safe_div(payables, assets), 4))
def cg_f045_receivables_payables_core114_slope_4q_v115_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_slope(_safe_div(receivables, revenue), 4))
def cg_f045_receivables_payables_core115_slope_4q_v116_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_slope(_safe_div(payables, cor), 4))
def cg_f045_receivables_payables_core116_slope_4q_v117_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    net_working = receivables - payables
    return _clean(_slope(_safe_div(net_working, assets), 4))
def cg_f045_receivables_payables_core117_slope_4q_v118_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_slope(_pct_change(receivables, 4), 4))
def cg_f045_receivables_payables_core118_slope_4q_v119_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_slope(_pct_change(payables, 4), 4))
def cg_f045_receivables_payables_core119_slope_4q_v120_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    net_working = receivables - payables
    return _clean(_slope(_log(net_working.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f045_receivables_payables_core120_ewm_8q_v121_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_ewm(receivables, 8))
def cg_f045_receivables_payables_core121_ewm_8q_v122_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_ewm(payables, 8))
def cg_f045_receivables_payables_core122_ewm_8q_v123_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_ewm(_safe_div(receivables, assets), 8))
def cg_f045_receivables_payables_core123_ewm_8q_v124_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_ewm(_safe_div(payables, assets), 8))
def cg_f045_receivables_payables_core124_ewm_8q_v125_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_ewm(_safe_div(receivables, revenue), 8))
def cg_f045_receivables_payables_core125_ewm_8q_v126_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_ewm(_safe_div(payables, cor), 8))
def cg_f045_receivables_payables_core126_ewm_8q_v127_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    net_working = receivables - payables
    return _clean(_ewm(_safe_div(net_working, assets), 8))
def cg_f045_receivables_payables_core127_ewm_8q_v128_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_ewm(_pct_change(receivables, 4), 8))
def cg_f045_receivables_payables_core128_ewm_8q_v129_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_ewm(_pct_change(payables, 4), 8))
def cg_f045_receivables_payables_core129_ewm_8q_v130_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    net_working = receivables - payables
    return _clean(_ewm(_log(net_working.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f045_receivables_payables_core130_stability_12q_v131_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_safe_div(_std(receivables, 12), _mean(receivables, 12).abs() + 1.0))
def cg_f045_receivables_payables_core131_stability_12q_v132_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_safe_div(_std(payables, 12), _mean(payables, 12).abs() + 1.0))
def cg_f045_receivables_payables_core132_stability_12q_v133_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    base = _safe_div(receivables, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f045_receivables_payables_core133_stability_12q_v134_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    base = _safe_div(payables, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f045_receivables_payables_core134_stability_12q_v135_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    base = _safe_div(receivables, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f045_receivables_payables_core135_stability_12q_v136_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    base = _safe_div(payables, cor)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f045_receivables_payables_core136_stability_12q_v137_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    net_working = receivables - payables
    base = _safe_div(net_working, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f045_receivables_payables_core137_stability_12q_v138_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    base = _pct_change(receivables, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f045_receivables_payables_core138_stability_12q_v139_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    base = _pct_change(payables, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f045_receivables_payables_core139_stability_12q_v140_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    net_working = receivables - payables
    base = _log(net_working.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f045_receivables_payables_core140_rec_level_v141_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(receivables)
def cg_f045_receivables_payables_core141_pay_level_v142_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(payables)
def cg_f045_receivables_payables_core142_rec_assets_v143_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_safe_div(receivables, assets))
def cg_f045_receivables_payables_core143_pay_assets_v144_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_safe_div(payables, assets))
def cg_f045_receivables_payables_core144_rec_rev_v145_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_safe_div(receivables, revenue))
def cg_f045_receivables_payables_core145_pay_cor_v146_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_safe_div(payables, cor))
def cg_f045_receivables_payables_core146_net_working_v147_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_safe_div(receivables - payables, assets))
def cg_f045_receivables_payables_core147_rec_growth_v148_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_pct_change(receivables, 4))
def cg_f045_receivables_payables_core148_pay_growth_v149_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_pct_change(payables, 4))
def cg_f045_receivables_payables_core149_net_growth_v150_signal(receivables, payables, assets, revenue, cor, marketcap, equity, opex):
    return _clean(_pct_change(receivables - payables, 4))
