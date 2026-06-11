import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f060_non_cash_expense_mix_core75_pct_4q_v076_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_pct_change(_safe_div(dep_am, opex.abs() + 1.0), 4))
def cg_f060_non_cash_expense_mix_core76_pct_4q_v077_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_pct_change(_safe_div(sbc + dep_am, ocf.abs() + 1.0), 4))
def cg_f060_non_cash_expense_mix_core77_pct_4q_v078_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_pct_change(_safe_div(sbc, sbc + dep_am + 1.0), 4))
def cg_f060_non_cash_expense_mix_core78_pct_4q_v079_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_pct_change(_diff(_safe_div(sbc + dep_am, opex.abs() + 1.0), 4), 4))
def cg_f060_non_cash_expense_mix_core79_pct_4q_v080_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_pct_change(_z(_safe_div(sbc + dep_am, assets), 12), 4))

# core80-89: std 8q
def cg_f060_non_cash_expense_mix_core80_std_8q_v081_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_std(_safe_div(sbc + dep_am, assets), 8))
def cg_f060_non_cash_expense_mix_core81_std_8q_v082_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_std(_safe_div(sbc + dep_am, revenue), 8))
def cg_f060_non_cash_expense_mix_core82_std_8q_v083_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_std(_safe_div(sbc + dep_am, marketcap), 8))
def cg_f060_non_cash_expense_mix_core83_std_8q_v084_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_std(_safe_div(sbc + dep_am, opex.abs() + 1.0), 8))
def cg_f060_non_cash_expense_mix_core84_std_8q_v085_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_std(_safe_div(sbc, opex.abs() + 1.0), 8))
def cg_f060_non_cash_expense_mix_core85_std_8q_v086_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_std(_safe_div(dep_am, opex.abs() + 1.0), 8))
def cg_f060_non_cash_expense_mix_core86_std_8q_v087_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_std(_safe_div(sbc + dep_am, ocf.abs() + 1.0), 8))
def cg_f060_non_cash_expense_mix_core87_std_8q_v088_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_std(_safe_div(sbc, sbc + dep_am + 1.0), 8))
def cg_f060_non_cash_expense_mix_core88_std_8q_v089_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_std(_diff(_safe_div(sbc + dep_am, opex.abs() + 1.0), 4), 8))
def cg_f060_non_cash_expense_mix_core89_std_8q_v090_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_std(_z(_safe_div(sbc + dep_am, assets), 12), 8))

# core90-99: log (proxied by log of absolute change + 1)
def cg_f060_non_cash_expense_mix_core90_log_v091_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(sbc + dep_am, assets)
    return _clean(_log(base.abs() + 1.0))
def cg_f060_non_cash_expense_mix_core91_log_v092_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(sbc + dep_am, revenue)
    return _clean(_log(base.abs() + 1.0))
def cg_f060_non_cash_expense_mix_core92_log_v093_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(sbc + dep_am, marketcap)
    return _clean(_log(base.abs() + 1.0))
def cg_f060_non_cash_expense_mix_core93_log_v094_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(sbc + dep_am, opex.abs() + 1.0)
    return _clean(_log(base.abs() + 1.0))
def cg_f060_non_cash_expense_mix_core94_log_v095_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(sbc, opex.abs() + 1.0)
    return _clean(_log(base.abs() + 1.0))
def cg_f060_non_cash_expense_mix_core95_log_v096_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(dep_am, opex.abs() + 1.0)
    return _clean(_log(base.abs() + 1.0))
def cg_f060_non_cash_expense_mix_core96_log_v097_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(sbc + dep_am, ocf.abs() + 1.0)
    return _clean(_log(base.abs() + 1.0))
def cg_f060_non_cash_expense_mix_core97_log_v098_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(sbc, sbc + dep_am + 1.0)
    return _clean(_log(base.abs() + 1.0))
