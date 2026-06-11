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
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f11_revenue_smoothness(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f11_recurring_proxy(revenue, w):
    g = revenue.pct_change(periods=w)
    return 1.0 / (1.0 + g.abs())


def _f11_revenue_cv(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / m.replace(0, np.nan).abs()

def f11drr_f11_diagnostics_recurring_revenue_smooth_5d_base_v001_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smooth_10d_base_v002_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smooth_21d_base_v003_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smooth_42d_base_v004_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smooth_63d_base_v005_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smooth_126d_base_v006_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smooth_189d_base_v007_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smooth_252d_base_v008_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smooth_378d_base_v009_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smooth_504d_base_v010_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smoothlog_5d_base_v011_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 5)
    result = np.log1p(base.clip(lower=0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smoothlog_10d_base_v012_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 10)
    result = np.log1p(base.clip(lower=0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smoothlog_21d_base_v013_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 21)
    result = np.log1p(base.clip(lower=0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smoothlog_42d_base_v014_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 42)
    result = np.log1p(base.clip(lower=0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smoothlog_63d_base_v015_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 63)
    result = np.log1p(base.clip(lower=0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smoothlog_126d_base_v016_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 126)
    result = np.log1p(base.clip(lower=0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smoothlog_189d_base_v017_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 189)
    result = np.log1p(base.clip(lower=0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smoothlog_252d_base_v018_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 252)
    result = np.log1p(base.clip(lower=0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smoothlog_378d_base_v019_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 378)
    result = np.log1p(base.clip(lower=0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_smoothlog_504d_base_v020_signal(revenue, closeadj):
    base = _f11_revenue_smoothness(revenue, 504)
    result = np.log1p(base.clip(lower=0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recur_5d_base_v021_signal(revenue, closeadj):
    base = _f11_recurring_proxy(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recur_10d_base_v022_signal(revenue, closeadj):
    base = _f11_recurring_proxy(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recur_21d_base_v023_signal(revenue, closeadj):
    base = _f11_recurring_proxy(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recur_42d_base_v024_signal(revenue, closeadj):
    base = _f11_recurring_proxy(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recur_63d_base_v025_signal(revenue, closeadj):
    base = _f11_recurring_proxy(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recur_126d_base_v026_signal(revenue, closeadj):
    base = _f11_recurring_proxy(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recur_189d_base_v027_signal(revenue, closeadj):
    base = _f11_recurring_proxy(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recur_252d_base_v028_signal(revenue, closeadj):
    base = _f11_recurring_proxy(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recur_378d_base_v029_signal(revenue, closeadj):
    base = _f11_recurring_proxy(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recur_504d_base_v030_signal(revenue, closeadj):
    base = _f11_recurring_proxy(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recurxdef_5d_base_v031_signal(revenue, deferredrev, closeadj):
    base = _f11_recurring_proxy(revenue, 5)
    rdr = deferredrev / revenue.replace(0, np.nan).abs()
    result = base * rdr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recurxdef_10d_base_v032_signal(revenue, deferredrev, closeadj):
    base = _f11_recurring_proxy(revenue, 10)
    rdr = deferredrev / revenue.replace(0, np.nan).abs()
    result = base * rdr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recurxdef_21d_base_v033_signal(revenue, deferredrev, closeadj):
    base = _f11_recurring_proxy(revenue, 21)
    rdr = deferredrev / revenue.replace(0, np.nan).abs()
    result = base * rdr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recurxdef_42d_base_v034_signal(revenue, deferredrev, closeadj):
    base = _f11_recurring_proxy(revenue, 42)
    rdr = deferredrev / revenue.replace(0, np.nan).abs()
    result = base * rdr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recurxdef_63d_base_v035_signal(revenue, deferredrev, closeadj):
    base = _f11_recurring_proxy(revenue, 63)
    rdr = deferredrev / revenue.replace(0, np.nan).abs()
    result = base * rdr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recurxdef_126d_base_v036_signal(revenue, deferredrev, closeadj):
    base = _f11_recurring_proxy(revenue, 126)
    rdr = deferredrev / revenue.replace(0, np.nan).abs()
    result = base * rdr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recurxdef_189d_base_v037_signal(revenue, deferredrev, closeadj):
    base = _f11_recurring_proxy(revenue, 189)
    rdr = deferredrev / revenue.replace(0, np.nan).abs()
    result = base * rdr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recurxdef_252d_base_v038_signal(revenue, deferredrev, closeadj):
    base = _f11_recurring_proxy(revenue, 252)
    rdr = deferredrev / revenue.replace(0, np.nan).abs()
    result = base * rdr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recurxdef_378d_base_v039_signal(revenue, deferredrev, closeadj):
    base = _f11_recurring_proxy(revenue, 378)
    rdr = deferredrev / revenue.replace(0, np.nan).abs()
    result = base * rdr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_recurxdef_504d_base_v040_signal(revenue, deferredrev, closeadj):
    base = _f11_recurring_proxy(revenue, 504)
    rdr = deferredrev / revenue.replace(0, np.nan).abs()
    result = base * rdr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cv_5d_base_v041_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cv_10d_base_v042_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cv_21d_base_v043_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cv_42d_base_v044_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cv_63d_base_v045_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cv_126d_base_v046_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cv_189d_base_v047_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cv_252d_base_v048_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cv_378d_base_v049_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cv_504d_base_v050_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cvinv_5d_base_v051_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 5)
    result = (1.0 / (1.0 + base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cvinv_10d_base_v052_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 10)
    result = (1.0 / (1.0 + base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cvinv_21d_base_v053_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 21)
    result = (1.0 / (1.0 + base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cvinv_42d_base_v054_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 42)
    result = (1.0 / (1.0 + base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cvinv_63d_base_v055_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 63)
    result = (1.0 / (1.0 + base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cvinv_126d_base_v056_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 126)
    result = (1.0 / (1.0 + base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cvinv_189d_base_v057_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 189)
    result = (1.0 / (1.0 + base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cvinv_252d_base_v058_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 252)
    result = (1.0 / (1.0 + base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cvinv_378d_base_v059_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 378)
    result = (1.0 / (1.0 + base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_cvinv_504d_base_v060_signal(revenue, closeadj):
    base = _f11_revenue_cv(revenue, 504)
    result = (1.0 / (1.0 + base)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_defratio_5d_base_v061_signal(revenue, deferredrev, closeadj):
    smooth = _f11_revenue_smoothness(revenue, 5)
    drr = deferredrev / revenue.replace(0, np.nan).abs()
    result = drr * smooth * closeadj / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_defratio_10d_base_v062_signal(revenue, deferredrev, closeadj):
    smooth = _f11_revenue_smoothness(revenue, 10)
    drr = deferredrev / revenue.replace(0, np.nan).abs()
    result = drr * smooth * closeadj / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_defratio_21d_base_v063_signal(revenue, deferredrev, closeadj):
    smooth = _f11_revenue_smoothness(revenue, 21)
    drr = deferredrev / revenue.replace(0, np.nan).abs()
    result = drr * smooth * closeadj / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_defratio_42d_base_v064_signal(revenue, deferredrev, closeadj):
    smooth = _f11_revenue_smoothness(revenue, 42)
    drr = deferredrev / revenue.replace(0, np.nan).abs()
    result = drr * smooth * closeadj / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_defratio_63d_base_v065_signal(revenue, deferredrev, closeadj):
    smooth = _f11_revenue_smoothness(revenue, 63)
    drr = deferredrev / revenue.replace(0, np.nan).abs()
    result = drr * smooth * closeadj / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_defratio_126d_base_v066_signal(revenue, deferredrev, closeadj):
    smooth = _f11_revenue_smoothness(revenue, 126)
    drr = deferredrev / revenue.replace(0, np.nan).abs()
    result = drr * smooth * closeadj / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_defratio_189d_base_v067_signal(revenue, deferredrev, closeadj):
    smooth = _f11_revenue_smoothness(revenue, 189)
    drr = deferredrev / revenue.replace(0, np.nan).abs()
    result = drr * smooth * closeadj / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_defratio_252d_base_v068_signal(revenue, deferredrev, closeadj):
    smooth = _f11_revenue_smoothness(revenue, 252)
    drr = deferredrev / revenue.replace(0, np.nan).abs()
    result = drr * smooth * closeadj / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_defratio_378d_base_v069_signal(revenue, deferredrev, closeadj):
    smooth = _f11_revenue_smoothness(revenue, 378)
    drr = deferredrev / revenue.replace(0, np.nan).abs()
    result = drr * smooth * closeadj / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_defratio_504d_base_v070_signal(revenue, deferredrev, closeadj):
    smooth = _f11_revenue_smoothness(revenue, 504)
    drr = deferredrev / revenue.replace(0, np.nan).abs()
    result = drr * smooth * closeadj / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_defgrowth_5d_base_v071_signal(deferredrev, revenue, closeadj):
    prim = _f11_revenue_smoothness(revenue, 5)
    dg = deferredrev.pct_change(periods=5)
    result = dg * prim * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_defgrowth_10d_base_v072_signal(deferredrev, revenue, closeadj):
    prim = _f11_revenue_smoothness(revenue, 10)
    dg = deferredrev.pct_change(periods=10)
    result = dg * prim * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_defgrowth_21d_base_v073_signal(deferredrev, revenue, closeadj):
    prim = _f11_revenue_smoothness(revenue, 21)
    dg = deferredrev.pct_change(periods=21)
    result = dg * prim * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_defgrowth_42d_base_v074_signal(deferredrev, revenue, closeadj):
    prim = _f11_revenue_smoothness(revenue, 42)
    dg = deferredrev.pct_change(periods=42)
    result = dg * prim * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11drr_f11_diagnostics_recurring_revenue_defgrowth_63d_base_v075_signal(deferredrev, revenue, closeadj):
    prim = _f11_revenue_smoothness(revenue, 63)
    dg = deferredrev.pct_change(periods=63)
    result = dg * prim * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f11drr_f11_diagnostics_recurring_revenue_smooth_5d_base_v001_signal,
    f11drr_f11_diagnostics_recurring_revenue_smooth_10d_base_v002_signal,
    f11drr_f11_diagnostics_recurring_revenue_smooth_21d_base_v003_signal,
    f11drr_f11_diagnostics_recurring_revenue_smooth_42d_base_v004_signal,
    f11drr_f11_diagnostics_recurring_revenue_smooth_63d_base_v005_signal,
    f11drr_f11_diagnostics_recurring_revenue_smooth_126d_base_v006_signal,
    f11drr_f11_diagnostics_recurring_revenue_smooth_189d_base_v007_signal,
    f11drr_f11_diagnostics_recurring_revenue_smooth_252d_base_v008_signal,
    f11drr_f11_diagnostics_recurring_revenue_smooth_378d_base_v009_signal,
    f11drr_f11_diagnostics_recurring_revenue_smooth_504d_base_v010_signal,
    f11drr_f11_diagnostics_recurring_revenue_smoothlog_5d_base_v011_signal,
    f11drr_f11_diagnostics_recurring_revenue_smoothlog_10d_base_v012_signal,
    f11drr_f11_diagnostics_recurring_revenue_smoothlog_21d_base_v013_signal,
    f11drr_f11_diagnostics_recurring_revenue_smoothlog_42d_base_v014_signal,
    f11drr_f11_diagnostics_recurring_revenue_smoothlog_63d_base_v015_signal,
    f11drr_f11_diagnostics_recurring_revenue_smoothlog_126d_base_v016_signal,
    f11drr_f11_diagnostics_recurring_revenue_smoothlog_189d_base_v017_signal,
    f11drr_f11_diagnostics_recurring_revenue_smoothlog_252d_base_v018_signal,
    f11drr_f11_diagnostics_recurring_revenue_smoothlog_378d_base_v019_signal,
    f11drr_f11_diagnostics_recurring_revenue_smoothlog_504d_base_v020_signal,
    f11drr_f11_diagnostics_recurring_revenue_recur_5d_base_v021_signal,
    f11drr_f11_diagnostics_recurring_revenue_recur_10d_base_v022_signal,
    f11drr_f11_diagnostics_recurring_revenue_recur_21d_base_v023_signal,
    f11drr_f11_diagnostics_recurring_revenue_recur_42d_base_v024_signal,
    f11drr_f11_diagnostics_recurring_revenue_recur_63d_base_v025_signal,
    f11drr_f11_diagnostics_recurring_revenue_recur_126d_base_v026_signal,
    f11drr_f11_diagnostics_recurring_revenue_recur_189d_base_v027_signal,
    f11drr_f11_diagnostics_recurring_revenue_recur_252d_base_v028_signal,
    f11drr_f11_diagnostics_recurring_revenue_recur_378d_base_v029_signal,
    f11drr_f11_diagnostics_recurring_revenue_recur_504d_base_v030_signal,
    f11drr_f11_diagnostics_recurring_revenue_recurxdef_5d_base_v031_signal,
    f11drr_f11_diagnostics_recurring_revenue_recurxdef_10d_base_v032_signal,
    f11drr_f11_diagnostics_recurring_revenue_recurxdef_21d_base_v033_signal,
    f11drr_f11_diagnostics_recurring_revenue_recurxdef_42d_base_v034_signal,
    f11drr_f11_diagnostics_recurring_revenue_recurxdef_63d_base_v035_signal,
    f11drr_f11_diagnostics_recurring_revenue_recurxdef_126d_base_v036_signal,
    f11drr_f11_diagnostics_recurring_revenue_recurxdef_189d_base_v037_signal,
    f11drr_f11_diagnostics_recurring_revenue_recurxdef_252d_base_v038_signal,
    f11drr_f11_diagnostics_recurring_revenue_recurxdef_378d_base_v039_signal,
    f11drr_f11_diagnostics_recurring_revenue_recurxdef_504d_base_v040_signal,
    f11drr_f11_diagnostics_recurring_revenue_cv_5d_base_v041_signal,
    f11drr_f11_diagnostics_recurring_revenue_cv_10d_base_v042_signal,
    f11drr_f11_diagnostics_recurring_revenue_cv_21d_base_v043_signal,
    f11drr_f11_diagnostics_recurring_revenue_cv_42d_base_v044_signal,
    f11drr_f11_diagnostics_recurring_revenue_cv_63d_base_v045_signal,
    f11drr_f11_diagnostics_recurring_revenue_cv_126d_base_v046_signal,
    f11drr_f11_diagnostics_recurring_revenue_cv_189d_base_v047_signal,
    f11drr_f11_diagnostics_recurring_revenue_cv_252d_base_v048_signal,
    f11drr_f11_diagnostics_recurring_revenue_cv_378d_base_v049_signal,
    f11drr_f11_diagnostics_recurring_revenue_cv_504d_base_v050_signal,
    f11drr_f11_diagnostics_recurring_revenue_cvinv_5d_base_v051_signal,
    f11drr_f11_diagnostics_recurring_revenue_cvinv_10d_base_v052_signal,
    f11drr_f11_diagnostics_recurring_revenue_cvinv_21d_base_v053_signal,
    f11drr_f11_diagnostics_recurring_revenue_cvinv_42d_base_v054_signal,
    f11drr_f11_diagnostics_recurring_revenue_cvinv_63d_base_v055_signal,
    f11drr_f11_diagnostics_recurring_revenue_cvinv_126d_base_v056_signal,
    f11drr_f11_diagnostics_recurring_revenue_cvinv_189d_base_v057_signal,
    f11drr_f11_diagnostics_recurring_revenue_cvinv_252d_base_v058_signal,
    f11drr_f11_diagnostics_recurring_revenue_cvinv_378d_base_v059_signal,
    f11drr_f11_diagnostics_recurring_revenue_cvinv_504d_base_v060_signal,
    f11drr_f11_diagnostics_recurring_revenue_defratio_5d_base_v061_signal,
    f11drr_f11_diagnostics_recurring_revenue_defratio_10d_base_v062_signal,
    f11drr_f11_diagnostics_recurring_revenue_defratio_21d_base_v063_signal,
    f11drr_f11_diagnostics_recurring_revenue_defratio_42d_base_v064_signal,
    f11drr_f11_diagnostics_recurring_revenue_defratio_63d_base_v065_signal,
    f11drr_f11_diagnostics_recurring_revenue_defratio_126d_base_v066_signal,
    f11drr_f11_diagnostics_recurring_revenue_defratio_189d_base_v067_signal,
    f11drr_f11_diagnostics_recurring_revenue_defratio_252d_base_v068_signal,
    f11drr_f11_diagnostics_recurring_revenue_defratio_378d_base_v069_signal,
    f11drr_f11_diagnostics_recurring_revenue_defratio_504d_base_v070_signal,
    f11drr_f11_diagnostics_recurring_revenue_defgrowth_5d_base_v071_signal,
    f11drr_f11_diagnostics_recurring_revenue_defgrowth_10d_base_v072_signal,
    f11drr_f11_diagnostics_recurring_revenue_defgrowth_21d_base_v073_signal,
    f11drr_f11_diagnostics_recurring_revenue_defgrowth_42d_base_v074_signal,
    f11drr_f11_diagnostics_recurring_revenue_defgrowth_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_DIAGNOSTICS_RECURRING_REVENUE_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f11_revenue_smoothness", "_f11_recurring_proxy", "_f11_revenue_cv",)
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
    print(f"OK f11_diagnostics_recurring_revenue_base_001_075_claude: {n_features} features pass")
