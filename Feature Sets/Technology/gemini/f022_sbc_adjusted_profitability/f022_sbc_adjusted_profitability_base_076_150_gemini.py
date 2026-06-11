import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f022_sbc_adjusted_profitability_core75_pct_4q_v076_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_pct_change(_safe_div(sbc, ebitda.clip(lower=0) + 1.0), 4))
def cg_f022_sbc_adjusted_profitability_core76_pct_4q_v077_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_pct_change(_safe_div(sbc, netinc.abs() + 1.0), 4))
def cg_f022_sbc_adjusted_profitability_core77_pct_4q_v078_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_pct_change(_safe_div(sbc, fcf.abs() + 1.0), 4))
def cg_f022_sbc_adjusted_profitability_core78_pct_4q_v079_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_pct_change(_safe_div(opinc + sbc, assets), 4))
def cg_f022_sbc_adjusted_profitability_core79_pct_4q_v080_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_pct_change(_log((opinc + sbc).clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f022_sbc_adjusted_profitability_core80_std_8q_v081_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_std(_safe_div(opinc + sbc, revenue), 8))
def cg_f022_sbc_adjusted_profitability_core81_std_8q_v082_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_std(_safe_div(ebitda + sbc, revenue), 8))
def cg_f022_sbc_adjusted_profitability_core82_std_8q_v083_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_std(_safe_div(netinc + sbc, revenue), 8))
def cg_f022_sbc_adjusted_profitability_core83_std_8q_v084_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_std(_safe_div(fcf + sbc, revenue), 8))
def cg_f022_sbc_adjusted_profitability_core84_std_8q_v085_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_std(_safe_div(sbc, opinc.abs() + 1.0), 8))
def cg_f022_sbc_adjusted_profitability_core85_std_8q_v086_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_std(_safe_div(sbc, ebitda.clip(lower=0) + 1.0), 8))
def cg_f022_sbc_adjusted_profitability_core86_std_8q_v087_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_std(_safe_div(sbc, netinc.abs() + 1.0), 8))
def cg_f022_sbc_adjusted_profitability_core87_std_8q_v088_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_std(_safe_div(sbc, fcf.abs() + 1.0), 8))
def cg_f022_sbc_adjusted_profitability_core88_std_8q_v089_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_std(_safe_div(opinc + sbc, assets), 8))
def cg_f022_sbc_adjusted_profitability_core89_std_8q_v090_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_std(_log((opinc + sbc).clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f022_sbc_adjusted_profitability_core90_log_v091_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_log((opinc + sbc).clip(lower=1.0)))
def cg_f022_sbc_adjusted_profitability_core91_log_v092_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_log((ebitda + sbc).clip(lower=1.0)))
def cg_f022_sbc_adjusted_profitability_core92_log_v093_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_log((netinc + sbc).clip(lower=1.0)))
def cg_f022_sbc_adjusted_profitability_core93_log_v094_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_log((fcf + sbc).clip(lower=1.0)))
def cg_f022_sbc_adjusted_profitability_core94_log_v095_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_log(_safe_div(opinc + sbc, revenue).clip(lower=0.001)))
def cg_f022_sbc_adjusted_profitability_core95_log_v096_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_log(_safe_div(ebitda + sbc, revenue).clip(lower=0.001)))
def cg_f022_sbc_adjusted_profitability_core96_log_v097_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_log(_safe_div(sbc, opinc.abs() + 1.0).clip(lower=0.001)))
def cg_f022_sbc_adjusted_profitability_core97_log_v098_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_log(_safe_div(sbc, revenue).clip(lower=0.001)))
def cg_f022_sbc_adjusted_profitability_core98_log_v099_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_log(_safe_div(opinc + sbc, assets).clip(lower=0.001)))
def cg_f022_sbc_adjusted_profitability_core99_log_v100_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_log(_safe_div(sbc, sharesbas).clip(lower=0.001)))

