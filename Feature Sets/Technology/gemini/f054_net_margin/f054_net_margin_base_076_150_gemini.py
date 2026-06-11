import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f054_net_margin_core75_pct_4q_v076_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_pct_change(_safe_div(netinc, ebitda.clip(lower=0) + 1.0), 4))
def cg_f054_net_margin_core76_pct_4q_v077_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_pct_change(_diff(netmargin, 4), 4))
def cg_f054_net_margin_core77_pct_4q_v078_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_pct_change(_pct_change(netinc, 4), 4))
def cg_f054_net_margin_core78_pct_4q_v079_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_pct_change(_safe_div(netmargin, _std(netmargin, 4) + 1e-9), 4))
def cg_f054_net_margin_core79_pct_4q_v080_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_pct_change(_log(netmargin.clip(lower=0.001) + 1.0), 4))

# Block 80-89: std 8q
def cg_f054_net_margin_core80_std_8q_v081_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_std(netmargin, 8))
def cg_f054_net_margin_core81_std_8q_v082_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_std(_safe_div(netinc, assets), 8))
def cg_f054_net_margin_core82_std_8q_v083_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_std(_safe_div(netinc, marketcap), 8))
def cg_f054_net_margin_core83_std_8q_v084_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_std(_safe_div(netinc, equity.abs() + 1.0), 8))
def cg_f054_net_margin_core84_std_8q_v085_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_std(_safe_div(netinc, opex.abs() + 1.0), 8))
def cg_f054_net_margin_core85_std_8q_v086_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_std(_safe_div(netinc, ebitda.clip(lower=0) + 1.0), 8))
def cg_f054_net_margin_core86_std_8q_v087_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_std(_diff(netmargin, 4), 8))
def cg_f054_net_margin_core87_std_8q_v088_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_std(_pct_change(netinc, 4), 8))
def cg_f054_net_margin_core88_std_8q_v089_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_std(_safe_div(netmargin, _std(netmargin, 4) + 1e-9), 8))
def cg_f054_net_margin_core89_std_8q_v090_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_std(_log(netmargin.clip(lower=0.001) + 1.0), 8))

# Block 90-99: log
def cg_f054_net_margin_core90_log_v091_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_log(netmargin.clip(lower=0.001) + 1.0))
def cg_f054_net_margin_core91_log_v092_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_log(_safe_div(netinc, assets).clip(lower=0.0001)))
def cg_f054_net_margin_core92_log_v093_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_log(_safe_div(netinc, marketcap).clip(lower=0.0001)))
def cg_f054_net_margin_core93_log_v094_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_log(_safe_div(netinc, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f054_net_margin_core95_log_v095_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_log(_safe_div(netinc, opex.abs() + 1.0).clip(lower=0.001)))
def cg_f054_net_margin_core95_log_v096_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_log(_safe_div(netinc, ebitda.clip(lower=0) + 1.0).clip(lower=0.001)))
def cg_f054_net_margin_core96_log_v097_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_log(_diff(netmargin, 4).clip(lower=-0.9) + 1.1))
def cg_f054_net_margin_core97_log_v098_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_log(_pct_change(netinc, 4).clip(lower=-0.9) + 1.1))
def cg_f054_net_margin_core98_log_v099_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_log(_safe_div(netmargin, _std(netmargin, 4) + 1e-9).clip(lower=0.001)))
def cg_f054_net_margin_core99_log_v100_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_log(_mean(netmargin, 4).clip(lower=0.001) + 1.0))

# Block 100-109: diff 1q
def cg_f054_net_margin_core100_diff_1q_v101_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_diff(netmargin, 1))
def cg_f054_net_margin_core101_diff_1q_v102_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_diff(_safe_div(netinc, assets), 1))
def cg_f054_net_margin_core102_diff_1q_v103_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_diff(_safe_div(netinc, marketcap), 1))
def cg_f054_net_margin_core103_diff_1q_v104_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_diff(_safe_div(netinc, equity.abs() + 1.0), 1))
def cg_f054_net_margin_core104_diff_1q_v105_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_diff(_safe_div(netinc, opex.abs() + 1.0), 1))
def cg_f054_net_margin_core105_diff_1q_v106_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_diff(_safe_div(netinc, ebitda.clip(lower=0) + 1.0), 1))
def cg_f054_net_margin_core106_diff_1q_v107_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_diff(_diff(netmargin, 4), 1))
def cg_f054_net_margin_core107_diff_1q_v108_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_diff(_pct_change(netinc, 4), 1))
def cg_f054_net_margin_core108_diff_1q_v109_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_diff(_safe_div(netmargin, _std(netmargin, 4) + 1e-9), 1))
def cg_f054_net_margin_core109_diff_1q_v110_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_diff(_log(netmargin.clip(lower=0.001) + 1.0), 1))

