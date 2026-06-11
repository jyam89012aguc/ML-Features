import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def _get_liq(cashneq, investmentsc): return cashneq + investmentsc

# core75-79: pct 4q (continued)
def cg_f002_short_term_investments_core75_pct4q_v076_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(_get_liq(cashneq, investmentsc), liabilities), 4))
def cg_f002_short_term_investments_core76_pct4q_v077_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(_get_liq(cashneq, investmentsc), debt), 4))
def cg_f002_short_term_investments_core77_pct4q_v078_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(investmentsc, cashneq + 1.0), 4))
def cg_f002_short_term_investments_core78_pct4q_v079_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(_get_liq(cashneq, investmentsc), opex.abs() + 1.0), 4))
def cg_f002_short_term_investments_core79_pct4q_v080_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(_get_liq(cashneq, investmentsc), capex.abs() + rnd.abs() + 1.0), 4))

# core80-89: std 8q
def cg_f002_short_term_investments_core80_std8q_v081_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_std(investmentsc, 8))
def cg_f002_short_term_investments_core81_std8q_v082_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_std(_get_liq(cashneq, investmentsc), 8))
def cg_f002_short_term_investments_core82_std8q_v083_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_std(_safe_div(_get_liq(cashneq, investmentsc), assets), 8))
def cg_f002_short_term_investments_core83_std8q_v084_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_std(_safe_div(_get_liq(cashneq, investmentsc), marketcap), 8))
def cg_f002_short_term_investments_core84_std8q_v085_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_std(_safe_div(_get_liq(cashneq, investmentsc), revenue), 8))
def cg_f002_short_term_investments_core85_std8q_v086_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_std(_safe_div(_get_liq(cashneq, investmentsc), liabilities), 8))
def cg_f002_short_term_investments_core86_std8q_v087_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_std(_safe_div(_get_liq(cashneq, investmentsc), debt), 8))
def cg_f002_short_term_investments_core87_std8q_v088_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_std(_safe_div(investmentsc, cashneq + 1.0), 8))
def cg_f002_short_term_investments_core88_std8q_v089_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_std(_safe_div(_get_liq(cashneq, investmentsc), opex.abs() + 1.0), 8))
def cg_f002_short_term_investments_core89_std8q_v090_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_std(_safe_div(_get_liq(cashneq, investmentsc), capex.abs() + rnd.abs() + 1.0), 8))

# core90-99: log
def cg_f002_short_term_investments_core90_log_v091_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_log(investmentsc.clip(lower=1.0)))
def cg_f002_short_term_investments_core91_log_v092_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_log(_get_liq(cashneq, investmentsc).clip(lower=1.0)))
def cg_f002_short_term_investments_core92_log_v093_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_log(_safe_div(_get_liq(cashneq, investmentsc), assets).clip(lower=0.001)))
def cg_f002_short_term_investments_core93_log_v094_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_log(_safe_div(_get_liq(cashneq, investmentsc), marketcap).clip(lower=0.001)))
def cg_f002_short_term_investments_core94_log_v095_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_log(_safe_div(_get_liq(cashneq, investmentsc), revenue).clip(lower=0.001)))
def cg_f002_short_term_investments_core95_log_v096_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_log(_safe_div(_get_liq(cashneq, investmentsc), liabilities).clip(lower=0.001)))
def cg_f002_short_term_investments_core96_log_v097_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_log(_safe_div(_get_liq(cashneq, investmentsc), debt).clip(lower=0.001)))
def cg_f002_short_term_investments_core97_log_v098_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_log(_safe_div(investmentsc, cashneq + 1.0).clip(lower=0.001)))
def cg_f002_short_term_investments_core98_log_v099_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_log(_safe_div(_get_liq(cashneq, investmentsc), opex.abs() + 1.0).clip(lower=0.001)))
def cg_f002_short_term_investments_core99_log_v100_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_log(_safe_div(_get_liq(cashneq, investmentsc), capex.abs() + rnd.abs() + 1.0).clip(lower=0.001)))

# core100-109: diff 1q
def cg_f002_short_term_investments_core100_diff1q_v101_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_diff(investmentsc, 1))
def cg_f002_short_term_investments_core101_diff1q_v102_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_diff(_get_liq(cashneq, investmentsc), 1))
def cg_f002_short_term_investments_core102_diff1q_v103_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_diff(_safe_div(_get_liq(cashneq, investmentsc), assets), 1))
def cg_f002_short_term_investments_core103_diff1q_v104_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_diff(_safe_div(_get_liq(cashneq, investmentsc), marketcap), 1))
def cg_f002_short_term_investments_core104_diff1q_v105_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_diff(_safe_div(_get_liq(cashneq, investmentsc), revenue), 1))
def cg_f002_short_term_investments_core105_diff1q_v106_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_diff(_safe_div(_get_liq(cashneq, investmentsc), liabilities), 1))
def cg_f002_short_term_investments_core106_diff1q_v107_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_diff(_safe_div(_get_liq(cashneq, investmentsc), debt), 1))
def cg_f002_short_term_investments_core107_diff1q_v108_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_diff(_safe_div(investmentsc, cashneq + 1.0), 1))
def cg_f002_short_term_investments_core108_diff1q_v109_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_diff(_safe_div(_get_liq(cashneq, investmentsc), opex.abs() + 1.0), 1))
def cg_f002_short_term_investments_core109_diff1q_v110_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_diff(_safe_div(_get_liq(cashneq, investmentsc), capex.abs() + rnd.abs() + 1.0), 1))

