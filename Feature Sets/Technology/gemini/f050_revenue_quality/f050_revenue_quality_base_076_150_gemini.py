import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f050_revenue_quality_core75_pct_4q_v076_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_safe_div(_diff(deferredrev, 4), revenue), 4))
def cg_f050_revenue_quality_core76_pct_4q_v077_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_safe_div(receivables, revenue) * 365, 4))
def cg_f050_revenue_quality_core77_pct_4q_v078_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_safe_div(deferredrev, revenue) * 365, 4))
def cg_f050_revenue_quality_core78_pct_4q_v079_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_pct_change(revenue, 4), 4))
def cg_f050_revenue_quality_core79_pct_4q_v080_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(_log(revenue.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f050_revenue_quality_core80_std_8q_v081_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_std(_safe_div(receivables, revenue), 8))
def cg_f050_revenue_quality_core81_std_8q_v082_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_std(_safe_div(deferredrev, revenue), 8))
def cg_f050_revenue_quality_core82_std_8q_v083_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_std(_pct_change(receivables, 4) - _pct_change(revenue, 4), 8))
def cg_f050_revenue_quality_core83_std_8q_v084_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_std(_pct_change(deferredrev, 4) - _pct_change(revenue, 4), 8))
def cg_f050_revenue_quality_core84_std_8q_v085_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_std(_safe_div(_diff(receivables, 4), revenue), 8))
def cg_f050_revenue_quality_core85_std_8q_v086_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_std(_safe_div(_diff(deferredrev, 4), revenue), 8))
def cg_f050_revenue_quality_core86_std_8q_v087_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_std(_safe_div(receivables, revenue) * 365, 8))
def cg_f050_revenue_quality_core87_std_8q_v088_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_std(_safe_div(deferredrev, revenue) * 365, 8))
def cg_f050_revenue_quality_core88_std_8q_v089_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_std(_pct_change(revenue, 4), 8))
def cg_f050_revenue_quality_core89_std_8q_v090_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_std(_log(revenue.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f050_revenue_quality_core90_log_v091_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_log(_safe_div(receivables, revenue).clip(lower=0.001)))
def cg_f050_revenue_quality_core91_log_v092_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_log(_safe_div(deferredrev, revenue).clip(lower=0.001)))
def cg_f050_revenue_quality_core92_log_v093_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_log((_pct_change(receivables, 4) - _pct_change(revenue, 4)).clip(lower=-0.9) + 1.1))
def cg_f050_revenue_quality_core93_log_v094_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_log((_pct_change(deferredrev, 4) - _pct_change(revenue, 4)).clip(lower=-0.9) + 1.1))
def cg_f050_revenue_quality_core94_log_v095_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_log(_safe_div(_diff(receivables, 4), revenue).clip(lower=-0.9) + 1.1))
def cg_f050_revenue_quality_core95_log_v096_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_log(_safe_div(_diff(deferredrev, 4), revenue).clip(lower=-0.9) + 1.1))
def cg_f050_revenue_quality_core96_log_v097_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_log((_safe_div(receivables, revenue) * 365).clip(lower=0.1)))
def cg_f050_revenue_quality_core97_log_v098_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_log((_safe_div(deferredrev, revenue) * 365).clip(lower=0.1)))
def cg_f050_revenue_quality_core98_log_v099_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_log(_pct_change(revenue, 4).clip(lower=-0.9) + 1.1))
def cg_f050_revenue_quality_core99_log_v100_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_log(revenue.clip(lower=1.0)))

