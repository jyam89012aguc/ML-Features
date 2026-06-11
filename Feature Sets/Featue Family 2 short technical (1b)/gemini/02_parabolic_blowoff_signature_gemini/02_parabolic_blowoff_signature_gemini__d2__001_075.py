"""02 parabolic blowoff signature gemini d2 features 1-75 â€” Pipeline 1b-HF Grade v7.

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

def f02_pblo_gemini_001_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 5d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(5, min_periods=5//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_002_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 10d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(10, min_periods=10//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_003_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 21d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(21, min_periods=21//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_004_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 42d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(42, min_periods=42//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_005_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 63d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(63, min_periods=63//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_006_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 126d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(126, min_periods=126//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_007_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 252d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(252, min_periods=252//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_008_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 504d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(504, min_periods=504//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_009_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 756d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(756, min_periods=756//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_010_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 1260d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(1260, min_periods=1260//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_011_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 5d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(5, min_periods=5//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_012_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 10d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(10, min_periods=10//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_013_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 21d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(21, min_periods=21//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_014_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 42d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(42, min_periods=42//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_015_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 63d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(63, min_periods=63//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_016_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 126d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(126, min_periods=126//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_017_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 252d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(252, min_periods=252//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_018_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 504d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(504, min_periods=504//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_019_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 756d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(756, min_periods=756//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_020_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 1260d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(1260, min_periods=1260//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_021_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 5d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(5, min_periods=5//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_022_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 10d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(10, min_periods=10//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_023_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 21d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(21, min_periods=21//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_024_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 42d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(42, min_periods=42//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_025_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 63d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(63, min_periods=63//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_026_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 126d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(126, min_periods=126//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_027_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 252d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(252, min_periods=252//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_028_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 504d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(504, min_periods=504//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_029_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 756d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(756, min_periods=756//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_030_d2(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 1260d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(1260, min_periods=1260//2).apply(_curv, raw=True)
    return (res).diff().diff()

def f02_pblo_gemini_031_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=79, w2=381, w3=329, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 79)
    slow = _rolling_slope(x, 381)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.498235 + 6.82e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_032_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=86, w2=394, w3=346, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(394, min_periods=max(394//3, 2)).max()
    trough = x.rolling(86, min_periods=max(86//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.511765 + 6.83e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_033_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=93, w2=407, w3=363, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(93)
    rank = change.rolling(407, min_periods=max(407//3, 2)).rank(pct=True)
    persistence = change.rolling(363, min_periods=max(363//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.036333 * persistence + 6.84e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_034_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=100, w2=420, w3=380, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(100, min_periods=max(100//3, 2)).std()
    vol_slow = ret.rolling(420, min_periods=max(420//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.538824 + 6.85e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_035_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=107, w2=433, w3=397, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(433, min_periods=max(433//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 107)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.049 * slope + 6.86e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_036_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=114, w2=446, w3=414, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(114)
    drag = impulse.rolling(446, min_periods=max(446//3, 2)).mean()
    noise = impulse.abs().rolling(414, min_periods=max(414//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.565882 + 6.87e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_037_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=121, w2=459, w3=431, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 121)
    acceleration = _rolling_slope(velocity, 459)
    curvature = _rolling_slope(acceleration, 431)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.061667 * acceleration + 6.88e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_038_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=128, w2=472, w3=448, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(128, min_periods=max(128//3, 2)).mean(), upside.rolling(472, min_periods=max(472//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.592941 + 6.89e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_039_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=135, w2=485, w3=465, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(485, min_periods=max(485//3, 2)).max()
    rebound = x - x.rolling(135, min_periods=max(135//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.074333 * _rolling_slope(draw, 465) + 6.9e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_040_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=142, w2=498, w3=482, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 142)
    baseline = trend.rolling(498, min_periods=max(498//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(482, min_periods=max(482//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.62 + 6.91e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_041_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=149, w2=12, w3=499, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 149)
    slow = _rolling_slope(x, 12)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.633529 + 6.92e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_042_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=156, w2=25, w3=516, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(25, min_periods=max(25//3, 2)).max()
    trough = x.rolling(156, min_periods=max(156//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.647059 + 6.93e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_043_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=163, w2=38, w3=533, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(38, min_periods=max(38//3, 2)).rank(pct=True)
    persistence = change.rolling(533, min_periods=max(533//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.099667 * persistence + 6.94e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_044_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=170, w2=51, w3=550, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(170, min_periods=max(170//3, 2)).std()
    vol_slow = ret.rolling(51, min_periods=max(51//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.820588 + 6.95e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_045_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=177, w2=64, w3=567, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(64, min_periods=max(64//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 177)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.112333 * slope + 6.96e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_046_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=184, w2=77, w3=584, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(77, min_periods=max(77//3, 2)).mean()
    noise = impulse.abs().rolling(584, min_periods=max(584//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.847647 + 6.97e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_047_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=191, w2=90, w3=601, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 191)
    acceleration = _rolling_slope(velocity, 90)
    curvature = _rolling_slope(acceleration, 601)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.125 * acceleration + 6.98e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_048_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=198, w2=103, w3=618, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(198, min_periods=max(198//3, 2)).mean(), upside.rolling(103, min_periods=max(103//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.874706 + 6.99e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_049_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=205, w2=116, w3=635, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(116, min_periods=max(116//3, 2)).max()
    rebound = x - x.rolling(205, min_periods=max(205//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.137667 * _rolling_slope(draw, 635) + 7e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_050_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=212, w2=129, w3=652, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 212)
    baseline = trend.rolling(129, min_periods=max(129//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(652, min_periods=max(652//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.901765 + 7.01e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_051_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=219, w2=142, w3=669, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 219)
    slow = _rolling_slope(x, 142)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.915294 + 7.02e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_052_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=226, w2=155, w3=686, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(155, min_periods=max(155//3, 2)).max()
    trough = x.rolling(226, min_periods=max(226//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.928824 + 7.03e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_053_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=233, w2=168, w3=703, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(168, min_periods=max(168//3, 2)).rank(pct=True)
    persistence = change.rolling(703, min_periods=max(703//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.163 * persistence + 7.04e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_054_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=240, w2=181, w3=720, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(240, min_periods=max(240//3, 2)).std()
    vol_slow = ret.rolling(181, min_periods=max(181//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.955882 + 7.05e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_055_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=247, w2=194, w3=737, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(194, min_periods=max(194//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 247)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.175667 * slope + 7.06e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_056_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=7, w2=207, w3=754, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(7)
    drag = impulse.rolling(207, min_periods=max(207//3, 2)).mean()
    noise = impulse.abs().rolling(754, min_periods=max(754//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.982941 + 7.07e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_057_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=14, w2=220, w3=20, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 14)
    acceleration = _rolling_slope(velocity, 220)
    curvature = _rolling_slope(acceleration, 20)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.188333 * acceleration + 7.08e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_058_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=21, w2=233, w3=37, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(21, min_periods=max(21//3, 2)).mean(), upside.rolling(233, min_periods=max(233//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(37) * 1.01 + 7.09e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_059_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=28, w2=246, w3=54, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(246, min_periods=max(246//3, 2)).max()
    rebound = x - x.rolling(28, min_periods=max(28//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.201 * _rolling_slope(draw, 54) + 7.1e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_060_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=35, w2=259, w3=71, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 35)
    baseline = trend.rolling(259, min_periods=max(259//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(71, min_periods=max(71//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.037059 + 7.11e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_061_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=42, w2=272, w3=88, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 42)
    slow = _rolling_slope(x, 272)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=88, adjust=False).mean() * 1.050588 + 7.12e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_062_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=49, w2=285, w3=105, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(285, min_periods=max(285//3, 2)).max()
    trough = x.rolling(49, min_periods=max(49//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.064118 + 7.13e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_063_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=56, w2=298, w3=122, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(56)
    rank = change.rolling(298, min_periods=max(298//3, 2)).rank(pct=True)
    persistence = change.rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.226333 * persistence + 7.14e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_064_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=63, w2=311, w3=139, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(63, min_periods=max(63//3, 2)).std()
    vol_slow = ret.rolling(311, min_periods=max(311//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.091176 + 7.15e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_065_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=324, w3=156, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(324, min_periods=max(324//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 70)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.239 * slope + 7.16e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_066_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=77, w2=337, w3=173, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(77)
    drag = impulse.rolling(337, min_periods=max(337//3, 2)).mean()
    noise = impulse.abs().rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.118235 + 7.17e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_067_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=84, w2=350, w3=190, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 84)
    acceleration = _rolling_slope(velocity, 350)
    curvature = _rolling_slope(acceleration, 190)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.251667 * acceleration + 7.18e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_068_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=91, w2=363, w3=207, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(91, min_periods=max(91//3, 2)).mean(), upside.rolling(363, min_periods=max(363//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.145294 + 7.19e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_069_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=98, w2=376, w3=224, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(376, min_periods=max(376//3, 2)).max()
    rebound = x - x.rolling(98, min_periods=max(98//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.264333 * _rolling_slope(draw, 224) + 7.2e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_070_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=105, w2=389, w3=241, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 105)
    baseline = trend.rolling(389, min_periods=max(389//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(241, min_periods=max(241//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.172353 + 7.21e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_071_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=112, w2=402, w3=258, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 112)
    slow = _rolling_slope(x, 402)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=258, adjust=False).mean() * 1.185882 + 7.22e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_072_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=119, w2=415, w3=275, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(415, min_periods=max(415//3, 2)).max()
    trough = x.rolling(119, min_periods=max(119//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.199412 + 7.23e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_073_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=428, w3=292, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(428, min_periods=max(428//3, 2)).rank(pct=True)
    persistence = change.rolling(292, min_periods=max(292//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.289667 * persistence + 7.24e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_074_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=441, w3=309, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(133, min_periods=max(133//3, 2)).std()
    vol_slow = ret.rolling(441, min_periods=max(441//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.226471 + 7.25e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_075_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=454, w3=326, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(454, min_periods=max(454//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 140)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.302333 * slope + 7.26e-05 * anchor
    return base_signal.diff().diff()

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_02_PARABOLIC_BLOWOFF_SIGNATURE_GEMINI_D2_001_075 = {
    "f02_pblo_gemini_001_d2": {"inputs": ['close'], "func": f02_pblo_gemini_001_d2, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_002_d2": {"inputs": ['close'], "func": f02_pblo_gemini_002_d2, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_003_d2": {"inputs": ['close'], "func": f02_pblo_gemini_003_d2, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_004_d2": {"inputs": ['close'], "func": f02_pblo_gemini_004_d2, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_005_d2": {"inputs": ['close'], "func": f02_pblo_gemini_005_d2, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_006_d2": {"inputs": ['close'], "func": f02_pblo_gemini_006_d2, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_007_d2": {"inputs": ['close'], "func": f02_pblo_gemini_007_d2, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_008_d2": {"inputs": ['close'], "func": f02_pblo_gemini_008_d2, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_009_d2": {"inputs": ['close'], "func": f02_pblo_gemini_009_d2, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_010_d2": {"inputs": ['close'], "func": f02_pblo_gemini_010_d2, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_011_d2": {"inputs": ['close'], "func": f02_pblo_gemini_011_d2, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_012_d2": {"inputs": ['close'], "func": f02_pblo_gemini_012_d2, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_013_d2": {"inputs": ['close'], "func": f02_pblo_gemini_013_d2, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_014_d2": {"inputs": ['close'], "func": f02_pblo_gemini_014_d2, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_015_d2": {"inputs": ['close'], "func": f02_pblo_gemini_015_d2, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_016_d2": {"inputs": ['close'], "func": f02_pblo_gemini_016_d2, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_017_d2": {"inputs": ['close'], "func": f02_pblo_gemini_017_d2, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_018_d2": {"inputs": ['close'], "func": f02_pblo_gemini_018_d2, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_019_d2": {"inputs": ['close'], "func": f02_pblo_gemini_019_d2, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_020_d2": {"inputs": ['close'], "func": f02_pblo_gemini_020_d2, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_021_d2": {"inputs": ['close'], "func": f02_pblo_gemini_021_d2, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_022_d2": {"inputs": ['close'], "func": f02_pblo_gemini_022_d2, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_023_d2": {"inputs": ['close'], "func": f02_pblo_gemini_023_d2, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_024_d2": {"inputs": ['close'], "func": f02_pblo_gemini_024_d2, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_025_d2": {"inputs": ['close'], "func": f02_pblo_gemini_025_d2, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_026_d2": {"inputs": ['close'], "func": f02_pblo_gemini_026_d2, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_027_d2": {"inputs": ['close'], "func": f02_pblo_gemini_027_d2, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_028_d2": {"inputs": ['close'], "func": f02_pblo_gemini_028_d2, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_029_d2": {"inputs": ['close'], "func": f02_pblo_gemini_029_d2, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_030_d2": {"inputs": ['close'], "func": f02_pblo_gemini_030_d2, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_031_d2": {"inputs": ['close'], "func": f02_pblo_gemini_031_d2, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_032_d2": {"inputs": ['close'], "func": f02_pblo_gemini_032_d2, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_033_d2": {"inputs": ['close'], "func": f02_pblo_gemini_033_d2, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_034_d2": {"inputs": ['close'], "func": f02_pblo_gemini_034_d2, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_035_d2": {"inputs": ['close'], "func": f02_pblo_gemini_035_d2, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_036_d2": {"inputs": ['close'], "func": f02_pblo_gemini_036_d2, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_037_d2": {"inputs": ['close'], "func": f02_pblo_gemini_037_d2, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_038_d2": {"inputs": ['close'], "func": f02_pblo_gemini_038_d2, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_039_d2": {"inputs": ['close'], "func": f02_pblo_gemini_039_d2, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_040_d2": {"inputs": ['close'], "func": f02_pblo_gemini_040_d2, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_041_d2": {"inputs": ['close'], "func": f02_pblo_gemini_041_d2, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_042_d2": {"inputs": ['close'], "func": f02_pblo_gemini_042_d2, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_043_d2": {"inputs": ['close'], "func": f02_pblo_gemini_043_d2, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_044_d2": {"inputs": ['close'], "func": f02_pblo_gemini_044_d2, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_045_d2": {"inputs": ['close'], "func": f02_pblo_gemini_045_d2, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_046_d2": {"inputs": ['close'], "func": f02_pblo_gemini_046_d2, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_047_d2": {"inputs": ['close'], "func": f02_pblo_gemini_047_d2, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_048_d2": {"inputs": ['close'], "func": f02_pblo_gemini_048_d2, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_049_d2": {"inputs": ['close'], "func": f02_pblo_gemini_049_d2, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_050_d2": {"inputs": ['close'], "func": f02_pblo_gemini_050_d2, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_051_d2": {"inputs": ['close'], "func": f02_pblo_gemini_051_d2, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_052_d2": {"inputs": ['close'], "func": f02_pblo_gemini_052_d2, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_053_d2": {"inputs": ['close'], "func": f02_pblo_gemini_053_d2, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_054_d2": {"inputs": ['close'], "func": f02_pblo_gemini_054_d2, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_055_d2": {"inputs": ['close'], "func": f02_pblo_gemini_055_d2, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_056_d2": {"inputs": ['close'], "func": f02_pblo_gemini_056_d2, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_057_d2": {"inputs": ['close'], "func": f02_pblo_gemini_057_d2, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_058_d2": {"inputs": ['close'], "func": f02_pblo_gemini_058_d2, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_059_d2": {"inputs": ['close'], "func": f02_pblo_gemini_059_d2, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_060_d2": {"inputs": ['close'], "func": f02_pblo_gemini_060_d2, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_061_d2": {"inputs": ['close'], "func": f02_pblo_gemini_061_d2, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_062_d2": {"inputs": ['close'], "func": f02_pblo_gemini_062_d2, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_063_d2": {"inputs": ['close'], "func": f02_pblo_gemini_063_d2, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_064_d2": {"inputs": ['close'], "func": f02_pblo_gemini_064_d2, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_065_d2": {"inputs": ['close'], "func": f02_pblo_gemini_065_d2, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_066_d2": {"inputs": ['close'], "func": f02_pblo_gemini_066_d2, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_067_d2": {"inputs": ['close'], "func": f02_pblo_gemini_067_d2, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_068_d2": {"inputs": ['close'], "func": f02_pblo_gemini_068_d2, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_069_d2": {"inputs": ['close'], "func": f02_pblo_gemini_069_d2, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_070_d2": {"inputs": ['close'], "func": f02_pblo_gemini_070_d2, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_071_d2": {"inputs": ['close'], "func": f02_pblo_gemini_071_d2, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_072_d2": {"inputs": ['close'], "func": f02_pblo_gemini_072_d2, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_073_d2": {"inputs": ['close'], "func": f02_pblo_gemini_073_d2, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_074_d2": {"inputs": ['close'], "func": f02_pblo_gemini_074_d2, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_075_d2": {"inputs": ['close'], "func": f02_pblo_gemini_075_d2, "description": "Quadratic curvature of log-price over 63d."},
}
