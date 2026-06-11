import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f038_market_capitalization_core75_pct_4q_v076_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_pct_change(_safe_div(marketcap, netinc.abs() + 1.0), 4))
def cg_f038_market_capitalization_core76_pct_4q_v077_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_pct_change(_safe_div(marketcap, sharesbas), 4))
def cg_f038_market_capitalization_core77_pct_4q_v078_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_pct_change(_safe_div(marketcap, opex.abs() + 1.0), 4))
def cg_f038_market_capitalization_core78_pct_4q_v079_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_pct_change(_pct_change(marketcap, 4), 4))
def cg_f038_market_capitalization_core79_pct_4q_v080_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_pct_change(_log(marketcap.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f038_market_capitalization_core80_std_8q_v081_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_std(marketcap, 8))
def cg_f038_market_capitalization_core81_std_8q_v082_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_std(_safe_div(marketcap, revenue), 8))
def cg_f038_market_capitalization_core82_std_8q_v083_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_std(_safe_div(marketcap, assets), 8))
def cg_f038_market_capitalization_core83_std_8q_v084_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_std(_safe_div(marketcap, equity.abs() + 1.0), 8))
def cg_f038_market_capitalization_core84_std_8q_v085_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_std(_safe_div(marketcap, ncfo.abs() + 1.0), 8))
def cg_f038_market_capitalization_core85_std_8q_v086_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_std(_safe_div(marketcap, netinc.abs() + 1.0), 8))
def cg_f038_market_capitalization_core86_std_8q_v087_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_std(_safe_div(marketcap, sharesbas), 8))
def cg_f038_market_capitalization_core87_std_8q_v088_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_std(_pct_change(marketcap, 4), 8))
def cg_f038_market_capitalization_core88_std_8q_v089_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_std(_safe_div(marketcap, opex.abs() + 1.0), 8))
def cg_f038_market_capitalization_core89_std_8q_v090_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_std(_log(marketcap.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f038_market_capitalization_core90_log_v091_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_log(marketcap.clip(lower=1.0)))
def cg_f038_market_capitalization_core91_log_v092_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_log(_safe_div(marketcap, revenue).clip(lower=0.0001)))
def cg_f038_market_capitalization_core92_log_v093_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_log(_safe_div(marketcap, assets).clip(lower=0.0001)))
def cg_f038_market_capitalization_core93_log_v094_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_log(_safe_div(marketcap, equity.abs() + 1.0).clip(lower=0.0001)))
def cg_f038_market_capitalization_core94_log_v095_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_log(_safe_div(marketcap, ncfo.abs() + 1.0).clip(lower=0.001)))
def cg_f038_market_capitalization_core95_log_v096_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_log(_safe_div(marketcap, netinc.abs() + 1.0).clip(lower=0.001)))
def cg_f038_market_capitalization_core96_log_v097_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_log(_safe_div(marketcap, sharesbas).clip(lower=0.1)))
def cg_f038_market_capitalization_core97_log_v098_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_log(_pct_change(marketcap, 4).clip(lower=-0.9) + 1.1))
def cg_f038_market_capitalization_core98_log_v099_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_log(_safe_div(marketcap, opex.abs() + 1.0).clip(lower=0.001)))
def cg_f038_market_capitalization_core99_log_v100_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_log(revenue.clip(lower=1.0)))

