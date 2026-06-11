import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f041_tangible_assets_core75_pct_4q_v076_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_pct_change(_safe_div(tangible, liabilities.abs() + 1.0), 4))
def cg_f041_tangible_assets_core76_pct_4q_v077_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_pct_change(_safe_div(tangible, opex.abs() + 1.0), 4))
def cg_f041_tangible_assets_core77_pct_4q_v078_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_pct_change(_pct_change(tangible, 4), 4))
def cg_f041_tangible_assets_core78_pct_4q_v079_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_pct_change(_safe_div(tangible, assets - liabilities), 4))
def cg_f041_tangible_assets_core79_pct_4q_v080_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_pct_change(_log(tangible.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f041_tangible_assets_core80_std_8q_v081_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_std(tangible, 8))
def cg_f041_tangible_assets_core81_std_8q_v082_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_std(_safe_div(tangible, assets), 8))
def cg_f041_tangible_assets_core82_std_8q_v083_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_std(_safe_div(tangible, revenue), 8))
def cg_f041_tangible_assets_core83_std_8q_v084_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_std(_safe_div(tangible, marketcap), 8))
def cg_f041_tangible_assets_core84_std_8q_v085_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_std(_safe_div(tangible, equity.abs() + 1.0), 8))
def cg_f041_tangible_assets_core85_std_8q_v086_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_std(_safe_div(tangible, liabilities.abs() + 1.0), 8))
def cg_f041_tangible_assets_core86_std_8q_v087_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_std(_safe_div(tangible, opex.abs() + 1.0), 8))
def cg_f041_tangible_assets_core87_std_8q_v088_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_std(_pct_change(tangible, 4), 8))
def cg_f041_tangible_assets_core88_std_8q_v089_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_std(_safe_div(tangible, assets - liabilities), 8))
def cg_f041_tangible_assets_core89_std_8q_v090_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_std(_log(tangible.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f041_tangible_assets_core90_log_v091_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_log(tangible.clip(lower=1.0)))
def cg_f041_tangible_assets_core91_log_v092_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_log(_safe_div(tangible, assets).clip(lower=0.001)))
def cg_f041_tangible_assets_core92_log_v093_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_log(_safe_div(tangible, revenue).clip(lower=0.0001)))
def cg_f041_tangible_assets_core93_log_v094_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_log(_safe_div(tangible, marketcap).clip(lower=0.0001)))
def cg_f041_tangible_assets_core94_log_v095_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_log(_safe_div(tangible, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f041_tangible_assets_core95_log_v096_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_log(_safe_div(tangible, liabilities.abs() + 1.0).abs().clip(lower=0.001)))
def cg_f041_tangible_assets_core96_log_v097_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_log(_safe_div(tangible, opex.abs() + 1.0).clip(lower=0.1)))
def cg_f041_tangible_assets_core97_log_v098_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_log(_pct_change(tangible, 4).clip(lower=-0.9) + 1.1))
def cg_f041_tangible_assets_core98_log_v099_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_log(_safe_div(tangible, assets - liabilities).clip(lower=0.001)))
def cg_f041_tangible_assets_core99_log_v100_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_log(assets.clip(lower=1.0)))