def cg_f060_non_cash_expense_mix_core98_log_v099_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _diff(_safe_div(sbc + dep_am, opex.abs() + 1.0), 4)
    return _clean(_log(base.abs() + 1.0))
def cg_f060_non_cash_expense_mix_core99_log_v100_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _z(_safe_div(sbc + dep_am, assets), 12)
    return _clean(_log(base.abs() + 1.0))

# core100-109: diff 1q
def cg_f060_non_cash_expense_mix_core100_diff_1q_v101_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_diff(_safe_div(sbc + dep_am, assets), 1))
def cg_f060_non_cash_expense_mix_core101_diff_1q_v102_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_diff(_safe_div(sbc + dep_am, revenue), 1))
def cg_f060_non_cash_expense_mix_core102_diff_1q_v103_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_diff(_safe_div(sbc + dep_am, marketcap), 1))
def cg_f060_non_cash_expense_mix_core103_diff_1q_v104_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_diff(_safe_div(sbc + dep_am, opex.abs() + 1.0), 1))
def cg_f060_non_cash_expense_mix_core104_diff_1q_v105_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_diff(_safe_div(sbc, opex.abs() + 1.0), 1))
def cg_f060_non_cash_expense_mix_core105_diff_1q_v106_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_diff(_safe_div(dep_am, opex.abs() + 1.0), 1))
def cg_f060_non_cash_expense_mix_core106_diff_1q_v107_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_diff(_safe_div(sbc + dep_am, ocf.abs() + 1.0), 1))
def cg_f060_non_cash_expense_mix_core107_diff_1q_v108_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_diff(_safe_div(sbc, sbc + dep_am + 1.0), 1))
def cg_f060_non_cash_expense_mix_core108_diff_1q_v109_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_diff(_diff(_safe_div(sbc + dep_am, opex.abs() + 1.0), 4), 1))
def cg_f060_non_cash_expense_mix_core109_diff_1q_v110_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_diff(_z(_safe_div(sbc + dep_am, assets), 12), 1))

# core110-119: slope 4q
def cg_f060_non_cash_expense_mix_core110_slope_4q_v111_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_slope(_safe_div(sbc + dep_am, assets), 4))
def cg_f060_non_cash_expense_mix_core111_slope_4q_v112_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_slope(_safe_div(sbc + dep_am, revenue), 4))
def cg_f060_non_cash_expense_mix_core112_slope_4q_v113_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_slope(_safe_div(sbc + dep_am, marketcap), 4))
def cg_f060_non_cash_expense_mix_core113_slope_4q_v114_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_slope(_safe_div(sbc + dep_am, opex.abs() + 1.0), 4))
def cg_f060_non_cash_expense_mix_core114_slope_4q_v115_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_slope(_safe_div(sbc, opex.abs() + 1.0), 4))
def cg_f060_non_cash_expense_mix_core115_slope_4q_v116_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_slope(_safe_div(dep_am, opex.abs() + 1.0), 4))
def cg_f060_non_cash_expense_mix_core116_slope_4q_v117_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_slope(_safe_div(sbc + dep_am, ocf.abs() + 1.0), 4))
def cg_f060_non_cash_expense_mix_core117_slope_4q_v118_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_slope(_safe_div(sbc, sbc + dep_am + 1.0), 4))
def cg_f060_non_cash_expense_mix_core118_slope_4q_v119_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_slope(_diff(_safe_div(sbc + dep_am, opex.abs() + 1.0), 4), 4))
def cg_f060_non_cash_expense_mix_core119_slope_4q_v120_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_slope(_z(_safe_div(sbc + dep_am, assets), 12), 4))

