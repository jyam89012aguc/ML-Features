import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f021_stock_based_compensation_core75_pct_4q_v076_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, sharesbas), 4))
def cg_f021_stock_based_compensation_core76_pct_4q_v077_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, fcf.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core77_pct_4q_v078_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, rnd.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core78_pct_4q_v079_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_safe_div(sbc, assets), 4))
def cg_f021_stock_based_compensation_core79_pct_4q_v080_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_pct_change(_log(sbc.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f021_stock_based_compensation_core80_std_8q_v081_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_std(sbc, 8))
def cg_f021_stock_based_compensation_core81_std_8q_v082_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_std(_safe_div(sbc, revenue), 8))
def cg_f021_stock_based_compensation_core82_std_8q_v083_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_std(_safe_div(sbc, netinc.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core83_std_8q_v084_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_std(_safe_div(sbc, opex.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core84_std_8q_v085_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_std(_safe_div(sbc, marketcap), 8))
def cg_f021_stock_based_compensation_core85_std_8q_v086_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_std(_safe_div(sbc, sharesbas), 8))
def cg_f021_stock_based_compensation_core86_std_8q_v087_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_std(_safe_div(sbc, fcf.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core87_std_8q_v088_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_std(_safe_div(sbc, rnd.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core88_std_8q_v089_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_std(_safe_div(sbc, assets), 8))
def cg_f021_stock_based_compensation_core89_std_8q_v090_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_std(_log(sbc.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f021_stock_based_compensation_core90_log_v091_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_log(sbc.clip(lower=1.0)))
def cg_f021_stock_based_compensation_core91_log_v092_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_log(_safe_div(sbc, revenue).clip(lower=0.001)))
def cg_f021_stock_based_compensation_core92_log_v093_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_log(_safe_div(sbc, netinc.abs() + 1.0).clip(lower=0.001)))
def cg_f021_stock_based_compensation_core93_log_v094_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_log(_safe_div(sbc, opex.abs() + 1.0).clip(lower=0.001)))
def cg_f021_stock_based_compensation_core94_log_v095_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_log(_safe_div(sbc, marketcap).clip(lower=0.0001)))
def cg_f021_stock_based_compensation_core95_log_v096_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_log(_safe_div(sbc, sharesbas).clip(lower=0.001)))
def cg_f021_stock_based_compensation_core96_log_v097_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_log(_safe_div(sbc, fcf.abs() + 1.0).clip(lower=0.001)))
def cg_f021_stock_based_compensation_core97_log_v098_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_log(_safe_div(sbc, rnd.abs() + 1.0).clip(lower=0.001)))
def cg_f021_stock_based_compensation_core98_log_v099_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_log(_safe_div(sbc, assets).clip(lower=0.0001)))
def cg_f021_stock_based_compensation_core99_log_v100_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_log(_safe_div(sbc, revenue).clip(lower=0.001)))

