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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)

# ===== folder domain primitives =====
def _f27_asset_growth(assets, w):
    return assets.pct_change(periods=w)


def _f27_capacity_pulse(ppnenet, w):
    g = ppnenet.pct_change(periods=w)
    return g - g.rolling(w, min_periods=max(1, w // 2)).mean()


def _f27_growth_quality(assets, capex, w):
    ag = assets.pct_change(periods=w)
    ci = capex.rolling(w, min_periods=max(1, w // 2)).sum() / assets.replace(0, np.nan).abs()
    return ag * ci



# ===== features =====

# bw=5 tr=21 sc=0 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_5d_t21s0d5_jerk_v001_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=21 sc=6 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_5d_t21s6d21_jerk_v002_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 5) + 21).rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=63 sc=4 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_5d_t63s4d63_jerk_v003_signal(assets, closeadj):
    base = _z(_f27_asset_growth(assets, 5), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=126 sc=3 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_5d_t126s3d5_jerk_v004_signal(assets, closeadj):
    base = _std(_f27_asset_growth(assets, 5), 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=252 sc=1 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_5d_t252s1d21_jerk_v005_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 5) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=252 sc=7 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_5d_t252s7d63_jerk_v006_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 5) * closeadj) * (closeadj.pct_change(252).abs() + 1.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=21 sc=6 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_10d_t21s6d5_jerk_v007_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 10) + 21).rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=63 sc=4 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_10d_t63s4d21_jerk_v008_signal(assets, closeadj):
    base = _z(_f27_asset_growth(assets, 10), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=126 sc=2 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_10d_t126s2d63_jerk_v009_signal(assets, closeadj):
    base = _mean(_f27_asset_growth(assets, 10), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=252 sc=1 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_10d_t252s1d5_jerk_v010_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 10) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=252 sc=7 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_10d_t252s7d21_jerk_v011_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 10) * closeadj) * (closeadj.pct_change(252).abs() + 1.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=21 sc=5 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_21d_t21s5d63_jerk_v012_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 21) * closeadj).shift(21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=63 sc=4 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_21d_t63s4d5_jerk_v013_signal(assets, closeadj):
    base = _z(_f27_asset_growth(assets, 21), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=126 sc=2 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_21d_t126s2d21_jerk_v014_signal(assets, closeadj):
    base = _mean(_f27_asset_growth(assets, 21), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=252 sc=0 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_21d_t252s0d63_jerk_v015_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=252 sc=7 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_21d_t252s7d5_jerk_v016_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 21) * closeadj) * (closeadj.pct_change(252).abs() + 1.0)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=21 sc=5 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_42d_t21s5d21_jerk_v017_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 42) * closeadj).shift(21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=63 sc=3 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_42d_t63s3d63_jerk_v018_signal(assets, closeadj):
    base = _std(_f27_asset_growth(assets, 42), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=126 sc=2 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_42d_t126s2d5_jerk_v019_signal(assets, closeadj):
    base = _mean(_f27_asset_growth(assets, 42), 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=252 sc=0 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_42d_t252s0d21_jerk_v020_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=252 sc=6 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_42d_t252s6d63_jerk_v021_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 42) + 252).rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=21 sc=5 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_63d_t21s5d5_jerk_v022_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 63) * closeadj).shift(21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=63 sc=3 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_63d_t63s3d21_jerk_v023_signal(assets, closeadj):
    base = _std(_f27_asset_growth(assets, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=126 sc=1 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_63d_t126s1d63_jerk_v024_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 63) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=252 sc=0 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_63d_t252s0d5_jerk_v025_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=252 sc=6 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_63d_t252s6d21_jerk_v026_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 63) + 252).rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=21 sc=4 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_126d_t21s4d63_jerk_v027_signal(assets, closeadj):
    base = _z(_f27_asset_growth(assets, 126), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=63 sc=3 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_126d_t63s3d5_jerk_v028_signal(assets, closeadj):
    base = _std(_f27_asset_growth(assets, 126), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=126 sc=1 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_126d_t126s1d21_jerk_v029_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 126) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=126 sc=7 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_126d_t126s7d63_jerk_v030_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 126) * closeadj) * (closeadj.pct_change(126).abs() + 1.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=252 sc=6 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_126d_t252s6d5_jerk_v031_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 126) + 252).rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=21 sc=4 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_189d_t21s4d21_jerk_v032_signal(assets, closeadj):
    base = _z(_f27_asset_growth(assets, 189), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=63 sc=2 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_189d_t63s2d63_jerk_v033_signal(assets, closeadj):
    base = _mean(_f27_asset_growth(assets, 189), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=126 sc=1 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_189d_t126s1d5_jerk_v034_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 189) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=126 sc=7 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_189d_t126s7d21_jerk_v035_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 189) * closeadj) * (closeadj.pct_change(126).abs() + 1.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=252 sc=5 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_189d_t252s5d63_jerk_v036_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 189) * closeadj).shift(252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=21 sc=4 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_252d_t21s4d5_jerk_v037_signal(assets, closeadj):
    base = _z(_f27_asset_growth(assets, 252), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=63 sc=2 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_252d_t63s2d21_jerk_v038_signal(assets, closeadj):
    base = _mean(_f27_asset_growth(assets, 252), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=126 sc=0 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_252d_t126s0d63_jerk_v039_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=126 sc=7 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_252d_t126s7d5_jerk_v040_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 252) * closeadj) * (closeadj.pct_change(126).abs() + 1.0)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=252 sc=5 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_252d_t252s5d21_jerk_v041_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 252) * closeadj).shift(252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=21 sc=3 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_378d_t21s3d63_jerk_v042_signal(assets, closeadj):
    base = _std(_f27_asset_growth(assets, 378), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=63 sc=2 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_378d_t63s2d5_jerk_v043_signal(assets, closeadj):
    base = _mean(_f27_asset_growth(assets, 378), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=126 sc=0 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_378d_t126s0d21_jerk_v044_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=126 sc=6 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_378d_t126s6d63_jerk_v045_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 378) + 126).rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=252 sc=5 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_378d_t252s5d5_jerk_v046_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 378) * closeadj).shift(252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=21 sc=3 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_504d_t21s3d21_jerk_v047_signal(assets, closeadj):
    base = _std(_f27_asset_growth(assets, 504), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=63 sc=1 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_504d_t63s1d63_jerk_v048_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 504) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=126 sc=0 dw=5 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_504d_t126s0d5_jerk_v049_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=126 sc=6 dw=21 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_504d_t126s6d21_jerk_v050_signal(assets, closeadj):
    base = (_f27_asset_growth(assets, 504) + 126).rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=252 sc=4 dw=63 prim=_f27_asset_growth mode=jerk
def f27icg_f27_ipp_capacity_growth_asset_growth_504d_t252s4d63_jerk_v051_signal(assets, closeadj):
    base = _z(_f27_asset_growth(assets, 504), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=21 sc=3 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t21s3d5_jerk_v052_signal(closeadj, ppnenet):
    base = _std(_f27_capacity_pulse(ppnenet, 5), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=63 sc=1 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t63s1d21_jerk_v053_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 5) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=63 sc=7 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t63s7d63_jerk_v054_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 5) * closeadj) * (closeadj.pct_change(63).abs() + 1.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=126 sc=6 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t126s6d5_jerk_v055_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 5) + 126).rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=252 sc=4 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t252s4d21_jerk_v056_signal(closeadj, ppnenet):
    base = _z(_f27_capacity_pulse(ppnenet, 5), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=21 sc=2 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t21s2d63_jerk_v057_signal(closeadj, ppnenet):
    base = _mean(_f27_capacity_pulse(ppnenet, 10), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=63 sc=1 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t63s1d5_jerk_v058_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 10) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=63 sc=7 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t63s7d21_jerk_v059_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 10) * closeadj) * (closeadj.pct_change(63).abs() + 1.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=126 sc=5 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t126s5d63_jerk_v060_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 10) * closeadj).shift(126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=252 sc=4 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t252s4d5_jerk_v061_signal(closeadj, ppnenet):
    base = _z(_f27_capacity_pulse(ppnenet, 10), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=21 sc=2 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t21s2d21_jerk_v062_signal(closeadj, ppnenet):
    base = _mean(_f27_capacity_pulse(ppnenet, 21), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=63 sc=0 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t63s0d63_jerk_v063_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=63 sc=7 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t63s7d5_jerk_v064_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 21) * closeadj) * (closeadj.pct_change(63).abs() + 1.0)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=126 sc=5 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t126s5d21_jerk_v065_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 21) * closeadj).shift(126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=252 sc=3 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t252s3d63_jerk_v066_signal(closeadj, ppnenet):
    base = _std(_f27_capacity_pulse(ppnenet, 21), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=21 sc=2 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t21s2d5_jerk_v067_signal(closeadj, ppnenet):
    base = _mean(_f27_capacity_pulse(ppnenet, 42), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=63 sc=0 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t63s0d21_jerk_v068_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=63 sc=6 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t63s6d63_jerk_v069_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 42) + 63).rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=126 sc=5 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t126s5d5_jerk_v070_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 42) * closeadj).shift(126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=252 sc=3 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t252s3d21_jerk_v071_signal(closeadj, ppnenet):
    base = _std(_f27_capacity_pulse(ppnenet, 42), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=21 sc=1 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t21s1d63_jerk_v072_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 63) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=63 sc=0 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t63s0d5_jerk_v073_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=63 sc=6 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t63s6d21_jerk_v074_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 63) + 63).rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=126 sc=4 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t126s4d63_jerk_v075_signal(closeadj, ppnenet):
    base = _z(_f27_capacity_pulse(ppnenet, 63), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=252 sc=3 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t252s3d5_jerk_v076_signal(closeadj, ppnenet):
    base = _std(_f27_capacity_pulse(ppnenet, 63), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=21 sc=1 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t21s1d21_jerk_v077_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 126) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=21 sc=7 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t21s7d63_jerk_v078_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 126) * closeadj) * (closeadj.pct_change(21).abs() + 1.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=63 sc=6 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t63s6d5_jerk_v079_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 126) + 63).rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=126 sc=4 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t126s4d21_jerk_v080_signal(closeadj, ppnenet):
    base = _z(_f27_capacity_pulse(ppnenet, 126), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=252 sc=2 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t252s2d63_jerk_v081_signal(closeadj, ppnenet):
    base = _mean(_f27_capacity_pulse(ppnenet, 126), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=21 sc=1 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t21s1d5_jerk_v082_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 189) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=21 sc=7 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t21s7d21_jerk_v083_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 189) * closeadj) * (closeadj.pct_change(21).abs() + 1.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=63 sc=5 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t63s5d63_jerk_v084_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 189) * closeadj).shift(63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=126 sc=4 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t126s4d5_jerk_v085_signal(closeadj, ppnenet):
    base = _z(_f27_capacity_pulse(ppnenet, 189), 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=252 sc=2 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t252s2d21_jerk_v086_signal(closeadj, ppnenet):
    base = _mean(_f27_capacity_pulse(ppnenet, 189), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=21 sc=0 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_252d_t21s0d63_jerk_v087_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=21 sc=7 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_252d_t21s7d5_jerk_v088_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 252) * closeadj) * (closeadj.pct_change(21).abs() + 1.0)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=63 sc=5 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_252d_t63s5d21_jerk_v089_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 252) * closeadj).shift(63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=126 sc=3 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_252d_t126s3d63_jerk_v090_signal(closeadj, ppnenet):
    base = _std(_f27_capacity_pulse(ppnenet, 252), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=252 sc=2 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_252d_t252s2d5_jerk_v091_signal(closeadj, ppnenet):
    base = _mean(_f27_capacity_pulse(ppnenet, 252), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=21 sc=0 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_378d_t21s0d21_jerk_v092_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=21 sc=6 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_378d_t21s6d63_jerk_v093_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 378) + 21).rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=63 sc=5 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_378d_t63s5d5_jerk_v094_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 378) * closeadj).shift(63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=126 sc=3 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_378d_t126s3d21_jerk_v095_signal(closeadj, ppnenet):
    base = _std(_f27_capacity_pulse(ppnenet, 378), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=252 sc=1 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_378d_t252s1d63_jerk_v096_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 378) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=21 sc=0 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_504d_t21s0d5_jerk_v097_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=21 sc=6 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_504d_t21s6d21_jerk_v098_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 504) + 21).rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=63 sc=4 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_504d_t63s4d63_jerk_v099_signal(closeadj, ppnenet):
    base = _z(_f27_capacity_pulse(ppnenet, 504), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=126 sc=3 dw=5 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_504d_t126s3d5_jerk_v100_signal(closeadj, ppnenet):
    base = _std(_f27_capacity_pulse(ppnenet, 504), 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=252 sc=1 dw=21 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_504d_t252s1d21_jerk_v101_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 504) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=252 sc=7 dw=63 prim=_f27_capacity_pulse mode=jerk
def f27icg_f27_ipp_capacity_growth_capacity_pulse_504d_t252s7d63_jerk_v102_signal(closeadj, ppnenet):
    base = (_f27_capacity_pulse(ppnenet, 504) * closeadj) * (closeadj.pct_change(252).abs() + 1.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=21 sc=6 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_5d_t21s6d5_jerk_v103_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 5) + 21).rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=63 sc=4 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_5d_t63s4d21_jerk_v104_signal(assets, capex, closeadj):
    base = _z(_f27_growth_quality(assets, capex, 5), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=126 sc=2 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_5d_t126s2d63_jerk_v105_signal(assets, capex, closeadj):
    base = _mean(_f27_growth_quality(assets, capex, 5), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=252 sc=1 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_5d_t252s1d5_jerk_v106_signal(assets, capex, closeadj):
    base = _f27_growth_quality(assets, capex, 5) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=5 tr=252 sc=7 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_5d_t252s7d21_jerk_v107_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 5) * closeadj) * (closeadj.pct_change(252).abs() + 1.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=21 sc=5 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_10d_t21s5d63_jerk_v108_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 10) * closeadj).shift(21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=63 sc=4 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_10d_t63s4d5_jerk_v109_signal(assets, capex, closeadj):
    base = _z(_f27_growth_quality(assets, capex, 10), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=126 sc=2 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_10d_t126s2d21_jerk_v110_signal(assets, capex, closeadj):
    base = _mean(_f27_growth_quality(assets, capex, 10), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=252 sc=0 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_10d_t252s0d63_jerk_v111_signal(assets, capex, closeadj):
    base = _f27_growth_quality(assets, capex, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=10 tr=252 sc=7 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_10d_t252s7d5_jerk_v112_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 10) * closeadj) * (closeadj.pct_change(252).abs() + 1.0)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=21 sc=5 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_21d_t21s5d21_jerk_v113_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 21) * closeadj).shift(21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=63 sc=3 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_21d_t63s3d63_jerk_v114_signal(assets, capex, closeadj):
    base = _std(_f27_growth_quality(assets, capex, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=126 sc=2 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_21d_t126s2d5_jerk_v115_signal(assets, capex, closeadj):
    base = _mean(_f27_growth_quality(assets, capex, 21), 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=252 sc=0 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_21d_t252s0d21_jerk_v116_signal(assets, capex, closeadj):
    base = _f27_growth_quality(assets, capex, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=21 tr=252 sc=6 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_21d_t252s6d63_jerk_v117_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 21) + 252).rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=21 sc=5 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_42d_t21s5d5_jerk_v118_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 42) * closeadj).shift(21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=63 sc=3 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_42d_t63s3d21_jerk_v119_signal(assets, capex, closeadj):
    base = _std(_f27_growth_quality(assets, capex, 42), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=126 sc=1 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_42d_t126s1d63_jerk_v120_signal(assets, capex, closeadj):
    base = _f27_growth_quality(assets, capex, 42) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=252 sc=0 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_42d_t252s0d5_jerk_v121_signal(assets, capex, closeadj):
    base = _f27_growth_quality(assets, capex, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=42 tr=252 sc=6 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_42d_t252s6d21_jerk_v122_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 42) + 252).rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=21 sc=4 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_63d_t21s4d63_jerk_v123_signal(assets, capex, closeadj):
    base = _z(_f27_growth_quality(assets, capex, 63), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=63 sc=3 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_63d_t63s3d5_jerk_v124_signal(assets, capex, closeadj):
    base = _std(_f27_growth_quality(assets, capex, 63), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=126 sc=1 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_63d_t126s1d21_jerk_v125_signal(assets, capex, closeadj):
    base = _f27_growth_quality(assets, capex, 63) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=126 sc=7 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_63d_t126s7d63_jerk_v126_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 63) * closeadj) * (closeadj.pct_change(126).abs() + 1.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=63 tr=252 sc=6 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_63d_t252s6d5_jerk_v127_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 63) + 252).rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=21 sc=4 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_126d_t21s4d21_jerk_v128_signal(assets, capex, closeadj):
    base = _z(_f27_growth_quality(assets, capex, 126), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=63 sc=2 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_126d_t63s2d63_jerk_v129_signal(assets, capex, closeadj):
    base = _mean(_f27_growth_quality(assets, capex, 126), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=126 sc=1 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_126d_t126s1d5_jerk_v130_signal(assets, capex, closeadj):
    base = _f27_growth_quality(assets, capex, 126) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=126 sc=7 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_126d_t126s7d21_jerk_v131_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 126) * closeadj) * (closeadj.pct_change(126).abs() + 1.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=126 tr=252 sc=5 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_126d_t252s5d63_jerk_v132_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 126) * closeadj).shift(252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=21 sc=4 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_189d_t21s4d5_jerk_v133_signal(assets, capex, closeadj):
    base = _z(_f27_growth_quality(assets, capex, 189), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=63 sc=2 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_189d_t63s2d21_jerk_v134_signal(assets, capex, closeadj):
    base = _mean(_f27_growth_quality(assets, capex, 189), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=126 sc=0 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_189d_t126s0d63_jerk_v135_signal(assets, capex, closeadj):
    base = _f27_growth_quality(assets, capex, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=126 sc=7 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_189d_t126s7d5_jerk_v136_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 189) * closeadj) * (closeadj.pct_change(126).abs() + 1.0)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=189 tr=252 sc=5 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_189d_t252s5d21_jerk_v137_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 189) * closeadj).shift(252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=21 sc=3 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_252d_t21s3d63_jerk_v138_signal(assets, capex, closeadj):
    base = _std(_f27_growth_quality(assets, capex, 252), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=63 sc=2 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_252d_t63s2d5_jerk_v139_signal(assets, capex, closeadj):
    base = _mean(_f27_growth_quality(assets, capex, 252), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=126 sc=0 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_252d_t126s0d21_jerk_v140_signal(assets, capex, closeadj):
    base = _f27_growth_quality(assets, capex, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=126 sc=6 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_252d_t126s6d63_jerk_v141_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 252) + 126).rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=252 tr=252 sc=5 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_252d_t252s5d5_jerk_v142_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 252) * closeadj).shift(252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=21 sc=3 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_378d_t21s3d21_jerk_v143_signal(assets, capex, closeadj):
    base = _std(_f27_growth_quality(assets, capex, 378), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=63 sc=1 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_378d_t63s1d63_jerk_v144_signal(assets, capex, closeadj):
    base = _f27_growth_quality(assets, capex, 378) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=126 sc=0 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_378d_t126s0d5_jerk_v145_signal(assets, capex, closeadj):
    base = _f27_growth_quality(assets, capex, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=126 sc=6 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_378d_t126s6d21_jerk_v146_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 378) + 126).rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=378 tr=252 sc=4 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_378d_t252s4d63_jerk_v147_signal(assets, capex, closeadj):
    base = _z(_f27_growth_quality(assets, capex, 378), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=21 sc=3 dw=5 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_504d_t21s3d5_jerk_v148_signal(assets, capex, closeadj):
    base = _std(_f27_growth_quality(assets, capex, 504), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=63 sc=1 dw=21 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_504d_t63s1d21_jerk_v149_signal(assets, capex, closeadj):
    base = _f27_growth_quality(assets, capex, 504) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# bw=504 tr=63 sc=7 dw=63 prim=_f27_growth_quality mode=jerk
def f27icg_f27_ipp_capacity_growth_growth_quality_504d_t63s7d63_jerk_v150_signal(assets, capex, closeadj):
    base = (_f27_growth_quality(assets, capex, 504) * closeadj) * (closeadj.pct_change(63).abs() + 1.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f27icg_f27_ipp_capacity_growth_asset_growth_5d_t21s0d5_jerk_v001_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_5d_t21s6d21_jerk_v002_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_5d_t63s4d63_jerk_v003_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_5d_t126s3d5_jerk_v004_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_5d_t252s1d21_jerk_v005_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_5d_t252s7d63_jerk_v006_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_10d_t21s6d5_jerk_v007_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_10d_t63s4d21_jerk_v008_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_10d_t126s2d63_jerk_v009_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_10d_t252s1d5_jerk_v010_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_10d_t252s7d21_jerk_v011_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_21d_t21s5d63_jerk_v012_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_21d_t63s4d5_jerk_v013_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_21d_t126s2d21_jerk_v014_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_21d_t252s0d63_jerk_v015_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_21d_t252s7d5_jerk_v016_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_42d_t21s5d21_jerk_v017_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_42d_t63s3d63_jerk_v018_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_42d_t126s2d5_jerk_v019_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_42d_t252s0d21_jerk_v020_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_42d_t252s6d63_jerk_v021_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_63d_t21s5d5_jerk_v022_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_63d_t63s3d21_jerk_v023_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_63d_t126s1d63_jerk_v024_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_63d_t252s0d5_jerk_v025_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_63d_t252s6d21_jerk_v026_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_126d_t21s4d63_jerk_v027_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_126d_t63s3d5_jerk_v028_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_126d_t126s1d21_jerk_v029_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_126d_t126s7d63_jerk_v030_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_126d_t252s6d5_jerk_v031_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_189d_t21s4d21_jerk_v032_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_189d_t63s2d63_jerk_v033_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_189d_t126s1d5_jerk_v034_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_189d_t126s7d21_jerk_v035_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_189d_t252s5d63_jerk_v036_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_252d_t21s4d5_jerk_v037_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_252d_t63s2d21_jerk_v038_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_252d_t126s0d63_jerk_v039_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_252d_t126s7d5_jerk_v040_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_252d_t252s5d21_jerk_v041_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_378d_t21s3d63_jerk_v042_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_378d_t63s2d5_jerk_v043_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_378d_t126s0d21_jerk_v044_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_378d_t126s6d63_jerk_v045_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_378d_t252s5d5_jerk_v046_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_504d_t21s3d21_jerk_v047_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_504d_t63s1d63_jerk_v048_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_504d_t126s0d5_jerk_v049_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_504d_t126s6d21_jerk_v050_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_504d_t252s4d63_jerk_v051_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t21s3d5_jerk_v052_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t63s1d21_jerk_v053_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t63s7d63_jerk_v054_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t126s6d5_jerk_v055_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t252s4d21_jerk_v056_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t21s2d63_jerk_v057_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t63s1d5_jerk_v058_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t63s7d21_jerk_v059_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t126s5d63_jerk_v060_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t252s4d5_jerk_v061_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t21s2d21_jerk_v062_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t63s0d63_jerk_v063_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t63s7d5_jerk_v064_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t126s5d21_jerk_v065_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t252s3d63_jerk_v066_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t21s2d5_jerk_v067_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t63s0d21_jerk_v068_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t63s6d63_jerk_v069_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t126s5d5_jerk_v070_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t252s3d21_jerk_v071_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t21s1d63_jerk_v072_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t63s0d5_jerk_v073_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t63s6d21_jerk_v074_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t126s4d63_jerk_v075_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t252s3d5_jerk_v076_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t21s1d21_jerk_v077_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t21s7d63_jerk_v078_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t63s6d5_jerk_v079_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t126s4d21_jerk_v080_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t252s2d63_jerk_v081_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t21s1d5_jerk_v082_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t21s7d21_jerk_v083_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t63s5d63_jerk_v084_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t126s4d5_jerk_v085_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t252s2d21_jerk_v086_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_252d_t21s0d63_jerk_v087_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_252d_t21s7d5_jerk_v088_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_252d_t63s5d21_jerk_v089_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_252d_t126s3d63_jerk_v090_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_252d_t252s2d5_jerk_v091_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_378d_t21s0d21_jerk_v092_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_378d_t21s6d63_jerk_v093_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_378d_t63s5d5_jerk_v094_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_378d_t126s3d21_jerk_v095_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_378d_t252s1d63_jerk_v096_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_504d_t21s0d5_jerk_v097_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_504d_t21s6d21_jerk_v098_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_504d_t63s4d63_jerk_v099_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_504d_t126s3d5_jerk_v100_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_504d_t252s1d21_jerk_v101_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_504d_t252s7d63_jerk_v102_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_5d_t21s6d5_jerk_v103_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_5d_t63s4d21_jerk_v104_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_5d_t126s2d63_jerk_v105_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_5d_t252s1d5_jerk_v106_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_5d_t252s7d21_jerk_v107_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_10d_t21s5d63_jerk_v108_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_10d_t63s4d5_jerk_v109_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_10d_t126s2d21_jerk_v110_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_10d_t252s0d63_jerk_v111_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_10d_t252s7d5_jerk_v112_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_21d_t21s5d21_jerk_v113_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_21d_t63s3d63_jerk_v114_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_21d_t126s2d5_jerk_v115_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_21d_t252s0d21_jerk_v116_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_21d_t252s6d63_jerk_v117_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_42d_t21s5d5_jerk_v118_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_42d_t63s3d21_jerk_v119_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_42d_t126s1d63_jerk_v120_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_42d_t252s0d5_jerk_v121_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_42d_t252s6d21_jerk_v122_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_63d_t21s4d63_jerk_v123_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_63d_t63s3d5_jerk_v124_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_63d_t126s1d21_jerk_v125_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_63d_t126s7d63_jerk_v126_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_63d_t252s6d5_jerk_v127_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_126d_t21s4d21_jerk_v128_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_126d_t63s2d63_jerk_v129_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_126d_t126s1d5_jerk_v130_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_126d_t126s7d21_jerk_v131_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_126d_t252s5d63_jerk_v132_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_189d_t21s4d5_jerk_v133_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_189d_t63s2d21_jerk_v134_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_189d_t126s0d63_jerk_v135_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_189d_t126s7d5_jerk_v136_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_189d_t252s5d21_jerk_v137_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_252d_t21s3d63_jerk_v138_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_252d_t63s2d5_jerk_v139_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_252d_t126s0d21_jerk_v140_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_252d_t126s6d63_jerk_v141_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_252d_t252s5d5_jerk_v142_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_378d_t21s3d21_jerk_v143_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_378d_t63s1d63_jerk_v144_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_378d_t126s0d5_jerk_v145_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_378d_t126s6d21_jerk_v146_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_378d_t252s4d63_jerk_v147_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_504d_t21s3d5_jerk_v148_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_504d_t63s1d21_jerk_v149_signal,
    f27icg_f27_ipp_capacity_growth_growth_quality_504d_t63s7d63_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_IPP_CAPACITY_GROWTH_REGISTRY_JERK_001_150 = REGISTRY


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
    domain_primitives = ('_f27_asset_growth', '_f27_capacity_pulse', '_f27_growth_quality')
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
    print(f"OK f27_ipp_capacity_growth_3rd_derivatives_001_150_claude: {n_features} features pass")
