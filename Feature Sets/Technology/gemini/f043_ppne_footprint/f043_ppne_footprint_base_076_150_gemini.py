import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f043_ppne_footprint_core75_pct_4q_v076_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_safe_div(ppnenet, equity.abs() + 1.0), 4))
def cg_f043_ppne_footprint_core76_pct_4q_v077_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_safe_div(ppnenet, ppneg), 4))
def cg_f043_ppne_footprint_core77_pct_4q_v078_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_pct_change(ppnenet, 4), 4))
def cg_f043_ppne_footprint_core78_pct_4q_v079_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_safe_div(ppnenet, opex.abs() + 1.0), 4))
def cg_f043_ppne_footprint_core79_pct_4q_v080_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(_log(ppnenet.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f043_ppne_footprint_core80_std_8q_v081_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_std(ppnenet, 8))
def cg_f043_ppne_footprint_core81_std_8q_v082_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_std(ppneg, 8))
def cg_f043_ppne_footprint_core82_std_8q_v083_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_std(_safe_div(ppnenet, assets), 8))
def cg_f043_ppne_footprint_core83_std_8q_v084_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_std(_safe_div(ppneg, assets), 8))
def cg_f043_ppne_footprint_core84_std_8q_v085_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_std(_safe_div(ppnenet, revenue), 8))
def cg_f043_ppne_footprint_core85_std_8q_v086_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_std(_safe_div(ppnenet, equity.abs() + 1.0), 8))
def cg_f043_ppne_footprint_core86_std_8q_v087_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_std(_safe_div(ppnenet, ppneg), 8))
def cg_f043_ppne_footprint_core87_std_8q_v088_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_std(_pct_change(ppnenet, 4), 8))
def cg_f043_ppne_footprint_core88_std_8q_v089_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_std(_safe_div(ppnenet, opex.abs() + 1.0), 8))
def cg_f043_ppne_footprint_core89_std_8q_v090_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_std(_log(ppnenet.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f043_ppne_footprint_core90_log_v091_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_log(ppnenet.clip(lower=1.0)))
def cg_f043_ppne_footprint_core91_log_v092_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_log(ppneg.clip(lower=1.0)))
def cg_f043_ppne_footprint_core92_log_v093_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_log(_safe_div(ppnenet, assets).clip(lower=0.0001)))
def cg_f043_ppne_footprint_core93_log_v094_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_log(_safe_div(ppneg, assets).clip(lower=0.0001)))
def cg_f043_ppne_footprint_core94_log_v095_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_log(_safe_div(ppnenet, revenue).clip(lower=0.0001)))
def cg_f043_ppne_footprint_core95_log_v096_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_log(_safe_div(ppnenet, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f043_ppne_footprint_core96_log_v097_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_log(_safe_div(ppnenet, ppneg).clip(lower=0.01)))
def cg_f043_ppne_footprint_core97_log_v098_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_log(_pct_change(ppnenet, 4).clip(lower=-0.9) + 1.1))
def cg_f043_ppne_footprint_core98_log_v099_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_log(_safe_div(ppnenet, opex.abs() + 1.0).clip(lower=0.001)))
def cg_f043_ppne_footprint_core99_log_v100_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_log(assets.clip(lower=1.0)))