# Block 110-119: slope 4q
def cg_f054_net_margin_core110_slope_4q_v111_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_slope(netmargin, 4))
def cg_f054_net_margin_core111_slope_4q_v112_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_slope(_safe_div(netinc, assets), 4))
def cg_f054_net_margin_core112_slope_4q_v113_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_slope(_safe_div(netinc, marketcap), 4))
def cg_f054_net_margin_core113_slope_4q_v114_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_slope(_safe_div(netinc, equity.abs() + 1.0), 4))
def cg_f054_net_margin_core114_slope_4q_v115_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_slope(_safe_div(netinc, opex.abs() + 1.0), 4))
def cg_f054_net_margin_core115_slope_4q_v116_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_slope(_safe_div(netinc, ebitda.clip(lower=0) + 1.0), 4))
def cg_f054_net_margin_core116_slope_4q_v117_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_slope(_diff(netmargin, 4), 4))
def cg_f054_net_margin_core117_slope_4q_v118_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_slope(_pct_change(netinc, 4), 4))
def cg_f054_net_margin_core118_slope_4q_v119_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_slope(_safe_div(netmargin, _std(netmargin, 4) + 1e-9), 4))
def cg_f054_net_margin_core119_slope_4q_v120_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_slope(_log(netmargin.clip(lower=0.001) + 1.0), 4))

# Block 120-129: ewm 8q
def cg_f054_net_margin_core120_ewm_8q_v121_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_ewm(netmargin, 8))
def cg_f054_net_margin_core121_ewm_8q_v122_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_ewm(_safe_div(netinc, assets), 8))
def cg_f054_net_margin_core122_ewm_8q_v123_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_ewm(_safe_div(netinc, marketcap), 8))
def cg_f054_net_margin_core123_ewm_8q_v124_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_ewm(_safe_div(netinc, equity.abs() + 1.0), 8))
def cg_f054_net_margin_core124_ewm_8q_v125_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_ewm(_safe_div(netinc, opex.abs() + 1.0), 8))
def cg_f054_net_margin_core125_ewm_8q_v126_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_ewm(_safe_div(netinc, ebitda.clip(lower=0) + 1.0), 8))
def cg_f054_net_margin_core126_ewm_8q_v127_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_ewm(_diff(netmargin, 4), 8))
def cg_f054_net_margin_core127_ewm_8q_v128_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_ewm(_pct_change(netinc, 4), 8))
def cg_f054_net_margin_core128_ewm_8q_v129_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_ewm(_safe_div(netmargin, _std(netmargin, 4) + 1e-9), 8))
def cg_f054_net_margin_core129_ewm_8q_v130_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_ewm(_log(netmargin.clip(lower=0.001) + 1.0), 8))

# Block 130-139: stability 12q
def cg_f054_net_margin_core130_stability_12q_v131_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_safe_div(_std(netmargin, 12), _mean(netmargin, 12).abs() + 1.0))
def cg_f054_net_margin_core131_stability_12q_v132_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    base = _safe_div(netinc, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f054_net_margin_core132_stability_12q_v133_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    base = _safe_div(netinc, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f054_net_margin_core133_stability_12q_v134_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    base = _safe_div(netinc, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f054_net_margin_core134_stability_12q_v135_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    base = _safe_div(netinc, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f054_net_margin_core135_stability_12q_v136_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    base = _safe_div(netinc, ebitda.clip(lower=0) + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f054_net_margin_core136_stability_12q_v137_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    base = _diff(netmargin, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f054_net_margin_core137_stability_12q_v138_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    base = _pct_change(netinc, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f054_net_margin_core138_stability_12q_v139_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    base = _safe_div(netmargin, _std(netmargin, 4) + 1e-9)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f054_net_margin_core139_stability_12q_v140_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    base = _log(netmargin.clip(lower=0.001) + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f054_net_margin_core140_level_v141_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(netmargin)
def cg_f054_net_margin_core141_ni_assets_v142_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_safe_div(netinc, assets))
def cg_f054_net_margin_core142_ni_mcap_v143_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_safe_div(netinc, marketcap))
def cg_f054_net_margin_core143_ni_equity_v144_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_safe_div(netinc, equity.abs() + 1.0))
def cg_f054_net_margin_core144_ni_opex_v145_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_safe_div(netinc, opex.abs() + 1.0))
def cg_f054_net_margin_core145_ni_ebitda_v146_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_safe_div(netinc, ebitda.clip(lower=0) + 1.0))
def cg_f054_net_margin_core146_nm_diff_v147_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_diff(netmargin, 4))
def cg_f054_net_margin_core147_ni_growth_v148_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_pct_change(netinc, 4))
def cg_f054_net_margin_core148_nm_sharpe_v149_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_safe_div(netmargin, _std(netmargin, 4) + 1e-9))
def cg_f054_net_margin_core149_nm_log_v150_signal(netmargin, netinc, revenue, assets, marketcap, opex, equity, ebitda):
    return _clean(_log(netmargin.clip(lower=0.001) + 1.0))
