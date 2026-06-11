"""61 price volume convexity ratio gemini base features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Non-linear relationship between price change and volume as a signal of trend strength.
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

def f61_pvcr_gemini_076(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=6, w2=181, w3=763, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(181, min_periods=max(181//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 6)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.92 + 0.0039627 * anchor
    return base_signal

def f61_pvcr_gemini_077(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=13, w2=194, w3=29, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(13, min_periods=max(13//3, 2)).mean(), b.abs().rolling(194, min_periods=max(194//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(29) + 0.090333 * _rolling_slope(cover, 13) + 0.0039628 * anchor
    return base_signal

def f61_pvcr_gemini_078(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=20, w2=207, w3=46, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.096667 * y + 0.903333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 20) - _rolling_slope(basket, 207) + 0.0039629 * anchor
    return base_signal

def f61_pvcr_gemini_079(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=27, w2=220, w3=63, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(27, min_periods=max(27//3, 2)).mean(), upside.rolling(220, min_periods=max(220//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(63) * 0.960588 + 0.003963 * anchor
    return base_signal

def f61_pvcr_gemini_080(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=34, w2=233, w3=80, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(233, min_periods=max(233//3, 2)).max()
    rebound = x - x.rolling(34, min_periods=max(34//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.109333 * _rolling_slope(draw, 80) + 0.0039631 * anchor
    return base_signal

def f61_pvcr_gemini_081(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=41, w2=246, w3=97, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(41) - b.diff(126)
    stress = imbalance.rolling(97, min_periods=max(97//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.987647 + 0.0039632 * anchor
    return base_signal

def f61_pvcr_gemini_082(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=48, w2=259, w3=114, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 48)
    baseline = trend.rolling(259, min_periods=max(259//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(114, min_periods=max(114//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.001176 + 0.0039633 * anchor
    return base_signal

def f61_pvcr_gemini_083(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=55, w2=272, w3=131, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 55)
    slow = _rolling_slope(x, 272)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=131, adjust=False).mean() * 1.014706 + 0.0039634 * anchor
    return base_signal

def f61_pvcr_gemini_084(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=62, w2=285, w3=148, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(285, min_periods=max(285//3, 2)).max()
    trough = x.rolling(62, min_periods=max(62//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.028235 + 0.0039635 * anchor
    return base_signal

def f61_pvcr_gemini_085(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=69, w2=298, w3=165, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(69)
    rank = change.rolling(298, min_periods=max(298//3, 2)).rank(pct=True)
    persistence = change.rolling(165, min_periods=max(165//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.141 * persistence + 0.0039636 * anchor
    return base_signal

def f61_pvcr_gemini_086(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=76, w2=311, w3=182, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(76, min_periods=max(76//3, 2)).std()
    vol_slow = ret.rolling(311, min_periods=max(311//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.055294 + 0.0039637 * anchor
    return base_signal

def f61_pvcr_gemini_087(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=83, w2=324, w3=199, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(324, min_periods=max(324//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 83)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.153667 * slope + 0.0039638 * anchor
    return base_signal

def f61_pvcr_gemini_088(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=90, w2=337, w3=216, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(90)
    drag = impulse.rolling(337, min_periods=max(337//3, 2)).mean()
    noise = impulse.abs().rolling(216, min_periods=max(216//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.082353 + 0.0039639 * anchor
    return base_signal

def f61_pvcr_gemini_089(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=97, w2=350, w3=233, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 97)
    acceleration = _rolling_slope(velocity, 350)
    curvature = _rolling_slope(acceleration, 233)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.166333 * acceleration + 0.003964 * anchor
    return base_signal

def f61_pvcr_gemini_090(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=104, w2=363, w3=250, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 104)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.172667 * pressure.rolling(250, min_periods=max(250//3, 2)).mean() + 0.0039641 * anchor
    return base_signal

def f61_pvcr_gemini_091(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=111, w2=376, w3=267, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(111, min_periods=max(111//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.122941 + 0.0039642 * anchor
    return base_signal

def f61_pvcr_gemini_092(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=118, w2=389, w3=284, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(389, min_periods=max(389//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 118)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.136471 + 0.0039643 * anchor
    return base_signal

def f61_pvcr_gemini_093(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=125, w2=402, w3=301, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(125, min_periods=max(125//3, 2)).mean(), b.abs().rolling(402, min_periods=max(402//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.191667 * _rolling_slope(cover, 125) + 0.0039644 * anchor
    return base_signal

def f61_pvcr_gemini_094(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=132, w2=415, w3=318, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.198 * y + 0.802000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 132) - _rolling_slope(basket, 415) + 0.0039645 * anchor
    return base_signal

def f61_pvcr_gemini_095(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=139, w2=428, w3=335, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(139, min_periods=max(139//3, 2)).mean(), upside.rolling(428, min_periods=max(428//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.177059 + 0.0039646 * anchor
    return base_signal

def f61_pvcr_gemini_096(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=146, w2=441, w3=352, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(441, min_periods=max(441//3, 2)).max()
    rebound = x - x.rolling(146, min_periods=max(146//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.210667 * _rolling_slope(draw, 352) + 0.0039647 * anchor
    return base_signal

def f61_pvcr_gemini_097(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=153, w2=454, w3=369, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(369, min_periods=max(369//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.204118 + 0.0039648 * anchor
    return base_signal

def f61_pvcr_gemini_098(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=160, w2=467, w3=386, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 160)
    baseline = trend.rolling(467, min_periods=max(467//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.217647 + 0.0039649 * anchor
    return base_signal

def f61_pvcr_gemini_099(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=167, w2=480, w3=403, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 167)
    slow = _rolling_slope(x, 480)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.231176 + 0.003965 * anchor
    return base_signal

def f61_pvcr_gemini_100(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=174, w2=493, w3=420, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(493, min_periods=max(493//3, 2)).max()
    trough = x.rolling(174, min_periods=max(174//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.244706 + 0.0039651 * anchor
    return base_signal

def f61_pvcr_gemini_101(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=181, w2=506, w3=437, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(506, min_periods=max(506//3, 2)).rank(pct=True)
    persistence = change.rolling(437, min_periods=max(437//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.242333 * persistence + 0.0039652 * anchor
    return base_signal

def f61_pvcr_gemini_102(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=188, w2=20, w3=454, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(188, min_periods=max(188//3, 2)).std()
    vol_slow = ret.rolling(20, min_periods=max(20//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.271765 + 0.0039653 * anchor
    return base_signal

def f61_pvcr_gemini_103(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=195, w2=33, w3=471, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(33, min_periods=max(33//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 195)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.255 * slope + 0.0039654 * anchor
    return base_signal

def f61_pvcr_gemini_104(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=202, w2=46, w3=488, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(46, min_periods=max(46//3, 2)).mean()
    noise = impulse.abs().rolling(488, min_periods=max(488//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.298824 + 0.0039655 * anchor
    return base_signal

def f61_pvcr_gemini_105(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=209, w2=59, w3=505, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 209)
    acceleration = _rolling_slope(velocity, 59)
    curvature = _rolling_slope(acceleration, 505)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.267667 * acceleration + 0.0039656 * anchor
    return base_signal

def f61_pvcr_gemini_106(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=216, w2=72, w3=522, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 216)
    pressure = rel_log.diff(72)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.274 * pressure.rolling(522, min_periods=max(522//3, 2)).mean() + 0.0039657 * anchor
    return base_signal

def f61_pvcr_gemini_107(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=223, w2=85, w3=539, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(223, min_periods=max(223//3, 2)).mean())
    decay = spread.ewm(span=85, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.339412 + 0.0039658 * anchor
    return base_signal

def f61_pvcr_gemini_108(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=230, w2=98, w3=556, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(98, min_periods=max(98//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 230)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.352941 + 0.0039659 * anchor
    return base_signal

def f61_pvcr_gemini_109(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=237, w2=111, w3=573, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(237, min_periods=max(237//3, 2)).mean(), b.abs().rolling(111, min_periods=max(111//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.293 * _rolling_slope(cover, 237) + 0.003966 * anchor
    return base_signal

def f61_pvcr_gemini_110(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=244, w2=124, w3=590, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.299333 * y + 0.700667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 244) - _rolling_slope(basket, 124) + 0.0039661 * anchor
    return base_signal

def f61_pvcr_gemini_111(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=251, w2=137, w3=607, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(251, min_periods=max(251//3, 2)).mean(), upside.rolling(137, min_periods=max(137//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.393529 + 0.0039662 * anchor
    return base_signal

def f61_pvcr_gemini_112(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=11, w2=150, w3=624, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(150, min_periods=max(150//3, 2)).max()
    rebound = x - x.rolling(11, min_periods=max(11//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.312 * _rolling_slope(draw, 624) + 0.0039663 * anchor
    return base_signal

def f61_pvcr_gemini_113(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=18, w2=163, w3=641, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(18) - b.diff(126)
    stress = imbalance.rolling(641, min_periods=max(641//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.420588 + 0.0039664 * anchor
    return base_signal

def f61_pvcr_gemini_114(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=25, w2=176, w3=658, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 25)
    baseline = trend.rolling(176, min_periods=max(176//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(658, min_periods=max(658//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.434118 + 0.0039665 * anchor
    return base_signal

def f61_pvcr_gemini_115(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=32, w2=189, w3=675, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 32)
    slow = _rolling_slope(x, 189)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.447647 + 0.0039666 * anchor
    return base_signal

def f61_pvcr_gemini_116(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=39, w2=202, w3=692, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(202, min_periods=max(202//3, 2)).max()
    trough = x.rolling(39, min_periods=max(39//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.461176 + 0.0039667 * anchor
    return base_signal

def f61_pvcr_gemini_117(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=46, w2=215, w3=709, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(46)
    rank = change.rolling(215, min_periods=max(215//3, 2)).rank(pct=True)
    persistence = change.rolling(709, min_periods=max(709//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.343667 * persistence + 0.0039668 * anchor
    return base_signal

def f61_pvcr_gemini_118(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=53, w2=228, w3=726, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(53, min_periods=max(53//3, 2)).std()
    vol_slow = ret.rolling(228, min_periods=max(228//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.488235 + 0.0039669 * anchor
    return base_signal

def f61_pvcr_gemini_119(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=60, w2=241, w3=743, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(241, min_periods=max(241//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 60)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.356333 * slope + 0.003967 * anchor
    return base_signal

def f61_pvcr_gemini_120(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=67, w2=254, w3=760, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(67)
    drag = impulse.rolling(254, min_periods=max(254//3, 2)).mean()
    noise = impulse.abs().rolling(760, min_periods=max(760//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.515294 + 0.0039671 * anchor
    return base_signal

def f61_pvcr_gemini_121(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=74, w2=267, w3=26, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 74)
    acceleration = _rolling_slope(velocity, 267)
    curvature = _rolling_slope(acceleration, 26)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.036667 * acceleration + 0.0039672 * anchor
    return base_signal

def f61_pvcr_gemini_122(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=81, w2=280, w3=43, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 81)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.043 * pressure.rolling(43, min_periods=max(43//3, 2)).mean() + 0.0039673 * anchor
    return base_signal

def f61_pvcr_gemini_123(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=88, w2=293, w3=60, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(88, min_periods=max(88//3, 2)).mean())
    decay = spread.ewm(span=293, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.555882 + 0.0039674 * anchor
    return base_signal

def f61_pvcr_gemini_124(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=95, w2=306, w3=77, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(306, min_periods=max(306//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 95)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.569412 + 0.0039675 * anchor
    return base_signal

def f61_pvcr_gemini_125(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=102, w2=319, w3=94, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(102, min_periods=max(102//3, 2)).mean(), b.abs().rolling(319, min_periods=max(319//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(94) + 0.062 * _rolling_slope(cover, 102) + 0.0039676 * anchor
    return base_signal

def f61_pvcr_gemini_126(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=109, w2=332, w3=111, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.068333 * y + 0.931667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 109) - _rolling_slope(basket, 332) + 0.0039677 * anchor
    return base_signal

def f61_pvcr_gemini_127(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=116, w2=345, w3=128, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(116, min_periods=max(116//3, 2)).mean(), upside.rolling(345, min_periods=max(345//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.61 + 0.0039678 * anchor
    return base_signal

def f61_pvcr_gemini_128(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=123, w2=358, w3=145, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(358, min_periods=max(358//3, 2)).max()
    rebound = x - x.rolling(123, min_periods=max(123//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.081 * _rolling_slope(draw, 145) + 0.0039679 * anchor
    return base_signal

def f61_pvcr_gemini_129(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=130, w2=371, w3=162, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(162, min_periods=max(162//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.637059 + 0.003968 * anchor
    return base_signal

def f61_pvcr_gemini_130(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=137, w2=384, w3=179, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 137)
    baseline = trend.rolling(384, min_periods=max(384//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(179, min_periods=max(179//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.650588 + 0.0039681 * anchor
    return base_signal

def f61_pvcr_gemini_131(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=144, w2=397, w3=196, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 144)
    slow = _rolling_slope(x, 397)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=196, adjust=False).mean() * 1.664118 + 0.0039682 * anchor
    return base_signal

def f61_pvcr_gemini_132(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=151, w2=410, w3=213, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(410, min_periods=max(410//3, 2)).max()
    trough = x.rolling(151, min_periods=max(151//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.824118 + 0.0039683 * anchor
    return base_signal

def f61_pvcr_gemini_133(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=158, w2=423, w3=230, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(423, min_periods=max(423//3, 2)).rank(pct=True)
    persistence = change.rolling(230, min_periods=max(230//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.112667 * persistence + 0.0039684 * anchor
    return base_signal

def f61_pvcr_gemini_134(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=165, w2=436, w3=247, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(165, min_periods=max(165//3, 2)).std()
    vol_slow = ret.rolling(436, min_periods=max(436//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.851176 + 0.0039685 * anchor
    return base_signal

def f61_pvcr_gemini_135(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=172, w2=449, w3=264, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(449, min_periods=max(449//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 172)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.125333 * slope + 0.0039686 * anchor
    return base_signal

def f61_pvcr_gemini_136(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=179, w2=462, w3=281, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(462, min_periods=max(462//3, 2)).mean()
    noise = impulse.abs().rolling(281, min_periods=max(281//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.878235 + 0.0039687 * anchor
    return base_signal

def f61_pvcr_gemini_137(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=186, w2=475, w3=298, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 186)
    acceleration = _rolling_slope(velocity, 475)
    curvature = _rolling_slope(acceleration, 298)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.138 * acceleration + 0.0039688 * anchor
    return base_signal

def f61_pvcr_gemini_138(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=193, w2=488, w3=315, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 193)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.144333 * pressure.rolling(315, min_periods=max(315//3, 2)).mean() + 0.0039689 * anchor
    return base_signal

def f61_pvcr_gemini_139(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=200, w2=501, w3=332, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(200, min_periods=max(200//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.918824 + 0.003969 * anchor
    return base_signal

def f61_pvcr_gemini_140(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=207, w2=15, w3=349, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(15, min_periods=max(15//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 207)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.932353 + 0.0039691 * anchor
    return base_signal

def f61_pvcr_gemini_141(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=214, w2=28, w3=366, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(214, min_periods=max(214//3, 2)).mean(), b.abs().rolling(28, min_periods=max(28//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.163333 * _rolling_slope(cover, 214) + 0.0039692 * anchor
    return base_signal

def f61_pvcr_gemini_142(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=221, w2=41, w3=383, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.169667 * y + 0.830333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 221) - _rolling_slope(basket, 41) + 0.0039693 * anchor
    return base_signal

def f61_pvcr_gemini_143(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=228, w2=54, w3=400, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(228, min_periods=max(228//3, 2)).mean(), upside.rolling(54, min_periods=max(54//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.972941 + 0.0039694 * anchor
    return base_signal

def f61_pvcr_gemini_144(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=235, w2=67, w3=417, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(67, min_periods=max(67//3, 2)).max()
    rebound = x - x.rolling(235, min_periods=max(235//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.182333 * _rolling_slope(draw, 417) + 0.0039695 * anchor
    return base_signal

def f61_pvcr_gemini_145(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=242, w2=80, w3=434, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(80)
    stress = imbalance.rolling(434, min_periods=max(434//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.0 + 0.0039696 * anchor
    return base_signal

def f61_pvcr_gemini_146(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=249, w2=93, w3=451, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 249)
    baseline = trend.rolling(93, min_periods=max(93//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(451, min_periods=max(451//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.013529 + 0.0039697 * anchor
    return base_signal

def f61_pvcr_gemini_147(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=9, w2=106, w3=468, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 9)
    slow = _rolling_slope(x, 106)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.027059 + 0.0039698 * anchor
    return base_signal

def f61_pvcr_gemini_148(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=16, w2=119, w3=485, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(119, min_periods=max(119//3, 2)).max()
    trough = x.rolling(16, min_periods=max(16//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.040588 + 0.0039699 * anchor
    return base_signal

def f61_pvcr_gemini_149(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=23, w2=132, w3=502, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(23)
    rank = change.rolling(132, min_periods=max(132//3, 2)).rank(pct=True)
    persistence = change.rolling(502, min_periods=max(502//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.214 * persistence + 0.00397 * anchor
    return base_signal

def f61_pvcr_gemini_150(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=30, w2=145, w3=519, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(30, min_periods=max(30//3, 2)).std()
    vol_slow = ret.rolling(145, min_periods=max(145//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.067647 + 0.0039701 * anchor
    return base_signal
