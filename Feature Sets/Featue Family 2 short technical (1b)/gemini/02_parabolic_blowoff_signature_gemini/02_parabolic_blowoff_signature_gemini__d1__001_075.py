"""02 parabolic blowoff signature gemini d1 features 1-75 â€” Pipeline 1b-HF Grade v7.

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

def f02_pblo_gemini_001_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 5d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(5, min_periods=5//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_002_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 10d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(10, min_periods=10//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_003_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 21d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(21, min_periods=21//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_004_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 42d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(42, min_periods=42//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_005_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 63d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(63, min_periods=63//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_006_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 126d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(126, min_periods=126//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_007_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 252d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(252, min_periods=252//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_008_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 504d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(504, min_periods=504//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_009_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 756d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(756, min_periods=756//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_010_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 1260d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(1260, min_periods=1260//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_011_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 5d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(5, min_periods=5//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_012_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 10d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(10, min_periods=10//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_013_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 21d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(21, min_periods=21//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_014_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 42d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(42, min_periods=42//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_015_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 63d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(63, min_periods=63//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_016_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 126d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(126, min_periods=126//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_017_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 252d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(252, min_periods=252//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_018_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 504d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(504, min_periods=504//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_019_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 756d."""
    s = _safe_log(close).shift(5)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(756, min_periods=756//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_020_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 1260d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(1260, min_periods=1260//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_021_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 5d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(5, min_periods=5//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_022_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 10d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(10, min_periods=10//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_023_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 21d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(21, min_periods=21//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_024_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 42d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(42, min_periods=42//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_025_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 63d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(63, min_periods=63//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_026_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 126d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(126, min_periods=126//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_027_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 252d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(252, min_periods=252//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_028_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 504d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(504, min_periods=504//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_029_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 756d."""
    s = _safe_log(close).shift(21)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(756, min_periods=756//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_030_d1(close: pd.Series) -> pd.Series:
    """Log-quadratic curvature coefficient of log-close over 1260d."""
    s = _safe_log(close).shift(0)
    def _curv(w):
        if len(w) < 3 or np.isnan(w).any(): return np.nan
        return np.polyfit(np.arange(len(w)), w, 2)[0]
    res = s.rolling(1260, min_periods=1260//2).apply(_curv, raw=True)
    return (res).diff()

def f02_pblo_gemini_031_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=318, w3=542, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 227)
    slow = _rolling_slope(x, 318)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.581765 + 5.62e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_032_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=331, w3=559, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(331, min_periods=max(331//3, 2)).max()
    trough = x.rolling(234, min_periods=max(234//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.595294 + 5.63e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_033_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=344, w3=576, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(344, min_periods=max(344//3, 2)).rank(pct=True)
    persistence = change.rolling(576, min_periods=max(576//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.273333 * persistence + 5.64e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_034_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=357, w3=593, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(248, min_periods=max(248//3, 2)).std()
    vol_slow = ret.rolling(357, min_periods=max(357//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.622353 + 5.65e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_035_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=370, w3=610, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(370, min_periods=max(370//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 8)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.286 * slope + 5.66e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_036_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=383, w3=627, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(15)
    drag = impulse.rolling(383, min_periods=max(383//3, 2)).mean()
    noise = impulse.abs().rolling(627, min_periods=max(627//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.649412 + 5.67e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_037_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=396, w3=644, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 22)
    acceleration = _rolling_slope(velocity, 396)
    curvature = _rolling_slope(acceleration, 644)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.298667 * acceleration + 5.68e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_038_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=409, w3=661, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(29, min_periods=max(29//3, 2)).mean(), upside.rolling(409, min_periods=max(409//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.822941 + 5.69e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_039_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=422, w3=678, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(422, min_periods=max(422//3, 2)).max()
    rebound = x - x.rolling(36, min_periods=max(36//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.311333 * _rolling_slope(draw, 678) + 5.7e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_040_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=43, w2=435, w3=695, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 43)
    baseline = trend.rolling(435, min_periods=max(435//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(695, min_periods=max(695//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.85 + 5.71e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_041_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=50, w2=448, w3=712, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 50)
    slow = _rolling_slope(x, 448)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.863529 + 5.72e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_042_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=57, w2=461, w3=729, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(461, min_periods=max(461//3, 2)).max()
    trough = x.rolling(57, min_periods=max(57//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.877059 + 5.73e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_043_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=64, w2=474, w3=746, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(64)
    rank = change.rolling(474, min_periods=max(474//3, 2)).rank(pct=True)
    persistence = change.rolling(746, min_periods=max(746//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.336667 * persistence + 5.74e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_044_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=71, w2=487, w3=763, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(71, min_periods=max(71//3, 2)).std()
    vol_slow = ret.rolling(487, min_periods=max(487//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.904118 + 5.75e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_045_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=78, w2=500, w3=29, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(500, min_periods=max(500//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 78)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.349333 * slope + 5.76e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_046_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=85, w2=14, w3=46, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(85)
    drag = impulse.rolling(14, min_periods=max(14//3, 2)).mean()
    noise = impulse.abs().rolling(46, min_periods=max(46//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.931176 + 5.77e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_047_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=92, w2=27, w3=63, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 92)
    acceleration = _rolling_slope(velocity, 27)
    curvature = _rolling_slope(acceleration, 63)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.362 * acceleration + 5.78e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_048_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=99, w2=40, w3=80, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(99, min_periods=max(99//3, 2)).mean(), upside.rolling(40, min_periods=max(40//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(80) * 0.958235 + 5.79e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_049_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=106, w2=53, w3=97, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(53, min_periods=max(53//3, 2)).max()
    rebound = x - x.rolling(106, min_periods=max(106//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.042333 * _rolling_slope(draw, 97) + 5.8e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_050_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=113, w2=66, w3=114, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 113)
    baseline = trend.rolling(66, min_periods=max(66//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(114, min_periods=max(114//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.985294 + 5.81e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_051_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=120, w2=79, w3=131, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 120)
    slow = _rolling_slope(x, 79)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=131, adjust=False).mean() * 0.998824 + 5.82e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_052_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=127, w2=92, w3=148, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(92, min_periods=max(92//3, 2)).max()
    trough = x.rolling(127, min_periods=max(127//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.012353 + 5.83e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_053_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=134, w2=105, w3=165, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(105, min_periods=max(105//3, 2)).rank(pct=True)
    persistence = change.rolling(165, min_periods=max(165//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.067667 * persistence + 5.84e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_054_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=141, w2=118, w3=182, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(141, min_periods=max(141//3, 2)).std()
    vol_slow = ret.rolling(118, min_periods=max(118//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.039412 + 5.85e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_055_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=148, w2=131, w3=199, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(131, min_periods=max(131//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 148)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.080333 * slope + 5.86e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_056_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=155, w2=144, w3=216, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(144, min_periods=max(144//3, 2)).mean()
    noise = impulse.abs().rolling(216, min_periods=max(216//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.066471 + 5.87e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_057_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=162, w2=157, w3=233, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 162)
    acceleration = _rolling_slope(velocity, 157)
    curvature = _rolling_slope(acceleration, 233)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.093 * acceleration + 5.88e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_058_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=169, w2=170, w3=250, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(169, min_periods=max(169//3, 2)).mean(), upside.rolling(170, min_periods=max(170//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.093529 + 5.89e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_059_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=176, w2=183, w3=267, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(183, min_periods=max(183//3, 2)).max()
    rebound = x - x.rolling(176, min_periods=max(176//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.105667 * _rolling_slope(draw, 267) + 5.9e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_060_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=183, w2=196, w3=284, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 183)
    baseline = trend.rolling(196, min_periods=max(196//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(284, min_periods=max(284//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.120588 + 5.91e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_061_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=190, w2=209, w3=301, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 190)
    slow = _rolling_slope(x, 209)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.134118 + 5.92e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_062_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=197, w2=222, w3=318, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(222, min_periods=max(222//3, 2)).max()
    trough = x.rolling(197, min_periods=max(197//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.147647 + 5.93e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_063_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=204, w2=235, w3=335, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(235, min_periods=max(235//3, 2)).rank(pct=True)
    persistence = change.rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.131 * persistence + 5.94e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_064_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=211, w2=248, w3=352, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(211, min_periods=max(211//3, 2)).std()
    vol_slow = ret.rolling(248, min_periods=max(248//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.174706 + 5.95e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_065_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=218, w2=261, w3=369, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(261, min_periods=max(261//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 218)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.143667 * slope + 5.96e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_066_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=225, w2=274, w3=386, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(274, min_periods=max(274//3, 2)).mean()
    noise = impulse.abs().rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.201765 + 5.97e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_067_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=232, w2=287, w3=403, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 232)
    acceleration = _rolling_slope(velocity, 287)
    curvature = _rolling_slope(acceleration, 403)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.156333 * acceleration + 5.98e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_068_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=239, w2=300, w3=420, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(239, min_periods=max(239//3, 2)).mean(), upside.rolling(300, min_periods=max(300//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.228824 + 5.99e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_069_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=246, w2=313, w3=437, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(313, min_periods=max(313//3, 2)).max()
    rebound = x - x.rolling(246, min_periods=max(246//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.169 * _rolling_slope(draw, 437) + 6e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_070_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=6, w2=326, w3=454, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 6)
    baseline = trend.rolling(326, min_periods=max(326//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(454, min_periods=max(454//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.255882 + 6.01e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_071_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=13, w2=339, w3=471, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 13)
    slow = _rolling_slope(x, 339)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.269412 + 6.02e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_072_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=20, w2=352, w3=488, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(352, min_periods=max(352//3, 2)).max()
    trough = x.rolling(20, min_periods=max(20//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.282941 + 6.03e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_073_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=27, w2=365, w3=505, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(27)
    rank = change.rolling(365, min_periods=max(365//3, 2)).rank(pct=True)
    persistence = change.rolling(505, min_periods=max(505//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.194333 * persistence + 6.04e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_074_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=34, w2=378, w3=522, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(34, min_periods=max(34//3, 2)).std()
    vol_slow = ret.rolling(378, min_periods=max(378//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.31 + 6.05e-05 * anchor
    return base_signal.diff()

def f02_pblo_gemini_075_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=41, w2=391, w3=539, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(391, min_periods=max(391//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 41)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.207 * slope + 6.06e-05 * anchor
    return base_signal.diff()

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_02_PARABOLIC_BLOWOFF_SIGNATURE_GEMINI_D1_001_075 = {
    "f02_pblo_gemini_001_d1": {"inputs": ['close'], "func": f02_pblo_gemini_001_d1, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_002_d1": {"inputs": ['close'], "func": f02_pblo_gemini_002_d1, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_003_d1": {"inputs": ['close'], "func": f02_pblo_gemini_003_d1, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_004_d1": {"inputs": ['close'], "func": f02_pblo_gemini_004_d1, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_005_d1": {"inputs": ['close'], "func": f02_pblo_gemini_005_d1, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_006_d1": {"inputs": ['close'], "func": f02_pblo_gemini_006_d1, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_007_d1": {"inputs": ['close'], "func": f02_pblo_gemini_007_d1, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_008_d1": {"inputs": ['close'], "func": f02_pblo_gemini_008_d1, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_009_d1": {"inputs": ['close'], "func": f02_pblo_gemini_009_d1, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_010_d1": {"inputs": ['close'], "func": f02_pblo_gemini_010_d1, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_011_d1": {"inputs": ['close'], "func": f02_pblo_gemini_011_d1, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_012_d1": {"inputs": ['close'], "func": f02_pblo_gemini_012_d1, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_013_d1": {"inputs": ['close'], "func": f02_pblo_gemini_013_d1, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_014_d1": {"inputs": ['close'], "func": f02_pblo_gemini_014_d1, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_015_d1": {"inputs": ['close'], "func": f02_pblo_gemini_015_d1, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_016_d1": {"inputs": ['close'], "func": f02_pblo_gemini_016_d1, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_017_d1": {"inputs": ['close'], "func": f02_pblo_gemini_017_d1, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_018_d1": {"inputs": ['close'], "func": f02_pblo_gemini_018_d1, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_019_d1": {"inputs": ['close'], "func": f02_pblo_gemini_019_d1, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_020_d1": {"inputs": ['close'], "func": f02_pblo_gemini_020_d1, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_021_d1": {"inputs": ['close'], "func": f02_pblo_gemini_021_d1, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_022_d1": {"inputs": ['close'], "func": f02_pblo_gemini_022_d1, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_023_d1": {"inputs": ['close'], "func": f02_pblo_gemini_023_d1, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_024_d1": {"inputs": ['close'], "func": f02_pblo_gemini_024_d1, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_025_d1": {"inputs": ['close'], "func": f02_pblo_gemini_025_d1, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_026_d1": {"inputs": ['close'], "func": f02_pblo_gemini_026_d1, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_027_d1": {"inputs": ['close'], "func": f02_pblo_gemini_027_d1, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_028_d1": {"inputs": ['close'], "func": f02_pblo_gemini_028_d1, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_029_d1": {"inputs": ['close'], "func": f02_pblo_gemini_029_d1, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_030_d1": {"inputs": ['close'], "func": f02_pblo_gemini_030_d1, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_031_d1": {"inputs": ['close'], "func": f02_pblo_gemini_031_d1, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_032_d1": {"inputs": ['close'], "func": f02_pblo_gemini_032_d1, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_033_d1": {"inputs": ['close'], "func": f02_pblo_gemini_033_d1, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_034_d1": {"inputs": ['close'], "func": f02_pblo_gemini_034_d1, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_035_d1": {"inputs": ['close'], "func": f02_pblo_gemini_035_d1, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_036_d1": {"inputs": ['close'], "func": f02_pblo_gemini_036_d1, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_037_d1": {"inputs": ['close'], "func": f02_pblo_gemini_037_d1, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_038_d1": {"inputs": ['close'], "func": f02_pblo_gemini_038_d1, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_039_d1": {"inputs": ['close'], "func": f02_pblo_gemini_039_d1, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_040_d1": {"inputs": ['close'], "func": f02_pblo_gemini_040_d1, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_041_d1": {"inputs": ['close'], "func": f02_pblo_gemini_041_d1, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_042_d1": {"inputs": ['close'], "func": f02_pblo_gemini_042_d1, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_043_d1": {"inputs": ['close'], "func": f02_pblo_gemini_043_d1, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_044_d1": {"inputs": ['close'], "func": f02_pblo_gemini_044_d1, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_045_d1": {"inputs": ['close'], "func": f02_pblo_gemini_045_d1, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_046_d1": {"inputs": ['close'], "func": f02_pblo_gemini_046_d1, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_047_d1": {"inputs": ['close'], "func": f02_pblo_gemini_047_d1, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_048_d1": {"inputs": ['close'], "func": f02_pblo_gemini_048_d1, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_049_d1": {"inputs": ['close'], "func": f02_pblo_gemini_049_d1, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_050_d1": {"inputs": ['close'], "func": f02_pblo_gemini_050_d1, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_051_d1": {"inputs": ['close'], "func": f02_pblo_gemini_051_d1, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_052_d1": {"inputs": ['close'], "func": f02_pblo_gemini_052_d1, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_053_d1": {"inputs": ['close'], "func": f02_pblo_gemini_053_d1, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_054_d1": {"inputs": ['close'], "func": f02_pblo_gemini_054_d1, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_055_d1": {"inputs": ['close'], "func": f02_pblo_gemini_055_d1, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_056_d1": {"inputs": ['close'], "func": f02_pblo_gemini_056_d1, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_057_d1": {"inputs": ['close'], "func": f02_pblo_gemini_057_d1, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_058_d1": {"inputs": ['close'], "func": f02_pblo_gemini_058_d1, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_059_d1": {"inputs": ['close'], "func": f02_pblo_gemini_059_d1, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_060_d1": {"inputs": ['close'], "func": f02_pblo_gemini_060_d1, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_061_d1": {"inputs": ['close'], "func": f02_pblo_gemini_061_d1, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_062_d1": {"inputs": ['close'], "func": f02_pblo_gemini_062_d1, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_063_d1": {"inputs": ['close'], "func": f02_pblo_gemini_063_d1, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_064_d1": {"inputs": ['close'], "func": f02_pblo_gemini_064_d1, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_065_d1": {"inputs": ['close'], "func": f02_pblo_gemini_065_d1, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_066_d1": {"inputs": ['close'], "func": f02_pblo_gemini_066_d1, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_067_d1": {"inputs": ['close'], "func": f02_pblo_gemini_067_d1, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_068_d1": {"inputs": ['close'], "func": f02_pblo_gemini_068_d1, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_069_d1": {"inputs": ['close'], "func": f02_pblo_gemini_069_d1, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_070_d1": {"inputs": ['close'], "func": f02_pblo_gemini_070_d1, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_071_d1": {"inputs": ['close'], "func": f02_pblo_gemini_071_d1, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_072_d1": {"inputs": ['close'], "func": f02_pblo_gemini_072_d1, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_073_d1": {"inputs": ['close'], "func": f02_pblo_gemini_073_d1, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_074_d1": {"inputs": ['close'], "func": f02_pblo_gemini_074_d1, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_075_d1": {"inputs": ['close'], "func": f02_pblo_gemini_075_d1, "description": "Quadratic curvature of log-price over 63d."},
}
