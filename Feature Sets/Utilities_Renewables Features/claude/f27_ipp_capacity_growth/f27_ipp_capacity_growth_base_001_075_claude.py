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

# w=10 tr=9 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_10d_t9s0i252_base_v001_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 10)
    val = base.rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=21 tr=1 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_21d_t1s0i252_base_v002_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 21)
    val = _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=21 tr=3 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_21d_t3s0i252_base_v003_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 21)
    val = _z(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=21 tr=5 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_21d_t5s0i252_base_v004_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 21)
    val = base.shift(252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=21 tr=7 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_21d_t7s0i252_base_v005_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 21)
    val = base - _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=21 tr=9 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_21d_t9s0i252_base_v006_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 21)
    val = base.rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=42 tr=1 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_42d_t1s0i252_base_v007_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 42)
    val = _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=42 tr=3 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_42d_t3s0i252_base_v008_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 42)
    val = _z(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=42 tr=5 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_42d_t5s0i252_base_v009_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 42)
    val = base.shift(252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=42 tr=7 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_42d_t7s0i252_base_v010_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 42)
    val = base - _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=42 tr=9 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_42d_t9s0i252_base_v011_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 42)
    val = base.rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=63 tr=1 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_63d_t1s0i252_base_v012_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 63)
    val = _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=63 tr=3 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_63d_t3s0i252_base_v013_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 63)
    val = _z(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=63 tr=5 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_63d_t5s0i252_base_v014_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 63)
    val = base.shift(252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=63 tr=7 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_63d_t7s0i252_base_v015_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 63)
    val = base - _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=63 tr=9 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_63d_t9s0i252_base_v016_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 63)
    val = base.rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=126 tr=1 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_126d_t1s0i252_base_v017_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 126)
    val = _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=126 tr=3 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_126d_t3s0i252_base_v018_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 126)
    val = _z(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=126 tr=5 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_126d_t5s0i252_base_v019_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 126)
    val = base.shift(252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=126 tr=7 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_126d_t7s0i252_base_v020_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 126)
    val = base - _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=126 tr=9 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_126d_t9s0i252_base_v021_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 126)
    val = base.rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=189 tr=1 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_189d_t1s0i252_base_v022_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 189)
    val = _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=189 tr=3 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_189d_t3s0i252_base_v023_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 189)
    val = _z(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=189 tr=5 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_189d_t5s0i252_base_v024_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 189)
    val = base.shift(252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=189 tr=7 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_189d_t7s0i252_base_v025_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 189)
    val = base - _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=189 tr=9 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_189d_t9s0i252_base_v026_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 189)
    val = base.rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=252 tr=1 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_252d_t1s0i252_base_v027_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 252)
    val = _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=252 tr=3 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_252d_t3s0i252_base_v028_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 252)
    val = _z(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=252 tr=5 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_252d_t5s0i252_base_v029_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 252)
    val = base.shift(252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=252 tr=7 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_252d_t7s0i252_base_v030_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 252)
    val = base - _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=252 tr=9 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_252d_t9s0i252_base_v031_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 252)
    val = base.rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=378 tr=1 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_378d_t1s0i252_base_v032_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 378)
    val = _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=378 tr=3 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_378d_t3s0i252_base_v033_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 378)
    val = _z(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=378 tr=5 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_378d_t5s0i252_base_v034_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 378)
    val = base.shift(252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=378 tr=7 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_378d_t7s0i252_base_v035_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 378)
    val = base - _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=378 tr=9 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_378d_t9s0i252_base_v036_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 378)
    val = base.rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=504 tr=1 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_504d_t1s0i252_base_v037_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 504)
    val = _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=504 tr=3 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_504d_t3s0i252_base_v038_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 504)
    val = _z(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=504 tr=5 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_504d_t5s0i252_base_v039_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 504)
    val = base.shift(252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=504 tr=7 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_504d_t7s0i252_base_v040_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 504)
    val = base - _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=504 tr=9 sc=0 iw=252 prim=_f27_asset_growth
