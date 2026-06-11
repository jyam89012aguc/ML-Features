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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f28_backlog_growth(deferredrev, w):
    return deferredrev.pct_change(periods=w)


def _f28_backlog_to_revenue(deferredrev, revenue):
    return deferredrev / revenue.replace(0, np.nan)


def _f28_drilling_backlog_score(deferredrev, w):
    g = deferredrev.pct_change(periods=w)
    m = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return (g - m) / sd.replace(0, np.nan)


# ===== features =====

def f28dbk_f28_drilling_backlog_backg_5d_base_xc_jsw5_jerk_v001_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 5)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_5d_base_xc_jsw5_jerk_v002_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 5)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_10d_base_xc_jsw5_jerk_v003_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 10)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_10d_base_xc_jsw5_jerk_v004_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 10)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_21d_base_xc_jsw5_jerk_v005_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 21)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_21d_base_xc_jsw5_jerk_v006_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 21)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_42d_base_xc_jsw5_jerk_v007_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 42)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_42d_base_xc_jsw5_jerk_v008_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 42)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_63d_base_xc_jsw5_jerk_v009_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 63)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_63d_base_xc_jsw5_jerk_v010_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 63)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_84d_base_xc_jsw5_jerk_v011_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 84)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_84d_base_xc_jsw5_jerk_v012_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 84)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_126d_base_xc_jsw5_jerk_v013_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 126)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_126d_base_xc_jsw5_jerk_v014_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 126)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_189d_base_xc_jsw5_jerk_v015_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 189)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_189d_base_xc_jsw5_jerk_v016_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 189)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_252d_base_xc_jsw5_jerk_v017_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 252)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_252d_base_xc_jsw5_jerk_v018_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 252)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_378d_base_xc_jsw5_jerk_v019_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 378)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_378d_base_xc_jsw5_jerk_v020_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 378)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_504d_base_xc_jsw5_jerk_v021_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 504)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_504d_base_xc_jsw5_jerk_v022_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 504)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_btr_base_xc_jsw5_jerk_v023_signal(deferredrev, revenue, closeadj):
    base = _f28_backlog_to_revenue(deferredrev, revenue)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_5d_base_xc2_jsw5_jerk_v024_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 5)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_5d_base_xc2_jsw5_jerk_v025_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 5)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_10d_base_xc2_jsw5_jerk_v026_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 10)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_10d_base_xc2_jsw5_jerk_v027_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 10)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_21d_base_xc2_jsw5_jerk_v028_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 21)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_21d_base_xc2_jsw5_jerk_v029_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 21)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_42d_base_xc2_jsw5_jerk_v030_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 42)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_42d_base_xc2_jsw5_jerk_v031_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 42)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_63d_base_xc2_jsw5_jerk_v032_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 63)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_63d_base_xc2_jsw5_jerk_v033_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 63)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_84d_base_xc2_jsw5_jerk_v034_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 84)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_84d_base_xc2_jsw5_jerk_v035_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 84)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_126d_base_xc2_jsw5_jerk_v036_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 126)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_126d_base_xc2_jsw5_jerk_v037_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 126)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_189d_base_xc2_jsw5_jerk_v038_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 189)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_189d_base_xc2_jsw5_jerk_v039_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 189)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_252d_base_xc2_jsw5_jerk_v040_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 252)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_252d_base_xc2_jsw5_jerk_v041_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 252)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_378d_base_xc2_jsw5_jerk_v042_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 378)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_378d_base_xc2_jsw5_jerk_v043_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 378)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_504d_base_xc2_jsw5_jerk_v044_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 504)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_504d_base_xc2_jsw5_jerk_v045_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 504)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_btr_base_xc2_jsw5_jerk_v046_signal(deferredrev, revenue, closeadj):
    base = _f28_backlog_to_revenue(deferredrev, revenue)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_5d_base_xmc_jsw5_jerk_v047_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 5)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_5d_base_xmc_jsw5_jerk_v048_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 5)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_10d_base_xmc_jsw5_jerk_v049_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 10)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_10d_base_xmc_jsw5_jerk_v050_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 10)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_21d_base_xmc_jsw5_jerk_v051_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 21)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_21d_base_xmc_jsw5_jerk_v052_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 21)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_42d_base_xmc_jsw5_jerk_v053_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 42)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_42d_base_xmc_jsw5_jerk_v054_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 42)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_63d_base_xmc_jsw5_jerk_v055_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 63)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_63d_base_xmc_jsw5_jerk_v056_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 63)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_84d_base_xmc_jsw5_jerk_v057_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 84)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_84d_base_xmc_jsw5_jerk_v058_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 84)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_126d_base_xmc_jsw5_jerk_v059_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 126)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_126d_base_xmc_jsw5_jerk_v060_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 126)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_189d_base_xmc_jsw5_jerk_v061_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 189)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_189d_base_xmc_jsw5_jerk_v062_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 189)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_252d_base_xmc_jsw5_jerk_v063_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 252)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_252d_base_xmc_jsw5_jerk_v064_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 252)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_378d_base_xmc_jsw5_jerk_v065_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 378)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_378d_base_xmc_jsw5_jerk_v066_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 378)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_504d_base_xmc_jsw5_jerk_v067_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 504)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_504d_base_xmc_jsw5_jerk_v068_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 504)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_btr_base_xmc_jsw5_jerk_v069_signal(deferredrev, revenue, closeadj):
    base = _f28_backlog_to_revenue(deferredrev, revenue)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_5d_base_xzc_jsw5_jerk_v070_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 5)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_5d_base_xzc_jsw5_jerk_v071_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 5)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_10d_base_xzc_jsw5_jerk_v072_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 10)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_10d_base_xzc_jsw5_jerk_v073_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 10)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_21d_base_xzc_jsw5_jerk_v074_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 21)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_21d_base_xzc_jsw5_jerk_v075_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 21)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_42d_base_xzc_jsw5_jerk_v076_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 42)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_42d_base_xzc_jsw5_jerk_v077_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 42)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_63d_base_xzc_jsw5_jerk_v078_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 63)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_63d_base_xzc_jsw5_jerk_v079_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 63)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_84d_base_xzc_jsw5_jerk_v080_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 84)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_84d_base_xzc_jsw5_jerk_v081_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 84)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_126d_base_xzc_jsw5_jerk_v082_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 126)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_126d_base_xzc_jsw5_jerk_v083_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 126)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_189d_base_xzc_jsw5_jerk_v084_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 189)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_189d_base_xzc_jsw5_jerk_v085_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 189)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_252d_base_xzc_jsw5_jerk_v086_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 252)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_252d_base_xzc_jsw5_jerk_v087_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 252)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_378d_base_xzc_jsw5_jerk_v088_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 378)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_378d_base_xzc_jsw5_jerk_v089_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 378)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_504d_base_xzc_jsw5_jerk_v090_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 504)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_504d_base_xzc_jsw5_jerk_v091_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 504)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_btr_base_xzc_jsw5_jerk_v092_signal(deferredrev, revenue, closeadj):
    base = _f28_backlog_to_revenue(deferredrev, revenue)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_5d_base_dmc_jsw5_jerk_v093_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 5)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_5d_base_dmc_jsw5_jerk_v094_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 5)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_10d_base_dmc_jsw5_jerk_v095_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 10)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_10d_base_dmc_jsw5_jerk_v096_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 10)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_21d_base_dmc_jsw5_jerk_v097_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 21)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_21d_base_dmc_jsw5_jerk_v098_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 21)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_42d_base_dmc_jsw5_jerk_v099_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 42)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_42d_base_dmc_jsw5_jerk_v100_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 42)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_63d_base_dmc_jsw5_jerk_v101_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 63)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_63d_base_dmc_jsw5_jerk_v102_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 63)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_84d_base_dmc_jsw5_jerk_v103_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 84)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_84d_base_dmc_jsw5_jerk_v104_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 84)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_126d_base_dmc_jsw5_jerk_v105_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 126)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_126d_base_dmc_jsw5_jerk_v106_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 126)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_189d_base_dmc_jsw5_jerk_v107_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 189)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_189d_base_dmc_jsw5_jerk_v108_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 189)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_252d_base_dmc_jsw5_jerk_v109_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 252)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_252d_base_dmc_jsw5_jerk_v110_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 252)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_378d_base_dmc_jsw5_jerk_v111_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 378)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_378d_base_dmc_jsw5_jerk_v112_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 378)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_504d_base_dmc_jsw5_jerk_v113_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 504)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_504d_base_dmc_jsw5_jerk_v114_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 504)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_btr_base_dmc_jsw5_jerk_v115_signal(deferredrev, revenue, closeadj):
    base = _f28_backlog_to_revenue(deferredrev, revenue)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_5d_m21_xc_jsw5_jerk_v116_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 5)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_5d_m21_xc_jsw5_jerk_v117_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 5)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_10d_m21_xc_jsw5_jerk_v118_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 10)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_10d_m21_xc_jsw5_jerk_v119_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 10)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_21d_m21_xc_jsw5_jerk_v120_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 21)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_21d_m21_xc_jsw5_jerk_v121_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 21)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_42d_m21_xc_jsw5_jerk_v122_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 42)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_42d_m21_xc_jsw5_jerk_v123_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 42)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_63d_m21_xc_jsw5_jerk_v124_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 63)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_63d_m21_xc_jsw5_jerk_v125_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 63)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_84d_m21_xc_jsw5_jerk_v126_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 84)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_84d_m21_xc_jsw5_jerk_v127_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 84)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_126d_m21_xc_jsw5_jerk_v128_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 126)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_126d_m21_xc_jsw5_jerk_v129_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 126)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_189d_m21_xc_jsw5_jerk_v130_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 189)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_189d_m21_xc_jsw5_jerk_v131_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 189)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_252d_m21_xc_jsw5_jerk_v132_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 252)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_252d_m21_xc_jsw5_jerk_v133_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 252)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_378d_m21_xc_jsw5_jerk_v134_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 378)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_378d_m21_xc_jsw5_jerk_v135_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 378)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_504d_m21_xc_jsw5_jerk_v136_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 504)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_504d_m21_xc_jsw5_jerk_v137_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 504)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_btr_m21_xc_jsw5_jerk_v138_signal(deferredrev, revenue, closeadj):
    base = _f28_backlog_to_revenue(deferredrev, revenue)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_5d_m21_xc2_jsw5_jerk_v139_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 5)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_5d_m21_xc2_jsw5_jerk_v140_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 5)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_10d_m21_xc2_jsw5_jerk_v141_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 10)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_10d_m21_xc2_jsw5_jerk_v142_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 10)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_21d_m21_xc2_jsw5_jerk_v143_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 21)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_21d_m21_xc2_jsw5_jerk_v144_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 21)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_42d_m21_xc2_jsw5_jerk_v145_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 42)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_42d_m21_xc2_jsw5_jerk_v146_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 42)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_63d_m21_xc2_jsw5_jerk_v147_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 63)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_63d_m21_xc2_jsw5_jerk_v148_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 63)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_84d_m21_xc2_jsw5_jerk_v149_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 84)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_84d_m21_xc2_jsw5_jerk_v150_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 84)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28dbk_f28_drilling_backlog_backg_5d_base_xc_jsw5_jerk_v001_signal,
    f28dbk_f28_drilling_backlog_backscore_5d_base_xc_jsw5_jerk_v002_signal,
    f28dbk_f28_drilling_backlog_backg_10d_base_xc_jsw5_jerk_v003_signal,
    f28dbk_f28_drilling_backlog_backscore_10d_base_xc_jsw5_jerk_v004_signal,
    f28dbk_f28_drilling_backlog_backg_21d_base_xc_jsw5_jerk_v005_signal,
    f28dbk_f28_drilling_backlog_backscore_21d_base_xc_jsw5_jerk_v006_signal,
    f28dbk_f28_drilling_backlog_backg_42d_base_xc_jsw5_jerk_v007_signal,
    f28dbk_f28_drilling_backlog_backscore_42d_base_xc_jsw5_jerk_v008_signal,
    f28dbk_f28_drilling_backlog_backg_63d_base_xc_jsw5_jerk_v009_signal,
    f28dbk_f28_drilling_backlog_backscore_63d_base_xc_jsw5_jerk_v010_signal,
    f28dbk_f28_drilling_backlog_backg_84d_base_xc_jsw5_jerk_v011_signal,
    f28dbk_f28_drilling_backlog_backscore_84d_base_xc_jsw5_jerk_v012_signal,
    f28dbk_f28_drilling_backlog_backg_126d_base_xc_jsw5_jerk_v013_signal,
    f28dbk_f28_drilling_backlog_backscore_126d_base_xc_jsw5_jerk_v014_signal,
    f28dbk_f28_drilling_backlog_backg_189d_base_xc_jsw5_jerk_v015_signal,
    f28dbk_f28_drilling_backlog_backscore_189d_base_xc_jsw5_jerk_v016_signal,
    f28dbk_f28_drilling_backlog_backg_252d_base_xc_jsw5_jerk_v017_signal,
    f28dbk_f28_drilling_backlog_backscore_252d_base_xc_jsw5_jerk_v018_signal,
    f28dbk_f28_drilling_backlog_backg_378d_base_xc_jsw5_jerk_v019_signal,
    f28dbk_f28_drilling_backlog_backscore_378d_base_xc_jsw5_jerk_v020_signal,
    f28dbk_f28_drilling_backlog_backg_504d_base_xc_jsw5_jerk_v021_signal,
    f28dbk_f28_drilling_backlog_backscore_504d_base_xc_jsw5_jerk_v022_signal,
    f28dbk_f28_drilling_backlog_btr_base_xc_jsw5_jerk_v023_signal,
    f28dbk_f28_drilling_backlog_backg_5d_base_xc2_jsw5_jerk_v024_signal,
    f28dbk_f28_drilling_backlog_backscore_5d_base_xc2_jsw5_jerk_v025_signal,
    f28dbk_f28_drilling_backlog_backg_10d_base_xc2_jsw5_jerk_v026_signal,
    f28dbk_f28_drilling_backlog_backscore_10d_base_xc2_jsw5_jerk_v027_signal,
    f28dbk_f28_drilling_backlog_backg_21d_base_xc2_jsw5_jerk_v028_signal,
    f28dbk_f28_drilling_backlog_backscore_21d_base_xc2_jsw5_jerk_v029_signal,
    f28dbk_f28_drilling_backlog_backg_42d_base_xc2_jsw5_jerk_v030_signal,
    f28dbk_f28_drilling_backlog_backscore_42d_base_xc2_jsw5_jerk_v031_signal,
    f28dbk_f28_drilling_backlog_backg_63d_base_xc2_jsw5_jerk_v032_signal,
    f28dbk_f28_drilling_backlog_backscore_63d_base_xc2_jsw5_jerk_v033_signal,
    f28dbk_f28_drilling_backlog_backg_84d_base_xc2_jsw5_jerk_v034_signal,
    f28dbk_f28_drilling_backlog_backscore_84d_base_xc2_jsw5_jerk_v035_signal,
    f28dbk_f28_drilling_backlog_backg_126d_base_xc2_jsw5_jerk_v036_signal,
    f28dbk_f28_drilling_backlog_backscore_126d_base_xc2_jsw5_jerk_v037_signal,
    f28dbk_f28_drilling_backlog_backg_189d_base_xc2_jsw5_jerk_v038_signal,
    f28dbk_f28_drilling_backlog_backscore_189d_base_xc2_jsw5_jerk_v039_signal,
    f28dbk_f28_drilling_backlog_backg_252d_base_xc2_jsw5_jerk_v040_signal,
    f28dbk_f28_drilling_backlog_backscore_252d_base_xc2_jsw5_jerk_v041_signal,
    f28dbk_f28_drilling_backlog_backg_378d_base_xc2_jsw5_jerk_v042_signal,
    f28dbk_f28_drilling_backlog_backscore_378d_base_xc2_jsw5_jerk_v043_signal,
    f28dbk_f28_drilling_backlog_backg_504d_base_xc2_jsw5_jerk_v044_signal,
    f28dbk_f28_drilling_backlog_backscore_504d_base_xc2_jsw5_jerk_v045_signal,
    f28dbk_f28_drilling_backlog_btr_base_xc2_jsw5_jerk_v046_signal,
    f28dbk_f28_drilling_backlog_backg_5d_base_xmc_jsw5_jerk_v047_signal,
    f28dbk_f28_drilling_backlog_backscore_5d_base_xmc_jsw5_jerk_v048_signal,
    f28dbk_f28_drilling_backlog_backg_10d_base_xmc_jsw5_jerk_v049_signal,
    f28dbk_f28_drilling_backlog_backscore_10d_base_xmc_jsw5_jerk_v050_signal,
    f28dbk_f28_drilling_backlog_backg_21d_base_xmc_jsw5_jerk_v051_signal,
    f28dbk_f28_drilling_backlog_backscore_21d_base_xmc_jsw5_jerk_v052_signal,
    f28dbk_f28_drilling_backlog_backg_42d_base_xmc_jsw5_jerk_v053_signal,
    f28dbk_f28_drilling_backlog_backscore_42d_base_xmc_jsw5_jerk_v054_signal,
    f28dbk_f28_drilling_backlog_backg_63d_base_xmc_jsw5_jerk_v055_signal,
    f28dbk_f28_drilling_backlog_backscore_63d_base_xmc_jsw5_jerk_v056_signal,
    f28dbk_f28_drilling_backlog_backg_84d_base_xmc_jsw5_jerk_v057_signal,
    f28dbk_f28_drilling_backlog_backscore_84d_base_xmc_jsw5_jerk_v058_signal,
    f28dbk_f28_drilling_backlog_backg_126d_base_xmc_jsw5_jerk_v059_signal,
    f28dbk_f28_drilling_backlog_backscore_126d_base_xmc_jsw5_jerk_v060_signal,
    f28dbk_f28_drilling_backlog_backg_189d_base_xmc_jsw5_jerk_v061_signal,
    f28dbk_f28_drilling_backlog_backscore_189d_base_xmc_jsw5_jerk_v062_signal,
    f28dbk_f28_drilling_backlog_backg_252d_base_xmc_jsw5_jerk_v063_signal,
    f28dbk_f28_drilling_backlog_backscore_252d_base_xmc_jsw5_jerk_v064_signal,
    f28dbk_f28_drilling_backlog_backg_378d_base_xmc_jsw5_jerk_v065_signal,
    f28dbk_f28_drilling_backlog_backscore_378d_base_xmc_jsw5_jerk_v066_signal,
    f28dbk_f28_drilling_backlog_backg_504d_base_xmc_jsw5_jerk_v067_signal,
    f28dbk_f28_drilling_backlog_backscore_504d_base_xmc_jsw5_jerk_v068_signal,
    f28dbk_f28_drilling_backlog_btr_base_xmc_jsw5_jerk_v069_signal,
    f28dbk_f28_drilling_backlog_backg_5d_base_xzc_jsw5_jerk_v070_signal,
    f28dbk_f28_drilling_backlog_backscore_5d_base_xzc_jsw5_jerk_v071_signal,
    f28dbk_f28_drilling_backlog_backg_10d_base_xzc_jsw5_jerk_v072_signal,
    f28dbk_f28_drilling_backlog_backscore_10d_base_xzc_jsw5_jerk_v073_signal,
    f28dbk_f28_drilling_backlog_backg_21d_base_xzc_jsw5_jerk_v074_signal,
    f28dbk_f28_drilling_backlog_backscore_21d_base_xzc_jsw5_jerk_v075_signal,
    f28dbk_f28_drilling_backlog_backg_42d_base_xzc_jsw5_jerk_v076_signal,
    f28dbk_f28_drilling_backlog_backscore_42d_base_xzc_jsw5_jerk_v077_signal,
    f28dbk_f28_drilling_backlog_backg_63d_base_xzc_jsw5_jerk_v078_signal,
    f28dbk_f28_drilling_backlog_backscore_63d_base_xzc_jsw5_jerk_v079_signal,
    f28dbk_f28_drilling_backlog_backg_84d_base_xzc_jsw5_jerk_v080_signal,
    f28dbk_f28_drilling_backlog_backscore_84d_base_xzc_jsw5_jerk_v081_signal,
    f28dbk_f28_drilling_backlog_backg_126d_base_xzc_jsw5_jerk_v082_signal,
    f28dbk_f28_drilling_backlog_backscore_126d_base_xzc_jsw5_jerk_v083_signal,
    f28dbk_f28_drilling_backlog_backg_189d_base_xzc_jsw5_jerk_v084_signal,
    f28dbk_f28_drilling_backlog_backscore_189d_base_xzc_jsw5_jerk_v085_signal,
    f28dbk_f28_drilling_backlog_backg_252d_base_xzc_jsw5_jerk_v086_signal,
    f28dbk_f28_drilling_backlog_backscore_252d_base_xzc_jsw5_jerk_v087_signal,
    f28dbk_f28_drilling_backlog_backg_378d_base_xzc_jsw5_jerk_v088_signal,
    f28dbk_f28_drilling_backlog_backscore_378d_base_xzc_jsw5_jerk_v089_signal,
    f28dbk_f28_drilling_backlog_backg_504d_base_xzc_jsw5_jerk_v090_signal,
    f28dbk_f28_drilling_backlog_backscore_504d_base_xzc_jsw5_jerk_v091_signal,
    f28dbk_f28_drilling_backlog_btr_base_xzc_jsw5_jerk_v092_signal,
    f28dbk_f28_drilling_backlog_backg_5d_base_dmc_jsw5_jerk_v093_signal,
    f28dbk_f28_drilling_backlog_backscore_5d_base_dmc_jsw5_jerk_v094_signal,
    f28dbk_f28_drilling_backlog_backg_10d_base_dmc_jsw5_jerk_v095_signal,
    f28dbk_f28_drilling_backlog_backscore_10d_base_dmc_jsw5_jerk_v096_signal,
    f28dbk_f28_drilling_backlog_backg_21d_base_dmc_jsw5_jerk_v097_signal,
    f28dbk_f28_drilling_backlog_backscore_21d_base_dmc_jsw5_jerk_v098_signal,
    f28dbk_f28_drilling_backlog_backg_42d_base_dmc_jsw5_jerk_v099_signal,
    f28dbk_f28_drilling_backlog_backscore_42d_base_dmc_jsw5_jerk_v100_signal,
    f28dbk_f28_drilling_backlog_backg_63d_base_dmc_jsw5_jerk_v101_signal,
    f28dbk_f28_drilling_backlog_backscore_63d_base_dmc_jsw5_jerk_v102_signal,
    f28dbk_f28_drilling_backlog_backg_84d_base_dmc_jsw5_jerk_v103_signal,
    f28dbk_f28_drilling_backlog_backscore_84d_base_dmc_jsw5_jerk_v104_signal,
    f28dbk_f28_drilling_backlog_backg_126d_base_dmc_jsw5_jerk_v105_signal,
    f28dbk_f28_drilling_backlog_backscore_126d_base_dmc_jsw5_jerk_v106_signal,
    f28dbk_f28_drilling_backlog_backg_189d_base_dmc_jsw5_jerk_v107_signal,
    f28dbk_f28_drilling_backlog_backscore_189d_base_dmc_jsw5_jerk_v108_signal,
    f28dbk_f28_drilling_backlog_backg_252d_base_dmc_jsw5_jerk_v109_signal,
    f28dbk_f28_drilling_backlog_backscore_252d_base_dmc_jsw5_jerk_v110_signal,
    f28dbk_f28_drilling_backlog_backg_378d_base_dmc_jsw5_jerk_v111_signal,
    f28dbk_f28_drilling_backlog_backscore_378d_base_dmc_jsw5_jerk_v112_signal,
    f28dbk_f28_drilling_backlog_backg_504d_base_dmc_jsw5_jerk_v113_signal,
    f28dbk_f28_drilling_backlog_backscore_504d_base_dmc_jsw5_jerk_v114_signal,
    f28dbk_f28_drilling_backlog_btr_base_dmc_jsw5_jerk_v115_signal,
    f28dbk_f28_drilling_backlog_backg_5d_m21_xc_jsw5_jerk_v116_signal,
    f28dbk_f28_drilling_backlog_backscore_5d_m21_xc_jsw5_jerk_v117_signal,
    f28dbk_f28_drilling_backlog_backg_10d_m21_xc_jsw5_jerk_v118_signal,
    f28dbk_f28_drilling_backlog_backscore_10d_m21_xc_jsw5_jerk_v119_signal,
    f28dbk_f28_drilling_backlog_backg_21d_m21_xc_jsw5_jerk_v120_signal,
    f28dbk_f28_drilling_backlog_backscore_21d_m21_xc_jsw5_jerk_v121_signal,
    f28dbk_f28_drilling_backlog_backg_42d_m21_xc_jsw5_jerk_v122_signal,
    f28dbk_f28_drilling_backlog_backscore_42d_m21_xc_jsw5_jerk_v123_signal,
    f28dbk_f28_drilling_backlog_backg_63d_m21_xc_jsw5_jerk_v124_signal,
    f28dbk_f28_drilling_backlog_backscore_63d_m21_xc_jsw5_jerk_v125_signal,
    f28dbk_f28_drilling_backlog_backg_84d_m21_xc_jsw5_jerk_v126_signal,
    f28dbk_f28_drilling_backlog_backscore_84d_m21_xc_jsw5_jerk_v127_signal,
    f28dbk_f28_drilling_backlog_backg_126d_m21_xc_jsw5_jerk_v128_signal,
    f28dbk_f28_drilling_backlog_backscore_126d_m21_xc_jsw5_jerk_v129_signal,
    f28dbk_f28_drilling_backlog_backg_189d_m21_xc_jsw5_jerk_v130_signal,
    f28dbk_f28_drilling_backlog_backscore_189d_m21_xc_jsw5_jerk_v131_signal,
    f28dbk_f28_drilling_backlog_backg_252d_m21_xc_jsw5_jerk_v132_signal,
    f28dbk_f28_drilling_backlog_backscore_252d_m21_xc_jsw5_jerk_v133_signal,
    f28dbk_f28_drilling_backlog_backg_378d_m21_xc_jsw5_jerk_v134_signal,
    f28dbk_f28_drilling_backlog_backscore_378d_m21_xc_jsw5_jerk_v135_signal,
    f28dbk_f28_drilling_backlog_backg_504d_m21_xc_jsw5_jerk_v136_signal,
    f28dbk_f28_drilling_backlog_backscore_504d_m21_xc_jsw5_jerk_v137_signal,
    f28dbk_f28_drilling_backlog_btr_m21_xc_jsw5_jerk_v138_signal,
    f28dbk_f28_drilling_backlog_backg_5d_m21_xc2_jsw5_jerk_v139_signal,
    f28dbk_f28_drilling_backlog_backscore_5d_m21_xc2_jsw5_jerk_v140_signal,
    f28dbk_f28_drilling_backlog_backg_10d_m21_xc2_jsw5_jerk_v141_signal,
    f28dbk_f28_drilling_backlog_backscore_10d_m21_xc2_jsw5_jerk_v142_signal,
    f28dbk_f28_drilling_backlog_backg_21d_m21_xc2_jsw5_jerk_v143_signal,
    f28dbk_f28_drilling_backlog_backscore_21d_m21_xc2_jsw5_jerk_v144_signal,
    f28dbk_f28_drilling_backlog_backg_42d_m21_xc2_jsw5_jerk_v145_signal,
    f28dbk_f28_drilling_backlog_backscore_42d_m21_xc2_jsw5_jerk_v146_signal,
    f28dbk_f28_drilling_backlog_backg_63d_m21_xc2_jsw5_jerk_v147_signal,
    f28dbk_f28_drilling_backlog_backscore_63d_m21_xc2_jsw5_jerk_v148_signal,
    f28dbk_f28_drilling_backlog_backg_84d_m21_xc2_jsw5_jerk_v149_signal,
    f28dbk_f28_drilling_backlog_backscore_84d_m21_xc2_jsw5_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_DRILLING_BACKLOG_REGISTRY_JERK_001_150 = REGISTRY


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
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda,
        "assets": assets, "equity": equity, "debt": debt, "cashneq": cashneq,
        "deferredrev": deferredrev, "ppnenet": ppnenet, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f28_backlog_growth', '_f28_backlog_to_revenue', '_f28_drilling_backlog_score',)
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
    print(f"OK f28_drilling_backlog_3rd_derivatives_001_150_claude: {n_features} features pass")
