import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f001_cash_and_equivalents_core75_pct_4q_v076_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, debt), 4))
def cg_f001_cash_and_equivalents_core76_pct_4q_v077_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, sharesbas), 4))
def cg_f001_cash_and_equivalents_core77_pct_4q_v078_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, capex.abs() + 1.0), 4))
def cg_f001_cash_and_equivalents_core78_pct_4q_v079_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, rnd.abs() + 1.0), 4))
def cg_f001_cash_and_equivalents_core79_pct_4q_v080_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(cashneq, opex.abs() + 1.0), 4))

# core80-89: std 8q
def cg_f001_cash_and_equivalents_core80_std_8q_v081_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_std(cashneq, 8))
def cg_f001_cash_and_equivalents_core81_std_8q_v082_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_std(_safe_div(cashneq, assets), 8))
def cg_f001_cash_and_equivalents_core82_std_8q_v083_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_std(_safe_div(cashneq, marketcap), 8))
def cg_f001_cash_and_equivalents_core83_std_8q_v084_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_std(_safe_div(cashneq, revenue), 8))
def cg_f001_cash_and_equivalents_core84_std_8q_v085_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_std(_safe_div(cashneq, liabilities), 8))
def cg_f001_cash_and_equivalents_core85_std_8q_v086_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_std(_safe_div(cashneq, debt), 8))
def cg_f001_cash_and_equivalents_core86_std_8q_v087_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_std(_safe_div(cashneq, sharesbas), 8))
def cg_f001_cash_and_equivalents_core87_std_8q_v088_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_std(_safe_div(cashneq, capex.abs() + 1.0), 8))
def cg_f001_cash_and_equivalents_core88_std_8q_v089_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_std(_safe_div(cashneq, rnd.abs() + 1.0), 8))
def cg_f001_cash_and_equivalents_core89_std_8q_v090_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_std(_safe_div(cashneq, opex.abs() + 1.0), 8))

# core90-99: log
def cg_f001_cash_and_equivalents_core90_log_v091_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_log(cashneq.clip(lower=1.0)))
def cg_f001_cash_and_equivalents_core91_log_v092_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_log(_safe_div(cashneq, assets).clip(lower=0.001)))
def cg_f001_cash_and_equivalents_core92_log_v093_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_log(_safe_div(cashneq, marketcap).clip(lower=0.001)))
def cg_f001_cash_and_equivalents_core93_log_v094_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_log(_safe_div(cashneq, revenue).clip(lower=0.001)))
def cg_f001_cash_and_equivalents_core94_log_v095_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_log(_safe_div(cashneq, liabilities).clip(lower=0.001)))
def cg_f001_cash_and_equivalents_core95_log_v096_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_log(_safe_div(cashneq, debt).clip(lower=0.001)))
def cg_f001_cash_and_equivalents_core96_log_v097_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_log(_safe_div(cashneq, sharesbas).clip(lower=0.001)))
def cg_f001_cash_and_equivalents_core97_log_v098_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_log(_safe_div(cashneq, capex.abs() + 1.0).clip(lower=0.001)))
def cg_f001_cash_and_equivalents_core98_log_v099_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_log(_safe_div(cashneq, rnd.abs() + 1.0).clip(lower=0.001)))
def cg_f001_cash_and_equivalents_core99_log_v100_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_log(_safe_div(cashneq, opex.abs() + 1.0).clip(lower=0.001)))

# core100-109: diff 1q
def cg_f001_cash_and_equivalents_core100_diff_1q_v101_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(cashneq, 1))
def cg_f001_cash_and_equivalents_core101_diff_1q_v102_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, assets), 1))
def cg_f001_cash_and_equivalents_core102_diff_1q_v103_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, marketcap), 1))
def cg_f001_cash_and_equivalents_core103_diff_1q_v104_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, revenue), 1))
def cg_f001_cash_and_equivalents_core104_diff_1q_v105_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, liabilities), 1))
def cg_f001_cash_and_equivalents_core105_diff_1q_v106_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, debt), 1))
def cg_f001_cash_and_equivalents_core106_diff_1q_v107_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, sharesbas), 1))
def cg_f001_cash_and_equivalents_core107_diff_1q_v108_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, capex.abs() + 1.0), 1))
def cg_f001_cash_and_equivalents_core108_diff_1q_v109_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, rnd.abs() + 1.0), 1))
def cg_f001_cash_and_equivalents_core109_diff_1q_v110_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_diff(_safe_div(cashneq, opex.abs() + 1.0), 1))

