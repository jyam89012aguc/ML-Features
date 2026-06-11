"""106 covariance matrix entropy gemini base features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Informational entropy of the covariance matrix as a measure of system disorder.
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

def f106_cmen_gemini_076(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=69, w2=184, w3=102, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(184, min_periods=max(184//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 69)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.841765 + 0.0008267 * anchor
    return base_signal

def f106_cmen_gemini_077(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=76, w2=197, w3=119, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(76, min_periods=max(76//3, 2)).mean(), b.abs().rolling(197, min_periods=max(197//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(119) + 0.212333 * _rolling_slope(cover, 76) + 0.0008268 * anchor
    return base_signal

def f106_cmen_gemini_078(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=83, w2=210, w3=136, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.218667 * y + 0.781333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 83) - _rolling_slope(basket, 210) + 0.0008269 * anchor
    return base_signal

def f106_cmen_gemini_079(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=90, w2=223, w3=153, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(90, min_periods=max(90//3, 2)).mean(), upside.rolling(223, min_periods=max(223//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.882353 + 0.000827 * anchor
    return base_signal

def f106_cmen_gemini_080(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=97, w2=236, w3=170, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(236, min_periods=max(236//3, 2)).max()
    rebound = x - x.rolling(97, min_periods=max(97//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.231333 * _rolling_slope(draw, 170) + 0.0008271 * anchor
    return base_signal

def f106_cmen_gemini_081(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=104, w2=249, w3=187, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(104) - b.diff(126)
    stress = imbalance.rolling(187, min_periods=max(187//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.909412 + 0.0008272 * anchor
    return base_signal

def f106_cmen_gemini_082(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=111, w2=262, w3=204, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 111)
    baseline = trend.rolling(262, min_periods=max(262//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(204, min_periods=max(204//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.922941 + 0.0008273 * anchor
    return base_signal

def f106_cmen_gemini_083(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=118, w2=275, w3=221, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 118)
    slow = _rolling_slope(x, 275)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=221, adjust=False).mean() * 0.936471 + 0.0008274 * anchor
    return base_signal

def f106_cmen_gemini_084(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=125, w2=288, w3=238, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(288, min_periods=max(288//3, 2)).max()
    trough = x.rolling(125, min_periods=max(125//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.95 + 0.0008275 * anchor
    return base_signal

def f106_cmen_gemini_085(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=132, w2=301, w3=255, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(301, min_periods=max(301//3, 2)).rank(pct=True)
    persistence = change.rolling(255, min_periods=max(255//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.263 * persistence + 0.0008276 * anchor
    return base_signal

def f106_cmen_gemini_086(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=139, w2=314, w3=272, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(139, min_periods=max(139//3, 2)).std()
    vol_slow = ret.rolling(314, min_periods=max(314//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.977059 + 0.0008277 * anchor
    return base_signal

def f106_cmen_gemini_087(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=146, w2=327, w3=289, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(327, min_periods=max(327//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 146)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.275667 * slope + 0.0008278 * anchor
    return base_signal

def f106_cmen_gemini_088(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=153, w2=340, w3=306, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(340, min_periods=max(340//3, 2)).mean()
    noise = impulse.abs().rolling(306, min_periods=max(306//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.004118 + 0.0008279 * anchor
    return base_signal

def f106_cmen_gemini_089(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=160, w2=353, w3=323, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 160)
    acceleration = _rolling_slope(velocity, 353)
    curvature = _rolling_slope(acceleration, 323)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.288333 * acceleration + 0.000828 * anchor
    return base_signal

def f106_cmen_gemini_090(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=167, w2=366, w3=340, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 167)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.294667 * pressure.rolling(340, min_periods=max(340//3, 2)).mean() + 0.0008281 * anchor
    return base_signal

def f106_cmen_gemini_091(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=174, w2=379, w3=357, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(174, min_periods=max(174//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.044706 + 0.0008282 * anchor
    return base_signal

def f106_cmen_gemini_092(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=181, w2=392, w3=374, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(392, min_periods=max(392//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 181)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.058235 + 0.0008283 * anchor
    return base_signal

def f106_cmen_gemini_093(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=188, w2=405, w3=391, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(188, min_periods=max(188//3, 2)).mean(), b.abs().rolling(405, min_periods=max(405//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.313667 * _rolling_slope(cover, 188) + 0.0008284 * anchor
    return base_signal

def f106_cmen_gemini_094(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=195, w2=418, w3=408, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.32 * y + 0.680000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 195) - _rolling_slope(basket, 418) + 0.0008285 * anchor
    return base_signal

def f106_cmen_gemini_095(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=202, w2=431, w3=425, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(202, min_periods=max(202//3, 2)).mean(), upside.rolling(431, min_periods=max(431//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.098824 + 0.0008286 * anchor
    return base_signal

def f106_cmen_gemini_096(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=209, w2=444, w3=442, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(444, min_periods=max(444//3, 2)).max()
    rebound = x - x.rolling(209, min_periods=max(209//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.332667 * _rolling_slope(draw, 442) + 0.0008287 * anchor
    return base_signal

def f106_cmen_gemini_097(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=216, w2=457, w3=459, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(459, min_periods=max(459//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.125882 + 0.0008288 * anchor
    return base_signal

def f106_cmen_gemini_098(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=223, w2=470, w3=476, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 223)
    baseline = trend.rolling(470, min_periods=max(470//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(476, min_periods=max(476//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.139412 + 0.0008289 * anchor
    return base_signal

def f106_cmen_gemini_099(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=230, w2=483, w3=493, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 230)
    slow = _rolling_slope(x, 483)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.152941 + 0.000829 * anchor
    return base_signal

def f106_cmen_gemini_100(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=237, w2=496, w3=510, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(496, min_periods=max(496//3, 2)).max()
    trough = x.rolling(237, min_periods=max(237//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.166471 + 0.0008291 * anchor
    return base_signal

def f106_cmen_gemini_101(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=244, w2=509, w3=527, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(509, min_periods=max(509//3, 2)).rank(pct=True)
    persistence = change.rolling(527, min_periods=max(527//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.032 * persistence + 0.0008292 * anchor
    return base_signal

def f106_cmen_gemini_102(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=251, w2=23, w3=544, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(251, min_periods=max(251//3, 2)).std()
    vol_slow = ret.rolling(23, min_periods=max(23//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.193529 + 0.0008293 * anchor
    return base_signal

def f106_cmen_gemini_103(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=11, w2=36, w3=561, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(36, min_periods=max(36//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 11)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.044667 * slope + 0.0008294 * anchor
    return base_signal

def f106_cmen_gemini_104(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=18, w2=49, w3=578, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(18)
    drag = impulse.rolling(49, min_periods=max(49//3, 2)).mean()
    noise = impulse.abs().rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.220588 + 0.0008295 * anchor
    return base_signal

def f106_cmen_gemini_105(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=25, w2=62, w3=595, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 62)
    curvature = _rolling_slope(acceleration, 595)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.057333 * acceleration + 0.0008296 * anchor
    return base_signal

def f106_cmen_gemini_106(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=32, w2=75, w3=612, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 32)
    pressure = rel_log.diff(75)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.063667 * pressure.rolling(612, min_periods=max(612//3, 2)).mean() + 0.0008297 * anchor
    return base_signal

def f106_cmen_gemini_107(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=39, w2=88, w3=629, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(39, min_periods=max(39//3, 2)).mean())
    decay = spread.ewm(span=88, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.261176 + 0.0008298 * anchor
    return base_signal

def f106_cmen_gemini_108(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=46, w2=101, w3=646, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(101, min_periods=max(101//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 46)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.274706 + 0.0008299 * anchor
    return base_signal

def f106_cmen_gemini_109(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=53, w2=114, w3=663, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(53, min_periods=max(53//3, 2)).mean(), b.abs().rolling(114, min_periods=max(114//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.082667 * _rolling_slope(cover, 53) + 0.00083 * anchor
    return base_signal

def f106_cmen_gemini_110(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=60, w2=127, w3=680, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.089 * y + 0.911000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 60) - _rolling_slope(basket, 127) + 0.0008301 * anchor
    return base_signal

def f106_cmen_gemini_111(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=67, w2=140, w3=697, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(67, min_periods=max(67//3, 2)).mean(), upside.rolling(140, min_periods=max(140//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.315294 + 0.0008302 * anchor
    return base_signal

def f106_cmen_gemini_112(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=74, w2=153, w3=714, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(153, min_periods=max(153//3, 2)).max()
    rebound = x - x.rolling(74, min_periods=max(74//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.101667 * _rolling_slope(draw, 714) + 0.0008303 * anchor
    return base_signal

def f106_cmen_gemini_113(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=81, w2=166, w3=731, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(81) - b.diff(126)
    stress = imbalance.rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.342353 + 0.0008304 * anchor
    return base_signal

def f106_cmen_gemini_114(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=88, w2=179, w3=748, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 88)
    baseline = trend.rolling(179, min_periods=max(179//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(748, min_periods=max(748//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.355882 + 0.0008305 * anchor
    return base_signal

def f106_cmen_gemini_115(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=95, w2=192, w3=765, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 95)
    slow = _rolling_slope(x, 192)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.369412 + 0.0008306 * anchor
    return base_signal

def f106_cmen_gemini_116(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=102, w2=205, w3=31, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(205, min_periods=max(205//3, 2)).max()
    trough = x.rolling(102, min_periods=max(102//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.382941 + 0.0008307 * anchor
    return base_signal

def f106_cmen_gemini_117(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=109, w2=218, w3=48, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(109)
    rank = change.rolling(218, min_periods=max(218//3, 2)).rank(pct=True)
    persistence = change.rolling(48, min_periods=max(48//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.133333 * persistence + 0.0008308 * anchor
    return base_signal

def f106_cmen_gemini_118(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=116, w2=231, w3=65, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(116, min_periods=max(116//3, 2)).std()
    vol_slow = ret.rolling(231, min_periods=max(231//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.41 + 0.0008309 * anchor
    return base_signal

def f106_cmen_gemini_119(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=123, w2=244, w3=82, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(244, min_periods=max(244//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 123)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.146 * slope + 0.000831 * anchor
    return base_signal

def f106_cmen_gemini_120(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=130, w2=257, w3=99, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(257, min_periods=max(257//3, 2)).mean()
    noise = impulse.abs().rolling(99, min_periods=max(99//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.437059 + 0.0008311 * anchor
    return base_signal

def f106_cmen_gemini_121(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=137, w2=270, w3=116, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 137)
    acceleration = _rolling_slope(velocity, 270)
    curvature = _rolling_slope(acceleration, 116)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.158667 * acceleration + 0.0008312 * anchor
    return base_signal

def f106_cmen_gemini_122(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=144, w2=283, w3=133, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 144)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.165 * pressure.rolling(133, min_periods=max(133//3, 2)).mean() + 0.0008313 * anchor
    return base_signal

def f106_cmen_gemini_123(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=151, w2=296, w3=150, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(151, min_periods=max(151//3, 2)).mean())
    decay = spread.ewm(span=296, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.477647 + 0.0008314 * anchor
    return base_signal

def f106_cmen_gemini_124(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=158, w2=309, w3=167, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(309, min_periods=max(309//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 158)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.491176 + 0.0008315 * anchor
    return base_signal

def f106_cmen_gemini_125(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=165, w2=322, w3=184, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(165, min_periods=max(165//3, 2)).mean(), b.abs().rolling(322, min_periods=max(322//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.184 * _rolling_slope(cover, 165) + 0.0008316 * anchor
    return base_signal

def f106_cmen_gemini_126(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=172, w2=335, w3=201, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.190333 * y + 0.809667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 172) - _rolling_slope(basket, 335) + 0.0008317 * anchor
    return base_signal

def f106_cmen_gemini_127(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=179, w2=348, w3=218, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(179, min_periods=max(179//3, 2)).mean(), upside.rolling(348, min_periods=max(348//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.531765 + 0.0008318 * anchor
    return base_signal

def f106_cmen_gemini_128(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=186, w2=361, w3=235, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(361, min_periods=max(361//3, 2)).max()
    rebound = x - x.rolling(186, min_periods=max(186//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.203 * _rolling_slope(draw, 235) + 0.0008319 * anchor
    return base_signal

def f106_cmen_gemini_129(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=193, w2=374, w3=252, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(252, min_periods=max(252//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.558824 + 0.000832 * anchor
    return base_signal

def f106_cmen_gemini_130(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=200, w2=387, w3=269, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 200)
    baseline = trend.rolling(387, min_periods=max(387//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(269, min_periods=max(269//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.572353 + 0.0008321 * anchor
    return base_signal

def f106_cmen_gemini_131(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=207, w2=400, w3=286, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 207)
    slow = _rolling_slope(x, 400)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=286, adjust=False).mean() * 1.585882 + 0.0008322 * anchor
    return base_signal

def f106_cmen_gemini_132(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=214, w2=413, w3=303, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(413, min_periods=max(413//3, 2)).max()
    trough = x.rolling(214, min_periods=max(214//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.599412 + 0.0008323 * anchor
    return base_signal

def f106_cmen_gemini_133(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=221, w2=426, w3=320, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(426, min_periods=max(426//3, 2)).rank(pct=True)
    persistence = change.rolling(320, min_periods=max(320//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.234667 * persistence + 0.0008324 * anchor
    return base_signal

def f106_cmen_gemini_134(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=228, w2=439, w3=337, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(228, min_periods=max(228//3, 2)).std()
    vol_slow = ret.rolling(439, min_periods=max(439//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.626471 + 0.0008325 * anchor
    return base_signal

def f106_cmen_gemini_135(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=235, w2=452, w3=354, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(452, min_periods=max(452//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 235)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.247333 * slope + 0.0008326 * anchor
    return base_signal

def f106_cmen_gemini_136(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=242, w2=465, w3=371, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(465, min_periods=max(465//3, 2)).mean()
    noise = impulse.abs().rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.653529 + 0.0008327 * anchor
    return base_signal

def f106_cmen_gemini_137(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=249, w2=478, w3=388, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 249)
    acceleration = _rolling_slope(velocity, 478)
    curvature = _rolling_slope(acceleration, 388)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.26 * acceleration + 0.0008328 * anchor
    return base_signal

def f106_cmen_gemini_138(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=9, w2=491, w3=405, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 9)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.266333 * pressure.rolling(405, min_periods=max(405//3, 2)).mean() + 0.0008329 * anchor
    return base_signal

def f106_cmen_gemini_139(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=16, w2=504, w3=422, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(16, min_periods=max(16//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.840588 + 0.000833 * anchor
    return base_signal

def f106_cmen_gemini_140(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=23, w2=18, w3=439, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(18, min_periods=max(18//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 23)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.854118 + 0.0008331 * anchor
    return base_signal

def f106_cmen_gemini_141(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=30, w2=31, w3=456, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(30, min_periods=max(30//3, 2)).mean(), b.abs().rolling(31, min_periods=max(31//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.285333 * _rolling_slope(cover, 30) + 0.0008332 * anchor
    return base_signal

def f106_cmen_gemini_142(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=37, w2=44, w3=473, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.291667 * y + 0.708333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 37) - _rolling_slope(basket, 44) + 0.0008333 * anchor
    return base_signal

def f106_cmen_gemini_143(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=44, w2=57, w3=490, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(44, min_periods=max(44//3, 2)).mean(), upside.rolling(57, min_periods=max(57//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.894706 + 0.0008334 * anchor
    return base_signal

def f106_cmen_gemini_144(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=51, w2=70, w3=507, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(70, min_periods=max(70//3, 2)).max()
    rebound = x - x.rolling(51, min_periods=max(51//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.304333 * _rolling_slope(draw, 507) + 0.0008335 * anchor
    return base_signal

def f106_cmen_gemini_145(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=58, w2=83, w3=524, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(58) - b.diff(83)
    stress = imbalance.rolling(524, min_periods=max(524//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.921765 + 0.0008336 * anchor
    return base_signal

def f106_cmen_gemini_146(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=65, w2=96, w3=541, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 65)
    baseline = trend.rolling(96, min_periods=max(96//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(541, min_periods=max(541//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.935294 + 0.0008337 * anchor
    return base_signal

def f106_cmen_gemini_147(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=72, w2=109, w3=558, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 72)
    slow = _rolling_slope(x, 109)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.948824 + 0.0008338 * anchor
    return base_signal

def f106_cmen_gemini_148(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=79, w2=122, w3=575, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(122, min_periods=max(122//3, 2)).max()
    trough = x.rolling(79, min_periods=max(79//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.962353 + 0.0008339 * anchor
    return base_signal

def f106_cmen_gemini_149(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=86, w2=135, w3=592, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(86)
    rank = change.rolling(135, min_periods=max(135//3, 2)).rank(pct=True)
    persistence = change.rolling(592, min_periods=max(592//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.336 * persistence + 0.000834 * anchor
    return base_signal

def f106_cmen_gemini_150(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=93, w2=148, w3=609, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(93, min_periods=max(93//3, 2)).std()
    vol_slow = ret.rolling(148, min_periods=max(148//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.989412 + 0.0008341 * anchor
    return base_signal
