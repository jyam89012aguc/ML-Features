import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f074_dividend_and_payout_valuation_core75_pct_4q_v076_signal(dps, dividends, divyield, payoutratio):
    return _clean(_pct_change(_safe_div(dividends, payoutratio.abs() + 0.01), 4))
def cg_f074_dividend_and_payout_valuation_core76_pct_4q_v077_signal(dps, dividends, divyield, payoutratio):
    return _clean(_pct_change(divyield * payoutratio, 4))
def cg_f074_dividend_and_payout_valuation_core77_pct_4q_v078_signal(dps, dividends, divyield, payoutratio):
    return _clean(_pct_change(dps * payoutratio, 4))
def cg_f074_dividend_and_payout_valuation_core78_pct_4q_v079_signal(dps, dividends, divyield, payoutratio):
    return _clean(_pct_change(_safe_div(divyield, payoutratio.abs() + 0.01), 4))
def cg_f074_dividend_and_payout_valuation_core79_pct_4q_v080_signal(dps, dividends, divyield, payoutratio):
    return _clean(_pct_change(_safe_div(dps, payoutratio.abs() + 0.01), 4))

# core80-89: std 8q
def cg_f074_dividend_and_payout_valuation_core80_std_8q_v081_signal(dps, dividends, divyield, payoutratio):
    return _clean(_std(dps, 8))
def cg_f074_dividend_and_payout_valuation_core81_std_8q_v082_signal(dps, dividends, divyield, payoutratio):
    return _clean(_std(dividends, 8))
def cg_f074_dividend_and_payout_valuation_core82_std_8q_v083_signal(dps, dividends, divyield, payoutratio):
    return _clean(_std(divyield, 8))
def cg_f074_dividend_and_payout_valuation_core83_std_8q_v084_signal(dps, dividends, divyield, payoutratio):
    return _clean(_std(payoutratio, 8))
def cg_f074_dividend_and_payout_valuation_core84_std_8q_v085_signal(dps, dividends, divyield, payoutratio):
    return _clean(_std(_safe_div(dps, divyield.abs() + 0.001), 8))
def cg_f074_dividend_and_payout_valuation_core85_std_8q_v086_signal(dps, dividends, divyield, payoutratio):
    return _clean(_std(_safe_div(dividends, payoutratio.abs() + 0.01), 8))
def cg_f074_dividend_and_payout_valuation_core86_std_8q_v087_signal(dps, dividends, divyield, payoutratio):
    return _clean(_std(divyield * payoutratio, 8))
def cg_f074_dividend_and_payout_valuation_core87_std_8q_v088_signal(dps, dividends, divyield, payoutratio):
    return _clean(_std(dps * payoutratio, 8))
def cg_f074_dividend_and_payout_valuation_core88_std_8q_v089_signal(dps, dividends, divyield, payoutratio):
    return _clean(_std(_safe_div(divyield, payoutratio.abs() + 0.01), 8))
def cg_f074_dividend_and_payout_valuation_core89_std_8q_v090_signal(dps, dividends, divyield, payoutratio):
    return _clean(_std(_safe_div(dps, payoutratio.abs() + 0.01), 8))

# core90-99: log
def cg_f074_dividend_and_payout_valuation_core90_log_v091_signal(dps, dividends, divyield, payoutratio):
    return _clean(_log(dps.clip(lower=0.01)))
def cg_f074_dividend_and_payout_valuation_core91_log_v092_signal(dps, dividends, divyield, payoutratio):
    return _clean(_log(dividends.clip(lower=1.0)))
def cg_f074_dividend_and_payout_valuation_core92_log_v093_signal(dps, dividends, divyield, payoutratio):
    return _clean(_log(divyield.clip(lower=0.0001)))
def cg_f074_dividend_and_payout_valuation_core93_log_v094_signal(dps, dividends, divyield, payoutratio):
    return _clean(_log(payoutratio.clip(lower=0.001)))
def cg_f074_dividend_and_payout_valuation_core94_log_v095_signal(dps, dividends, divyield, payoutratio):
    return _clean(_log(_safe_div(dps, divyield.abs() + 0.001).clip(lower=1.0)))
def cg_f074_dividend_and_payout_valuation_core95_log_v096_signal(dps, dividends, divyield, payoutratio):
    return _clean(_log(_safe_div(dividends, payoutratio.abs() + 0.01).clip(lower=1.0)))
def cg_f074_dividend_and_payout_valuation_core96_log_v097_signal(dps, dividends, divyield, payoutratio):
    return _clean(_log((divyield * payoutratio).clip(lower=0.0001)))
def cg_f074_dividend_and_payout_valuation_core97_log_v098_signal(dps, dividends, divyield, payoutratio):
    return _clean(_log((dps * payoutratio).clip(lower=0.001)))
def cg_f074_dividend_and_payout_valuation_core98_log_v099_signal(dps, dividends, divyield, payoutratio):
    return _clean(_log(_safe_div(divyield, payoutratio.abs() + 0.01).clip(lower=0.0001)))
