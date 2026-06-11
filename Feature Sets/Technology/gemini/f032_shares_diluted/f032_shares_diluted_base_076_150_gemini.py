import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f032_shares_diluted_core75_pct_4q_v076_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesdil, equity.abs() + 1.0), 4))
def cg_f032_shares_diluted_core76_pct_4q_v077_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesdil - sharesbas, sharesbas.abs() + 1.0), 4))
def cg_f032_shares_diluted_core77_pct_4q_v078_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_safe_div(sharesdil, opex.abs() + 1.0), 4))
def cg_f032_shares_diluted_core78_pct_4q_v079_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_pct_change(sharesdil, 4), 4))
def cg_f032_shares_diluted_core79_pct_4q_v080_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(_log(sharesdil.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f032_shares_diluted_core80_std_8q_v081_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(sharesdil, 8))
def cg_f032_shares_diluted_core81_std_8q_v082_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_safe_div(sharesdil, assets), 8))
def cg_f032_shares_diluted_core82_std_8q_v083_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_safe_div(sharesdil, revenue), 8))
def cg_f032_shares_diluted_core83_std_8q_v084_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_safe_div(sharesdil, marketcap), 8))
def cg_f032_shares_diluted_core84_std_8q_v085_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_safe_div(sharesdil, netinc.abs() + 1.0), 8))
def cg_f032_shares_diluted_core85_std_8q_v086_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_safe_div(sharesdil, equity.abs() + 1.0), 8))
def cg_f032_shares_diluted_core86_std_8q_v087_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_safe_div(sharesdil - sharesbas, sharesbas.abs() + 1.0), 8))
def cg_f032_shares_diluted_core87_std_8q_v088_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_safe_div(sharesdil, opex.abs() + 1.0), 8))
def cg_f032_shares_diluted_core88_std_8q_v089_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_pct_change(sharesdil, 4), 8))
def cg_f032_shares_diluted_core89_std_8q_v090_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_std(_log(sharesdil.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f032_shares_diluted_core90_log_v091_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(sharesdil.clip(lower=1.0)))
def cg_f032_shares_diluted_core91_log_v092_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesdil, assets).clip(lower=0.0001)))
def cg_f032_shares_diluted_core92_log_v093_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesdil, revenue).clip(lower=0.0001)))
def cg_f032_shares_diluted_core93_log_v094_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesdil, marketcap).clip(lower=0.0001)))
def cg_f032_shares_diluted_core94_log_v095_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesdil, netinc.abs() + 1.0).clip(lower=0.001)))
def cg_f032_shares_diluted_core95_log_v096_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesdil, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f032_shares_diluted_core96_log_v097_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesdil - sharesbas, sharesbas.abs() + 1.0).clip(lower=0.001)))
def cg_f032_shares_diluted_core97_log_v098_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesdil, opex.abs() + 1.0).clip(lower=0.001)))
def cg_f032_shares_diluted_core98_log_v099_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_pct_change(sharesdil, 4).clip(lower=-0.9) + 1.1))
def cg_f032_shares_diluted_core99_log_v100_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(_safe_div(sharesdil, assets).clip(lower=0.0001)))

