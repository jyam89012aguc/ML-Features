import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f035_buyback_share_reduction_core75_pct_4q_v076_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction_value = _pct_change(sharesbas, 1).clip(upper=0).abs() * marketcap
    return _clean(_pct_change(_safe_div(reduction_value, ncfo.abs() + 1.0), 4))
def cg_f035_buyback_share_reduction_core76_pct_4q_v077_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(_diff(sharesbas, 4).clip(upper=0).abs(), 4))
def cg_f035_buyback_share_reduction_core77_pct_4q_v078_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncff, equity.abs() + 1.0), 4))
def cg_f035_buyback_share_reduction_core78_pct_4q_v079_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(ncff, 4))
def cg_f035_buyback_share_reduction_core79_pct_4q_v080_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(_log(sharesbas.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f035_buyback_share_reduction_core80_std_8q_v081_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 1).clip(upper=0).abs()
    return _clean(_std(reduction, 8))
def cg_f035_buyback_share_reduction_core81_std_8q_v082_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_std(_safe_div(ncff, marketcap), 8))
def cg_f035_buyback_share_reduction_core82_std_8q_v083_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_std(_safe_div(ncff, ncfo.abs() + 1.0), 8))
def cg_f035_buyback_share_reduction_core83_std_8q_v084_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_std(_pct_change(sharesbas, 4).clip(upper=0).abs(), 8))
def cg_f035_buyback_share_reduction_core84_std_8q_v085_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_std(_safe_div(ncff, assets), 8))
def cg_f035_buyback_share_reduction_core85_std_8q_v086_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_std(_safe_div(ncff, revenue), 8))
def cg_f035_buyback_share_reduction_core86_std_8q_v087_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction_value = _pct_change(sharesbas, 1).clip(upper=0).abs() * marketcap
    return _clean(_std(_safe_div(reduction_value, ncfo.abs() + 1.0), 8))
def cg_f035_buyback_share_reduction_core87_std_8q_v088_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_std(_safe_div(ncff, equity.abs() + 1.0), 8))
def cg_f035_buyback_share_reduction_core88_std_8q_v089_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_std(ncff, 8))
def cg_f035_buyback_share_reduction_core89_std_8q_v090_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_std(_log(sharesbas.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f035_buyback_share_reduction_core90_log_v091_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_log(sharesbas.clip(lower=1.0)))
def cg_f035_buyback_share_reduction_core91_log_v092_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_log(_pct_change(sharesbas, 1).clip(upper=0).abs().clip(lower=0.001)))
def cg_f035_buyback_share_reduction_core92_log_v093_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_log(_safe_div(ncff.abs(), marketcap).clip(lower=0.0001)))
def cg_f035_buyback_share_reduction_core93_log_v094_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_log(_safe_div(ncff.abs(), ncfo.abs() + 1.0).clip(lower=0.001)))
def cg_f035_buyback_share_reduction_core94_log_v095_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_log(_pct_change(sharesbas, 4).clip(upper=0).abs().clip(lower=0.001)))
def cg_f035_buyback_share_reduction_core95_log_v096_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_log(_safe_div(ncff.abs(), assets).clip(lower=0.0001)))
def cg_f035_buyback_share_reduction_core96_log_v097_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_log(_safe_div(ncff.abs(), revenue).clip(lower=0.0001)))
def cg_f035_buyback_share_reduction_core97_log_v098_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction_value = _pct_change(sharesbas, 1).clip(upper=0).abs() * marketcap
    return _clean(_log(_safe_div(reduction_value, ncfo.abs() + 1.0).clip(lower=0.001)))
def cg_f035_buyback_share_reduction_core98_log_v099_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_log(_safe_div(ncff.abs(), equity.abs() + 1.0).clip(lower=0.001)))
def cg_f035_buyback_share_reduction_core99_log_v100_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_log(marketcap.clip(lower=1.0)))

# Block 100-109: diff 1q
def cg_f035_buyback_share_reduction_core100_diff_1q_v101_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 1).clip(upper=0).abs()
    return _clean(_diff(reduction, 1))
def cg_f035_buyback_share_reduction_core101_diff_1q_v102_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_diff(_safe_div(ncff, marketcap), 1))
def cg_f035_buyback_share_reduction_core102_diff_1q_v103_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_diff(_safe_div(ncff, ncfo.abs() + 1.0), 1))
def cg_f035_buyback_share_reduction_core103_diff_1q_v104_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 4).clip(upper=0).abs()
    return _clean(_diff(reduction, 1))
def cg_f035_buyback_share_reduction_core104_diff_1q_v105_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_diff(_safe_div(ncff, assets), 1))
def cg_f035_buyback_share_reduction_core105_diff_1q_v106_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_diff(_safe_div(ncff, revenue), 1))
def cg_f035_buyback_share_reduction_core106_diff_1q_v107_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction_value = _pct_change(sharesbas, 1).clip(upper=0).abs() * marketcap
    return _clean(_diff(_safe_div(reduction_value, ncfo.abs() + 1.0), 1))
def cg_f035_buyback_share_reduction_core107_diff_1q_v108_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_diff(_safe_div(ncff, equity.abs() + 1.0), 1))
def cg_f035_buyback_share_reduction_core108_diff_1q_v109_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_diff(ncff, 1))
def cg_f035_buyback_share_reduction_core109_diff_1q_v110_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_diff(_log(sharesbas.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f035_buyback_share_reduction_core110_slope_4q_v111_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 1).clip(upper=0).abs()
    return _clean(_slope(reduction, 4))
def cg_f035_buyback_share_reduction_core111_slope_4q_v112_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_slope(_safe_div(ncff, marketcap), 4))
def cg_f035_buyback_share_reduction_core112_slope_4q_v113_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_slope(_safe_div(ncff, ncfo.abs() + 1.0), 4))
def cg_f035_buyback_share_reduction_core113_slope_4q_v114_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 4).clip(upper=0).abs()
    return _clean(_slope(reduction, 4))