# core110-119: slope 4q
def cg_f002_short_term_investments_core110_slope4q_v111_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_slope(investmentsc, 4))
def cg_f002_short_term_investments_core111_slope4q_v112_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_slope(_get_liq(cashneq, investmentsc), 4))
def cg_f002_short_term_investments_core112_slope4q_v113_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_slope(_safe_div(_get_liq(cashneq, investmentsc), assets), 4))
def cg_f002_short_term_investments_core113_slope4q_v114_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_slope(_safe_div(_get_liq(cashneq, investmentsc), marketcap), 4))
def cg_f002_short_term_investments_core114_slope4q_v115_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_slope(_safe_div(_get_liq(cashneq, investmentsc), revenue), 4))
def cg_f002_short_term_investments_core115_slope4q_v116_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_slope(_safe_div(_get_liq(cashneq, investmentsc), liabilities), 4))
def cg_f002_short_term_investments_core116_slope4q_v117_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_slope(_safe_div(_get_liq(cashneq, investmentsc), debt), 4))
def cg_f002_short_term_investments_core117_slope4q_v118_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_slope(_safe_div(investmentsc, cashneq + 1.0), 4))
def cg_f002_short_term_investments_core118_slope4q_v119_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_slope(_safe_div(_get_liq(cashneq, investmentsc), opex.abs() + 1.0), 4))
def cg_f002_short_term_investments_core119_slope4q_v120_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_slope(_safe_div(_get_liq(cashneq, investmentsc), capex.abs() + rnd.abs() + 1.0), 4))

# core120-129: ewm 8q
def cg_f002_short_term_investments_core120_ewm8q_v121_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_ewm(investmentsc, 8))
def cg_f002_short_term_investments_core121_ewm8q_v122_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_ewm(_get_liq(cashneq, investmentsc), 8))
def cg_f002_short_term_investments_core122_ewm8q_v123_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_ewm(_safe_div(_get_liq(cashneq, investmentsc), assets), 8))
def cg_f002_short_term_investments_core123_ewm8q_v124_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_ewm(_safe_div(_get_liq(cashneq, investmentsc), marketcap), 8))
def cg_f002_short_term_investments_core124_ewm8q_v125_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_ewm(_safe_div(_get_liq(cashneq, investmentsc), revenue), 8))
def cg_f002_short_term_investments_core125_ewm8q_v126_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_ewm(_safe_div(_get_liq(cashneq, investmentsc), liabilities), 8))
def cg_f002_short_term_investments_core126_ewm8q_v127_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_ewm(_safe_div(_get_liq(cashneq, investmentsc), debt), 8))
def cg_f002_short_term_investments_core127_ewm8q_v128_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_ewm(_safe_div(investmentsc, cashneq + 1.0), 8))
def cg_f002_short_term_investments_core128_ewm8q_v129_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_ewm(_safe_div(_get_liq(cashneq, investmentsc), opex.abs() + 1.0), 8))
def cg_f002_short_term_investments_core129_ewm8q_v130_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_ewm(_safe_div(_get_liq(cashneq, investmentsc), capex.abs() + rnd.abs() + 1.0), 8))

# core130-139: stability 12q
def cg_f002_short_term_investments_core130_stability12q_v131_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_safe_div(_std(investmentsc, 12), _mean(investmentsc, 12)))
def cg_f002_short_term_investments_core131_stability12q_v132_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    base = _get_liq(cashneq, investmentsc)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f002_short_term_investments_core132_stability12q_v133_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    base = _safe_div(_get_liq(cashneq, investmentsc), assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f002_short_term_investments_core133_stability12q_v134_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    base = _safe_div(_get_liq(cashneq, investmentsc), marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f002_short_term_investments_core134_stability12q_v135_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    base = _safe_div(_get_liq(cashneq, investmentsc), revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f002_short_term_investments_core135_stability12q_v136_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    base = _safe_div(_get_liq(cashneq, investmentsc), liabilities)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f002_short_term_investments_core136_stability12q_v137_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    base = _safe_div(_get_liq(cashneq, investmentsc), debt)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f002_short_term_investments_core137_stability12q_v138_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    base = _safe_div(investmentsc, cashneq + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f002_short_term_investments_core138_stability12q_v139_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    base = _safe_div(_get_liq(cashneq, investmentsc), opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f002_short_term_investments_core139_stability12q_v140_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    base = _safe_div(_get_liq(cashneq, investmentsc), capex.abs() + rnd.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))

# core140-149: levels (optimized)
def cg_f002_short_term_investments_core140_level_v141_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(investmentsc)
def cg_f002_short_term_investments_core141_liq_v142_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_get_liq(cashneq, investmentsc))
def cg_f002_short_term_investments_core142_liq_assets_v143_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_safe_div(_get_liq(cashneq, investmentsc), assets))
def cg_f002_short_term_investments_core143_liq_mcap_v144_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_safe_div(_get_liq(cashneq, investmentsc), marketcap))
def cg_f002_short_term_investments_core144_liq_rev_v145_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_safe_div(_get_liq(cashneq, investmentsc), revenue))
def cg_f002_short_term_investments_core145_liq_liab_v146_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_safe_div(_get_liq(cashneq, investmentsc), liabilities))
def cg_f002_short_term_investments_core146_liq_debt_v147_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_safe_div(_get_liq(cashneq, investmentsc), debt))
def cg_f002_short_term_investments_core147_inv_cash_v148_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_safe_div(investmentsc, cashneq + 1.0))
def cg_f002_short_term_investments_core148_liq_opex_v149_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_safe_div(_get_liq(cashneq, investmentsc), opex.abs() + 1.0))
def cg_f002_short_term_investments_core149_liq_capex_rnd_v150_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_safe_div(_get_liq(cashneq, investmentsc), capex.abs() + rnd.abs() + 1.0))
