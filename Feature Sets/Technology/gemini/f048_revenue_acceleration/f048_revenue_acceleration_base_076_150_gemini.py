import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f048_revenue_acceleration_core75_pct_4q_v076_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_assets = _diff(_pct_change(assets, 4), 1)
    return _clean(_pct_change(accel - accel_assets, 4))
def cg_f048_revenue_acceleration_core76_pct_4q_v077_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_opex = _diff(_pct_change(opex, 4), 1)
    return _clean(_pct_change(accel - accel_opex, 4))
def cg_f048_revenue_acceleration_core77_pct_4q_v078_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_diff(_pct_change(revenue, 4), 1), 1), 4))
def cg_f048_revenue_acceleration_core78_pct_4q_v079_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_diff(_pct_change(revenue, 4), 4), 4), 4))
def cg_f048_revenue_acceleration_core79_pct_4q_v080_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_z(_diff(_pct_change(revenue, 4), 1), 12), 4))

# core80-89: std 8q
def cg_f048_revenue_acceleration_core80_std_8q_v081_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_diff(_pct_change(revenue, 4), 1), 8))
def cg_f048_revenue_acceleration_core81_std_8q_v082_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_diff(_pct_change(revenue, 4), 4), 8))
def cg_f048_revenue_acceleration_core82_std_8q_v083_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_diff(_pct_change(revenue, 1), 1), 8))
def cg_f048_revenue_acceleration_core83_std_8q_v084_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_diff(_pct_change(_safe_div(revenue, assets), 4), 1), 8))
def cg_f048_revenue_acceleration_core84_std_8q_v085_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1), 8))
def cg_f048_revenue_acceleration_core85_std_8q_v086_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_assets = _diff(_pct_change(assets, 4), 1)
    return _clean(_std(accel - accel_assets, 8))
def cg_f048_revenue_acceleration_core86_std_8q_v087_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_opex = _diff(_pct_change(opex, 4), 1)
    return _clean(_std(accel - accel_opex, 8))
def cg_f048_revenue_acceleration_core87_std_8q_v088_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_diff(_diff(_pct_change(revenue, 4), 1), 1), 8))
def cg_f048_revenue_acceleration_core88_std_8q_v089_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_diff(_diff(_pct_change(revenue, 4), 4), 4), 8))
def cg_f048_revenue_acceleration_core89_std_8q_v090_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_z(_diff(_pct_change(revenue, 4), 1), 12), 8))

# core90-99: log (proxied by log of absolute change + 1)
def cg_f048_revenue_acceleration_core90_log_v091_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_pct_change(revenue, 4), 1)
    return _clean(_log(base.abs() + 1.0))
def cg_f048_revenue_acceleration_core91_log_v092_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_pct_change(revenue, 4), 4)
    return _clean(_log(base.abs() + 1.0))
def cg_f048_revenue_acceleration_core92_log_v093_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_pct_change(revenue, 1), 1)
    return _clean(_log(base.abs() + 1.0))
def cg_f048_revenue_acceleration_core93_log_v094_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_pct_change(_safe_div(revenue, assets), 4), 1)
    return _clean(_log(base.abs() + 1.0))
def cg_f048_revenue_acceleration_core94_log_v095_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1)
    return _clean(_log(base.abs() + 1.0))
def cg_f048_revenue_acceleration_core95_log_v096_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_assets = _diff(_pct_change(assets, 4), 1)
    return _clean(_log((accel - accel_assets).abs() + 1.0))
def cg_f048_revenue_acceleration_core96_log_v097_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_opex = _diff(_pct_change(opex, 4), 1)
    return _clean(_log((accel - accel_opex).abs() + 1.0))
def cg_f048_revenue_acceleration_core97_log_v098_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_diff(_pct_change(revenue, 4), 1), 1)
    return _clean(_log(base.abs() + 1.0))
def cg_f048_revenue_acceleration_core98_log_v099_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_diff(_pct_change(revenue, 4), 4), 4)
    return _clean(_log(base.abs() + 1.0))
def cg_f048_revenue_acceleration_core99_log_v100_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _z(_diff(_pct_change(revenue, 4), 1), 12)
    return _clean(_log(base.abs() + 1.0))

# core100-109: diff 1q
def cg_f048_revenue_acceleration_core100_diff_1q_v101_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_diff(_pct_change(revenue, 4), 1), 1))
def cg_f048_revenue_acceleration_core101_diff_1q_v102_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_diff(_pct_change(revenue, 4), 4), 1))
def cg_f048_revenue_acceleration_core102_diff_1q_v103_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_diff(_pct_change(revenue, 1), 1), 1))
def cg_f048_revenue_acceleration_core103_diff_1q_v104_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_diff(_pct_change(_safe_div(revenue, assets), 4), 1), 1))
def cg_f048_revenue_acceleration_core104_diff_1q_v105_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1), 1))
def cg_f048_revenue_acceleration_core105_diff_1q_v106_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_assets = _diff(_pct_change(assets, 4), 1)
    return _clean(_diff(accel - accel_assets, 1))
def cg_f048_revenue_acceleration_core106_diff_1q_v107_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_opex = _diff(_pct_change(opex, 4), 1)
    return _clean(_diff(accel - accel_opex, 1))
def cg_f048_revenue_acceleration_core107_diff_1q_v108_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_diff(_diff(_pct_change(revenue, 4), 1), 1), 1))
def cg_f048_revenue_acceleration_core108_diff_1q_v109_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_diff(_diff(_pct_change(revenue, 4), 4), 4), 1))
def cg_f048_revenue_acceleration_core109_diff_1q_v110_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_z(_diff(_pct_change(revenue, 4), 1), 12), 1))

