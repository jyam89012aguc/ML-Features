import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f053_ebitda_margin_core75_pct_4q_v076_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(ebitda - netinc, revenue), 4))
def cg_f053_ebitda_margin_core76_pct_4q_v077_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_diff(ebitdamargin, 4), 4))
def cg_f053_ebitda_margin_core77_pct_4q_v078_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_pct_change(ebitda, 4), 4))
def cg_f053_ebitda_margin_core78_pct_4q_v079_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(ebitdamargin, _std(ebitdamargin, 4) + 1e-9), 4))
def cg_f053_ebitda_margin_core79_pct_4q_v080_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_log(ebitdamargin.clip(lower=0.001) + 1.0), 4))

# Block 80-89: std 8q
def cg_f053_ebitda_margin_core80_std_8q_v081_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(ebitdamargin, 8))
def cg_f053_ebitda_margin_core81_std_8q_v082_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(ebitda, assets), 8))
def cg_f053_ebitda_margin_core82_std_8q_v083_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(ebitda, marketcap), 8))
def cg_f053_ebitda_margin_core83_std_8q_v084_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(ebitda, equity.abs() + 1.0), 8))
def cg_f053_ebitda_margin_core84_std_8q_v085_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(ebitda, opex.abs() + 1.0), 8))
def cg_f053_ebitda_margin_core85_std_8q_v086_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(ebitda - netinc, revenue), 8))
def cg_f053_ebitda_margin_core86_std_8q_v087_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_diff(ebitdamargin, 4), 8))
def cg_f053_ebitda_margin_core87_std_8q_v088_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_pct_change(ebitda, 4), 8))
def cg_f053_ebitda_margin_core88_std_8q_v089_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(ebitdamargin, _std(ebitdamargin, 4) + 1e-9), 8))
def cg_f053_ebitda_margin_core89_std_8q_v090_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_log(ebitdamargin.clip(lower=0.001) + 1.0), 8))

# Block 90-99: log
def cg_f053_ebitda_margin_core90_log_v091_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(ebitdamargin.clip(lower=0.001) + 1.0))
def cg_f053_ebitda_margin_core91_log_v092_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(ebitda, assets).clip(lower=0.0001)))
def cg_f053_ebitda_margin_core92_log_v093_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(ebitda, marketcap).clip(lower=0.0001)))
def cg_f053_ebitda_margin_core93_log_v094_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(ebitda, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f053_ebitda_margin_core94_log_v095_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(ebitda, opex.abs() + 1.0).clip(lower=0.001)))
def cg_f053_ebitda_margin_core95_log_v096_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(ebitda - netinc, revenue).clip(lower=0.001) + 1.0))
def cg_f053_ebitda_margin_core96_log_v097_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_diff(ebitdamargin, 4).clip(lower=-0.9) + 1.1))
def cg_f053_ebitda_margin_core97_log_v098_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_pct_change(ebitda, 4).clip(lower=-0.9) + 1.1))
def cg_f053_ebitda_margin_core98_log_v099_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(ebitdamargin, _std(ebitdamargin, 4) + 1e-9).clip(lower=0.001)))
def cg_f053_ebitda_margin_core99_log_v100_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_mean(ebitdamargin, 4).clip(lower=0.001) + 1.0))

# Block 100-109: diff 1q
def cg_f053_ebitda_margin_core100_diff_1q_v101_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(ebitdamargin, 1))
def cg_f053_ebitda_margin_core101_diff_1q_v102_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(ebitda, assets), 1))
def cg_f053_ebitda_margin_core102_diff_1q_v103_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(ebitda, marketcap), 1))
def cg_f053_ebitda_margin_core103_diff_1q_v104_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(ebitda, equity.abs() + 1.0), 1))
def cg_f053_ebitda_margin_core104_diff_1q_v105_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(ebitda, opex.abs() + 1.0), 1))
def cg_f053_ebitda_margin_core105_diff_1q_v106_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(ebitda - netinc, revenue), 1))
def cg_f053_ebitda_margin_core106_diff_1q_v107_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_diff(ebitdamargin, 4), 1))
def cg_f053_ebitda_margin_core107_diff_1q_v108_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_pct_change(ebitda, 4), 1))
def cg_f053_ebitda_margin_core108_diff_1q_v109_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(ebitdamargin, _std(ebitdamargin, 4) + 1e-9), 1))
def cg_f053_ebitda_margin_core109_diff_1q_v110_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_log(ebitdamargin.clip(lower=0.001) + 1.0), 1))

