import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f028_retained_earnings_trajectory_core75_pct_4q_v076_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(retainedearnings, debtt.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core76_pct_4q_v077_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(retainedearnings, sharesbas), 4))
def cg_f028_retained_earnings_trajectory_core77_pct_4q_v078_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(retainedearnings, opex.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core78_pct_4q_v079_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_safe_div(_diff(retainedearnings, 4), netinc.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core79_pct_4q_v080_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_pct_change(_log(retainedearnings.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f028_retained_earnings_trajectory_core80_std_8q_v081_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_std(_safe_div(retainedearnings, assets), 8))
def cg_f028_retained_earnings_trajectory_core81_std_8q_v082_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_std(_safe_div(retainedearnings, equity.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core82_std_8q_v083_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_std(_safe_div(retainedearnings, marketcap), 8))
def cg_f028_retained_earnings_trajectory_core83_std_8q_v084_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_std(_safe_div(retainedearnings, revenue), 8))
def cg_f028_retained_earnings_trajectory_core85_std_8q_v086_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_std(_safe_div(retainedearnings, debtt.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core86_std_8q_v087_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_std(_safe_div(retainedearnings, sharesbas), 8))
def cg_f028_retained_earnings_trajectory_core87_std_8q_v088_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_std(_safe_div(retainedearnings, opex.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core88_std_8q_v089_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_std(retainedearnings, 8))
def cg_f028_retained_earnings_trajectory_core89_std_8q_v090_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_std(_log(retainedearnings.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f028_retained_earnings_trajectory_core90_log_v091_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_log(retainedearnings.clip(lower=1.0)))
def cg_f028_retained_earnings_trajectory_core91_log_v092_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_log(_safe_div(retainedearnings, assets).clip(lower=0.001)))
def cg_f028_retained_earnings_trajectory_core92_log_v093_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_log(_safe_div(retainedearnings, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f028_retained_earnings_trajectory_core93_log_v094_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_log(_safe_div(retainedearnings, marketcap).clip(lower=0.001)))
def cg_f028_retained_earnings_trajectory_core94_log_v095_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_log(_safe_div(retainedearnings, revenue).clip(lower=0.001)))
def cg_f028_retained_earnings_trajectory_core95_log_v096_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_log(_safe_div(retainedearnings, debtt.abs() + 1.0).clip(lower=0.001)))
def cg_f028_retained_earnings_trajectory_core96_log_v097_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_log(_safe_div(retainedearnings, sharesbas).clip(lower=0.001)))
def cg_f028_retained_earnings_trajectory_core97_log_v098_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_log(_safe_div(retainedearnings, opex.abs() + 1.0).clip(lower=0.001)))
def cg_f028_retained_earnings_trajectory_core98_log_v099_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_log(_safe_div(_diff(retainedearnings, 4), netinc.abs() + 1.0).clip(lower=0.001)))
def cg_f028_retained_earnings_trajectory_core99_log_v100_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_log(assets.clip(lower=1.0)))

# Block 100-109: diff 1q
def cg_f028_retained_earnings_trajectory_core100_diff_1q_v101_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_diff(_safe_div(retainedearnings, assets), 1))
def cg_f028_retained_earnings_trajectory_core101_diff_1q_v102_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_diff(_safe_div(retainedearnings, equity.abs() + 1.0), 1))
def cg_f028_retained_earnings_trajectory_core102_diff_1q_v103_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_diff(_safe_div(retainedearnings, marketcap), 1))
def cg_f028_retained_earnings_trajectory_core103_diff_1q_v104_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_diff(_safe_div(retainedearnings, revenue), 1))
def cg_f028_retained_earnings_trajectory_core104_diff_1q_v105_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_diff(_safe_div(retainedearnings, debtt.abs() + 1.0), 1))
def cg_f028_retained_earnings_trajectory_core105_diff_1q_v106_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_diff(_safe_div(retainedearnings, sharesbas), 1))
def cg_f028_retained_earnings_trajectory_core106_diff_1q_v107_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_diff(_safe_div(retainedearnings, opex.abs() + 1.0), 1))
def cg_f028_retained_earnings_trajectory_core107_diff_1q_v108_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_diff(retainedearnings, 1))
def cg_f028_retained_earnings_trajectory_core108_diff_1q_v109_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_diff(_log(retainedearnings.clip(lower=1.0)), 1))
def cg_f028_retained_earnings_trajectory_core109_diff_1q_v110_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_diff(_safe_div(_diff(retainedearnings, 4), netinc.abs() + 1.0), 1))

