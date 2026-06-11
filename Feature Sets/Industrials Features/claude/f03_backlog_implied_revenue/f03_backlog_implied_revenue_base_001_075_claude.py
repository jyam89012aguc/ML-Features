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

def f03bir_f03_backlog_implied_revenue_rsm_5d_base_v001_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 5)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsm_10d_base_v002_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 10)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsm_21d_base_v003_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 21)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsm_42d_base_v004_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 42)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsm_63d_base_v005_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 63)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsm_126d_base_v006_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 126)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsm_189d_base_v007_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 189)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsm_252d_base_v008_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 252)
    result = (base / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgp_5d_base_v009_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgp_10d_base_v010_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgp_21d_base_v011_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgp_42d_base_v012_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgp_63d_base_v013_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgp_126d_base_v014_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgp_189d_base_v015_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgp_252d_base_v016_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drp_5d_base_v017_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drp_10d_base_v018_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drp_21d_base_v019_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drp_42d_base_v020_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drp_63d_base_v021_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drp_126d_base_v022_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drp_189d_base_v023_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drp_252d_base_v024_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmstd_5d_base_v025_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 5)
    result = _std(base, 5) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmstd_10d_base_v026_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 10)
    result = _std(base, 10) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmstd_21d_base_v027_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 21)
    result = _std(base, 21) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmstd_42d_base_v028_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 42)
    result = _std(base, 42) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmstd_63d_base_v029_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 63)
    result = _std(base, 63) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmstd_126d_base_v030_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 126)
    result = _std(base, 126) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmstd_189d_base_v031_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 189)
    result = _std(base, 189) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmstd_252d_base_v032_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 252)
    result = _std(base, 252) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpstd_5d_base_v033_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 5)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpstd_10d_base_v034_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 10)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpstd_21d_base_v035_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpstd_42d_base_v036_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpstd_63d_base_v037_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpstd_126d_base_v038_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpstd_189d_base_v039_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpstd_252d_base_v040_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpstd_5d_base_v041_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 5)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpstd_10d_base_v042_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 10)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpstd_21d_base_v043_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpstd_42d_base_v044_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpstd_63d_base_v045_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpstd_126d_base_v046_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpstd_189d_base_v047_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpstd_252d_base_v048_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmz_21d_base_v049_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 21)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmz_63d_base_v050_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmz_126d_base_v051_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmz_252d_base_v052_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpz_21d_base_v053_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 21)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpz_63d_base_v054_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpz_126d_base_v055_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpz_252d_base_v056_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpz_21d_base_v057_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 21)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpz_63d_base_v058_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpz_126d_base_v059_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpz_252d_base_v060_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpaccel_21d_base_v061_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 21)
    result = base.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpaccel_63d_base_v062_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 63)
    result = base.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpaccel_126d_base_v063_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 126)
    result = base.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rgpaccel_252d_base_v064_signal(revenue, closeadj):
    base = _f03_revenue_growth_persistence(revenue, 252)
    result = base.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmaccel_21d_base_v065_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 21)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmaccel_63d_base_v066_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmaccel_126d_base_v067_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 126)
    result = base.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmaccel_252d_base_v068_signal(revenue, closeadj):
    base = _f03_revenue_smoothed(revenue, 252)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpaccel_21d_base_v069_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 21)
    result = base.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpaccel_63d_base_v070_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 63)
    result = base.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpaccel_126d_base_v071_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 126)
    result = base.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_drpaccel_252d_base_v072_signal(deferredrev, revenue, closeadj):
    base = _f03_deferred_rev_pulse(deferredrev, revenue, 252)
    result = base.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxrgp_21d_base_v073_signal(revenue, closeadj):
    a = _f03_revenue_smoothed(revenue, 21)
    b = _f03_revenue_growth_persistence(revenue, 21)
    result = (a / 1e9) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxrgp_63d_base_v074_signal(revenue, closeadj):
    a = _f03_revenue_smoothed(revenue, 63)
    b = _f03_revenue_growth_persistence(revenue, 63)
    result = (a / 1e9) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03bir_f03_backlog_implied_revenue_rsmxrgp_126d_base_v075_signal(revenue, closeadj):
    a = _f03_revenue_smoothed(revenue, 126)
    b = _f03_revenue_growth_persistence(revenue, 126)
    result = (a / 1e9) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03bir_f03_backlog_implied_revenue_rsm_5d_base_v001_signal,
    f03bir_f03_backlog_implied_revenue_rsm_10d_base_v002_signal,
    f03bir_f03_backlog_implied_revenue_rsm_21d_base_v003_signal,
    f03bir_f03_backlog_implied_revenue_rsm_42d_base_v004_signal,
    f03bir_f03_backlog_implied_revenue_rsm_63d_base_v005_signal,
    f03bir_f03_backlog_implied_revenue_rsm_126d_base_v006_signal,
    f03bir_f03_backlog_implied_revenue_rsm_189d_base_v007_signal,
    f03bir_f03_backlog_implied_revenue_rsm_252d_base_v008_signal,
    f03bir_f03_backlog_implied_revenue_rgp_5d_base_v009_signal,
    f03bir_f03_backlog_implied_revenue_rgp_10d_base_v010_signal,
    f03bir_f03_backlog_implied_revenue_rgp_21d_base_v011_signal,
    f03bir_f03_backlog_implied_revenue_rgp_42d_base_v012_signal,
    f03bir_f03_backlog_implied_revenue_rgp_63d_base_v013_signal,
    f03bir_f03_backlog_implied_revenue_rgp_126d_base_v014_signal,
    f03bir_f03_backlog_implied_revenue_rgp_189d_base_v015_signal,
    f03bir_f03_backlog_implied_revenue_rgp_252d_base_v016_signal,
    f03bir_f03_backlog_implied_revenue_drp_5d_base_v017_signal,
    f03bir_f03_backlog_implied_revenue_drp_10d_base_v018_signal,
    f03bir_f03_backlog_implied_revenue_drp_21d_base_v019_signal,
    f03bir_f03_backlog_implied_revenue_drp_42d_base_v020_signal,
    f03bir_f03_backlog_implied_revenue_drp_63d_base_v021_signal,
    f03bir_f03_backlog_implied_revenue_drp_126d_base_v022_signal,
    f03bir_f03_backlog_implied_revenue_drp_189d_base_v023_signal,
    f03bir_f03_backlog_implied_revenue_drp_252d_base_v024_signal,
    f03bir_f03_backlog_implied_revenue_rsmstd_5d_base_v025_signal,
    f03bir_f03_backlog_implied_revenue_rsmstd_10d_base_v026_signal,
    f03bir_f03_backlog_implied_revenue_rsmstd_21d_base_v027_signal,
    f03bir_f03_backlog_implied_revenue_rsmstd_42d_base_v028_signal,
    f03bir_f03_backlog_implied_revenue_rsmstd_63d_base_v029_signal,
    f03bir_f03_backlog_implied_revenue_rsmstd_126d_base_v030_signal,
    f03bir_f03_backlog_implied_revenue_rsmstd_189d_base_v031_signal,
    f03bir_f03_backlog_implied_revenue_rsmstd_252d_base_v032_signal,
    f03bir_f03_backlog_implied_revenue_rgpstd_5d_base_v033_signal,
    f03bir_f03_backlog_implied_revenue_rgpstd_10d_base_v034_signal,
    f03bir_f03_backlog_implied_revenue_rgpstd_21d_base_v035_signal,
    f03bir_f03_backlog_implied_revenue_rgpstd_42d_base_v036_signal,
    f03bir_f03_backlog_implied_revenue_rgpstd_63d_base_v037_signal,
    f03bir_f03_backlog_implied_revenue_rgpstd_126d_base_v038_signal,
    f03bir_f03_backlog_implied_revenue_rgpstd_189d_base_v039_signal,
    f03bir_f03_backlog_implied_revenue_rgpstd_252d_base_v040_signal,
    f03bir_f03_backlog_implied_revenue_drpstd_5d_base_v041_signal,
    f03bir_f03_backlog_implied_revenue_drpstd_10d_base_v042_signal,
    f03bir_f03_backlog_implied_revenue_drpstd_21d_base_v043_signal,
    f03bir_f03_backlog_implied_revenue_drpstd_42d_base_v044_signal,
    f03bir_f03_backlog_implied_revenue_drpstd_63d_base_v045_signal,
    f03bir_f03_backlog_implied_revenue_drpstd_126d_base_v046_signal,
    f03bir_f03_backlog_implied_revenue_drpstd_189d_base_v047_signal,
    f03bir_f03_backlog_implied_revenue_drpstd_252d_base_v048_signal,
    f03bir_f03_backlog_implied_revenue_rsmz_21d_base_v049_signal,
    f03bir_f03_backlog_implied_revenue_rsmz_63d_base_v050_signal,
    f03bir_f03_backlog_implied_revenue_rsmz_126d_base_v051_signal,
    f03bir_f03_backlog_implied_revenue_rsmz_252d_base_v052_signal,
    f03bir_f03_backlog_implied_revenue_rgpz_21d_base_v053_signal,
    f03bir_f03_backlog_implied_revenue_rgpz_63d_base_v054_signal,
    f03bir_f03_backlog_implied_revenue_rgpz_126d_base_v055_signal,
    f03bir_f03_backlog_implied_revenue_rgpz_252d_base_v056_signal,
    f03bir_f03_backlog_implied_revenue_drpz_21d_base_v057_signal,
    f03bir_f03_backlog_implied_revenue_drpz_63d_base_v058_signal,
    f03bir_f03_backlog_implied_revenue_drpz_126d_base_v059_signal,
    f03bir_f03_backlog_implied_revenue_drpz_252d_base_v060_signal,
    f03bir_f03_backlog_implied_revenue_rgpaccel_21d_base_v061_signal,
    f03bir_f03_backlog_implied_revenue_rgpaccel_63d_base_v062_signal,
    f03bir_f03_backlog_implied_revenue_rgpaccel_126d_base_v063_signal,
    f03bir_f03_backlog_implied_revenue_rgpaccel_252d_base_v064_signal,
    f03bir_f03_backlog_implied_revenue_rsmaccel_21d_base_v065_signal,
    f03bir_f03_backlog_implied_revenue_rsmaccel_63d_base_v066_signal,
    f03bir_f03_backlog_implied_revenue_rsmaccel_126d_base_v067_signal,
    f03bir_f03_backlog_implied_revenue_rsmaccel_252d_base_v068_signal,
    f03bir_f03_backlog_implied_revenue_drpaccel_21d_base_v069_signal,
    f03bir_f03_backlog_implied_revenue_drpaccel_63d_base_v070_signal,
    f03bir_f03_backlog_implied_revenue_drpaccel_126d_base_v071_signal,
    f03bir_f03_backlog_implied_revenue_drpaccel_252d_base_v072_signal,
    f03bir_f03_backlog_implied_revenue_rsmxrgp_21d_base_v073_signal,
    f03bir_f03_backlog_implied_revenue_rsmxrgp_63d_base_v074_signal,
    f03bir_f03_backlog_implied_revenue_rsmxrgp_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_BACKLOG_IMPLIED_REVENUE_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f03_backlog_implied_revenue_base_001_075_claude: {n_features} features pass")