# Block 100-109: diff 1q
def cg_f043_ppne_footprint_core100_diff_1q_v101_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_diff(ppnenet, 1))
def cg_f043_ppne_footprint_core101_diff_1q_v102_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_diff(ppneg, 1))
def cg_f043_ppne_footprint_core102_diff_1q_v103_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_diff(_safe_div(ppnenet, assets), 1))
def cg_f043_ppne_footprint_core103_diff_1q_v104_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_diff(_safe_div(ppneg, assets), 1))
def cg_f043_ppne_footprint_core104_diff_1q_v105_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_diff(_safe_div(ppnenet, revenue), 1))
def cg_f043_ppne_footprint_core105_diff_1q_v106_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_diff(_safe_div(ppnenet, equity.abs() + 1.0), 1))
def cg_f043_ppne_footprint_core106_diff_1q_v107_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_diff(_safe_div(ppnenet, ppneg), 1))
def cg_f043_ppne_footprint_core107_diff_1q_v108_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_diff(_pct_change(ppnenet, 4), 1))
def cg_f043_ppne_footprint_core108_diff_1q_v109_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_diff(_safe_div(ppnenet, opex.abs() + 1.0), 1))
def cg_f043_ppne_footprint_core109_diff_1q_v110_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_diff(_log(ppnenet.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f043_ppne_footprint_core110_slope_4q_v111_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_slope(ppnenet, 4))
def cg_f043_ppne_footprint_core111_slope_4q_v112_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_slope(ppneg, 4))
def cg_f043_ppne_footprint_core112_slope_4q_v113_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_slope(_safe_div(ppnenet, assets), 4))
def cg_f043_ppne_footprint_core113_slope_4q_v114_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_slope(_safe_div(ppneg, assets), 4))
def cg_f043_ppne_footprint_core114_slope_4q_v115_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_slope(_safe_div(ppnenet, revenue), 4))
def cg_f043_ppne_footprint_core115_slope_4q_v116_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_slope(_safe_div(ppnenet, equity.abs() + 1.0), 4))
def cg_f043_ppne_footprint_core116_slope_4q_v117_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_slope(_safe_div(ppnenet, ppneg), 4))
def cg_f043_ppne_footprint_core117_slope_4q_v118_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_slope(_pct_change(ppnenet, 4), 4))
def cg_f043_ppne_footprint_core118_slope_4q_v119_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_slope(_safe_div(ppnenet, opex.abs() + 1.0), 4))
def cg_f043_ppne_footprint_core119_slope_4q_v120_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_slope(_log(ppnenet.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f043_ppne_footprint_core120_ewm_8q_v121_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_ewm(ppnenet, 8))
def cg_f043_ppne_footprint_core121_ewm_8q_v122_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_ewm(ppneg, 8))
def cg_f043_ppne_footprint_core122_ewm_8q_v123_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_ewm(_safe_div(ppnenet, assets), 8))
def cg_f043_ppne_footprint_core123_ewm_8q_v124_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_ewm(_safe_div(ppneg, assets), 8))
def cg_f043_ppne_footprint_core124_ewm_8q_v125_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_ewm(_safe_div(ppnenet, revenue), 8))
def cg_f043_ppne_footprint_core125_ewm_8q_v126_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_ewm(_safe_div(ppnenet, equity.abs() + 1.0), 8))
def cg_f043_ppne_footprint_core126_ewm_8q_v127_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_ewm(_safe_div(ppnenet, ppneg), 8))
def cg_f043_ppne_footprint_core127_ewm_8q_v128_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_ewm(_pct_change(ppnenet, 4), 8))
def cg_f043_ppne_footprint_core128_ewm_8q_v129_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_ewm(_safe_div(ppnenet, opex.abs() + 1.0), 8))
def cg_f043_ppne_footprint_core129_ewm_8q_v130_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_ewm(_log(ppnenet.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f043_ppne_footprint_core130_stability_12q_v131_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_safe_div(_std(ppnenet, 12), _mean(ppnenet, 12).abs() + 1.0))
def cg_f043_ppne_footprint_core131_stability_12q_v132_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    base = ppneg
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f043_ppne_footprint_core132_stability_12q_v133_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    base = _safe_div(ppnenet, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f043_ppne_footprint_core133_stability_12q_v134_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    base = _safe_div(ppneg, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f043_ppne_footprint_core134_stability_12q_v135_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    base = _safe_div(ppnenet, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f043_ppne_footprint_core135_stability_12q_v136_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    base = _safe_div(ppnenet, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f043_ppne_footprint_core136_stability_12q_v137_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    base = _safe_div(ppnenet, ppneg)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f043_ppne_footprint_core137_stability_12q_v138_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    base = _pct_change(ppnenet, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f043_ppne_footprint_core138_stability_12q_v139_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    base = _safe_div(ppnenet, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f043_ppne_footprint_core139_stability_12q_v140_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    base = _log(ppnenet.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f043_ppne_footprint_core140_level_v141_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(ppnenet)
def cg_f043_ppne_footprint_core141_gross_level_v142_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(ppneg)
def cg_f043_ppne_footprint_core142_ratio_assets_v143_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_safe_div(ppnenet, assets))
def cg_f043_ppne_footprint_core143_gross_ratio_assets_v144_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_safe_div(ppneg, assets))
def cg_f043_ppne_footprint_core144_ratio_rev_v145_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_safe_div(ppnenet, revenue))
def cg_f043_ppne_footprint_core145_ratio_equity_v146_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_safe_div(ppnenet, equity.abs() + 1.0))
def cg_f043_ppne_footprint_core146_age_proxy_v147_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    # Higher implies newer or less depreciated.
    return _clean(_safe_div(ppnenet, ppneg))
def cg_f043_ppne_footprint_core147_growth_yoy_v148_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_pct_change(ppnenet, 4))
def cg_f043_ppne_footprint_core148_ratio_opex_v149_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_safe_div(ppnenet, opex.abs() + 1.0))
def cg_f043_ppne_footprint_core149_log_level_v150_signal(ppnenet, ppneg, assets, revenue, marketcap, equity, ncfo, opex):
    return _clean(_log(ppnenet.clip(lower=1.0)))
