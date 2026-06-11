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
def _f26_backlog_growth(deferredrev, w):
    return deferredrev.pct_change(periods=w)


def _f26_backlog_to_revenue(deferredrev, revenue):
    return deferredrev / revenue.replace(0, np.nan)


def _f26_backlog_acceleration(deferredrev, w):
    g1 = deferredrev.pct_change(periods=w)
    g2 = deferredrev.pct_change(periods=w).shift(w)
    return g1 - g2


# 3d slope of blggrowth base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowth_3d_slope_v001_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    base = g * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of blggrowth base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowth_5d_slope_v002_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    base = g * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of blggrowth base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowth_10d_slope_v003_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    base = g * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of blggrowth base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowth_21d_slope_v004_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    base = g * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of blggrowth base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowth_42d_slope_v005_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    base = g * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of blggrowth base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowth_63d_slope_v006_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    base = g * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of blggrowth base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowth_84d_slope_v007_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    base = g * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of blggrowth base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowth_126d_slope_v008_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    base = g * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of blggrowth base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowth_168d_slope_v009_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    base = g * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of blggrowth base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowth_189d_slope_v010_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 21)
    base = g * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of blggrowth base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowth_3d_slope_v011_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    base = g * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of blggrowth base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowth_5d_slope_v012_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    base = g * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of blggrowth base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowth_10d_slope_v013_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    base = g * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of blggrowth base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowth_21d_slope_v014_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    base = g * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of blggrowth base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowth_42d_slope_v015_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    base = g * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of blggrowth base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowth_63d_slope_v016_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    base = g * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of blggrowth base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowth_84d_slope_v017_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    base = g * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of blggrowth base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowth_126d_slope_v018_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    base = g * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of blggrowth base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowth_168d_slope_v019_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    base = g * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of blggrowth base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowth_189d_slope_v020_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 63)
    base = g * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of blggrowth base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowth_3d_slope_v021_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 252)
    base = g * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of blggrowth base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowth_5d_slope_v022_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 252)
    base = g * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of blggrowth base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowth_10d_slope_v023_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 252)
    base = g * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of blggrowth base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowth_21d_slope_v024_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 252)
    base = g * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of blggrowth base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowth_42d_slope_v025_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 252)
    base = g * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of blggrowth base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowth_63d_slope_v026_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 252)
    base = g * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of blggrowth base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowth_84d_slope_v027_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 252)
    base = g * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of blggrowth base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowth_126d_slope_v028_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 252)
    base = g * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of blggrowth base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowth_168d_slope_v029_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 252)
    base = g * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of blggrowth base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowth_189d_slope_v030_signal(deferredrev, closeadj):
    g = _f26_backlog_growth(deferredrev, 252)
    base = g * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of blgtorev base_w=21
