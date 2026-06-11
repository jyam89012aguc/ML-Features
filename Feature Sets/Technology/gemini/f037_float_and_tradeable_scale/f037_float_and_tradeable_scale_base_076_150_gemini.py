import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f037_float_and_tradeable_scale_core75_pct_4q_v076_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(marketcap, equity.abs() + 1.0), 4))
def cg_f037_float_and_tradeable_scale_core76_pct_4q_v077_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(marketcap, opex.abs() + 1.0), 4))
def cg_f037_float_and_tradeable_scale_core77_pct_4q_v078_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_pct_change(marketcap, 4), 4))
def cg_f037_float_and_tradeable_scale_core78_pct_4q_v079_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(volume, sharesbas * 100.0), 4))
def cg_f037_float_and_tradeable_scale_core79_pct_4q_v080_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(_log(marketcap.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f037_float_and_tradeable_scale_core80_std_8q_v081_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_std(marketcap, 8))
def cg_f037_float_and_tradeable_scale_core81_std_8q_v082_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_std(_safe_div(marketcap, assets), 8))
def cg_f037_float_and_tradeable_scale_core82_std_8q_v083_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_std(_safe_div(marketcap, revenue), 8))
def cg_f037_float_and_tradeable_scale_core83_std_8q_v084_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_std(_safe_div(volume, sharesbas), 8))
def cg_f037_float_and_tradeable_scale_core84_std_8q_v085_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_std(_safe_div(marketcap, ncfo.abs() + 1.0), 8))
def cg_f037_float_and_tradeable_scale_core85_std_8q_v086_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_std(_safe_div(marketcap, equity.abs() + 1.0), 8))
def cg_f037_float_and_tradeable_scale_core86_std_8q_v087_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_std(_safe_div(marketcap, opex.abs() + 1.0), 8))
def cg_f037_float_and_tradeable_scale_core87_std_8q_v088_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_std(_pct_change(marketcap, 4), 8))
def cg_f037_float_and_tradeable_scale_core88_std_8q_v089_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_std(_safe_div(volume, sharesbas * 100.0), 8))
def cg_f037_float_and_tradeable_scale_core89_std_8q_v090_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_std(_log(marketcap.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f037_float_and_tradeable_scale_core90_log_v091_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_log(marketcap.clip(lower=1.0)))
def cg_f037_float_and_tradeable_scale_core91_log_v092_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_log(_safe_div(marketcap, assets).clip(lower=0.0001)))
def cg_f037_float_and_tradeable_scale_core92_log_v093_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_log(_safe_div(marketcap, revenue).clip(lower=0.0001)))
def cg_f037_float_and_tradeable_scale_core93_log_v094_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_log(_safe_div(volume, sharesbas).clip(lower=0.0001)))
def cg_f037_float_and_tradeable_scale_core94_log_v095_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_log(_safe_div(marketcap, ncfo.abs() + 1.0).clip(lower=0.001)))
def cg_f037_float_and_tradeable_scale_core95_log_v096_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_log(_safe_div(marketcap, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f037_float_and_tradeable_scale_core96_log_v097_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_log(_safe_div(marketcap, opex.abs() + 1.0).clip(lower=0.001)))
def cg_f037_float_and_tradeable_scale_core97_log_v098_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_log(_pct_change(marketcap, 4).clip(lower=-0.9) + 1.1))
def cg_f037_float_and_tradeable_scale_core98_log_v099_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_log(_safe_div(volume, sharesbas * 100.0).clip(lower=0.0001)))
def cg_f037_float_and_tradeable_scale_core99_log_v100_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_log(assets.clip(lower=1.0)))

