import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f023_debt_level_core75_pct_4q_v076_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debt, ebitda.clip(lower=0) + 1.0), 4))
def cg_f023_debt_level_core76_pct_4q_v077_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debt, capital.abs() + 1.0), 4))
def cg_f023_debt_level_core77_pct_4q_v078_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debt, sharesbas), 4))
def cg_f023_debt_level_core78_pct_4q_v079_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_safe_div(debtt - debt, debtt.abs() + 1.0), 4))
def cg_f023_debt_level_core79_pct_4q_v080_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_pct_change(_log(debt.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f023_debt_level_core80_std_8q_v081_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_std(debt, 8))
def cg_f023_debt_level_core81_std_8q_v082_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_std(_safe_div(debt, assets), 8))
def cg_f023_debt_level_core82_std_8q_v083_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_std(_safe_div(debt, marketcap), 8))
def cg_f023_debt_level_core83_std_8q_v084_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_std(_safe_div(debt, ebitda.clip(lower=0) + 1.0), 8))
def cg_f023_debt_level_core84_std_8q_v085_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_std(_safe_div(debt, capital.abs() + 1.0), 8))
def cg_f023_debt_level_core85_std_8q_v086_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_std(_safe_div(debt, ncfo.abs() + 1.0), 8))
def cg_f023_debt_level_core86_std_8q_v087_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_std(_safe_div(debtt - debt, debtt.abs() + 1.0), 8))
def cg_f023_debt_level_core87_std_8q_v088_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_std(_safe_div(debt, equity.abs() + 1.0), 8))
def cg_f023_debt_level_core88_std_8q_v089_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_std(_safe_div(debt, sharesbas), 8))
def cg_f023_debt_level_core89_std_8q_v090_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_std(_log(debt.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f023_debt_level_core90_log_v091_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_log(debt.clip(lower=1.0)))
def cg_f023_debt_level_core91_log_v092_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_log(_safe_div(debt, assets).clip(lower=0.0001)))
def cg_f023_debt_level_core92_log_v093_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_log(_safe_div(debt, marketcap).clip(lower=0.0001)))
def cg_f023_debt_level_core93_log_v094_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_log(_safe_div(debt, ebitda.clip(lower=0) + 1.0).clip(lower=0.01)))
def cg_f023_debt_level_core94_log_v095_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_log(_safe_div(debt, capital.abs() + 1.0).clip(lower=0.01)))
def cg_f023_debt_level_core95_log_v096_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_log(_safe_div(debt, ncfo.abs() + 1.0).clip(lower=0.01)))
def cg_f023_debt_level_core96_log_v097_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_log(_safe_div(debtt - debt, debtt.abs() + 1.0).clip(lower=0.01)))
def cg_f023_debt_level_core97_log_v098_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_log(_safe_div(debt, equity.abs() + 1.0).clip(lower=0.01)))
def cg_f023_debt_level_core98_log_v099_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_log(_safe_div(debt, sharesbas).clip(lower=0.01)))
def cg_f023_debt_level_core99_log_v100_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_log(_safe_div(debt, assets).clip(lower=0.0001)))

