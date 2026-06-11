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
def _f28_revenue_per_asset(revenue, assets):
    return revenue / assets.replace(0, np.nan).abs()


def _f28_pricing_proxy(revenue, ppnenet, w):
    rpa = revenue / ppnenet.replace(0, np.nan).abs()
    return rpa.rolling(w, min_periods=max(1, w // 2)).mean()


def _f28_pricing_dynamics(revenue, assets, w):
    rpa = revenue / assets.replace(0, np.nan).abs()
    return rpa.pct_change(periods=w)



# ===== features =====

# bw=5 tr=21 sc=0 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_5d_t21s0d5_slope_v001_signal(assets, closeadj, revenue):
    base = _f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=21 sc=6 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_5d_t21s6d21_slope_v002_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 5) + 21).rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=63 sc=4 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_5d_t63s4d63_slope_v003_signal(assets, closeadj, revenue):
    base = _z(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 5), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=126 sc=3 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_5d_t126s3d5_slope_v004_signal(assets, closeadj, revenue):
    base = _std(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 5), 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=252 sc=1 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_5d_t252s1d21_slope_v005_signal(assets, closeadj, revenue):
    base = _f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 5) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=252 sc=7 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_5d_t252s7d63_slope_v006_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 5) * closeadj) * (closeadj.pct_change(252).abs() + 1.0)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=21 sc=6 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_10d_t21s6d5_slope_v007_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 10) + 21).rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=63 sc=4 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_10d_t63s4d21_slope_v008_signal(assets, closeadj, revenue):
    base = _z(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 10), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=126 sc=2 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_10d_t126s2d63_slope_v009_signal(assets, closeadj, revenue):
    base = _mean(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 10), 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=252 sc=1 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_10d_t252s1d5_slope_v010_signal(assets, closeadj, revenue):
    base = _f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 10) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=252 sc=7 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_10d_t252s7d21_slope_v011_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 10) * closeadj) * (closeadj.pct_change(252).abs() + 1.0)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=21 sc=5 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_21d_t21s5d63_slope_v012_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 21) * closeadj).shift(21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=63 sc=4 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_21d_t63s4d5_slope_v013_signal(assets, closeadj, revenue):
    base = _z(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 21), 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=126 sc=2 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_21d_t126s2d21_slope_v014_signal(assets, closeadj, revenue):
    base = _mean(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 21), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=252 sc=0 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_21d_t252s0d63_slope_v015_signal(assets, closeadj, revenue):
    base = _f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=252 sc=7 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_21d_t252s7d5_slope_v016_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 21) * closeadj) * (closeadj.pct_change(252).abs() + 1.0)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=21 sc=5 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_42d_t21s5d21_slope_v017_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 42) * closeadj).shift(21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=63 sc=3 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_42d_t63s3d63_slope_v018_signal(assets, closeadj, revenue):
    base = _std(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 42), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=126 sc=2 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_42d_t126s2d5_slope_v019_signal(assets, closeadj, revenue):
    base = _mean(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 42), 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=252 sc=0 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_42d_t252s0d21_slope_v020_signal(assets, closeadj, revenue):
    base = _f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=252 sc=6 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_42d_t252s6d63_slope_v021_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 42) + 252).rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=21 sc=5 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_63d_t21s5d5_slope_v022_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 63) * closeadj).shift(21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=63 sc=3 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_63d_t63s3d21_slope_v023_signal(assets, closeadj, revenue):
    base = _std(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 63), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=126 sc=1 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_63d_t126s1d63_slope_v024_signal(assets, closeadj, revenue):
    base = _f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 63) * closeadj * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=252 sc=0 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_63d_t252s0d5_slope_v025_signal(assets, closeadj, revenue):
    base = _f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=252 sc=6 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_63d_t252s6d21_slope_v026_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 63) + 252).rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=21 sc=4 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_126d_t21s4d63_slope_v027_signal(assets, closeadj, revenue):
    base = _z(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 126), 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=63 sc=3 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_126d_t63s3d5_slope_v028_signal(assets, closeadj, revenue):
    base = _std(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 126), 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=126 sc=1 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_126d_t126s1d21_slope_v029_signal(assets, closeadj, revenue):
    base = _f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 126) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=126 sc=7 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_126d_t126s7d63_slope_v030_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 126) * closeadj) * (closeadj.pct_change(126).abs() + 1.0)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=252 sc=6 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_126d_t252s6d5_slope_v031_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 126) + 252).rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=21 sc=4 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_189d_t21s4d21_slope_v032_signal(assets, closeadj, revenue):
    base = _z(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 189), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=63 sc=2 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_189d_t63s2d63_slope_v033_signal(assets, closeadj, revenue):
    base = _mean(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 189), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=126 sc=1 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_189d_t126s1d5_slope_v034_signal(assets, closeadj, revenue):
    base = _f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 189) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=126 sc=7 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_189d_t126s7d21_slope_v035_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 189) * closeadj) * (closeadj.pct_change(126).abs() + 1.0)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=252 sc=5 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_189d_t252s5d63_slope_v036_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 189) * closeadj).shift(252)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=21 sc=4 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_252d_t21s4d5_slope_v037_signal(assets, closeadj, revenue):
    base = _z(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 252), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=63 sc=2 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_252d_t63s2d21_slope_v038_signal(assets, closeadj, revenue):
    base = _mean(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 252), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=126 sc=0 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_252d_t126s0d63_slope_v039_signal(assets, closeadj, revenue):
    base = _f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=126 sc=7 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_252d_t126s7d5_slope_v040_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 252) * closeadj) * (closeadj.pct_change(126).abs() + 1.0)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=252 sc=5 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_252d_t252s5d21_slope_v041_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 252) * closeadj).shift(252)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=21 sc=3 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_378d_t21s3d63_slope_v042_signal(assets, closeadj, revenue):
    base = _std(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 378), 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=63 sc=2 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_378d_t63s2d5_slope_v043_signal(assets, closeadj, revenue):
    base = _mean(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 378), 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=126 sc=0 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_378d_t126s0d21_slope_v044_signal(assets, closeadj, revenue):
    base = _f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 378) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=126 sc=6 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_378d_t126s6d63_slope_v045_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 378) + 126).rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=252 sc=5 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_378d_t252s5d5_slope_v046_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 378) * closeadj).shift(252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=21 sc=3 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_504d_t21s3d21_slope_v047_signal(assets, closeadj, revenue):
    base = _std(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 504), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=63 sc=1 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_504d_t63s1d63_slope_v048_signal(assets, closeadj, revenue):
    base = _f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 504) * closeadj * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=126 sc=0 dw=5 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_504d_t126s0d5_slope_v049_signal(assets, closeadj, revenue):
    base = _f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=126 sc=6 dw=21 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_504d_t126s6d21_slope_v050_signal(assets, closeadj, revenue):
    base = (_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 504) + 126).rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=252 sc=4 dw=63 prim=_f28_revenue_per_asset mode=slope
