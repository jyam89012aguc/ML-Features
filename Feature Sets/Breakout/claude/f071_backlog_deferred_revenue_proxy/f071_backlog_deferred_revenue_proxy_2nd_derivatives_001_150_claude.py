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

def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

# ===== folder domain primitives =====
def _f071_deferred_change(deferredrev, w):
    return _slope_diff_norm_local(deferredrev, w) * deferredrev


def _f071_backlog_growth(deferredrev, w):
    avg = deferredrev.rolling(w, min_periods=max(1, w // 2)).mean()
    return (deferredrev - avg) / avg.replace(0, np.nan).abs() * deferredrev


def _f071_forward_demand(deferredrev, revenue, w):
    ratio = deferredrev / revenue.replace(0, np.nan).abs()
    return ratio * deferredrev.rolling(w, min_periods=max(1, w // 2)).mean()


def _slope_diff_norm_local(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v001_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v002_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v003_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 5) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v004_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 5) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v005_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v006_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v007_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v008_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v009_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_deferred_change(deferredrev, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v010_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_deferred_change(deferredrev, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v011_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v012_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v013_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 21) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v014_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 21) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v015_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v016_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v017_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v018_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v019_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_deferred_change(deferredrev, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v020_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_deferred_change(deferredrev, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v021_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v022_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v023_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 63) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v024_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 63) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v025_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v026_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v027_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v028_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v029_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_deferred_change(deferredrev, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v030_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_deferred_change(deferredrev, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v031_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v032_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v033_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 126) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v034_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 126) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v035_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v036_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v037_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v038_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v039_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_deferred_change(deferredrev, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v040_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_deferred_change(deferredrev, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v041_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v042_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v043_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 252) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v044_signal(deferredrev, revenue, closeadj):
    base = _f071_deferred_change(deferredrev, 252) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v045_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v046_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v047_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v048_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_deferred_change(deferredrev, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v049_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_deferred_change(deferredrev, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v050_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_deferred_change(deferredrev, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v051_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v052_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v053_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 5) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v054_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 5) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v055_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v056_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v057_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v058_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v059_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_backlog_growth(deferredrev, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v060_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_backlog_growth(deferredrev, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v061_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v062_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v063_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 21) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v064_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 21) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v065_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v066_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v067_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v068_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v069_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_backlog_growth(deferredrev, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v070_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_backlog_growth(deferredrev, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v071_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v072_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v073_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 63) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v074_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 63) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v075_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v076_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v077_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v078_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v079_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_backlog_growth(deferredrev, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v080_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_backlog_growth(deferredrev, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v081_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v082_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v083_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 126) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v084_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 126) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v085_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v086_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v087_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v088_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v089_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_backlog_growth(deferredrev, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v090_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_backlog_growth(deferredrev, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v091_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v092_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v093_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 252) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v094_signal(deferredrev, revenue, closeadj):
    base = _f071_backlog_growth(deferredrev, 252) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v095_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v096_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v097_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v098_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_backlog_growth(deferredrev, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v099_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_backlog_growth(deferredrev, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v100_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_backlog_growth(deferredrev, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v101_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v102_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v103_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 5) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v104_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 5) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v105_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v106_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v107_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v108_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v109_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_forward_demand(deferredrev, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v110_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_forward_demand(deferredrev, revenue, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v111_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v112_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v113_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 21) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v114_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 21) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v115_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v116_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v117_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v118_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v119_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_forward_demand(deferredrev, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v120_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_forward_demand(deferredrev, revenue, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v121_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v122_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v123_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 63) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v124_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v125_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v126_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v127_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v128_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v129_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_forward_demand(deferredrev, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v130_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_forward_demand(deferredrev, revenue, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v131_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v132_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v133_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 126) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v134_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 126) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v135_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v136_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v137_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v138_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v139_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_forward_demand(deferredrev, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v140_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_forward_demand(deferredrev, revenue, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v141_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v142_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v143_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 252) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v144_signal(deferredrev, revenue, closeadj):
    base = _f071_forward_demand(deferredrev, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v145_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v146_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v147_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v148_signal(deferredrev, revenue, closeadj):
    base = _mean(_f071_forward_demand(deferredrev, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v149_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_forward_demand(deferredrev, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v150_signal(deferredrev, revenue, closeadj):
    base = _std(_f071_forward_demand(deferredrev, revenue, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v001_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v002_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v003_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v004_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v005_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v006_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v007_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v008_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v009_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_slope_v010_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v011_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v012_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v013_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v014_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v015_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v016_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v017_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v018_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v019_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_slope_v020_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v021_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v022_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v023_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v024_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v025_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v026_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v027_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v028_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v029_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_slope_v030_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v031_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v032_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v033_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v034_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v035_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v036_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v037_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v038_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v039_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_slope_v040_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v041_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v042_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v043_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v044_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v045_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v046_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v047_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v048_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v049_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_slope_v050_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v051_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v052_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v053_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v054_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v055_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v056_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v057_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v058_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v059_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_slope_v060_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v061_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v062_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v063_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v064_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v065_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v066_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v067_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v068_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v069_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_slope_v070_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v071_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v072_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v073_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v074_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v075_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v076_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v077_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v078_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v079_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_slope_v080_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v081_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v082_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v083_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v084_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v085_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v086_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v087_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v088_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v089_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_slope_v090_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v091_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v092_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v093_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v094_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v095_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v096_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v097_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v098_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v099_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_slope_v100_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v101_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v102_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v103_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v104_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v105_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v106_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v107_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v108_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v109_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_slope_v110_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v111_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v112_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v113_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v114_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v115_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v116_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v117_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v118_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v119_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_slope_v120_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v121_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v122_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v123_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v124_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v125_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v126_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v127_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v128_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v129_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_slope_v130_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v131_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v132_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v133_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v134_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v135_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v136_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v137_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v138_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v139_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_slope_v140_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v141_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v142_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v143_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v144_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v145_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v146_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v147_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v148_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v149_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F071_BACKLOG_DEFERRED_REVENUE_PROXY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    cols = {"deferredrev": deferredrev, "revenue": revenue, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f071_deferred_change", "_f071_backlog_growth", "_f071_forward_demand")
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
    print(f"OK f071_backlog_deferred_revenue_proxy_slope_001_150_claude: {n_features} features pass")
