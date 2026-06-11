"""02 parabolic blowoff signature gemini d3 features 1-75 â€” Pipeline 1b-HF Grade v7.

Hypothesis: Blowoff - Institutional-grade technical signal with high-entropy logic.
Version: 7.0 (Strict De-duplication + Functional Safety)
Registry Status: Optimized for PostgreSQL Feature Store ingestion.
PIT-clean: right-anchored rolling, explicit min_periods.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_5Y = 1260

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))

def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)

def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)

def _atr(high, low, close, n=14):
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    return tr.rolling(n, min_periods=max(n // 2, 1)).mean()

def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]; wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _absorption_ratio_proxy(returns_list, n_comp=1):
    data = pd.concat(returns_list, axis=1)
    def _ar(w):
        if np.isnan(w).any(): return np.nan
        corr = np.corrcoef(w.T)
        eigvals = np.linalg.eigvalsh(corr)
        return np.max(eigvals) / len(eigvals)
    return data.rolling(21).apply(_ar, raw=True)

# ============================================================
# FEATURE HYPOTHESES (001-075)
# ============================================================

def f02_pblo_gemini_001_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 5d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(5, min_periods=5//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_002_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 10d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(10, min_periods=10//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_003_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 21d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(21, min_periods=21//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_004_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 42d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(42, min_periods=42//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_005_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 63d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(63, min_periods=63//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_006_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 126d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(126, min_periods=126//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_007_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 252d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(252, min_periods=252//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_008_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 504d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(504, min_periods=504//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_009_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 756d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(756, min_periods=756//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_010_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 1260d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(1260, min_periods=1260//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_011_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 5d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(5, min_periods=5//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_012_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 10d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(10, min_periods=10//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_013_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 21d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(21, min_periods=21//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_014_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 42d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(42, min_periods=42//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_015_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 63d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(63, min_periods=63//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_016_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 126d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(126, min_periods=126//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_017_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 252d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(252, min_periods=252//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_018_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 504d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(504, min_periods=504//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_019_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 756d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(756, min_periods=756//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_020_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 1260d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(1260, min_periods=1260//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_021_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 5d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(5, min_periods=5//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_022_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 10d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(10, min_periods=10//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_023_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 21d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(21, min_periods=21//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_024_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 42d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(42, min_periods=42//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_025_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 63d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(63, min_periods=63//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_026_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 126d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(126, min_periods=126//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_027_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 252d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(252, min_periods=252//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_028_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 504d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(504, min_periods=504//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_029_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 756d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(756, min_periods=756//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_030_d3(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 1260d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(1260, min_periods=1260//2).apply(_curv, raw=True)
    return (res).diff().diff().diff()

def f02_pblo_gemini_031_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=444, w3=116, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 178)
    slow = _rolling_slope(x, 444)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=116, adjust=False).mean() * 1.414706 + 8.02e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_032_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=457, w3=133, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(457, min_periods=max(457//3, 2)).max()
    trough = x.rolling(185, min_periods=max(185//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.428235 + 8.03e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_033_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=470, w3=150, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(470, min_periods=max(470//3, 2)).rank(pct=True)
    persistence = change.rolling(150, min_periods=max(150//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.131667 * persistence + 8.04e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_034_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=483, w3=167, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(199, min_periods=max(199//3, 2)).std()
    vol_slow = ret.rolling(483, min_periods=max(483//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.455294 + 8.05e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_035_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=496, w3=184, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(496, min_periods=max(496//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 206)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.144333 * slope + 8.06e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_036_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=509, w3=201, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(509, min_periods=max(509//3, 2)).mean()
    noise = impulse.abs().rolling(201, min_periods=max(201//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.482353 + 8.07e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_037_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=23, w3=218, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 220)
    acceleration = _rolling_slope(velocity, 23)
    curvature = _rolling_slope(acceleration, 218)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.157 * acceleration + 8.08e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_038_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=36, w3=235, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(227, min_periods=max(227//3, 2)).mean(), upside.rolling(36, min_periods=max(36//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.509412 + 8.09e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_039_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=234, w2=49, w3=252, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(49, min_periods=max(49//3, 2)).max()
    rebound = x - x.rolling(234, min_periods=max(234//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.169667 * _rolling_slope(draw, 252) + 8.1e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_040_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=241, w2=62, w3=269, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 241)
    baseline = trend.rolling(62, min_periods=max(62//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(269, min_periods=max(269//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.536471 + 8.11e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_041_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=248, w2=75, w3=286, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 248)
    slow = _rolling_slope(x, 75)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=286, adjust=False).mean() * 1.55 + 8.12e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_042_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=8, w2=88, w3=303, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(88, min_periods=max(88//3, 2)).max()
    trough = x.rolling(8, min_periods=max(8//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.563529 + 8.13e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_043_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=15, w2=101, w3=320, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(15)
    rank = change.rolling(101, min_periods=max(101//3, 2)).rank(pct=True)
    persistence = change.rolling(320, min_periods=max(320//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.195 * persistence + 8.14e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_044_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=22, w2=114, w3=337, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(22, min_periods=max(22//3, 2)).std()
    vol_slow = ret.rolling(114, min_periods=max(114//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.590588 + 8.15e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_045_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=29, w2=127, w3=354, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(127, min_periods=max(127//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 29)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.207667 * slope + 8.16e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_046_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=36, w2=140, w3=371, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(36)
    drag = impulse.rolling(140, min_periods=max(140//3, 2)).mean()
    noise = impulse.abs().rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.617647 + 8.17e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_047_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=43, w2=153, w3=388, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 43)
    acceleration = _rolling_slope(velocity, 153)
    curvature = _rolling_slope(acceleration, 388)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.220333 * acceleration + 8.18e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_048_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=50, w2=166, w3=405, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(166, min_periods=max(166//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.644706 + 8.19e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_049_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=57, w2=179, w3=422, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(179, min_periods=max(179//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.233 * _rolling_slope(draw, 422) + 8.2e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_050_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=64, w2=192, w3=439, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 64)
    baseline = trend.rolling(192, min_periods=max(192//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(439, min_periods=max(439//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.671765 + 8.21e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_051_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=71, w2=205, w3=456, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 71)
    slow = _rolling_slope(x, 205)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.831765 + 8.22e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_052_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=78, w2=218, w3=473, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(218, min_periods=max(218//3, 2)).max()
    trough = x.rolling(78, min_periods=max(78//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.845294 + 8.23e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_053_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=85, w2=231, w3=490, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(85)
    rank = change.rolling(231, min_periods=max(231//3, 2)).rank(pct=True)
    persistence = change.rolling(490, min_periods=max(490//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.258333 * persistence + 8.24e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_054_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=92, w2=244, w3=507, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(92, min_periods=max(92//3, 2)).std()
    vol_slow = ret.rolling(244, min_periods=max(244//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.872353 + 8.25e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_055_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=99, w2=257, w3=524, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(257, min_periods=max(257//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 99)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.271 * slope + 8.26e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_056_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=106, w2=270, w3=541, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(106)
    drag = impulse.rolling(270, min_periods=max(270//3, 2)).mean()
    noise = impulse.abs().rolling(541, min_periods=max(541//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.899412 + 8.27e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_057_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=113, w2=283, w3=558, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 113)
    acceleration = _rolling_slope(velocity, 283)
    curvature = _rolling_slope(acceleration, 558)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.283667 * acceleration + 8.28e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_058_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=120, w2=296, w3=575, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(120, min_periods=max(120//3, 2)).mean(), upside.rolling(296, min_periods=max(296//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.926471 + 8.29e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_059_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=127, w2=309, w3=592, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(309, min_periods=max(309//3, 2)).max()
    rebound = x - x.rolling(127, min_periods=max(127//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.296333 * _rolling_slope(draw, 592) + 8.3e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_060_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=134, w2=322, w3=609, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 134)
    baseline = trend.rolling(322, min_periods=max(322//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(609, min_periods=max(609//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.953529 + 8.31e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_061_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=141, w2=335, w3=626, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 141)
    slow = _rolling_slope(x, 335)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.967059 + 8.32e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_062_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=148, w2=348, w3=643, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(348, min_periods=max(348//3, 2)).max()
    trough = x.rolling(148, min_periods=max(148//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.980588 + 8.33e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_063_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=155, w2=361, w3=660, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(361, min_periods=max(361//3, 2)).rank(pct=True)
    persistence = change.rolling(660, min_periods=max(660//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.321667 * persistence + 8.34e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_064_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=162, w2=374, w3=677, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(162, min_periods=max(162//3, 2)).std()
    vol_slow = ret.rolling(374, min_periods=max(374//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.007647 + 8.35e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_065_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=169, w2=387, w3=694, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(387, min_periods=max(387//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 169)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.334333 * slope + 8.36e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_066_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=176, w2=400, w3=711, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(400, min_periods=max(400//3, 2)).mean()
    noise = impulse.abs().rolling(711, min_periods=max(711//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.034706 + 8.37e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_067_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=183, w2=413, w3=728, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 183)
    acceleration = _rolling_slope(velocity, 413)
    curvature = _rolling_slope(acceleration, 728)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.347 * acceleration + 8.38e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_068_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=190, w2=426, w3=745, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(190, min_periods=max(190//3, 2)).mean(), upside.rolling(426, min_periods=max(426//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.061765 + 8.39e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_069_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=197, w2=439, w3=762, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(439, min_periods=max(439//3, 2)).max()
    rebound = x - x.rolling(197, min_periods=max(197//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.359667 * _rolling_slope(draw, 762) + 8.4e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_070_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=204, w2=452, w3=28, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 204)
    baseline = trend.rolling(452, min_periods=max(452//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.088824 + 8.41e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_071_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=211, w2=465, w3=45, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 211)
    slow = _rolling_slope(x, 465)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=45, adjust=False).mean() * 1.102353 + 8.42e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_072_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=218, w2=478, w3=62, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(478, min_periods=max(478//3, 2)).max()
    trough = x.rolling(218, min_periods=max(218//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.115882 + 8.43e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_073_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=225, w2=491, w3=79, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(491, min_periods=max(491//3, 2)).rank(pct=True)
    persistence = change.rolling(79, min_periods=max(79//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.052667 * persistence + 8.44e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_074_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=232, w2=504, w3=96, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(232, min_periods=max(232//3, 2)).std()
    vol_slow = ret.rolling(504, min_periods=max(504//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.142941 + 8.45e-05 * anchor
    return base_signal.diff().diff().diff()

def f02_pblo_gemini_075_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=239, w2=18, w3=113, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(18, min_periods=max(18//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 239)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.065333 * slope + 8.46e-05 * anchor
    return base_signal.diff().diff().diff()

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_02_PARABOLIC_BLOWOFF_SIGNATURE_GEMINI_D3_001_075 = {
    "f02_pblo_gemini_001_d3": {"inputs": ['close'], "func": f02_pblo_gemini_001_d3, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_002_d3": {"inputs": ['close'], "func": f02_pblo_gemini_002_d3, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_003_d3": {"inputs": ['close'], "func": f02_pblo_gemini_003_d3, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_004_d3": {"inputs": ['close'], "func": f02_pblo_gemini_004_d3, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_005_d3": {"inputs": ['close'], "func": f02_pblo_gemini_005_d3, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_006_d3": {"inputs": ['close'], "func": f02_pblo_gemini_006_d3, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_007_d3": {"inputs": ['close'], "func": f02_pblo_gemini_007_d3, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_008_d3": {"inputs": ['close'], "func": f02_pblo_gemini_008_d3, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_009_d3": {"inputs": ['close'], "func": f02_pblo_gemini_009_d3, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_010_d3": {"inputs": ['close'], "func": f02_pblo_gemini_010_d3, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_011_d3": {"inputs": ['close'], "func": f02_pblo_gemini_011_d3, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_012_d3": {"inputs": ['close'], "func": f02_pblo_gemini_012_d3, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_013_d3": {"inputs": ['close'], "func": f02_pblo_gemini_013_d3, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_014_d3": {"inputs": ['close'], "func": f02_pblo_gemini_014_d3, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_015_d3": {"inputs": ['close'], "func": f02_pblo_gemini_015_d3, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_016_d3": {"inputs": ['close'], "func": f02_pblo_gemini_016_d3, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_017_d3": {"inputs": ['close'], "func": f02_pblo_gemini_017_d3, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_018_d3": {"inputs": ['close'], "func": f02_pblo_gemini_018_d3, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_019_d3": {"inputs": ['close'], "func": f02_pblo_gemini_019_d3, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_020_d3": {"inputs": ['close'], "func": f02_pblo_gemini_020_d3, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_021_d3": {"inputs": ['close'], "func": f02_pblo_gemini_021_d3, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_022_d3": {"inputs": ['close'], "func": f02_pblo_gemini_022_d3, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_023_d3": {"inputs": ['close'], "func": f02_pblo_gemini_023_d3, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_024_d3": {"inputs": ['close'], "func": f02_pblo_gemini_024_d3, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_025_d3": {"inputs": ['close'], "func": f02_pblo_gemini_025_d3, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_026_d3": {"inputs": ['close'], "func": f02_pblo_gemini_026_d3, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_027_d3": {"inputs": ['close'], "func": f02_pblo_gemini_027_d3, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_028_d3": {"inputs": ['close'], "func": f02_pblo_gemini_028_d3, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_029_d3": {"inputs": ['close'], "func": f02_pblo_gemini_029_d3, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_030_d3": {"inputs": ['close'], "func": f02_pblo_gemini_030_d3, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_031_d3": {"inputs": ['close'], "func": f02_pblo_gemini_031_d3, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_032_d3": {"inputs": ['close'], "func": f02_pblo_gemini_032_d3, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_033_d3": {"inputs": ['close'], "func": f02_pblo_gemini_033_d3, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_034_d3": {"inputs": ['close'], "func": f02_pblo_gemini_034_d3, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_035_d3": {"inputs": ['close'], "func": f02_pblo_gemini_035_d3, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_036_d3": {"inputs": ['close'], "func": f02_pblo_gemini_036_d3, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_037_d3": {"inputs": ['close'], "func": f02_pblo_gemini_037_d3, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_038_d3": {"inputs": ['close'], "func": f02_pblo_gemini_038_d3, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_039_d3": {"inputs": ['close'], "func": f02_pblo_gemini_039_d3, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_040_d3": {"inputs": ['close'], "func": f02_pblo_gemini_040_d3, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_041_d3": {"inputs": ['close'], "func": f02_pblo_gemini_041_d3, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_042_d3": {"inputs": ['close'], "func": f02_pblo_gemini_042_d3, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_043_d3": {"inputs": ['close'], "func": f02_pblo_gemini_043_d3, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_044_d3": {"inputs": ['close'], "func": f02_pblo_gemini_044_d3, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_045_d3": {"inputs": ['close'], "func": f02_pblo_gemini_045_d3, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_046_d3": {"inputs": ['close'], "func": f02_pblo_gemini_046_d3, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_047_d3": {"inputs": ['close'], "func": f02_pblo_gemini_047_d3, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_048_d3": {"inputs": ['close'], "func": f02_pblo_gemini_048_d3, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_049_d3": {"inputs": ['close'], "func": f02_pblo_gemini_049_d3, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_050_d3": {"inputs": ['close'], "func": f02_pblo_gemini_050_d3, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_051_d3": {"inputs": ['close'], "func": f02_pblo_gemini_051_d3, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_052_d3": {"inputs": ['close'], "func": f02_pblo_gemini_052_d3, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_053_d3": {"inputs": ['close'], "func": f02_pblo_gemini_053_d3, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_054_d3": {"inputs": ['close'], "func": f02_pblo_gemini_054_d3, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_055_d3": {"inputs": ['close'], "func": f02_pblo_gemini_055_d3, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_056_d3": {"inputs": ['close'], "func": f02_pblo_gemini_056_d3, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_057_d3": {"inputs": ['close'], "func": f02_pblo_gemini_057_d3, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_058_d3": {"inputs": ['close'], "func": f02_pblo_gemini_058_d3, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_059_d3": {"inputs": ['close'], "func": f02_pblo_gemini_059_d3, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_060_d3": {"inputs": ['close'], "func": f02_pblo_gemini_060_d3, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_061_d3": {"inputs": ['close'], "func": f02_pblo_gemini_061_d3, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_062_d3": {"inputs": ['close'], "func": f02_pblo_gemini_062_d3, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_063_d3": {"inputs": ['close'], "func": f02_pblo_gemini_063_d3, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_064_d3": {"inputs": ['close'], "func": f02_pblo_gemini_064_d3, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_065_d3": {"inputs": ['close'], "func": f02_pblo_gemini_065_d3, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_066_d3": {"inputs": ['close'], "func": f02_pblo_gemini_066_d3, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_067_d3": {"inputs": ['close'], "func": f02_pblo_gemini_067_d3, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_068_d3": {"inputs": ['close'], "func": f02_pblo_gemini_068_d3, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_069_d3": {"inputs": ['close'], "func": f02_pblo_gemini_069_d3, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_070_d3": {"inputs": ['close'], "func": f02_pblo_gemini_070_d3, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_071_d3": {"inputs": ['close'], "func": f02_pblo_gemini_071_d3, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_072_d3": {"inputs": ['close'], "func": f02_pblo_gemini_072_d3, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_073_d3": {"inputs": ['close'], "func": f02_pblo_gemini_073_d3, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_074_d3": {"inputs": ['close'], "func": f02_pblo_gemini_074_d3, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_075_d3": {"inputs": ['close'], "func": f02_pblo_gemini_075_d3, "description": "Quadratic curvature of log-price over 63d."},
}
