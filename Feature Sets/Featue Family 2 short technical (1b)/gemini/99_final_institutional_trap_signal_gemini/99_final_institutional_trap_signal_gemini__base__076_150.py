"""99 final institutional trap signal gemini base features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Specific price-volume patterns signaling a final trap for retail participants.
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

def f99_fits_gemini_076(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=25, w2=375, w3=541, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(375, min_periods=max(375//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 25)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.186471 + 0.0060907 * anchor
    return base_signal

def f99_fits_gemini_077(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=32, w2=388, w3=558, lag=21)."""
    a = high.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(32, min_periods=max(32//3, 2)).mean(), b.abs().rolling(388, min_periods=max(388//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.268667 * _rolling_slope(cover, 32) + 0.0060908 * anchor
    return base_signal

def f99_fits_gemini_078(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=39, w2=401, w3=575, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.275 * y + 0.725000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 39) - _rolling_slope(basket, 401) + 0.0060909 * anchor
    return base_signal

def f99_fits_gemini_079(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=46, w2=414, w3=592, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(46, min_periods=max(46//3, 2)).mean(), upside.rolling(414, min_periods=max(414//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.227059 + 0.006091 * anchor
    return base_signal

def f99_fits_gemini_080(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=53, w2=427, w3=609, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(427, min_periods=max(427//3, 2)).max()
    rebound = x - x.rolling(53, min_periods=max(53//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.287667 * _rolling_slope(draw, 609) + 0.0060911 * anchor
    return base_signal

def f99_fits_gemini_081(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=60, w2=440, w3=626, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(60) - b.diff(126)
    stress = imbalance.rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.254118 + 0.0060912 * anchor
    return base_signal

def f99_fits_gemini_082(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=67, w2=453, w3=643, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 67)
    baseline = trend.rolling(453, min_periods=max(453//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(643, min_periods=max(643//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.267647 + 0.0060913 * anchor
    return base_signal

def f99_fits_gemini_083(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=74, w2=466, w3=660, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 74)
    slow = _rolling_slope(x, 466)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.281176 + 0.0060914 * anchor
    return base_signal

def f99_fits_gemini_084(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=81, w2=479, w3=677, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(479, min_periods=max(479//3, 2)).max()
    trough = x.rolling(81, min_periods=max(81//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.294706 + 0.0060915 * anchor
    return base_signal

def f99_fits_gemini_085(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=88, w2=492, w3=694, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(88)
    rank = change.rolling(492, min_periods=max(492//3, 2)).rank(pct=True)
    persistence = change.rolling(694, min_periods=max(694//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.319333 * persistence + 0.0060916 * anchor
    return base_signal

def f99_fits_gemini_086(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=95, w2=505, w3=711, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(95, min_periods=max(95//3, 2)).std()
    vol_slow = ret.rolling(505, min_periods=max(505//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.321765 + 0.0060917 * anchor
    return base_signal

def f99_fits_gemini_087(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=102, w2=19, w3=728, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(19, min_periods=max(19//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 102)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.332 * slope + 0.0060918 * anchor
    return base_signal

def f99_fits_gemini_088(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=109, w2=32, w3=745, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(109)
    drag = impulse.rolling(32, min_periods=max(32//3, 2)).mean()
    noise = impulse.abs().rolling(745, min_periods=max(745//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.348824 + 0.0060919 * anchor
    return base_signal

def f99_fits_gemini_089(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=116, w2=45, w3=762, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 116)
    acceleration = _rolling_slope(velocity, 45)
    curvature = _rolling_slope(acceleration, 762)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.344667 * acceleration + 0.006092 * anchor
    return base_signal

def f99_fits_gemini_090(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=123, w2=58, w3=28, lag=0)."""
    rel = _safe_div(high.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 123)
    pressure = rel_log.diff(58)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.351 * pressure.rolling(28, min_periods=max(28//3, 2)).mean() + 0.0060921 * anchor
    return base_signal

def f99_fits_gemini_091(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=130, w2=71, w3=45, lag=1)."""
    a = high.shift(1)
    b = close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(130, min_periods=max(130//3, 2)).mean())
    decay = spread.ewm(span=71, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.389412 + 0.0060922 * anchor
    return base_signal

def f99_fits_gemini_092(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=137, w2=84, w3=62, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(close.abs() + 1.0).shift(2)
    corr = a.rolling(84, min_periods=max(84//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 137)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.402941 + 0.0060923 * anchor
    return base_signal

def f99_fits_gemini_093(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=144, w2=97, w3=79, lag=3)."""
    a = high.shift(3)
    b = close.shift(3)
    cover = _safe_div(a.rolling(144, min_periods=max(144//3, 2)).mean(), b.abs().rolling(97, min_periods=max(97//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(79) + 0.037667 * _rolling_slope(cover, 144) + 0.0060924 * anchor
    return base_signal

def f99_fits_gemini_094(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=151, w2=110, w3=96, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(close.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.044 * y + 0.956000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 151) - _rolling_slope(basket, 110) + 0.0060925 * anchor
    return base_signal

def f99_fits_gemini_095(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=158, w2=123, w3=113, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(158, min_periods=max(158//3, 2)).mean(), upside.rolling(123, min_periods=max(123//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(113) * 1.443529 + 0.0060926 * anchor
    return base_signal

def f99_fits_gemini_096(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=165, w2=136, w3=130, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(136, min_periods=max(136//3, 2)).max()
    rebound = x - x.rolling(165, min_periods=max(165//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.056667 * _rolling_slope(draw, 130) + 0.0060927 * anchor
    return base_signal

def f99_fits_gemini_097(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=172, w2=149, w3=147, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(close.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(147, min_periods=max(147//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.470588 + 0.0060928 * anchor
    return base_signal

def f99_fits_gemini_098(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=179, w2=162, w3=164, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 179)
    baseline = trend.rolling(162, min_periods=max(162//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(164, min_periods=max(164//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.484118 + 0.0060929 * anchor
    return base_signal

def f99_fits_gemini_099(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=186, w2=175, w3=181, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 186)
    slow = _rolling_slope(x, 175)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=181, adjust=False).mean() * 1.497647 + 0.006093 * anchor
    return base_signal

def f99_fits_gemini_100(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=193, w2=188, w3=198, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(188, min_periods=max(188//3, 2)).max()
    trough = x.rolling(193, min_periods=max(193//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.511176 + 0.0060931 * anchor
    return base_signal

def f99_fits_gemini_101(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=200, w2=201, w3=215, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(201, min_periods=max(201//3, 2)).rank(pct=True)
    persistence = change.rolling(215, min_periods=max(215//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.088333 * persistence + 0.0060932 * anchor
    return base_signal

def f99_fits_gemini_102(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=207, w2=214, w3=232, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(207, min_periods=max(207//3, 2)).std()
    vol_slow = ret.rolling(214, min_periods=max(214//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.538235 + 0.0060933 * anchor
    return base_signal

def f99_fits_gemini_103(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=214, w2=227, w3=249, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(227, min_periods=max(227//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 214)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.101 * slope + 0.0060934 * anchor
    return base_signal

def f99_fits_gemini_104(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=221, w2=240, w3=266, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(240, min_periods=max(240//3, 2)).mean()
    noise = impulse.abs().rolling(266, min_periods=max(266//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.565294 + 0.0060935 * anchor
    return base_signal

def f99_fits_gemini_105(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=228, w2=253, w3=283, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 228)
    acceleration = _rolling_slope(velocity, 253)
    curvature = _rolling_slope(acceleration, 283)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.113667 * acceleration + 0.0060936 * anchor
    return base_signal

def f99_fits_gemini_106(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=235, w2=266, w3=300, lag=13)."""
    rel = _safe_div(high.shift(13), close.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 235)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.12 * pressure.rolling(300, min_periods=max(300//3, 2)).mean() + 0.0060937 * anchor
    return base_signal

def f99_fits_gemini_107(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=242, w2=279, w3=317, lag=21)."""
    a = high.shift(21)
    b = close.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(242, min_periods=max(242//3, 2)).mean())
    decay = spread.ewm(span=279, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.605882 + 0.0060938 * anchor
    return base_signal

def f99_fits_gemini_108(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=249, w2=292, w3=334, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(close.abs() + 1.0).shift(34)
    corr = a.rolling(292, min_periods=max(292//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 249)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.619412 + 0.0060939 * anchor
    return base_signal

def f99_fits_gemini_109(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=9, w2=305, w3=351, lag=55)."""
    a = high.shift(55)
    b = close.shift(55)
    cover = _safe_div(a.rolling(9, min_periods=max(9//3, 2)).mean(), b.abs().rolling(305, min_periods=max(305//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.139 * _rolling_slope(cover, 9) + 0.006094 * anchor
    return base_signal

def f99_fits_gemini_110(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=16, w2=318, w3=368, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(close.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.145333 * y + 0.854667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 16) - _rolling_slope(basket, 318) + 0.0060941 * anchor
    return base_signal

def f99_fits_gemini_111(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=23, w2=331, w3=385, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(331, min_periods=max(331//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.66 + 0.0060942 * anchor
    return base_signal

def f99_fits_gemini_112(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=30, w2=344, w3=402, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(344, min_periods=max(344//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.158 * _rolling_slope(draw, 402) + 0.0060943 * anchor
    return base_signal

def f99_fits_gemini_113(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=37, w2=357, w3=419, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(close.abs() + 1.0).shift(3)
    imbalance = a.diff(37) - b.diff(126)
    stress = imbalance.rolling(419, min_periods=max(419//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.833529 + 0.0060944 * anchor
    return base_signal

def f99_fits_gemini_114(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=44, w2=370, w3=436, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 44)
    baseline = trend.rolling(370, min_periods=max(370//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(436, min_periods=max(436//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.847059 + 0.0060945 * anchor
    return base_signal

def f99_fits_gemini_115(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=51, w2=383, w3=453, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 51)
    slow = _rolling_slope(x, 383)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.860588 + 0.0060946 * anchor
    return base_signal

def f99_fits_gemini_116(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=58, w2=396, w3=470, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(396, min_periods=max(396//3, 2)).max()
    trough = x.rolling(58, min_periods=max(58//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.874118 + 0.0060947 * anchor
    return base_signal

def f99_fits_gemini_117(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=65, w2=409, w3=487, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(65)
    rank = change.rolling(409, min_periods=max(409//3, 2)).rank(pct=True)
    persistence = change.rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.189667 * persistence + 0.0060948 * anchor
    return base_signal

def f99_fits_gemini_118(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=72, w2=422, w3=504, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(72, min_periods=max(72//3, 2)).std()
    vol_slow = ret.rolling(422, min_periods=max(422//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.901176 + 0.0060949 * anchor
    return base_signal

def f99_fits_gemini_119(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=79, w2=435, w3=521, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(435, min_periods=max(435//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 79)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.202333 * slope + 0.006095 * anchor
    return base_signal

def f99_fits_gemini_120(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=86, w2=448, w3=538, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(86)
    drag = impulse.rolling(448, min_periods=max(448//3, 2)).mean()
    noise = impulse.abs().rolling(538, min_periods=max(538//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.928235 + 0.0060951 * anchor
    return base_signal

def f99_fits_gemini_121(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=93, w2=461, w3=555, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 93)
    acceleration = _rolling_slope(velocity, 461)
    curvature = _rolling_slope(acceleration, 555)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.215 * acceleration + 0.0060952 * anchor
    return base_signal

def f99_fits_gemini_122(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=100, w2=474, w3=572, lag=2)."""
    rel = _safe_div(high.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 100)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.221333 * pressure.rolling(572, min_periods=max(572//3, 2)).mean() + 0.0060953 * anchor
    return base_signal

def f99_fits_gemini_123(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=107, w2=487, w3=589, lag=3)."""
    a = high.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(107, min_periods=max(107//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.968824 + 0.0060954 * anchor
    return base_signal

def f99_fits_gemini_124(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=114, w2=500, w3=606, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(500, min_periods=max(500//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 114)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.982353 + 0.0060955 * anchor
    return base_signal

def f99_fits_gemini_125(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=121, w2=14, w3=623, lag=8)."""
    a = high.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(121, min_periods=max(121//3, 2)).mean(), b.abs().rolling(14, min_periods=max(14//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.240333 * _rolling_slope(cover, 121) + 0.0060956 * anchor
    return base_signal

def f99_fits_gemini_126(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=128, w2=27, w3=640, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.246667 * y + 0.753333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 128) - _rolling_slope(basket, 27) + 0.0060957 * anchor
    return base_signal

def f99_fits_gemini_127(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=135, w2=40, w3=657, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(40, min_periods=max(40//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.022941 + 0.0060958 * anchor
    return base_signal

def f99_fits_gemini_128(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=142, w2=53, w3=674, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(53, min_periods=max(53//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.259333 * _rolling_slope(draw, 674) + 0.0060959 * anchor
    return base_signal

def f99_fits_gemini_129(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=149, w2=66, w3=691, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(66)
    stress = imbalance.rolling(691, min_periods=max(691//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.05 + 0.006096 * anchor
    return base_signal

def f99_fits_gemini_130(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=156, w2=79, w3=708, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 156)
    baseline = trend.rolling(79, min_periods=max(79//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.063529 + 0.0060961 * anchor
    return base_signal

def f99_fits_gemini_131(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=163, w2=92, w3=725, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 163)
    slow = _rolling_slope(x, 92)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.077059 + 0.0060962 * anchor
    return base_signal

def f99_fits_gemini_132(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=170, w2=105, w3=742, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(105, min_periods=max(105//3, 2)).max()
    trough = x.rolling(170, min_periods=max(170//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.090588 + 0.0060963 * anchor
    return base_signal

def f99_fits_gemini_133(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=177, w2=118, w3=759, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(118, min_periods=max(118//3, 2)).rank(pct=True)
    persistence = change.rolling(759, min_periods=max(759//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.291 * persistence + 0.0060964 * anchor
    return base_signal

def f99_fits_gemini_134(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=184, w2=131, w3=25, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(184, min_periods=max(184//3, 2)).std()
    vol_slow = ret.rolling(131, min_periods=max(131//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.117647 + 0.0060965 * anchor
    return base_signal

def f99_fits_gemini_135(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=191, w2=144, w3=42, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(144, min_periods=max(144//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 191)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.303667 * slope + 0.0060966 * anchor
    return base_signal

def f99_fits_gemini_136(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=198, w2=157, w3=59, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(157, min_periods=max(157//3, 2)).mean()
    noise = impulse.abs().rolling(59, min_periods=max(59//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.144706 + 0.0060967 * anchor
    return base_signal

def f99_fits_gemini_137(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=205, w2=170, w3=76, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 205)
    acceleration = _rolling_slope(velocity, 170)
    curvature = _rolling_slope(acceleration, 76)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.316333 * acceleration + 0.0060968 * anchor
    return base_signal

def f99_fits_gemini_138(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=212, w2=183, w3=93, lag=34)."""
    rel = _safe_div(high.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 212)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.322667 * pressure.rolling(93, min_periods=max(93//3, 2)).mean() + 0.0060969 * anchor
    return base_signal

def f99_fits_gemini_139(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=219, w2=196, w3=110, lag=55)."""
    a = high.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(219, min_periods=max(219//3, 2)).mean())
    decay = spread.ewm(span=196, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.185294 + 0.006097 * anchor
    return base_signal

def f99_fits_gemini_140(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=226, w2=209, w3=127, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(209, min_periods=max(209//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 226)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.198824 + 0.0060971 * anchor
    return base_signal

def f99_fits_gemini_141(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=233, w2=222, w3=144, lag=1)."""
    a = high.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(233, min_periods=max(233//3, 2)).mean(), b.abs().rolling(222, min_periods=max(222//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.341667 * _rolling_slope(cover, 233) + 0.0060972 * anchor
    return base_signal

def f99_fits_gemini_142(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=240, w2=235, w3=161, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.348 * y + 0.652000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 240) - _rolling_slope(basket, 235) + 0.0060973 * anchor
    return base_signal

def f99_fits_gemini_143(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=247, w2=248, w3=178, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(247, min_periods=max(247//3, 2)).mean(), upside.rolling(248, min_periods=max(248//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.239412 + 0.0060974 * anchor
    return base_signal

def f99_fits_gemini_144(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=7, w2=261, w3=195, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(261, min_periods=max(261//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.360667 * _rolling_slope(draw, 195) + 0.0060975 * anchor
    return base_signal

def f99_fits_gemini_145(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=14, w2=274, w3=212, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(14) - b.diff(126)
    stress = imbalance.rolling(212, min_periods=max(212//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.266471 + 0.0060976 * anchor
    return base_signal

def f99_fits_gemini_146(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=21, w2=287, w3=229, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 21)
    baseline = trend.rolling(287, min_periods=max(287//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(229, min_periods=max(229//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.28 + 0.0060977 * anchor
    return base_signal

def f99_fits_gemini_147(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=28, w2=300, w3=246, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 28)
    slow = _rolling_slope(x, 300)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=246, adjust=False).mean() * 1.293529 + 0.0060978 * anchor
    return base_signal

def f99_fits_gemini_148(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=35, w2=313, w3=263, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(313, min_periods=max(313//3, 2)).max()
    trough = x.rolling(35, min_periods=max(35//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.307059 + 0.0060979 * anchor
    return base_signal

def f99_fits_gemini_149(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=42, w2=326, w3=280, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(42)
    rank = change.rolling(326, min_periods=max(326//3, 2)).rank(pct=True)
    persistence = change.rolling(280, min_periods=max(280//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.06 * persistence + 0.006098 * anchor
    return base_signal

def f99_fits_gemini_150(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=49, w2=339, w3=297, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(49, min_periods=max(49//3, 2)).std()
    vol_slow = ret.rolling(339, min_periods=max(339//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.334118 + 0.0060981 * anchor
    return base_signal
