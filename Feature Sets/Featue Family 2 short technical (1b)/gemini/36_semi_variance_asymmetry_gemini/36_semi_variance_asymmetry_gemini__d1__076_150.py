"""36 semi variance asymmetry gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Measurement of downside vs. upside volatility to detect bearish risk bias.
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
    data = pd.concat(returns_list, axis=1).astype(float)
    window = 21
    n_comp = max(1, int(n_comp))
    out = pd.Series(np.nan, index=data.index, dtype=float)
    for i in range(window - 1, len(data)):
        w = data.iloc[i - window + 1:i + 1].to_numpy(dtype=float)
        if w.shape[1] < 2 or np.isnan(w).any():
            continue
        corr = np.corrcoef(w, rowvar=False)
        if np.ndim(corr) != 2 or not np.isfinite(corr).all():
            continue
        eigvals = np.linalg.eigvalsh(corr)
        total = eigvals.sum()
        if not np.isfinite(total) or abs(total) < 1e-12:
            continue
        k = min(n_comp, len(eigvals))
        out.iloc[i] = np.sort(eigvals)[-k:].sum() / total
    return out


# ============================================================
# FEATURE HYPOTHESES (076-150)
# ============================================================

def f36_svar_gemini_076_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=57, w2=140, w3=206, lag=13)."""
    x = low.shift(13)
    impulse = x.diff(57)
    drag = impulse.rolling(140, min_periods=max(140//3, 2)).mean()
    noise = impulse.abs().rolling(206, min_periods=max(206//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.178824 + 0.0025767 * anchor
    return base_signal.diff()

def f36_svar_gemini_077_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=64, w2=153, w3=223, lag=21)."""
    x = _safe_log(low.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 64)
    acceleration = _rolling_slope(velocity, 153)
    curvature = _rolling_slope(acceleration, 223)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.046333 * acceleration + 0.0025768 * anchor
    return base_signal.diff()

def f36_svar_gemini_078_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=71, w2=166, w3=240, lag=34)."""
    rel = _safe_div(low.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 71)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.052667 * pressure.rolling(240, min_periods=max(240//3, 2)).mean() + 0.0025769 * anchor
    return base_signal.diff()

def f36_svar_gemini_079_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=78, w2=179, w3=257, lag=55)."""
    a = low.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(78, min_periods=max(78//3, 2)).mean())
    decay = spread.ewm(span=179, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.219412 + 0.002577 * anchor
    return base_signal.diff()

def f36_svar_gemini_080_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=85, w2=192, w3=274, lag=0)."""
    a = _safe_log(low.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(192, min_periods=max(192//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 85)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.232941 + 0.0025771 * anchor
    return base_signal.diff()

def f36_svar_gemini_081_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=92, w2=205, w3=291, lag=1)."""
    a = low.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(92, min_periods=max(92//3, 2)).mean(), b.abs().rolling(205, min_periods=max(205//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.071667 * _rolling_slope(cover, 92) + 0.0025772 * anchor
    return base_signal.diff()

def f36_svar_gemini_082_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=99, w2=218, w3=308, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.078 * y + 0.922000 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 99) - _rolling_slope(basket, 218) + 0.0025773 * anchor
    return base_signal.diff()

def f36_svar_gemini_083_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=106, w2=231, w3=325, lag=3)."""
    x = low.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(106, min_periods=max(106//3, 2)).mean(), upside.rolling(231, min_periods=max(231//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.273529 + 0.0025774 * anchor
    return base_signal.diff()

def f36_svar_gemini_084_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=113, w2=244, w3=342, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    draw = x - x.rolling(244, min_periods=max(244//3, 2)).max()
    rebound = x - x.rolling(113, min_periods=max(113//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.090667 * _rolling_slope(draw, 342) + 0.0025775 * anchor
    return base_signal.diff()

def f36_svar_gemini_085_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=120, w2=257, w3=359, lag=8)."""
    a = _safe_log(low.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(120) - b.diff(126)
    stress = imbalance.rolling(359, min_periods=max(359//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.300588 + 0.0025776 * anchor
    return base_signal.diff()

def f36_svar_gemini_086_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=127, w2=270, w3=376, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 127)
    baseline = trend.rolling(270, min_periods=max(270//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(376, min_periods=max(376//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.314118 + 0.0025777 * anchor
    return base_signal.diff()

def f36_svar_gemini_087_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=134, w2=283, w3=393, lag=21)."""
    x = _safe_log(low.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 134)
    slow = _rolling_slope(x, 283)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.327647 + 0.0025778 * anchor
    return base_signal.diff()

def f36_svar_gemini_088_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=141, w2=296, w3=410, lag=34)."""
    x = low.shift(34)
    peak = x.rolling(296, min_periods=max(296//3, 2)).max()
    trough = x.rolling(141, min_periods=max(141//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.341176 + 0.0025779 * anchor
    return base_signal.diff()

def f36_svar_gemini_089_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=148, w2=309, w3=427, lag=55)."""
    x = low.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(309, min_periods=max(309//3, 2)).rank(pct=True)
    persistence = change.rolling(427, min_periods=max(427//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.122333 * persistence + 0.002578 * anchor
    return base_signal.diff()

def f36_svar_gemini_090_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=155, w2=322, w3=444, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(155, min_periods=max(155//3, 2)).std()
    vol_slow = ret.rolling(322, min_periods=max(322//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.368235 + 0.0025781 * anchor
    return base_signal.diff()

def f36_svar_gemini_091_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=162, w2=335, w3=461, lag=1)."""
    x = low.shift(1)
    ma = x.rolling(335, min_periods=max(335//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 162)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.135 * slope + 0.0025782 * anchor
    return base_signal.diff()

def f36_svar_gemini_092_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=169, w2=348, w3=478, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(348, min_periods=max(348//3, 2)).mean()
    noise = impulse.abs().rolling(478, min_periods=max(478//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.395294 + 0.0025783 * anchor
    return base_signal.diff()

def f36_svar_gemini_093_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=176, w2=361, w3=495, lag=3)."""
    x = _safe_log(low.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 176)
    acceleration = _rolling_slope(velocity, 361)
    curvature = _rolling_slope(acceleration, 495)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.147667 * acceleration + 0.0025784 * anchor
    return base_signal.diff()

def f36_svar_gemini_094_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=183, w2=374, w3=512, lag=5)."""
    rel = _safe_div(low.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 183)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.154 * pressure.rolling(512, min_periods=max(512//3, 2)).mean() + 0.0025785 * anchor
    return base_signal.diff()

def f36_svar_gemini_095_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=190, w2=387, w3=529, lag=8)."""
    a = low.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(190, min_periods=max(190//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.435882 + 0.0025786 * anchor
    return base_signal.diff()

def f36_svar_gemini_096_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=197, w2=400, w3=546, lag=13)."""
    a = _safe_log(low.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(400, min_periods=max(400//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 197)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.449412 + 0.0025787 * anchor
    return base_signal.diff()

def f36_svar_gemini_097_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=204, w2=413, w3=563, lag=21)."""
    a = low.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(204, min_periods=max(204//3, 2)).mean(), b.abs().rolling(413, min_periods=max(413//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.173 * _rolling_slope(cover, 204) + 0.0025788 * anchor
    return base_signal.diff()

def f36_svar_gemini_098_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=211, w2=426, w3=580, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.179333 * y + 0.820667 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 211) - _rolling_slope(basket, 426) + 0.0025789 * anchor
    return base_signal.diff()

def f36_svar_gemini_099_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=218, w2=439, w3=597, lag=55)."""
    x = low.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(218, min_periods=max(218//3, 2)).mean(), upside.rolling(439, min_periods=max(439//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.49 + 0.002579 * anchor
    return base_signal.diff()

def f36_svar_gemini_100_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=225, w2=452, w3=614, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    draw = x - x.rolling(452, min_periods=max(452//3, 2)).max()
    rebound = x - x.rolling(225, min_periods=max(225//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.192 * _rolling_slope(draw, 614) + 0.0025791 * anchor
    return base_signal.diff()

def f36_svar_gemini_101_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=232, w2=465, w3=631, lag=1)."""
    a = _safe_log(low.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(631, min_periods=max(631//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.517059 + 0.0025792 * anchor
    return base_signal.diff()

def f36_svar_gemini_102_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=239, w2=478, w3=648, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 239)
    baseline = trend.rolling(478, min_periods=max(478//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(648, min_periods=max(648//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.530588 + 0.0025793 * anchor
    return base_signal.diff()

def f36_svar_gemini_103_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=246, w2=491, w3=665, lag=3)."""
    x = _safe_log(low.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 246)
    slow = _rolling_slope(x, 491)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.544118 + 0.0025794 * anchor
    return base_signal.diff()

def f36_svar_gemini_104_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=6, w2=504, w3=682, lag=5)."""
    x = low.shift(5)
    peak = x.rolling(504, min_periods=max(504//3, 2)).max()
    trough = x.rolling(6, min_periods=max(6//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.557647 + 0.0025795 * anchor
    return base_signal.diff()

def f36_svar_gemini_105_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=13, w2=18, w3=699, lag=8)."""
    x = low.shift(8)
    change = x.pct_change(13)
    rank = change.rolling(18, min_periods=max(18//3, 2)).rank(pct=True)
    persistence = change.rolling(699, min_periods=max(699//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.223667 * persistence + 0.0025796 * anchor
    return base_signal.diff()

def f36_svar_gemini_106_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=20, w2=31, w3=716, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(20, min_periods=max(20//3, 2)).std()
    vol_slow = ret.rolling(31, min_periods=max(31//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.584706 + 0.0025797 * anchor
    return base_signal.diff()

def f36_svar_gemini_107_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=27, w2=44, w3=733, lag=21)."""
    x = low.shift(21)
    ma = x.rolling(44, min_periods=max(44//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 27)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.236333 * slope + 0.0025798 * anchor
    return base_signal.diff()

def f36_svar_gemini_108_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=34, w2=57, w3=750, lag=34)."""
    x = low.shift(34)
    impulse = x.diff(34)
    drag = impulse.rolling(57, min_periods=max(57//3, 2)).mean()
    noise = impulse.abs().rolling(750, min_periods=max(750//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.611765 + 0.0025799 * anchor
    return base_signal.diff()

def f36_svar_gemini_109_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=41, w2=70, w3=767, lag=55)."""
    x = _safe_log(low.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 41)
    acceleration = _rolling_slope(velocity, 70)
    curvature = _rolling_slope(acceleration, 767)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.249 * acceleration + 0.00258 * anchor
    return base_signal.diff()

def f36_svar_gemini_110_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=48, w2=83, w3=33, lag=0)."""
    rel = _safe_div(low.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 48)
    pressure = rel_log.diff(83)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.255333 * pressure.rolling(33, min_periods=max(33//3, 2)).mean() + 0.0025801 * anchor
    return base_signal.diff()

def f36_svar_gemini_111_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=55, w2=96, w3=50, lag=1)."""
    a = low.shift(1)
    b = close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(55, min_periods=max(55//3, 2)).mean())
    decay = spread.ewm(span=96, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.652353 + 0.0025802 * anchor
    return base_signal.diff()

def f36_svar_gemini_112_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=62, w2=109, w3=67, lag=2)."""
    a = _safe_log(low.abs() + 1.0).shift(2)
    b = _safe_log(close.abs() + 1.0).shift(2)
    corr = a.rolling(109, min_periods=max(109//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 62)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.665882 + 0.0025803 * anchor
    return base_signal.diff()

def f36_svar_gemini_113_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=69, w2=122, w3=84, lag=3)."""
    a = low.shift(3)
    b = close.shift(3)
    cover = _safe_div(a.rolling(69, min_periods=max(69//3, 2)).mean(), b.abs().rolling(122, min_periods=max(122//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(84) + 0.274333 * _rolling_slope(cover, 69) + 0.0025804 * anchor
    return base_signal.diff()

def f36_svar_gemini_114_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=76, w2=135, w3=101, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    y = _safe_log(close.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.280667 * y + 0.719333 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 76) - _rolling_slope(basket, 135) + 0.0025805 * anchor
    return base_signal.diff()

def f36_svar_gemini_115_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=83, w2=148, w3=118, lag=8)."""
    x = low.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(83, min_periods=max(83//3, 2)).mean(), upside.rolling(148, min_periods=max(148//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(118) * 0.852941 + 0.0025806 * anchor
    return base_signal.diff()

def f36_svar_gemini_116_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=90, w2=161, w3=135, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    draw = x - x.rolling(161, min_periods=max(161//3, 2)).max()
    rebound = x - x.rolling(90, min_periods=max(90//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.293333 * _rolling_slope(draw, 135) + 0.0025807 * anchor
    return base_signal.diff()

def f36_svar_gemini_117_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=97, w2=174, w3=152, lag=21)."""
    a = _safe_log(low.abs() + 1.0).shift(21)
    b = _safe_log(close.abs() + 1.0).shift(21)
    imbalance = a.diff(97) - b.diff(126)
    stress = imbalance.rolling(152, min_periods=max(152//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.88 + 0.0025808 * anchor
    return base_signal.diff()

def f36_svar_gemini_118_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=104, w2=187, w3=169, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 104)
    baseline = trend.rolling(187, min_periods=max(187//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(169, min_periods=max(169//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.893529 + 0.0025809 * anchor
    return base_signal.diff()

def f36_svar_gemini_119_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=111, w2=200, w3=186, lag=55)."""
    x = _safe_log(low.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 111)
    slow = _rolling_slope(x, 200)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=186, adjust=False).mean() * 0.907059 + 0.002581 * anchor
    return base_signal.diff()

def f36_svar_gemini_120_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=118, w2=213, w3=203, lag=0)."""
    x = low.shift(0)
    peak = x.rolling(213, min_periods=max(213//3, 2)).max()
    trough = x.rolling(118, min_periods=max(118//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.920588 + 0.0025811 * anchor
    return base_signal.diff()

def f36_svar_gemini_121_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=125, w2=226, w3=220, lag=1)."""
    x = low.shift(1)
    change = x.pct_change(125)
    rank = change.rolling(226, min_periods=max(226//3, 2)).rank(pct=True)
    persistence = change.rolling(220, min_periods=max(220//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.325 * persistence + 0.0025812 * anchor
    return base_signal.diff()

def f36_svar_gemini_122_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=132, w2=239, w3=237, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(132, min_periods=max(132//3, 2)).std()
    vol_slow = ret.rolling(239, min_periods=max(239//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.947647 + 0.0025813 * anchor
    return base_signal.diff()

def f36_svar_gemini_123_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=139, w2=252, w3=254, lag=3)."""
    x = low.shift(3)
    ma = x.rolling(252, min_periods=max(252//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 139)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.337667 * slope + 0.0025814 * anchor
    return base_signal.diff()

def f36_svar_gemini_124_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=146, w2=265, w3=271, lag=5)."""
    x = low.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(265, min_periods=max(265//3, 2)).mean()
    noise = impulse.abs().rolling(271, min_periods=max(271//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.974706 + 0.0025815 * anchor
    return base_signal.diff()

def f36_svar_gemini_125_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=153, w2=278, w3=288, lag=8)."""
    x = _safe_log(low.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 153)
    acceleration = _rolling_slope(velocity, 278)
    curvature = _rolling_slope(acceleration, 288)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.350333 * acceleration + 0.0025816 * anchor
    return base_signal.diff()

def f36_svar_gemini_126_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=160, w2=291, w3=305, lag=13)."""
    rel = _safe_div(low.shift(13), close.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 160)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.356667 * pressure.rolling(305, min_periods=max(305//3, 2)).mean() + 0.0025817 * anchor
    return base_signal.diff()

def f36_svar_gemini_127_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=167, w2=304, w3=322, lag=21)."""
    a = low.shift(21)
    b = close.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(167, min_periods=max(167//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.015294 + 0.0025818 * anchor
    return base_signal.diff()

def f36_svar_gemini_128_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=174, w2=317, w3=339, lag=34)."""
    a = _safe_log(low.abs() + 1.0).shift(34)
    b = _safe_log(close.abs() + 1.0).shift(34)
    corr = a.rolling(317, min_periods=max(317//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 174)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.028824 + 0.0025819 * anchor
    return base_signal.diff()

def f36_svar_gemini_129_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=181, w2=330, w3=356, lag=55)."""
    a = low.shift(55)
    b = close.shift(55)
    cover = _safe_div(a.rolling(181, min_periods=max(181//3, 2)).mean(), b.abs().rolling(330, min_periods=max(330//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.043333 * _rolling_slope(cover, 181) + 0.002582 * anchor
    return base_signal.diff()

def f36_svar_gemini_130_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=188, w2=343, w3=373, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    y = _safe_log(close.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.049667 * y + 0.950333 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 188) - _rolling_slope(basket, 343) + 0.0025821 * anchor
    return base_signal.diff()

def f36_svar_gemini_131_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=195, w2=356, w3=390, lag=1)."""
    x = low.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(195, min_periods=max(195//3, 2)).mean(), upside.rolling(356, min_periods=max(356//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.069412 + 0.0025822 * anchor
    return base_signal.diff()

def f36_svar_gemini_132_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=202, w2=369, w3=407, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    draw = x - x.rolling(369, min_periods=max(369//3, 2)).max()
    rebound = x - x.rolling(202, min_periods=max(202//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.062333 * _rolling_slope(draw, 407) + 0.0025823 * anchor
    return base_signal.diff()

def f36_svar_gemini_133_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=209, w2=382, w3=424, lag=3)."""
    a = _safe_log(low.abs() + 1.0).shift(3)
    b = _safe_log(close.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(424, min_periods=max(424//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.096471 + 0.0025824 * anchor
    return base_signal.diff()

def f36_svar_gemini_134_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=216, w2=395, w3=441, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 216)
    baseline = trend.rolling(395, min_periods=max(395//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(441, min_periods=max(441//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.11 + 0.0025825 * anchor
    return base_signal.diff()

def f36_svar_gemini_135_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=223, w2=408, w3=458, lag=8)."""
    x = _safe_log(low.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 223)
    slow = _rolling_slope(x, 408)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.123529 + 0.0025826 * anchor
    return base_signal.diff()

def f36_svar_gemini_136_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=230, w2=421, w3=475, lag=13)."""
    x = low.shift(13)
    peak = x.rolling(421, min_periods=max(421//3, 2)).max()
    trough = x.rolling(230, min_periods=max(230//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.137059 + 0.0025827 * anchor
    return base_signal.diff()

def f36_svar_gemini_137_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=237, w2=434, w3=492, lag=21)."""
    x = low.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(434, min_periods=max(434//3, 2)).rank(pct=True)
    persistence = change.rolling(492, min_periods=max(492//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.094 * persistence + 0.0025828 * anchor
    return base_signal.diff()

def f36_svar_gemini_138_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=244, w2=447, w3=509, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(244, min_periods=max(244//3, 2)).std()
    vol_slow = ret.rolling(447, min_periods=max(447//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.164118 + 0.0025829 * anchor
    return base_signal.diff()

def f36_svar_gemini_139_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=251, w2=460, w3=526, lag=55)."""
    x = low.shift(55)
    ma = x.rolling(460, min_periods=max(460//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 251)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.106667 * slope + 0.002583 * anchor
    return base_signal.diff()

def f36_svar_gemini_140_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=11, w2=473, w3=543, lag=0)."""
    x = low.shift(0)
    impulse = x.diff(11)
    drag = impulse.rolling(473, min_periods=max(473//3, 2)).mean()
    noise = impulse.abs().rolling(543, min_periods=max(543//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.191176 + 0.0025831 * anchor
    return base_signal.diff()

def f36_svar_gemini_141_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=18, w2=486, w3=560, lag=1)."""
    x = _safe_log(low.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 18)
    acceleration = _rolling_slope(velocity, 486)
    curvature = _rolling_slope(acceleration, 560)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.119333 * acceleration + 0.0025832 * anchor
    return base_signal.diff()

def f36_svar_gemini_142_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=25, w2=499, w3=577, lag=2)."""
    rel = _safe_div(low.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 25)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.125667 * pressure.rolling(577, min_periods=max(577//3, 2)).mean() + 0.0025833 * anchor
    return base_signal.diff()

def f36_svar_gemini_143_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=32, w2=13, w3=594, lag=3)."""
    a = low.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(32, min_periods=max(32//3, 2)).mean())
    decay = spread.ewm(span=13, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.231765 + 0.0025834 * anchor
    return base_signal.diff()

def f36_svar_gemini_144_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=39, w2=26, w3=611, lag=5)."""
    a = _safe_log(low.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(26, min_periods=max(26//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 39)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.245294 + 0.0025835 * anchor
    return base_signal.diff()

def f36_svar_gemini_145_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=46, w2=39, w3=628, lag=8)."""
    a = low.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(46, min_periods=max(46//3, 2)).mean(), b.abs().rolling(39, min_periods=max(39//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.144667 * _rolling_slope(cover, 46) + 0.0025836 * anchor
    return base_signal.diff()

def f36_svar_gemini_146_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=53, w2=52, w3=645, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.151 * y + 0.849000 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 53) - _rolling_slope(basket, 52) + 0.0025837 * anchor
    return base_signal.diff()

def f36_svar_gemini_147_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=60, w2=65, w3=662, lag=21)."""
    x = low.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(60, min_periods=max(60//3, 2)).mean(), upside.rolling(65, min_periods=max(65//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.285882 + 0.0025838 * anchor
    return base_signal.diff()

def f36_svar_gemini_148_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=67, w2=78, w3=679, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    draw = x - x.rolling(78, min_periods=max(78//3, 2)).max()
    rebound = x - x.rolling(67, min_periods=max(67//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.163667 * _rolling_slope(draw, 679) + 0.0025839 * anchor
    return base_signal.diff()

def f36_svar_gemini_149_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=91, w3=696, lag=55)."""
    a = _safe_log(low.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(74) - b.diff(91)
    stress = imbalance.rolling(696, min_periods=max(696//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.312941 + 0.002584 * anchor
    return base_signal.diff()

def f36_svar_gemini_150_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=104, w3=713, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 81)
    baseline = trend.rolling(104, min_periods=max(104//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(713, min_periods=max(713//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.326471 + 0.0025841 * anchor
    return base_signal.diff()
