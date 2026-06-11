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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f050_rev_to_ocf(revenue, ncfo):
    return revenue / ncfo.replace(0, np.nan).abs()


# 63d z-score of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_z_63d_base_v076_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_z_126d_base_v077_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_z_252d_base_v078_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_z_504d_base_v079_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_z_63d_base_v080_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_z_126d_base_v081_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_z_252d_base_v082_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_z_504d_base_v083_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_z_63d_base_v084_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_z_126d_base_v085_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_z_252d_base_v086_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_z_504d_base_v087_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_z_63d_base_v088_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_z_126d_base_v089_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_z_252d_base_v090_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_z_504d_base_v091_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_z_63d_base_v092_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_z_126d_base_v093_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_z_252d_base_v094_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_z_504d_base_v095_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_z_63d_base_v096_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_z_126d_base_v097_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_z_252d_base_v098_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_z_504d_base_v099_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_z_63d_base_v100_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_z_126d_base_v101_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_z_252d_base_v102_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_z_504d_base_v103_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_distmax_252d_base_v104_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_distmax_504d_base_v105_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_distmax_252d_base_v106_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_distmax_504d_base_v107_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_distmax_252d_base_v108_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_distmax_504d_base_v109_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_distmax_252d_base_v110_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_distmax_504d_base_v111_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_distmax_252d_base_v112_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_distmax_504d_base_v113_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_distmax_252d_base_v114_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_distmax_504d_base_v115_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_distmax_252d_base_v116_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_distmax_504d_base_v117_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_distmed_126d_base_v118_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_distmed_252d_base_v119_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_distmed_504d_base_v120_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_distmed_126d_base_v121_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_distmed_252d_base_v122_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_distmed_504d_base_v123_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_distmed_126d_base_v124_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_distmed_252d_base_v125_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_distmed_504d_base_v126_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_distmed_126d_base_v127_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_distmed_252d_base_v128_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of drev_chg
def f050rvq_f050_revenue_quality_drev_chg_distmed_504d_base_v129_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_distmed_126d_base_v130_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_distmed_252d_base_v131_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_distmed_504d_base_v132_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_distmed_126d_base_v133_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_distmed_252d_base_v134_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_distmed_504d_base_v135_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_distmed_126d_base_v136_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_distmed_252d_base_v137_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_ex_drev
def f050rvq_f050_revenue_quality_rev_ex_drev_distmed_504d_base_v138_signal(revenue, deferredrev, closeadj):
    base = (revenue - deferredrev.diff(periods=63).fillna(0))
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_chg_63d_base_v139_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_to_ocf
def f050rvq_f050_revenue_quality_rev_to_ocf_chg_252d_base_v140_signal(revenue, ncfo, closeadj):
    base = _f050_rev_to_ocf(revenue, ncfo)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_chg_63d_base_v141_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ocf_to_rev
def f050rvq_f050_revenue_quality_ocf_to_rev_chg_252d_base_v142_signal(ncfo, revenue, closeadj):
    base = ncfo / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_chg_63d_base_v143_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rcv_growth_to_rev
def f050rvq_f050_revenue_quality_rcv_growth_to_rev_chg_252d_base_v144_signal(receivables, revenue, closeadj):
    base = receivables.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in drev_chg
def f050rvq_f050_revenue_quality_drev_chg_chg_63d_base_v145_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in drev_chg
def f050rvq_f050_revenue_quality_drev_chg_chg_252d_base_v146_signal(deferredrev, closeadj):
    base = deferredrev.diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_chg_63d_base_v147_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rcv_to_rev_lvl
def f050rvq_f050_revenue_quality_rcv_to_rev_lvl_chg_252d_base_v148_signal(receivables, revenue, closeadj):
    base = receivables / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_chg_63d_base_v149_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in drev_to_rev
def f050rvq_f050_revenue_quality_drev_to_rev_chg_252d_base_v150_signal(deferredrev, revenue, closeadj):
    base = deferredrev / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

