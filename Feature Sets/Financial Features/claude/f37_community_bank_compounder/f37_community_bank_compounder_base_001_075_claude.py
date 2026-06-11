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

# ===== folder domain primitives =====
def _f37_size_score(marketcap, assets):
    # Smaller-bank emphasis: invert relative size, scale by marketcap to ensure variation.
    rel = _safe_div(assets, marketcap)
    return rel * marketcap / (rel + 1.0)


def _f37_steady_growth(revenue, w):
    g = revenue.pct_change(periods=w)
    sd = g.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return _safe_div(g, sd) * revenue


def _f37_community_score(marketcap, revenue, bvps, w):
    g = revenue.pct_change(periods=w)
    sd = g.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return (g / sd) * bvps * marketcap / (marketcap + 1.0)

def f37cbc_f37_community_bank_compounder_size_k1_base_v001_signal(marketcap, assets):
    base = _f37_size_score(marketcap, assets)
    result = base * (0.01)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_size_k2_base_v002_signal(marketcap, assets):
    base = _f37_size_score(marketcap, assets)
    result = base * (0.1)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_size_k3_base_v003_signal(marketcap, assets):
    base = _f37_size_score(marketcap, assets)
    result = base * (0.5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_size_k4_base_v004_signal(marketcap, assets):
    base = _f37_size_score(marketcap, assets)
    result = base * (1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_size_k5_base_v005_signal(marketcap, assets):
    base = _f37_size_score(marketcap, assets)
    result = base * (2.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_size_k6_base_v006_signal(marketcap, assets):
    base = _f37_size_score(marketcap, assets)
    result = base * (5.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_size_k7_base_v007_signal(marketcap, assets):
    base = _f37_size_score(marketcap, assets)
    result = base * (10.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_size_k8_base_v008_signal(marketcap, assets):
    base = _f37_size_score(marketcap, assets)
    result = base * (50.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_size_k9_base_v009_signal(marketcap, assets):
    base = _f37_size_score(marketcap, assets)
    result = base * (100.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_size_k10_base_v010_signal(marketcap, assets):
    base = _f37_size_score(marketcap, assets)
    result = base * (500.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steady_5d_base_v011_signal(revenue):
    result = _f37_steady_growth(revenue, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steady_10d_base_v012_signal(revenue):
    result = _f37_steady_growth(revenue, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steady_21d_base_v013_signal(revenue):
    result = _f37_steady_growth(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steady_42d_base_v014_signal(revenue):
    result = _f37_steady_growth(revenue, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steady_63d_base_v015_signal(revenue):
    result = _f37_steady_growth(revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steady_126d_base_v016_signal(revenue):
    result = _f37_steady_growth(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steady_189d_base_v017_signal(revenue):
    result = _f37_steady_growth(revenue, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steady_252d_base_v018_signal(revenue):
    result = _f37_steady_growth(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steady_378d_base_v019_signal(revenue):
    result = _f37_steady_growth(revenue, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steady_504d_base_v020_signal(revenue):
    result = _f37_steady_growth(revenue, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyema_63d_base_v021_signal(revenue):
    base = _f37_steady_growth(revenue, 63)
    result = _ema(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyema_252d_base_v022_signal(revenue):
    base = _f37_steady_growth(revenue, 252)
    result = _ema(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_comm_5d_base_v023_signal(marketcap, revenue, bvps):
    result = _f37_community_score(marketcap, revenue, bvps, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_comm_10d_base_v024_signal(marketcap, revenue, bvps):
    result = _f37_community_score(marketcap, revenue, bvps, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_comm_21d_base_v025_signal(marketcap, revenue, bvps):
    result = _f37_community_score(marketcap, revenue, bvps, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_comm_42d_base_v026_signal(marketcap, revenue, bvps):
    result = _f37_community_score(marketcap, revenue, bvps, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_comm_63d_base_v027_signal(marketcap, revenue, bvps):
    result = _f37_community_score(marketcap, revenue, bvps, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_comm_126d_base_v028_signal(marketcap, revenue, bvps):
    result = _f37_community_score(marketcap, revenue, bvps, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_comm_189d_base_v029_signal(marketcap, revenue, bvps):
    result = _f37_community_score(marketcap, revenue, bvps, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_comm_252d_base_v030_signal(marketcap, revenue, bvps):
    result = _f37_community_score(marketcap, revenue, bvps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_comm_378d_base_v031_signal(marketcap, revenue, bvps):
    result = _f37_community_score(marketcap, revenue, bvps, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_comm_504d_base_v032_signal(marketcap, revenue, bvps):
    result = _f37_community_score(marketcap, revenue, bvps, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commema_21d_base_v033_signal(marketcap, revenue, bvps):
    base = _f37_community_score(marketcap, revenue, bvps, 21)
    result = _ema(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commema_63d_base_v034_signal(marketcap, revenue, bvps):
    base = _f37_community_score(marketcap, revenue, bvps, 63)
    result = _ema(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commema_126d_base_v035_signal(marketcap, revenue, bvps):
    base = _f37_community_score(marketcap, revenue, bvps, 126)
    result = _ema(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commema_252d_base_v036_signal(marketcap, revenue, bvps):
    base = _f37_community_score(marketcap, revenue, bvps, 252)
    result = _ema(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizexca_21d_base_v037_signal(marketcap, assets, closeadj):
    base = _f37_size_score(marketcap, assets)
    result = base * _mean(closeadj, 21) / _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizexca_63d_base_v038_signal(marketcap, assets, closeadj):
    base = _f37_size_score(marketcap, assets)
    result = base * _mean(closeadj, 63) / _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizexca_126d_base_v039_signal(marketcap, assets, closeadj):
    base = _f37_size_score(marketcap, assets)
    result = base * _mean(closeadj, 126) / _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizexca_252d_base_v040_signal(marketcap, assets, closeadj):
    base = _f37_size_score(marketcap, assets)
    result = base * _mean(closeadj, 252) / _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyxca_21d_base_v041_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 21)
    result = base * _mean(closeadj, 21) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyxca_63d_base_v042_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 63)
    result = base * _mean(closeadj, 21) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyxca_126d_base_v043_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 126)
    result = base * _mean(closeadj, 21) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyxca_252d_base_v044_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 252)
    result = base * _mean(closeadj, 21) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commxca_21d_base_v045_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 21)
    result = base * _mean(closeadj, 21) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commxca_63d_base_v046_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 63)
    result = base * _mean(closeadj, 21) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commxca_126d_base_v047_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 126)
    result = base * _mean(closeadj, 21) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commxca_252d_base_v048_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 252)
    result = base * _mean(closeadj, 21) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyz_21d_base_v049_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 21)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyz_63d_base_v050_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyz_126d_base_v051_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyz_252d_base_v052_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commz_21d_base_v053_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 21)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commz_63d_base_v054_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commz_126d_base_v055_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commz_252d_base_v056_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizexbvg_21d_base_v057_signal(marketcap, assets, bvps, closeadj):
    base = _f37_size_score(marketcap, assets)
    bg = bvps.pct_change(periods=21)
    result = base * bg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizexbvg_63d_base_v058_signal(marketcap, assets, bvps, closeadj):
    base = _f37_size_score(marketcap, assets)
    bg = bvps.pct_change(periods=63)
    result = base * bg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizexbvg_126d_base_v059_signal(marketcap, assets, bvps, closeadj):
    base = _f37_size_score(marketcap, assets)
    bg = bvps.pct_change(periods=126)
    result = base * bg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizexbvg_252d_base_v060_signal(marketcap, assets, bvps, closeadj):
    base = _f37_size_score(marketcap, assets)
    bg = bvps.pct_change(periods=252)
    result = base * bg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadystd_21d_base_v061_signal(revenue):
    base = _f37_steady_growth(revenue, 21)
    result = _std(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadystd_63d_base_v062_signal(revenue):
    base = _f37_steady_growth(revenue, 63)
    result = _std(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadystd_126d_base_v063_signal(revenue):
    base = _f37_steady_growth(revenue, 126)
    result = _std(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadystd_252d_base_v064_signal(revenue):
    base = _f37_steady_growth(revenue, 252)
    result = _std(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commstd_21d_base_v065_signal(marketcap, revenue, bvps):
    base = _f37_community_score(marketcap, revenue, bvps, 21)
    result = _std(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commstd_63d_base_v066_signal(marketcap, revenue, bvps):
    base = _f37_community_score(marketcap, revenue, bvps, 63)
    result = _std(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commstd_126d_base_v067_signal(marketcap, revenue, bvps):
    base = _f37_community_score(marketcap, revenue, bvps, 126)
    result = _std(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commstd_252d_base_v068_signal(marketcap, revenue, bvps):
    base = _f37_community_score(marketcap, revenue, bvps, 252)
    result = _std(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commxrev_21d_base_v069_signal(marketcap, revenue, bvps):
    base = _f37_community_score(marketcap, revenue, bvps, 21)
    result = base * _mean(revenue, 21) / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commxrev_63d_base_v070_signal(marketcap, revenue, bvps):
    base = _f37_community_score(marketcap, revenue, bvps, 63)
    result = base * _mean(revenue, 21) / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commxrev_126d_base_v071_signal(marketcap, revenue, bvps):
    base = _f37_community_score(marketcap, revenue, bvps, 126)
    result = base * _mean(revenue, 21) / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyxbvm_21d_base_v072_signal(revenue, bvps, closeadj):
    base = _f37_steady_growth(revenue, 21)
    result = base * _mean(bvps, 21) / 10.0 * closeadj / 1e10
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyxbvm_63d_base_v073_signal(revenue, bvps, closeadj):
    base = _f37_steady_growth(revenue, 63)
    result = base * _mean(bvps, 21) / 10.0 * closeadj / 1e10
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyxbvm_126d_base_v074_signal(revenue, bvps, closeadj):
    base = _f37_steady_growth(revenue, 126)
    result = base * _mean(bvps, 21) / 10.0 * closeadj / 1e10
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyxbvm_252d_base_v075_signal(revenue, bvps, closeadj):
    base = _f37_steady_growth(revenue, 252)
    result = base * _mean(bvps, 21) / 10.0 * closeadj / 1e10
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37cbc_f37_community_bank_compounder_size_k1_base_v001_signal,
    f37cbc_f37_community_bank_compounder_size_k2_base_v002_signal,
    f37cbc_f37_community_bank_compounder_size_k3_base_v003_signal,
    f37cbc_f37_community_bank_compounder_size_k4_base_v004_signal,
    f37cbc_f37_community_bank_compounder_size_k5_base_v005_signal,
    f37cbc_f37_community_bank_compounder_size_k6_base_v006_signal,
    f37cbc_f37_community_bank_compounder_size_k7_base_v007_signal,
    f37cbc_f37_community_bank_compounder_size_k8_base_v008_signal,
    f37cbc_f37_community_bank_compounder_size_k9_base_v009_signal,
    f37cbc_f37_community_bank_compounder_size_k10_base_v010_signal,
    f37cbc_f37_community_bank_compounder_steady_5d_base_v011_signal,
    f37cbc_f37_community_bank_compounder_steady_10d_base_v012_signal,
    f37cbc_f37_community_bank_compounder_steady_21d_base_v013_signal,
    f37cbc_f37_community_bank_compounder_steady_42d_base_v014_signal,
    f37cbc_f37_community_bank_compounder_steady_63d_base_v015_signal,
    f37cbc_f37_community_bank_compounder_steady_126d_base_v016_signal,
    f37cbc_f37_community_bank_compounder_steady_189d_base_v017_signal,
    f37cbc_f37_community_bank_compounder_steady_252d_base_v018_signal,
    f37cbc_f37_community_bank_compounder_steady_378d_base_v019_signal,
    f37cbc_f37_community_bank_compounder_steady_504d_base_v020_signal,
    f37cbc_f37_community_bank_compounder_steadyema_63d_base_v021_signal,
    f37cbc_f37_community_bank_compounder_steadyema_252d_base_v022_signal,
    f37cbc_f37_community_bank_compounder_comm_5d_base_v023_signal,
    f37cbc_f37_community_bank_compounder_comm_10d_base_v024_signal,
    f37cbc_f37_community_bank_compounder_comm_21d_base_v025_signal,
    f37cbc_f37_community_bank_compounder_comm_42d_base_v026_signal,
    f37cbc_f37_community_bank_compounder_comm_63d_base_v027_signal,
    f37cbc_f37_community_bank_compounder_comm_126d_base_v028_signal,
    f37cbc_f37_community_bank_compounder_comm_189d_base_v029_signal,
    f37cbc_f37_community_bank_compounder_comm_252d_base_v030_signal,
    f37cbc_f37_community_bank_compounder_comm_378d_base_v031_signal,
    f37cbc_f37_community_bank_compounder_comm_504d_base_v032_signal,
    f37cbc_f37_community_bank_compounder_commema_21d_base_v033_signal,
    f37cbc_f37_community_bank_compounder_commema_63d_base_v034_signal,
    f37cbc_f37_community_bank_compounder_commema_126d_base_v035_signal,
    f37cbc_f37_community_bank_compounder_commema_252d_base_v036_signal,
    f37cbc_f37_community_bank_compounder_sizexca_21d_base_v037_signal,
    f37cbc_f37_community_bank_compounder_sizexca_63d_base_v038_signal,
    f37cbc_f37_community_bank_compounder_sizexca_126d_base_v039_signal,
    f37cbc_f37_community_bank_compounder_sizexca_252d_base_v040_signal,
    f37cbc_f37_community_bank_compounder_steadyxca_21d_base_v041_signal,
    f37cbc_f37_community_bank_compounder_steadyxca_63d_base_v042_signal,
    f37cbc_f37_community_bank_compounder_steadyxca_126d_base_v043_signal,
    f37cbc_f37_community_bank_compounder_steadyxca_252d_base_v044_signal,
    f37cbc_f37_community_bank_compounder_commxca_21d_base_v045_signal,
    f37cbc_f37_community_bank_compounder_commxca_63d_base_v046_signal,
    f37cbc_f37_community_bank_compounder_commxca_126d_base_v047_signal,
    f37cbc_f37_community_bank_compounder_commxca_252d_base_v048_signal,
    f37cbc_f37_community_bank_compounder_steadyz_21d_base_v049_signal,
    f37cbc_f37_community_bank_compounder_steadyz_63d_base_v050_signal,
    f37cbc_f37_community_bank_compounder_steadyz_126d_base_v051_signal,
    f37cbc_f37_community_bank_compounder_steadyz_252d_base_v052_signal,
    f37cbc_f37_community_bank_compounder_commz_21d_base_v053_signal,
    f37cbc_f37_community_bank_compounder_commz_63d_base_v054_signal,
    f37cbc_f37_community_bank_compounder_commz_126d_base_v055_signal,
    f37cbc_f37_community_bank_compounder_commz_252d_base_v056_signal,
    f37cbc_f37_community_bank_compounder_sizexbvg_21d_base_v057_signal,
    f37cbc_f37_community_bank_compounder_sizexbvg_63d_base_v058_signal,
    f37cbc_f37_community_bank_compounder_sizexbvg_126d_base_v059_signal,
    f37cbc_f37_community_bank_compounder_sizexbvg_252d_base_v060_signal,
    f37cbc_f37_community_bank_compounder_steadystd_21d_base_v061_signal,
    f37cbc_f37_community_bank_compounder_steadystd_63d_base_v062_signal,
    f37cbc_f37_community_bank_compounder_steadystd_126d_base_v063_signal,
    f37cbc_f37_community_bank_compounder_steadystd_252d_base_v064_signal,
    f37cbc_f37_community_bank_compounder_commstd_21d_base_v065_signal,
    f37cbc_f37_community_bank_compounder_commstd_63d_base_v066_signal,
    f37cbc_f37_community_bank_compounder_commstd_126d_base_v067_signal,
    f37cbc_f37_community_bank_compounder_commstd_252d_base_v068_signal,
    f37cbc_f37_community_bank_compounder_commxrev_21d_base_v069_signal,
    f37cbc_f37_community_bank_compounder_commxrev_63d_base_v070_signal,
    f37cbc_f37_community_bank_compounder_commxrev_126d_base_v071_signal,
    f37cbc_f37_community_bank_compounder_steadyxbvm_21d_base_v072_signal,
    f37cbc_f37_community_bank_compounder_steadyxbvm_63d_base_v073_signal,
    f37cbc_f37_community_bank_compounder_steadyxbvm_126d_base_v074_signal,
    f37cbc_f37_community_bank_compounder_steadyxbvm_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_COMMUNITY_BANK_COMPOUNDER_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f37_size_score", "_f37_steady_growth", "_f37_community_score")
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
    print(f"OK f37_community_bank_compounder_base_001_075_claude: {n_features} features pass")
