import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f047_revenue_growth_core75_pct_4q_v076_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_pct_change(revenue, 4) - _pct_change(opex, 4), 4))
def cg_f047_revenue_growth_core76_pct_4q_v077_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_pct_change(revenue, 4), 1), 4))
def cg_f047_revenue_growth_core77_pct_4q_v078_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_pct_change(revenue, 4), 4), 4))
def cg_f047_revenue_growth_core78_pct_4q_v079_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_log(revenue.clip(lower=1.0)), 4), 4))
def cg_f047_revenue_growth_core79_pct_4q_v080_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_z(_pct_change(revenue, 4), 12), 4))

# Block 80-89: std 8q
def cg_f047_revenue_growth_core80_std_8q_v081_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_pct_change(revenue, 4), 8))
def cg_f047_revenue_growth_core81_std_8q_v082_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_pct_change(revenue, 1), 8))
def cg_f047_revenue_growth_core82_std_8q_v083_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_pct_change(_safe_div(revenue, assets), 4), 8))
def cg_f047_revenue_growth_core83_std_8q_v084_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 8))
def cg_f047_revenue_growth_core84_std_8q_v085_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_pct_change(revenue, 4) - _pct_change(assets, 4), 8))
def cg_f047_revenue_growth_core85_std_8q_v086_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_pct_change(revenue, 4) - _pct_change(opex, 4), 8))
def cg_f047_revenue_growth_core86_std_8q_v087_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_diff(_pct_change(revenue, 4), 1), 8))
def cg_f047_revenue_growth_core87_std_8q_v088_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_diff(_pct_change(revenue, 4), 4), 8))
def cg_f047_revenue_growth_core88_std_8q_v089_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_diff(_log(revenue.clip(lower=1.0)), 4), 8))
def cg_f047_revenue_growth_core89_std_8q_v090_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_std(_z(_pct_change(revenue, 4), 12), 8))

# Block 90-99: log
def cg_f047_revenue_growth_core90_log_v091_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_log(_pct_change(revenue, 4).clip(lower=-0.9) + 1.1))
def cg_f047_revenue_growth_core91_log_v092_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_log(_pct_change(revenue, 1).clip(lower=-0.9) + 1.1))
def cg_f047_revenue_growth_core92_log_v093_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_log(_pct_change(_safe_div(revenue, assets), 4).clip(lower=-0.9) + 1.1))
def cg_f047_revenue_growth_core93_log_v094_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_log(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4).clip(lower=-0.9) + 1.1))
def cg_f047_revenue_growth_core94_log_v095_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_log((_pct_change(revenue, 4) - _pct_change(assets, 4)).clip(lower=-0.9) + 1.1))
def cg_f047_revenue_growth_core95_log_v096_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_log((_pct_change(revenue, 4) - _pct_change(opex, 4)).clip(lower=-0.9) + 1.1))
def cg_f047_revenue_growth_core96_log_v097_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_log(_diff(_pct_change(revenue, 4), 1).clip(lower=-0.9) + 1.1))
def cg_f047_revenue_growth_core97_log_v098_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_log(_diff(_pct_change(revenue, 4), 4).clip(lower=-0.9) + 1.1))
def cg_f047_revenue_growth_core98_log_v099_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_log(_diff(_log(revenue.clip(lower=1.0)), 4).clip(lower=-0.9) + 1.1))
def cg_f047_revenue_growth_core99_log_v100_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_log(_z(_pct_change(revenue, 4), 12).clip(lower=-0.9) + 1.1))

# Block 100-109: diff 1q
def cg_f047_revenue_growth_core100_diff_1q_v101_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_pct_change(revenue, 4), 1))
def cg_f047_revenue_growth_core101_diff_1q_v102_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_pct_change(revenue, 1), 1))
def cg_f047_revenue_growth_core102_diff_1q_v103_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_pct_change(_safe_div(revenue, assets), 4), 1))
def cg_f047_revenue_growth_core103_diff_1q_v104_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1))
def cg_f047_revenue_growth_core104_diff_1q_v105_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_pct_change(revenue, 4) - _pct_change(assets, 4), 1))
def cg_f047_revenue_growth_core105_diff_1q_v106_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_pct_change(revenue, 4) - _pct_change(opex, 4), 1))
def cg_f047_revenue_growth_core106_diff_1q_v107_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_diff(_pct_change(revenue, 4), 1), 1))
def cg_f047_revenue_growth_core107_diff_1q_v108_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_diff(_pct_change(revenue, 4), 4), 1))
def cg_f047_revenue_growth_core108_diff_1q_v109_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_diff(_log(revenue.clip(lower=1.0)), 4), 1))
def cg_f047_revenue_growth_core109_diff_1q_v110_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_z(_pct_change(revenue, 4), 12), 1))

