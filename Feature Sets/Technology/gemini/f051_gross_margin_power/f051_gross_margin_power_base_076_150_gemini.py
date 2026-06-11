import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f051_gross_margin_power_core75_pct_4q_v076_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(gp - netinc, revenue), 4))
def cg_f051_gross_margin_power_core76_pct_4q_v077_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_diff(grossmargin, 4), 4))
def cg_f051_gross_margin_power_core77_pct_4q_v078_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_pct_change(gp, 4), 4))
def cg_f051_gross_margin_power_core78_pct_4q_v079_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(grossmargin, _std(grossmargin, 4) + 1e-9), 4))
def cg_f051_gross_margin_power_core79_pct_4q_v080_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_log(grossmargin.clip(lower=0.001) + 1.0), 4))

# Block 80-89: std 8q
def cg_f051_gross_margin_power_core80_std_8q_v081_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(grossmargin, 8))
def cg_f051_gross_margin_power_core81_std_8q_v082_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(gp, assets), 8))
def cg_f051_gross_margin_power_core82_std_8q_v083_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(gp, marketcap), 8))
def cg_f051_gross_margin_power_core83_std_8q_v084_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(gp, equity.abs() + 1.0), 8))
def cg_f051_gross_margin_power_core84_std_8q_v085_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(gp, opex.abs() + 1.0), 8))
def cg_f051_gross_margin_power_core85_std_8q_v086_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(gp - netinc, revenue), 8))
def cg_f051_gross_margin_power_core86_std_8q_v087_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_diff(grossmargin, 4), 8))
def cg_f051_gross_margin_power_core87_std_8q_v088_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_pct_change(gp, 4), 8))
def cg_f051_gross_margin_power_core88_std_8q_v089_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(grossmargin, _std(grossmargin, 4) + 1e-9), 8))
def cg_f051_gross_margin_power_core89_std_8q_v090_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_log(grossmargin.clip(lower=0.001) + 1.0), 8))

# Block 90-99: log
def cg_f051_gross_margin_power_core90_log_v091_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(grossmargin.clip(lower=0.001) + 1.0))
def cg_f051_gross_margin_power_core91_log_v092_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(gp, assets).clip(lower=0.0001)))
def cg_f051_gross_margin_power_core92_log_v093_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(gp, marketcap).clip(lower=0.0001)))
def cg_f051_gross_margin_power_core93_log_v094_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(gp, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f051_gross_margin_power_core94_log_v095_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(gp, opex.abs() + 1.0).clip(lower=0.001)))
def cg_f051_gross_margin_power_core95_log_v096_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(gp - netinc, revenue).clip(lower=0.001) + 1.0))
def cg_f051_gross_margin_power_core96_log_v097_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_diff(grossmargin, 4).clip(lower=-0.9) + 1.1))
def cg_f051_gross_margin_power_core97_log_v098_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_pct_change(gp, 4).clip(lower=-0.9) + 1.1))
def cg_f051_gross_margin_power_core98_log_v099_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(grossmargin, _std(grossmargin, 4) + 1e-9).clip(lower=0.001)))
def cg_f051_gross_margin_power_core99_log_v100_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_mean(grossmargin, 4).clip(lower=0.001) + 1.0))

# Block 100-109: diff 1q
def cg_f051_gross_margin_power_core100_diff_1q_v101_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(grossmargin, 1))
def cg_f051_gross_margin_power_core101_diff_1q_v102_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(gp, assets), 1))
def cg_f051_gross_margin_power_core102_diff_1q_v103_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(gp, marketcap), 1))
def cg_f051_gross_margin_power_core103_diff_1q_v104_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(gp, equity.abs() + 1.0), 1))
def cg_f051_gross_margin_power_core104_diff_1q_v105_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(gp, opex.abs() + 1.0), 1))
def cg_f051_gross_margin_power_core105_diff_1q_v106_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(gp - netinc, revenue), 1))
def cg_f051_gross_margin_power_core106_diff_1q_v107_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_diff(grossmargin, 4), 1))
def cg_f051_gross_margin_power_core107_diff_1q_v108_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_pct_change(gp, 4), 1))
def cg_f051_gross_margin_power_core108_diff_1q_v109_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(grossmargin, _std(grossmargin, 4) + 1e-9), 1))
def cg_f051_gross_margin_power_core109_diff_1q_v110_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_log(grossmargin.clip(lower=0.001) + 1.0), 1))