def f26cbg_f26_cro_backlog_growth_blgtorev_3d_slope_v031_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(21, min_periods=11).mean() * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of blgtorev base_w=21
def f26cbg_f26_cro_backlog_growth_blgtorev_5d_slope_v032_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(21, min_periods=11).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of blgtorev base_w=21
def f26cbg_f26_cro_backlog_growth_blgtorev_10d_slope_v033_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(21, min_periods=11).mean() * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of blgtorev base_w=21
def f26cbg_f26_cro_backlog_growth_blgtorev_21d_slope_v034_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(21, min_periods=11).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of blgtorev base_w=21
def f26cbg_f26_cro_backlog_growth_blgtorev_42d_slope_v035_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(21, min_periods=11).mean() * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of blgtorev base_w=21
def f26cbg_f26_cro_backlog_growth_blgtorev_63d_slope_v036_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(21, min_periods=11).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of blgtorev base_w=21
def f26cbg_f26_cro_backlog_growth_blgtorev_84d_slope_v037_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(21, min_periods=11).mean() * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of blgtorev base_w=21
def f26cbg_f26_cro_backlog_growth_blgtorev_126d_slope_v038_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(21, min_periods=11).mean() * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of blgtorev base_w=21
def f26cbg_f26_cro_backlog_growth_blgtorev_168d_slope_v039_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(21, min_periods=11).mean() * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of blgtorev base_w=21
def f26cbg_f26_cro_backlog_growth_blgtorev_189d_slope_v040_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(21, min_periods=11).mean() * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of blgtorev base_w=63
def f26cbg_f26_cro_backlog_growth_blgtorev_3d_slope_v041_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(63, min_periods=32).mean() * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of blgtorev base_w=63
def f26cbg_f26_cro_backlog_growth_blgtorev_5d_slope_v042_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(63, min_periods=32).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of blgtorev base_w=63
def f26cbg_f26_cro_backlog_growth_blgtorev_10d_slope_v043_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(63, min_periods=32).mean() * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of blgtorev base_w=63
def f26cbg_f26_cro_backlog_growth_blgtorev_21d_slope_v044_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(63, min_periods=32).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of blgtorev base_w=63
def f26cbg_f26_cro_backlog_growth_blgtorev_42d_slope_v045_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(63, min_periods=32).mean() * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of blgtorev base_w=63
def f26cbg_f26_cro_backlog_growth_blgtorev_63d_slope_v046_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(63, min_periods=32).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of blgtorev base_w=63
def f26cbg_f26_cro_backlog_growth_blgtorev_84d_slope_v047_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(63, min_periods=32).mean() * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of blgtorev base_w=63
def f26cbg_f26_cro_backlog_growth_blgtorev_126d_slope_v048_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(63, min_periods=32).mean() * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of blgtorev base_w=63
def f26cbg_f26_cro_backlog_growth_blgtorev_168d_slope_v049_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(63, min_periods=32).mean() * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of blgtorev base_w=63
def f26cbg_f26_cro_backlog_growth_blgtorev_189d_slope_v050_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(63, min_periods=32).mean() * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of blgtorev base_w=252
def f26cbg_f26_cro_backlog_growth_blgtorev_3d_slope_v051_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(252, min_periods=126).mean() * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of blgtorev base_w=252
def f26cbg_f26_cro_backlog_growth_blgtorev_5d_slope_v052_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(252, min_periods=126).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of blgtorev base_w=252
def f26cbg_f26_cro_backlog_growth_blgtorev_10d_slope_v053_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(252, min_periods=126).mean() * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of blgtorev base_w=252
def f26cbg_f26_cro_backlog_growth_blgtorev_21d_slope_v054_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(252, min_periods=126).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of blgtorev base_w=252
def f26cbg_f26_cro_backlog_growth_blgtorev_42d_slope_v055_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(252, min_periods=126).mean() * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of blgtorev base_w=252
def f26cbg_f26_cro_backlog_growth_blgtorev_63d_slope_v056_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(252, min_periods=126).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of blgtorev base_w=252
def f26cbg_f26_cro_backlog_growth_blgtorev_84d_slope_v057_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(252, min_periods=126).mean() * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of blgtorev base_w=252
def f26cbg_f26_cro_backlog_growth_blgtorev_126d_slope_v058_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(252, min_periods=126).mean() * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of blgtorev base_w=252
def f26cbg_f26_cro_backlog_growth_blgtorev_168d_slope_v059_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(252, min_periods=126).mean() * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of blgtorev base_w=252
def f26cbg_f26_cro_backlog_growth_blgtorev_189d_slope_v060_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(252, min_periods=126).mean() * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of blgaccel base_w=21
def f26cbg_f26_cro_backlog_growth_blgaccel_3d_slope_v061_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 21)
    base = a * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of blgaccel base_w=21
def f26cbg_f26_cro_backlog_growth_blgaccel_5d_slope_v062_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 21)
    base = a * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of blgaccel base_w=21
def f26cbg_f26_cro_backlog_growth_blgaccel_10d_slope_v063_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 21)
    base = a * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of blgaccel base_w=21