# Block 100-109: diff 1q
def cg_f038_market_capitalization_core100_diff_1q_v101_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_diff(marketcap, 1))
def cg_f038_market_capitalization_core101_diff_1q_v102_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_diff(_safe_div(marketcap, revenue), 1))
def cg_f038_market_capitalization_core102_diff_1q_v103_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_diff(_safe_div(marketcap, assets), 1))
def cg_f038_market_capitalization_core103_diff_1q_v104_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_diff(_safe_div(marketcap, equity.abs() + 1.0), 1))
def cg_f038_market_capitalization_core104_diff_1q_v105_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_diff(_safe_div(marketcap, ncfo.abs() + 1.0), 1))
def cg_f038_market_capitalization_core105_diff_1q_v106_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_diff(_safe_div(marketcap, netinc.abs() + 1.0), 1))
def cg_f038_market_capitalization_core106_diff_1q_v107_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_diff(_safe_div(marketcap, sharesbas), 1))
def cg_f038_market_capitalization_core107_diff_1q_v108_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_diff(_pct_change(marketcap, 4), 1))
def cg_f038_market_capitalization_core108_diff_1q_v109_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_diff(_safe_div(marketcap, opex.abs() + 1.0), 1))
def cg_f038_market_capitalization_core109_diff_1q_v110_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_diff(_log(marketcap.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f038_market_capitalization_core110_slope_4q_v111_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_slope(marketcap, 4))
def cg_f038_market_capitalization_core111_slope_4q_v112_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_slope(_safe_div(marketcap, revenue), 4))
def cg_f038_market_capitalization_core112_slope_4q_v113_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_slope(_safe_div(marketcap, assets), 4))
def cg_f038_market_capitalization_core113_slope_4q_v114_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_slope(_safe_div(marketcap, equity.abs() + 1.0), 4))
def cg_f038_market_capitalization_core114_slope_4q_v115_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_slope(_safe_div(marketcap, ncfo.abs() + 1.0), 4))
def cg_f038_market_capitalization_core115_slope_4q_v116_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_slope(_safe_div(marketcap, netinc.abs() + 1.0), 4))
def cg_f038_market_capitalization_core116_slope_4q_v117_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_slope(_safe_div(marketcap, sharesbas), 4))
def cg_f038_market_capitalization_core117_slope_4q_v118_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_slope(_pct_change(marketcap, 4), 4))
def cg_f038_market_capitalization_core118_slope_4q_v119_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_slope(_safe_div(marketcap, opex.abs() + 1.0), 4))
def cg_f038_market_capitalization_core119_slope_4q_v120_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_slope(_log(marketcap.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f038_market_capitalization_core120_ewm_8q_v121_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_ewm(marketcap, 8))
def cg_f038_market_capitalization_core121_ewm_8q_v122_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_ewm(_safe_div(marketcap, revenue), 8))
def cg_f038_market_capitalization_core122_ewm_8q_v123_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_ewm(_safe_div(marketcap, assets), 8))
def cg_f038_market_capitalization_core123_ewm_8q_v124_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_ewm(_safe_div(marketcap, equity.abs() + 1.0), 8))
def cg_f038_market_capitalization_core124_ewm_8q_v125_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_ewm(_safe_div(marketcap, ncfo.abs() + 1.0), 8))
def cg_f038_market_capitalization_core125_ewm_8q_v126_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_ewm(_safe_div(marketcap, netinc.abs() + 1.0), 8))
def cg_f038_market_capitalization_core126_ewm_8q_v127_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_ewm(_safe_div(marketcap, sharesbas), 8))
def cg_f038_market_capitalization_core127_ewm_8q_v128_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_ewm(_pct_change(marketcap, 4), 8))
def cg_f038_market_capitalization_core128_ewm_8q_v129_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_ewm(_safe_div(marketcap, opex.abs() + 1.0), 8))
def cg_f038_market_capitalization_core129_ewm_8q_v130_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_ewm(_log(marketcap.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f038_market_capitalization_core130_stability_12q_v131_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_safe_div(_std(marketcap, 12), _mean(marketcap, 12).abs() + 1.0))
def cg_f038_market_capitalization_core131_stability_12q_v132_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    base = _safe_div(marketcap, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f038_market_capitalization_core132_stability_12q_v133_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    base = _safe_div(marketcap, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f038_market_capitalization_core133_stability_12q_v134_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    base = _safe_div(marketcap, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f038_market_capitalization_core134_stability_12q_v135_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    base = _safe_div(marketcap, ncfo.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f038_market_capitalization_core135_stability_12q_v136_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    base = _safe_div(marketcap, netinc.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f038_market_capitalization_core136_stability_12q_v137_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    base = _safe_div(marketcap, sharesbas)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f038_market_capitalization_core137_stability_12q_v138_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    base = _pct_change(marketcap, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f038_market_capitalization_core138_stability_12q_v139_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    base = marketcap
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f038_market_capitalization_core139_stability_12q_v140_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    base = _log(marketcap.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f038_market_capitalization_core140_level_v141_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(marketcap)
def cg_f038_market_capitalization_core141_ratio_rev_v142_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_safe_div(marketcap, revenue))
def cg_f038_market_capitalization_core142_ratio_assets_v143_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_safe_div(marketcap, assets))
def cg_f038_market_capitalization_core143_ratio_equity_v144_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_safe_div(marketcap, equity.abs() + 1.0))
def cg_f038_market_capitalization_core144_ratio_ncfo_v145_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_safe_div(marketcap, ncfo.abs() + 1.0))
def cg_f038_market_capitalization_core145_ratio_ni_v146_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_safe_div(marketcap, netinc.abs() + 1.0))
def cg_f038_market_capitalization_core146_price_proxy_v147_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_safe_div(marketcap, sharesbas))
def cg_f038_market_capitalization_core147_growth_yoy_v148_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_pct_change(marketcap, 4))
def cg_f038_market_capitalization_core148_ratio_opex_v149_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_safe_div(marketcap, opex.abs() + 1.0))
def cg_f038_market_capitalization_core149_log_level_v150_signal(marketcap, revenue, assets, equity, ncfo, netinc, sharesbas, opex):
    return _clean(_log(marketcap.clip(lower=1.0)))