# Block 110-119: slope 4q
def cg_f051_gross_margin_power_core110_slope_4q_v111_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(grossmargin, 4))
def cg_f051_gross_margin_power_core111_slope_4q_v112_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(gp, assets), 4))
def cg_f051_gross_margin_power_core112_slope_4q_v113_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(gp, marketcap), 4))
def cg_f051_gross_margin_power_core113_slope_4q_v114_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(gp, equity.abs() + 1.0), 4))
def cg_f051_gross_margin_power_core114_slope_4q_v115_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(gp, opex.abs() + 1.0), 4))
def cg_f051_gross_margin_power_core115_slope_4q_v116_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(gp - netinc, revenue), 4))
def cg_f051_gross_margin_power_core116_slope_4q_v117_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_diff(grossmargin, 4), 4))
def cg_f051_gross_margin_power_core117_slope_4q_v118_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_pct_change(gp, 4), 4))
def cg_f051_gross_margin_power_core118_slope_4q_v119_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(grossmargin, _std(grossmargin, 4) + 1e-9), 4))
def cg_f051_gross_margin_power_core119_slope_4q_v120_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_log(grossmargin.clip(lower=0.001) + 1.0), 4))

# Block 120-129: ewm 8q
def cg_f051_gross_margin_power_core120_ewm_8q_v121_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(grossmargin, 8))
def cg_f051_gross_margin_power_core121_ewm_8q_v122_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(gp, assets), 8))
def cg_f051_gross_margin_power_core122_ewm_8q_v123_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(gp, marketcap), 8))
def cg_f051_gross_margin_power_core123_ewm_8q_v124_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(gp, equity.abs() + 1.0), 8))
def cg_f051_gross_margin_power_core124_ewm_8q_v125_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(gp, opex.abs() + 1.0), 8))
def cg_f051_gross_margin_power_core125_ewm_8q_v126_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(gp - netinc, revenue), 8))
def cg_f051_gross_margin_power_core126_ewm_8q_v127_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_diff(grossmargin, 4), 8))
def cg_f051_gross_margin_power_core127_ewm_8q_v128_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_pct_change(gp, 4), 8))
def cg_f051_gross_margin_power_core128_ewm_8q_v129_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(grossmargin, _std(grossmargin, 4) + 1e-9), 8))
def cg_f051_gross_margin_power_core129_ewm_8q_v130_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_log(grossmargin.clip(lower=0.001) + 1.0), 8))

# Block 130-139: stability 12q
def cg_f051_gross_margin_power_core130_stability_12q_v131_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(_std(grossmargin, 12), _mean(grossmargin, 12).abs() + 1.0))
def cg_f051_gross_margin_power_core131_stability_12q_v132_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(gp, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f051_gross_margin_power_core132_stability_12q_v133_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(gp, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f051_gross_margin_power_core133_stability_12q_v134_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(gp, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f051_gross_margin_power_core134_stability_12q_v135_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(gp, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f051_gross_margin_power_core135_stability_12q_v136_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(gp - netinc, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f051_gross_margin_power_core136_stability_12q_v137_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    base = _diff(grossmargin, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f051_gross_margin_power_core137_stability_12q_v138_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    base = _pct_change(gp, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f051_gross_margin_power_core138_stability_12q_v139_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(grossmargin, _std(grossmargin, 4) + 1e-9)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f051_gross_margin_power_core139_stability_12q_v140_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    base = _log(grossmargin.clip(lower=0.001) + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f051_gross_margin_power_core140_level_v141_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(grossmargin)
def cg_f051_gross_margin_power_core141_gp_assets_v142_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(gp, assets))
def cg_f051_gross_margin_power_core142_gp_mcap_v143_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(gp, marketcap))
def cg_f051_gross_margin_power_core143_gp_equity_v144_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(gp, equity.abs() + 1.0))
def cg_f051_gross_margin_power_core144_gp_opex_v145_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(gp, opex.abs() + 1.0))
def cg_f051_gross_margin_power_core145_gm_ni_spread_v146_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(gp - netinc, revenue))
def cg_f051_gross_margin_power_core146_gm_diff_v147_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(grossmargin, 4))
def cg_f051_gross_margin_power_core147_gp_growth_v148_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(gp, 4))
def cg_f051_gross_margin_power_core148_gm_sharpe_v149_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(grossmargin, _std(grossmargin, 4) + 1e-9))
def cg_f051_gross_margin_power_core149_gm_log_v150_signal(grossmargin, gp, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(grossmargin.clip(lower=0.001) + 1.0))