def f26cbg_f26_cro_backlog_growth_blgaccel_21d_slope_v064_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 21)
    base = a * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of blgaccel base_w=21
def f26cbg_f26_cro_backlog_growth_blgaccel_42d_slope_v065_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 21)
    base = a * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of blgaccel base_w=21
def f26cbg_f26_cro_backlog_growth_blgaccel_63d_slope_v066_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 21)
    base = a * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of blgaccel base_w=21
def f26cbg_f26_cro_backlog_growth_blgaccel_84d_slope_v067_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 21)
    base = a * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of blgaccel base_w=21
def f26cbg_f26_cro_backlog_growth_blgaccel_126d_slope_v068_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 21)
    base = a * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of blgaccel base_w=21
def f26cbg_f26_cro_backlog_growth_blgaccel_168d_slope_v069_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 21)
    base = a * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of blgaccel base_w=21
def f26cbg_f26_cro_backlog_growth_blgaccel_189d_slope_v070_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 21)
    base = a * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of blgaccel base_w=63
def f26cbg_f26_cro_backlog_growth_blgaccel_3d_slope_v071_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 63)
    base = a * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of blgaccel base_w=63
def f26cbg_f26_cro_backlog_growth_blgaccel_5d_slope_v072_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 63)
    base = a * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of blgaccel base_w=63
def f26cbg_f26_cro_backlog_growth_blgaccel_10d_slope_v073_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 63)
    base = a * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of blgaccel base_w=63
def f26cbg_f26_cro_backlog_growth_blgaccel_21d_slope_v074_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 63)
    base = a * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of blgaccel base_w=63
def f26cbg_f26_cro_backlog_growth_blgaccel_42d_slope_v075_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 63)
    base = a * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of blgaccel base_w=63
def f26cbg_f26_cro_backlog_growth_blgaccel_63d_slope_v076_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 63)
    base = a * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of blgaccel base_w=63
def f26cbg_f26_cro_backlog_growth_blgaccel_84d_slope_v077_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 63)
    base = a * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of blgaccel base_w=63
def f26cbg_f26_cro_backlog_growth_blgaccel_126d_slope_v078_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 63)
    base = a * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of blgaccel base_w=63
def f26cbg_f26_cro_backlog_growth_blgaccel_168d_slope_v079_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 63)
    base = a * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of blgaccel base_w=63
def f26cbg_f26_cro_backlog_growth_blgaccel_189d_slope_v080_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 63)
    base = a * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of blgaccel base_w=252
def f26cbg_f26_cro_backlog_growth_blgaccel_3d_slope_v081_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 252)
    base = a * closeadj
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of blgaccel base_w=252
def f26cbg_f26_cro_backlog_growth_blgaccel_5d_slope_v082_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 252)
    base = a * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of blgaccel base_w=252
def f26cbg_f26_cro_backlog_growth_blgaccel_10d_slope_v083_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 252)
    base = a * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of blgaccel base_w=252
def f26cbg_f26_cro_backlog_growth_blgaccel_21d_slope_v084_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 252)
    base = a * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of blgaccel base_w=252
def f26cbg_f26_cro_backlog_growth_blgaccel_42d_slope_v085_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 252)
    base = a * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of blgaccel base_w=252
def f26cbg_f26_cro_backlog_growth_blgaccel_63d_slope_v086_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 252)
    base = a * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of blgaccel base_w=252
def f26cbg_f26_cro_backlog_growth_blgaccel_84d_slope_v087_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 252)
    base = a * closeadj
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of blgaccel base_w=252
def f26cbg_f26_cro_backlog_growth_blgaccel_126d_slope_v088_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 252)
    base = a * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of blgaccel base_w=252
