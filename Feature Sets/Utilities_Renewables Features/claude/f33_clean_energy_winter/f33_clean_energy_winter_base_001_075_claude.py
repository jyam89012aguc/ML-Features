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

def f33cew_f33_clean_energy_winter_p0_xcls_10d_base_v001_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_10d_base_v002_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_10d_base_v003_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 10)) * closeadj * (_f33_revenue_drawdown(revenue, 10)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_10d_base_v004_signal(closeadj, revenue):
    result = _mean(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_10d_base_v005_signal(closeadj, revenue):
    result = _std(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_10d_base_v006_signal(closeadj, revenue):
    result = _z(_f33_revenue_drawdown(revenue, 10), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_10d_base_v007_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 10)).ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_10d_base_v008_signal(closeadj, revenue):
    result = np.log((_f33_revenue_drawdown(revenue, 10)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_10d_base_v009_signal(closeadj, revenue):
    result = np.sign(_f33_revenue_drawdown(revenue, 10)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 10)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_10d_base_v010_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 10)) * closeadj * closeadj.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_10d_base_v011_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 10)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_10d_base_v012_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcumcls_10d_base_v013_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 10)).rolling(5, min_periods=max(1, 5//2)).sum() * closeadj / 5
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_21d_base_v014_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_21d_base_v015_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 21)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_21d_base_v016_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 21)) * closeadj * (_f33_revenue_drawdown(revenue, 21)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_21d_base_v017_signal(closeadj, revenue):
    result = _mean(_f33_revenue_drawdown(revenue, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_21d_base_v018_signal(closeadj, revenue):
    result = _std(_f33_revenue_drawdown(revenue, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_21d_base_v019_signal(closeadj, revenue):
    result = _z(_f33_revenue_drawdown(revenue, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_21d_base_v020_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 21)).ewm(span=10, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_21d_base_v021_signal(closeadj, revenue):
    result = np.log((_f33_revenue_drawdown(revenue, 21)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_21d_base_v022_signal(closeadj, revenue):
    result = np.sign(_f33_revenue_drawdown(revenue, 21)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 21)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_21d_base_v023_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 21)) * closeadj * closeadj.pct_change(7)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_21d_base_v024_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 21)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_21d_base_v025_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 21)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcumcls_21d_base_v026_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 21)).rolling(10, min_periods=max(1, 10//2)).sum() * closeadj / 10
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_42d_base_v027_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_42d_base_v028_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 42)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_42d_base_v029_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 42)) * closeadj * (_f33_revenue_drawdown(revenue, 42)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_42d_base_v030_signal(closeadj, revenue):
    result = _mean(_f33_revenue_drawdown(revenue, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_42d_base_v031_signal(closeadj, revenue):
    result = _std(_f33_revenue_drawdown(revenue, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_42d_base_v032_signal(closeadj, revenue):
    result = _z(_f33_revenue_drawdown(revenue, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_42d_base_v033_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 42)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_42d_base_v034_signal(closeadj, revenue):
    result = np.log((_f33_revenue_drawdown(revenue, 42)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_42d_base_v035_signal(closeadj, revenue):
    result = np.sign(_f33_revenue_drawdown(revenue, 42)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 42)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_42d_base_v036_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 42)) * closeadj * closeadj.pct_change(14)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_42d_base_v037_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 42)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_42d_base_v038_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 42)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcumcls_42d_base_v039_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 42)).rolling(21, min_periods=max(1, 21//2)).sum() * closeadj / 21
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_63d_base_v040_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_63d_base_v041_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 63)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_63d_base_v042_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 63)) * closeadj * (_f33_revenue_drawdown(revenue, 63)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_63d_base_v043_signal(closeadj, revenue):
    result = _mean(_f33_revenue_drawdown(revenue, 63), 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_63d_base_v044_signal(closeadj, revenue):
    result = _std(_f33_revenue_drawdown(revenue, 63), 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_63d_base_v045_signal(closeadj, revenue):
    result = _z(_f33_revenue_drawdown(revenue, 63), 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_63d_base_v046_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 63)).ewm(span=31, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_63d_base_v047_signal(closeadj, revenue):
    result = np.log((_f33_revenue_drawdown(revenue, 63)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_63d_base_v048_signal(closeadj, revenue):
    result = np.sign(_f33_revenue_drawdown(revenue, 63)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 63)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_63d_base_v049_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 63)) * closeadj * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_63d_base_v050_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 63)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_63d_base_v051_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 63)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcumcls_63d_base_v052_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 63)).rolling(31, min_periods=max(1, 31//2)).sum() * closeadj / 31
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_126d_base_v053_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_126d_base_v054_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 126)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_126d_base_v055_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 126)) * closeadj * (_f33_revenue_drawdown(revenue, 126)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_126d_base_v056_signal(closeadj, revenue):
    result = _mean(_f33_revenue_drawdown(revenue, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_126d_base_v057_signal(closeadj, revenue):
    result = _std(_f33_revenue_drawdown(revenue, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_126d_base_v058_signal(closeadj, revenue):
    result = _z(_f33_revenue_drawdown(revenue, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_126d_base_v059_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 126)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_126d_base_v060_signal(closeadj, revenue):
    result = np.log((_f33_revenue_drawdown(revenue, 126)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_126d_base_v061_signal(closeadj, revenue):
    result = np.sign(_f33_revenue_drawdown(revenue, 126)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 126)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_126d_base_v062_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 126)) * closeadj * closeadj.pct_change(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsema21_126d_base_v063_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 126)) * closeadj.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsma63_126d_base_v064_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 126)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcumcls_126d_base_v065_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 126)).rolling(63, min_periods=max(1, 63//2)).sum() * closeadj / 63
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xcls_189d_base_v066_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsabs_189d_base_v067_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 189)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclssq_189d_base_v068_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 189)) * closeadj * (_f33_revenue_drawdown(revenue, 189)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xmcls_189d_base_v069_signal(closeadj, revenue):
    result = _mean(_f33_revenue_drawdown(revenue, 189), 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xstdcls_189d_base_v070_signal(closeadj, revenue):
    result = _std(_f33_revenue_drawdown(revenue, 189), 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xzcls_189d_base_v071_signal(closeadj, revenue):
    result = _z(_f33_revenue_drawdown(revenue, 189), 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xemacls_189d_base_v072_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 189)).ewm(span=94, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xlogcls_189d_base_v073_signal(closeadj, revenue):
    result = np.log((_f33_revenue_drawdown(revenue, 189)).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xsgncls_189d_base_v074_signal(closeadj, revenue):
    result = np.sign(_f33_revenue_drawdown(revenue, 189)) * closeadj * (1.0 + (_f33_revenue_drawdown(revenue, 189)).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f33cew_f33_clean_energy_winter_p0_xclsret_189d_base_v075_signal(closeadj, revenue):
    result = (_f33_revenue_drawdown(revenue, 189)) * closeadj * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33cew_f33_clean_energy_winter_p0_xcls_10d_base_v001_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_10d_base_v002_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_10d_base_v003_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_10d_base_v004_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_10d_base_v005_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_10d_base_v006_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_10d_base_v007_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_10d_base_v008_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_10d_base_v009_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_10d_base_v010_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_10d_base_v011_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_10d_base_v012_signal,
    f33cew_f33_clean_energy_winter_p0_xcumcls_10d_base_v013_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_21d_base_v014_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_21d_base_v015_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_21d_base_v016_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_21d_base_v017_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_21d_base_v018_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_21d_base_v019_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_21d_base_v020_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_21d_base_v021_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_21d_base_v022_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_21d_base_v023_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_21d_base_v024_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_21d_base_v025_signal,
    f33cew_f33_clean_energy_winter_p0_xcumcls_21d_base_v026_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_42d_base_v027_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_42d_base_v028_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_42d_base_v029_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_42d_base_v030_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_42d_base_v031_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_42d_base_v032_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_42d_base_v033_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_42d_base_v034_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_42d_base_v035_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_42d_base_v036_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_42d_base_v037_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_42d_base_v038_signal,
    f33cew_f33_clean_energy_winter_p0_xcumcls_42d_base_v039_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_63d_base_v040_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_63d_base_v041_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_63d_base_v042_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_63d_base_v043_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_63d_base_v044_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_63d_base_v045_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_63d_base_v046_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_63d_base_v047_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_63d_base_v048_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_63d_base_v049_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_63d_base_v050_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_63d_base_v051_signal,
    f33cew_f33_clean_energy_winter_p0_xcumcls_63d_base_v052_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_126d_base_v053_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_126d_base_v054_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_126d_base_v055_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_126d_base_v056_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_126d_base_v057_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_126d_base_v058_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_126d_base_v059_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_126d_base_v060_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_126d_base_v061_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_126d_base_v062_signal,
    f33cew_f33_clean_energy_winter_p0_xclsema21_126d_base_v063_signal,
    f33cew_f33_clean_energy_winter_p0_xclsma63_126d_base_v064_signal,
    f33cew_f33_clean_energy_winter_p0_xcumcls_126d_base_v065_signal,
    f33cew_f33_clean_energy_winter_p0_xcls_189d_base_v066_signal,
    f33cew_f33_clean_energy_winter_p0_xclsabs_189d_base_v067_signal,
    f33cew_f33_clean_energy_winter_p0_xclssq_189d_base_v068_signal,
    f33cew_f33_clean_energy_winter_p0_xmcls_189d_base_v069_signal,
    f33cew_f33_clean_energy_winter_p0_xstdcls_189d_base_v070_signal,
    f33cew_f33_clean_energy_winter_p0_xzcls_189d_base_v071_signal,
    f33cew_f33_clean_energy_winter_p0_xemacls_189d_base_v072_signal,
    f33cew_f33_clean_energy_winter_p0_xlogcls_189d_base_v073_signal,
    f33cew_f33_clean_energy_winter_p0_xsgncls_189d_base_v074_signal,
    f33cew_f33_clean_energy_winter_p0_xclsret_189d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_CLEAN_ENERGY_WINTER_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f33_clean_energy_winter_base_001_075_claude: {n_features} features pass")
