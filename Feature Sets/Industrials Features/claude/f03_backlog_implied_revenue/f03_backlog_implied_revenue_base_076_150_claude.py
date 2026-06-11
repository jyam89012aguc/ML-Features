import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)

# ===== folder domain primitives =====
def _f03_revenue_smoothed(revenue, w):
    return revenue.rolling(w, min_periods=max(1, w // 2)).mean()


def _f03_revenue_growth_persistence(revenue, w):
    g = revenue.pct_change(periods=w)
    return g.rolling(w, min_periods=max(1, w // 2)).mean()


def _f03_deferred_rev_pulse(deferredrev, revenue, w):
    ratio = deferredrev / revenue.replace(0, np.nan).abs()
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()

def f03bir_f03_backlog_implied_revenue_rsmxrgp_252d_base_v076_signal(revenue, closeadj):
    a = _f03_revenue_smoothed(revenue, 252)
    b = _f03_revenue_growth_persistence(revenue, 252)
    result = (a / 1e9) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxdrp_21d_base_v077_signal(revenue, deferredrev, closeadj):
    a = _f03_revenue_smoothed(revenue, 21)
    b = _f03_deferred_rev_pulse(deferredrev, revenue, 21)
    result = (a / 1e9) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxdrp_63d_base_v078_signal(revenue, deferredrev, closeadj):
    a = _f03_revenue_smoothed(revenue, 63)
    b = _f03_deferred_rev_pulse(deferredrev, revenue, 63)
    result = (a / 1e9) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxdrp_126d_base_v079_signal(revenue, deferredrev, closeadj):
    a = _f03_revenue_smoothed(revenue, 126)
    b = _f03_deferred_rev_pulse(deferredrev, revenue, 126)
    result = (a / 1e9) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxdrp_252d_base_v080_signal(revenue, deferredrev, closeadj):
    a = _f03_revenue_smoothed(revenue, 252)
    b = _f03_deferred_rev_pulse(deferredrev, revenue, 252)
    result = (a / 1e9) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpxdrp_21d_base_v081_signal(revenue, deferredrev, closeadj):
    a = _f03_revenue_growth_persistence(revenue, 21)
    b = _f03_deferred_rev_pulse(deferredrev, revenue, 21)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpxdrp_63d_base_v082_signal(revenue, deferredrev, closeadj):
    a = _f03_revenue_growth_persistence(revenue, 63)
    b = _f03_deferred_rev_pulse(deferredrev, revenue, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpxdrp_126d_base_v083_signal(revenue, deferredrev, closeadj):
    a = _f03_revenue_growth_persistence(revenue, 126)
    b = _f03_deferred_rev_pulse(deferredrev, revenue, 126)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpxdrp_252d_base_v084_signal(revenue, deferredrev, closeadj):
    a = _f03_revenue_growth_persistence(revenue, 252)
    b = _f03_deferred_rev_pulse(deferredrev, revenue, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_trio_21d_base_v085_signal(revenue, deferredrev, closeadj):
    a = _f03_revenue_smoothed(revenue, 21)
    b = _f03_revenue_growth_persistence(revenue, 21)
    c = _f03_deferred_rev_pulse(deferredrev, revenue, 21)
    result = ((a / 1e9) + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_trio_63d_base_v086_signal(revenue, deferredrev, closeadj):
    a = _f03_revenue_smoothed(revenue, 63)
    b = _f03_revenue_growth_persistence(revenue, 63)
    c = _f03_deferred_rev_pulse(deferredrev, revenue, 63)
    result = ((a / 1e9) + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_trio_126d_base_v087_signal(revenue, deferredrev, closeadj):
    a = _f03_revenue_smoothed(revenue, 126)
    b = _f03_revenue_growth_persistence(revenue, 126)
    c = _f03_deferred_rev_pulse(deferredrev, revenue, 126)
    result = ((a / 1e9) + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_trio_252d_base_v088_signal(revenue, deferredrev, closeadj):
    a = _f03_revenue_smoothed(revenue, 252)
    b = _f03_revenue_growth_persistence(revenue, 252)
    c = _f03_deferred_rev_pulse(deferredrev, revenue, 252)
    result = ((a / 1e9) + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpxret_21d_base_v089_signal(revenue, closeadj):
    a = _f03_revenue_growth_persistence(revenue, 21)
    ret = closeadj.pct_change(21)
    result = a * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpxret_63d_base_v090_signal(revenue, closeadj):
    a = _f03_revenue_growth_persistence(revenue, 63)
    ret = closeadj.pct_change(63)
    result = a * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpxret_126d_base_v091_signal(revenue, closeadj):
    a = _f03_revenue_growth_persistence(revenue, 126)
    ret = closeadj.pct_change(126)
    result = a * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpxvol_21d_base_v092_signal(deferredrev, revenue, closeadj, volume):
    a = _f03_deferred_rev_pulse(deferredrev, revenue, 21)
    result = a * _mean(closeadj * volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpxvol_63d_base_v093_signal(deferredrev, revenue, closeadj, volume):
    a = _f03_deferred_rev_pulse(deferredrev, revenue, 63)
    result = a * _mean(closeadj * volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpxvol_126d_base_v094_signal(deferredrev, revenue, closeadj, volume):
    a = _f03_deferred_rev_pulse(deferredrev, revenue, 126)
    result = a * _mean(closeadj * volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxvol_21d_base_v095_signal(revenue, closeadj, volume):
    a = _f03_revenue_smoothed(revenue, 21)
    result = (a / 1e9) * _mean(closeadj * volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxvol_63d_base_v096_signal(revenue, closeadj, volume):
    a = _f03_revenue_smoothed(revenue, 63)
    result = (a / 1e9) * _mean(closeadj * volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxvol_126d_base_v097_signal(revenue, closeadj, volume):
    a = _f03_revenue_smoothed(revenue, 126)
    result = (a / 1e9) * _mean(closeadj * volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmema_21d_base_v098_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 21)
    result = base.ewm(span=21, min_periods=10).mean() / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmema_63d_base_v099_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 63)
    result = base.ewm(span=63, min_periods=31).mean() / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmema_126d_base_v100_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 126)
    result = base.ewm(span=126, min_periods=63).mean() / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpema_21d_base_v101_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 21)
    result = base.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpema_63d_base_v102_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 63)
    result = base.ewm(span=63, min_periods=31).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpema_126d_base_v103_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 126)
    result = base.ewm(span=126, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpema_21d_base_v104_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 21)
    result = base.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpema_63d_base_v105_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 63)
    result = base.ewm(span=63, min_periods=31).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpema_126d_base_v106_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 126)
    result = base.ewm(span=126, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmsmooth_21d_base_v107_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 21)
    result = _mean(base, 21) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmsmooth_63d_base_v108_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 63)
    result = _mean(base, 63) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmsmooth_126d_base_v109_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 126)
    result = _mean(base, 126) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmsmooth_252d_base_v110_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 252)
    result = _mean(base, 252) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpsmooth_21d_base_v111_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpsmooth_63d_base_v112_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpsmooth_126d_base_v113_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpsmooth_252d_base_v114_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpsmooth_21d_base_v115_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpsmooth_63d_base_v116_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpsmooth_126d_base_v117_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpsmooth_252d_base_v118_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxmcap_21d_base_v119_signal(revenue, marketcap, closeadj):
    a = _f03_revenue_smoothed(revenue, 21)
    result = (a / 1e9) * (marketcap / 1e8) + _f03_revenue_growth_persistence(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxmcap_63d_base_v120_signal(revenue, marketcap, closeadj):
    a = _f03_revenue_smoothed(revenue, 63)
    result = (a / 1e9) * (marketcap / 1e8) + _f03_revenue_growth_persistence(revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxmcap_126d_base_v121_signal(revenue, marketcap, closeadj):
    a = _f03_revenue_smoothed(revenue, 126)
    result = (a / 1e9) * (marketcap / 1e8) + _f03_revenue_growth_persistence(revenue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpxmcap_21d_base_v122_signal(revenue, marketcap, closeadj):
    a = _f03_revenue_growth_persistence(revenue, 21)
    result = a * (marketcap / 1e8) + _f03_revenue_smoothed(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpxmcap_63d_base_v123_signal(revenue, marketcap, closeadj):
    a = _f03_revenue_growth_persistence(revenue, 63)
    result = a * (marketcap / 1e8) + _f03_revenue_smoothed(revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpxmcap_126d_base_v124_signal(revenue, marketcap, closeadj):
    a = _f03_revenue_growth_persistence(revenue, 126)
    result = a * (marketcap / 1e8) + _f03_revenue_smoothed(revenue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxgp_21d_base_v125_signal(revenue, gp, closeadj):
    a = _f03_revenue_smoothed(revenue, 21)
    b = _f03_revenue_smoothed(gp, 21)
    result = (a / 1e9) * (b / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxgp_63d_base_v126_signal(revenue, gp, closeadj):
    a = _f03_revenue_smoothed(revenue, 63)
    b = _f03_revenue_smoothed(gp, 63)
    result = (a / 1e9) * (b / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxgp_126d_base_v127_signal(revenue, gp, closeadj):
    a = _f03_revenue_smoothed(revenue, 126)
    b = _f03_revenue_smoothed(gp, 126)
    result = (a / 1e9) * (b / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxgp_252d_base_v128_signal(revenue, gp, closeadj):
    a = _f03_revenue_smoothed(revenue, 252)
    b = _f03_revenue_smoothed(gp, 252)
    result = (a / 1e9) * (b / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgprev_vs_gp_21d_base_v129_signal(revenue, gp, closeadj):
    a = _f03_revenue_growth_persistence(revenue, 21)
    b = _f03_revenue_growth_persistence(gp, 21)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgprev_vs_gp_63d_base_v130_signal(revenue, gp, closeadj):
    a = _f03_revenue_growth_persistence(revenue, 63)
    b = _f03_revenue_growth_persistence(gp, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgprev_vs_gp_126d_base_v131_signal(revenue, gp, closeadj):
    a = _f03_revenue_growth_persistence(revenue, 126)
    b = _f03_revenue_growth_persistence(gp, 126)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgprev_vs_gp_252d_base_v132_signal(revenue, gp, closeadj):
    a = _f03_revenue_growth_persistence(revenue, 252)
    b = _f03_revenue_growth_persistence(gp, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpebitda_21d_base_v133_signal(ebitda, closeadj):
    base = _f03_revenue_growth_persistence(ebitda, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpebitda_63d_base_v134_signal(ebitda, closeadj):
    base = _f03_revenue_growth_persistence(ebitda, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpebitda_126d_base_v135_signal(ebitda, closeadj):
    base = _f03_revenue_growth_persistence(ebitda, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpebitda_252d_base_v136_signal(ebitda, closeadj):
    base = _f03_revenue_growth_persistence(ebitda, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmgp_21d_base_v137_signal(gp, closeadj):
    base = _f03_revenue_smoothed(gp, 21)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmgp_63d_base_v138_signal(gp, closeadj):
    base = _f03_revenue_smoothed(gp, 63)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmgp_126d_base_v139_signal(gp, closeadj):
    base = _f03_revenue_smoothed(gp, 126)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmgp_252d_base_v140_signal(gp, closeadj):
    base = _f03_revenue_smoothed(gp, 252)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmebit_21d_base_v141_signal(ebit, closeadj):
    base = _f03_revenue_smoothed(ebit, 21)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmebit_63d_base_v142_signal(ebit, closeadj):
    base = _f03_revenue_smoothed(ebit, 63)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmebit_126d_base_v143_signal(ebit, closeadj):
    base = _f03_revenue_smoothed(ebit, 126)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmebit_252d_base_v144_signal(ebit, closeadj):
    base = _f03_revenue_smoothed(ebit, 252)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpdeferred_21d_base_v145_signal(deferredrev, closeadj):
    base = _f03_revenue_growth_persistence(deferredrev, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpdeferred_63d_base_v146_signal(deferredrev, closeadj):
    base = _f03_revenue_growth_persistence(deferredrev, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpdeferred_126d_base_v147_signal(deferredrev, closeadj):
    base = _f03_revenue_growth_persistence(deferredrev, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpdeferred_252d_base_v148_signal(deferredrev, closeadj):
    base = _f03_revenue_growth_persistence(deferredrev, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpxgrow_21d_base_v149_signal(deferredrev, revenue, closeadj):
    a = _f03_deferred_rev_pulse(deferredrev, revenue, 21)
    b = _f03_revenue_growth_persistence(revenue, 21)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpxgrow_63d_base_v150_signal(deferredrev, revenue, closeadj):
    a = _f03_deferred_rev_pulse(deferredrev, revenue, 63)
    b = _f03_revenue_growth_persistence(revenue, 63)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03bir_f03_backlog_implied_revenue_rsmxrgp_252d_base_v076_signal,
    f03bir_f03_backlog_implied_revenue_rsmxdrp_21d_base_v077_signal,
    f03bir_f03_backlog_implied_revenue_rsmxdrp_63d_base_v078_signal,
    f03bir_f03_backlog_implied_revenue_rsmxdrp_126d_base_v079_signal,
    f03bir_f03_backlog_implied_revenue_rsmxdrp_252d_base_v080_signal,
    f03bir_f03_backlog_implied_revenue_rgpxdrp_21d_base_v081_signal,
    f03bir_f03_backlog_implied_revenue_rgpxdrp_63d_base_v082_signal,
    f03bir_f03_backlog_implied_revenue_rgpxdrp_126d_base_v083_signal,
    f03bir_f03_backlog_implied_revenue_rgpxdrp_252d_base_v084_signal,
    f03bir_f03_backlog_implied_revenue_trio_21d_base_v085_signal,
    f03bir_f03_backlog_implied_revenue_trio_63d_base_v086_signal,
    f03bir_f03_backlog_implied_revenue_trio_126d_base_v087_signal,
    f03bir_f03_backlog_implied_revenue_trio_252d_base_v088_signal,
    f03bir_f03_backlog_implied_revenue_rgpxret_21d_base_v089_signal,
    f03bir_f03_backlog_implied_revenue_rgpxret_63d_base_v090_signal,
    f03bir_f03_backlog_implied_revenue_rgpxret_126d_base_v091_signal,
    f03bir_f03_backlog_implied_revenue_drpxvol_21d_base_v092_signal,
    f03bir_f03_backlog_implied_revenue_drpxvol_63d_base_v093_signal,
    f03bir_f03_backlog_implied_revenue_drpxvol_126d_base_v094_signal,
    f03bir_f03_backlog_implied_revenue_rsmxvol_21d_base_v095_signal,
    f03bir_f03_backlog_implied_revenue_rsmxvol_63d_base_v096_signal,
    f03bir_f03_backlog_implied_revenue_rsmxvol_126d_base_v097_signal,
    f03bir_f03_backlog_implied_revenue_rsmema_21d_base_v098_signal,
    f03bir_f03_backlog_implied_revenue_rsmema_63d_base_v099_signal,
    f03bir_f03_backlog_implied_revenue_rsmema_126d_base_v100_signal,
    f03bir_f03_backlog_implied_revenue_rgpema_21d_base_v101_signal,
    f03bir_f03_backlog_implied_revenue_rgpema_63d_base_v102_signal,
    f03bir_f03_backlog_implied_revenue_rgpema_126d_base_v103_signal,
    f03bir_f03_backlog_implied_revenue_drpema_21d_base_v104_signal,
    f03bir_f03_backlog_implied_revenue_drpema_63d_base_v105_signal,
    f03bir_f03_backlog_implied_revenue_drpema_126d_base_v106_signal,
    f03bir_f03_backlog_implied_revenue_rsmsmooth_21d_base_v107_signal,
    f03bir_f03_backlog_implied_revenue_rsmsmooth_63d_base_v108_signal,
    f03bir_f03_backlog_implied_revenue_rsmsmooth_126d_base_v109_signal,
    f03bir_f03_backlog_implied_revenue_rsmsmooth_252d_base_v110_signal,
    f03bir_f03_backlog_implied_revenue_rgpsmooth_21d_base_v111_signal,
    f03bir_f03_backlog_implied_revenue_rgpsmooth_63d_base_v112_signal,
    f03bir_f03_backlog_implied_revenue_rgpsmooth_126d_base_v113_signal,
    f03bir_f03_backlog_implied_revenue_rgpsmooth_252d_base_v114_signal,
    f03bir_f03_backlog_implied_revenue_drpsmooth_21d_base_v115_signal,
    f03bir_f03_backlog_implied_revenue_drpsmooth_63d_base_v116_signal,
    f03bir_f03_backlog_implied_revenue_drpsmooth_126d_base_v117_signal,
    f03bir_f03_backlog_implied_revenue_drpsmooth_252d_base_v118_signal,
    f03bir_f03_backlog_implied_revenue_rsmxmcap_21d_base_v119_signal,
    f03bir_f03_backlog_implied_revenue_rsmxmcap_63d_base_v120_signal,
    f03bir_f03_backlog_implied_revenue_rsmxmcap_126d_base_v121_signal,
    f03bir_f03_backlog_implied_revenue_rgpxmcap_21d_base_v122_signal,
    f03bir_f03_backlog_implied_revenue_rgpxmcap_63d_base_v123_signal,
    f03bir_f03_backlog_implied_revenue_rgpxmcap_126d_base_v124_signal,
    f03bir_f03_backlog_implied_revenue_rsmxgp_21d_base_v125_signal,
    f03bir_f03_backlog_implied_revenue_rsmxgp_63d_base_v126_signal,
    f03bir_f03_backlog_implied_revenue_rsmxgp_126d_base_v127_signal,
    f03bir_f03_backlog_implied_revenue_rsmxgp_252d_base_v128_signal,
    f03bir_f03_backlog_implied_revenue_rgprev_vs_gp_21d_base_v129_signal,
    f03bir_f03_backlog_implied_revenue_rgprev_vs_gp_63d_base_v130_signal,
    f03bir_f03_backlog_implied_revenue_rgprev_vs_gp_126d_base_v131_signal,
    f03bir_f03_backlog_implied_revenue_rgprev_vs_gp_252d_base_v132_signal,
    f03bir_f03_backlog_implied_revenue_rgpebitda_21d_base_v133_signal,
    f03bir_f03_backlog_implied_revenue_rgpebitda_63d_base_v134_signal,
    f03bir_f03_backlog_implied_revenue_rgpebitda_126d_base_v135_signal,
    f03bir_f03_backlog_implied_revenue_rgpebitda_252d_base_v136_signal,
    f03bir_f03_backlog_implied_revenue_rsmgp_21d_base_v137_signal,
    f03bir_f03_backlog_implied_revenue_rsmgp_63d_base_v138_signal,
    f03bir_f03_backlog_implied_revenue_rsmgp_126d_base_v139_signal,
    f03bir_f03_backlog_implied_revenue_rsmgp_252d_base_v140_signal,
    f03bir_f03_backlog_implied_revenue_rsmebit_21d_base_v141_signal,
    f03bir_f03_backlog_implied_revenue_rsmebit_63d_base_v142_signal,
    f03bir_f03_backlog_implied_revenue_rsmebit_126d_base_v143_signal,
    f03bir_f03_backlog_implied_revenue_rsmebit_252d_base_v144_signal,
    f03bir_f03_backlog_implied_revenue_rgpdeferred_21d_base_v145_signal,
    f03bir_f03_backlog_implied_revenue_rgpdeferred_63d_base_v146_signal,
    f03bir_f03_backlog_implied_revenue_rgpdeferred_126d_base_v147_signal,
    f03bir_f03_backlog_implied_revenue_rgpdeferred_252d_base_v148_signal,
    f03bir_f03_backlog_implied_revenue_drpxgrow_21d_base_v149_signal,
    f03bir_f03_backlog_implied_revenue_drpxgrow_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_BACKLOG_IMPLIED_REVENUE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f03_revenue_smoothed', '_f03_revenue_growth_persistence', '_f03_deferred_rev_pulse')
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f03_backlog_implied_revenue_base_076_150_claude: {n_features} features pass")
