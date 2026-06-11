import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f044_inventory_dynamics_core75_pct_4q_v076_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(inventory, ncfo.abs() + 1.0), 4))
def cg_f044_inventory_dynamics_core76_pct_4q_v077_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(inventory, marketcap), 4))
def cg_f044_inventory_dynamics_core77_pct_4q_v078_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_pct_change(inventory, 4), 4))
def cg_f044_inventory_dynamics_core78_pct_4q_v079_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_pct_change(inventory, 4) - _pct_change(revenue, 4), 4))
def cg_f044_inventory_dynamics_core79_pct_4q_v080_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_log(inventory.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f044_inventory_dynamics_core80_std_8q_v081_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(inventory, 8))
def cg_f044_inventory_dynamics_core81_std_8q_v082_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_safe_div(inventory, assets), 8))
def cg_f044_inventory_dynamics_core82_std_8q_v083_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_safe_div(inventory, revenue), 8))
def cg_f044_inventory_dynamics_core83_std_8q_v084_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_safe_div(inventory, cor), 8))
def cg_f044_inventory_dynamics_core84_std_8q_v085_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_safe_div(inventory, marketcap), 8))
def cg_f044_inventory_dynamics_core85_std_8q_v086_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_safe_div(inventory, equity.abs() + 1.0), 8))
def cg_f044_inventory_dynamics_core86_std_8q_v087_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_safe_div(inventory, ncfo.abs() + 1.0), 8))
def cg_f044_inventory_dynamics_core87_std_8q_v088_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_pct_change(inventory, 4), 8))
def cg_f044_inventory_dynamics_core88_std_8q_v089_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_pct_change(inventory, 4) - _pct_change(revenue, 4), 8))
def cg_f044_inventory_dynamics_core89_std_8q_v090_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_log(inventory.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f044_inventory_dynamics_core90_log_v091_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(inventory.clip(lower=1.0)))
def cg_f044_inventory_dynamics_core91_log_v092_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_safe_div(inventory, assets).clip(lower=0.0001)))
def cg_f044_inventory_dynamics_core92_log_v093_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_safe_div(inventory, revenue).clip(lower=0.0001)))
def cg_f044_inventory_dynamics_core93_log_v094_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_safe_div(inventory, cor).clip(lower=0.0001)))
def cg_f044_inventory_dynamics_core94_log_v095_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_safe_div(inventory, marketcap).clip(lower=0.0001)))
def cg_f044_inventory_dynamics_core95_log_v096_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_safe_div(inventory, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f044_inventory_dynamics_core96_log_v097_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_safe_div(inventory, ncfo.abs() + 1.0).clip(lower=0.001)))
def cg_f044_inventory_dynamics_core97_log_v098_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_pct_change(inventory, 4).clip(lower=-0.9) + 1.1))
def cg_f044_inventory_dynamics_core98_log_v099_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log((_pct_change(inventory, 4) - _pct_change(revenue, 4)).clip(lower=-0.9) + 1.1))
def cg_f044_inventory_dynamics_core99_log_v100_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(assets.clip(lower=1.0)))

