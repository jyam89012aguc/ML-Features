import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f042_intangibles_goodwill_core75_pct_4q_v076_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_pct_change(_safe_div(intangibles, equity.abs() + 1.0), 4))
def cg_f042_intangibles_goodwill_core76_pct_4q_v077_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_pct_change(_safe_div(goodwill, equity.abs() + 1.0), 4))
def cg_f042_intangibles_goodwill_core77_pct_4q_v078_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_pct_change(_pct_change(intangibles, 4), 4))
def cg_f042_intangibles_goodwill_core78_pct_4q_v079_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_pct_change(_pct_change(goodwill, 4), 4))
def cg_f042_intangibles_goodwill_core79_pct_4q_v080_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_pct_change(_log(intangibles.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f042_intangibles_goodwill_core80_std_8q_v081_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_std(intangibles, 8))
def cg_f042_intangibles_goodwill_core81_std_8q_v082_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_std(goodwill, 8))
def cg_f042_intangibles_goodwill_core82_std_8q_v083_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_std(_safe_div(intangibles, assets), 8))
def cg_f042_intangibles_goodwill_core83_std_8q_v084_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_std(_safe_div(goodwill, assets), 8))
def cg_f042_intangibles_goodwill_core84_std_8q_v085_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_std(_safe_div(intangibles + goodwill, assets), 8))
def cg_f042_intangibles_goodwill_core85_std_8q_v086_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_std(_safe_div(intangibles, equity.abs() + 1.0), 8))
def cg_f042_intangibles_goodwill_core86_std_8q_v087_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_std(_safe_div(goodwill, equity.abs() + 1.0), 8))
def cg_f042_intangibles_goodwill_core87_std_8q_v088_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_std(_pct_change(intangibles, 4), 8))
def cg_f042_intangibles_goodwill_core88_std_8q_v089_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_std(_pct_change(goodwill, 4), 8))
def cg_f042_intangibles_goodwill_core89_std_8q_v090_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_std(_log(intangibles.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f042_intangibles_goodwill_core90_log_v091_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_log(intangibles.clip(lower=1.0)))
def cg_f042_intangibles_goodwill_core91_log_v092_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_log(goodwill.clip(lower=1.0)))
def cg_f042_intangibles_goodwill_core92_log_v093_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_log(_safe_div(intangibles, assets).clip(lower=0.0001)))
def cg_f042_intangibles_goodwill_core93_log_v094_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_log(_safe_div(goodwill, assets).clip(lower=0.0001)))
def cg_f042_intangibles_goodwill_core94_log_v095_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_log(_safe_div(intangibles + goodwill, assets).clip(lower=0.0001)))
def cg_f042_intangibles_goodwill_core95_log_v096_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_log(_safe_div(intangibles, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f042_intangibles_goodwill_core96_log_v097_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_log(_safe_div(goodwill, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f042_intangibles_goodwill_core97_log_v098_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_log(_pct_change(intangibles, 4).clip(lower=-0.9) + 1.1))
def cg_f042_intangibles_goodwill_core98_log_v099_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_log(_pct_change(goodwill, 4).clip(lower=-0.9) + 1.1))
def cg_f042_intangibles_goodwill_core99_log_v100_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_log(assets.clip(lower=1.0)))

# Block 100-109: diff 1q
def cg_f042_intangibles_goodwill_core100_diff_1q_v101_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_diff(intangibles, 1))
def cg_f042_intangibles_goodwill_core101_diff_1q_v102_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_diff(goodwill, 1))
def cg_f042_intangibles_goodwill_core102_diff_1q_v103_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_diff(_safe_div(intangibles, assets), 1))
def cg_f042_intangibles_goodwill_core103_diff_1q_v104_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_diff(_safe_div(goodwill, assets), 1))
def cg_f042_intangibles_goodwill_core104_diff_1q_v105_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_diff(_safe_div(intangibles + goodwill, assets), 1))
def cg_f042_intangibles_goodwill_core105_diff_1q_v106_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_diff(_safe_div(intangibles, equity.abs() + 1.0), 1))
def cg_f042_intangibles_goodwill_core106_diff_1q_v107_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_diff(_safe_div(goodwill, equity.abs() + 1.0), 1))
def cg_f042_intangibles_goodwill_core107_diff_1q_v108_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_diff(_pct_change(intangibles, 4), 1))
def cg_f042_intangibles_goodwill_core108_diff_1q_v109_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_diff(_pct_change(goodwill, 4), 1))
def cg_f042_intangibles_goodwill_core109_diff_1q_v110_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_diff(_log(intangibles.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f042_intangibles_goodwill_core110_slope_4q_v111_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_slope(intangibles, 4))
def cg_f042_intangibles_goodwill_core111_slope_4q_v112_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_slope(goodwill, 4))
def cg_f042_intangibles_goodwill_core112_slope_4q_v113_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_slope(_safe_div(intangibles, assets), 4))
def cg_f042_intangibles_goodwill_core113_slope_4q_v114_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_slope(_safe_div(goodwill, assets), 4))
def cg_f042_intangibles_goodwill_core114_slope_4q_v115_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_slope(_safe_div(intangibles + goodwill, assets), 4))
def cg_f042_intangibles_goodwill_core115_slope_4q_v116_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_slope(_safe_div(intangibles, equity.abs() + 1.0), 4))
def cg_f042_intangibles_goodwill_core116_slope_4q_v117_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_slope(_safe_div(goodwill, equity.abs() + 1.0), 4))
def cg_f042_intangibles_goodwill_core117_slope_4q_v118_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_slope(_pct_change(intangibles, 4), 4))
def cg_f042_intangibles_goodwill_core118_slope_4q_v119_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_slope(_pct_change(goodwill, 4), 4))
def cg_f042_intangibles_goodwill_core119_slope_4q_v120_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_slope(_log(intangibles.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f042_intangibles_goodwill_core120_ewm_8q_v121_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_ewm(intangibles, 8))
def cg_f042_intangibles_goodwill_core121_ewm_8q_v122_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_ewm(goodwill, 8))
def cg_f042_intangibles_goodwill_core122_ewm_8q_v123_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_ewm(_safe_div(intangibles, assets), 8))
def cg_f042_intangibles_goodwill_core123_ewm_8q_v124_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_ewm(_safe_div(goodwill, assets), 8))
def cg_f042_intangibles_goodwill_core124_ewm_8q_v125_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_ewm(_safe_div(intangibles + goodwill, assets), 8))
def cg_f042_intangibles_goodwill_core125_ewm_8q_v126_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_ewm(_safe_div(intangibles, equity.abs() + 1.0), 8))
def cg_f042_intangibles_goodwill_core126_ewm_8q_v127_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_ewm(_safe_div(goodwill, equity.abs() + 1.0), 8))
def cg_f042_intangibles_goodwill_core127_ewm_8q_v128_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_ewm(_pct_change(intangibles, 4), 8))
def cg_f042_intangibles_goodwill_core128_ewm_8q_v129_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_ewm(_pct_change(goodwill, 4), 8))
def cg_f042_intangibles_goodwill_core129_ewm_8q_v130_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_ewm(_log(intangibles.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f042_intangibles_goodwill_core130_stability_12q_v131_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_safe_div(_std(intangibles, 12), _mean(intangibles, 12).abs() + 1.0))
def cg_f042_intangibles_goodwill_core131_stability_12q_v132_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    base = goodwill
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f042_intangibles_goodwill_core132_stability_12q_v133_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    base = _safe_div(intangibles, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f042_intangibles_goodwill_core133_stability_12q_v134_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    base = _safe_div(goodwill, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f042_intangibles_goodwill_core134_stability_12q_v135_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    base = _safe_div(intangibles + goodwill, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f042_intangibles_goodwill_core135_stability_12q_v136_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    base = _safe_div(intangibles, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f042_intangibles_goodwill_core136_stability_12q_v137_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    base = _safe_div(goodwill, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f042_intangibles_goodwill_core137_stability_12q_v138_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    base = _pct_change(intangibles, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f042_intangibles_goodwill_core138_stability_12q_v139_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    base = _pct_change(goodwill, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f042_intangibles_goodwill_core139_stability_12q_v140_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    base = _log(intangibles.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f042_intangibles_goodwill_core140_level_v141_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(intangibles)
def cg_f042_intangibles_goodwill_core141_gw_level_v142_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(goodwill)
def cg_f042_intangibles_goodwill_core142_int_assets_v143_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_safe_div(intangibles, assets))
def cg_f042_intangibles_goodwill_core143_gw_assets_v144_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_safe_div(goodwill, assets))
def cg_f042_intangibles_goodwill_core144_total_int_assets_v145_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_safe_div(intangibles + goodwill, assets))
def cg_f042_intangibles_goodwill_core145_int_equity_v146_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_safe_div(intangibles, equity.abs() + 1.0))
def cg_f042_intangibles_goodwill_core146_gw_equity_v147_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_safe_div(goodwill, equity.abs() + 1.0))
def cg_f042_intangibles_goodwill_core147_growth_yoy_v148_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_pct_change(intangibles, 4))
def cg_f042_intangibles_goodwill_core148_gw_growth_yoy_v149_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_pct_change(goodwill, 4))
def cg_f042_intangibles_goodwill_core149_log_level_v150_signal(intangibles, goodwill, assets, revenue, marketcap, equity, netinc, opex):
    return _clean(_log(intangibles.clip(lower=1.0)))