def cg_f074_dividend_and_payout_valuation_core99_log_v100_signal(dps, dividends, divyield, payoutratio):
    return _clean(_log(_safe_div(dps, payoutratio.abs() + 0.01).clip(lower=0.001)))

# core100-109: diff 1q
def cg_f074_dividend_and_payout_valuation_core100_diff_1q_v101_signal(dps, dividends, divyield, payoutratio):
    return _clean(_diff(dps, 1))
def cg_f074_dividend_and_payout_valuation_core101_diff_1q_v102_signal(dps, dividends, divyield, payoutratio):
    return _clean(_diff(dividends, 1))
def cg_f074_dividend_and_payout_valuation_core102_diff_1q_v103_signal(dps, dividends, divyield, payoutratio):
    return _clean(_diff(divyield, 1))
def cg_f074_dividend_and_payout_valuation_core103_diff_1q_v104_signal(dps, dividends, divyield, payoutratio):
    return _clean(_diff(payoutratio, 1))
def cg_f074_dividend_and_payout_valuation_core104_diff_1q_v105_signal(dps, dividends, divyield, payoutratio):
    return _clean(_diff(_safe_div(dps, divyield.abs() + 0.001), 1))
def cg_f074_dividend_and_payout_valuation_core105_diff_1q_v106_signal(dps, dividends, divyield, payoutratio):
    return _clean(_diff(_safe_div(dividends, payoutratio.abs() + 0.01), 1))
def cg_f074_dividend_and_payout_valuation_core106_diff_1q_v107_signal(dps, dividends, divyield, payoutratio):
    return _clean(_diff(divyield * payoutratio, 1))
def cg_f074_dividend_and_payout_valuation_core107_diff_1q_v108_signal(dps, dividends, divyield, payoutratio):
    return _clean(_diff(dps * payoutratio, 1))
def cg_f074_dividend_and_payout_valuation_core108_diff_1q_v109_signal(dps, dividends, divyield, payoutratio):
    return _clean(_diff(_safe_div(divyield, payoutratio.abs() + 0.01), 1))
def cg_f074_dividend_and_payout_valuation_core109_diff_1q_v110_signal(dps, dividends, divyield, payoutratio):
    return _clean(_diff(_safe_div(dps, payoutratio.abs() + 0.01), 1))

# core110-119: slope 4q
def cg_f074_dividend_and_payout_valuation_core110_slope_4q_v111_signal(dps, dividends, divyield, payoutratio):
    return _clean(_slope(dps, 4))
def cg_f074_dividend_and_payout_valuation_core111_slope_4q_v112_signal(dps, dividends, divyield, payoutratio):
    return _clean(_slope(dividends, 4))
def cg_f074_dividend_and_payout_valuation_core112_slope_4q_v113_signal(dps, dividends, divyield, payoutratio):
    return _clean(_slope(divyield, 4))
def cg_f074_dividend_and_payout_valuation_core113_slope_4q_v114_signal(dps, dividends, divyield, payoutratio):
    return _clean(_slope(payoutratio, 4))
def cg_f074_dividend_and_payout_valuation_core114_slope_4q_v115_signal(dps, dividends, divyield, payoutratio):
    return _clean(_slope(_safe_div(dps, divyield.abs() + 0.001), 4))
def cg_f074_dividend_and_payout_valuation_core115_slope_4q_v116_signal(dps, dividends, divyield, payoutratio):
    return _clean(_slope(_safe_div(dividends, payoutratio.abs() + 0.01), 4))
def cg_f074_dividend_and_payout_valuation_core116_slope_4q_v117_signal(dps, dividends, divyield, payoutratio):
    return _clean(_slope(divyield * payoutratio, 4))
def cg_f074_dividend_and_payout_valuation_core117_slope_4q_v118_signal(dps, dividends, divyield, payoutratio):
    return _clean(_slope(dps * payoutratio, 4))
def cg_f074_dividend_and_payout_valuation_core118_slope_4q_v119_signal(dps, dividends, divyield, payoutratio):
    return _clean(_slope(_safe_div(divyield, payoutratio.abs() + 0.01), 4))
def cg_f074_dividend_and_payout_valuation_core119_slope_4q_v120_signal(dps, dividends, divyield, payoutratio):
    return _clean(_slope(_safe_div(dps, payoutratio.abs() + 0.01), 4))

# core120-129: ewm 8q
def cg_f074_dividend_and_payout_valuation_core120_ewm_8q_v121_signal(dps, dividends, divyield, payoutratio):
    return _clean(_ewm(dps, 8))
def cg_f074_dividend_and_payout_valuation_core121_ewm_8q_v122_signal(dps, dividends, divyield, payoutratio):
    return _clean(_ewm(dividends, 8))
def cg_f074_dividend_and_payout_valuation_core122_ewm_8q_v123_signal(dps, dividends, divyield, payoutratio):
    return _clean(_ewm(divyield, 8))
def cg_f074_dividend_and_payout_valuation_core123_ewm_8q_v124_signal(dps, dividends, divyield, payoutratio):
    return _clean(_ewm(payoutratio, 8))
