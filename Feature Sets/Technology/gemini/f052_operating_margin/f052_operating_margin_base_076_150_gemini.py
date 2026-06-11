import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f052_operating_margin_core75_pct_4q_v076_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(opinc - netinc, revenue), 4))
def cg_f052_operating_margin_core76_pct_4q_v077_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_diff(opmargin, 4), 4))
def cg_f052_operating_margin_core77_pct_4q_v078_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_pct_change(opinc, 4), 4))
def cg_f052_operating_margin_core78_pct_4q_v079_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_safe_div(opmargin, _std(opmargin, 4) + 1e-9), 4))
def cg_f052_operating_margin_core79_pct_4q_v080_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(_log(opmargin.clip(lower=0.001) + 1.0), 4))

# Block 80-89: std 8q
def cg_f052_operating_margin_core80_std_8q_v081_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(opmargin, 8))
def cg_f052_operating_margin_core81_std_8q_v082_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(opinc, assets), 8))
def cg_f052_operating_margin_core82_std_8q_v083_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(opinc, marketcap), 8))
def cg_f052_operating_margin_core83_std_8q_v084_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(opinc, equity.abs() + 1.0), 8))
def cg_f052_operating_margin_core84_std_8q_v085_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(opinc, opex.abs() + 1.0), 8))
def cg_f052_operating_margin_core85_std_8q_v086_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(opinc - netinc, revenue), 8))
def cg_f052_operating_margin_core86_std_8q_v087_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_diff(opmargin, 4), 8))
def cg_f052_operating_margin_core87_std_8q_v088_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_pct_change(opinc, 4), 8))
def cg_f052_operating_margin_core88_std_8q_v089_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_safe_div(opmargin, _std(opmargin, 4) + 1e-9), 8))
def cg_f052_operating_margin_core89_std_8q_v090_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_std(_log(opmargin.clip(lower=0.001) + 1.0), 8))

# Block 90-99: log
def cg_f052_operating_margin_core90_log_v091_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(opmargin.clip(lower=0.001) + 1.0))
def cg_f052_operating_margin_core91_log_v092_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(opinc, assets).clip(lower=0.0001)))
def cg_f052_operating_margin_core92_log_v093_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(opinc, marketcap).clip(lower=0.0001)))
def cg_f052_operating_margin_core93_log_v094_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(opinc, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f052_operating_margin_core94_log_v095_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(opinc, opex.abs() + 1.0).clip(lower=0.001)))
def cg_f052_operating_margin_core95_log_v096_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(opinc - netinc, revenue).clip(lower=0.001) + 1.0))
def cg_f052_operating_margin_core96_log_v097_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_diff(opmargin, 4).clip(lower=-0.9) + 1.1))
def cg_f052_operating_margin_core97_log_v098_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_pct_change(opinc, 4).clip(lower=-0.9) + 1.1))
def cg_f052_operating_margin_core98_log_v099_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_safe_div(opmargin, _std(opmargin, 4) + 1e-9).clip(lower=0.001)))
def cg_f052_operating_margin_core99_log_v100_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(_mean(opmargin, 4).clip(lower=0.001) + 1.0))

# Block 100-109: diff 1q
def cg_f052_operating_margin_core100_diff_1q_v101_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(opmargin, 1))
def cg_f052_operating_margin_core101_diff_1q_v102_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(opinc, assets), 1))
def cg_f052_operating_margin_core102_diff_1q_v103_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(opinc, marketcap), 1))
def cg_f052_operating_margin_core103_diff_1q_v104_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(opinc, equity.abs() + 1.0), 1))
def cg_f052_operating_margin_core104_diff_1q_v105_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(opinc, opex.abs() + 1.0), 1))
def cg_f052_operating_margin_core105_diff_1q_v106_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(opinc - netinc, revenue), 1))
def cg_f052_operating_margin_core106_diff_1q_v107_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_diff(opmargin, 4), 1))
def cg_f052_operating_margin_core107_diff_1q_v108_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_pct_change(opinc, 4), 1))
def cg_f052_operating_margin_core108_diff_1q_v109_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_safe_div(opmargin, _std(opmargin, 4) + 1e-9), 1))
def cg_f052_operating_margin_core109_diff_1q_v110_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(_log(opmargin.clip(lower=0.001) + 1.0), 1))