# Block 100-109: diff 1q
def cg_f044_inventory_dynamics_core100_diff_1q_v101_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(inventory, 1))
def cg_f044_inventory_dynamics_core101_diff_1q_v102_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_safe_div(inventory, assets), 1))
def cg_f044_inventory_dynamics_core102_diff_1q_v103_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_safe_div(inventory, revenue), 1))
def cg_f044_inventory_dynamics_core103_diff_1q_v104_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_safe_div(inventory, cor), 1))
def cg_f044_inventory_dynamics_core104_diff_1q_v105_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_safe_div(inventory, marketcap), 1))
def cg_f044_inventory_dynamics_core105_diff_1q_v106_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_safe_div(inventory, equity.abs() + 1.0), 1))
def cg_f044_inventory_dynamics_core106_diff_1q_v107_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_safe_div(inventory, ncfo.abs() + 1.0), 1))
def cg_f044_inventory_dynamics_core107_diff_1q_v108_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_pct_change(inventory, 4), 1))
def cg_f044_inventory_dynamics_core108_diff_1q_v109_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_pct_change(inventory, 4) - _pct_change(revenue, 4), 1))
def cg_f044_inventory_dynamics_core109_diff_1q_v110_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_log(inventory.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f044_inventory_dynamics_core110_slope_4q_v111_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(inventory, 4))
def cg_f044_inventory_dynamics_core111_slope_4q_v112_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_safe_div(inventory, assets), 4))
def cg_f044_inventory_dynamics_core112_slope_4q_v113_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_safe_div(inventory, revenue), 4))
def cg_f044_inventory_dynamics_core113_slope_4q_v114_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_safe_div(inventory, cor), 4))
def cg_f044_inventory_dynamics_core114_slope_4q_v115_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_safe_div(inventory, marketcap), 4))
def cg_f044_inventory_dynamics_core115_slope_4q_v116_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_safe_div(inventory, equity.abs() + 1.0), 4))
def cg_f044_inventory_dynamics_core116_slope_4q_v117_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_safe_div(inventory, ncfo.abs() + 1.0), 4))
def cg_f044_inventory_dynamics_core117_slope_4q_v118_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_pct_change(inventory, 4), 4))
def cg_f044_inventory_dynamics_core118_slope_4q_v119_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_pct_change(inventory, 4) - _pct_change(revenue, 4), 4))
def cg_f044_inventory_dynamics_core119_slope_4q_v120_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_log(inventory.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f044_inventory_dynamics_core120_ewm_8q_v121_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(inventory, 8))
def cg_f044_inventory_dynamics_core121_ewm_8q_v122_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(inventory, assets), 8))
def cg_f044_inventory_dynamics_core122_ewm_8q_v123_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(inventory, revenue), 8))
def cg_f044_inventory_dynamics_core123_ewm_8q_v124_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(inventory, cor), 8))
def cg_f044_inventory_dynamics_core124_ewm_8q_v125_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(inventory, marketcap), 8))
def cg_f044_inventory_dynamics_core125_ewm_8q_v126_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(inventory, equity.abs() + 1.0), 8))
def cg_f044_inventory_dynamics_core126_ewm_8q_v127_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(inventory, ncfo.abs() + 1.0), 8))
def cg_f044_inventory_dynamics_core127_ewm_8q_v128_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_pct_change(inventory, 4), 8))
def cg_f044_inventory_dynamics_core128_ewm_8q_v129_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_pct_change(inventory, 4) - _pct_change(revenue, 4), 8))
def cg_f044_inventory_dynamics_core129_ewm_8q_v130_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_log(inventory.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f044_inventory_dynamics_core130_stability_12q_v131_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_safe_div(_std(inventory, 12), _mean(inventory, 12).abs() + 1.0))
def cg_f044_inventory_dynamics_core131_stability_12q_v132_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    base = _safe_div(inventory, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f044_inventory_dynamics_core132_stability_12q_v133_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    base = _safe_div(inventory, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f044_inventory_dynamics_core133_stability_12q_v134_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    base = _safe_div(inventory, cor)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f044_inventory_dynamics_core134_stability_12q_v135_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    base = _safe_div(inventory, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f044_inventory_dynamics_core135_stability_12q_v136_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    base = _safe_div(inventory, ncfo.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f044_inventory_dynamics_core136_stability_12q_v137_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    base = _safe_div(inventory, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f044_inventory_dynamics_core137_stability_12q_v138_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    base = _pct_change(inventory, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f044_inventory_dynamics_core138_stability_12q_v139_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    base = _pct_change(inventory, 4) - _pct_change(revenue, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f044_inventory_dynamics_core139_stability_12q_v140_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    base = _log(inventory.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f044_inventory_dynamics_core140_level_v141_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(inventory)
def cg_f044_inventory_dynamics_core141_ratio_assets_v142_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_safe_div(inventory, assets))
def cg_f044_inventory_dynamics_core142_ratio_rev_v143_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_safe_div(inventory, revenue))
def cg_f044_inventory_dynamics_core143_ratio_cor_v144_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_safe_div(inventory, cor))
def cg_f044_inventory_dynamics_core144_ratio_ncfo_v145_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_safe_div(inventory, ncfo.abs() + 1.0))
def cg_f044_inventory_dynamics_core145_growth_yoy_v146_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(inventory, 4))
def cg_f044_inventory_dynamics_core146_growth_spread_v147_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(inventory, 4) - _pct_change(revenue, 4))
def cg_f044_inventory_dynamics_core147_ratio_equity_v148_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_safe_div(inventory, equity.abs() + 1.0))
def cg_f044_inventory_dynamics_core148_ratio_mcap_v149_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_safe_div(inventory, marketcap))
def cg_f044_inventory_dynamics_core149_log_level_v150_signal(inventory, cor, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(inventory.clip(lower=1.0)))
