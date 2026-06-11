import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f071_price_book_valuation_core75_pct_4q_v076_signal(marketcap, equity, bvps, tbvps):
    return _clean(_pct_change(_safe_div(marketcap, equity.abs() + 1.0), 4))
def cg_f071_price_book_valuation_core76_pct_4q_v077_signal(marketcap, equity, bvps, tbvps):
    return _clean(_pct_change(marketcap - equity, 4))
def cg_f071_price_book_valuation_core77_pct_4q_v078_signal(marketcap, equity, bvps, tbvps):
    return _clean(_pct_change(_safe_div(marketcap - equity, equity.abs() + 1.0), 4))
def cg_f071_price_book_valuation_core78_pct_4q_v079_signal(marketcap, equity, bvps, tbvps):
    return _clean(_pct_change(_safe_div(bvps, tbvps.abs() + 0.01), 4))
def cg_f071_price_book_valuation_core79_pct_4q_v080_signal(marketcap, equity, bvps, tbvps):
    return _clean(_pct_change(_safe_div(equity, marketcap.abs() + 1.0), 4))

# core80-89: std 8q
def cg_f071_price_book_valuation_core80_std_8q_v081_signal(marketcap, equity, bvps, tbvps):
    return _clean(_std(marketcap, 8))
def cg_f071_price_book_valuation_core81_std_8q_v082_signal(marketcap, equity, bvps, tbvps):
    return _clean(_std(_safe_div(marketcap, equity), 8))
def cg_f071_price_book_valuation_core82_std_8q_v083_signal(marketcap, equity, bvps, tbvps):
    return _clean(_std(equity, 8))
def cg_f071_price_book_valuation_core83_std_8q_v084_signal(marketcap, equity, bvps, tbvps):
    return _clean(_std(bvps, 8))
def cg_f071_price_book_valuation_core84_std_8q_v085_signal(marketcap, equity, bvps, tbvps):
    return _clean(_std(tbvps, 8))
def cg_f071_price_book_valuation_core85_std_8q_v086_signal(marketcap, equity, bvps, tbvps):
    return _clean(_std(_safe_div(marketcap, equity.abs() + 1.0), 8))
def cg_f071_price_book_valuation_core86_std_8q_v087_signal(marketcap, equity, bvps, tbvps):
    return _clean(_std(marketcap - equity, 8))
def cg_f071_price_book_valuation_core87_std_8q_v088_signal(marketcap, equity, bvps, tbvps):
    return _clean(_std(_safe_div(marketcap - equity, equity.abs() + 1.0), 8))
def cg_f071_price_book_valuation_core88_std_8q_v089_signal(marketcap, equity, bvps, tbvps):
    return _clean(_std(_safe_div(bvps, tbvps.abs() + 0.01), 8))
def cg_f071_price_book_valuation_core89_std_8q_v090_signal(marketcap, equity, bvps, tbvps):
    return _clean(_std(_safe_div(equity, marketcap.abs() + 1.0), 8))

# core90-99: log
def cg_f071_price_book_valuation_core90_log_v091_signal(marketcap, equity, bvps, tbvps):
    return _clean(_log(marketcap.clip(lower=1.0)))
def cg_f071_price_book_valuation_core91_log_v092_signal(marketcap, equity, bvps, tbvps):
    return _clean(_log(_safe_div(marketcap, equity).clip(lower=0.001)))
def cg_f071_price_book_valuation_core92_log_v093_signal(marketcap, equity, bvps, tbvps):
    return _clean(_log(equity.clip(lower=1.0)))
def cg_f071_price_book_valuation_core93_log_v094_signal(marketcap, equity, bvps, tbvps):
    return _clean(_log(bvps.clip(lower=0.001)))
def cg_f071_price_book_valuation_core94_log_v095_signal(marketcap, equity, bvps, tbvps):
    return _clean(_log(tbvps.clip(lower=0.001)))
