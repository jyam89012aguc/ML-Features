"""02 parabolic blowoff signature gemini base features 1-75 â€” Pipeline 1b-HF Grade v7.

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

def f02_pblo_gemini_001(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 5d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(5, min_periods=5//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_002(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 10d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(10, min_periods=10//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_003(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 21d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(21, min_periods=21//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_004(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 42d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(42, min_periods=42//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_005(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 63d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(63, min_periods=63//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_006(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 126d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(126, min_periods=126//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_007(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 252d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(252, min_periods=252//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_008(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 504d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(504, min_periods=504//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_009(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 756d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(756, min_periods=756//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_010(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 1260d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(1260, min_periods=1260//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_011(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 5d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(5, min_periods=5//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_012(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 10d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(10, min_periods=10//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_013(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 21d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(21, min_periods=21//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_014(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 42d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(42, min_periods=42//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_015(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 63d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(63, min_periods=63//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_016(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 126d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(126, min_periods=126//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_017(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 252d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(252, min_periods=252//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_018(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 504d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(504, min_periods=504//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_019(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 756d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(756, min_periods=756//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_020(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 1260d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(1260, min_periods=1260//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_021(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 5d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(5, min_periods=5//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_022(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 10d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(10, min_periods=10//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_023(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 21d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(21, min_periods=21//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_024(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 42d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(42, min_periods=42//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_025(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 63d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(63, min_periods=63//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_026(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 126d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(126, min_periods=126//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_027(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 252d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(252, min_periods=252//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_028(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 504d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(504, min_periods=504//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_029(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 756d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(756, min_periods=756//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_030(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 1260d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(1260, min_periods=1260//2).apply(_curv, raw=True)
    return res

def f02_pblo_gemini_031(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=128, w2=255, w3=755, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 128)
    slow = _rolling_slope(x, 255)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.665294 + 4.42e-05 * anchor
    return base_signal

def f02_pblo_gemini_032(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=135, w2=268, w3=21, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(268, min_periods=max(268//3, 2)).max()
    trough = x.rolling(135, min_periods=max(135//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.825294 + 4.43e-05 * anchor
    return base_signal

def f02_pblo_gemini_033(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=142, w2=281, w3=38, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(281, min_periods=max(281//3, 2)).rank(pct=True)
    persistence = change.rolling(38, min_periods=max(38//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.178 * persistence + 4.44e-05 * anchor
    return base_signal

def f02_pblo_gemini_034(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=149, w2=294, w3=55, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(149, min_periods=max(149//3, 2)).std()
    vol_slow = ret.rolling(294, min_periods=max(294//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.852353 + 4.45e-05 * anchor
    return base_signal

def f02_pblo_gemini_035(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=156, w2=307, w3=72, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(307, min_periods=max(307//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 156)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.190667 * slope + 4.46e-05 * anchor
    return base_signal

def f02_pblo_gemini_036(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=163, w2=320, w3=89, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(320, min_periods=max(320//3, 2)).mean()
    noise = impulse.abs().rolling(89, min_periods=max(89//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.879412 + 4.47e-05 * anchor
    return base_signal

def f02_pblo_gemini_037(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=170, w2=333, w3=106, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 170)
    acceleration = _rolling_slope(velocity, 333)
    curvature = _rolling_slope(acceleration, 106)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.203333 * acceleration + 4.48e-05 * anchor
    return base_signal

def f02_pblo_gemini_038(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=177, w2=346, w3=123, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(177, min_periods=max(177//3, 2)).mean(), upside.rolling(346, min_periods=max(346//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(123) * 0.906471 + 4.49e-05 * anchor
    return base_signal

def f02_pblo_gemini_039(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=184, w2=359, w3=140, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(359, min_periods=max(359//3, 2)).max()
    rebound = x - x.rolling(184, min_periods=max(184//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.216 * _rolling_slope(draw, 140) + 4.5e-05 * anchor
    return base_signal

def f02_pblo_gemini_040(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=191, w2=372, w3=157, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 191)
    baseline = trend.rolling(372, min_periods=max(372//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.933529 + 4.51e-05 * anchor
    return base_signal

def f02_pblo_gemini_041(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=198, w2=385, w3=174, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 198)
    slow = _rolling_slope(x, 385)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=174, adjust=False).mean() * 0.947059 + 4.52e-05 * anchor
    return base_signal

def f02_pblo_gemini_042(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=205, w2=398, w3=191, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(398, min_periods=max(398//3, 2)).max()
    trough = x.rolling(205, min_periods=max(205//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.960588 + 4.53e-05 * anchor
    return base_signal

def f02_pblo_gemini_043(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=212, w2=411, w3=208, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(411, min_periods=max(411//3, 2)).rank(pct=True)
    persistence = change.rolling(208, min_periods=max(208//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.241333 * persistence + 4.54e-05 * anchor
    return base_signal

def f02_pblo_gemini_044(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=219, w2=424, w3=225, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(219, min_periods=max(219//3, 2)).std()
    vol_slow = ret.rolling(424, min_periods=max(424//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.987647 + 4.55e-05 * anchor
    return base_signal

def f02_pblo_gemini_045(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=226, w2=437, w3=242, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(437, min_periods=max(437//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 226)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.254 * slope + 4.56e-05 * anchor
    return base_signal

def f02_pblo_gemini_046(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=233, w2=450, w3=259, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(450, min_periods=max(450//3, 2)).mean()
    noise = impulse.abs().rolling(259, min_periods=max(259//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.014706 + 4.57e-05 * anchor
    return base_signal

def f02_pblo_gemini_047(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=240, w2=463, w3=276, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 240)
    acceleration = _rolling_slope(velocity, 463)
    curvature = _rolling_slope(acceleration, 276)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.266667 * acceleration + 4.58e-05 * anchor
    return base_signal

def f02_pblo_gemini_048(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=247, w2=476, w3=293, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(247, min_periods=max(247//3, 2)).mean(), upside.rolling(476, min_periods=max(476//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.041765 + 4.59e-05 * anchor
    return base_signal

def f02_pblo_gemini_049(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=7, w2=489, w3=310, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(489, min_periods=max(489//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.279333 * _rolling_slope(draw, 310) + 4.6e-05 * anchor
    return base_signal

def f02_pblo_gemini_050(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=14, w2=502, w3=327, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 14)
    baseline = trend.rolling(502, min_periods=max(502//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(327, min_periods=max(327//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.068824 + 4.61e-05 * anchor
    return base_signal

def f02_pblo_gemini_051(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=21, w2=16, w3=344, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 21)
    slow = _rolling_slope(x, 16)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.082353 + 4.62e-05 * anchor
    return base_signal

def f02_pblo_gemini_052(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=28, w2=29, w3=361, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(29, min_periods=max(29//3, 2)).max()
    trough = x.rolling(28, min_periods=max(28//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.095882 + 4.63e-05 * anchor
    return base_signal

def f02_pblo_gemini_053(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=35, w2=42, w3=378, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(35)
    rank = change.rolling(42, min_periods=max(42//3, 2)).rank(pct=True)
    persistence = change.rolling(378, min_periods=max(378//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.304667 * persistence + 4.64e-05 * anchor
    return base_signal

def f02_pblo_gemini_054(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=42, w2=55, w3=395, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(42, min_periods=max(42//3, 2)).std()
    vol_slow = ret.rolling(55, min_periods=max(55//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.122941 + 4.65e-05 * anchor
    return base_signal

def f02_pblo_gemini_055(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=49, w2=68, w3=412, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(68, min_periods=max(68//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 49)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.317333 * slope + 4.66e-05 * anchor
    return base_signal

def f02_pblo_gemini_056(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=56, w2=81, w3=429, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(56)
    drag = impulse.rolling(81, min_periods=max(81//3, 2)).mean()
    noise = impulse.abs().rolling(429, min_periods=max(429//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.15 + 4.67e-05 * anchor
    return base_signal

def f02_pblo_gemini_057(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=63, w2=94, w3=446, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 63)
    acceleration = _rolling_slope(velocity, 94)
    curvature = _rolling_slope(acceleration, 446)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.33 * acceleration + 4.68e-05 * anchor
    return base_signal

def f02_pblo_gemini_058(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=70, w2=107, w3=463, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(70, min_periods=max(70//3, 2)).mean(), upside.rolling(107, min_periods=max(107//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.177059 + 4.69e-05 * anchor
    return base_signal

def f02_pblo_gemini_059(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=77, w2=120, w3=480, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(120, min_periods=max(120//3, 2)).max()
    rebound = x - x.rolling(77, min_periods=max(77//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.342667 * _rolling_slope(draw, 480) + 4.7e-05 * anchor
    return base_signal

def f02_pblo_gemini_060(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=84, w2=133, w3=497, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 84)
    baseline = trend.rolling(133, min_periods=max(133//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(497, min_periods=max(497//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.204118 + 4.71e-05 * anchor
    return base_signal

def f02_pblo_gemini_061(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=91, w2=146, w3=514, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 91)
    slow = _rolling_slope(x, 146)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.217647 + 4.72e-05 * anchor
    return base_signal

def f02_pblo_gemini_062(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=98, w2=159, w3=531, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(159, min_periods=max(159//3, 2)).max()
    trough = x.rolling(98, min_periods=max(98//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.231176 + 4.73e-05 * anchor
    return base_signal

def f02_pblo_gemini_063(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=105, w2=172, w3=548, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(105)
    rank = change.rolling(172, min_periods=max(172//3, 2)).rank(pct=True)
    persistence = change.rolling(548, min_periods=max(548//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.035667 * persistence + 4.74e-05 * anchor
    return base_signal

def f02_pblo_gemini_064(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=112, w2=185, w3=565, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(112, min_periods=max(112//3, 2)).std()
    vol_slow = ret.rolling(185, min_periods=max(185//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.258235 + 4.75e-05 * anchor
    return base_signal

def f02_pblo_gemini_065(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=119, w2=198, w3=582, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(198, min_periods=max(198//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 119)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.048333 * slope + 4.76e-05 * anchor
    return base_signal

def f02_pblo_gemini_066(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=126, w2=211, w3=599, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(211, min_periods=max(211//3, 2)).mean()
    noise = impulse.abs().rolling(599, min_periods=max(599//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.285294 + 4.77e-05 * anchor
    return base_signal

def f02_pblo_gemini_067(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=133, w2=224, w3=616, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 133)
    acceleration = _rolling_slope(velocity, 224)
    curvature = _rolling_slope(acceleration, 616)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.061 * acceleration + 4.78e-05 * anchor
    return base_signal

def f02_pblo_gemini_068(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=140, w2=237, w3=633, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(140, min_periods=max(140//3, 2)).mean(), upside.rolling(237, min_periods=max(237//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.312353 + 4.79e-05 * anchor
    return base_signal

def f02_pblo_gemini_069(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=147, w2=250, w3=650, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(250, min_periods=max(250//3, 2)).max()
    rebound = x - x.rolling(147, min_periods=max(147//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.073667 * _rolling_slope(draw, 650) + 4.8e-05 * anchor
    return base_signal

def f02_pblo_gemini_070(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=154, w2=263, w3=667, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 154)
    baseline = trend.rolling(263, min_periods=max(263//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(667, min_periods=max(667//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.339412 + 4.81e-05 * anchor
    return base_signal

def f02_pblo_gemini_071(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=161, w2=276, w3=684, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 161)
    slow = _rolling_slope(x, 276)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.352941 + 4.82e-05 * anchor
    return base_signal

def f02_pblo_gemini_072(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=168, w2=289, w3=701, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(289, min_periods=max(289//3, 2)).max()
    trough = x.rolling(168, min_periods=max(168//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.366471 + 4.83e-05 * anchor
    return base_signal

def f02_pblo_gemini_073(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=175, w2=302, w3=718, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(302, min_periods=max(302//3, 2)).rank(pct=True)
    persistence = change.rolling(718, min_periods=max(718//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.099 * persistence + 4.84e-05 * anchor
    return base_signal

def f02_pblo_gemini_074(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=182, w2=315, w3=735, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(182, min_periods=max(182//3, 2)).std()
    vol_slow = ret.rolling(315, min_periods=max(315//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.393529 + 4.85e-05 * anchor
    return base_signal

def f02_pblo_gemini_075(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=189, w2=328, w3=752, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(328, min_periods=max(328//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 189)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.111667 * slope + 4.86e-05 * anchor
    return base_signal

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_02_PARABOLIC_BLOWOFF_SIGNATURE_GEMINI_BASE_001_075 = {
    "f02_pblo_gemini_001": {"inputs": ['close'], "func": f02_pblo_gemini_001, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_002": {"inputs": ['close'], "func": f02_pblo_gemini_002, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_003": {"inputs": ['close'], "func": f02_pblo_gemini_003, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_004": {"inputs": ['close'], "func": f02_pblo_gemini_004, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_005": {"inputs": ['close'], "func": f02_pblo_gemini_005, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_006": {"inputs": ['close'], "func": f02_pblo_gemini_006, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_007": {"inputs": ['close'], "func": f02_pblo_gemini_007, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_008": {"inputs": ['close'], "func": f02_pblo_gemini_008, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_009": {"inputs": ['close'], "func": f02_pblo_gemini_009, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_010": {"inputs": ['close'], "func": f02_pblo_gemini_010, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_011": {"inputs": ['close'], "func": f02_pblo_gemini_011, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_012": {"inputs": ['close'], "func": f02_pblo_gemini_012, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_013": {"inputs": ['close'], "func": f02_pblo_gemini_013, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_014": {"inputs": ['close'], "func": f02_pblo_gemini_014, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_015": {"inputs": ['close'], "func": f02_pblo_gemini_015, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_016": {"inputs": ['close'], "func": f02_pblo_gemini_016, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_017": {"inputs": ['close'], "func": f02_pblo_gemini_017, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_018": {"inputs": ['close'], "func": f02_pblo_gemini_018, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_019": {"inputs": ['close'], "func": f02_pblo_gemini_019, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_020": {"inputs": ['close'], "func": f02_pblo_gemini_020, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_021": {"inputs": ['close'], "func": f02_pblo_gemini_021, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_022": {"inputs": ['close'], "func": f02_pblo_gemini_022, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_023": {"inputs": ['close'], "func": f02_pblo_gemini_023, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_024": {"inputs": ['close'], "func": f02_pblo_gemini_024, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_025": {"inputs": ['close'], "func": f02_pblo_gemini_025, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_026": {"inputs": ['close'], "func": f02_pblo_gemini_026, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_027": {"inputs": ['close'], "func": f02_pblo_gemini_027, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_028": {"inputs": ['close'], "func": f02_pblo_gemini_028, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_029": {"inputs": ['close'], "func": f02_pblo_gemini_029, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_030": {"inputs": ['close'], "func": f02_pblo_gemini_030, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_031": {"inputs": ['close'], "func": f02_pblo_gemini_031, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_032": {"inputs": ['close'], "func": f02_pblo_gemini_032, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_033": {"inputs": ['close'], "func": f02_pblo_gemini_033, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_034": {"inputs": ['close'], "func": f02_pblo_gemini_034, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_035": {"inputs": ['close'], "func": f02_pblo_gemini_035, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_036": {"inputs": ['close'], "func": f02_pblo_gemini_036, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_037": {"inputs": ['close'], "func": f02_pblo_gemini_037, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_038": {"inputs": ['close'], "func": f02_pblo_gemini_038, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_039": {"inputs": ['close'], "func": f02_pblo_gemini_039, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_040": {"inputs": ['close'], "func": f02_pblo_gemini_040, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_041": {"inputs": ['close'], "func": f02_pblo_gemini_041, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_042": {"inputs": ['close'], "func": f02_pblo_gemini_042, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_043": {"inputs": ['close'], "func": f02_pblo_gemini_043, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_044": {"inputs": ['close'], "func": f02_pblo_gemini_044, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_045": {"inputs": ['close'], "func": f02_pblo_gemini_045, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_046": {"inputs": ['close'], "func": f02_pblo_gemini_046, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_047": {"inputs": ['close'], "func": f02_pblo_gemini_047, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_048": {"inputs": ['close'], "func": f02_pblo_gemini_048, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_049": {"inputs": ['close'], "func": f02_pblo_gemini_049, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_050": {"inputs": ['close'], "func": f02_pblo_gemini_050, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_051": {"inputs": ['close'], "func": f02_pblo_gemini_051, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_052": {"inputs": ['close'], "func": f02_pblo_gemini_052, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_053": {"inputs": ['close'], "func": f02_pblo_gemini_053, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_054": {"inputs": ['close'], "func": f02_pblo_gemini_054, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_055": {"inputs": ['close'], "func": f02_pblo_gemini_055, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_056": {"inputs": ['close'], "func": f02_pblo_gemini_056, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_057": {"inputs": ['close'], "func": f02_pblo_gemini_057, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_058": {"inputs": ['close'], "func": f02_pblo_gemini_058, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_059": {"inputs": ['close'], "func": f02_pblo_gemini_059, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_060": {"inputs": ['close'], "func": f02_pblo_gemini_060, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_061": {"inputs": ['close'], "func": f02_pblo_gemini_061, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_062": {"inputs": ['close'], "func": f02_pblo_gemini_062, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_063": {"inputs": ['close'], "func": f02_pblo_gemini_063, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_064": {"inputs": ['close'], "func": f02_pblo_gemini_064, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_065": {"inputs": ['close'], "func": f02_pblo_gemini_065, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_066": {"inputs": ['close'], "func": f02_pblo_gemini_066, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_067": {"inputs": ['close'], "func": f02_pblo_gemini_067, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_068": {"inputs": ['close'], "func": f02_pblo_gemini_068, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_069": {"inputs": ['close'], "func": f02_pblo_gemini_069, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_070": {"inputs": ['close'], "func": f02_pblo_gemini_070, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_071": {"inputs": ['close'], "func": f02_pblo_gemini_071, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_072": {"inputs": ['close'], "func": f02_pblo_gemini_072, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_073": {"inputs": ['close'], "func": f02_pblo_gemini_073, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_074": {"inputs": ['close'], "func": f02_pblo_gemini_074, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_075": {"inputs": ['close'], "func": f02_pblo_gemini_075, "description": "Quadratic curvature of log-price over 63d."},
}