# Block 100-109: diff 1q
def cg_f037_float_and_tradeable_scale_core100_diff_1q_v101_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_diff(marketcap, 1))
def cg_f037_float_and_tradeable_scale_core101_diff_1q_v102_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_diff(_safe_div(marketcap, assets), 1))
def cg_f037_float_and_tradeable_scale_core102_diff_1q_v103_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_diff(_safe_div(marketcap, revenue), 1))
def cg_f037_float_and_tradeable_scale_core103_diff_1q_v104_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_diff(_safe_div(volume, sharesbas), 1))
def cg_f037_float_and_tradeable_scale_core104_diff_1q_v105_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_diff(_safe_div(marketcap, ncfo.abs() + 1.0), 1))
def cg_f037_float_and_tradeable_scale_core105_diff_1q_v106_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_diff(_safe_div(marketcap, equity.abs() + 1.0), 1))
def cg_f037_float_and_tradeable_scale_core106_diff_1q_v107_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_diff(_safe_div(marketcap, opex.abs() + 1.0), 1))
def cg_f037_float_and_tradeable_scale_core107_diff_1q_v108_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_diff(_pct_change(marketcap, 4), 1))
def cg_f037_float_and_tradeable_scale_core108_diff_1q_v109_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_diff(_safe_div(volume, sharesbas * 100.0), 1))
def cg_f037_float_and_tradeable_scale_core109_diff_1q_v110_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_diff(_log(marketcap.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f037_float_and_tradeable_scale_core110_slope_4q_v111_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_slope(marketcap, 4))
def cg_f037_float_and_tradeable_scale_core111_slope_4q_v112_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_slope(_safe_div(marketcap, assets), 4))
def cg_f037_float_and_tradeable_scale_core112_slope_4q_v113_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_slope(_safe_div(marketcap, revenue), 4))
def cg_f037_float_and_tradeable_scale_core113_slope_4q_v114_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_slope(_safe_div(volume, sharesbas), 4))
def cg_f037_float_and_tradeable_scale_core114_slope_4q_v115_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_slope(_safe_div(marketcap, ncfo.abs() + 1.0), 4))
def cg_f037_float_and_tradeable_scale_core115_slope_4q_v116_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_slope(_safe_div(marketcap, equity.abs() + 1.0), 4))
def cg_f037_float_and_tradeable_scale_core116_slope_4q_v117_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_slope(_safe_div(marketcap, opex.abs() + 1.0), 4))
def cg_f037_float_and_tradeable_scale_core117_slope_4q_v118_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_slope(_pct_change(marketcap, 4), 4))
def cg_f037_float_and_tradeable_scale_core118_slope_4q_v119_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_slope(_safe_div(volume, sharesbas * 100.0), 4))
def cg_f037_float_and_tradeable_scale_core119_slope_4q_v120_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_slope(_log(marketcap.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f037_float_and_tradeable_scale_core120_ewm_8q_v121_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_ewm(marketcap, 8))
def cg_f037_float_and_tradeable_scale_core121_ewm_8q_v122_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(marketcap, assets), 8))
def cg_f037_float_and_tradeable_scale_core122_ewm_8q_v123_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(marketcap, revenue), 8))
def cg_f037_float_and_tradeable_scale_core123_ewm_8q_v124_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(volume, sharesbas), 8))
def cg_f037_float_and_tradeable_scale_core124_ewm_8q_v125_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(marketcap, ncfo.abs() + 1.0), 8))
def cg_f037_float_and_tradeable_scale_core125_ewm_8q_v126_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(marketcap, equity.abs() + 1.0), 8))
def cg_f037_float_and_tradeable_scale_core126_ewm_8q_v127_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(marketcap, opex.abs() + 1.0), 8))
def cg_f037_float_and_tradeable_scale_core127_ewm_8q_v128_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_ewm(_pct_change(marketcap, 4), 8))
def cg_f037_float_and_tradeable_scale_core128_ewm_8q_v129_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(volume, sharesbas * 100.0), 8))
def cg_f037_float_and_tradeable_scale_core129_ewm_8q_v130_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_ewm(_log(marketcap.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f037_float_and_tradeable_scale_core130_stability_12q_v131_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_safe_div(_std(marketcap, 12), _mean(marketcap, 12).abs() + 1.0))
def cg_f037_float_and_tradeable_scale_core131_stability_12q_v132_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    base = _safe_div(marketcap, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f037_float_and_tradeable_scale_core132_stability_12q_v133_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    base = _safe_div(marketcap, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f037_float_and_tradeable_scale_core133_stability_12q_v134_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    base = _safe_div(volume, sharesbas)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f037_float_and_tradeable_scale_core134_stability_12q_v135_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    base = _safe_div(marketcap, ncfo.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f037_float_and_tradeable_scale_core135_stability_12q_v136_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    base = _safe_div(marketcap, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f037_float_and_tradeable_scale_core136_stability_12q_v137_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    base = _safe_div(marketcap, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f037_float_and_tradeable_scale_core137_stability_12q_v138_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    base = _pct_change(marketcap, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f037_float_and_tradeable_scale_core138_stability_12q_v139_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    base = _safe_div(volume, sharesbas * 100.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f037_float_and_tradeable_scale_core139_stability_12q_v140_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    base = _log(marketcap.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f037_float_and_tradeable_scale_core140_mcap_level_v141_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(marketcap)
def cg_f037_float_and_tradeable_scale_core141_mcap_assets_v142_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_safe_div(marketcap, assets))
def cg_f037_float_and_tradeable_scale_core142_mcap_rev_v143_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_safe_div(marketcap, revenue))
def cg_f037_float_and_tradeable_scale_core143_turnover_v144_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_safe_div(volume, sharesbas))
def cg_f037_float_and_tradeable_scale_core144_mcap_ncfo_v145_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_safe_div(marketcap, ncfo.abs() + 1.0))
def cg_f037_float_and_tradeable_scale_core145_mcap_equity_v146_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_safe_div(marketcap, equity.abs() + 1.0))
def cg_f037_float_and_tradeable_scale_core146_mcap_opex_v147_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_safe_div(marketcap, opex.abs() + 1.0))
def cg_f037_float_and_tradeable_scale_core147_mcap_growth_v148_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_pct_change(marketcap, 4))
def cg_f037_float_and_tradeable_scale_core148_volume_scale_v149_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_safe_div(volume, sharesbas * 100.0))
def cg_f037_float_and_tradeable_scale_core149_mcap_log_v150_signal(marketcap, sharesbas, volume, assets, revenue, ncfo, equity, opex):
    return _clean(_log(marketcap.clip(lower=1.0)))
