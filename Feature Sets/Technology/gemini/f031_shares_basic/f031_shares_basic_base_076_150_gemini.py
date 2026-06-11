import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f031_shares_basic_core75_pct_4q_v076_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesbas, equity.abs() + 1.0), 4))
def cg_f031_shares_basic_core76_pct_4q_v077_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesbas, opex.abs() + 1.0), 4))
def cg_f031_shares_basic_core77_pct_4q_v078_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesbas, sharesdil.abs() + 1.0), 4))
def cg_f031_shares_basic_core78_pct_4q_v079_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_pct_change(sharesbas, 4), 4))
def cg_f031_shares_basic_core79_pct_4q_v080_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_log(sharesbas.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f031_shares_basic_core80_std_8q_v081_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(sharesbas, 8))
def cg_f031_shares_basic_core81_std_8q_v082_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_safe_div(sharesbas, assets), 8))
def cg_f031_shares_basic_core82_std_8q_v083_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_safe_div(sharesbas, revenue), 8))
def cg_f031_shares_basic_core83_std_8q_v084_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_safe_div(sharesbas, marketcap), 8))
def cg_f031_shares_basic_core84_std_8q_v085_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_safe_div(sharesbas, netinc.abs() + 1.0), 8))
def cg_f031_shares_basic_core85_std_8q_v086_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_safe_div(sharesbas, equity.abs() + 1.0), 8))
def cg_f031_shares_basic_core86_std_8q_v087_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_safe_div(sharesbas, opex.abs() + 1.0), 8))
def cg_f031_shares_basic_core87_std_8q_v088_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_safe_div(sharesbas, sharesdil.abs() + 1.0), 8))
def cg_f031_shares_basic_core88_std_8q_v089_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_pct_change(sharesbas, 4), 8))
def cg_f031_shares_basic_core89_std_8q_v090_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_log(sharesbas.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f031_shares_basic_core90_log_v091_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(sharesbas.clip(lower=1.0)))
def cg_f031_shares_basic_core91_log_v092_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesbas, assets).clip(lower=0.0001)))
def cg_f031_shares_basic_core92_log_v093_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesbas, revenue).clip(lower=0.0001)))
def cg_f031_shares_basic_core93_log_v094_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesbas, marketcap).clip(lower=0.0001)))
def cg_f031_shares_basic_core94_log_v095_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesbas, netinc.abs() + 1.0).clip(lower=0.001)))
def cg_f031_shares_basic_core95_log_v096_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesbas, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f031_shares_basic_core96_log_v097_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesbas, opex.abs() + 1.0).clip(lower=0.001)))
def cg_f031_shares_basic_core97_log_v098_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesbas, sharesdil.abs() + 1.0).clip(lower=0.1)))
def cg_f031_shares_basic_core98_log_v099_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_pct_change(sharesbas, 4).clip(lower=-0.9) + 1.1))
def cg_f031_shares_basic_core99_log_v100_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesbas, assets).clip(lower=0.0001)))

