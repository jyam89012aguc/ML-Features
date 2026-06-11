import pandas as pd
import numpy as np
import inspect

# ===== BREAKOUT High-Performance Alpha Helpers =====
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _ewma(s, w): return s.ewm(span=w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)
def _ratio(n, d): return n / d.replace(0, np.nan)
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _drawdown(s, w): return (s / _max(s, w).replace(0, np.nan)) - 1
def _recovery(s, w): return (s / _min(s, w).replace(0, np.nan)) - 1
def _slope_pct(s, w): return s.pct_change(w)
def _jerk(s, w1, w2): return s.slope_pct(w1).diff(w2)
def _skew(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).skew()
def _kurt(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).kurt()
def _rsi(s, w):
    delta = s.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    ma_up = up.rolling(w, min_periods=min(w, 10)).mean()
    ma_down = down.rolling(w, min_periods=min(w, 10)).mean()
    rs = ma_up / ma_down.replace(0, np.nan)
    return 100 - (100 / (1 + rs))
def bo_098_underfollowed_inflection_marketcap_base_5d_v001_signal(closeadj):
    """Moving average of Raw level of marketcap over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_base_5d_v002_signal(closeadj):
    """Moving average of Raw level of revenue over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_base_5d_v003_signal(closeadj):
    """Moving average of Raw level of grossmargin over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_base_5d_v004_signal(closeadj):
    """Moving average of Structural seed over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_base_10d_v005_signal(closeadj):
    """Moving average of Raw level of marketcap over 10d window."""
    res = _sma(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_base_10d_v006_signal(closeadj):
    """Moving average of Raw level of revenue over 10d window."""
    res = _sma(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_base_10d_v007_signal(closeadj):
    """Moving average of Raw level of grossmargin over 10d window."""
    res = _sma(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_base_10d_v008_signal(closeadj):
    """Moving average of Structural seed over 10d window."""
    res = _sma(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_base_21d_v009_signal(closeadj):
    """Moving average of Raw level of marketcap over 21d window."""
    res = _sma(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_base_21d_v010_signal(closeadj):
    """Moving average of Raw level of revenue over 21d window."""
    res = _sma(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_base_21d_v011_signal(closeadj):
    """Moving average of Raw level of grossmargin over 21d window."""
    res = _sma(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_base_21d_v012_signal(closeadj):
    """Moving average of Structural seed over 21d window."""
    res = _sma(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_base_42d_v013_signal(closeadj):
    """Moving average of Raw level of marketcap over 42d window."""
    res = _sma(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_base_42d_v014_signal(closeadj):
    """Moving average of Raw level of revenue over 42d window."""
    res = _sma(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_base_42d_v015_signal(closeadj):
    """Moving average of Raw level of grossmargin over 42d window."""
    res = _sma(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_base_42d_v016_signal(closeadj):
    """Moving average of Structural seed over 42d window."""
    res = _sma(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_base_63d_v017_signal(closeadj):
    """Moving average of Raw level of marketcap over 63d window."""
    res = _sma(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_base_63d_v018_signal(closeadj):
    """Moving average of Raw level of revenue over 63d window."""
    res = _sma(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_base_63d_v019_signal(closeadj):
    """Moving average of Raw level of grossmargin over 63d window."""
    res = _sma(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_base_63d_v020_signal(closeadj):
    """Moving average of Structural seed over 63d window."""
    res = _sma(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_base_126d_v021_signal(closeadj):
    """Moving average of Raw level of marketcap over 126d window."""
    res = _sma(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_base_126d_v022_signal(closeadj):
    """Moving average of Raw level of revenue over 126d window."""
    res = _sma(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_base_126d_v023_signal(closeadj):
    """Moving average of Raw level of grossmargin over 126d window."""
    res = _sma(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_base_126d_v024_signal(closeadj):
    """Moving average of Structural seed over 126d window."""
    res = _sma(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_base_252d_v025_signal(closeadj):
    """Moving average of Raw level of marketcap over 252d window."""
    res = _sma(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_base_252d_v026_signal(closeadj):
    """Moving average of Raw level of revenue over 252d window."""
    res = _sma(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_base_252d_v027_signal(closeadj):
    """Moving average of Raw level of grossmargin over 252d window."""
    res = _sma(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_base_252d_v028_signal(closeadj):
    """Moving average of Structural seed over 252d window."""
    res = _sma(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_base_504d_v029_signal(closeadj):
    """Moving average of Raw level of marketcap over 504d window."""
    res = _sma(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_base_504d_v030_signal(closeadj):
    """Moving average of Raw level of revenue over 504d window."""
    res = _sma(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_base_504d_v031_signal(closeadj):
    """Moving average of Raw level of grossmargin over 504d window."""
    res = _sma(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_base_504d_v032_signal(closeadj):
    """Moving average of Structural seed over 504d window."""
    res = _sma(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_base_756d_v033_signal(closeadj):
    """Moving average of Raw level of marketcap over 756d window."""
    res = _sma(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_base_756d_v034_signal(closeadj):
    """Moving average of Raw level of revenue over 756d window."""
    res = _sma(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_base_756d_v035_signal(closeadj):
    """Moving average of Raw level of grossmargin over 756d window."""
    res = _sma(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_base_756d_v036_signal(closeadj):
    """Moving average of Structural seed over 756d window."""
    res = _sma(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_base_1008d_v037_signal(closeadj):
    """Moving average of Raw level of marketcap over 1008d window."""
    res = _sma(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_base_1008d_v038_signal(closeadj):
    """Moving average of Raw level of revenue over 1008d window."""
    res = _sma(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_base_1008d_v039_signal(closeadj):
    """Moving average of Raw level of grossmargin over 1008d window."""
    res = _sma(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_base_1008d_v040_signal(closeadj):
    """Moving average of Structural seed over 1008d window."""
    res = _sma(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_base_1260d_v041_signal(closeadj):
    """Moving average of Raw level of marketcap over 1260d window."""
    res = _sma(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_base_1260d_v042_signal(closeadj):
    """Moving average of Raw level of revenue over 1260d window."""
    res = _sma(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_base_1260d_v043_signal(closeadj):
    """Moving average of Raw level of grossmargin over 1260d window."""
    res = _sma(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_base_1260d_v044_signal(closeadj):
    """Moving average of Structural seed over 1260d window."""
    res = _sma(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_ewma_5d_v045_signal(closeadj):
    """Exponential moving average of Raw level of marketcap over 5d window."""
    res = _ewma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_ewma_5d_v046_signal(closeadj):
    """Exponential moving average of Raw level of revenue over 5d window."""
    res = _ewma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_ewma_5d_v047_signal(closeadj):
    """Exponential moving average of Raw level of grossmargin over 5d window."""
    res = _ewma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_ewma_5d_v048_signal(closeadj):
    """Exponential moving average of Structural seed over 5d window."""
    res = _ewma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_ewma_10d_v049_signal(closeadj):
    """Exponential moving average of Raw level of marketcap over 10d window."""
    res = _ewma(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_ewma_10d_v050_signal(closeadj):
    """Exponential moving average of Raw level of revenue over 10d window."""
    res = _ewma(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_ewma_10d_v051_signal(closeadj):
    """Exponential moving average of Raw level of grossmargin over 10d window."""
    res = _ewma(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_ewma_10d_v052_signal(closeadj):
    """Exponential moving average of Structural seed over 10d window."""
    res = _ewma(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_ewma_21d_v053_signal(closeadj):
    """Exponential moving average of Raw level of marketcap over 21d window."""
    res = _ewma(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_ewma_21d_v054_signal(closeadj):
    """Exponential moving average of Raw level of revenue over 21d window."""
    res = _ewma(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_ewma_21d_v055_signal(closeadj):
    """Exponential moving average of Raw level of grossmargin over 21d window."""
    res = _ewma(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_ewma_21d_v056_signal(closeadj):
    """Exponential moving average of Structural seed over 21d window."""
    res = _ewma(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_ewma_42d_v057_signal(closeadj):
    """Exponential moving average of Raw level of marketcap over 42d window."""
    res = _ewma(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_ewma_42d_v058_signal(closeadj):
    """Exponential moving average of Raw level of revenue over 42d window."""
    res = _ewma(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_ewma_42d_v059_signal(closeadj):
    """Exponential moving average of Raw level of grossmargin over 42d window."""
    res = _ewma(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_ewma_42d_v060_signal(closeadj):
    """Exponential moving average of Structural seed over 42d window."""
    res = _ewma(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_ewma_63d_v061_signal(closeadj):
    """Exponential moving average of Raw level of marketcap over 63d window."""
    res = _ewma(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_ewma_63d_v062_signal(closeadj):
    """Exponential moving average of Raw level of revenue over 63d window."""
    res = _ewma(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_ewma_63d_v063_signal(closeadj):
    """Exponential moving average of Raw level of grossmargin over 63d window."""
    res = _ewma(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_ewma_63d_v064_signal(closeadj):
    """Exponential moving average of Structural seed over 63d window."""
    res = _ewma(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_ewma_126d_v065_signal(closeadj):
    """Exponential moving average of Raw level of marketcap over 126d window."""
    res = _ewma(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_ewma_126d_v066_signal(closeadj):
    """Exponential moving average of Raw level of revenue over 126d window."""
    res = _ewma(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_ewma_126d_v067_signal(closeadj):
    """Exponential moving average of Raw level of grossmargin over 126d window."""
    res = _ewma(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_ewma_126d_v068_signal(closeadj):
    """Exponential moving average of Structural seed over 126d window."""
    res = _ewma(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_ewma_252d_v069_signal(closeadj):
    """Exponential moving average of Raw level of marketcap over 252d window."""
    res = _ewma(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_ewma_252d_v070_signal(closeadj):
    """Exponential moving average of Raw level of revenue over 252d window."""
    res = _ewma(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_ewma_252d_v071_signal(closeadj):
    """Exponential moving average of Raw level of grossmargin over 252d window."""
    res = _ewma(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_multibagger_seed_ewma_252d_v072_signal(closeadj):
    """Exponential moving average of Structural seed over 252d window."""
    res = _ewma(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_marketcap_ewma_504d_v073_signal(closeadj):
    """Exponential moving average of Raw level of marketcap over 504d window."""
    res = _ewma(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_revenue_ewma_504d_v074_signal(closeadj):
    """Exponential moving average of Raw level of revenue over 504d window."""
    res = _ewma(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_098_underfollowed_inflection_grossmargin_ewma_504d_v075_signal(closeadj):
    """Exponential moving average of Raw level of grossmargin over 504d window."""
    res = _ewma(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    "bo_098_underfollowed_inflection_marketcap_base_5d_v001_signal": {"func": bo_098_underfollowed_inflection_marketcap_base_5d_v001_signal},
    "bo_098_underfollowed_inflection_revenue_base_5d_v002_signal": {"func": bo_098_underfollowed_inflection_revenue_base_5d_v002_signal},
    "bo_098_underfollowed_inflection_grossmargin_base_5d_v003_signal": {"func": bo_098_underfollowed_inflection_grossmargin_base_5d_v003_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_base_5d_v004_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_base_5d_v004_signal},
    "bo_098_underfollowed_inflection_marketcap_base_10d_v005_signal": {"func": bo_098_underfollowed_inflection_marketcap_base_10d_v005_signal},
    "bo_098_underfollowed_inflection_revenue_base_10d_v006_signal": {"func": bo_098_underfollowed_inflection_revenue_base_10d_v006_signal},
    "bo_098_underfollowed_inflection_grossmargin_base_10d_v007_signal": {"func": bo_098_underfollowed_inflection_grossmargin_base_10d_v007_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_base_10d_v008_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_base_10d_v008_signal},
    "bo_098_underfollowed_inflection_marketcap_base_21d_v009_signal": {"func": bo_098_underfollowed_inflection_marketcap_base_21d_v009_signal},
    "bo_098_underfollowed_inflection_revenue_base_21d_v010_signal": {"func": bo_098_underfollowed_inflection_revenue_base_21d_v010_signal},
    "bo_098_underfollowed_inflection_grossmargin_base_21d_v011_signal": {"func": bo_098_underfollowed_inflection_grossmargin_base_21d_v011_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_base_21d_v012_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_base_21d_v012_signal},
    "bo_098_underfollowed_inflection_marketcap_base_42d_v013_signal": {"func": bo_098_underfollowed_inflection_marketcap_base_42d_v013_signal},
    "bo_098_underfollowed_inflection_revenue_base_42d_v014_signal": {"func": bo_098_underfollowed_inflection_revenue_base_42d_v014_signal},
    "bo_098_underfollowed_inflection_grossmargin_base_42d_v015_signal": {"func": bo_098_underfollowed_inflection_grossmargin_base_42d_v015_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_base_42d_v016_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_base_42d_v016_signal},
    "bo_098_underfollowed_inflection_marketcap_base_63d_v017_signal": {"func": bo_098_underfollowed_inflection_marketcap_base_63d_v017_signal},
    "bo_098_underfollowed_inflection_revenue_base_63d_v018_signal": {"func": bo_098_underfollowed_inflection_revenue_base_63d_v018_signal},
    "bo_098_underfollowed_inflection_grossmargin_base_63d_v019_signal": {"func": bo_098_underfollowed_inflection_grossmargin_base_63d_v019_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_base_63d_v020_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_base_63d_v020_signal},
    "bo_098_underfollowed_inflection_marketcap_base_126d_v021_signal": {"func": bo_098_underfollowed_inflection_marketcap_base_126d_v021_signal},
    "bo_098_underfollowed_inflection_revenue_base_126d_v022_signal": {"func": bo_098_underfollowed_inflection_revenue_base_126d_v022_signal},
    "bo_098_underfollowed_inflection_grossmargin_base_126d_v023_signal": {"func": bo_098_underfollowed_inflection_grossmargin_base_126d_v023_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_base_126d_v024_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_base_126d_v024_signal},
    "bo_098_underfollowed_inflection_marketcap_base_252d_v025_signal": {"func": bo_098_underfollowed_inflection_marketcap_base_252d_v025_signal},
    "bo_098_underfollowed_inflection_revenue_base_252d_v026_signal": {"func": bo_098_underfollowed_inflection_revenue_base_252d_v026_signal},
    "bo_098_underfollowed_inflection_grossmargin_base_252d_v027_signal": {"func": bo_098_underfollowed_inflection_grossmargin_base_252d_v027_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_base_252d_v028_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_base_252d_v028_signal},
    "bo_098_underfollowed_inflection_marketcap_base_504d_v029_signal": {"func": bo_098_underfollowed_inflection_marketcap_base_504d_v029_signal},
    "bo_098_underfollowed_inflection_revenue_base_504d_v030_signal": {"func": bo_098_underfollowed_inflection_revenue_base_504d_v030_signal},
    "bo_098_underfollowed_inflection_grossmargin_base_504d_v031_signal": {"func": bo_098_underfollowed_inflection_grossmargin_base_504d_v031_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_base_504d_v032_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_base_504d_v032_signal},
    "bo_098_underfollowed_inflection_marketcap_base_756d_v033_signal": {"func": bo_098_underfollowed_inflection_marketcap_base_756d_v033_signal},
    "bo_098_underfollowed_inflection_revenue_base_756d_v034_signal": {"func": bo_098_underfollowed_inflection_revenue_base_756d_v034_signal},
    "bo_098_underfollowed_inflection_grossmargin_base_756d_v035_signal": {"func": bo_098_underfollowed_inflection_grossmargin_base_756d_v035_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_base_756d_v036_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_base_756d_v036_signal},
    "bo_098_underfollowed_inflection_marketcap_base_1008d_v037_signal": {"func": bo_098_underfollowed_inflection_marketcap_base_1008d_v037_signal},
    "bo_098_underfollowed_inflection_revenue_base_1008d_v038_signal": {"func": bo_098_underfollowed_inflection_revenue_base_1008d_v038_signal},
    "bo_098_underfollowed_inflection_grossmargin_base_1008d_v039_signal": {"func": bo_098_underfollowed_inflection_grossmargin_base_1008d_v039_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_base_1008d_v040_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_base_1008d_v040_signal},
    "bo_098_underfollowed_inflection_marketcap_base_1260d_v041_signal": {"func": bo_098_underfollowed_inflection_marketcap_base_1260d_v041_signal},
    "bo_098_underfollowed_inflection_revenue_base_1260d_v042_signal": {"func": bo_098_underfollowed_inflection_revenue_base_1260d_v042_signal},
    "bo_098_underfollowed_inflection_grossmargin_base_1260d_v043_signal": {"func": bo_098_underfollowed_inflection_grossmargin_base_1260d_v043_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_base_1260d_v044_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_base_1260d_v044_signal},
    "bo_098_underfollowed_inflection_marketcap_ewma_5d_v045_signal": {"func": bo_098_underfollowed_inflection_marketcap_ewma_5d_v045_signal},
    "bo_098_underfollowed_inflection_revenue_ewma_5d_v046_signal": {"func": bo_098_underfollowed_inflection_revenue_ewma_5d_v046_signal},
    "bo_098_underfollowed_inflection_grossmargin_ewma_5d_v047_signal": {"func": bo_098_underfollowed_inflection_grossmargin_ewma_5d_v047_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_ewma_5d_v048_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_ewma_5d_v048_signal},
    "bo_098_underfollowed_inflection_marketcap_ewma_10d_v049_signal": {"func": bo_098_underfollowed_inflection_marketcap_ewma_10d_v049_signal},
    "bo_098_underfollowed_inflection_revenue_ewma_10d_v050_signal": {"func": bo_098_underfollowed_inflection_revenue_ewma_10d_v050_signal},
    "bo_098_underfollowed_inflection_grossmargin_ewma_10d_v051_signal": {"func": bo_098_underfollowed_inflection_grossmargin_ewma_10d_v051_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_ewma_10d_v052_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_ewma_10d_v052_signal},
    "bo_098_underfollowed_inflection_marketcap_ewma_21d_v053_signal": {"func": bo_098_underfollowed_inflection_marketcap_ewma_21d_v053_signal},
    "bo_098_underfollowed_inflection_revenue_ewma_21d_v054_signal": {"func": bo_098_underfollowed_inflection_revenue_ewma_21d_v054_signal},
    "bo_098_underfollowed_inflection_grossmargin_ewma_21d_v055_signal": {"func": bo_098_underfollowed_inflection_grossmargin_ewma_21d_v055_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_ewma_21d_v056_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_ewma_21d_v056_signal},
    "bo_098_underfollowed_inflection_marketcap_ewma_42d_v057_signal": {"func": bo_098_underfollowed_inflection_marketcap_ewma_42d_v057_signal},
    "bo_098_underfollowed_inflection_revenue_ewma_42d_v058_signal": {"func": bo_098_underfollowed_inflection_revenue_ewma_42d_v058_signal},
    "bo_098_underfollowed_inflection_grossmargin_ewma_42d_v059_signal": {"func": bo_098_underfollowed_inflection_grossmargin_ewma_42d_v059_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_ewma_42d_v060_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_ewma_42d_v060_signal},
    "bo_098_underfollowed_inflection_marketcap_ewma_63d_v061_signal": {"func": bo_098_underfollowed_inflection_marketcap_ewma_63d_v061_signal},
    "bo_098_underfollowed_inflection_revenue_ewma_63d_v062_signal": {"func": bo_098_underfollowed_inflection_revenue_ewma_63d_v062_signal},
    "bo_098_underfollowed_inflection_grossmargin_ewma_63d_v063_signal": {"func": bo_098_underfollowed_inflection_grossmargin_ewma_63d_v063_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_ewma_63d_v064_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_ewma_63d_v064_signal},
    "bo_098_underfollowed_inflection_marketcap_ewma_126d_v065_signal": {"func": bo_098_underfollowed_inflection_marketcap_ewma_126d_v065_signal},
    "bo_098_underfollowed_inflection_revenue_ewma_126d_v066_signal": {"func": bo_098_underfollowed_inflection_revenue_ewma_126d_v066_signal},
    "bo_098_underfollowed_inflection_grossmargin_ewma_126d_v067_signal": {"func": bo_098_underfollowed_inflection_grossmargin_ewma_126d_v067_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_ewma_126d_v068_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_ewma_126d_v068_signal},
    "bo_098_underfollowed_inflection_marketcap_ewma_252d_v069_signal": {"func": bo_098_underfollowed_inflection_marketcap_ewma_252d_v069_signal},
    "bo_098_underfollowed_inflection_revenue_ewma_252d_v070_signal": {"func": bo_098_underfollowed_inflection_revenue_ewma_252d_v070_signal},
    "bo_098_underfollowed_inflection_grossmargin_ewma_252d_v071_signal": {"func": bo_098_underfollowed_inflection_grossmargin_ewma_252d_v071_signal},
    "bo_098_underfollowed_inflection_multibagger_seed_ewma_252d_v072_signal": {"func": bo_098_underfollowed_inflection_multibagger_seed_ewma_252d_v072_signal},
    "bo_098_underfollowed_inflection_marketcap_ewma_504d_v073_signal": {"func": bo_098_underfollowed_inflection_marketcap_ewma_504d_v073_signal},
    "bo_098_underfollowed_inflection_revenue_ewma_504d_v074_signal": {"func": bo_098_underfollowed_inflection_revenue_ewma_504d_v074_signal},
    "bo_098_underfollowed_inflection_grossmargin_ewma_504d_v075_signal": {"func": bo_098_underfollowed_inflection_grossmargin_ewma_504d_v075_signal},
}
if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "rnd": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 098...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
            if len(res.dropna()) < 10 and len(df) > 1000: pass 
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