# Block 110-119: slope 4q
def cg_f047_revenue_growth_core110_slope_4q_v111_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_pct_change(revenue, 4), 4))
def cg_f047_revenue_growth_core111_slope_4q_v112_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_pct_change(revenue, 1), 4))
def cg_f047_revenue_growth_core112_slope_4q_v113_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_pct_change(_safe_div(revenue, assets), 4), 4))
def cg_f047_revenue_growth_core113_slope_4q_v114_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 4))
def cg_f047_revenue_growth_core114_slope_4q_v115_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_pct_change(revenue, 4) - _pct_change(assets, 4), 4))
def cg_f047_revenue_growth_core115_slope_4q_v116_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_pct_change(revenue, 4) - _pct_change(opex, 4), 4))
def cg_f047_revenue_growth_core116_slope_4q_v117_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_diff(_pct_change(revenue, 4), 1), 4))
def cg_f047_revenue_growth_core117_slope_4q_v118_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_diff(_pct_change(revenue, 4), 4), 4))
def cg_f047_revenue_growth_core118_slope_4q_v119_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_diff(_log(revenue.clip(lower=1.0)), 4), 4))
def cg_f047_revenue_growth_core119_slope_4q_v120_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_slope(_z(_pct_change(revenue, 4), 12), 4))

# Block 120-129: ewm 8q
def cg_f047_revenue_growth_core120_ewm_8q_v121_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_pct_change(revenue, 4), 8))
def cg_f047_revenue_growth_core121_ewm_8q_v122_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_pct_change(revenue, 1), 8))
def cg_f047_revenue_growth_core122_ewm_8q_v123_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_pct_change(_safe_div(revenue, assets), 4), 8))
def cg_f047_revenue_growth_core123_ewm_8q_v124_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 8))
def cg_f047_revenue_growth_core124_ewm_8q_v125_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_pct_change(revenue, 4) - _pct_change(assets, 4), 8))
def cg_f047_revenue_growth_core125_ewm_8q_v126_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_pct_change(revenue, 4) - _pct_change(opex, 4), 8))
def cg_f047_revenue_growth_core126_ewm_8q_v127_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_diff(_pct_change(revenue, 4), 1), 8))
def cg_f047_revenue_growth_core127_ewm_8q_v128_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_diff(_pct_change(revenue, 4), 4), 8))
def cg_f047_revenue_growth_core128_ewm_8q_v129_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_diff(_log(revenue.clip(lower=1.0)), 4), 8))
def cg_f047_revenue_growth_core129_ewm_8q_v130_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_ewm(_z(_pct_change(revenue, 4), 12), 8))

# Block 130-139: stability 12q
def cg_f047_revenue_growth_core130_stability_12q_v131_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _pct_change(revenue, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f047_revenue_growth_core131_stability_12q_v132_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _pct_change(revenue, 1)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f047_revenue_growth_core132_stability_12q_v133_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _pct_change(_safe_div(revenue, assets), 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f047_revenue_growth_core133_stability_12q_v134_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _pct_change(_safe_div(revenue, opex.abs() + 1.0), 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f047_revenue_growth_core134_stability_12q_v135_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _pct_change(revenue, 4) - _pct_change(assets, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f047_revenue_growth_core135_stability_12q_v136_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _pct_change(revenue, 4) - _pct_change(opex, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f047_revenue_growth_core136_stability_12q_v137_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_pct_change(revenue, 4), 1)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f047_revenue_growth_core137_stability_12q_v138_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_pct_change(revenue, 4), 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f047_revenue_growth_core138_stability_12q_v139_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _diff(_log(revenue.clip(lower=1.0)), 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f047_revenue_growth_core139_stability_12q_v140_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    base = _z(_pct_change(revenue, 4), 12)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f047_revenue_growth_core140_yoy_v141_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(revenue, 4))
def cg_f047_revenue_growth_core141_qoq_v142_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(revenue, 1))
def cg_f047_revenue_growth_core142_assets_yoy_v143_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_safe_div(revenue, assets), 4))
def cg_f047_revenue_growth_core143_opex_yoy_v144_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4))
def cg_f047_revenue_growth_core144_spread_assets_v145_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(revenue, 4) - _pct_change(assets, 4))
def cg_f047_revenue_growth_core145_spread_opex_v146_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(revenue, 4) - _pct_change(opex, 4))
def cg_f047_revenue_growth_core146_accel_qoq_v147_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_pct_change(revenue, 4), 1))
def cg_f047_revenue_growth_core147_accel_yoy_v148_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_pct_change(revenue, 4), 4))
def cg_f047_revenue_growth_core148_logdiff_yoy_v149_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_diff(_log(revenue.clip(lower=1.0)), 4))
def cg_f047_revenue_growth_core149_z_yoy_v150_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_pct_change(revenue, 4), 12))