def cg_f071_price_book_valuation_core95_log_v096_signal(marketcap, equity, bvps, tbvps):
    return _clean(_log(_safe_div(marketcap, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f071_price_book_valuation_core96_log_v097_signal(marketcap, equity, bvps, tbvps):
    return _clean(_log((marketcap - equity).clip(lower=1.0)))
def cg_f071_price_book_valuation_core97_log_v098_signal(marketcap, equity, bvps, tbvps):
    return _clean(_log(_safe_div(marketcap - equity, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f071_price_book_valuation_core98_log_v099_signal(marketcap, equity, bvps, tbvps):
    return _clean(_log(_safe_div(bvps, tbvps.abs() + 0.01).clip(lower=0.001)))
def cg_f071_price_book_valuation_core99_log_v100_signal(marketcap, equity, bvps, tbvps):
    return _clean(_log(_safe_div(equity, marketcap.abs() + 1.0).clip(lower=0.001)))

# core100-109: diff 1q
def cg_f071_price_book_valuation_core100_diff_1q_v101_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(marketcap, 1))
def cg_f071_price_book_valuation_core101_diff_1q_v102_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_safe_div(marketcap, equity), 1))
def cg_f071_price_book_valuation_core102_diff_1q_v103_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(equity, 1))
def cg_f071_price_book_valuation_core103_diff_1q_v104_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(bvps, 1))
def cg_f071_price_book_valuation_core104_diff_1q_v105_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(tbvps, 1))
def cg_f071_price_book_valuation_core105_diff_1q_v106_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_safe_div(marketcap, equity.abs() + 1.0), 1))
def cg_f071_price_book_valuation_core106_diff_1q_v107_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(marketcap - equity, 1))
def cg_f071_price_book_valuation_core107_diff_1q_v108_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_safe_div(marketcap - equity, equity.abs() + 1.0), 1))
def cg_f071_price_book_valuation_core108_diff_1q_v109_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_safe_div(bvps, tbvps.abs() + 0.01), 1))
def cg_f071_price_book_valuation_core109_diff_1q_v110_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_safe_div(equity, marketcap.abs() + 1.0), 1))

# core110-119: slope 4q
def cg_f071_price_book_valuation_core110_slope_4q_v111_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(marketcap, 4))
def cg_f071_price_book_valuation_core111_slope_4q_v112_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_safe_div(marketcap, equity), 4))
def cg_f071_price_book_valuation_core112_slope_4q_v113_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(equity, 4))
def cg_f071_price_book_valuation_core113_slope_4q_v114_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(bvps, 4))
def cg_f071_price_book_valuation_core114_slope_4q_v115_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(tbvps, 4))
def cg_f071_price_book_valuation_core115_slope_4q_v116_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_safe_div(marketcap, equity.abs() + 1.0), 4))
def cg_f071_price_book_valuation_core116_slope_4q_v117_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(marketcap - equity, 4))
def cg_f071_price_book_valuation_core117_slope_4q_v118_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_safe_div(marketcap - equity, equity.abs() + 1.0), 4))
def cg_f071_price_book_valuation_core118_slope_4q_v119_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_safe_div(bvps, tbvps.abs() + 0.01), 4))
def cg_f071_price_book_valuation_core119_slope_4q_v120_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_safe_div(equity, marketcap.abs() + 1.0), 4))

# core120-129: ewm 8q
def cg_f071_price_book_valuation_core120_ewm_8q_v121_signal(marketcap, equity, bvps, tbvps):
    return _clean(_ewm(marketcap, 8))
def cg_f071_price_book_valuation_core121_ewm_8q_v122_signal(marketcap, equity, bvps, tbvps):
    return _clean(_ewm(_safe_div(marketcap, equity), 8))
def cg_f071_price_book_valuation_core122_ewm_8q_v123_signal(marketcap, equity, bvps, tbvps):
    return _clean(_ewm(equity, 8))
def cg_f071_price_book_valuation_core123_ewm_8q_v124_signal(marketcap, equity, bvps, tbvps):
    return _clean(_ewm(bvps, 8))
def cg_f071_price_book_valuation_core124_ewm_8q_v125_signal(marketcap, equity, bvps, tbvps):
    return _clean(_ewm(tbvps, 8))
def cg_f071_price_book_valuation_core125_ewm_8q_v126_signal(marketcap, equity, bvps, tbvps):
    return _clean(_ewm(_safe_div(marketcap, equity.abs() + 1.0), 8))
