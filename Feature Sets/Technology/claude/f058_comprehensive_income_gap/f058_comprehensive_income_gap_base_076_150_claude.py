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
def _f058_gap(consolinc, netinc):
    return consolinc - netinc


# 63d z-score of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_z_63d_base_v076_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_z_126d_base_v077_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_z_252d_base_v078_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_z_504d_base_v079_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_z_63d_base_v080_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_z_126d_base_v081_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_z_252d_base_v082_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_z_504d_base_v083_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_z_63d_base_v084_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_z_126d_base_v085_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_z_252d_base_v086_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_z_504d_base_v087_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_z_63d_base_v088_signal(consolinc, closeadj):
    base = consolinc
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_z_126d_base_v089_signal(consolinc, closeadj):
    base = consolinc
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_z_252d_base_v090_signal(consolinc, closeadj):
    base = consolinc
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_z_504d_base_v091_signal(consolinc, closeadj):
    base = consolinc
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_z_63d_base_v092_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_z_126d_base_v093_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_z_252d_base_v094_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_z_504d_base_v095_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_z_63d_base_v096_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_z_126d_base_v097_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_z_252d_base_v098_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_z_504d_base_v099_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_z_63d_base_v100_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_z_126d_base_v101_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_z_252d_base_v102_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_z_504d_base_v103_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_distmax_252d_base_v104_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_distmax_504d_base_v105_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_distmax_252d_base_v106_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_distmax_504d_base_v107_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_distmax_252d_base_v108_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_distmax_504d_base_v109_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_distmax_252d_base_v110_signal(consolinc, closeadj):
    base = consolinc
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_distmax_504d_base_v111_signal(consolinc, closeadj):
    base = consolinc
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_distmax_252d_base_v112_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_distmax_504d_base_v113_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_distmax_252d_base_v114_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_distmax_504d_base_v115_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_distmax_252d_base_v116_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_distmax_504d_base_v117_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_distmed_126d_base_v118_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_distmed_252d_base_v119_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_distmed_504d_base_v120_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_distmed_126d_base_v121_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_distmed_252d_base_v122_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_distmed_504d_base_v123_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_distmed_126d_base_v124_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_distmed_252d_base_v125_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_distmed_504d_base_v126_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_distmed_126d_base_v127_signal(consolinc, closeadj):
    base = consolinc
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_distmed_252d_base_v128_signal(consolinc, closeadj):
    base = consolinc
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_distmed_504d_base_v129_signal(consolinc, closeadj):
    base = consolinc
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_distmed_126d_base_v130_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_distmed_252d_base_v131_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_distmed_504d_base_v132_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_distmed_126d_base_v133_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_distmed_252d_base_v134_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_distmed_504d_base_v135_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_distmed_126d_base_v136_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_distmed_252d_base_v137_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_distmed_504d_base_v138_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_chg_63d_base_v139_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_chg_252d_base_v140_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_chg_63d_base_v141_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_chg_252d_base_v142_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_chg_63d_base_v143_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_chg_252d_base_v144_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_chg_63d_base_v145_signal(consolinc, closeadj):
    base = consolinc
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_chg_252d_base_v146_signal(consolinc, closeadj):
    base = consolinc
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_chg_63d_base_v147_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_chg_252d_base_v148_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_chg_63d_base_v149_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_chg_252d_base_v150_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

