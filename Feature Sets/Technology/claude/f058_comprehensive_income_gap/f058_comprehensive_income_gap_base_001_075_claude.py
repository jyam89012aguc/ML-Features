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


# 21d mean of ci_gap scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_mean_21d_base_v001_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ci_gap scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_mean_63d_base_v002_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ci_gap scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_mean_126d_base_v003_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ci_gap scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_mean_252d_base_v004_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ci_gap scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_mean_504d_base_v005_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ci_gap_to_equity scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_mean_21d_base_v006_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ci_gap_to_equity scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_mean_63d_base_v007_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ci_gap_to_equity scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_mean_126d_base_v008_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ci_gap_to_equity scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_mean_252d_base_v009_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ci_gap_to_equity scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_mean_504d_base_v010_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ci_gap_to_ni scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_mean_21d_base_v011_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ci_gap_to_ni scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_mean_63d_base_v012_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ci_gap_to_ni scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_mean_126d_base_v013_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ci_gap_to_ni scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_mean_252d_base_v014_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ci_gap_to_ni scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_mean_504d_base_v015_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of consolinc_lvl scaled by closeadj
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_mean_21d_base_v016_signal(consolinc, closeadj):
    base = consolinc
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of consolinc_lvl scaled by closeadj
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_mean_63d_base_v017_signal(consolinc, closeadj):
    base = consolinc
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of consolinc_lvl scaled by closeadj
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_mean_126d_base_v018_signal(consolinc, closeadj):
    base = consolinc
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of consolinc_lvl scaled by closeadj
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_mean_252d_base_v019_signal(consolinc, closeadj):
    base = consolinc
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of consolinc_lvl scaled by closeadj
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_mean_504d_base_v020_signal(consolinc, closeadj):
    base = consolinc
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ci_gap_yoy scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_mean_21d_base_v021_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ci_gap_yoy scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_mean_63d_base_v022_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ci_gap_yoy scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_mean_126d_base_v023_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ci_gap_yoy scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_mean_252d_base_v024_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ci_gap_yoy scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_mean_504d_base_v025_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ci_gap_to_rev scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_mean_21d_base_v026_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ci_gap_to_rev scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_mean_63d_base_v027_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ci_gap_to_rev scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_mean_126d_base_v028_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ci_gap_to_rev scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_mean_252d_base_v029_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ci_gap_to_rev scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_mean_504d_base_v030_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ci_gap_sign scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_mean_21d_base_v031_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ci_gap_sign scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_mean_63d_base_v032_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ci_gap_sign scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_mean_126d_base_v033_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ci_gap_sign scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_mean_252d_base_v034_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ci_gap_sign scaled by closeadj
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_mean_504d_base_v035_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_median_63d_base_v036_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_median_252d_base_v037_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_median_504d_base_v038_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_median_63d_base_v039_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_median_252d_base_v040_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_median_504d_base_v041_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_median_63d_base_v042_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_median_252d_base_v043_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_median_504d_base_v044_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_median_63d_base_v045_signal(consolinc, closeadj):
    base = consolinc
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_median_252d_base_v046_signal(consolinc, closeadj):
    base = consolinc
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_median_504d_base_v047_signal(consolinc, closeadj):
    base = consolinc
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_median_63d_base_v048_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_median_252d_base_v049_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_median_504d_base_v050_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_median_63d_base_v051_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_median_252d_base_v052_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_median_504d_base_v053_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_median_63d_base_v054_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_median_252d_base_v055_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_median_504d_base_v056_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_rmax_252d_base_v057_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_rmax_504d_base_v058_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_rmax_252d_base_v059_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_rmax_504d_base_v060_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_rmax_252d_base_v061_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_rmax_504d_base_v062_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_rmax_252d_base_v063_signal(consolinc, closeadj):
    base = consolinc
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_rmax_504d_base_v064_signal(consolinc, closeadj):
    base = consolinc
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_rmax_252d_base_v065_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_rmax_504d_base_v066_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_rmax_252d_base_v067_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_rmax_504d_base_v068_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_rmax_252d_base_v069_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_rmax_504d_base_v070_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_rmin_252d_base_v071_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_rmin_504d_base_v072_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_rmin_252d_base_v073_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_rmin_504d_base_v074_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_rmin_252d_base_v075_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