def cg_f071_price_book_valuation_core126_ewm_8q_v127_signal(marketcap, equity, bvps, tbvps):
    return _clean(_ewm(marketcap - equity, 8))
def cg_f071_price_book_valuation_core127_ewm_8q_v128_signal(marketcap, equity, bvps, tbvps):
    return _clean(_ewm(_safe_div(marketcap - equity, equity.abs() + 1.0), 8))
def cg_f071_price_book_valuation_core128_ewm_8q_v129_signal(marketcap, equity, bvps, tbvps):
    return _clean(_ewm(_safe_div(bvps, tbvps.abs() + 0.01), 8))
def cg_f071_price_book_valuation_core129_ewm_8q_v130_signal(marketcap, equity, bvps, tbvps):
    return _clean(_ewm(_safe_div(equity, marketcap.abs() + 1.0), 8))

# core130-139: stability 12q
def cg_f071_price_book_valuation_core130_stability_12q_v131_signal(marketcap, equity, bvps, tbvps):
    return _clean(_safe_div(_std(marketcap, 12), _mean(marketcap, 12)))
def cg_f071_price_book_valuation_core131_stability_12q_v132_signal(marketcap, equity, bvps, tbvps):
    base = _safe_div(marketcap, equity)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f071_price_book_valuation_core132_stability_12q_v133_signal(marketcap, equity, bvps, tbvps):
    base = equity
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f071_price_book_valuation_core133_stability_12q_v134_signal(marketcap, equity, bvps, tbvps):
    base = bvps
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f071_price_book_valuation_core134_stability_12q_v135_signal(marketcap, equity, bvps, tbvps):
    base = tbvps
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f071_price_book_valuation_core135_stability_12q_v136_signal(marketcap, equity, bvps, tbvps):
    base = _safe_div(marketcap, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f071_price_book_valuation_core136_stability_12q_v137_signal(marketcap, equity, bvps, tbvps):
    base = marketcap - equity
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f071_price_book_valuation_core137_stability_12q_v138_signal(marketcap, equity, bvps, tbvps):
    base = _safe_div(marketcap - equity, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f071_price_book_valuation_core138_stability_12q_v139_signal(marketcap, equity, bvps, tbvps):
    base = _safe_div(bvps, tbvps.abs() + 0.01)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))
def cg_f071_price_book_valuation_core139_stability_12q_v140_signal(marketcap, equity, bvps, tbvps):
    base = _safe_div(equity, marketcap.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12)))

# core140-149: level
def cg_f071_price_book_valuation_core140_level_v141_signal(marketcap, equity, bvps, tbvps):
    return _clean(marketcap)
def cg_f071_price_book_valuation_core141_pb_v142_signal(marketcap, equity, bvps, tbvps):
    return _clean(_safe_div(marketcap, equity))
def cg_f071_price_book_valuation_core142_equity_v143_signal(marketcap, equity, bvps, tbvps):
    return _clean(equity)
def cg_f071_price_book_valuation_core143_bvps_v144_signal(marketcap, equity, bvps, tbvps):
    return _clean(bvps)
def cg_f071_price_book_valuation_core144_tbvps_v145_signal(marketcap, equity, bvps, tbvps):
    return _clean(tbvps)
def cg_f071_price_book_valuation_core145_to_equity_abs_v146_signal(marketcap, equity, bvps, tbvps):
    return _clean(_safe_div(marketcap, equity.abs() + 1.0))
def cg_f071_price_book_valuation_core146_marketcap_minus_equity_v147_signal(marketcap, equity, bvps, tbvps):
    return _clean(marketcap - equity)
def cg_f071_price_book_valuation_core147_marketcap_minus_equity_to_equity_v148_signal(marketcap, equity, bvps, tbvps):
    return _clean(_safe_div(marketcap - equity, equity.abs() + 1.0))
def cg_f071_price_book_valuation_core148_bvps_to_tbvps_v149_signal(marketcap, equity, bvps, tbvps):
    return _clean(_safe_div(bvps, tbvps.abs() + 0.01))
def cg_f071_price_book_valuation_core149_equity_to_marketcap_v150_signal(marketcap, equity, bvps, tbvps):
    return _clean(_safe_div(equity, marketcap.abs() + 1.0))
