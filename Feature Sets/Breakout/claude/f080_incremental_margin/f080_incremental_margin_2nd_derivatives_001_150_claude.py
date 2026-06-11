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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

# ===== folder domain primitives =====
def _f080_delta_revenue(rv, w):
    return rv - rv.shift(w)

def _f080_delta_op_inc(eb, w):
    return eb - eb.shift(w)

def _f080_incremental_margin(eb, rv, w):
    deb = eb - eb.shift(w)
    drv = rv - rv.shift(w)
    return deb / drv.replace(0, np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v001_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v002_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v003_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v004_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v005_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v006_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v007_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v008_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v009_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=21, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v010_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v011_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v012_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v013_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v014_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v015_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v016_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v017_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v018_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v019_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_21d_slope_v020_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v021_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v022_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v023_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v024_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v025_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v026_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v027_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v028_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v029_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=63, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v030_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v031_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v032_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v033_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v034_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v035_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v036_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v037_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v038_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v039_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_63d_slope_v040_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_126d_slope_v041_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_126d_slope_v042_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_126d_slope_v043_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_126d_slope_v044_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_126d_slope_v045_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_mean(base, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_126d_slope_v046_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_126d_slope_v047_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_126d_slope_v048_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_126d_slope_v049_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=126, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_revenue_126d_slope_v050_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_revenue(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v051_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v052_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v053_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v054_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v055_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v056_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v057_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v058_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v059_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=21, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v060_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v061_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v062_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v063_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v064_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v065_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v066_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v067_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v068_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v069_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v070_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v071_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v072_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v073_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v074_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v075_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v076_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v077_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v078_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v079_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=63, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v080_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v081_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v082_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v083_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v084_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v085_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v086_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v087_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v088_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v089_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v090_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v091_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v092_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v093_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v094_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v095_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_mean(base, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v096_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v097_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v098_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v099_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=126, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v100_signal(ebit, revenue, closeadj):
    base = _mean(_f080_delta_op_inc(ebit, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v101_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v102_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v103_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v104_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v105_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v106_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v107_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v108_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v109_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=21, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v110_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v111_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v112_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v113_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v114_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v115_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v116_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v117_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v118_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v119_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_21d_slope_v120_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v121_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v122_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v123_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v124_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v125_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v126_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v127_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v128_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v129_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=63, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v130_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v131_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v132_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v133_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v134_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v135_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v136_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v137_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v138_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v139_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_63d_slope_v140_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_126d_slope_v141_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_126d_slope_v142_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_126d_slope_v143_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_126d_slope_v144_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_126d_slope_v145_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_mean(base, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_126d_slope_v146_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_126d_slope_v147_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_126d_slope_v148_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_126d_slope_v149_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=126, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f080imr_f080_incremental_margin_incremental_margin_126d_slope_v150_signal(ebit, revenue, closeadj):
    base = _mean(_f080_incremental_margin(ebit, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v001_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v002_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v003_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v004_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v005_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v006_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v007_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v008_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v009_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v010_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v011_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v012_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v013_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v014_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v015_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v016_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v017_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v018_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v019_signal,
    f080imr_f080_incremental_margin_delta_revenue_21d_slope_v020_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v021_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v022_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v023_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v024_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v025_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v026_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v027_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v028_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v029_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v030_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v031_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v032_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v033_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v034_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v035_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v036_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v037_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v038_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v039_signal,
    f080imr_f080_incremental_margin_delta_revenue_63d_slope_v040_signal,
    f080imr_f080_incremental_margin_delta_revenue_126d_slope_v041_signal,
    f080imr_f080_incremental_margin_delta_revenue_126d_slope_v042_signal,
    f080imr_f080_incremental_margin_delta_revenue_126d_slope_v043_signal,
    f080imr_f080_incremental_margin_delta_revenue_126d_slope_v044_signal,
    f080imr_f080_incremental_margin_delta_revenue_126d_slope_v045_signal,
    f080imr_f080_incremental_margin_delta_revenue_126d_slope_v046_signal,
    f080imr_f080_incremental_margin_delta_revenue_126d_slope_v047_signal,
    f080imr_f080_incremental_margin_delta_revenue_126d_slope_v048_signal,
    f080imr_f080_incremental_margin_delta_revenue_126d_slope_v049_signal,
    f080imr_f080_incremental_margin_delta_revenue_126d_slope_v050_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v051_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v052_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v053_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v054_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v055_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v056_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v057_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v058_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v059_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v060_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v061_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v062_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v063_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v064_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v065_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v066_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v067_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v068_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v069_signal,
    f080imr_f080_incremental_margin_delta_op_inc_21d_slope_v070_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v071_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v072_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v073_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v074_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v075_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v076_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v077_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v078_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v079_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v080_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v081_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v082_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v083_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v084_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v085_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v086_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v087_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v088_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v089_signal,
    f080imr_f080_incremental_margin_delta_op_inc_63d_slope_v090_signal,
    f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v091_signal,
    f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v092_signal,
    f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v093_signal,
    f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v094_signal,
    f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v095_signal,
    f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v096_signal,
    f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v097_signal,
    f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v098_signal,
    f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v099_signal,
    f080imr_f080_incremental_margin_delta_op_inc_126d_slope_v100_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v101_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v102_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v103_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v104_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v105_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v106_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v107_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v108_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v109_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v110_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v111_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v112_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v113_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v114_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v115_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v116_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v117_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v118_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v119_signal,
    f080imr_f080_incremental_margin_incremental_margin_21d_slope_v120_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v121_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v122_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v123_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v124_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v125_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v126_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v127_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v128_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v129_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v130_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v131_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v132_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v133_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v134_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v135_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v136_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v137_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v138_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v139_signal,
    f080imr_f080_incremental_margin_incremental_margin_63d_slope_v140_signal,
    f080imr_f080_incremental_margin_incremental_margin_126d_slope_v141_signal,
    f080imr_f080_incremental_margin_incremental_margin_126d_slope_v142_signal,
    f080imr_f080_incremental_margin_incremental_margin_126d_slope_v143_signal,
    f080imr_f080_incremental_margin_incremental_margin_126d_slope_v144_signal,
    f080imr_f080_incremental_margin_incremental_margin_126d_slope_v145_signal,
    f080imr_f080_incremental_margin_incremental_margin_126d_slope_v146_signal,
    f080imr_f080_incremental_margin_incremental_margin_126d_slope_v147_signal,
    f080imr_f080_incremental_margin_incremental_margin_126d_slope_v148_signal,
    f080imr_f080_incremental_margin_incremental_margin_126d_slope_v149_signal,
    f080imr_f080_incremental_margin_incremental_margin_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F080_INCREMENTAL_MARGIN_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    cols = {"ebit": ebit, "revenue": revenue, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f080_delta_revenue", "_f080_delta_op_inc", "_f080_incremental_margin",)
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
    print(f"OK f080_incremental_margin_2nd_derivatives_001_150_claude: {n_features} features pass")