# Block 100-109: diff 1q
def cg_f041_tangible_assets_core100_diff_1q_v101_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_diff(tangible, 1))
def cg_f041_tangible_assets_core101_diff_1q_v102_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_diff(_safe_div(tangible, assets), 1))
def cg_f041_tangible_assets_core102_diff_1q_v103_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_diff(_safe_div(tangible, revenue), 1))
def cg_f041_tangible_assets_core103_diff_1q_v104_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_diff(_safe_div(tangible, marketcap), 1))
def cg_f041_tangible_assets_core104_diff_1q_v105_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_diff(_safe_div(tangible, equity.abs() + 1.0), 1))
def cg_f041_tangible_assets_core105_diff_1q_v106_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_diff(_safe_div(tangible, liabilities.abs() + 1.0), 1))
def cg_f041_tangible_assets_core106_diff_1q_v107_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_diff(_safe_div(tangible, opex.abs() + 1.0), 1))
def cg_f041_tangible_assets_core107_diff_1q_v108_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_diff(_pct_change(tangible, 4), 1))
def cg_f041_tangible_assets_core108_diff_1q_v109_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_diff(_safe_div(tangible, assets - liabilities), 1))
def cg_f041_tangible_assets_core109_diff_1q_v110_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_diff(_log(tangible.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f041_tangible_assets_core110_slope_4q_v111_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_slope(tangible, 4))
def cg_f041_tangible_assets_core111_slope_4q_v112_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_slope(_safe_div(tangible, assets), 4))
def cg_f041_tangible_assets_core112_slope_4q_v113_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_slope(_safe_div(tangible, revenue), 4))
def cg_f041_tangible_assets_core113_slope_4q_v114_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_slope(_safe_div(tangible, marketcap), 4))
def cg_f041_tangible_assets_core114_slope_4q_v115_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_slope(_safe_div(tangible, equity.abs() + 1.0), 4))
def cg_f041_tangible_assets_core115_slope_4q_v116_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_slope(_safe_div(tangible, liabilities.abs() + 1.0), 4))
def cg_f041_tangible_assets_core116_slope_4q_v117_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_slope(_safe_div(tangible, opex.abs() + 1.0), 4))
def cg_f041_tangible_assets_core117_slope_4q_v118_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_slope(_pct_change(tangible, 4), 4))
def cg_f041_tangible_assets_core118_slope_4q_v119_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_slope(_safe_div(tangible, assets - liabilities), 4))
def cg_f041_tangible_assets_core119_slope_4q_v120_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_slope(_log(tangible.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f041_tangible_assets_core120_ewm_8q_v121_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_ewm(tangible, 8))
def cg_f041_tangible_assets_core121_ewm_8q_v122_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_ewm(_safe_div(tangible, assets), 8))
def cg_f041_tangible_assets_core122_ewm_8q_v123_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_ewm(_safe_div(tangible, revenue), 8))
def cg_f041_tangible_assets_core123_ewm_8q_v124_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_ewm(_safe_div(tangible, marketcap), 8))
def cg_f041_tangible_assets_core124_ewm_8q_v125_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_ewm(_safe_div(tangible, equity.abs() + 1.0), 8))
def cg_f041_tangible_assets_core125_ewm_8q_v126_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_ewm(_safe_div(tangible, liabilities.abs() + 1.0), 8))
def cg_f041_tangible_assets_core126_ewm_8q_v127_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_ewm(_safe_div(tangible, opex.abs() + 1.0), 8))
def cg_f041_tangible_assets_core127_ewm_8q_v128_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_ewm(_pct_change(tangible, 4), 8))
def cg_f041_tangible_assets_core128_ewm_8q_v129_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_ewm(_safe_div(tangible, assets - liabilities), 8))
def cg_f041_tangible_assets_core129_ewm_8q_v130_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_ewm(_log(tangible.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f041_tangible_assets_core130_stability_12q_v131_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_safe_div(_std(tangible, 12), _mean(tangible, 12).abs() + 1.0))
def cg_f041_tangible_assets_core131_stability_12q_v132_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    base = _safe_div(tangible, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f041_tangible_assets_core132_stability_12q_v133_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    base = _safe_div(tangible, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f041_tangible_assets_core133_stability_12q_v134_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    base = _safe_div(tangible, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f041_tangible_assets_core134_stability_12q_v135_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    base = _safe_div(tangible, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f041_tangible_assets_core135_stability_12q_v136_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    base = _safe_div(tangible, liabilities.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f041_tangible_assets_core136_stability_12q_v137_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    base = _safe_div(tangible, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f041_tangible_assets_core137_stability_12q_v138_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    base = _pct_change(tangible, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f041_tangible_assets_core138_stability_12q_v139_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    base = tangible
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f041_tangible_assets_core139_stability_12q_v140_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    base = _log(tangible.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f041_tangible_assets_core140_level_v141_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(tangible)
def cg_f041_tangible_assets_core141_ratio_assets_v142_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_safe_div(tangible, assets))
def cg_f041_tangible_assets_core142_ratio_rev_v143_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_safe_div(tangible, revenue))
def cg_f041_tangible_assets_core143_ratio_mcap_v144_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_safe_div(tangible, marketcap))
def cg_f041_tangible_assets_core144_ratio_equity_v145_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_safe_div(tangible, equity.abs() + 1.0))
def cg_f041_tangible_assets_core145_ratio_bv_assets_v146_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_safe_div(tangible, assets - liabilities))
def cg_f041_tangible_assets_core146_ratio_liab_v147_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_safe_div(tangible, liabilities.abs() + 1.0))
def cg_f041_tangible_assets_core147_growth_yoy_v148_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_pct_change(tangible, 4))
def cg_f041_tangible_assets_core148_ratio_opex_v149_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_safe_div(tangible, opex.abs() + 1.0))
def cg_f041_tangible_assets_core149_log_level_v150_signal(assets, intangibles, goodwill, revenue, marketcap, equity, liabilities, opex):
    tangible = assets - intangibles.fillna(0) - goodwill.fillna(0)
    return _clean(_log(tangible.clip(lower=1.0)))
