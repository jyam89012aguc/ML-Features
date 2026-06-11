import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f040_asset_base_core75_pct_4q_v076_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_safe_div(assets - liabilities, assets), 4))
def cg_f040_asset_base_core76_pct_4q_v077_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_safe_div(assets, sharesbas), 4))
def cg_f040_asset_base_core77_pct_4q_v078_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_safe_div(assets, opex.abs() + 1.0), 4))
def cg_f040_asset_base_core78_pct_4q_v079_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_pct_change(assets, 4), 4))
def cg_f040_asset_base_core79_pct_4q_v080_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_log(assets.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f040_asset_base_core80_std_8q_v081_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_std(assets, 8))
def cg_f040_asset_base_core81_std_8q_v082_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_std(_safe_div(assetsc, assets), 8))
def cg_f040_asset_base_core82_std_8q_v083_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_std(_safe_div(assets, revenue), 8))
def cg_f040_asset_base_core83_std_8q_v084_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_std(_safe_div(assets, marketcap), 8))
def cg_f040_asset_base_core84_std_8q_v085_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_std(_safe_div(assets, equity.abs() + 1.0), 8))
def cg_f040_asset_base_core85_std_8q_v086_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_std(_safe_div(assets - liabilities, assets), 8))
def cg_f040_asset_base_core86_std_8q_v087_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_std(_safe_div(assets, sharesbas), 8))
def cg_f040_asset_base_core87_std_8q_v088_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_std(_pct_change(assets, 4), 8))
def cg_f040_asset_base_core88_std_8q_v089_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_std(_safe_div(assets, opex.abs() + 1.0), 8))
def cg_f040_asset_base_core89_std_8q_v090_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_std(_log(assets.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f040_asset_base_core90_log_v091_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_log(assets.clip(lower=1.0)))
def cg_f040_asset_base_core91_log_v092_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_log(_safe_div(assetsc, assets).clip(lower=0.001)))
def cg_f040_asset_base_core92_log_v093_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_log(_safe_div(assets, revenue).clip(lower=0.0001)))
def cg_f040_asset_base_core93_log_v094_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_log(_safe_div(assets, marketcap).clip(lower=0.0001)))
def cg_f040_asset_base_core94_log_v095_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_log(_safe_div(assets, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f040_asset_base_core95_log_v096_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_log(_safe_div(assets - liabilities, assets).abs().clip(lower=0.01)))
def cg_f040_asset_base_core96_log_v097_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_log(_safe_div(assets, sharesbas).clip(lower=0.1)))
def cg_f040_asset_base_core97_log_v098_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_log(_pct_change(assets, 4).clip(lower=-0.9) + 1.1))
def cg_f040_asset_base_core98_log_v099_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_log(_safe_div(assets, opex.abs() + 1.0).clip(lower=0.001)))
def cg_f040_asset_base_core99_log_v100_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_log(revenue.clip(lower=1.0)))

