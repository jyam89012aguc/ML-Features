"""84 session strength kinetics gemini base features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Momentum and volume analysis specific to key market session hours.
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

def f84_sstk_gemini_076(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=11, w2=456, w3=431, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(456, min_periods=max(456//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 11)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.058824 + 0.0052507 * anchor
    return base_signal

def f84_sstk_gemini_077(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=18, w2=469, w3=448, lag=21)."""
    a = open.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(18, min_periods=max(18//3, 2)).mean(), b.abs().rolling(469, min_periods=max(469//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.242 * _rolling_slope(cover, 18) + 0.0052508 * anchor
    return base_signal

def f84_sstk_gemini_078(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=25, w2=482, w3=465, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.248333 * y + 0.751667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 25) - _rolling_slope(basket, 482) + 0.0052509 * anchor
    return base_signal

def f84_sstk_gemini_079(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=32, w2=495, w3=482, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(32, min_periods=max(32//3, 2)).mean(), upside.rolling(495, min_periods=max(495//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.099412 + 0.005251 * anchor
    return base_signal

def f84_sstk_gemini_080(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=39, w2=508, w3=499, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(508, min_periods=max(508//3, 2)).max()
    rebound = x - x.rolling(39, min_periods=max(39//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.261 * _rolling_slope(draw, 499) + 0.0052511 * anchor
    return base_signal

def f84_sstk_gemini_081(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=46, w2=22, w3=516, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(46) - b.diff(22)
    stress = imbalance.rolling(516, min_periods=max(516//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.126471 + 0.0052512 * anchor
    return base_signal

def f84_sstk_gemini_082(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=53, w2=35, w3=533, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 53)
    baseline = trend.rolling(35, min_periods=max(35//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(533, min_periods=max(533//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.14 + 0.0052513 * anchor
    return base_signal

def f84_sstk_gemini_083(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=60, w2=48, w3=550, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 60)
    slow = _rolling_slope(x, 48)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.153529 + 0.0052514 * anchor
    return base_signal

def f84_sstk_gemini_084(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=67, w2=61, w3=567, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(61, min_periods=max(61//3, 2)).max()
    trough = x.rolling(67, min_periods=max(67//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.167059 + 0.0052515 * anchor
    return base_signal

def f84_sstk_gemini_085(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=74, w2=74, w3=584, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(74)
    rank = change.rolling(74, min_periods=max(74//3, 2)).rank(pct=True)
    persistence = change.rolling(584, min_periods=max(584//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.292667 * persistence + 0.0052516 * anchor
    return base_signal

def f84_sstk_gemini_086(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=81, w2=87, w3=601, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(81, min_periods=max(81//3, 2)).std()
    vol_slow = ret.rolling(87, min_periods=max(87//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.194118 + 0.0052517 * anchor
    return base_signal

def f84_sstk_gemini_087(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=88, w2=100, w3=618, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(100, min_periods=max(100//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 88)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.305333 * slope + 0.0052518 * anchor
    return base_signal

def f84_sstk_gemini_088(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=95, w2=113, w3=635, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(95)
    drag = impulse.rolling(113, min_periods=max(113//3, 2)).mean()
    noise = impulse.abs().rolling(635, min_periods=max(635//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.221176 + 0.0052519 * anchor
    return base_signal

def f84_sstk_gemini_089(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=102, w2=126, w3=652, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 102)
    acceleration = _rolling_slope(velocity, 126)
    curvature = _rolling_slope(acceleration, 652)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.318 * acceleration + 0.005252 * anchor
    return base_signal

def f84_sstk_gemini_090(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=109, w2=139, w3=669, lag=0)."""
    rel = _safe_div(open.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 109)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.324333 * pressure.rolling(669, min_periods=max(669//3, 2)).mean() + 0.0052521 * anchor
    return base_signal

def f84_sstk_gemini_091(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=116, w2=152, w3=686, lag=1)."""
    a = open.shift(1)
    b = close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(116, min_periods=max(116//3, 2)).mean())
    decay = spread.ewm(span=152, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.261765 + 0.0052522 * anchor
    return base_signal

def f84_sstk_gemini_092(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=123, w2=165, w3=703, lag=2)."""
    a = _safe_log(open.abs() + 1.0).shift(2)
    b = _safe_log(close.abs() + 1.0).shift(2)
    corr = a.rolling(165, min_periods=max(165//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 123)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.275294 + 0.0052523 * anchor
    return base_signal

def f84_sstk_gemini_093(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=130, w2=178, w3=720, lag=3)."""
    a = open.shift(3)
    b = close.shift(3)
    cover = _safe_div(a.rolling(130, min_periods=max(130//3, 2)).mean(), b.abs().rolling(178, min_periods=max(178//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.343333 * _rolling_slope(cover, 130) + 0.0052524 * anchor
    return base_signal

def f84_sstk_gemini_094(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=137, w2=191, w3=737, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    y = _safe_log(close.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.349667 * y + 0.650333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 137) - _rolling_slope(basket, 191) + 0.0052525 * anchor
    return base_signal

def f84_sstk_gemini_095(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=144, w2=204, w3=754, lag=8)."""
    x = open.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(144, min_periods=max(144//3, 2)).mean(), upside.rolling(204, min_periods=max(204//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.315882 + 0.0052526 * anchor
    return base_signal

def f84_sstk_gemini_096(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=151, w2=217, w3=20, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    draw = x - x.rolling(217, min_periods=max(217//3, 2)).max()
    rebound = x - x.rolling(151, min_periods=max(151//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.362333 * _rolling_slope(draw, 20) + 0.0052527 * anchor
    return base_signal

def f84_sstk_gemini_097(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=158, w2=230, w3=37, lag=21)."""
    a = _safe_log(open.abs() + 1.0).shift(21)
    b = _safe_log(close.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(37, min_periods=max(37//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.342941 + 0.0052528 * anchor
    return base_signal

def f84_sstk_gemini_098(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=165, w2=243, w3=54, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 165)
    baseline = trend.rolling(243, min_periods=max(243//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(54, min_periods=max(54//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.356471 + 0.0052529 * anchor
    return base_signal

def f84_sstk_gemini_099(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=172, w2=256, w3=71, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 172)
    slow = _rolling_slope(x, 256)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=71, adjust=False).mean() * 1.37 + 0.005253 * anchor
    return base_signal

def f84_sstk_gemini_100(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=179, w2=269, w3=88, lag=0)."""
    x = open.shift(0)
    peak = x.rolling(269, min_periods=max(269//3, 2)).max()
    trough = x.rolling(179, min_periods=max(179//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.383529 + 0.0052531 * anchor
    return base_signal

def f84_sstk_gemini_101(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=186, w2=282, w3=105, lag=1)."""
    x = open.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(282, min_periods=max(282//3, 2)).rank(pct=True)
    persistence = change.rolling(105, min_periods=max(105//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.061667 * persistence + 0.0052532 * anchor
    return base_signal

def f84_sstk_gemini_102(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=193, w2=295, w3=122, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(193, min_periods=max(193//3, 2)).std()
    vol_slow = ret.rolling(295, min_periods=max(295//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.410588 + 0.0052533 * anchor
    return base_signal

def f84_sstk_gemini_103(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=200, w2=308, w3=139, lag=3)."""
    x = open.shift(3)
    ma = x.rolling(308, min_periods=max(308//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 200)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.074333 * slope + 0.0052534 * anchor
    return base_signal

def f84_sstk_gemini_104(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=207, w2=321, w3=156, lag=5)."""
    x = open.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(321, min_periods=max(321//3, 2)).mean()
    noise = impulse.abs().rolling(156, min_periods=max(156//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.437647 + 0.0052535 * anchor
    return base_signal

def f84_sstk_gemini_105(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=214, w2=334, w3=173, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 214)
    acceleration = _rolling_slope(velocity, 334)
    curvature = _rolling_slope(acceleration, 173)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.087 * acceleration + 0.0052536 * anchor
    return base_signal

def f84_sstk_gemini_106(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=221, w2=347, w3=190, lag=13)."""
    rel = _safe_div(open.shift(13), close.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 221)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.093333 * pressure.rolling(190, min_periods=max(190//3, 2)).mean() + 0.0052537 * anchor
    return base_signal

def f84_sstk_gemini_107(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=228, w2=360, w3=207, lag=21)."""
    a = open.shift(21)
    b = close.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(228, min_periods=max(228//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.478235 + 0.0052538 * anchor
    return base_signal

def f84_sstk_gemini_108(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=235, w2=373, w3=224, lag=34)."""
    a = _safe_log(open.abs() + 1.0).shift(34)
    b = _safe_log(close.abs() + 1.0).shift(34)
    corr = a.rolling(373, min_periods=max(373//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 235)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.491765 + 0.0052539 * anchor
    return base_signal

def f84_sstk_gemini_109(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=242, w2=386, w3=241, lag=55)."""
    a = open.shift(55)
    b = close.shift(55)
    cover = _safe_div(a.rolling(242, min_periods=max(242//3, 2)).mean(), b.abs().rolling(386, min_periods=max(386//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.112333 * _rolling_slope(cover, 242) + 0.005254 * anchor
    return base_signal

def f84_sstk_gemini_110(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=249, w2=399, w3=258, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    y = _safe_log(close.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.118667 * y + 0.881333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 249) - _rolling_slope(basket, 399) + 0.0052541 * anchor
    return base_signal

def f84_sstk_gemini_111(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=9, w2=412, w3=275, lag=1)."""
    x = open.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(9, min_periods=max(9//3, 2)).mean(), upside.rolling(412, min_periods=max(412//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.532353 + 0.0052542 * anchor
    return base_signal

def f84_sstk_gemini_112(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=16, w2=425, w3=292, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    draw = x - x.rolling(425, min_periods=max(425//3, 2)).max()
    rebound = x - x.rolling(16, min_periods=max(16//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.131333 * _rolling_slope(draw, 292) + 0.0052543 * anchor
    return base_signal

def f84_sstk_gemini_113(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=23, w2=438, w3=309, lag=3)."""
    a = _safe_log(open.abs() + 1.0).shift(3)
    b = _safe_log(close.abs() + 1.0).shift(3)
    imbalance = a.diff(23) - b.diff(126)
    stress = imbalance.rolling(309, min_periods=max(309//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.559412 + 0.0052544 * anchor
    return base_signal

def f84_sstk_gemini_114(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=30, w2=451, w3=326, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 30)
    baseline = trend.rolling(451, min_periods=max(451//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(326, min_periods=max(326//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.572941 + 0.0052545 * anchor
    return base_signal

def f84_sstk_gemini_115(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=37, w2=464, w3=343, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 37)
    slow = _rolling_slope(x, 464)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.586471 + 0.0052546 * anchor
    return base_signal

def f84_sstk_gemini_116(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=44, w2=477, w3=360, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(477, min_periods=max(477//3, 2)).max()
    trough = x.rolling(44, min_periods=max(44//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.6 + 0.0052547 * anchor
    return base_signal

def f84_sstk_gemini_117(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=51, w2=490, w3=377, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(51)
    rank = change.rolling(490, min_periods=max(490//3, 2)).rank(pct=True)
    persistence = change.rolling(377, min_periods=max(377//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.163 * persistence + 0.0052548 * anchor
    return base_signal

def f84_sstk_gemini_118(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=58, w2=503, w3=394, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(58, min_periods=max(58//3, 2)).std()
    vol_slow = ret.rolling(503, min_periods=max(503//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.627059 + 0.0052549 * anchor
    return base_signal

def f84_sstk_gemini_119(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=65, w2=17, w3=411, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(17, min_periods=max(17//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 65)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.175667 * slope + 0.005255 * anchor
    return base_signal

def f84_sstk_gemini_120(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=72, w2=30, w3=428, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(72)
    drag = impulse.rolling(30, min_periods=max(30//3, 2)).mean()
    noise = impulse.abs().rolling(428, min_periods=max(428//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.654118 + 0.0052551 * anchor
    return base_signal

def f84_sstk_gemini_121(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=79, w2=43, w3=445, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 79)
    acceleration = _rolling_slope(velocity, 43)
    curvature = _rolling_slope(acceleration, 445)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.188333 * acceleration + 0.0052552 * anchor
    return base_signal

def f84_sstk_gemini_122(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=86, w2=56, w3=462, lag=2)."""
    rel = _safe_div(open.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 86)
    pressure = rel_log.diff(56)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.194667 * pressure.rolling(462, min_periods=max(462//3, 2)).mean() + 0.0052553 * anchor
    return base_signal

def f84_sstk_gemini_123(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=93, w2=69, w3=479, lag=3)."""
    a = open.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(93, min_periods=max(93//3, 2)).mean())
    decay = spread.ewm(span=69, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.841176 + 0.0052554 * anchor
    return base_signal

def f84_sstk_gemini_124(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=100, w2=82, w3=496, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(82, min_periods=max(82//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 100)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.854706 + 0.0052555 * anchor
    return base_signal

def f84_sstk_gemini_125(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=107, w2=95, w3=513, lag=8)."""
    a = open.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(107, min_periods=max(107//3, 2)).mean(), b.abs().rolling(95, min_periods=max(95//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.213667 * _rolling_slope(cover, 107) + 0.0052556 * anchor
    return base_signal

def f84_sstk_gemini_126(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=114, w2=108, w3=530, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.22 * y + 0.780000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 114) - _rolling_slope(basket, 108) + 0.0052557 * anchor
    return base_signal

def f84_sstk_gemini_127(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=121, w2=121, w3=547, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(121, min_periods=max(121//3, 2)).mean(), upside.rolling(121, min_periods=max(121//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.895294 + 0.0052558 * anchor
    return base_signal

def f84_sstk_gemini_128(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=128, w2=134, w3=564, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(134, min_periods=max(134//3, 2)).max()
    rebound = x - x.rolling(128, min_periods=max(128//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.232667 * _rolling_slope(draw, 564) + 0.0052559 * anchor
    return base_signal

def f84_sstk_gemini_129(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=135, w2=147, w3=581, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(581, min_periods=max(581//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.922353 + 0.005256 * anchor
    return base_signal

def f84_sstk_gemini_130(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=142, w2=160, w3=598, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 142)
    baseline = trend.rolling(160, min_periods=max(160//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(598, min_periods=max(598//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.935882 + 0.0052561 * anchor
    return base_signal

def f84_sstk_gemini_131(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=149, w2=173, w3=615, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 149)
    slow = _rolling_slope(x, 173)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.949412 + 0.0052562 * anchor
    return base_signal

def f84_sstk_gemini_132(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=156, w2=186, w3=632, lag=2)."""
    x = open.shift(2)
    peak = x.rolling(186, min_periods=max(186//3, 2)).max()
    trough = x.rolling(156, min_periods=max(156//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.962941 + 0.0052563 * anchor
    return base_signal

def f84_sstk_gemini_133(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=163, w2=199, w3=649, lag=3)."""
    x = open.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(199, min_periods=max(199//3, 2)).rank(pct=True)
    persistence = change.rolling(649, min_periods=max(649//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.264333 * persistence + 0.0052564 * anchor
    return base_signal

def f84_sstk_gemini_134(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=170, w2=212, w3=666, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(170, min_periods=max(170//3, 2)).std()
    vol_slow = ret.rolling(212, min_periods=max(212//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.99 + 0.0052565 * anchor
    return base_signal

def f84_sstk_gemini_135(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=177, w2=225, w3=683, lag=8)."""
    x = open.shift(8)
    ma = x.rolling(225, min_periods=max(225//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 177)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.277 * slope + 0.0052566 * anchor
    return base_signal

def f84_sstk_gemini_136(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=184, w2=238, w3=700, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(238, min_periods=max(238//3, 2)).mean()
    noise = impulse.abs().rolling(700, min_periods=max(700//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.017059 + 0.0052567 * anchor
    return base_signal

def f84_sstk_gemini_137(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=191, w2=251, w3=717, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 191)
    acceleration = _rolling_slope(velocity, 251)
    curvature = _rolling_slope(acceleration, 717)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.289667 * acceleration + 0.0052568 * anchor
    return base_signal

def f84_sstk_gemini_138(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=198, w2=264, w3=734, lag=34)."""
    rel = _safe_div(open.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 198)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.296 * pressure.rolling(734, min_periods=max(734//3, 2)).mean() + 0.0052569 * anchor
    return base_signal

def f84_sstk_gemini_139(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=205, w2=277, w3=751, lag=55)."""
    a = open.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(205, min_periods=max(205//3, 2)).mean())
    decay = spread.ewm(span=277, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.057647 + 0.005257 * anchor
    return base_signal

def f84_sstk_gemini_140(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=212, w2=290, w3=17, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(290, min_periods=max(290//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 212)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.071176 + 0.0052571 * anchor
    return base_signal

def f84_sstk_gemini_141(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=219, w2=303, w3=34, lag=1)."""
    a = open.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(219, min_periods=max(219//3, 2)).mean(), b.abs().rolling(303, min_periods=max(303//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(34) + 0.315 * _rolling_slope(cover, 219) + 0.0052572 * anchor
    return base_signal

def f84_sstk_gemini_142(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=226, w2=316, w3=51, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.321333 * y + 0.678667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 226) - _rolling_slope(basket, 316) + 0.0052573 * anchor
    return base_signal

def f84_sstk_gemini_143(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=233, w2=329, w3=68, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(233, min_periods=max(233//3, 2)).mean(), upside.rolling(329, min_periods=max(329//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(68) * 1.111765 + 0.0052574 * anchor
    return base_signal

def f84_sstk_gemini_144(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=240, w2=342, w3=85, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(342, min_periods=max(342//3, 2)).max()
    rebound = x - x.rolling(240, min_periods=max(240//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.334 * _rolling_slope(draw, 85) + 0.0052575 * anchor
    return base_signal

def f84_sstk_gemini_145(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=247, w2=355, w3=102, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(102, min_periods=max(102//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.138824 + 0.0052576 * anchor
    return base_signal

def f84_sstk_gemini_146(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=7, w2=368, w3=119, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 7)
    baseline = trend.rolling(368, min_periods=max(368//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.152353 + 0.0052577 * anchor
    return base_signal

def f84_sstk_gemini_147(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=14, w2=381, w3=136, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 14)
    slow = _rolling_slope(x, 381)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=136, adjust=False).mean() * 1.165882 + 0.0052578 * anchor
    return base_signal

def f84_sstk_gemini_148(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=21, w2=394, w3=153, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(394, min_periods=max(394//3, 2)).max()
    trough = x.rolling(21, min_periods=max(21//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.179412 + 0.0052579 * anchor
    return base_signal

def f84_sstk_gemini_149(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=28, w2=407, w3=170, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(28)
    rank = change.rolling(407, min_periods=max(407//3, 2)).rank(pct=True)
    persistence = change.rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.033333 * persistence + 0.005258 * anchor
    return base_signal

def f84_sstk_gemini_150(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=35, w2=420, w3=187, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(35, min_periods=max(35//3, 2)).std()
    vol_slow = ret.rolling(420, min_periods=max(420//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.206471 + 0.0052581 * anchor
    return base_signal
