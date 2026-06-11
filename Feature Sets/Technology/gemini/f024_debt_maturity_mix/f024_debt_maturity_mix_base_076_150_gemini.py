import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f024_debt_maturity_mix_core75_pct_4q_v076_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt - debt, revenue), 4))
def cg_f024_debt_maturity_mix_core76_pct_4q_v077_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debt, assets), 4))
def cg_f024_debt_maturity_mix_core77_pct_4q_v078_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt - debt, marketcap), 4))
def cg_f024_debt_maturity_mix_core78_pct_4q_v079_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_pct_change(_safe_div(debtt - debt, sharesbas), 4))
def cg_f024_debt_maturity_mix_core79_pct_4q_v080_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_pct_change(_log((debtt - debt).clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f024_debt_maturity_mix_core80_std_8q_v081_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_std(_safe_div(debtt - debt, debt.abs() + 1.0), 8))
def cg_f024_debt_maturity_mix_core81_std_8q_v082_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_std(_safe_div(debt, debtt.abs() + 1.0), 8))
def cg_f024_debt_maturity_mix_core82_std_8q_v083_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_std(_safe_div(debtt - debt, assets), 8))
def cg_f024_debt_maturity_mix_core83_std_8q_v084_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_std(_safe_div(debtt - debt, ncfo.abs() + 1.0), 8))
def cg_f024_debt_maturity_mix_core84_std_8q_v085_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_std(_safe_div(debtt - debt, cashneq.abs() + 1.0), 8))
def cg_f024_debt_maturity_mix_core85_std_8q_v086_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_std(_safe_div(debtt - debt, revenue), 8))
def cg_f024_debt_maturity_mix_core86_std_8q_v087_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_std(_safe_div(debt, assets), 8))
def cg_f024_debt_maturity_mix_core87_std_8q_v088_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_std(_safe_div(debtt - debt, marketcap), 8))
def cg_f024_debt_maturity_mix_core88_std_8q_v089_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_std(_safe_div(debtt - debt, sharesbas), 8))
def cg_f024_debt_maturity_mix_core89_std_8q_v090_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_std(_log((debtt - debt).clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f024_debt_maturity_mix_core90_log_v091_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_log((debtt - debt).clip(lower=1.0)))
def cg_f024_debt_maturity_mix_core91_log_v092_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_log(_safe_div(debtt - debt, debt.abs() + 1.0).clip(lower=0.001)))
def cg_f024_debt_maturity_mix_core92_log_v093_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_log(_safe_div(debt, debtt.abs() + 1.0).clip(lower=0.001)))
def cg_f024_debt_maturity_mix_core93_log_v094_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_log(_safe_div(debtt - debt, assets).clip(lower=0.001)))
def cg_f024_debt_maturity_mix_core94_log_v095_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_log(_safe_div(debtt - debt, ncfo.abs() + 1.0).clip(lower=0.001)))
def cg_f024_debt_maturity_mix_core95_log_v096_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_log(_safe_div(debtt - debt, cashneq.abs() + 1.0).clip(lower=0.001)))
def cg_f024_debt_maturity_mix_core96_log_v097_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_log(_safe_div(debtt - debt, revenue).clip(lower=0.001)))
def cg_f024_debt_maturity_mix_core97_log_v098_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_log(_safe_div(debt, assets).clip(lower=0.001)))
def cg_f024_debt_maturity_mix_core98_log_v099_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_log(_safe_div(debtt - debt, marketcap).clip(lower=0.001)))
def cg_f024_debt_maturity_mix_core99_log_v100_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_log(_safe_div(debtt - debt, sharesbas).clip(lower=0.001)))