def cg_f035_buyback_share_reduction_core114_slope_4q_v115_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_slope(_safe_div(ncff, assets), 4))
def cg_f035_buyback_share_reduction_core115_slope_4q_v116_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_slope(_safe_div(ncff, revenue), 4))
def cg_f035_buyback_share_reduction_core116_slope_4q_v117_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction_value = _pct_change(sharesbas, 1).clip(upper=0).abs() * marketcap
    return _clean(_slope(_safe_div(reduction_value, ncfo.abs() + 1.0), 4))
def cg_f035_buyback_share_reduction_core117_slope_4q_v118_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_slope(_safe_div(ncff, equity.abs() + 1.0), 4))
def cg_f035_buyback_share_reduction_core118_slope_4q_v119_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_slope(ncff, 4))
def cg_f035_buyback_share_reduction_core119_slope_4q_v120_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_slope(_log(sharesbas.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f035_buyback_share_reduction_core120_ewm_8q_v121_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 1).clip(upper=0).abs()
    return _clean(_ewm(reduction, 8))
def cg_f035_buyback_share_reduction_core121_ewm_8q_v122_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(ncff, marketcap), 8))
def cg_f035_buyback_share_reduction_core122_ewm_8q_v123_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(ncff, ncfo.abs() + 1.0), 8))
def cg_f035_buyback_share_reduction_core123_ewm_8q_v124_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 4).clip(upper=0).abs()
    return _clean(_ewm(reduction, 8))
def cg_f035_buyback_share_reduction_core124_ewm_8q_v125_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(ncff, assets), 8))
def cg_f035_buyback_share_reduction_core125_ewm_8q_v126_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(ncff, revenue), 8))
def cg_f035_buyback_share_reduction_core126_ewm_8q_v127_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction_value = _pct_change(sharesbas, 1).clip(upper=0).abs() * marketcap
    return _clean(_ewm(_safe_div(reduction_value, ncfo.abs() + 1.0), 8))
def cg_f035_buyback_share_reduction_core127_ewm_8q_v128_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(ncff, equity.abs() + 1.0), 8))
def cg_f035_buyback_share_reduction_core128_ewm_8q_v129_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_ewm(ncff, 8))
def cg_f035_buyback_share_reduction_core129_ewm_8q_v130_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_ewm(_log(sharesbas.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f035_buyback_share_reduction_core130_stability_12q_v131_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 1).clip(upper=0).abs()
    return _clean(_safe_div(_std(reduction, 12), _mean(reduction, 12).abs() + 1.0))
def cg_f035_buyback_share_reduction_core131_stability_12q_v132_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    base = _safe_div(ncff, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f035_buyback_share_reduction_core132_stability_12q_v133_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    base = _safe_div(ncff, ncfo.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f035_buyback_share_reduction_core133_stability_12q_v134_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction = _pct_change(sharesbas, 4).clip(upper=0).abs()
    return _clean(_safe_div(_std(reduction, 12), _mean(reduction, 12).abs() + 1.0))
def cg_f035_buyback_share_reduction_core134_stability_12q_v135_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    base = _safe_div(ncff, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f035_buyback_share_reduction_core135_stability_12q_v136_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    base = _safe_div(ncff, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f035_buyback_share_reduction_core136_stability_12q_v137_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction_value = _pct_change(sharesbas, 1).clip(upper=0).abs() * marketcap
    base = _safe_div(reduction_value, ncfo.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f035_buyback_share_reduction_core137_stability_12q_v138_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    base = _safe_div(ncff, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f035_buyback_share_reduction_core138_stability_12q_v139_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    base = ncff
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f035_buyback_share_reduction_core139_stability_12q_v140_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    base = _log(sharesbas.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f035_buyback_share_reduction_core140_reduction_v141_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(sharesbas, 1).clip(upper=0).abs())
def cg_f035_buyback_share_reduction_core141_ncff_mcap_v142_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_safe_div(ncff, marketcap))
def cg_f035_buyback_share_reduction_core142_ncff_ncfo_v143_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_safe_div(ncff, ncfo.abs() + 1.0))
def cg_f035_buyback_share_reduction_core143_reduction_yoy_v144_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_pct_change(sharesbas, 4).clip(upper=0).abs())
def cg_f035_buyback_share_reduction_core144_ncff_assets_v145_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_safe_div(ncff, assets))
def cg_f035_buyback_share_reduction_core145_ncff_rev_v146_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_safe_div(ncff, revenue))
def cg_f035_buyback_share_reduction_core146_reduction_intensity_v147_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    reduction_value = _pct_change(sharesbas, 1).clip(upper=0).abs() * marketcap
    return _clean(_safe_div(reduction_value, ncfo.abs() + 1.0))
def cg_f035_buyback_share_reduction_core147_ncff_equity_v148_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_safe_div(ncff, equity.abs() + 1.0))
def cg_f035_buyback_share_reduction_core148_reduction_diff_v149_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_diff(sharesbas, 4).clip(upper=0).abs())
def cg_f035_buyback_share_reduction_core149_shares_log_v150_signal(sharesbas, ncff, marketcap, revenue, assets, ncfo, equity, opex):
    return _clean(_log(sharesbas.clip(lower=1.0)))