# Block 100-109: diff 1q
def cg_f040_asset_base_core100_diff_1q_v101_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_diff(assets, 1))
def cg_f040_asset_base_core101_diff_1q_v102_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_diff(_safe_div(assetsc, assets), 1))
def cg_f040_asset_base_core102_diff_1q_v103_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_diff(_safe_div(assets, revenue), 1))
def cg_f040_asset_base_core103_diff_1q_v104_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_diff(_safe_div(assets, marketcap), 1))
def cg_f040_asset_base_core104_diff_1q_v105_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_diff(_safe_div(assets, equity.abs() + 1.0), 1))
def cg_f040_asset_base_core105_diff_1q_v106_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_diff(_safe_div(assets - liabilities, assets), 1))
def cg_f040_asset_base_core106_diff_1q_v107_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_diff(_safe_div(assets, sharesbas), 1))
def cg_f040_asset_base_core107_diff_1q_v108_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_diff(_pct_change(assets, 4), 1))
def cg_f040_asset_base_core108_diff_1q_v109_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_diff(_safe_div(assets, opex.abs() + 1.0), 1))
def cg_f040_asset_base_core109_diff_1q_v110_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_diff(_log(assets.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f040_asset_base_core110_slope_4q_v111_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_slope(assets, 4))
def cg_f040_asset_base_core111_slope_4q_v112_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_slope(_safe_div(assetsc, assets), 4))
def cg_f040_asset_base_core112_slope_4q_v113_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_slope(_safe_div(assets, revenue), 4))
def cg_f040_asset_base_core113_slope_4q_v114_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_slope(_safe_div(assets, marketcap), 4))
def cg_f040_asset_base_core114_slope_4q_v115_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_slope(_safe_div(assets, equity.abs() + 1.0), 4))
def cg_f040_asset_base_core115_slope_4q_v116_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_slope(_safe_div(assets - liabilities, assets), 4))
def cg_f040_asset_base_core116_slope_4q_v117_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_slope(_safe_div(assets, sharesbas), 4))
def cg_f040_asset_base_core117_slope_4q_v118_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_slope(_pct_change(assets, 4), 4))
def cg_f040_asset_base_core118_slope_4q_v119_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_slope(_safe_div(assets, opex.abs() + 1.0), 4))
def cg_f040_asset_base_core119_slope_4q_v120_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_slope(_log(assets.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f040_asset_base_core120_ewm_8q_v121_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_ewm(assets, 8))
def cg_f040_asset_base_core121_ewm_8q_v122_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_ewm(_safe_div(assetsc, assets), 8))
def cg_f040_asset_base_core122_ewm_8q_v123_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_ewm(_safe_div(assets, revenue), 8))
def cg_f040_asset_base_core123_ewm_8q_v124_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_ewm(_safe_div(assets, marketcap), 8))
def cg_f040_asset_base_core124_ewm_8q_v125_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_ewm(_safe_div(assets, equity.abs() + 1.0), 8))
def cg_f040_asset_base_core125_ewm_8q_v126_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_ewm(_safe_div(assets - liabilities, assets), 8))
def cg_f040_asset_base_core126_ewm_8q_v127_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_ewm(_safe_div(assets, sharesbas), 8))
def cg_f040_asset_base_core127_ewm_8q_v128_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_ewm(_pct_change(assets, 4), 8))
def cg_f040_asset_base_core128_ewm_8q_v129_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_ewm(_safe_div(assets, opex.abs() + 1.0), 8))
def cg_f040_asset_base_core129_ewm_8q_v130_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_ewm(_log(assets.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f040_asset_base_core130_stability_12q_v131_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_safe_div(_std(assets, 12), _mean(assets, 12).abs() + 1.0))
def cg_f040_asset_base_core131_stability_12q_v132_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    base = _safe_div(assetsc, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f040_asset_base_core132_stability_12q_v133_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    base = _safe_div(assets, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f040_asset_base_core133_stability_12q_v134_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    base = _safe_div(assets, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f040_asset_base_core134_stability_12q_v135_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    base = _safe_div(assets, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f040_asset_base_core135_stability_12q_v136_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    base = _safe_div(assets - liabilities, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f040_asset_base_core136_stability_12q_v137_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    base = _safe_div(assets, sharesbas)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f040_asset_base_core137_stability_12q_v138_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    base = _pct_change(assets, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f040_asset_base_core138_stability_12q_v139_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    base = assets
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f040_asset_base_core139_stability_12q_v140_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    base = _log(assets.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f040_asset_base_core140_level_v141_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(assets)
def cg_f040_asset_base_core141_ratio_current_v142_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_safe_div(assetsc, assets))
def cg_f040_asset_base_core142_ratio_rev_v143_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_safe_div(assets, revenue))
def cg_f040_asset_base_core143_ratio_mcap_v144_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_safe_div(assets, marketcap))
def cg_f040_asset_base_core144_ratio_equity_v145_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_safe_div(assets, equity.abs() + 1.0))
def cg_f040_asset_base_core145_ratio_bv_assets_v146_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_safe_div(assets - liabilities, assets))
def cg_f040_asset_base_core146_ratio_shares_v147_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_safe_div(assets, sharesbas))
def cg_f040_asset_base_core147_growth_yoy_v148_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(assets, 4))
def cg_f040_asset_base_core148_ratio_opex_v149_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_safe_div(assets, opex.abs() + 1.0))
def cg_f040_asset_base_core149_log_level_v150_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_log(assets.clip(lower=1.0)))