def f26cbg_f26_cro_backlog_growth_blgaccel_168d_slope_v089_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 252)
    base = a * closeadj
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of blgaccel base_w=252
def f26cbg_f26_cro_backlog_growth_blgaccel_189d_slope_v090_signal(deferredrev, closeadj):
    a = _f26_backlog_acceleration(deferredrev, 252)
    base = a * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of blggrowthxrev base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_3d_slope_v091_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of blggrowthxrev base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_5d_slope_v092_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of blggrowthxrev base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_10d_slope_v093_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of blggrowthxrev base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_21d_slope_v094_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of blggrowthxrev base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_42d_slope_v095_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of blggrowthxrev base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_63d_slope_v096_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of blggrowthxrev base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_84d_slope_v097_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of blggrowthxrev base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_126d_slope_v098_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of blggrowthxrev base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_168d_slope_v099_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of blggrowthxrev base_w=21
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_189d_slope_v100_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of blggrowthxrev base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_3d_slope_v101_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of blggrowthxrev base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_5d_slope_v102_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of blggrowthxrev base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_10d_slope_v103_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of blggrowthxrev base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_21d_slope_v104_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of blggrowthxrev base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_42d_slope_v105_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of blggrowthxrev base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_63d_slope_v106_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of blggrowthxrev base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_84d_slope_v107_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of blggrowthxrev base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_126d_slope_v108_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of blggrowthxrev base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_168d_slope_v109_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of blggrowthxrev base_w=63
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_189d_slope_v110_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of blggrowthxrev base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_3d_slope_v111_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of blggrowthxrev base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_5d_slope_v112_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of blggrowthxrev base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_10d_slope_v113_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of blggrowthxrev base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_21d_slope_v114_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of blggrowthxrev base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_42d_slope_v115_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of blggrowthxrev base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_63d_slope_v116_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of blggrowthxrev base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_84d_slope_v117_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of blggrowthxrev base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_126d_slope_v118_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of blggrowthxrev base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_168d_slope_v119_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of blggrowthxrev base_w=252
def f26cbg_f26_cro_backlog_growth_blggrowthxrev_189d_slope_v120_signal(deferredrev, revenue):
    g = _f26_backlog_growth(deferredrev, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = g * rm / 1e9
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of blgtorevsq base_w=42
def f26cbg_f26_cro_backlog_growth_blgtorevsq_3d_slope_v121_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(42, min_periods=21).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of blgtorevsq base_w=42
def f26cbg_f26_cro_backlog_growth_blgtorevsq_5d_slope_v122_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(42, min_periods=21).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of blgtorevsq base_w=42
def f26cbg_f26_cro_backlog_growth_blgtorevsq_10d_slope_v123_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(42, min_periods=21).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of blgtorevsq base_w=42
def f26cbg_f26_cro_backlog_growth_blgtorevsq_21d_slope_v124_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(42, min_periods=21).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of blgtorevsq base_w=42
def f26cbg_f26_cro_backlog_growth_blgtorevsq_42d_slope_v125_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(42, min_periods=21).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of blgtorevsq base_w=42
def f26cbg_f26_cro_backlog_growth_blgtorevsq_63d_slope_v126_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(42, min_periods=21).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of blgtorevsq base_w=42
def f26cbg_f26_cro_backlog_growth_blgtorevsq_84d_slope_v127_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(42, min_periods=21).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of blgtorevsq base_w=42
def f26cbg_f26_cro_backlog_growth_blgtorevsq_126d_slope_v128_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(42, min_periods=21).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of blgtorevsq base_w=42
def f26cbg_f26_cro_backlog_growth_blgtorevsq_168d_slope_v129_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(42, min_periods=21).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of blgtorevsq base_w=42
def f26cbg_f26_cro_backlog_growth_blgtorevsq_189d_slope_v130_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(42, min_periods=21).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of blgtorevsq base_w=126
def f26cbg_f26_cro_backlog_growth_blgtorevsq_3d_slope_v131_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(126, min_periods=63).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of blgtorevsq base_w=126
def f26cbg_f26_cro_backlog_growth_blgtorevsq_5d_slope_v132_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(126, min_periods=63).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of blgtorevsq base_w=126
def f26cbg_f26_cro_backlog_growth_blgtorevsq_10d_slope_v133_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(126, min_periods=63).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of blgtorevsq base_w=126
def f26cbg_f26_cro_backlog_growth_blgtorevsq_21d_slope_v134_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(126, min_periods=63).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of blgtorevsq base_w=126
def f26cbg_f26_cro_backlog_growth_blgtorevsq_42d_slope_v135_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(126, min_periods=63).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of blgtorevsq base_w=126
def f26cbg_f26_cro_backlog_growth_blgtorevsq_63d_slope_v136_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(126, min_periods=63).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of blgtorevsq base_w=126
def f26cbg_f26_cro_backlog_growth_blgtorevsq_84d_slope_v137_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(126, min_periods=63).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of blgtorevsq base_w=126
def f26cbg_f26_cro_backlog_growth_blgtorevsq_126d_slope_v138_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(126, min_periods=63).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of blgtorevsq base_w=126
def f26cbg_f26_cro_backlog_growth_blgtorevsq_168d_slope_v139_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(126, min_periods=63).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of blgtorevsq base_w=126
def f26cbg_f26_cro_backlog_growth_blgtorevsq_189d_slope_v140_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(126, min_periods=63).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d slope of blgtorevsq base_w=504
def f26cbg_f26_cro_backlog_growth_blgtorevsq_3d_slope_v141_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(504, min_periods=252).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of blgtorevsq base_w=504
def f26cbg_f26_cro_backlog_growth_blgtorevsq_5d_slope_v142_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(504, min_periods=252).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d slope of blgtorevsq base_w=504
def f26cbg_f26_cro_backlog_growth_blgtorevsq_10d_slope_v143_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(504, min_periods=252).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of blgtorevsq base_w=504
def f26cbg_f26_cro_backlog_growth_blgtorevsq_21d_slope_v144_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(504, min_periods=252).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d slope of blgtorevsq base_w=504
def f26cbg_f26_cro_backlog_growth_blgtorevsq_42d_slope_v145_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(504, min_periods=252).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of blgtorevsq base_w=504
def f26cbg_f26_cro_backlog_growth_blgtorevsq_63d_slope_v146_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(504, min_periods=252).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d slope of blgtorevsq base_w=504
def f26cbg_f26_cro_backlog_growth_blgtorevsq_84d_slope_v147_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(504, min_periods=252).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of blgtorevsq base_w=504
def f26cbg_f26_cro_backlog_growth_blgtorevsq_126d_slope_v148_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(504, min_periods=252).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d slope of blgtorevsq base_w=504
def f26cbg_f26_cro_backlog_growth_blgtorevsq_168d_slope_v149_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(504, min_periods=252).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d slope of blgtorevsq base_w=504
def f26cbg_f26_cro_backlog_growth_blgtorevsq_189d_slope_v150_signal(deferredrev, revenue, closeadj):
    br = _f26_backlog_to_revenue(deferredrev, revenue)
    base = br.rolling(504, min_periods=252).mean() * closeadj * closeadj / 100.0
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f26cbg_f26_cro_backlog_growth_blggrowth_3d_slope_v001_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_5d_slope_v002_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_10d_slope_v003_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_21d_slope_v004_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_42d_slope_v005_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_63d_slope_v006_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_84d_slope_v007_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_126d_slope_v008_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_168d_slope_v009_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_189d_slope_v010_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_3d_slope_v011_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_5d_slope_v012_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_10d_slope_v013_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_21d_slope_v014_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_42d_slope_v015_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_63d_slope_v016_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_84d_slope_v017_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_126d_slope_v018_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_168d_slope_v019_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_189d_slope_v020_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_3d_slope_v021_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_5d_slope_v022_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_10d_slope_v023_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_21d_slope_v024_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_42d_slope_v025_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_63d_slope_v026_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_84d_slope_v027_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_126d_slope_v028_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_168d_slope_v029_signal,
    f26cbg_f26_cro_backlog_growth_blggrowth_189d_slope_v030_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_3d_slope_v031_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_5d_slope_v032_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_10d_slope_v033_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_21d_slope_v034_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_42d_slope_v035_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_63d_slope_v036_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_84d_slope_v037_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_126d_slope_v038_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_168d_slope_v039_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_189d_slope_v040_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_3d_slope_v041_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_5d_slope_v042_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_10d_slope_v043_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_21d_slope_v044_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_42d_slope_v045_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_63d_slope_v046_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_84d_slope_v047_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_126d_slope_v048_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_168d_slope_v049_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_189d_slope_v050_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_3d_slope_v051_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_5d_slope_v052_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_10d_slope_v053_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_21d_slope_v054_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_42d_slope_v055_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_63d_slope_v056_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_84d_slope_v057_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_126d_slope_v058_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_168d_slope_v059_signal,
    f26cbg_f26_cro_backlog_growth_blgtorev_189d_slope_v060_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_3d_slope_v061_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_5d_slope_v062_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_10d_slope_v063_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_21d_slope_v064_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_42d_slope_v065_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_63d_slope_v066_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_84d_slope_v067_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_126d_slope_v068_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_168d_slope_v069_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_189d_slope_v070_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_3d_slope_v071_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_5d_slope_v072_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_10d_slope_v073_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_21d_slope_v074_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_42d_slope_v075_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_63d_slope_v076_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_84d_slope_v077_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_126d_slope_v078_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_168d_slope_v079_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_189d_slope_v080_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_3d_slope_v081_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_5d_slope_v082_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_10d_slope_v083_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_21d_slope_v084_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_42d_slope_v085_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_63d_slope_v086_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_84d_slope_v087_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_126d_slope_v088_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_168d_slope_v089_signal,
    f26cbg_f26_cro_backlog_growth_blgaccel_189d_slope_v090_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_3d_slope_v091_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_5d_slope_v092_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_10d_slope_v093_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_21d_slope_v094_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_42d_slope_v095_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_63d_slope_v096_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_84d_slope_v097_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_126d_slope_v098_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_168d_slope_v099_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_189d_slope_v100_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_3d_slope_v101_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_5d_slope_v102_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_10d_slope_v103_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_21d_slope_v104_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_42d_slope_v105_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_63d_slope_v106_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_84d_slope_v107_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_126d_slope_v108_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_168d_slope_v109_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_189d_slope_v110_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_3d_slope_v111_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_5d_slope_v112_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_10d_slope_v113_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_21d_slope_v114_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_42d_slope_v115_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_63d_slope_v116_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_84d_slope_v117_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_126d_slope_v118_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_168d_slope_v119_signal,
    f26cbg_f26_cro_backlog_growth_blggrowthxrev_189d_slope_v120_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_3d_slope_v121_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_5d_slope_v122_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_10d_slope_v123_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_21d_slope_v124_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_42d_slope_v125_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_63d_slope_v126_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_84d_slope_v127_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_126d_slope_v128_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_168d_slope_v129_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_189d_slope_v130_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_3d_slope_v131_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_5d_slope_v132_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_10d_slope_v133_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_21d_slope_v134_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_42d_slope_v135_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_63d_slope_v136_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_84d_slope_v137_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_126d_slope_v138_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_168d_slope_v139_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_189d_slope_v140_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_3d_slope_v141_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_5d_slope_v142_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_10d_slope_v143_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_21d_slope_v144_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_42d_slope_v145_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_63d_slope_v146_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_84d_slope_v147_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_126d_slope_v148_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_168d_slope_v149_signal,
    f26cbg_f26_cro_backlog_growth_blgtorevsq_189d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_CRO_BACKLOG_GROWTH_REGISTRY_SLOPE_001_150 = REGISTRY


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
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "fcf": fcf, "capex": capex,
        "deferredrev": deferredrev,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f26_backlog_growth", "_f26_backlog_to_revenue", "_f26_backlog_acceleration",)
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
    print(f"OK f26_cro_backlog_growth_2nd_derivatives_001_150_claude: {n_features} features pass")
