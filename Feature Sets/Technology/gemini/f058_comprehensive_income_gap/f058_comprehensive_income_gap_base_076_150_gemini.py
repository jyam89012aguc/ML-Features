import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f058_comprehensive_income_gap_core75_pct_4q_v076_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_safe_div(compinc - netinc, netinc.abs() + 1e-9), 4))
def cg_f058_comprehensive_income_gap_core76_pct_4q_v077_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_safe_div(compinc, ncfo), 4))
def cg_f058_comprehensive_income_gap_core77_pct_4q_v078_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_safe_div(compinc, fcf), 4))
def cg_f058_comprehensive_income_gap_core78_pct_4q_v079_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_pct_change(_diff(compinc - netinc, 4), 4))
def cg_f058_comprehensive_income_gap_core79_pct_4q_v080_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    gap = compinc - netinc
    return _clean(_pct_change(_safe_div(gap, _std(gap, 4) + 1e-9), 4))

# Block 80-89: std 8q
def cg_f058_comprehensive_income_gap_core80_std_8q_v081_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_std(compinc - netinc, 8))
def cg_f058_comprehensive_income_gap_core81_std_8q_v082_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_std(_safe_div(compinc - netinc, assets), 8))
def cg_f058_comprehensive_income_gap_core82_std_8q_v083_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_std(_safe_div(compinc - netinc, equity.abs() + 1.0), 8))
def cg_f058_comprehensive_income_gap_core83_std_8q_v084_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_std(_safe_div(compinc - netinc, revenue), 8))
def cg_f058_comprehensive_income_gap_core84_std_8q_v085_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_std(_safe_div(compinc - netinc, marketcap), 8))
def cg_f058_comprehensive_income_gap_core85_std_8q_v086_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_std(_safe_div(compinc - netinc, netinc.abs() + 1e-9), 8))
def cg_f058_comprehensive_income_gap_core86_std_8q_v087_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_std(_safe_div(compinc, ncfo), 8))
def cg_f058_comprehensive_income_gap_core87_std_8q_v088_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_std(_safe_div(compinc, fcf), 8))
def cg_f058_comprehensive_income_gap_core88_std_8q_v089_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_std(_diff(compinc - netinc, 4), 8))
def cg_f058_comprehensive_income_gap_core89_std_8q_v090_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    gap = compinc - netinc
    return _clean(_std(_safe_div(gap, _std(gap, 4) + 1e-9), 8))

# Block 90-99: log
def cg_f058_comprehensive_income_gap_core90_log_v091_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_log((compinc - netinc).clip(lower=0.001) + 1.0))
def cg_f058_comprehensive_income_gap_core91_log_v092_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_log(_safe_div(compinc - netinc, assets).clip(lower=0.0001)))
def cg_f058_comprehensive_income_gap_core92_log_v093_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_log(_safe_div(compinc - netinc, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f058_comprehensive_income_gap_core93_log_v094_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_log(_safe_div(compinc - netinc, revenue).clip(lower=0.0001)))
def cg_f058_comprehensive_income_gap_core94_log_v095_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_log(_safe_div(compinc - netinc, marketcap).clip(lower=0.0001)))
def cg_f058_comprehensive_income_gap_core95_log_v096_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_log(_safe_div(compinc - netinc, netinc.abs() + 1e-9).clip(lower=0.001)))
def cg_f058_comprehensive_income_gap_core96_log_v097_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_log(_safe_div(compinc, ncfo).clip(lower=0.001)))
def cg_f058_comprehensive_income_gap_core97_log_v098_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_log(_safe_div(compinc, fcf).clip(lower=0.001)))
def cg_f058_comprehensive_income_gap_core98_log_v099_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_log(_diff(compinc - netinc, 4).clip(lower=-0.9) + 1.1))
def cg_f058_comprehensive_income_gap_core99_log_v100_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    gap = compinc - netinc
    return _clean(_log(_safe_div(gap, _std(gap, 4) + 1e-9).clip(lower=0.001)))

# Block 100-109: diff 1q
def cg_f058_comprehensive_income_gap_core100_diff_1q_v101_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_diff(compinc - netinc, 1))
def cg_f058_comprehensive_income_gap_core101_diff_1q_v102_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_diff(_safe_div(compinc - netinc, assets), 1))
def cg_f058_comprehensive_income_gap_core102_diff_1q_v103_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_diff(_safe_div(compinc - netinc, equity.abs() + 1.0), 1))
def cg_f058_comprehensive_income_gap_core103_diff_1q_v104_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_diff(_safe_div(compinc - netinc, revenue), 1))
def cg_f058_comprehensive_income_gap_core104_diff_1q_v105_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_diff(_safe_div(compinc - netinc, marketcap), 1))
def cg_f058_comprehensive_income_gap_core105_diff_1q_v106_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_diff(_safe_div(compinc - netinc, netinc.abs() + 1e-9), 1))
def cg_f058_comprehensive_income_gap_core106_diff_1q_v107_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_diff(_safe_div(compinc, ncfo), 1))
def cg_f058_comprehensive_income_gap_core107_diff_1q_v108_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_diff(_safe_div(compinc, fcf), 1))
def cg_f058_comprehensive_income_gap_core108_diff_1q_v109_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_diff(_diff(compinc - netinc, 4), 1))
def cg_f058_comprehensive_income_gap_core109_diff_1q_v110_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    gap = compinc - netinc
    return _clean(_diff(_safe_div(gap, _std(gap, 4) + 1e-9), 1))