# core120-129: ewm 8q
def cg_f060_non_cash_expense_mix_core120_ewm_8q_v121_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_ewm(_safe_div(sbc + dep_am, assets), 8))
def cg_f060_non_cash_expense_mix_core121_ewm_8q_v122_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_ewm(_safe_div(sbc + dep_am, revenue), 8))
def cg_f060_non_cash_expense_mix_core122_ewm_8q_v123_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_ewm(_safe_div(sbc + dep_am, marketcap), 8))
def cg_f060_non_cash_expense_mix_core123_ewm_8q_v124_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_ewm(_safe_div(sbc + dep_am, opex.abs() + 1.0), 8))
def cg_f060_non_cash_expense_mix_core124_ewm_8q_v125_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_ewm(_safe_div(sbc, opex.abs() + 1.0), 8))
def cg_f060_non_cash_expense_mix_core125_ewm_8q_v126_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_ewm(_safe_div(dep_am, opex.abs() + 1.0), 8))
def cg_f060_non_cash_expense_mix_core126_ewm_8q_v127_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_ewm(_safe_div(sbc + dep_am, ocf.abs() + 1.0), 8))
def cg_f060_non_cash_expense_mix_core127_ewm_8q_v128_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_ewm(_safe_div(sbc, sbc + dep_am + 1.0), 8))
def cg_f060_non_cash_expense_mix_core128_ewm_8q_v129_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_ewm(_diff(_safe_div(sbc + dep_am, opex.abs() + 1.0), 4), 8))
def cg_f060_non_cash_expense_mix_core129_ewm_8q_v130_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_ewm(_z(_safe_div(sbc + dep_am, assets), 12), 8))

# core130-139: stability 12q
def cg_f060_non_cash_expense_mix_core130_stability_12q_v131_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(sbc + dep_am, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f060_non_cash_expense_mix_core131_stability_12q_v132_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(sbc + dep_am, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f060_non_cash_expense_mix_core132_stability_12q_v133_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(sbc + dep_am, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f060_non_cash_expense_mix_core133_stability_12q_v134_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(sbc + dep_am, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f060_non_cash_expense_mix_core134_stability_12q_v135_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(sbc, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f060_non_cash_expense_mix_core135_stability_12q_v136_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(dep_am, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f060_non_cash_expense_mix_core136_stability_12q_v137_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(sbc + dep_am, ocf.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f060_non_cash_expense_mix_core137_stability_12q_v138_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _safe_div(sbc, sbc + dep_am + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f060_non_cash_expense_mix_core138_stability_12q_v139_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _diff(_safe_div(sbc + dep_am, opex.abs() + 1.0), 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f060_non_cash_expense_mix_core139_stability_12q_v140_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    base = _z(_safe_div(sbc + dep_am, assets), 12)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# core140-149: raw levels
def cg_f060_non_cash_expense_mix_core140_non_cash_v141_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_safe_div(sbc + dep_am, assets))
def cg_f060_non_cash_expense_mix_core141_non_cash_rev_v142_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_safe_div(sbc + dep_am, revenue))
def cg_f060_non_cash_expense_mix_core142_non_cash_mc_v143_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_safe_div(sbc + dep_am, marketcap))
def cg_f060_non_cash_expense_mix_core143_non_cash_opex_v144_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_safe_div(sbc + dep_am, opex.abs() + 1.0))
def cg_f060_non_cash_expense_mix_core144_sbc_opex_v145_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_safe_div(sbc, opex.abs() + 1.0))
def cg_f060_non_cash_expense_mix_core145_dep_opex_v146_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_safe_div(dep_am, opex.abs() + 1.0))
def cg_f060_non_cash_expense_mix_core146_non_cash_ocf_v147_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_safe_div(sbc + dep_am, ocf.abs() + 1.0))
def cg_f060_non_cash_expense_mix_core147_sbc_mix_v148_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_safe_div(sbc, sbc + dep_am + 1.0))
def cg_f060_non_cash_expense_mix_core148_non_cash_yoy_v149_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_diff(_safe_div(sbc + dep_am, opex.abs() + 1.0), 4))
def cg_f060_non_cash_expense_mix_core149_non_cash_z_v150_signal(netinc, ocf, sbc, dep_am, assets, revenue, marketcap, opex):
    return _clean(_z(_safe_div(sbc + dep_am, assets), 12))