def cg_f074_dividend_and_payout_valuation_core124_ewm_8q_v125_signal(dps, dividends, divyield, payoutratio):
    return _clean(_ewm(_safe_div(dps, divyield.abs() + 0.001), 8))
def cg_f074_dividend_and_payout_valuation_core125_ewm_8q_v126_signal(dps, dividends, divyield, payoutratio):
    return _clean(_ewm(_safe_div(dividends, payoutratio.abs() + 0.01), 8))
def cg_f074_dividend_and_payout_valuation_core126_ewm_8q_v127_signal(dps, dividends, divyield, payoutratio):
    return _clean(_ewm(divyield * payoutratio, 8))
def cg_f074_dividend_and_payout_valuation_core127_ewm_8q_v128_signal(dps, dividends, divyield, payoutratio):
    return _clean(_ewm(dps * payoutratio, 8))
def cg_f074_dividend_and_payout_valuation_core128_ewm_8q_v129_signal(dps, dividends, divyield, payoutratio):
    return _clean(_ewm(_safe_div(divyield, payoutratio.abs() + 0.01), 8))
def cg_f074_dividend_and_payout_valuation_core129_ewm_8q_v130_signal(dps, dividends, divyield, payoutratio):
    return _clean(_ewm(_safe_div(dps, payoutratio.abs() + 0.01), 8))

# core130-139: stability 12q
def cg_f074_dividend_and_payout_valuation_core130_stability_12q_v131_signal(dps, dividends, divyield, payoutratio):
    return _clean(_safe_div(_std(dps, 12), _mean(dps, 12)))
def cg_f074_dividend_and_payout_valuation_core131_stability_12q_v132_signal(dps, dividends, divyield, payoutratio):
    base = dividends
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f074_dividend_and_payout_valuation_core132_stability_12q_v133_signal(dps, dividends, divyield, payoutratio):
    base = divyield
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f074_dividend_and_payout_valuation_core133_stability_12q_v134_signal(dps, dividends, divyield, payoutratio):
    base = payoutratio
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f074_dividend_and_payout_valuation_core134_stability_12q_v135_signal(dps, dividends, divyield, payoutratio):
    base = _safe_div(dps, divyield.abs() + 0.001)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f074_dividend_and_payout_valuation_core135_stability_12q_v136_signal(dps, dividends, divyield, payoutratio):
    base = _safe_div(dividends, payoutratio.abs() + 0.01)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f074_dividend_and_payout_valuation_core136_stability_12q_v137_signal(dps, dividends, divyield, payoutratio):
    base = divyield * payoutratio
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f074_dividend_and_payout_valuation_core137_stability_12q_v138_signal(dps, dividends, divyield, payoutratio):
    base = dps * payoutratio
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f074_dividend_and_payout_valuation_core138_stability_12q_v139_signal(dps, dividends, divyield, payoutratio):
    base = _safe_div(divyield, payoutratio.abs() + 0.01)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f074_dividend_and_payout_valuation_core139_stability_12q_v140_signal(dps, dividends, divyield, payoutratio):
    base = _safe_div(dps, payoutratio.abs() + 0.01)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))

# core140-149: level
def cg_f074_dividend_and_payout_valuation_core140_dps_v141_signal(dps, dividends, divyield, payoutratio):
    return _clean(dps)
def cg_f074_dividend_and_payout_valuation_core141_dividends_v142_signal(dps, dividends, divyield, payoutratio):
    return _clean(dividends)
def cg_f074_dividend_and_payout_valuation_core142_divyield_v143_signal(dps, dividends, divyield, payoutratio):
    return _clean(divyield)
def cg_f074_dividend_and_payout_valuation_core143_payoutratio_v144_signal(dps, dividends, divyield, payoutratio):
    return _clean(payoutratio)
def cg_f074_dividend_and_payout_valuation_core144_dps_to_yield_v145_signal(dps, dividends, divyield, payoutratio):
    return _clean(_safe_div(dps, divyield.abs() + 0.001))
def cg_f074_dividend_and_payout_valuation_core145_div_to_payout_v146_signal(dps, dividends, divyield, payoutratio):
    return _clean(_safe_div(dividends, payoutratio.abs() + 0.01))
def cg_f074_dividend_and_payout_valuation_core146_yield_times_payout_v147_signal(dps, dividends, divyield, payoutratio):
    return _clean(divyield * payoutratio)
def cg_f074_dividend_and_payout_valuation_core147_dps_times_payout_v148_signal(dps, dividends, divyield, payoutratio):
    return _clean(dps * payoutratio)
def cg_f074_dividend_and_payout_valuation_core148_yield_to_payout_v149_signal(dps, dividends, divyield, payoutratio):
    return _clean(_safe_div(divyield, payoutratio.abs() + 0.01))
def cg_f074_dividend_and_payout_valuation_core149_dps_to_payout_v150_signal(dps, dividends, divyield, payoutratio):
    return _clean(_safe_div(dps, payoutratio.abs() + 0.01))
