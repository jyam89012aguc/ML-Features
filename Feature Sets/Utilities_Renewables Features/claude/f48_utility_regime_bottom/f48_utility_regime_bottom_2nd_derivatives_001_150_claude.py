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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f48_revenue_bottom(revenue, w):
    mn = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    return (revenue - mn) / mn.replace(0, np.nan).abs()


def _f48_margin_bottom(ebitdamargin, w):
    mn = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    return ebitdamargin - mn


def _f48_regime_bottom_score(revenue, ebitda, fcf, w):
    rb = (revenue - revenue.rolling(w, min_periods=max(1, w // 2)).min())
    eb = (ebitda - ebitda.rolling(w, min_periods=max(1, w // 2)).min())
    fb = (fcf - fcf.rolling(w, min_periods=max(1, w // 2)).min())
    return rb + eb + fb


# ===== features =====
def f48urb_f48_utility_regime_bottom_rb_rev_5d_s00_sw21_slope_v001_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 5)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_5d_s00_sw63_slope_v002_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 5)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_5d_s00_sw126_slope_v003_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 5)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_5d_s00_sw21_slope_v004_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 5)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_5d_s00_sw63_slope_v005_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 5)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_5d_s00_sw126_slope_v006_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 5)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_5d_s00_sw21_slope_v007_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 5)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_5d_s00_sw63_slope_v008_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 5)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_5d_s00_sw126_slope_v009_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 5)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_10d_s00_sw21_slope_v010_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 10)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_10d_s00_sw63_slope_v011_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 10)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_10d_s00_sw126_slope_v012_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 10)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_10d_s00_sw21_slope_v013_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 10)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_10d_s00_sw63_slope_v014_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 10)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_10d_s00_sw126_slope_v015_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 10)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_10d_s00_sw21_slope_v016_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 10)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_10d_s00_sw63_slope_v017_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 10)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_10d_s00_sw126_slope_v018_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 10)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_21d_s00_sw21_slope_v019_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_21d_s00_sw63_slope_v020_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_21d_s00_sw126_slope_v021_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_21d_s00_sw21_slope_v022_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_21d_s00_sw63_slope_v023_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_21d_s00_sw126_slope_v024_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_21d_s00_sw21_slope_v025_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_21d_s00_sw63_slope_v026_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_21d_s00_sw126_slope_v027_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_42d_s00_sw21_slope_v028_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 42)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_42d_s00_sw63_slope_v029_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 42)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_42d_s00_sw126_slope_v030_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 42)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_42d_s00_sw21_slope_v031_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 42)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_42d_s00_sw63_slope_v032_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 42)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_42d_s00_sw126_slope_v033_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 42)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_42d_s00_sw21_slope_v034_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 42)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_42d_s00_sw63_slope_v035_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 42)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_42d_s00_sw126_slope_v036_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 42)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_63d_s00_sw21_slope_v037_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_63d_s00_sw63_slope_v038_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_63d_s00_sw126_slope_v039_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 63)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_63d_s00_sw21_slope_v040_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_63d_s00_sw63_slope_v041_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_63d_s00_sw126_slope_v042_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_63d_s00_sw21_slope_v043_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_63d_s00_sw63_slope_v044_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_63d_s00_sw126_slope_v045_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 63)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_84d_s00_sw21_slope_v046_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 84)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_84d_s00_sw63_slope_v047_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 84)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_84d_s00_sw126_slope_v048_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 84)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_84d_s00_sw21_slope_v049_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 84)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_84d_s00_sw63_slope_v050_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 84)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_84d_s00_sw126_slope_v051_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 84)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_84d_s00_sw21_slope_v052_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 84)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_84d_s00_sw63_slope_v053_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 84)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_84d_s00_sw126_slope_v054_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 84)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_105d_s00_sw21_slope_v055_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 105)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_105d_s00_sw63_slope_v056_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 105)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_105d_s00_sw126_slope_v057_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 105)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_105d_s00_sw21_slope_v058_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 105)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_105d_s00_sw63_slope_v059_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 105)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_105d_s00_sw126_slope_v060_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 105)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_105d_s00_sw21_slope_v061_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 105)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_105d_s00_sw63_slope_v062_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 105)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_105d_s00_sw126_slope_v063_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 105)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_126d_s00_sw21_slope_v064_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_126d_s00_sw63_slope_v065_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_126d_s00_sw126_slope_v066_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 126)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_126d_s00_sw21_slope_v067_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_126d_s00_sw63_slope_v068_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_126d_s00_sw126_slope_v069_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_126d_s00_sw21_slope_v070_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_126d_s00_sw63_slope_v071_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_126d_s00_sw126_slope_v072_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 126)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_147d_s00_sw21_slope_v073_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 147)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_147d_s00_sw63_slope_v074_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 147)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_147d_s00_sw126_slope_v075_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 147)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_147d_s00_sw21_slope_v076_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 147)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_147d_s00_sw63_slope_v077_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 147)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_147d_s00_sw126_slope_v078_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 147)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_147d_s00_sw21_slope_v079_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 147)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_147d_s00_sw63_slope_v080_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 147)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_147d_s00_sw126_slope_v081_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 147)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_168d_s00_sw21_slope_v082_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 168)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_168d_s00_sw63_slope_v083_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 168)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_168d_s00_sw126_slope_v084_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 168)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_168d_s00_sw21_slope_v085_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 168)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_168d_s00_sw63_slope_v086_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 168)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_168d_s00_sw126_slope_v087_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 168)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_168d_s00_sw21_slope_v088_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 168)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_168d_s00_sw63_slope_v089_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 168)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_168d_s00_sw126_slope_v090_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 168)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_189d_s00_sw21_slope_v091_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 189)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_189d_s00_sw63_slope_v092_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 189)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_189d_s00_sw126_slope_v093_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 189)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_189d_s00_sw21_slope_v094_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 189)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_189d_s00_sw63_slope_v095_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 189)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_189d_s00_sw126_slope_v096_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 189)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_189d_s00_sw21_slope_v097_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 189)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_189d_s00_sw63_slope_v098_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 189)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_189d_s00_sw126_slope_v099_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 189)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_210d_s00_sw21_slope_v100_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 210)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_210d_s00_sw63_slope_v101_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 210)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_210d_s00_sw126_slope_v102_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 210)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_210d_s00_sw21_slope_v103_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 210)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_210d_s00_sw63_slope_v104_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 210)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_210d_s00_sw126_slope_v105_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 210)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_210d_s00_sw21_slope_v106_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 210)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_210d_s00_sw63_slope_v107_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 210)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_210d_s00_sw126_slope_v108_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 210)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_231d_s00_sw21_slope_v109_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 231)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_231d_s00_sw63_slope_v110_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 231)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_231d_s00_sw126_slope_v111_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 231)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_231d_s00_sw21_slope_v112_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 231)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_231d_s00_sw63_slope_v113_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 231)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_231d_s00_sw126_slope_v114_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 231)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_231d_s00_sw21_slope_v115_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 231)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_231d_s00_sw63_slope_v116_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 231)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_231d_s00_sw126_slope_v117_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 231)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_252d_s00_sw21_slope_v118_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 252)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_252d_s00_sw63_slope_v119_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 252)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_252d_s00_sw126_slope_v120_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_252d_s00_sw21_slope_v121_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_252d_s00_sw63_slope_v122_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_252d_s00_sw126_slope_v123_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_252d_s00_sw21_slope_v124_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 252)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_252d_s00_sw63_slope_v125_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 252)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_252d_s00_sw126_slope_v126_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_294d_s00_sw21_slope_v127_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 294)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_294d_s00_sw63_slope_v128_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 294)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_294d_s00_sw126_slope_v129_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 294)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_294d_s00_sw21_slope_v130_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 294)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_294d_s00_sw63_slope_v131_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 294)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_294d_s00_sw126_slope_v132_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 294)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_294d_s00_sw21_slope_v133_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 294)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_294d_s00_sw63_slope_v134_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 294)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_294d_s00_sw126_slope_v135_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 294)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_336d_s00_sw21_slope_v136_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 336)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_336d_s00_sw63_slope_v137_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 336)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_336d_s00_sw126_slope_v138_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 336)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_336d_s00_sw21_slope_v139_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 336)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_336d_s00_sw63_slope_v140_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 336)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_336d_s00_sw126_slope_v141_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 336)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_336d_s00_sw21_slope_v142_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 336)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_336d_s00_sw63_slope_v143_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 336)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_336d_s00_sw126_slope_v144_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 336)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_378d_s00_sw21_slope_v145_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 378)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_378d_s00_sw63_slope_v146_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 378)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_378d_s00_sw126_slope_v147_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 378)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_378d_s00_sw21_slope_v148_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 378)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_378d_s00_sw63_slope_v149_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 378)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_378d_s00_sw126_slope_v150_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 378)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f48urb_f48_utility_regime_bottom_rb_rev_5d_s00_sw21_slope_v001_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_5d_s00_sw63_slope_v002_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_5d_s00_sw126_slope_v003_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_5d_s00_sw21_slope_v004_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_5d_s00_sw63_slope_v005_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_5d_s00_sw126_slope_v006_signal,
    f48urb_f48_utility_regime_bottom_rs_full_5d_s00_sw21_slope_v007_signal,
    f48urb_f48_utility_regime_bottom_rs_full_5d_s00_sw63_slope_v008_signal,
    f48urb_f48_utility_regime_bottom_rs_full_5d_s00_sw126_slope_v009_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_10d_s00_sw21_slope_v010_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_10d_s00_sw63_slope_v011_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_10d_s00_sw126_slope_v012_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_10d_s00_sw21_slope_v013_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_10d_s00_sw63_slope_v014_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_10d_s00_sw126_slope_v015_signal,
    f48urb_f48_utility_regime_bottom_rs_full_10d_s00_sw21_slope_v016_signal,
    f48urb_f48_utility_regime_bottom_rs_full_10d_s00_sw63_slope_v017_signal,
    f48urb_f48_utility_regime_bottom_rs_full_10d_s00_sw126_slope_v018_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_21d_s00_sw21_slope_v019_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_21d_s00_sw63_slope_v020_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_21d_s00_sw126_slope_v021_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_21d_s00_sw21_slope_v022_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_21d_s00_sw63_slope_v023_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_21d_s00_sw126_slope_v024_signal,
    f48urb_f48_utility_regime_bottom_rs_full_21d_s00_sw21_slope_v025_signal,
    f48urb_f48_utility_regime_bottom_rs_full_21d_s00_sw63_slope_v026_signal,
    f48urb_f48_utility_regime_bottom_rs_full_21d_s00_sw126_slope_v027_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_42d_s00_sw21_slope_v028_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_42d_s00_sw63_slope_v029_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_42d_s00_sw126_slope_v030_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_42d_s00_sw21_slope_v031_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_42d_s00_sw63_slope_v032_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_42d_s00_sw126_slope_v033_signal,
    f48urb_f48_utility_regime_bottom_rs_full_42d_s00_sw21_slope_v034_signal,
    f48urb_f48_utility_regime_bottom_rs_full_42d_s00_sw63_slope_v035_signal,
    f48urb_f48_utility_regime_bottom_rs_full_42d_s00_sw126_slope_v036_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_63d_s00_sw21_slope_v037_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_63d_s00_sw63_slope_v038_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_63d_s00_sw126_slope_v039_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_63d_s00_sw21_slope_v040_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_63d_s00_sw63_slope_v041_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_63d_s00_sw126_slope_v042_signal,
    f48urb_f48_utility_regime_bottom_rs_full_63d_s00_sw21_slope_v043_signal,
    f48urb_f48_utility_regime_bottom_rs_full_63d_s00_sw63_slope_v044_signal,
    f48urb_f48_utility_regime_bottom_rs_full_63d_s00_sw126_slope_v045_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_84d_s00_sw21_slope_v046_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_84d_s00_sw63_slope_v047_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_84d_s00_sw126_slope_v048_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_84d_s00_sw21_slope_v049_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_84d_s00_sw63_slope_v050_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_84d_s00_sw126_slope_v051_signal,
    f48urb_f48_utility_regime_bottom_rs_full_84d_s00_sw21_slope_v052_signal,
    f48urb_f48_utility_regime_bottom_rs_full_84d_s00_sw63_slope_v053_signal,
    f48urb_f48_utility_regime_bottom_rs_full_84d_s00_sw126_slope_v054_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_105d_s00_sw21_slope_v055_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_105d_s00_sw63_slope_v056_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_105d_s00_sw126_slope_v057_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_105d_s00_sw21_slope_v058_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_105d_s00_sw63_slope_v059_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_105d_s00_sw126_slope_v060_signal,
    f48urb_f48_utility_regime_bottom_rs_full_105d_s00_sw21_slope_v061_signal,
    f48urb_f48_utility_regime_bottom_rs_full_105d_s00_sw63_slope_v062_signal,
    f48urb_f48_utility_regime_bottom_rs_full_105d_s00_sw126_slope_v063_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_126d_s00_sw21_slope_v064_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_126d_s00_sw63_slope_v065_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_126d_s00_sw126_slope_v066_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_126d_s00_sw21_slope_v067_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_126d_s00_sw63_slope_v068_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_126d_s00_sw126_slope_v069_signal,
    f48urb_f48_utility_regime_bottom_rs_full_126d_s00_sw21_slope_v070_signal,
    f48urb_f48_utility_regime_bottom_rs_full_126d_s00_sw63_slope_v071_signal,
    f48urb_f48_utility_regime_bottom_rs_full_126d_s00_sw126_slope_v072_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_147d_s00_sw21_slope_v073_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_147d_s00_sw63_slope_v074_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_147d_s00_sw126_slope_v075_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_147d_s00_sw21_slope_v076_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_147d_s00_sw63_slope_v077_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_147d_s00_sw126_slope_v078_signal,
    f48urb_f48_utility_regime_bottom_rs_full_147d_s00_sw21_slope_v079_signal,
    f48urb_f48_utility_regime_bottom_rs_full_147d_s00_sw63_slope_v080_signal,
    f48urb_f48_utility_regime_bottom_rs_full_147d_s00_sw126_slope_v081_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_168d_s00_sw21_slope_v082_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_168d_s00_sw63_slope_v083_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_168d_s00_sw126_slope_v084_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_168d_s00_sw21_slope_v085_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_168d_s00_sw63_slope_v086_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_168d_s00_sw126_slope_v087_signal,
    f48urb_f48_utility_regime_bottom_rs_full_168d_s00_sw21_slope_v088_signal,
    f48urb_f48_utility_regime_bottom_rs_full_168d_s00_sw63_slope_v089_signal,
    f48urb_f48_utility_regime_bottom_rs_full_168d_s00_sw126_slope_v090_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_189d_s00_sw21_slope_v091_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_189d_s00_sw63_slope_v092_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_189d_s00_sw126_slope_v093_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_189d_s00_sw21_slope_v094_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_189d_s00_sw63_slope_v095_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_189d_s00_sw126_slope_v096_signal,
    f48urb_f48_utility_regime_bottom_rs_full_189d_s00_sw21_slope_v097_signal,
    f48urb_f48_utility_regime_bottom_rs_full_189d_s00_sw63_slope_v098_signal,
    f48urb_f48_utility_regime_bottom_rs_full_189d_s00_sw126_slope_v099_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_210d_s00_sw21_slope_v100_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_210d_s00_sw63_slope_v101_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_210d_s00_sw126_slope_v102_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_210d_s00_sw21_slope_v103_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_210d_s00_sw63_slope_v104_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_210d_s00_sw126_slope_v105_signal,
    f48urb_f48_utility_regime_bottom_rs_full_210d_s00_sw21_slope_v106_signal,
    f48urb_f48_utility_regime_bottom_rs_full_210d_s00_sw63_slope_v107_signal,
    f48urb_f48_utility_regime_bottom_rs_full_210d_s00_sw126_slope_v108_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_231d_s00_sw21_slope_v109_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_231d_s00_sw63_slope_v110_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_231d_s00_sw126_slope_v111_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_231d_s00_sw21_slope_v112_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_231d_s00_sw63_slope_v113_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_231d_s00_sw126_slope_v114_signal,
    f48urb_f48_utility_regime_bottom_rs_full_231d_s00_sw21_slope_v115_signal,
    f48urb_f48_utility_regime_bottom_rs_full_231d_s00_sw63_slope_v116_signal,
    f48urb_f48_utility_regime_bottom_rs_full_231d_s00_sw126_slope_v117_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_252d_s00_sw21_slope_v118_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_252d_s00_sw63_slope_v119_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_252d_s00_sw126_slope_v120_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_252d_s00_sw21_slope_v121_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_252d_s00_sw63_slope_v122_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_252d_s00_sw126_slope_v123_signal,
    f48urb_f48_utility_regime_bottom_rs_full_252d_s00_sw21_slope_v124_signal,
    f48urb_f48_utility_regime_bottom_rs_full_252d_s00_sw63_slope_v125_signal,
    f48urb_f48_utility_regime_bottom_rs_full_252d_s00_sw126_slope_v126_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_294d_s00_sw21_slope_v127_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_294d_s00_sw63_slope_v128_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_294d_s00_sw126_slope_v129_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_294d_s00_sw21_slope_v130_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_294d_s00_sw63_slope_v131_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_294d_s00_sw126_slope_v132_signal,
    f48urb_f48_utility_regime_bottom_rs_full_294d_s00_sw21_slope_v133_signal,
    f48urb_f48_utility_regime_bottom_rs_full_294d_s00_sw63_slope_v134_signal,
    f48urb_f48_utility_regime_bottom_rs_full_294d_s00_sw126_slope_v135_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_336d_s00_sw21_slope_v136_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_336d_s00_sw63_slope_v137_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_336d_s00_sw126_slope_v138_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_336d_s00_sw21_slope_v139_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_336d_s00_sw63_slope_v140_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_336d_s00_sw126_slope_v141_signal,
    f48urb_f48_utility_regime_bottom_rs_full_336d_s00_sw21_slope_v142_signal,
    f48urb_f48_utility_regime_bottom_rs_full_336d_s00_sw63_slope_v143_signal,
    f48urb_f48_utility_regime_bottom_rs_full_336d_s00_sw126_slope_v144_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_378d_s00_sw21_slope_v145_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_378d_s00_sw63_slope_v146_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_378d_s00_sw126_slope_v147_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_378d_s00_sw21_slope_v148_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_378d_s00_sw63_slope_v149_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_378d_s00_sw126_slope_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_UTILITY_REGIME_BOTTOM_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    cols = {"closeadj": closeadj, "ebitda": ebitda, "ebitdamargin": ebitdamargin, "fcf": fcf, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f48_revenue_bottom", "_f48_margin_bottom", "_f48_regime_bottom_score",)
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f48_utility_regime_bottom_2nd_derivatives_001_150_claude: {n_features} features pass")