# Block 110-119: slope 4q
def cg_f053_ebitda_margin_core110_slope_4q_v111_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(ebitdamargin, 4))
def cg_f053_ebitda_margin_core111_slope_4q_v112_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(ebitda, assets), 4))
def cg_f053_ebitda_margin_core112_slope_4q_v113_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(ebitda, marketcap), 4))
def cg_f053_ebitda_margin_core113_slope_4q_v114_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(ebitda, equity.abs() + 1.0), 4))
def cg_f053_ebitda_margin_core114_slope_4q_v115_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(ebitda, opex.abs() + 1.0), 4))
def cg_f053_ebitda_margin_core115_slope_4q_v116_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(ebitda - netinc, revenue), 4))
def cg_f053_ebitda_margin_core116_slope_4q_v117_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_diff(ebitdamargin, 4), 4))
def cg_f053_ebitda_margin_core117_slope_4q_v118_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_pct_change(ebitda, 4), 4))
def cg_f053_ebitda_margin_core118_slope_4q_v119_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(ebitdamargin, _std(ebitdamargin, 4) + 1e-9), 4))
def cg_f053_ebitda_margin_core119_slope_4q_v120_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_log(ebitdamargin.clip(lower=0.001) + 1.0), 4))

# Block 120-129: ewm 8q
def cg_f053_ebitda_margin_core120_ewm_8q_v121_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(ebitdamargin, 8))
def cg_f053_ebitda_margin_core121_ewm_8q_v122_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(ebitda, assets), 8))
def cg_f053_ebitda_margin_core122_ewm_8q_v123_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(ebitda, marketcap), 8))
def cg_f053_ebitda_margin_core123_ewm_8q_v124_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(ebitda, equity.abs() + 1.0), 8))
def cg_f053_ebitda_margin_core124_ewm_8q_v125_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(ebitda, opex.abs() + 1.0), 8))
def cg_f053_ebitda_margin_core125_ewm_8q_v126_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(ebitda - netinc, revenue), 8))
def cg_f053_ebitda_margin_core126_ewm_8q_v127_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_diff(ebitdamargin, 4), 8))
def cg_f053_ebitda_margin_core127_ewm_8q_v128_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_pct_change(ebitda, 4), 8))
def cg_f053_ebitda_margin_core128_ewm_8q_v129_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(ebitdamargin, _std(ebitdamargin, 4) + 1e-9), 8))
def cg_f053_ebitda_margin_core129_ewm_8q_v130_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_log(ebitdamargin.clip(lower=0.001) + 1.0), 8))

# Block 130-139: stability 12q
def cg_f053_ebitda_margin_core130_stability_12q_v131_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(_std(ebitdamargin, 12), _mean(ebitdamargin, 12).abs() + 1.0))
def cg_f053_ebitda_margin_core131_stability_12q_v132_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(ebitda, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f053_ebitda_margin_core132_stability_12q_v133_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(ebitda, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f053_ebitda_margin_core133_stability_12q_v134_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(ebitda, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f053_ebitda_margin_core134_stability_12q_v135_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(ebitda, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f053_ebitda_margin_core135_stability_12q_v136_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(ebitda - netinc, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f053_ebitda_margin_core136_stability_12q_v137_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    base = _diff(ebitdamargin, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f053_ebitda_margin_core137_stability_12q_v138_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    base = _pct_change(ebitda, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f053_ebitda_margin_core138_stability_12q_v139_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(ebitdamargin, _std(ebitdamargin, 4) + 1e-9)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f053_ebitda_margin_core139_stability_12q_v140_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    base = _log(ebitdamargin.clip(lower=0.001) + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f053_ebitda_margin_core140_level_v141_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(ebitdamargin)
def cg_f053_ebitda_margin_core141_ebitda_assets_v142_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(ebitda, assets))
def cg_f053_ebitda_margin_core142_ebitda_mcap_v143_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(ebitda, marketcap))
def cg_f053_ebitda_margin_core143_ebitda_equity_v144_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(ebitda, equity.abs() + 1.0))
def cg_f053_ebitda_margin_core144_ebitda_opex_v145_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(ebitda, opex.abs() + 1.0))
def cg_f053_ebitda_margin_core145_ebitda_ni_spread_v146_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(ebitda - netinc, revenue))
def cg_f053_ebitda_margin_core146_ebm_diff_v147_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(ebitdamargin, 4))
def cg_f053_ebitda_margin_core147_ebitda_growth_v148_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(ebitda, 4))
def cg_f053_ebitda_margin_core148_ebm_sharpe_v149_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(ebitdamargin, _std(ebitdamargin, 4) + 1e-9))
def cg_f053_ebitda_margin_core149_ebm_log_v150_signal(ebitdamargin, ebitda, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(ebitdamargin.clip(lower=0.001) + 1.0))
