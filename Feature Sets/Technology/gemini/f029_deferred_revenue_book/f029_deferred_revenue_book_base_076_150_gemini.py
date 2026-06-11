import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f029_deferred_revenue_book_core75_pct_4q_v076_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(deferredrev, sharesbas), 4))
def cg_f029_deferred_revenue_book_core76_pct_4q_v077_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(revenue + _diff(deferredrev, 4), revenue), 4))
def cg_f029_deferred_revenue_book_core77_pct_4q_v078_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(deferredrev, opex.abs() + 1.0), 4))
def cg_f029_deferred_revenue_book_core78_pct_4q_v079_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(deferredrev, fcf.abs() + 1.0), 4))
def cg_f029_deferred_revenue_book_core79_pct_4q_v080_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_log(deferredrev.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f029_deferred_revenue_book_core80_std_8q_v081_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_std(_safe_div(deferredrev, revenue), 8))
def cg_f029_deferred_revenue_book_core81_std_8q_v082_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_std(_safe_div(_diff(deferredrev, 4), revenue), 8))
def cg_f029_deferred_revenue_book_core82_std_8q_v083_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_std(_safe_div(deferredrev, assets), 8))
def cg_f029_deferred_revenue_book_core83_std_8q_v084_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_std(_safe_div(deferredrev, marketcap), 8))
def cg_f029_deferred_revenue_book_core84_std_8q_v085_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_std(_safe_div(deferredrev, sharesbas), 8))
def cg_f029_deferred_revenue_book_core85_std_8q_v086_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_std(_safe_div(revenue + _diff(deferredrev, 4), revenue), 8))
def cg_f029_deferred_revenue_book_core86_std_8q_v087_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_std(_safe_div(deferredrev, opex.abs() + 1.0), 8))
def cg_f029_deferred_revenue_book_core87_std_8q_v088_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_std(_safe_div(deferredrev, fcf.abs() + 1.0), 8))
def cg_f029_deferred_revenue_book_core88_std_8q_v089_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_std(deferredrev, 8))
def cg_f029_deferred_revenue_book_core89_std_8q_v090_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_std(_log(deferredrev.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f029_deferred_revenue_book_core90_log_v091_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_log(deferredrev.clip(lower=1.0)))
def cg_f029_deferred_revenue_book_core91_log_v092_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_log(_safe_div(deferredrev, revenue).clip(lower=0.001)))
def cg_f029_deferred_revenue_book_core92_log_v093_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_log(_safe_div(_diff(deferredrev, 4), revenue).abs().clip(lower=0.001)))
def cg_f029_deferred_revenue_book_core93_log_v094_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_log(_safe_div(deferredrev, assets).clip(lower=0.001)))
def cg_f029_deferred_revenue_book_core94_log_v095_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_log(_safe_div(deferredrev, marketcap).clip(lower=0.001)))
def cg_f029_deferred_revenue_book_core95_log_v096_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_log(_safe_div(deferredrev, sharesbas).clip(lower=0.001)))
def cg_f029_deferred_revenue_book_core96_log_v097_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_log(_safe_div(revenue + _diff(deferredrev, 4), revenue).clip(lower=0.001)))
def cg_f029_deferred_revenue_book_core97_log_v098_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_log(_safe_div(deferredrev, opex.abs() + 1.0).clip(lower=0.001)))
def cg_f029_deferred_revenue_book_core98_log_v099_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_log(_safe_div(deferredrev, fcf.abs() + 1.0).clip(lower=0.001)))
def cg_f029_deferred_revenue_book_core99_log_v100_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_log(revenue.clip(lower=1.0)))