def f27icg_f27_ipp_capacity_growth_asset_growth_504d_t9s0i252_base_v041_signal(assets, closeadj):
    base = _f27_asset_growth(assets, 504)
    val = base.rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=5 tr=1 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t1s0i252_base_v042_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 5)
    val = _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=5 tr=3 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t3s0i252_base_v043_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 5)
    val = _z(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=5 tr=5 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t5s0i252_base_v044_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 5)
    val = base.shift(252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=5 tr=7 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t7s0i252_base_v045_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 5)
    val = base - _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=5 tr=9 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t9s0i252_base_v046_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 5)
    val = base.rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=10 tr=1 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t1s0i252_base_v047_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 10)
    val = _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=10 tr=3 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t3s0i252_base_v048_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 10)
    val = _z(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=10 tr=5 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t5s0i252_base_v049_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 10)
    val = base.shift(252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=10 tr=7 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t7s0i252_base_v050_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 10)
    val = base - _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=10 tr=9 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t9s0i252_base_v051_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 10)
    val = base.rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=21 tr=1 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t1s0i252_base_v052_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 21)
    val = _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=21 tr=3 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t3s0i252_base_v053_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 21)
    val = _z(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=21 tr=5 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t5s0i252_base_v054_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 21)
    val = base.shift(252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=21 tr=7 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t7s0i252_base_v055_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 21)
    val = base - _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=21 tr=9 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t9s0i252_base_v056_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 21)
    val = base.rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=42 tr=1 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t1s0i252_base_v057_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 42)
    val = _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=42 tr=3 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t3s0i252_base_v058_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 42)
    val = _z(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=42 tr=5 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t5s0i252_base_v059_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 42)
    val = base.shift(252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=42 tr=7 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t7s0i252_base_v060_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 42)
    val = base - _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=42 tr=9 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t9s0i252_base_v061_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 42)
    val = base.rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=63 tr=1 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t1s0i252_base_v062_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 63)
    val = _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=63 tr=3 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t3s0i252_base_v063_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 63)
    val = _z(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=63 tr=5 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t5s0i252_base_v064_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 63)
    val = base.shift(252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=63 tr=7 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t7s0i252_base_v065_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 63)
    val = base - _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=63 tr=9 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t9s0i252_base_v066_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 63)
    val = base.rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=126 tr=1 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t1s0i252_base_v067_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 126)
    val = _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=126 tr=3 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t3s0i252_base_v068_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 126)
    val = _z(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=126 tr=5 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t5s0i252_base_v069_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 126)
    val = base.shift(252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=126 tr=7 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t7s0i252_base_v070_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 126)
    val = base - _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=126 tr=9 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t9s0i252_base_v071_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 126)
    val = base.rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=189 tr=1 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t1s0i252_base_v072_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 189)
    val = _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=189 tr=3 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t3s0i252_base_v073_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 189)
    val = _z(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=189 tr=5 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t5s0i252_base_v074_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 189)
    val = base.shift(252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# w=189 tr=7 sc=0 iw=252 prim=_f27_capacity_pulse
def f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t7s0i252_base_v075_signal(closeadj, ppnenet):
    base = _f27_capacity_pulse(ppnenet, 189)
    val = base - _mean(base, 252)
    result = val * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f27icg_f27_ipp_capacity_growth_asset_growth_10d_t9s0i252_base_v001_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_21d_t1s0i252_base_v002_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_21d_t3s0i252_base_v003_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_21d_t5s0i252_base_v004_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_21d_t7s0i252_base_v005_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_21d_t9s0i252_base_v006_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_42d_t1s0i252_base_v007_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_42d_t3s0i252_base_v008_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_42d_t5s0i252_base_v009_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_42d_t7s0i252_base_v010_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_42d_t9s0i252_base_v011_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_63d_t1s0i252_base_v012_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_63d_t3s0i252_base_v013_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_63d_t5s0i252_base_v014_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_63d_t7s0i252_base_v015_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_63d_t9s0i252_base_v016_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_126d_t1s0i252_base_v017_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_126d_t3s0i252_base_v018_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_126d_t5s0i252_base_v019_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_126d_t7s0i252_base_v020_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_126d_t9s0i252_base_v021_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_189d_t1s0i252_base_v022_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_189d_t3s0i252_base_v023_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_189d_t5s0i252_base_v024_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_189d_t7s0i252_base_v025_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_189d_t9s0i252_base_v026_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_252d_t1s0i252_base_v027_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_252d_t3s0i252_base_v028_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_252d_t5s0i252_base_v029_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_252d_t7s0i252_base_v030_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_252d_t9s0i252_base_v031_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_378d_t1s0i252_base_v032_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_378d_t3s0i252_base_v033_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_378d_t5s0i252_base_v034_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_378d_t7s0i252_base_v035_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_378d_t9s0i252_base_v036_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_504d_t1s0i252_base_v037_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_504d_t3s0i252_base_v038_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_504d_t5s0i252_base_v039_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_504d_t7s0i252_base_v040_signal,
    f27icg_f27_ipp_capacity_growth_asset_growth_504d_t9s0i252_base_v041_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t1s0i252_base_v042_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t3s0i252_base_v043_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t5s0i252_base_v044_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t7s0i252_base_v045_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_5d_t9s0i252_base_v046_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t1s0i252_base_v047_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t3s0i252_base_v048_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t5s0i252_base_v049_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t7s0i252_base_v050_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_10d_t9s0i252_base_v051_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t1s0i252_base_v052_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t3s0i252_base_v053_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t5s0i252_base_v054_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t7s0i252_base_v055_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_21d_t9s0i252_base_v056_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t1s0i252_base_v057_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t3s0i252_base_v058_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t5s0i252_base_v059_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t7s0i252_base_v060_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_42d_t9s0i252_base_v061_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t1s0i252_base_v062_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t3s0i252_base_v063_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t5s0i252_base_v064_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t7s0i252_base_v065_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_63d_t9s0i252_base_v066_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t1s0i252_base_v067_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t3s0i252_base_v068_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t5s0i252_base_v069_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t7s0i252_base_v070_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_126d_t9s0i252_base_v071_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t1s0i252_base_v072_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t3s0i252_base_v073_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t5s0i252_base_v074_signal,
    f27icg_f27_ipp_capacity_growth_capacity_pulse_189d_t7s0i252_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_IPP_CAPACITY_GROWTH_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f27_ipp_capacity_growth_base_001_075_claude: {n_features} features pass")