# Block 100-109: diff 1q
def cg_f050_revenue_quality_core100_diff_1q_v101_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_diff(_safe_div(receivables, revenue), 1))
def cg_f050_revenue_quality_core101_diff_1q_v102_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_diff(_safe_div(deferredrev, revenue), 1))
def cg_f050_revenue_quality_core102_diff_1q_v103_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_diff(_pct_change(receivables, 4) - _pct_change(revenue, 4), 1))
def cg_f050_revenue_quality_core103_diff_1q_v104_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_diff(_pct_change(deferredrev, 4) - _pct_change(revenue, 4), 1))
def cg_f050_revenue_quality_core104_diff_1q_v105_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_diff(_safe_div(_diff(receivables, 4), revenue), 1))
def cg_f050_revenue_quality_core105_diff_1q_v106_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_diff(_safe_div(_diff(deferredrev, 4), revenue), 1))
def cg_f050_revenue_quality_core106_diff_1q_v107_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_diff(_safe_div(receivables, revenue) * 365, 1))
def cg_f050_revenue_quality_core107_diff_1q_v108_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_diff(_safe_div(deferredrev, revenue) * 365, 1))
def cg_f050_revenue_quality_core108_diff_1q_v109_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_diff(_pct_change(revenue, 4), 1))
def cg_f050_revenue_quality_core109_diff_1q_v110_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_diff(_log(revenue.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f050_revenue_quality_core110_slope_4q_v111_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_slope(_safe_div(receivables, revenue), 4))
def cg_f050_revenue_quality_core111_slope_4q_v112_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_slope(_safe_div(deferredrev, revenue), 4))
def cg_f050_revenue_quality_core112_slope_4q_v113_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_slope(_pct_change(receivables, 4) - _pct_change(revenue, 4), 4))
def cg_f050_revenue_quality_core113_slope_4q_v114_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_slope(_pct_change(deferredrev, 4) - _pct_change(revenue, 4), 4))
def cg_f050_revenue_quality_core114_slope_4q_v115_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_slope(_safe_div(_diff(receivables, 4), revenue), 4))
def cg_f050_revenue_quality_core115_slope_4q_v116_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_slope(_safe_div(_diff(deferredrev, 4), revenue), 4))
def cg_f050_revenue_quality_core116_slope_4q_v117_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_slope(_safe_div(receivables, revenue) * 365, 4))
def cg_f050_revenue_quality_core117_slope_4q_v118_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_slope(_safe_div(deferredrev, revenue) * 365, 4))
def cg_f050_revenue_quality_core118_slope_4q_v119_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_slope(_pct_change(revenue, 4), 4))
def cg_f050_revenue_quality_core119_slope_4q_v120_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_slope(_log(revenue.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f050_revenue_quality_core120_ewm_8q_v121_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_ewm(_safe_div(receivables, revenue), 8))
def cg_f050_revenue_quality_core121_ewm_8q_v122_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_ewm(_safe_div(deferredrev, revenue), 8))
def cg_f050_revenue_quality_core122_ewm_8q_v123_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_ewm(_pct_change(receivables, 4) - _pct_change(revenue, 4), 8))
def cg_f050_revenue_quality_core123_ewm_8q_v124_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_ewm(_pct_change(deferredrev, 4) - _pct_change(revenue, 4), 8))
def cg_f050_revenue_quality_core124_ewm_8q_v125_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_ewm(_safe_div(_diff(receivables, 4), revenue), 8))
def cg_f050_revenue_quality_core125_ewm_8q_v126_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_ewm(_safe_div(_diff(deferredrev, 4), revenue), 8))
def cg_f050_revenue_quality_core126_ewm_8q_v127_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_ewm(_safe_div(receivables, revenue) * 365, 8))
def cg_f050_revenue_quality_core127_ewm_8q_v128_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_ewm(_safe_div(deferredrev, revenue) * 365, 8))
def cg_f050_revenue_quality_core128_ewm_8q_v129_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_ewm(_pct_change(revenue, 4), 8))
def cg_f050_revenue_quality_core129_ewm_8q_v130_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_ewm(_log(revenue.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f050_revenue_quality_core130_stability_12q_v131_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    base = _safe_div(receivables, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f050_revenue_quality_core131_stability_12q_v132_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    base = _safe_div(deferredrev, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f050_revenue_quality_core132_stability_12q_v133_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    base = _pct_change(receivables, 4) - _pct_change(revenue, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f050_revenue_quality_core133_stability_12q_v134_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    base = _pct_change(deferredrev, 4) - _pct_change(revenue, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f050_revenue_quality_core134_stability_12q_v135_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    base = _safe_div(_diff(receivables, 4), revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f050_revenue_quality_core135_stability_12q_v136_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    base = _safe_div(_diff(deferredrev, 4), revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f050_revenue_quality_core136_stability_12q_v137_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    base = _safe_div(receivables, revenue) * 365
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f050_revenue_quality_core137_stability_12q_v138_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    base = _safe_div(deferredrev, revenue) * 365
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f050_revenue_quality_core138_stability_12q_v139_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    base = _pct_change(revenue, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f050_revenue_quality_core139_stability_12q_v140_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    base = _log(revenue.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f050_revenue_quality_core140_rec_rev_v141_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_safe_div(receivables, revenue))
def cg_f050_revenue_quality_core141_def_rev_v142_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_safe_div(deferredrev, revenue))
def cg_f050_revenue_quality_core142_rec_growth_spread_v143_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(receivables, 4) - _pct_change(revenue, 4))
def cg_f050_revenue_quality_core143_def_growth_spread_v144_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(deferredrev, 4) - _pct_change(revenue, 4))
def cg_f050_revenue_quality_core144_dso_proxy_v145_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_safe_div(receivables, revenue) * 365)
def cg_f050_revenue_quality_core145_dpo_proxy_v146_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_safe_div(deferredrev, revenue) * 365)
def cg_f050_revenue_quality_core146_rec_impact_v147_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_safe_div(_diff(receivables, 4), revenue))
def cg_f050_revenue_quality_core147_def_impact_v148_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_safe_div(_diff(deferredrev, 4), revenue))
def cg_f050_revenue_quality_core148_yoy_v149_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_pct_change(revenue, 4))
def cg_f050_revenue_quality_core149_log_v150_signal(revenue, receivables, deferredrev, assets, marketcap, opex, cor, equity):
    return _clean(_log(revenue.clip(lower=1.0)))