# Block 100-109: diff 1q
def cg_f021_stock_based_compensation_core100_diff_1q_v101_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_diff(sbc, 1))
def cg_f021_stock_based_compensation_core101_diff_1q_v102_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_diff(_safe_div(sbc, revenue), 1))
def cg_f021_stock_based_compensation_core102_diff_1q_v103_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_diff(_safe_div(sbc, netinc.abs() + 1.0), 1))
def cg_f021_stock_based_compensation_core103_diff_1q_v104_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_diff(_safe_div(sbc, opex.abs() + 1.0), 1))
def cg_f021_stock_based_compensation_core104_diff_1q_v105_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_diff(_safe_div(sbc, marketcap), 1))
def cg_f021_stock_based_compensation_core105_diff_1q_v106_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_diff(_safe_div(sbc, sharesbas), 1))
def cg_f021_stock_based_compensation_core106_diff_1q_v107_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_diff(_safe_div(sbc, fcf.abs() + 1.0), 1))
def cg_f021_stock_based_compensation_core107_diff_1q_v108_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_diff(_safe_div(sbc, rnd.abs() + 1.0), 1))
def cg_f021_stock_based_compensation_core108_diff_1q_v109_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_diff(_safe_div(sbc, assets), 1))
def cg_f021_stock_based_compensation_core109_diff_1q_v110_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_diff(_log(sbc.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f021_stock_based_compensation_core110_slope_4q_v111_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_slope(sbc, 4))
def cg_f021_stock_based_compensation_core111_slope_4q_v112_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_slope(_safe_div(sbc, revenue), 4))
def cg_f021_stock_based_compensation_core112_slope_4q_v113_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_slope(_safe_div(sbc, netinc.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core113_slope_4q_v114_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_slope(_safe_div(sbc, opex.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core114_slope_4q_v115_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_slope(_safe_div(sbc, marketcap), 4))
def cg_f021_stock_based_compensation_core115_slope_4q_v116_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_slope(_safe_div(sbc, sharesbas), 4))
def cg_f021_stock_based_compensation_core116_slope_4q_v117_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_slope(_safe_div(sbc, fcf.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core117_slope_4q_v118_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_slope(_safe_div(sbc, rnd.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core118_slope_4q_v119_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_slope(_safe_div(sbc, assets), 4))
def cg_f021_stock_based_compensation_core119_slope_4q_v120_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_slope(_log(sbc.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f021_stock_based_compensation_core120_ewm_8q_v121_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_ewm(sbc, 8))
def cg_f021_stock_based_compensation_core121_ewm_8q_v122_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_ewm(_safe_div(sbc, revenue), 8))
def cg_f021_stock_based_compensation_core122_ewm_8q_v123_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_ewm(_safe_div(sbc, netinc.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core123_ewm_8q_v124_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_ewm(_safe_div(sbc, opex.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core124_ewm_8q_v125_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_ewm(_safe_div(sbc, marketcap), 8))
def cg_f021_stock_based_compensation_core125_ewm_8q_v126_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_ewm(_safe_div(sbc, sharesbas), 8))
def cg_f021_stock_based_compensation_core126_ewm_8q_v127_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_ewm(_safe_div(sbc, fcf.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core127_ewm_8q_v128_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_ewm(_safe_div(sbc, rnd.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core128_ewm_8q_v129_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_ewm(_safe_div(sbc, assets), 8))
def cg_f021_stock_based_compensation_core129_ewm_8q_v130_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_ewm(_log(sbc.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f021_stock_based_compensation_core130_stability_12q_v131_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_safe_div(_std(sbc, 12), _mean(sbc, 12).abs() + 1.0))
def cg_f021_stock_based_compensation_core131_stability_12q_v132_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    base = _safe_div(sbc, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f021_stock_based_compensation_core132_stability_12q_v133_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    base = _safe_div(sbc, netinc.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f021_stock_based_compensation_core133_stability_12q_v134_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    base = _safe_div(sbc, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f021_stock_based_compensation_core134_stability_12q_v135_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    base = _safe_div(sbc, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f021_stock_based_compensation_core135_stability_12q_v136_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    base = _safe_div(sbc, sharesbas)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f021_stock_based_compensation_core136_stability_12q_v137_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    base = _safe_div(sbc, fcf.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f021_stock_based_compensation_core137_stability_12q_v138_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    base = _safe_div(sbc, rnd.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f021_stock_based_compensation_core138_stability_12q_v139_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    base = _safe_div(sbc, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f021_stock_based_compensation_core139_stability_12q_v140_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    base = _log(sbc.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: raw levels (optimized)
def cg_f021_stock_based_compensation_core140_sbc_v141_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(sbc)
def cg_f021_stock_based_compensation_core141_sbc_rev_v142_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_safe_div(sbc, revenue))
def cg_f021_stock_based_compensation_core142_sbc_ni_v143_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_safe_div(sbc, netinc.abs() + 1.0))
def cg_f021_stock_based_compensation_core143_sbc_opex_v144_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_safe_div(sbc, opex.abs() + 1.0))
def cg_f021_stock_based_compensation_core144_sbc_mcap_v145_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_safe_div(sbc, marketcap))
def cg_f021_stock_based_compensation_core145_sbc_shares_v146_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_safe_div(sbc, sharesbas))
def cg_f021_stock_based_compensation_core146_sbc_fcf_v147_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_safe_div(sbc, fcf.abs() + 1.0))
def cg_f021_stock_based_compensation_core147_sbc_rnd_v148_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_safe_div(sbc, rnd.abs() + 1.0))
def cg_f021_stock_based_compensation_core148_sbc_assets_v149_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_safe_div(sbc, assets))
def cg_f021_stock_based_compensation_core149_sbc_log_v150_signal(sbc, revenue, netinc, opex, marketcap, sharesbas, fcf, rnd, assets):
    return _clean(_log(sbc.clip(lower=1.0)))