# core110-119: slope 4q
def cg_f048_revenue_acceleration_core110_slope_4q_v111_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_diff(_pct_change(revenue, 4), 1), 4))
def cg_f048_revenue_acceleration_core111_slope_4q_v112_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_diff(_pct_change(revenue, 4), 4), 4))
def cg_f048_revenue_acceleration_core112_slope_4q_v113_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_diff(_pct_change(revenue, 1), 1), 4))
def cg_f048_revenue_acceleration_core113_slope_4q_v114_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_diff(_pct_change(_safe_div(revenue, assets), 4), 1), 4))
def cg_f048_revenue_acceleration_core114_slope_4q_v115_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1), 4))
def cg_f048_revenue_acceleration_core115_slope_4q_v116_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_assets = _diff(_pct_change(assets, 4), 1)
    return _clean(_slope(accel - accel_assets, 4))
def cg_f048_revenue_acceleration_core116_slope_4q_v117_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_opex = _diff(_pct_change(opex, 4), 1)
    return _clean(_slope(accel - accel_opex, 4))
def cg_f048_revenue_acceleration_core117_slope_4q_v118_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_diff(_diff(_pct_change(revenue, 4), 1), 1), 4))
def cg_f048_revenue_acceleration_core118_slope_4q_v119_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_diff(_diff(_pct_change(revenue, 4), 4), 4), 4))
def cg_f048_revenue_acceleration_core119_slope_4q_v120_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_z(_diff(_pct_change(revenue, 4), 1), 12), 4))

# core120-129: ewm 8q
def cg_f048_revenue_acceleration_core120_ewm_8q_v121_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_diff(_pct_change(revenue, 4), 1), 8))
def cg_f048_revenue_acceleration_core121_ewm_8q_v122_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_diff(_pct_change(revenue, 4), 4), 8))
def cg_f048_revenue_acceleration_core122_ewm_8q_v123_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_diff(_pct_change(revenue, 1), 1), 8))
def cg_f048_revenue_acceleration_core123_ewm_8q_v124_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_diff(_pct_change(_safe_div(revenue, assets), 4), 1), 8))
def cg_f048_revenue_acceleration_core124_ewm_8q_v125_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1), 8))
def cg_f048_revenue_acceleration_core125_ewm_8q_v126_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_assets = _diff(_pct_change(assets, 4), 1)
    return _clean(_ewm(accel - accel_assets, 8))
def cg_f048_revenue_acceleration_core126_ewm_8q_v127_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_opex = _diff(_pct_change(opex, 4), 1)
    return _clean(_ewm(accel - accel_opex, 8))
def cg_f048_revenue_acceleration_core127_ewm_8q_v128_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_diff(_diff(_pct_change(revenue, 4), 1), 1), 8))
def cg_f048_revenue_acceleration_core128_ewm_8q_v129_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_diff(_diff(_pct_change(revenue, 4), 4), 4), 8))
def cg_f048_revenue_acceleration_core129_ewm_8q_v130_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_z(_diff(_pct_change(revenue, 4), 1), 12), 8))

# core130-139: stability 12q
def cg_f048_revenue_acceleration_core130_stability_12q_v131_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_pct_change(revenue, 4), 1)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f048_revenue_acceleration_core131_stability_12q_v132_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_pct_change(revenue, 4), 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f048_revenue_acceleration_core132_stability_12q_v133_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_pct_change(revenue, 1), 1)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f048_revenue_acceleration_core133_stability_12q_v134_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_pct_change(_safe_div(revenue, assets), 4), 1)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f048_revenue_acceleration_core134_stability_12q_v135_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f048_revenue_acceleration_core135_stability_12q_v136_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_assets = _diff(_pct_change(assets, 4), 1)
    base = accel - accel_assets
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f048_revenue_acceleration_core136_stability_12q_v137_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_opex = _diff(_pct_change(opex, 4), 1)
    base = accel - accel_opex
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f048_revenue_acceleration_core137_stability_12q_v138_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_diff(_pct_change(revenue, 4), 1), 1)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f048_revenue_acceleration_core138_stability_12q_v139_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_diff(_pct_change(revenue, 4), 4), 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f048_revenue_acceleration_core139_stability_12q_v140_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _z(_diff(_pct_change(revenue, 4), 1), 12)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# core140-149: raw levels
def cg_f048_revenue_acceleration_core140_accel_v141_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_pct_change(revenue, 4), 1))
def cg_f048_revenue_acceleration_core141_accel_yoy_v142_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_pct_change(revenue, 4), 4))
def cg_f048_revenue_acceleration_core142_accel_qoq_v143_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_pct_change(revenue, 1), 1))
def cg_f048_revenue_acceleration_core143_accel_assets_v144_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_pct_change(_safe_div(revenue, assets), 4), 1))
def cg_f048_revenue_acceleration_core144_accel_opex_v145_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1))
def cg_f048_revenue_acceleration_core145_accel_spread_assets_v146_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_assets = _diff(_pct_change(assets, 4), 1)
    return _clean(accel - accel_assets)
def cg_f048_revenue_acceleration_core146_accel_spread_opex_v147_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    accel = _diff(_pct_change(revenue, 4), 1)
    accel_opex = _diff(_pct_change(opex, 4), 1)
    return _clean(accel - accel_opex)
def cg_f048_revenue_acceleration_core147_accel_2nd_deriv_v148_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_diff(_pct_change(revenue, 4), 1), 1))
def cg_f048_revenue_acceleration_core148_accel_log_v149_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_pct_change(revenue, 4), 1)
    return _clean(_log(base.abs() + 1.0))
def cg_f048_revenue_acceleration_core149_accel_z_v150_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_pct_change(revenue, 4), 1), 12))