# Block 100-109: diff 1q
def cg_f023_debt_level_core100_diff_1q_v101_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_diff(debt, 1))
def cg_f023_debt_level_core101_diff_1q_v102_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_diff(_safe_div(debt, assets), 1))
def cg_f023_debt_level_core102_diff_1q_v103_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_diff(_safe_div(debt, marketcap), 1))
def cg_f023_debt_level_core103_diff_1q_v104_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_diff(_safe_div(debt, ebitda.clip(lower=0) + 1.0), 1))
def cg_f023_debt_level_core104_diff_1q_v105_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_diff(_safe_div(debt, capital.abs() + 1.0), 1))
def cg_f023_debt_level_core105_diff_1q_v106_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_diff(_safe_div(debt, ncfo.abs() + 1.0), 1))
def cg_f023_debt_level_core106_diff_1q_v107_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_diff(_safe_div(debtt - debt, debtt.abs() + 1.0), 1))
def cg_f023_debt_level_core107_diff_1q_v108_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_diff(_safe_div(debt, equity.abs() + 1.0), 1))
def cg_f023_debt_level_core108_diff_1q_v109_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_diff(_safe_div(debt, sharesbas), 1))
def cg_f023_debt_level_core109_diff_1q_v110_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_diff(_log(debt.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f023_debt_level_core110_slope_4q_v111_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_slope(debt, 4))
def cg_f023_debt_level_core111_slope_4q_v112_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_slope(_safe_div(debt, assets), 4))
def cg_f023_debt_level_core112_slope_4q_v113_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_slope(_safe_div(debt, marketcap), 4))
def cg_f023_debt_level_core113_slope_4q_v114_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_slope(_safe_div(debt, ebitda.clip(lower=0) + 1.0), 4))
def cg_f023_debt_level_core114_slope_4q_v115_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_slope(_safe_div(debt, capital.abs() + 1.0), 4))
def cg_f023_debt_level_core115_slope_4q_v116_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_slope(_safe_div(debt, ncfo.abs() + 1.0), 4))
def cg_f023_debt_level_core116_slope_4q_v117_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_slope(_safe_div(debtt - debt, debtt.abs() + 1.0), 4))
def cg_f023_debt_level_core117_slope_4q_v118_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_slope(_safe_div(debt, equity.abs() + 1.0), 4))
def cg_f023_debt_level_core118_slope_4q_v119_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_slope(_safe_div(debt, sharesbas), 4))
def cg_f023_debt_level_core119_slope_4q_v120_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_slope(_log(debt.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f023_debt_level_core120_ewm_8q_v121_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_ewm(debt, 8))
def cg_f023_debt_level_core121_ewm_8q_v122_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_ewm(_safe_div(debt, assets), 8))
def cg_f023_debt_level_core122_ewm_8q_v123_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_ewm(_safe_div(debt, marketcap), 8))
def cg_f023_debt_level_core123_ewm_8q_v124_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_ewm(_safe_div(debt, ebitda.clip(lower=0) + 1.0), 8))
def cg_f023_debt_level_core124_ewm_8q_v125_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_ewm(_safe_div(debt, capital.abs() + 1.0), 8))
def cg_f023_debt_level_core125_ewm_8q_v126_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_ewm(_safe_div(debt, ncfo.abs() + 1.0), 8))
def cg_f023_debt_level_core126_ewm_8q_v127_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_ewm(_safe_div(debtt - debt, debtt.abs() + 1.0), 8))
def cg_f023_debt_level_core127_ewm_8q_v128_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_ewm(_safe_div(debt, equity.abs() + 1.0), 8))
def cg_f023_debt_level_core128_ewm_8q_v129_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_ewm(_safe_div(debt, sharesbas), 8))
def cg_f023_debt_level_core129_ewm_8q_v130_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_ewm(_log(debt.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f023_debt_level_core130_stability_12q_v131_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_safe_div(_std(debt, 12), _mean(debt, 12).abs() + 1.0))
def cg_f023_debt_level_core131_stability_12q_v132_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    base = _safe_div(debt, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f023_debt_level_core132_stability_12q_v133_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    base = _safe_div(debt, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f023_debt_level_core133_stability_12q_v134_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    base = _safe_div(debt, ebitda.clip(lower=0) + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f023_debt_level_core134_stability_12q_v135_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    base = _safe_div(debt, capital.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f023_debt_level_core135_stability_12q_v136_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    base = _safe_div(debt, ncfo.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f023_debt_level_core136_stability_12q_v137_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    base = _safe_div(debtt - debt, debtt.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f023_debt_level_core137_stability_12q_v138_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    base = _safe_div(debt, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f023_debt_level_core138_stability_12q_v139_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    base = _safe_div(debt, sharesbas)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f023_debt_level_core139_stability_12q_v140_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    base = _log(debt.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f023_debt_level_core140_debt_v141_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(debt)
def cg_f023_debt_level_core141_debt_assets_v142_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_safe_div(debt, assets))
def cg_f023_debt_level_core142_debt_mcap_v143_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_safe_div(debt, marketcap))
def cg_f023_debt_level_core143_debt_ebitda_v144_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_safe_div(debt, ebitda.clip(lower=0) + 1.0))
def cg_f023_debt_level_core144_debt_cap_v145_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_safe_div(debt, capital.abs() + 1.0))
def cg_f023_debt_level_core145_debt_ncfo_v146_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_safe_div(debt, ncfo.abs() + 1.0))
def cg_f023_debt_level_core146_st_ratio_v147_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_safe_div(debtt - debt, debtt.abs() + 1.0))
def cg_f023_debt_level_core147_debt_equity_v148_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_safe_div(debt, equity.abs() + 1.0))
def cg_f023_debt_level_core148_debt_shares_v149_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_safe_div(debt, sharesbas))
def cg_f023_debt_level_core149_debt_log_v150_signal(debt, assets, marketcap, equity, ncfo, ebitda, capital, sharesbas, debtt):
    return _clean(_log(debt.clip(lower=1.0)))