# Block 100-109: diff 1q
def cg_f031_shares_basic_core100_diff_1q_v101_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(sharesbas, 1))
def cg_f031_shares_basic_core101_diff_1q_v102_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_safe_div(sharesbas, assets), 1))
def cg_f031_shares_basic_core102_diff_1q_v103_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_safe_div(sharesbas, revenue), 1))
def cg_f031_shares_basic_core103_diff_1q_v104_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_safe_div(sharesbas, marketcap), 1))
def cg_f031_shares_basic_core104_diff_1q_v105_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_safe_div(sharesbas, netinc.abs() + 1.0), 1))
def cg_f031_shares_basic_core105_diff_1q_v106_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_safe_div(sharesbas, equity.abs() + 1.0), 1))
def cg_f031_shares_basic_core106_diff_1q_v107_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_safe_div(sharesbas, opex.abs() + 1.0), 1))
def cg_f031_shares_basic_core107_diff_1q_v108_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_safe_div(sharesbas, sharesdil.abs() + 1.0), 1))
def cg_f031_shares_basic_core108_diff_1q_v109_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_pct_change(sharesbas, 4), 1))
def cg_f031_shares_basic_core109_diff_1q_v110_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_log(sharesbas.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f031_shares_basic_core110_slope_4q_v111_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(sharesbas, 4))
def cg_f031_shares_basic_core111_slope_4q_v112_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_safe_div(sharesbas, assets), 4))
def cg_f031_shares_basic_core112_slope_4q_v113_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_safe_div(sharesbas, revenue), 4))
def cg_f031_shares_basic_core113_slope_4q_v114_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_safe_div(sharesbas, marketcap), 4))
def cg_f031_shares_basic_core114_slope_4q_v115_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_safe_div(sharesbas, netinc.abs() + 1.0), 4))
def cg_f031_shares_basic_core115_slope_4q_v116_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_safe_div(sharesbas, equity.abs() + 1.0), 4))
def cg_f031_shares_basic_core116_slope_4q_v117_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_safe_div(sharesbas, opex.abs() + 1.0), 4))
def cg_f031_shares_basic_core117_slope_4q_v118_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_safe_div(sharesbas, sharesdil.abs() + 1.0), 4))
def cg_f031_shares_basic_core118_slope_4q_v119_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_pct_change(sharesbas, 4), 4))
def cg_f031_shares_basic_core119_slope_4q_v120_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_log(sharesbas.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f031_shares_basic_core120_ewm_8q_v121_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(sharesbas, 8))
def cg_f031_shares_basic_core121_ewm_8q_v122_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_safe_div(sharesbas, assets), 8))
def cg_f031_shares_basic_core122_ewm_8q_v123_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_safe_div(sharesbas, revenue), 8))
def cg_f031_shares_basic_core123_ewm_8q_v124_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_safe_div(sharesbas, marketcap), 8))
def cg_f031_shares_basic_core124_ewm_8q_v125_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_safe_div(sharesbas, netinc.abs() + 1.0), 8))
def cg_f031_shares_basic_core125_ewm_8q_v126_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_safe_div(sharesbas, equity.abs() + 1.0), 8))
def cg_f031_shares_basic_core126_ewm_8q_v127_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_safe_div(sharesbas, opex.abs() + 1.0), 8))
def cg_f031_shares_basic_core127_ewm_8q_v128_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_safe_div(sharesbas, sharesdil.abs() + 1.0), 8))
def cg_f031_shares_basic_core128_ewm_8q_v129_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_pct_change(sharesbas, 4), 8))
def cg_f031_shares_basic_core129_ewm_8q_v130_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_log(sharesbas.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f031_shares_basic_core130_stability_12q_v131_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(_std(sharesbas, 12), _mean(sharesbas, 12).abs() + 1.0))
def cg_f031_shares_basic_core131_stability_12q_v132_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    base = _safe_div(sharesbas, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f031_shares_basic_core132_stability_12q_v133_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    base = _safe_div(sharesbas, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f031_shares_basic_core133_stability_12q_v134_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    base = _safe_div(sharesbas, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f031_shares_basic_core134_stability_12q_v135_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    base = _safe_div(sharesbas, netinc.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f031_shares_basic_core135_stability_12q_v136_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    base = _safe_div(sharesbas, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f031_shares_basic_core136_stability_12q_v137_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    base = _safe_div(sharesbas, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f031_shares_basic_core137_stability_12q_v138_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    base = _safe_div(sharesbas, sharesdil.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f031_shares_basic_core138_stability_12q_v139_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    base = _pct_change(sharesbas, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f031_shares_basic_core139_stability_12q_v140_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    base = _log(sharesbas.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f031_shares_basic_core140_level_v141_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(sharesbas)
def cg_f031_shares_basic_core141_ratio_assets_v142_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(sharesbas, assets))
def cg_f031_shares_basic_core142_ratio_rev_v143_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(sharesbas, revenue))
def cg_f031_shares_basic_core143_ratio_mcap_v144_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(sharesbas, marketcap))
def cg_f031_shares_basic_core144_ratio_netinc_v145_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(sharesbas, netinc.abs() + 1.0))
def cg_f031_shares_basic_core145_ratio_equity_v146_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(sharesbas, equity.abs() + 1.0))
def cg_f031_shares_basic_core146_ratio_opex_v147_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(sharesbas, opex.abs() + 1.0))
def cg_f031_shares_basic_core147_ratio_dil_v148_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(sharesbas, sharesdil.abs() + 1.0))
def cg_f031_shares_basic_core148_growth_yoy_v149_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(sharesbas, 4))
def cg_f031_shares_basic_core149_log_level_v150_signal(sharesbas, sharesdil, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(sharesbas.clip(lower=1.0)))