# Block 110-119: slope 4q
def cg_f058_comprehensive_income_gap_core110_slope_4q_v111_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_slope(compinc - netinc, 4))
def cg_f058_comprehensive_income_gap_core111_slope_4q_v112_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_slope(_safe_div(compinc - netinc, assets), 4))
def cg_f058_comprehensive_income_gap_core112_slope_4q_v113_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_slope(_safe_div(compinc - netinc, equity.abs() + 1.0), 4))
def cg_f058_comprehensive_income_gap_core113_slope_4q_v114_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_slope(_safe_div(compinc - netinc, revenue), 4))
def cg_f058_comprehensive_income_gap_core114_slope_4q_v115_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_slope(_safe_div(compinc - netinc, marketcap), 4))
def cg_f058_comprehensive_income_gap_core115_slope_4q_v116_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_slope(_safe_div(compinc - netinc, netinc.abs() + 1e-9), 4))
def cg_f058_comprehensive_income_gap_core116_slope_4q_v117_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_slope(_safe_div(compinc, ncfo), 4))
def cg_f058_comprehensive_income_gap_core117_slope_4q_v118_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_slope(_safe_div(compinc, fcf), 4))
def cg_f058_comprehensive_income_gap_core118_slope_4q_v119_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_slope(_diff(compinc - netinc, 4), 4))
def cg_f058_comprehensive_income_gap_core119_slope_4q_v120_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    gap = compinc - netinc
    return _clean(_slope(_safe_div(gap, _std(gap, 4) + 1e-9), 4))

# Block 120-129: ewm 8q
def cg_f058_comprehensive_income_gap_core120_ewm_8q_v121_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_ewm(compinc - netinc, 8))
def cg_f058_comprehensive_income_gap_core121_ewm_8q_v122_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_ewm(_safe_div(compinc - netinc, assets), 8))
def cg_f058_comprehensive_income_gap_core122_ewm_8q_v123_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_ewm(_safe_div(compinc - netinc, equity.abs() + 1.0), 8))
def cg_f058_comprehensive_income_gap_core123_ewm_8q_v124_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_ewm(_safe_div(compinc - netinc, revenue), 8))
def cg_f058_comprehensive_income_gap_core124_ewm_8q_v125_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_ewm(_safe_div(compinc - netinc, marketcap), 8))
def cg_f058_comprehensive_income_gap_core125_ewm_8q_v126_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_ewm(_safe_div(compinc - netinc, netinc.abs() + 1e-9), 8))
def cg_f058_comprehensive_income_gap_core126_ewm_8q_v127_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_ewm(_safe_div(compinc, ncfo), 8))
def cg_f058_comprehensive_income_gap_core127_ewm_8q_v128_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_ewm(_safe_div(compinc, fcf), 8))
def cg_f058_comprehensive_income_gap_core128_ewm_8q_v129_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_ewm(_diff(compinc - netinc, 4), 8))
def cg_f058_comprehensive_income_gap_core129_ewm_8q_v130_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    gap = compinc - netinc
    return _clean(_ewm(_safe_div(gap, _std(gap, 4) + 1e-9), 8))

# Block 130-139: stability 12q
def cg_f058_comprehensive_income_gap_core130_stability_12q_v131_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    base = compinc - netinc
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f058_comprehensive_income_gap_core131_stability_12q_v132_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    base = _safe_div(compinc - netinc, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f058_comprehensive_income_gap_core132_stability_12q_v133_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    base = _safe_div(compinc - netinc, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f058_comprehensive_income_gap_core133_stability_12q_v134_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    base = _safe_div(compinc - netinc, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f058_comprehensive_income_gap_core134_stability_12q_v135_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    base = _safe_div(compinc - netinc, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f058_comprehensive_income_gap_core135_stability_12q_v136_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    base = _safe_div(compinc - netinc, netinc.abs() + 1e-9)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f058_comprehensive_income_gap_core136_stability_12q_v137_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    base = _safe_div(compinc, ncfo)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f058_comprehensive_income_gap_core137_stability_12q_v138_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    base = _safe_div(compinc, fcf)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f058_comprehensive_income_gap_core138_stability_12q_v139_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    base = _diff(compinc - netinc, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f058_comprehensive_income_gap_core139_stability_12q_v140_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    gap = compinc - netinc
    base = _safe_div(gap, _std(gap, 4) + 1e-9)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f058_comprehensive_income_gap_core140_level_v141_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(compinc - netinc)
def cg_f058_comprehensive_income_gap_core141_to_assets_v142_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_safe_div(compinc - netinc, assets))
def cg_f058_comprehensive_income_gap_core142_to_equity_v143_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_safe_div(compinc - netinc, equity.abs() + 1.0))
def cg_f058_comprehensive_income_gap_core143_to_revenue_v144_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_safe_div(compinc - netinc, revenue))
def cg_f058_comprehensive_income_gap_core144_to_mcap_v145_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_safe_div(compinc - netinc, marketcap))
def cg_f058_comprehensive_income_gap_core145_to_netinc_v146_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_safe_div(compinc - netinc, netinc.abs() + 1e-9))
def cg_f058_comprehensive_income_gap_core146_compinc_to_ncfo_v147_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_safe_div(compinc, ncfo))
def cg_f058_comprehensive_income_gap_core147_compinc_to_fcf_v148_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_safe_div(compinc, fcf))
def cg_f058_comprehensive_income_gap_core148_diff_v149_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    return _clean(_diff(compinc - netinc, 4))
def cg_f058_comprehensive_income_gap_core149_sharpe_v150_signal(netinc, compinc, revenue, assets, marketcap, equity, fcf, ncfo):
    gap = compinc - netinc
    return _clean(_safe_div(gap, _std(gap, 4) + 1e-9))