def f28ppd_f28_power_pricing_dynamics_revenue_per_asset_504d_t252s4d63_slope_v051_signal(assets, closeadj, revenue):
    base = _z(_f28_revenue_per_asset(revenue, assets) * _mean(closeadj, 504), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=21 sc=3 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_5d_t21s3d5_slope_v052_signal(closeadj, ppnenet, revenue):
    base = _std(_f28_pricing_proxy(revenue, ppnenet, 5), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=63 sc=1 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_5d_t63s1d21_slope_v053_signal(closeadj, ppnenet, revenue):
    base = _f28_pricing_proxy(revenue, ppnenet, 5) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=63 sc=7 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_5d_t63s7d63_slope_v054_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 5) * closeadj) * (closeadj.pct_change(63).abs() + 1.0)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=126 sc=6 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_5d_t126s6d5_slope_v055_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 5) + 126).rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=252 sc=4 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_5d_t252s4d21_slope_v056_signal(closeadj, ppnenet, revenue):
    base = _z(_f28_pricing_proxy(revenue, ppnenet, 5), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=21 sc=2 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_10d_t21s2d63_slope_v057_signal(closeadj, ppnenet, revenue):
    base = _mean(_f28_pricing_proxy(revenue, ppnenet, 10), 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=63 sc=1 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_10d_t63s1d5_slope_v058_signal(closeadj, ppnenet, revenue):
    base = _f28_pricing_proxy(revenue, ppnenet, 10) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=63 sc=7 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_10d_t63s7d21_slope_v059_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 10) * closeadj) * (closeadj.pct_change(63).abs() + 1.0)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=126 sc=5 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_10d_t126s5d63_slope_v060_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 10) * closeadj).shift(126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=252 sc=4 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_10d_t252s4d5_slope_v061_signal(closeadj, ppnenet, revenue):
    base = _z(_f28_pricing_proxy(revenue, ppnenet, 10), 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=21 sc=2 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_21d_t21s2d21_slope_v062_signal(closeadj, ppnenet, revenue):
    base = _mean(_f28_pricing_proxy(revenue, ppnenet, 21), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=63 sc=0 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_21d_t63s0d63_slope_v063_signal(closeadj, ppnenet, revenue):
    base = _f28_pricing_proxy(revenue, ppnenet, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=63 sc=7 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_21d_t63s7d5_slope_v064_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 21) * closeadj) * (closeadj.pct_change(63).abs() + 1.0)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=126 sc=5 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_21d_t126s5d21_slope_v065_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 21) * closeadj).shift(126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=252 sc=3 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_21d_t252s3d63_slope_v066_signal(closeadj, ppnenet, revenue):
    base = _std(_f28_pricing_proxy(revenue, ppnenet, 21), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=21 sc=2 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_42d_t21s2d5_slope_v067_signal(closeadj, ppnenet, revenue):
    base = _mean(_f28_pricing_proxy(revenue, ppnenet, 42), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=63 sc=0 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_42d_t63s0d21_slope_v068_signal(closeadj, ppnenet, revenue):
    base = _f28_pricing_proxy(revenue, ppnenet, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=63 sc=6 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_42d_t63s6d63_slope_v069_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 42) + 63).rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=126 sc=5 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_42d_t126s5d5_slope_v070_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 42) * closeadj).shift(126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=252 sc=3 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_42d_t252s3d21_slope_v071_signal(closeadj, ppnenet, revenue):
    base = _std(_f28_pricing_proxy(revenue, ppnenet, 42), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=21 sc=1 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_63d_t21s1d63_slope_v072_signal(closeadj, ppnenet, revenue):
    base = _f28_pricing_proxy(revenue, ppnenet, 63) * closeadj * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=63 sc=0 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_63d_t63s0d5_slope_v073_signal(closeadj, ppnenet, revenue):
    base = _f28_pricing_proxy(revenue, ppnenet, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=63 sc=6 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_63d_t63s6d21_slope_v074_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 63) + 63).rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=126 sc=4 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_63d_t126s4d63_slope_v075_signal(closeadj, ppnenet, revenue):
    base = _z(_f28_pricing_proxy(revenue, ppnenet, 63), 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=252 sc=3 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_63d_t252s3d5_slope_v076_signal(closeadj, ppnenet, revenue):
    base = _std(_f28_pricing_proxy(revenue, ppnenet, 63), 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=21 sc=1 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_126d_t21s1d21_slope_v077_signal(closeadj, ppnenet, revenue):
    base = _f28_pricing_proxy(revenue, ppnenet, 126) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=21 sc=7 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_126d_t21s7d63_slope_v078_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 126) * closeadj) * (closeadj.pct_change(21).abs() + 1.0)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=63 sc=6 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_126d_t63s6d5_slope_v079_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 126) + 63).rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=126 sc=4 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_126d_t126s4d21_slope_v080_signal(closeadj, ppnenet, revenue):
    base = _z(_f28_pricing_proxy(revenue, ppnenet, 126), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=252 sc=2 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_126d_t252s2d63_slope_v081_signal(closeadj, ppnenet, revenue):
    base = _mean(_f28_pricing_proxy(revenue, ppnenet, 126), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=21 sc=1 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_189d_t21s1d5_slope_v082_signal(closeadj, ppnenet, revenue):
    base = _f28_pricing_proxy(revenue, ppnenet, 189) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=21 sc=7 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_189d_t21s7d21_slope_v083_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 189) * closeadj) * (closeadj.pct_change(21).abs() + 1.0)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=63 sc=5 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_189d_t63s5d63_slope_v084_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 189) * closeadj).shift(63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=126 sc=4 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_189d_t126s4d5_slope_v085_signal(closeadj, ppnenet, revenue):
    base = _z(_f28_pricing_proxy(revenue, ppnenet, 189), 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=252 sc=2 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_189d_t252s2d21_slope_v086_signal(closeadj, ppnenet, revenue):
    base = _mean(_f28_pricing_proxy(revenue, ppnenet, 189), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=21 sc=0 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_252d_t21s0d63_slope_v087_signal(closeadj, ppnenet, revenue):
    base = _f28_pricing_proxy(revenue, ppnenet, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=21 sc=7 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_252d_t21s7d5_slope_v088_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 252) * closeadj) * (closeadj.pct_change(21).abs() + 1.0)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=63 sc=5 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_252d_t63s5d21_slope_v089_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 252) * closeadj).shift(63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=126 sc=3 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_252d_t126s3d63_slope_v090_signal(closeadj, ppnenet, revenue):
    base = _std(_f28_pricing_proxy(revenue, ppnenet, 252), 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=252 sc=2 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_252d_t252s2d5_slope_v091_signal(closeadj, ppnenet, revenue):
    base = _mean(_f28_pricing_proxy(revenue, ppnenet, 252), 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=21 sc=0 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_378d_t21s0d21_slope_v092_signal(closeadj, ppnenet, revenue):
    base = _f28_pricing_proxy(revenue, ppnenet, 378) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=21 sc=6 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_378d_t21s6d63_slope_v093_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 378) + 21).rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=63 sc=5 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_378d_t63s5d5_slope_v094_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 378) * closeadj).shift(63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=126 sc=3 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_378d_t126s3d21_slope_v095_signal(closeadj, ppnenet, revenue):
    base = _std(_f28_pricing_proxy(revenue, ppnenet, 378), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=252 sc=1 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_378d_t252s1d63_slope_v096_signal(closeadj, ppnenet, revenue):
    base = _f28_pricing_proxy(revenue, ppnenet, 378) * closeadj * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=21 sc=0 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_504d_t21s0d5_slope_v097_signal(closeadj, ppnenet, revenue):
    base = _f28_pricing_proxy(revenue, ppnenet, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=21 sc=6 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_504d_t21s6d21_slope_v098_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 504) + 21).rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=63 sc=4 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_504d_t63s4d63_slope_v099_signal(closeadj, ppnenet, revenue):
    base = _z(_f28_pricing_proxy(revenue, ppnenet, 504), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=126 sc=3 dw=5 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_504d_t126s3d5_slope_v100_signal(closeadj, ppnenet, revenue):
    base = _std(_f28_pricing_proxy(revenue, ppnenet, 504), 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=252 sc=1 dw=21 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_504d_t252s1d21_slope_v101_signal(closeadj, ppnenet, revenue):
    base = _f28_pricing_proxy(revenue, ppnenet, 504) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=252 sc=7 dw=63 prim=_f28_pricing_proxy mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_proxy_504d_t252s7d63_slope_v102_signal(closeadj, ppnenet, revenue):
    base = (_f28_pricing_proxy(revenue, ppnenet, 504) * closeadj) * (closeadj.pct_change(252).abs() + 1.0)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=21 sc=6 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_5d_t21s6d5_slope_v103_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 5) + 21).rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=63 sc=4 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_5d_t63s4d21_slope_v104_signal(assets, closeadj, revenue):
    base = _z(_f28_pricing_dynamics(revenue, assets, 5), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=126 sc=2 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_5d_t126s2d63_slope_v105_signal(assets, closeadj, revenue):
    base = _mean(_f28_pricing_dynamics(revenue, assets, 5), 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=252 sc=1 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_5d_t252s1d5_slope_v106_signal(assets, closeadj, revenue):
    base = _f28_pricing_dynamics(revenue, assets, 5) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=252 sc=7 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_5d_t252s7d21_slope_v107_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 5) * closeadj) * (closeadj.pct_change(252).abs() + 1.0)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=21 sc=5 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_10d_t21s5d63_slope_v108_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 10) * closeadj).shift(21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=63 sc=4 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_10d_t63s4d5_slope_v109_signal(assets, closeadj, revenue):
    base = _z(_f28_pricing_dynamics(revenue, assets, 10), 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=126 sc=2 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_10d_t126s2d21_slope_v110_signal(assets, closeadj, revenue):
    base = _mean(_f28_pricing_dynamics(revenue, assets, 10), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=252 sc=0 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_10d_t252s0d63_slope_v111_signal(assets, closeadj, revenue):
    base = _f28_pricing_dynamics(revenue, assets, 10) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=252 sc=7 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_10d_t252s7d5_slope_v112_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 10) * closeadj) * (closeadj.pct_change(252).abs() + 1.0)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=21 sc=5 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_21d_t21s5d21_slope_v113_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 21) * closeadj).shift(21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=63 sc=3 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_21d_t63s3d63_slope_v114_signal(assets, closeadj, revenue):
    base = _std(_f28_pricing_dynamics(revenue, assets, 21), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=126 sc=2 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_21d_t126s2d5_slope_v115_signal(assets, closeadj, revenue):
    base = _mean(_f28_pricing_dynamics(revenue, assets, 21), 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=252 sc=0 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_21d_t252s0d21_slope_v116_signal(assets, closeadj, revenue):
    base = _f28_pricing_dynamics(revenue, assets, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=252 sc=6 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_21d_t252s6d63_slope_v117_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 21) + 252).rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=21 sc=5 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_42d_t21s5d5_slope_v118_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 42) * closeadj).shift(21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=63 sc=3 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_42d_t63s3d21_slope_v119_signal(assets, closeadj, revenue):
    base = _std(_f28_pricing_dynamics(revenue, assets, 42), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=126 sc=1 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_42d_t126s1d63_slope_v120_signal(assets, closeadj, revenue):
    base = _f28_pricing_dynamics(revenue, assets, 42) * closeadj * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=252 sc=0 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_42d_t252s0d5_slope_v121_signal(assets, closeadj, revenue):
    base = _f28_pricing_dynamics(revenue, assets, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=252 sc=6 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_42d_t252s6d21_slope_v122_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 42) + 252).rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=21 sc=4 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_63d_t21s4d63_slope_v123_signal(assets, closeadj, revenue):
    base = _z(_f28_pricing_dynamics(revenue, assets, 63), 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=63 sc=3 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_63d_t63s3d5_slope_v124_signal(assets, closeadj, revenue):
    base = _std(_f28_pricing_dynamics(revenue, assets, 63), 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=126 sc=1 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_63d_t126s1d21_slope_v125_signal(assets, closeadj, revenue):
    base = _f28_pricing_dynamics(revenue, assets, 63) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=126 sc=7 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_63d_t126s7d63_slope_v126_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 63) * closeadj) * (closeadj.pct_change(126).abs() + 1.0)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=252 sc=6 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_63d_t252s6d5_slope_v127_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 63) + 252).rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=21 sc=4 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_126d_t21s4d21_slope_v128_signal(assets, closeadj, revenue):
    base = _z(_f28_pricing_dynamics(revenue, assets, 126), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=63 sc=2 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_126d_t63s2d63_slope_v129_signal(assets, closeadj, revenue):
    base = _mean(_f28_pricing_dynamics(revenue, assets, 126), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=126 sc=1 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_126d_t126s1d5_slope_v130_signal(assets, closeadj, revenue):
    base = _f28_pricing_dynamics(revenue, assets, 126) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=126 sc=7 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_126d_t126s7d21_slope_v131_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 126) * closeadj) * (closeadj.pct_change(126).abs() + 1.0)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=252 sc=5 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_126d_t252s5d63_slope_v132_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 126) * closeadj).shift(252)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=21 sc=4 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_189d_t21s4d5_slope_v133_signal(assets, closeadj, revenue):
    base = _z(_f28_pricing_dynamics(revenue, assets, 189), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=63 sc=2 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_189d_t63s2d21_slope_v134_signal(assets, closeadj, revenue):
    base = _mean(_f28_pricing_dynamics(revenue, assets, 189), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=126 sc=0 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_189d_t126s0d63_slope_v135_signal(assets, closeadj, revenue):
    base = _f28_pricing_dynamics(revenue, assets, 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=126 sc=7 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_189d_t126s7d5_slope_v136_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 189) * closeadj) * (closeadj.pct_change(126).abs() + 1.0)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=252 sc=5 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_189d_t252s5d21_slope_v137_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 189) * closeadj).shift(252)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=21 sc=3 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_252d_t21s3d63_slope_v138_signal(assets, closeadj, revenue):
    base = _std(_f28_pricing_dynamics(revenue, assets, 252), 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=63 sc=2 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_252d_t63s2d5_slope_v139_signal(assets, closeadj, revenue):
    base = _mean(_f28_pricing_dynamics(revenue, assets, 252), 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=126 sc=0 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_252d_t126s0d21_slope_v140_signal(assets, closeadj, revenue):
    base = _f28_pricing_dynamics(revenue, assets, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=126 sc=6 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_252d_t126s6d63_slope_v141_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 252) + 126).rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=252 sc=5 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_252d_t252s5d5_slope_v142_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 252) * closeadj).shift(252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=21 sc=3 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_378d_t21s3d21_slope_v143_signal(assets, closeadj, revenue):
    base = _std(_f28_pricing_dynamics(revenue, assets, 378), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=63 sc=1 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_378d_t63s1d63_slope_v144_signal(assets, closeadj, revenue):
    base = _f28_pricing_dynamics(revenue, assets, 378) * closeadj * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=126 sc=0 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_378d_t126s0d5_slope_v145_signal(assets, closeadj, revenue):
    base = _f28_pricing_dynamics(revenue, assets, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=126 sc=6 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_378d_t126s6d21_slope_v146_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 378) + 126).rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=252 sc=4 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_378d_t252s4d63_slope_v147_signal(assets, closeadj, revenue):
    base = _z(_f28_pricing_dynamics(revenue, assets, 378), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=21 sc=3 dw=5 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_504d_t21s3d5_slope_v148_signal(assets, closeadj, revenue):
    base = _std(_f28_pricing_dynamics(revenue, assets, 504), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=63 sc=1 dw=21 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_504d_t63s1d21_slope_v149_signal(assets, closeadj, revenue):
    base = _f28_pricing_dynamics(revenue, assets, 504) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=63 sc=7 dw=63 prim=_f28_pricing_dynamics mode=slope
def f28ppd_f28_power_pricing_dynamics_pricing_dynamics_504d_t63s7d63_slope_v150_signal(assets, closeadj, revenue):
    base = (_f28_pricing_dynamics(revenue, assets, 504) * closeadj) * (closeadj.pct_change(63).abs() + 1.0)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_5d_t21s0d5_slope_v001_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_5d_t21s6d21_slope_v002_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_5d_t63s4d63_slope_v003_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_5d_t126s3d5_slope_v004_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_5d_t252s1d21_slope_v005_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_5d_t252s7d63_slope_v006_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_10d_t21s6d5_slope_v007_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_10d_t63s4d21_slope_v008_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_10d_t126s2d63_slope_v009_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_10d_t252s1d5_slope_v010_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_10d_t252s7d21_slope_v011_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_21d_t21s5d63_slope_v012_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_21d_t63s4d5_slope_v013_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_21d_t126s2d21_slope_v014_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_21d_t252s0d63_slope_v015_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_21d_t252s7d5_slope_v016_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_42d_t21s5d21_slope_v017_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_42d_t63s3d63_slope_v018_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_42d_t126s2d5_slope_v019_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_42d_t252s0d21_slope_v020_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_42d_t252s6d63_slope_v021_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_63d_t21s5d5_slope_v022_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_63d_t63s3d21_slope_v023_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_63d_t126s1d63_slope_v024_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_63d_t252s0d5_slope_v025_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_63d_t252s6d21_slope_v026_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_126d_t21s4d63_slope_v027_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_126d_t63s3d5_slope_v028_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_126d_t126s1d21_slope_v029_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_126d_t126s7d63_slope_v030_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_126d_t252s6d5_slope_v031_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_189d_t21s4d21_slope_v032_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_189d_t63s2d63_slope_v033_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_189d_t126s1d5_slope_v034_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_189d_t126s7d21_slope_v035_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_189d_t252s5d63_slope_v036_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_252d_t21s4d5_slope_v037_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_252d_t63s2d21_slope_v038_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_252d_t126s0d63_slope_v039_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_252d_t126s7d5_slope_v040_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_252d_t252s5d21_slope_v041_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_378d_t21s3d63_slope_v042_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_378d_t63s2d5_slope_v043_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_378d_t126s0d21_slope_v044_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_378d_t126s6d63_slope_v045_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_378d_t252s5d5_slope_v046_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_504d_t21s3d21_slope_v047_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_504d_t63s1d63_slope_v048_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_504d_t126s0d5_slope_v049_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_504d_t126s6d21_slope_v050_signal,
    f28ppd_f28_power_pricing_dynamics_revenue_per_asset_504d_t252s4d63_slope_v051_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_5d_t21s3d5_slope_v052_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_5d_t63s1d21_slope_v053_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_5d_t63s7d63_slope_v054_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_5d_t126s6d5_slope_v055_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_5d_t252s4d21_slope_v056_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_10d_t21s2d63_slope_v057_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_10d_t63s1d5_slope_v058_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_10d_t63s7d21_slope_v059_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_10d_t126s5d63_slope_v060_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_10d_t252s4d5_slope_v061_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_21d_t21s2d21_slope_v062_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_21d_t63s0d63_slope_v063_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_21d_t63s7d5_slope_v064_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_21d_t126s5d21_slope_v065_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_21d_t252s3d63_slope_v066_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_42d_t21s2d5_slope_v067_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_42d_t63s0d21_slope_v068_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_42d_t63s6d63_slope_v069_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_42d_t126s5d5_slope_v070_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_42d_t252s3d21_slope_v071_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_63d_t21s1d63_slope_v072_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_63d_t63s0d5_slope_v073_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_63d_t63s6d21_slope_v074_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_63d_t126s4d63_slope_v075_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_63d_t252s3d5_slope_v076_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_126d_t21s1d21_slope_v077_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_126d_t21s7d63_slope_v078_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_126d_t63s6d5_slope_v079_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_126d_t126s4d21_slope_v080_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_126d_t252s2d63_slope_v081_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_189d_t21s1d5_slope_v082_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_189d_t21s7d21_slope_v083_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_189d_t63s5d63_slope_v084_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_189d_t126s4d5_slope_v085_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_189d_t252s2d21_slope_v086_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_252d_t21s0d63_slope_v087_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_252d_t21s7d5_slope_v088_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_252d_t63s5d21_slope_v089_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_252d_t126s3d63_slope_v090_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_252d_t252s2d5_slope_v091_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_378d_t21s0d21_slope_v092_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_378d_t21s6d63_slope_v093_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_378d_t63s5d5_slope_v094_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_378d_t126s3d21_slope_v095_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_378d_t252s1d63_slope_v096_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_504d_t21s0d5_slope_v097_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_504d_t21s6d21_slope_v098_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_504d_t63s4d63_slope_v099_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_504d_t126s3d5_slope_v100_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_504d_t252s1d21_slope_v101_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_proxy_504d_t252s7d63_slope_v102_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_5d_t21s6d5_slope_v103_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_5d_t63s4d21_slope_v104_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_5d_t126s2d63_slope_v105_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_5d_t252s1d5_slope_v106_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_5d_t252s7d21_slope_v107_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_10d_t21s5d63_slope_v108_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_10d_t63s4d5_slope_v109_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_10d_t126s2d21_slope_v110_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_10d_t252s0d63_slope_v111_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_10d_t252s7d5_slope_v112_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_21d_t21s5d21_slope_v113_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_21d_t63s3d63_slope_v114_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_21d_t126s2d5_slope_v115_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_21d_t252s0d21_slope_v116_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_21d_t252s6d63_slope_v117_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_42d_t21s5d5_slope_v118_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_42d_t63s3d21_slope_v119_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_42d_t126s1d63_slope_v120_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_42d_t252s0d5_slope_v121_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_42d_t252s6d21_slope_v122_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_63d_t21s4d63_slope_v123_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_63d_t63s3d5_slope_v124_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_63d_t126s1d21_slope_v125_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_63d_t126s7d63_slope_v126_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_63d_t252s6d5_slope_v127_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_126d_t21s4d21_slope_v128_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_126d_t63s2d63_slope_v129_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_126d_t126s1d5_slope_v130_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_126d_t126s7d21_slope_v131_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_126d_t252s5d63_slope_v132_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_189d_t21s4d5_slope_v133_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_189d_t63s2d21_slope_v134_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_189d_t126s0d63_slope_v135_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_189d_t126s7d5_slope_v136_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_189d_t252s5d21_slope_v137_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_252d_t21s3d63_slope_v138_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_252d_t63s2d5_slope_v139_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_252d_t126s0d21_slope_v140_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_252d_t126s6d63_slope_v141_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_252d_t252s5d5_slope_v142_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_378d_t21s3d21_slope_v143_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_378d_t63s1d63_slope_v144_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_378d_t126s0d5_slope_v145_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_378d_t126s6d21_slope_v146_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_378d_t252s4d63_slope_v147_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_504d_t21s3d5_slope_v148_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_504d_t63s1d21_slope_v149_signal,
    f28ppd_f28_power_pricing_dynamics_pricing_dynamics_504d_t63s7d63_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_POWER_PRICING_DYNAMICS_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ('_f28_revenue_per_asset', '_f28_pricing_proxy', '_f28_pricing_dynamics')
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
    print(f"OK f28_power_pricing_dynamics_2nd_derivatives_001_150_claude: {n_features} features pass")