# Block 100-109: diff 1q
def cg_f024_debt_maturity_mix_core100_diff_1q_v101_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debtt - debt, debt.abs() + 1.0), 1))
def cg_f024_debt_maturity_mix_core101_diff_1q_v102_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debt, debtt.abs() + 1.0), 1))
def cg_f024_debt_maturity_mix_core102_diff_1q_v103_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debtt - debt, assets), 1))
def cg_f024_debt_maturity_mix_core103_diff_1q_v104_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debtt - debt, ncfo.abs() + 1.0), 1))
def cg_f024_debt_maturity_mix_core104_diff_1q_v105_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debtt - debt, cashneq.abs() + 1.0), 1))
def cg_f024_debt_maturity_mix_core105_diff_1q_v106_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debtt - debt, revenue), 1))
def cg_f024_debt_maturity_mix_core106_diff_1q_v107_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debt, assets), 1))
def cg_f024_debt_maturity_mix_core107_diff_1q_v108_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debtt - debt, marketcap), 1))
def cg_f024_debt_maturity_mix_core108_diff_1q_v109_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_diff(_safe_div(debtt - debt, sharesbas), 1))
def cg_f024_debt_maturity_mix_core109_diff_1q_v110_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_diff(_log((debtt - debt).clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f024_debt_maturity_mix_core110_slope_4q_v111_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debtt - debt, debt.abs() + 1.0), 4))
def cg_f024_debt_maturity_mix_core111_slope_4q_v112_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debt, debtt.abs() + 1.0), 4))
def cg_f024_debt_maturity_mix_core112_slope_4q_v113_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debtt - debt, assets), 4))
def cg_f024_debt_maturity_mix_core113_slope_4q_v114_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debtt - debt, ncfo.abs() + 1.0), 4))
def cg_f024_debt_maturity_mix_core114_slope_4q_v115_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debtt - debt, cashneq.abs() + 1.0), 4))
def cg_f024_debt_maturity_mix_core115_slope_4q_v116_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debtt - debt, revenue), 4))
def cg_f024_debt_maturity_mix_core116_slope_4q_v117_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debt, assets), 4))
def cg_f024_debt_maturity_mix_core117_slope_4q_v118_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debtt - debt, marketcap), 4))
def cg_f024_debt_maturity_mix_core118_slope_4q_v119_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_slope(_safe_div(debtt - debt, sharesbas), 4))
def cg_f024_debt_maturity_mix_core119_slope_4q_v120_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_slope(_log((debtt - debt).clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f024_debt_maturity_mix_core120_ewm_8q_v121_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debtt - debt, debt.abs() + 1.0), 8))
def cg_f024_debt_maturity_mix_core121_ewm_8q_v122_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debt, debtt.abs() + 1.0), 8))
def cg_f024_debt_maturity_mix_core122_ewm_8q_v123_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debtt - debt, assets), 8))
def cg_f024_debt_maturity_mix_core123_ewm_8q_v124_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debtt - debt, ncfo.abs() + 1.0), 8))
def cg_f024_debt_maturity_mix_core124_ewm_8q_v125_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debtt - debt, cashneq.abs() + 1.0), 8))
def cg_f024_debt_maturity_mix_core125_ewm_8q_v126_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debtt - debt, revenue), 8))
def cg_f024_debt_maturity_mix_core126_ewm_8q_v127_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debt, assets), 8))
def cg_f024_debt_maturity_mix_core127_ewm_8q_v128_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debtt - debt, marketcap), 8))
def cg_f024_debt_maturity_mix_core128_ewm_8q_v129_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_ewm(_safe_div(debtt - debt, sharesbas), 8))
def cg_f024_debt_maturity_mix_core129_ewm_8q_v130_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_ewm(_log((debtt - debt).clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f024_debt_maturity_mix_core130_stability_12q_v131_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    base = _safe_div(debtt - debt, debt.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f024_debt_maturity_mix_core131_stability_12q_v132_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    base = _safe_div(debt, debtt.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f024_debt_maturity_mix_core132_stability_12q_v133_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    base = _safe_div(debtt - debt, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f024_debt_maturity_mix_core133_stability_12q_v134_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    base = _safe_div(debtt - debt, ncfo.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f024_debt_maturity_mix_core134_stability_12q_v135_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    base = _safe_div(debtt - debt, cashneq.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f024_debt_maturity_mix_core135_stability_12q_v136_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    base = _safe_div(debtt - debt, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f024_debt_maturity_mix_core136_stability_12q_v137_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    base = _safe_div(debt, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f024_debt_maturity_mix_core137_stability_12q_v138_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    base = _safe_div(debtt - debt, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f024_debt_maturity_mix_core138_stability_12q_v139_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    base = _safe_div(debtt - debt, sharesbas)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f024_debt_maturity_mix_core139_stability_12q_v140_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    base = _log((debtt - debt).clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f024_debt_maturity_mix_core140_lt_debt_v141_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(debtt - debt)
def cg_f024_debt_maturity_mix_core141_st_debt_v142_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(debt)
def cg_f024_debt_maturity_mix_core142_lt_ratio_v143_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_safe_div(debtt - debt, debtt.abs() + 1.0))
def cg_f024_debt_maturity_mix_core143_st_ratio_v144_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_safe_div(debt, debtt.abs() + 1.0))
def cg_f024_debt_maturity_mix_core144_lt_assets_v145_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_safe_div(debtt - debt, assets))
def cg_f024_debt_maturity_mix_core145_lt_ncfo_v146_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_safe_div(debtt - debt, ncfo.abs() + 1.0))
def cg_f024_debt_maturity_mix_core146_lt_cash_v147_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_safe_div(debtt - debt, cashneq.abs() + 1.0))
def cg_f024_debt_maturity_mix_core147_lt_revenue_v148_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_safe_div(debtt - debt, revenue))
def cg_f024_debt_maturity_mix_core148_lt_mcap_v149_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_safe_div(debtt - debt, marketcap))
def cg_f024_debt_maturity_mix_core149_lt_log_v150_signal(debtt, debt, assets, ncfo, cashneq, revenue, marketcap, sharesbas):
    return _clean(_log((debtt - debt).clip(lower=1.0)))