# Block 100-109: diff 1q
def cg_f029_deferred_revenue_book_core100_diff_1q_v101_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_diff(_safe_div(deferredrev, revenue), 1))
def cg_f029_deferred_revenue_book_core101_diff_1q_v102_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_diff(_safe_div(_diff(deferredrev, 4), revenue), 1))
def cg_f029_deferred_revenue_book_core102_diff_1q_v103_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_diff(_safe_div(deferredrev, assets), 1))
def cg_f029_deferred_revenue_book_core103_diff_1q_v104_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_diff(_safe_div(deferredrev, marketcap), 1))
def cg_f029_deferred_revenue_book_core104_diff_1q_v105_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_diff(_safe_div(deferredrev, sharesbas), 1))
def cg_f029_deferred_revenue_book_core105_diff_1q_v106_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_diff(_safe_div(revenue + _diff(deferredrev, 4), revenue), 1))
def cg_f029_deferred_revenue_book_core106_diff_1q_v107_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_diff(_safe_div(deferredrev, opex.abs() + 1.0), 1))
def cg_f029_deferred_revenue_book_core107_diff_1q_v108_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_diff(_safe_div(deferredrev, fcf.abs() + 1.0), 1))
def cg_f029_deferred_revenue_book_core108_diff_1q_v109_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_diff(deferredrev, 1))
def cg_f029_deferred_revenue_book_core109_diff_1q_v110_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_diff(_log(deferredrev.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f029_deferred_revenue_book_core110_slope_4q_v111_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_slope(_safe_div(deferredrev, revenue), 4))
def cg_f029_deferred_revenue_book_core111_slope_4q_v112_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_slope(_safe_div(_diff(deferredrev, 4), revenue), 4))
def cg_f029_deferred_revenue_book_core112_slope_4q_v113_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_slope(_safe_div(deferredrev, assets), 4))
def cg_f029_deferred_revenue_book_core113_slope_4q_v114_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_slope(_safe_div(deferredrev, marketcap), 4))
def cg_f029_deferred_revenue_book_core114_slope_4q_v115_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_slope(_safe_div(deferredrev, sharesbas), 4))
def cg_f029_deferred_revenue_book_core115_slope_4q_v116_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_slope(_safe_div(revenue + _diff(deferredrev, 4), revenue), 4))
def cg_f029_deferred_revenue_book_core116_slope_4q_v117_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_slope(_safe_div(deferredrev, opex.abs() + 1.0), 4))
def cg_f029_deferred_revenue_book_core117_slope_4q_v118_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_slope(_safe_div(deferredrev, fcf.abs() + 1.0), 4))
def cg_f029_deferred_revenue_book_core118_slope_4q_v119_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_slope(deferredrev, 4))
def cg_f029_deferred_revenue_book_core119_slope_4q_v120_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_slope(_log(deferredrev.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f029_deferred_revenue_book_core120_ewm_8q_v121_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_ewm(_safe_div(deferredrev, revenue), 8))
def cg_f029_deferred_revenue_book_core121_ewm_8q_v122_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_ewm(_safe_div(_diff(deferredrev, 4), revenue), 8))
def cg_f029_deferred_revenue_book_core122_ewm_8q_v123_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_ewm(_safe_div(deferredrev, assets), 8))
def cg_f029_deferred_revenue_book_core123_ewm_8q_v124_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_ewm(_safe_div(deferredrev, marketcap), 8))
def cg_f029_deferred_revenue_book_core124_ewm_8q_v125_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_ewm(_safe_div(deferredrev, sharesbas), 8))
def cg_f029_deferred_revenue_book_core125_ewm_8q_v126_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_ewm(_safe_div(revenue + _diff(deferredrev, 4), revenue), 8))
def cg_f029_deferred_revenue_book_core126_ewm_8q_v127_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_ewm(_safe_div(deferredrev, opex.abs() + 1.0), 8))
def cg_f029_deferred_revenue_book_core127_ewm_8q_v128_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_ewm(_safe_div(deferredrev, fcf.abs() + 1.0), 8))
def cg_f029_deferred_revenue_book_core128_ewm_8q_v129_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_ewm(deferredrev, 8))
def cg_f029_deferred_revenue_book_core129_ewm_8q_v130_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_ewm(_log(deferredrev.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f029_deferred_revenue_book_core130_stability_12q_v131_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    base = _safe_div(deferredrev, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f029_deferred_revenue_book_core131_stability_12q_v132_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    base = _safe_div(_diff(deferredrev, 4), revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f029_deferred_revenue_book_core132_stability_12q_v133_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    base = _safe_div(deferredrev, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f029_deferred_revenue_book_core133_stability_12q_v134_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    base = _safe_div(deferredrev, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f029_deferred_revenue_book_core134_stability_12q_v135_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    base = _safe_div(deferredrev, sharesbas)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f029_deferred_revenue_book_core135_stability_12q_v136_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    base = _safe_div(revenue + _diff(deferredrev, 4), revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f029_deferred_revenue_book_core136_stability_12q_v137_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    base = _safe_div(deferredrev, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f029_deferred_revenue_book_core137_stability_12q_v138_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    base = _safe_div(deferredrev, fcf.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f029_deferred_revenue_book_core138_stability_12q_v139_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    base = deferredrev
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f029_deferred_revenue_book_core139_stability_12q_v140_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    base = _log(deferredrev.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f029_deferred_revenue_book_core140_dr_v141_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(deferredrev)
def cg_f029_deferred_revenue_book_core141_dr_rev_v142_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_safe_div(deferredrev, revenue))
def cg_f029_deferred_revenue_book_core142_dr_growth_v143_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_safe_div(_diff(deferredrev, 4), revenue))
def cg_f029_deferred_revenue_book_core143_dr_assets_v144_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_safe_div(deferredrev, assets))
def cg_f029_deferred_revenue_book_core144_dr_mcap_v145_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_safe_div(deferredrev, marketcap))
def cg_f029_deferred_revenue_book_core145_dr_shares_v146_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_safe_div(deferredrev, sharesbas))
def cg_f029_deferred_revenue_book_core146_true_growth_v147_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_safe_div(revenue + _diff(deferredrev, 4), revenue))
def cg_f029_deferred_revenue_book_core147_dr_opex_v148_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_safe_div(deferredrev, opex.abs() + 1.0))
def cg_f029_deferred_revenue_book_core148_dr_fcf_v149_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_safe_div(deferredrev, fcf.abs() + 1.0))
def cg_f029_deferred_revenue_book_core149_dr_log_v150_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_log(deferredrev.clip(lower=1.0)))