# Block 110-119: slope 4q
def cg_f052_operating_margin_core110_slope_4q_v111_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(opmargin, 4))
def cg_f052_operating_margin_core111_slope_4q_v112_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(opinc, assets), 4))
def cg_f052_operating_margin_core112_slope_4q_v113_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(opinc, marketcap), 4))
def cg_f052_operating_margin_core113_slope_4q_v114_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(opinc, equity.abs() + 1.0), 4))
def cg_f052_operating_margin_core114_slope_4q_v115_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(opinc, opex.abs() + 1.0), 4))
def cg_f052_operating_margin_core115_slope_4q_v116_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(opinc - netinc, revenue), 4))
def cg_f052_operating_margin_core116_slope_4q_v117_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_diff(opmargin, 4), 4))
def cg_f052_operating_margin_core117_slope_4q_v118_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_pct_change(opinc, 4), 4))
def cg_f052_operating_margin_core118_slope_4q_v119_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_safe_div(opmargin, _std(opmargin, 4) + 1e-9), 4))
def cg_f052_operating_margin_core119_slope_4q_v120_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_slope(_log(opmargin.clip(lower=0.001) + 1.0), 4))

# Block 120-129: ewm 8q
def cg_f052_operating_margin_core120_ewm_8q_v121_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(opmargin, 8))
def cg_f052_operating_margin_core121_ewm_8q_v122_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(opinc, assets), 8))
def cg_f052_operating_margin_core122_ewm_8q_v123_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(opinc, marketcap), 8))
def cg_f052_operating_margin_core123_ewm_8q_v124_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(opinc, equity.abs() + 1.0), 8))
def cg_f052_operating_margin_core124_ewm_8q_v125_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(opinc, opex.abs() + 1.0), 8))
def cg_f052_operating_margin_core125_ewm_8q_v126_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(opinc - netinc, revenue), 8))
def cg_f052_operating_margin_core126_ewm_8q_v127_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_diff(opmargin, 4), 8))
def cg_f052_operating_margin_core127_ewm_8q_v128_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_pct_change(opinc, 4), 8))
def cg_f052_operating_margin_core128_ewm_8q_v129_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_safe_div(opmargin, _std(opmargin, 4) + 1e-9), 8))
def cg_f052_operating_margin_core129_ewm_8q_v130_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_ewm(_log(opmargin.clip(lower=0.001) + 1.0), 8))

# Block 130-139: stability 12q
def cg_f052_operating_margin_core130_stability_12q_v131_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(_std(opmargin, 12), _mean(opmargin, 12).abs() + 1.0))
def cg_f052_operating_margin_core131_stability_12q_v132_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(opinc, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f052_operating_margin_core132_stability_12q_v133_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(opinc, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f052_operating_margin_core133_stability_12q_v134_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(opinc, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f052_operating_margin_core134_stability_12q_v135_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(opinc, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f052_operating_margin_core135_stability_12q_v136_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(opinc - netinc, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f052_operating_margin_core136_stability_12q_v137_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    base = _diff(opmargin, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f052_operating_margin_core137_stability_12q_v138_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    base = _pct_change(opinc, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f052_operating_margin_core138_stability_12q_v139_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    base = _safe_div(opmargin, _std(opmargin, 4) + 1e-9)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f052_operating_margin_core139_stability_12q_v140_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    base = _log(opmargin.clip(lower=0.001) + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f052_operating_margin_core140_level_v141_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(opmargin)
def cg_f052_operating_margin_core141_opinc_assets_v142_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(opinc, assets))
def cg_f052_operating_margin_core142_opinc_mcap_v143_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(opinc, marketcap))
def cg_f052_operating_margin_core143_opinc_equity_v144_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(opinc, equity.abs() + 1.0))
def cg_f052_operating_margin_core144_opinc_opex_v145_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(opinc, opex.abs() + 1.0))
def cg_f052_operating_margin_core145_om_ni_spread_v146_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(opinc - netinc, revenue))
def cg_f052_operating_margin_core146_om_diff_v147_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_diff(opmargin, 4))
def cg_f052_operating_margin_core147_opinc_growth_v148_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_pct_change(opinc, 4))
def cg_f052_operating_margin_core148_om_sharpe_v149_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_safe_div(opmargin, _std(opmargin, 4) + 1e-9))
def cg_f052_operating_margin_core149_om_log_v150_signal(opmargin, opinc, revenue, assets, marketcap, opex, equity, netinc):
    return _clean(_log(opmargin.clip(lower=0.001) + 1.0))