# Block 110-119: slope 4q
def cg_f028_retained_earnings_trajectory_core110_slope_4q_v111_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_slope(_safe_div(retainedearnings, assets), 4))
def cg_f028_retained_earnings_trajectory_core111_slope_4q_v112_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_slope(_safe_div(retainedearnings, equity.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core112_slope_4q_v113_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_slope(_safe_div(retainedearnings, marketcap), 4))
def cg_f028_retained_earnings_trajectory_core113_slope_4q_v114_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_slope(_safe_div(retainedearnings, revenue), 4))
def cg_f028_retained_earnings_trajectory_core114_slope_4q_v115_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_slope(_safe_div(retainedearnings, debtt.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core115_slope_4q_v116_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_slope(_safe_div(retainedearnings, sharesbas), 4))
def cg_f028_retained_earnings_trajectory_core116_slope_4q_v117_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_slope(_safe_div(retainedearnings, opex.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core117_slope_4q_v118_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_slope(retainedearnings, 4))
def cg_f028_retained_earnings_trajectory_core118_slope_4q_v119_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_slope(_log(retainedearnings.clip(lower=1.0)), 4))
def cg_f028_retained_earnings_trajectory_core119_slope_4q_v120_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_slope(_safe_div(_diff(retainedearnings, 4), netinc.abs() + 1.0), 4))

# Block 120-129: ewm 8q
def cg_f028_retained_earnings_trajectory_core120_ewm_8q_v121_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_ewm(_safe_div(retainedearnings, assets), 8))
def cg_f028_retained_earnings_trajectory_core121_ewm_8q_v122_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_ewm(_safe_div(retainedearnings, equity.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core122_ewm_8q_v123_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_ewm(_safe_div(retainedearnings, marketcap), 8))
def cg_f028_retained_earnings_trajectory_core123_ewm_8q_v124_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_ewm(_safe_div(retainedearnings, revenue), 8))
def cg_f028_retained_earnings_trajectory_core124_ewm_8q_v125_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_ewm(_safe_div(retainedearnings, debtt.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core125_ewm_8q_v126_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_ewm(_safe_div(retainedearnings, sharesbas), 8))
def cg_f028_retained_earnings_trajectory_core126_ewm_8q_v127_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_ewm(_safe_div(retainedearnings, opex.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core127_ewm_8q_v128_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_ewm(retainedearnings, 8))
def cg_f028_retained_earnings_trajectory_core128_ewm_8q_v129_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_ewm(_log(retainedearnings.clip(lower=1.0)), 8))
def cg_f028_retained_earnings_trajectory_core129_ewm_8q_v130_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_ewm(_safe_div(_diff(retainedearnings, 4), netinc.abs() + 1.0), 8))

# Block 130-139: stability 12q
def cg_f028_retained_earnings_trajectory_core130_stability_12q_v131_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    base = _safe_div(retainedearnings, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f028_retained_earnings_trajectory_core131_stability_12q_v132_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    base = _safe_div(retainedearnings, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f028_retained_earnings_trajectory_core132_stability_12q_v133_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    base = _safe_div(retainedearnings, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f028_retained_earnings_trajectory_core133_stability_12q_v134_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    base = _safe_div(retainedearnings, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f028_retained_earnings_trajectory_core134_stability_12q_v135_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    base = _safe_div(retainedearnings, debtt.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f028_retained_earnings_trajectory_core135_stability_12q_v136_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    base = _safe_div(retainedearnings, sharesbas)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f028_retained_earnings_trajectory_core136_stability_12q_v137_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    base = _safe_div(retainedearnings, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f028_retained_earnings_trajectory_core137_stability_12q_v138_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    base = retainedearnings
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f028_retained_earnings_trajectory_core138_stability_12q_v139_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    base = _log(retainedearnings.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f028_retained_earnings_trajectory_core139_stability_12q_v140_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    base = _safe_div(_diff(retainedearnings, 4), netinc.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f028_retained_earnings_trajectory_core140_re_v141_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(retainedearnings)
def cg_f028_retained_earnings_trajectory_core141_re_assets_v142_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_safe_div(retainedearnings, assets))
def cg_f028_retained_earnings_trajectory_core142_re_equity_v143_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_safe_div(retainedearnings, equity.abs() + 1.0))
def cg_f028_retained_earnings_trajectory_core143_re_mcap_v144_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_safe_div(retainedearnings, marketcap))
def cg_f028_retained_earnings_trajectory_core144_re_rev_v145_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_safe_div(retainedearnings, revenue))
def cg_f028_retained_earnings_trajectory_core145_re_debt_v146_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_safe_div(retainedearnings, debtt.abs() + 1.0))
def cg_f028_retained_earnings_trajectory_core146_re_shares_v147_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_safe_div(retainedearnings, sharesbas))
def cg_f028_retained_earnings_trajectory_core147_re_opex_v148_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_safe_div(retainedearnings, opex.abs() + 1.0))
def cg_f028_retained_earnings_trajectory_core148_retention_v149_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_safe_div(_diff(retainedearnings, 4), netinc.abs() + 1.0))
def cg_f028_retained_earnings_trajectory_core149_re_log_v150_signal(retainedearnings, assets, equity, marketcap, netinc, revenue, debtt, sharesbas, opex):
    return _clean(_log(retainedearnings.clip(lower=1.0)))

def cg_f028_retained_earnings_trajectory_retearn_to_asset_z_126d_base_v085_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