# Block 100-109: diff 1q
def cg_f022_sbc_adjusted_profitability_core100_diff_1q_v101_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_diff(_safe_div(opinc + sbc, revenue), 1))
def cg_f022_sbc_adjusted_profitability_core101_diff_1q_v102_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_diff(_safe_div(ebitda + sbc, revenue), 1))
def cg_f022_sbc_adjusted_profitability_core102_diff_1q_v103_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_diff(_safe_div(netinc + sbc, revenue), 1))
def cg_f022_sbc_adjusted_profitability_core103_diff_1q_v104_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_diff(_safe_div(fcf + sbc, revenue), 1))
def cg_f022_sbc_adjusted_profitability_core104_diff_1q_v105_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_diff(_safe_div(sbc, opinc.abs() + 1.0), 1))
def cg_f022_sbc_adjusted_profitability_core105_diff_1q_v106_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_diff(_safe_div(sbc, ebitda.clip(lower=0) + 1.0), 1))
def cg_f022_sbc_adjusted_profitability_core106_diff_1q_v107_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_diff(_safe_div(sbc, netinc.abs() + 1.0), 1))
def cg_f022_sbc_adjusted_profitability_core107_diff_1q_v108_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_diff(_safe_div(sbc, fcf.abs() + 1.0), 1))
def cg_f022_sbc_adjusted_profitability_core108_diff_1q_v109_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_diff(_safe_div(opinc + sbc, assets), 1))
def cg_f022_sbc_adjusted_profitability_core109_diff_1q_v110_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_diff(_log((opinc + sbc).clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f022_sbc_adjusted_profitability_core110_slope_4q_v111_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_slope(_safe_div(opinc + sbc, revenue), 4))
def cg_f022_sbc_adjusted_profitability_core111_slope_4q_v112_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_slope(_safe_div(ebitda + sbc, revenue), 4))
def cg_f022_sbc_adjusted_profitability_core112_slope_4q_v113_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_slope(_safe_div(netinc + sbc, revenue), 4))
def cg_f022_sbc_adjusted_profitability_core113_slope_4q_v114_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_slope(_safe_div(fcf + sbc, revenue), 4))
def cg_f022_sbc_adjusted_profitability_core114_slope_4q_v115_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_slope(_safe_div(sbc, opinc.abs() + 1.0), 4))
def cg_f022_sbc_adjusted_profitability_core115_slope_4q_v116_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_slope(_safe_div(sbc, ebitda.clip(lower=0) + 1.0), 4))
def cg_f022_sbc_adjusted_profitability_core116_slope_4q_v117_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_slope(_safe_div(sbc, netinc.abs() + 1.0), 4))
def cg_f022_sbc_adjusted_profitability_core117_slope_4q_v118_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_slope(_safe_div(sbc, fcf.abs() + 1.0), 4))
def cg_f022_sbc_adjusted_profitability_core118_slope_4q_v119_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_slope(_safe_div(opinc + sbc, assets), 4))
def cg_f022_sbc_adjusted_profitability_core119_slope_4q_v120_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_slope(_log((opinc + sbc).clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f022_sbc_adjusted_profitability_core120_ewm_8q_v121_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_ewm(_safe_div(opinc + sbc, revenue), 8))
def cg_f022_sbc_adjusted_profitability_core121_ewm_8q_v122_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_ewm(_safe_div(ebitda + sbc, revenue), 8))
def cg_f022_sbc_adjusted_profitability_core122_ewm_8q_v123_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_ewm(_safe_div(netinc + sbc, revenue), 8))
def cg_f022_sbc_adjusted_profitability_core123_ewm_8q_v124_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_ewm(_safe_div(fcf + sbc, revenue), 8))
def cg_f022_sbc_adjusted_profitability_core124_ewm_8q_v125_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_ewm(_safe_div(sbc, opinc.abs() + 1.0), 8))
def cg_f022_sbc_adjusted_profitability_core125_ewm_8q_v126_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_ewm(_safe_div(sbc, ebitda.clip(lower=0) + 1.0), 8))
def cg_f022_sbc_adjusted_profitability_core126_ewm_8q_v127_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_ewm(_safe_div(sbc, netinc.abs() + 1.0), 8))
def cg_f022_sbc_adjusted_profitability_core127_ewm_8q_v128_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_ewm(_safe_div(sbc, fcf.abs() + 1.0), 8))
def cg_f022_sbc_adjusted_profitability_core128_ewm_8q_v129_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_ewm(_safe_div(opinc + sbc, assets), 8))
def cg_f022_sbc_adjusted_profitability_core129_ewm_8q_v130_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_ewm(_log((opinc + sbc).clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f022_sbc_adjusted_profitability_core130_stability_12q_v131_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    base = _safe_div(opinc + sbc, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f022_sbc_adjusted_profitability_core131_stability_12q_v132_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    base = _safe_div(ebitda + sbc, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f022_sbc_adjusted_profitability_core132_stability_12q_v133_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    base = _safe_div(netinc + sbc, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f022_sbc_adjusted_profitability_core133_stability_12q_v134_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    base = _safe_div(fcf + sbc, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f022_sbc_adjusted_profitability_core134_stability_12q_v135_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    base = _safe_div(sbc, opinc.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f022_sbc_adjusted_profitability_core135_stability_12q_v136_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    base = _safe_div(sbc, ebitda.clip(lower=0) + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f022_sbc_adjusted_profitability_core136_stability_12q_v137_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    base = _safe_div(sbc, netinc.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f022_sbc_adjusted_profitability_core137_stability_12q_v138_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    base = _safe_div(sbc, fcf.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f022_sbc_adjusted_profitability_core138_stability_12q_v139_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    base = _safe_div(opinc + sbc, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f022_sbc_adjusted_profitability_core139_stability_12q_v140_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    base = _log((opinc + sbc).clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f022_sbc_adjusted_profitability_core140_adj_op_v141_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_safe_div(opinc + sbc, revenue))
def cg_f022_sbc_adjusted_profitability_core141_adj_ebitda_v142_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_safe_div(ebitda + sbc, revenue))
def cg_f022_sbc_adjusted_profitability_core142_adj_net_v143_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_safe_div(netinc + sbc, revenue))
def cg_f022_sbc_adjusted_profitability_core143_adj_fcf_v144_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_safe_div(fcf + sbc, revenue))
def cg_f022_sbc_adjusted_profitability_core144_sbc_drag_v145_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_safe_div(sbc, opinc.abs() + 1.0))
def cg_f022_sbc_adjusted_profitability_core145_sbc_ebitda_drag_v146_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_safe_div(sbc, ebitda.clip(lower=0) + 1.0))
def cg_f022_sbc_adjusted_profitability_core146_sbc_ni_drag_v147_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_safe_div(sbc, netinc.abs() + 1.0))
def cg_f022_sbc_adjusted_profitability_core147_sbc_fcf_drag_v148_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_safe_div(sbc, fcf.abs() + 1.0))
def cg_f022_sbc_adjusted_profitability_core148_adj_roa_v149_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_safe_div(opinc + sbc, assets))
def cg_f022_sbc_adjusted_profitability_core149_adj_op_log_v150_signal(sbc, opinc, revenue, ebitda, netinc, fcf, assets, marketcap, opex, sharesbas):
    return _clean(_log((opinc + sbc).clip(lower=1.0)))