# core110-119: slope 4q
def cg_f001_cash_and_equivalents_core110_slope_4q_v111_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(cashneq, 4))
def cg_f001_cash_and_equivalents_core111_slope_4q_v112_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, assets), 4))
def cg_f001_cash_and_equivalents_core112_slope_4q_v113_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, marketcap), 4))
def cg_f001_cash_and_equivalents_core113_slope_4q_v114_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, revenue), 4))
def cg_f001_cash_and_equivalents_core114_slope_4q_v115_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, liabilities), 4))
def cg_f001_cash_and_equivalents_core115_slope_4q_v116_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, debt), 4))
def cg_f001_cash_and_equivalents_core116_slope_4q_v117_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, sharesbas), 4))
def cg_f001_cash_and_equivalents_core117_slope_4q_v118_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, capex.abs() + 1.0), 4))
def cg_f001_cash_and_equivalents_core118_slope_4q_v119_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, rnd.abs() + 1.0), 4))
def cg_f001_cash_and_equivalents_core119_slope_4q_v120_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_slope(_safe_div(cashneq, opex.abs() + 1.0), 4))

# core120-129: ewm 8q
def cg_f001_cash_and_equivalents_core120_ewm_8q_v121_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_ewm(cashneq, 8))
def cg_f001_cash_and_equivalents_core121_ewm_8q_v122_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_ewm(_safe_div(cashneq, assets), 8))
def cg_f001_cash_and_equivalents_core122_ewm_8q_v123_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_ewm(_safe_div(cashneq, marketcap), 8))
def cg_f001_cash_and_equivalents_core123_ewm_8q_v124_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_ewm(_safe_div(cashneq, revenue), 8))
def cg_f001_cash_and_equivalents_core124_ewm_8q_v125_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_ewm(_safe_div(cashneq, liabilities), 8))
def cg_f001_cash_and_equivalents_core125_ewm_8q_v126_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_ewm(_safe_div(cashneq, debt), 8))
def cg_f001_cash_and_equivalents_core126_ewm_8q_v127_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_ewm(_safe_div(cashneq, sharesbas), 8))
def cg_f001_cash_and_equivalents_core127_ewm_8q_v128_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_ewm(_safe_div(cashneq, capex.abs() + 1.0), 8))
def cg_f001_cash_and_equivalents_core128_ewm_8q_v129_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_ewm(_safe_div(cashneq, rnd.abs() + 1.0), 8))
def cg_f001_cash_and_equivalents_core129_ewm_8q_v130_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_ewm(_safe_div(cashneq, opex.abs() + 1.0), 8))

# core130-139: stability 12q
def cg_f001_cash_and_equivalents_core130_stability_12q_v131_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_safe_div(_std(cashneq, 12), _mean(cashneq, 12)))
def cg_f001_cash_and_equivalents_core131_stability_12q_v132_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    base = _safe_div(cashneq, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f001_cash_and_equivalents_core132_stability_12q_v133_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    base = _safe_div(cashneq, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f001_cash_and_equivalents_core133_stability_12q_v134_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    base = _safe_div(cashneq, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f001_cash_and_equivalents_core134_stability_12q_v135_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    base = _safe_div(cashneq, liabilities)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f001_cash_and_equivalents_core135_stability_12q_v136_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    base = _safe_div(cashneq, debt)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f001_cash_and_equivalents_core136_stability_12q_v137_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    base = _safe_div(cashneq, sharesbas)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f001_cash_and_equivalents_core137_stability_12q_v138_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    base = _safe_div(cashneq, capex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f001_cash_and_equivalents_core138_stability_12q_v139_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    base = _safe_div(cashneq, rnd.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f001_cash_and_equivalents_core139_stability_12q_v140_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    base = _safe_div(cashneq, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))

# core140-149: raw levels (optimized)
def cg_f001_cash_and_equivalents_core140_level_v141_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(cashneq)
def cg_f001_cash_and_equivalents_core141_to_assets_v142_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_safe_div(cashneq, assets))
def cg_f001_cash_and_equivalents_core142_to_marketcap_v143_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_safe_div(cashneq, marketcap))
def cg_f001_cash_and_equivalents_core143_to_revenue_v144_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_safe_div(cashneq, revenue))
def cg_f001_cash_and_equivalents_core144_to_liabilities_v145_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_safe_div(cashneq, liabilities))
def cg_f001_cash_and_equivalents_core145_to_debt_v146_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_safe_div(cashneq, debt))
def cg_f001_cash_and_equivalents_core146_per_share_v147_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_safe_div(cashneq, sharesbas))
def cg_f001_cash_and_equivalents_core147_to_capex_v148_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_safe_div(cashneq, capex.abs() + 1.0))
def cg_f001_cash_and_equivalents_core148_to_rnd_v149_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_safe_div(cashneq, rnd.abs() + 1.0))
def cg_f001_cash_and_equivalents_core149_to_opex_v150_signal(cashneq, assets, marketcap, revenue, liabilities, debt, sharesbas, capex, rnd, opex):
    return _clean(_safe_div(cashneq, opex.abs() + 1.0))