# Block 100-109: diff 1q
def cg_f032_shares_diluted_core100_diff_1q_v101_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(sharesdil, 1))
def cg_f032_shares_diluted_core101_diff_1q_v102_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_safe_div(sharesdil, assets), 1))
def cg_f032_shares_diluted_core102_diff_1q_v103_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_safe_div(sharesdil, revenue), 1))
def cg_f032_shares_diluted_core103_diff_1q_v104_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_safe_div(sharesdil, marketcap), 1))
def cg_f032_shares_diluted_core104_diff_1q_v105_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_safe_div(sharesdil, netinc.abs() + 1.0), 1))
def cg_f032_shares_diluted_core105_diff_1q_v106_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_safe_div(sharesdil, equity.abs() + 1.0), 1))
def cg_f032_shares_diluted_core106_diff_1q_v107_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_safe_div(sharesdil - sharesbas, sharesbas.abs() + 1.0), 1))
def cg_f032_shares_diluted_core107_diff_1q_v108_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_safe_div(sharesdil, opex.abs() + 1.0), 1))
def cg_f032_shares_diluted_core108_diff_1q_v109_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_pct_change(sharesdil, 4), 1))
def cg_f032_shares_diluted_core109_diff_1q_v110_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_diff(_log(sharesdil.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f032_shares_diluted_core110_slope_4q_v111_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(sharesdil, 4))
def cg_f032_shares_diluted_core111_slope_4q_v112_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_safe_div(sharesdil, assets), 4))
def cg_f032_shares_diluted_core112_slope_4q_v113_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_safe_div(sharesdil, revenue), 4))
def cg_f032_shares_diluted_core113_slope_4q_v114_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_safe_div(sharesdil, marketcap), 4))
def cg_f032_shares_diluted_core114_slope_4q_v115_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_safe_div(sharesdil, netinc.abs() + 1.0), 4))
def cg_f032_shares_diluted_core115_slope_4q_v116_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_safe_div(sharesdil, equity.abs() + 1.0), 4))
def cg_f032_shares_diluted_core116_slope_4q_v117_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_safe_div(sharesdil - sharesbas, sharesbas.abs() + 1.0), 4))
def cg_f032_shares_diluted_core117_slope_4q_v118_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_safe_div(sharesdil, opex.abs() + 1.0), 4))
def cg_f032_shares_diluted_core118_slope_4q_v119_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_pct_change(sharesdil, 4), 4))
def cg_f032_shares_diluted_core119_slope_4q_v120_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_slope(_log(sharesdil.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f032_shares_diluted_core120_ewm_8q_v121_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(sharesdil, 8))
def cg_f032_shares_diluted_core121_ewm_8q_v122_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_safe_div(sharesdil, assets), 8))
def cg_f032_shares_diluted_core122_ewm_8q_v123_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_safe_div(sharesdil, revenue), 8))
def cg_f032_shares_diluted_core123_ewm_8q_v124_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_safe_div(sharesdil, marketcap), 8))
def cg_f032_shares_diluted_core124_ewm_8q_v125_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_safe_div(sharesdil, netinc.abs() + 1.0), 8))
def cg_f032_shares_diluted_core125_ewm_8q_v126_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_safe_div(sharesdil, equity.abs() + 1.0), 8))
def cg_f032_shares_diluted_core126_ewm_8q_v127_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_safe_div(sharesdil - sharesbas, sharesbas.abs() + 1.0), 8))
def cg_f032_shares_diluted_core127_ewm_8q_v128_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_safe_div(sharesdil, opex.abs() + 1.0), 8))
def cg_f032_shares_diluted_core128_ewm_8q_v129_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_pct_change(sharesdil, 4), 8))
def cg_f032_shares_diluted_core129_ewm_8q_v130_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_ewm(_log(sharesdil.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f032_shares_diluted_core130_stability_12q_v131_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(_std(sharesdil, 12), _mean(sharesdil, 12).abs() + 1.0))
def cg_f032_shares_diluted_core131_stability_12q_v132_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    base = _safe_div(sharesdil, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f032_shares_diluted_core132_stability_12q_v133_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    base = _safe_div(sharesdil, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f032_shares_diluted_core133_stability_12q_v134_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    base = _safe_div(sharesdil, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f032_shares_diluted_core134_stability_12q_v135_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    base = _safe_div(sharesdil, netinc.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f032_shares_diluted_core135_stability_12q_v136_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    base = _safe_div(sharesdil, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f032_shares_diluted_core136_stability_12q_v137_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    base = _safe_div(sharesdil - sharesbas, sharesbas.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f032_shares_diluted_core137_stability_12q_v138_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    base = _safe_div(sharesdil, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f032_shares_diluted_core138_stability_12q_v139_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    base = _pct_change(sharesdil, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f032_shares_diluted_core139_stability_12q_v140_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    base = _log(sharesdil.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f032_shares_diluted_core140_level_v141_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(sharesdil)
def cg_f032_shares_diluted_core141_ratio_assets_v142_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(sharesdil, assets))
def cg_f032_shares_diluted_core142_ratio_rev_v143_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(sharesdil, revenue))
def cg_f032_shares_diluted_core143_ratio_mcap_v144_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(sharesdil, marketcap))
def cg_f032_shares_diluted_core144_ratio_netinc_v145_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(sharesdil, netinc.abs() + 1.0))
def cg_f032_shares_diluted_core145_ratio_equity_v146_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(sharesdil, equity.abs() + 1.0))
def cg_f032_shares_diluted_core146_ratio_dilgap_v147_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(sharesdil - sharesbas, sharesbas.abs() + 1.0))
def cg_f032_shares_diluted_core147_ratio_opex_v148_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_safe_div(sharesdil, opex.abs() + 1.0))
def cg_f032_shares_diluted_core148_growth_yoy_v149_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_pct_change(sharesdil, 4))
def cg_f032_shares_diluted_core149_log_level_v150_signal(sharesdil, sharesbas, assets, revenue, marketcap, netinc, equity, opex):
    return _clean(_log(sharesdil.clip(lower=1.0)))
