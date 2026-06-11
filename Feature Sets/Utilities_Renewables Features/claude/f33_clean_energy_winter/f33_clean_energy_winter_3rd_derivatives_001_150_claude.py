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
def _f33_revenue_drawdown(revenue, w):
    pk = revenue.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan)
    return (revenue - pk) / pk.abs()


def _f33_collapse_signature(revenue, ebitda, w):
    pk_r = revenue.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan)
    pk_e = ebitda.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan)
    return ((revenue - pk_r) / pk_r.abs()) + ((ebitda - pk_e) / pk_e.abs())


def _f33_winter_score(revenue, fcf, w):
    rdd = (revenue - revenue.rolling(w, min_periods=max(1, w // 2)).max()) / revenue.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan).abs()
    fcf_neg = (fcf < 0).astype(float)
    return rdd.abs() * (1.0 + fcf_neg)

def f33cew_f33_clean_energy_winter_p0_xcls_jk5_10d_jerk_v001_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_jk25_10d_jerk_v002_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj
    result = _jerk(base, 5).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_jksgn5_10d_jerk_v003_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj
    result = np.sign(_jerk(base, 5)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_jk21_10d_jerk_v004_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_jk221_10d_jerk_v005_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj
    result = _jerk(base, 21).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_jksgn21_10d_jerk_v006_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj
    result = np.sign(_jerk(base, 21)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_jk63_10d_jerk_v007_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_jk263_10d_jerk_v008_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj
    result = _jerk(base, 63).rolling(31, min_periods=max(1, 31//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_jksgn63_10d_jerk_v009_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj
    result = np.sign(_jerk(base, 63)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_jk126_10d_jerk_v010_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_jk2126_10d_jerk_v011_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj
    result = _jerk(base, 126).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_jksgn126_10d_jerk_v012_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj
    result = np.sign(_jerk(base, 126)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_jk5_10d_jerk_v013_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_jk25_10d_jerk_v014_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).abs() * closeadj
    result = _jerk(base, 5).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_jksgn5_10d_jerk_v015_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).abs() * closeadj
    result = np.sign(_jerk(base, 5)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_jk21_10d_jerk_v016_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_jk221_10d_jerk_v017_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).abs() * closeadj
    result = _jerk(base, 21).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_jksgn21_10d_jerk_v018_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).abs() * closeadj
    result = np.sign(_jerk(base, 21)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_jk63_10d_jerk_v019_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_jk263_10d_jerk_v020_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).abs() * closeadj
    result = _jerk(base, 63).rolling(31, min_periods=max(1, 31//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_jksgn63_10d_jerk_v021_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).abs() * closeadj
    result = np.sign(_jerk(base, 63)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_jk126_10d_jerk_v022_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_jk2126_10d_jerk_v023_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).abs() * closeadj
    result = _jerk(base, 126).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_jksgn126_10d_jerk_v024_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).abs() * closeadj
    result = np.sign(_jerk(base, 126)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_jk5_10d_jerk_v025_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * (_f33_revenue_drawdown(revenue, 10)).abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_jk25_10d_jerk_v026_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * (_f33_revenue_drawdown(revenue, 10)).abs()
    result = _jerk(base, 5).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_jksgn5_10d_jerk_v027_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * (_f33_revenue_drawdown(revenue, 10)).abs()
    result = np.sign(_jerk(base, 5)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_jk21_10d_jerk_v028_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * (_f33_revenue_drawdown(revenue, 10)).abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_jk221_10d_jerk_v029_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * (_f33_revenue_drawdown(revenue, 10)).abs()
    result = _jerk(base, 21).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_jksgn21_10d_jerk_v030_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * (_f33_revenue_drawdown(revenue, 10)).abs()
    result = np.sign(_jerk(base, 21)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_jk63_10d_jerk_v031_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * (_f33_revenue_drawdown(revenue, 10)).abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_jk263_10d_jerk_v032_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * (_f33_revenue_drawdown(revenue, 10)).abs()
    result = _jerk(base, 63).rolling(31, min_periods=max(1, 31//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_jksgn63_10d_jerk_v033_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * (_f33_revenue_drawdown(revenue, 10)).abs()
    result = np.sign(_jerk(base, 63)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_jk126_10d_jerk_v034_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * (_f33_revenue_drawdown(revenue, 10)).abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_jk2126_10d_jerk_v035_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * (_f33_revenue_drawdown(revenue, 10)).abs()
    result = _jerk(base, 126).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_jksgn126_10d_jerk_v036_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * (_f33_revenue_drawdown(revenue, 10)).abs()
    result = np.sign(_jerk(base, 126)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_jk5_10d_jerk_v037_signal(closeadj, revenue):
    base = _mean(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_jk25_10d_jerk_v038_signal(closeadj, revenue):
    base = _mean(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 5).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_jksgn5_10d_jerk_v039_signal(closeadj, revenue):
    base = _mean(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = np.sign(_jerk(base, 5)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_jk21_10d_jerk_v040_signal(closeadj, revenue):
    base = _mean(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_jk221_10d_jerk_v041_signal(closeadj, revenue):
    base = _mean(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 21).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_jksgn21_10d_jerk_v042_signal(closeadj, revenue):
    base = _mean(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = np.sign(_jerk(base, 21)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_jk63_10d_jerk_v043_signal(closeadj, revenue):
    base = _mean(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_jk263_10d_jerk_v044_signal(closeadj, revenue):
    base = _mean(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 63).rolling(31, min_periods=max(1, 31//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_jksgn63_10d_jerk_v045_signal(closeadj, revenue):
    base = _mean(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = np.sign(_jerk(base, 63)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_jk126_10d_jerk_v046_signal(closeadj, revenue):
    base = _mean(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_jk2126_10d_jerk_v047_signal(closeadj, revenue):
    base = _mean(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 126).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_jksgn126_10d_jerk_v048_signal(closeadj, revenue):
    base = _mean(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = np.sign(_jerk(base, 126)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_jk5_10d_jerk_v049_signal(closeadj, revenue):
    base = _std(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_jk25_10d_jerk_v050_signal(closeadj, revenue):
    base = _std(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 5).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_jksgn5_10d_jerk_v051_signal(closeadj, revenue):
    base = _std(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = np.sign(_jerk(base, 5)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_jk21_10d_jerk_v052_signal(closeadj, revenue):
    base = _std(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_jk221_10d_jerk_v053_signal(closeadj, revenue):
    base = _std(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 21).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_jksgn21_10d_jerk_v054_signal(closeadj, revenue):
    base = _std(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = np.sign(_jerk(base, 21)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_jk63_10d_jerk_v055_signal(closeadj, revenue):
    base = _std(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_jk263_10d_jerk_v056_signal(closeadj, revenue):
    base = _std(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 63).rolling(31, min_periods=max(1, 31//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_jksgn63_10d_jerk_v057_signal(closeadj, revenue):
    base = _std(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = np.sign(_jerk(base, 63)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_jk126_10d_jerk_v058_signal(closeadj, revenue):
    base = _std(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_jk2126_10d_jerk_v059_signal(closeadj, revenue):
    base = _std(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 126).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_jksgn126_10d_jerk_v060_signal(closeadj, revenue):
    base = _std(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = np.sign(_jerk(base, 126)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_jk5_10d_jerk_v061_signal(closeadj, revenue):
    base = _z(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_jk25_10d_jerk_v062_signal(closeadj, revenue):
    base = _z(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 5).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_jksgn5_10d_jerk_v063_signal(closeadj, revenue):
    base = _z(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = np.sign(_jerk(base, 5)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_jk21_10d_jerk_v064_signal(closeadj, revenue):
    base = _z(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_jk221_10d_jerk_v065_signal(closeadj, revenue):
    base = _z(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 21).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_jksgn21_10d_jerk_v066_signal(closeadj, revenue):
    base = _z(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = np.sign(_jerk(base, 21)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_jk63_10d_jerk_v067_signal(closeadj, revenue):
    base = _z(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_jk263_10d_jerk_v068_signal(closeadj, revenue):
    base = _z(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 63).rolling(31, min_periods=max(1, 31//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_jksgn63_10d_jerk_v069_signal(closeadj, revenue):
    base = _z(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = np.sign(_jerk(base, 63)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_jk126_10d_jerk_v070_signal(closeadj, revenue):
    base = _z(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_jk2126_10d_jerk_v071_signal(closeadj, revenue):
    base = _z(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = _jerk(base, 126).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_jksgn126_10d_jerk_v072_signal(closeadj, revenue):
    base = _z(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    result = np.sign(_jerk(base, 126)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_jk5_10d_jerk_v073_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).ewm(span=5, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_jk25_10d_jerk_v074_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).ewm(span=5, adjust=False).mean() * closeadj
    result = _jerk(base, 5).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_jksgn5_10d_jerk_v075_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).ewm(span=5, adjust=False).mean() * closeadj
    result = np.sign(_jerk(base, 5)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_jk21_10d_jerk_v076_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).ewm(span=5, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_jk221_10d_jerk_v077_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).ewm(span=5, adjust=False).mean() * closeadj
    result = _jerk(base, 21).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_jksgn21_10d_jerk_v078_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).ewm(span=5, adjust=False).mean() * closeadj
    result = np.sign(_jerk(base, 21)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_jk63_10d_jerk_v079_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).ewm(span=5, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_jk263_10d_jerk_v080_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).ewm(span=5, adjust=False).mean() * closeadj
    result = _jerk(base, 63).rolling(31, min_periods=max(1, 31//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_jksgn63_10d_jerk_v081_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).ewm(span=5, adjust=False).mean() * closeadj
    result = np.sign(_jerk(base, 63)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_jk126_10d_jerk_v082_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).ewm(span=5, adjust=False).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_jk2126_10d_jerk_v083_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).ewm(span=5, adjust=False).mean() * closeadj
    result = _jerk(base, 126).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_jksgn126_10d_jerk_v084_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).ewm(span=5, adjust=False).mean() * closeadj
    result = np.sign(_jerk(base, 126)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_jk5_10d_jerk_v085_signal(closeadj, revenue):
    base = np.log((_f33_revenue_drawdown(revenue, 10)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_jk25_10d_jerk_v086_signal(closeadj, revenue):
    base = np.log((_f33_revenue_drawdown(revenue, 10)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _jerk(base, 5).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_jksgn5_10d_jerk_v087_signal(closeadj, revenue):
    base = np.log((_f33_revenue_drawdown(revenue, 10)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = np.sign(_jerk(base, 5)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_jk21_10d_jerk_v088_signal(closeadj, revenue):
    base = np.log((_f33_revenue_drawdown(revenue, 10)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_jk221_10d_jerk_v089_signal(closeadj, revenue):
    base = np.log((_f33_revenue_drawdown(revenue, 10)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _jerk(base, 21).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_jksgn21_10d_jerk_v090_signal(closeadj, revenue):
    base = np.log((_f33_revenue_drawdown(revenue, 10)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = np.sign(_jerk(base, 21)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_jk63_10d_jerk_v091_signal(closeadj, revenue):
    base = np.log((_f33_revenue_drawdown(revenue, 10)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_jk263_10d_jerk_v092_signal(closeadj, revenue):
    base = np.log((_f33_revenue_drawdown(revenue, 10)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _jerk(base, 63).rolling(31, min_periods=max(1, 31//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_jksgn63_10d_jerk_v093_signal(closeadj, revenue):
    base = np.log((_f33_revenue_drawdown(revenue, 10)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = np.sign(_jerk(base, 63)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_jk126_10d_jerk_v094_signal(closeadj, revenue):
    base = np.log((_f33_revenue_drawdown(revenue, 10)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_jk2126_10d_jerk_v095_signal(closeadj, revenue):
    base = np.log((_f33_revenue_drawdown(revenue, 10)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = _jerk(base, 126).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_jksgn126_10d_jerk_v096_signal(closeadj, revenue):
    base = np.log((_f33_revenue_drawdown(revenue, 10)).abs().replace(0, np.nan) + 1.0) * closeadj
    result = np.sign(_jerk(base, 126)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_jk5_10d_jerk_v097_signal(closeadj, revenue):
    base = np.sign(_f33_revenue_drawdown(revenue, 10)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 10)).abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_jk25_10d_jerk_v098_signal(closeadj, revenue):
    base = np.sign(_f33_revenue_drawdown(revenue, 10)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 10)).abs())
    result = _jerk(base, 5).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_jksgn5_10d_jerk_v099_signal(closeadj, revenue):
    base = np.sign(_f33_revenue_drawdown(revenue, 10)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 10)).abs())
    result = np.sign(_jerk(base, 5)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_jk21_10d_jerk_v100_signal(closeadj, revenue):
    base = np.sign(_f33_revenue_drawdown(revenue, 10)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 10)).abs())
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_jk221_10d_jerk_v101_signal(closeadj, revenue):
    base = np.sign(_f33_revenue_drawdown(revenue, 10)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 10)).abs())
    result = _jerk(base, 21).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_jksgn21_10d_jerk_v102_signal(closeadj, revenue):
    base = np.sign(_f33_revenue_drawdown(revenue, 10)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 10)).abs())
    result = np.sign(_jerk(base, 21)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_jk63_10d_jerk_v103_signal(closeadj, revenue):
    base = np.sign(_f33_revenue_drawdown(revenue, 10)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 10)).abs())
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_jk263_10d_jerk_v104_signal(closeadj, revenue):
    base = np.sign(_f33_revenue_drawdown(revenue, 10)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 10)).abs())
    result = _jerk(base, 63).rolling(31, min_periods=max(1, 31//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_jksgn63_10d_jerk_v105_signal(closeadj, revenue):
    base = np.sign(_f33_revenue_drawdown(revenue, 10)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 10)).abs())
    result = np.sign(_jerk(base, 63)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_jk126_10d_jerk_v106_signal(closeadj, revenue):
    base = np.sign(_f33_revenue_drawdown(revenue, 10)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 10)).abs())
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_jk2126_10d_jerk_v107_signal(closeadj, revenue):
    base = np.sign(_f33_revenue_drawdown(revenue, 10)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 10)).abs())
    result = _jerk(base, 126).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_jksgn126_10d_jerk_v108_signal(closeadj, revenue):
    base = np.sign(_f33_revenue_drawdown(revenue, 10)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 10)).abs())
    result = np.sign(_jerk(base, 126)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_jk5_10d_jerk_v109_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * closeadj.pct_change(5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_jk25_10d_jerk_v110_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * closeadj.pct_change(5)
    result = _jerk(base, 5).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_jksgn5_10d_jerk_v111_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * closeadj.pct_change(5)
    result = np.sign(_jerk(base, 5)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_jk21_10d_jerk_v112_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * closeadj.pct_change(5)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_jk221_10d_jerk_v113_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * closeadj.pct_change(5)
    result = _jerk(base, 21).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_jksgn21_10d_jerk_v114_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * closeadj.pct_change(5)
    result = np.sign(_jerk(base, 21)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_jk63_10d_jerk_v115_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * closeadj.pct_change(5)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_jk263_10d_jerk_v116_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * closeadj.pct_change(5)
    result = _jerk(base, 63).rolling(31, min_periods=max(1, 31//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_jksgn63_10d_jerk_v117_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * closeadj.pct_change(5)
    result = np.sign(_jerk(base, 63)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_jk126_10d_jerk_v118_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * closeadj.pct_change(5)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_jk2126_10d_jerk_v119_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * closeadj.pct_change(5)
    result = _jerk(base, 126).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_jksgn126_10d_jerk_v120_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj * closeadj.pct_change(5)
    result = np.sign(_jerk(base, 126)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_jk5_10d_jerk_v121_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_jk25_10d_jerk_v122_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _jerk(base, 5).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_jksgn5_10d_jerk_v123_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.ewm(span=21, adjust=False).mean()
    result = np.sign(_jerk(base, 5)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_jk21_10d_jerk_v124_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_jk221_10d_jerk_v125_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _jerk(base, 21).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_jksgn21_10d_jerk_v126_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.ewm(span=21, adjust=False).mean()
    result = np.sign(_jerk(base, 21)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_jk63_10d_jerk_v127_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_jk263_10d_jerk_v128_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _jerk(base, 63).rolling(31, min_periods=max(1, 31//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_jksgn63_10d_jerk_v129_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.ewm(span=21, adjust=False).mean()
    result = np.sign(_jerk(base, 63)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_jk126_10d_jerk_v130_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_jk2126_10d_jerk_v131_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.ewm(span=21, adjust=False).mean()
    result = _jerk(base, 126).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_jksgn126_10d_jerk_v132_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.ewm(span=21, adjust=False).mean()
    result = np.sign(_jerk(base, 126)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_jk5_10d_jerk_v133_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_jk25_10d_jerk_v134_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(base, 5).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_jksgn5_10d_jerk_v135_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = np.sign(_jerk(base, 5)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_jk21_10d_jerk_v136_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_jk221_10d_jerk_v137_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(base, 21).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_jksgn21_10d_jerk_v138_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = np.sign(_jerk(base, 21)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_jk63_10d_jerk_v139_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_jk263_10d_jerk_v140_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(base, 63).rolling(31, min_periods=max(1, 31//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_jksgn63_10d_jerk_v141_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = np.sign(_jerk(base, 63)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_jk126_10d_jerk_v142_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_jk2126_10d_jerk_v143_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(base, 126).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_jksgn126_10d_jerk_v144_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = np.sign(_jerk(base, 126)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcumcls_jk5_10d_jerk_v145_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).rolling(5, min_periods=max(1, 5//2)).sum() * closeadj / 5
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcumcls_jk25_10d_jerk_v146_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).rolling(5, min_periods=max(1, 5//2)).sum() * closeadj / 5
    result = _jerk(base, 5).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcumcls_jksgn5_10d_jerk_v147_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).rolling(5, min_periods=max(1, 5//2)).sum() * closeadj / 5
    result = np.sign(_jerk(base, 5)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcumcls_jk21_10d_jerk_v148_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).rolling(5, min_periods=max(1, 5//2)).sum() * closeadj / 5
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcumcls_jk221_10d_jerk_v149_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).rolling(5, min_periods=max(1, 5//2)).sum() * closeadj / 5
    result = _jerk(base, 21).rolling(10, min_periods=max(1, 10//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcumcls_jksgn21_10d_jerk_v150_signal(closeadj, revenue):
    base = (_f33_revenue_drawdown(revenue, 10)).rolling(5, min_periods=max(1, 5//2)).sum() * closeadj / 5
    result = np.sign(_jerk(base, 21)) * base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33cew_f33_clean_energy_winter_p0_xcls_jk5_10d_jerk_v001_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_jk25_10d_jerk_v002_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_jksgn5_10d_jerk_v003_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_jk21_10d_jerk_v004_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_jk221_10d_jerk_v005_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_jksgn21_10d_jerk_v006_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_jk63_10d_jerk_v007_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_jk263_10d_jerk_v008_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_jksgn63_10d_jerk_v009_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_jk126_10d_jerk_v010_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_jk2126_10d_jerk_v011_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_jksgn126_10d_jerk_v012_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_jk5_10d_jerk_v013_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_jk25_10d_jerk_v014_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_jksgn5_10d_jerk_v015_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_jk21_10d_jerk_v016_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_jk221_10d_jerk_v017_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_jksgn21_10d_jerk_v018_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_jk63_10d_jerk_v019_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_jk263_10d_jerk_v020_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_jksgn63_10d_jerk_v021_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_jk126_10d_jerk_v022_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_jk2126_10d_jerk_v023_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_jksgn126_10d_jerk_v024_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_jk5_10d_jerk_v025_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_jk25_10d_jerk_v026_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_jksgn5_10d_jerk_v027_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_jk21_10d_jerk_v028_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_jk221_10d_jerk_v029_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_jksgn21_10d_jerk_v030_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_jk63_10d_jerk_v031_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_jk263_10d_jerk_v032_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_jksgn63_10d_jerk_v033_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_jk126_10d_jerk_v034_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_jk2126_10d_jerk_v035_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_jksgn126_10d_jerk_v036_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_jk5_10d_jerk_v037_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_jk25_10d_jerk_v038_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_jksgn5_10d_jerk_v039_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_jk21_10d_jerk_v040_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_jk221_10d_jerk_v041_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_jksgn21_10d_jerk_v042_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_jk63_10d_jerk_v043_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_jk263_10d_jerk_v044_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_jksgn63_10d_jerk_v045_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_jk126_10d_jerk_v046_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_jk2126_10d_jerk_v047_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_jksgn126_10d_jerk_v048_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_jk5_10d_jerk_v049_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_jk25_10d_jerk_v050_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_jksgn5_10d_jerk_v051_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_jk21_10d_jerk_v052_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_jk221_10d_jerk_v053_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_jksgn21_10d_jerk_v054_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_jk63_10d_jerk_v055_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_jk263_10d_jerk_v056_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_jksgn63_10d_jerk_v057_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_jk126_10d_jerk_v058_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_jk2126_10d_jerk_v059_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_jksgn126_10d_jerk_v060_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_jk5_10d_jerk_v061_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_jk25_10d_jerk_v062_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_jksgn5_10d_jerk_v063_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_jk21_10d_jerk_v064_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_jk221_10d_jerk_v065_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_jksgn21_10d_jerk_v066_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_jk63_10d_jerk_v067_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_jk263_10d_jerk_v068_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_jksgn63_10d_jerk_v069_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_jk126_10d_jerk_v070_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_jk2126_10d_jerk_v071_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_jksgn126_10d_jerk_v072_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_jk5_10d_jerk_v073_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_jk25_10d_jerk_v074_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_jksgn5_10d_jerk_v075_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_jk21_10d_jerk_v076_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_jk221_10d_jerk_v077_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_jksgn21_10d_jerk_v078_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_jk63_10d_jerk_v079_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_jk263_10d_jerk_v080_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_jksgn63_10d_jerk_v081_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_jk126_10d_jerk_v082_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_jk2126_10d_jerk_v083_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_jksgn126_10d_jerk_v084_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_jk5_10d_jerk_v085_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_jk25_10d_jerk_v086_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_jksgn5_10d_jerk_v087_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_jk21_10d_jerk_v088_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_jk221_10d_jerk_v089_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_jksgn21_10d_jerk_v090_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_jk63_10d_jerk_v091_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_jk263_10d_jerk_v092_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_jksgn63_10d_jerk_v093_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_jk126_10d_jerk_v094_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_jk2126_10d_jerk_v095_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_jksgn126_10d_jerk_v096_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_jk5_10d_jerk_v097_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_jk25_10d_jerk_v098_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_jksgn5_10d_jerk_v099_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_jk21_10d_jerk_v100_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_jk221_10d_jerk_v101_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_jksgn21_10d_jerk_v102_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_jk63_10d_jerk_v103_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_jk263_10d_jerk_v104_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_jksgn63_10d_jerk_v105_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_jk126_10d_jerk_v106_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_jk2126_10d_jerk_v107_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_jksgn126_10d_jerk_v108_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_jk5_10d_jerk_v109_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_jk25_10d_jerk_v110_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_jksgn5_10d_jerk_v111_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_jk21_10d_jerk_v112_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_jk221_10d_jerk_v113_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_jksgn21_10d_jerk_v114_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_jk63_10d_jerk_v115_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_jk263_10d_jerk_v116_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_jksgn63_10d_jerk_v117_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_jk126_10d_jerk_v118_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_jk2126_10d_jerk_v119_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_jksgn126_10d_jerk_v120_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_jk5_10d_jerk_v121_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_jk25_10d_jerk_v122_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_jksgn5_10d_jerk_v123_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_jk21_10d_jerk_v124_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_jk221_10d_jerk_v125_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_jksgn21_10d_jerk_v126_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_jk63_10d_jerk_v127_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_jk263_10d_jerk_v128_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_jksgn63_10d_jerk_v129_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_jk126_10d_jerk_v130_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_jk2126_10d_jerk_v131_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_jksgn126_10d_jerk_v132_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_jk5_10d_jerk_v133_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_jk25_10d_jerk_v134_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_jksgn5_10d_jerk_v135_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_jk21_10d_jerk_v136_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_jk221_10d_jerk_v137_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_jksgn21_10d_jerk_v138_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_jk63_10d_jerk_v139_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_jk263_10d_jerk_v140_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_jksgn63_10d_jerk_v141_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_jk126_10d_jerk_v142_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_jk2126_10d_jerk_v143_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_jksgn126_10d_jerk_v144_signal,
    f33cew_f33_clean_energy_winter_p0_xcumcls_jk5_10d_jerk_v145_signal,
    f33cew_f33_clean_energy_winter_p0_xcumcls_jk25_10d_jerk_v146_signal,
    f33cew_f33_clean_energy_winter_p0_xcumcls_jksgn5_10d_jerk_v147_signal,
    f33cew_f33_clean_energy_winter_p0_xcumcls_jk21_10d_jerk_v148_signal,
    f33cew_f33_clean_energy_winter_p0_xcumcls_jk221_10d_jerk_v149_signal,
    f33cew_f33_clean_energy_winter_p0_xcumcls_jksgn21_10d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_CLEAN_ENERGY_WINTER_REGISTRY_JERK_001_150 = REGISTRY


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
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "fcf": fcf, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f33_revenue_drawdown', '_f33_collapse_signature', '_f33_winter_score')
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
    print(f"OK f33_clean_energy_winter_3rd_derivatives_001_150_claude: {n_features} features pass")
