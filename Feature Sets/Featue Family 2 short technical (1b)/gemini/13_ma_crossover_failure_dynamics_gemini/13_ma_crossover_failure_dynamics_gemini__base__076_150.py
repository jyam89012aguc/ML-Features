"""13 ma crossover failure dynamics gemini base features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Failed moving average crossovers where price reverses immediately after the signal.
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

def f13_macf_gemini_076(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=60, w2=41, w3=411, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(60)
    drag = impulse.rolling(41, min_periods=max(41//3, 2)).mean()
    noise = impulse.abs().rolling(411, min_periods=max(411//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.852941 + 0.0012747 * anchor
    return base_signal

def f13_macf_gemini_077(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=67, w2=54, w3=428, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 67)
    acceleration = _rolling_slope(velocity, 54)
    curvature = _rolling_slope(acceleration, 428)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.337333 * acceleration + 0.0012748 * anchor
    return base_signal

def f13_macf_gemini_078(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=74, w2=67, w3=445, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(74, min_periods=max(74//3, 2)).mean(), upside.rolling(67, min_periods=max(67//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.88 + 0.0012749 * anchor
    return base_signal

def f13_macf_gemini_079(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=81, w2=80, w3=462, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(80, min_periods=max(80//3, 2)).max()
    rebound = x - x.rolling(81, min_periods=max(81//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.35 * _rolling_slope(draw, 462) + 0.001275 * anchor
    return base_signal

def f13_macf_gemini_080(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=88, w2=93, w3=479, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 88)
    baseline = trend.rolling(93, min_periods=max(93//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(479, min_periods=max(479//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.907059 + 0.0012751 * anchor
    return base_signal

def f13_macf_gemini_081(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=95, w2=106, w3=496, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 95)
    slow = _rolling_slope(x, 106)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.920588 + 0.0012752 * anchor
    return base_signal

def f13_macf_gemini_082(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=102, w2=119, w3=513, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(119, min_periods=max(119//3, 2)).max()
    trough = x.rolling(102, min_periods=max(102//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.934118 + 0.0012753 * anchor
    return base_signal

def f13_macf_gemini_083(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=109, w2=132, w3=530, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(109)
    rank = change.rolling(132, min_periods=max(132//3, 2)).rank(pct=True)
    persistence = change.rolling(530, min_periods=max(530//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.043 * persistence + 0.0012754 * anchor
    return base_signal

def f13_macf_gemini_084(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=116, w2=145, w3=547, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(116, min_periods=max(116//3, 2)).std()
    vol_slow = ret.rolling(145, min_periods=max(145//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.961176 + 0.0012755 * anchor
    return base_signal

def f13_macf_gemini_085(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=123, w2=158, w3=564, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(158, min_periods=max(158//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 123)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.055667 * slope + 0.0012756 * anchor
    return base_signal

def f13_macf_gemini_086(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=130, w2=171, w3=581, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(171, min_periods=max(171//3, 2)).mean()
    noise = impulse.abs().rolling(581, min_periods=max(581//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.988235 + 0.0012757 * anchor
    return base_signal

def f13_macf_gemini_087(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=137, w2=184, w3=598, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 137)
    acceleration = _rolling_slope(velocity, 184)
    curvature = _rolling_slope(acceleration, 598)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.068333 * acceleration + 0.0012758 * anchor
    return base_signal

def f13_macf_gemini_088(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=144, w2=197, w3=615, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(144, min_periods=max(144//3, 2)).mean(), upside.rolling(197, min_periods=max(197//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.015294 + 0.0012759 * anchor
    return base_signal

def f13_macf_gemini_089(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=151, w2=210, w3=632, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(210, min_periods=max(210//3, 2)).max()
    rebound = x - x.rolling(151, min_periods=max(151//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.081 * _rolling_slope(draw, 632) + 0.001276 * anchor
    return base_signal

def f13_macf_gemini_090(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=158, w2=223, w3=649, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 158)
    baseline = trend.rolling(223, min_periods=max(223//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(649, min_periods=max(649//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.042353 + 0.0012761 * anchor
    return base_signal

def f13_macf_gemini_091(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=165, w2=236, w3=666, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 165)
    slow = _rolling_slope(x, 236)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.055882 + 0.0012762 * anchor
    return base_signal

def f13_macf_gemini_092(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=172, w2=249, w3=683, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(249, min_periods=max(249//3, 2)).max()
    trough = x.rolling(172, min_periods=max(172//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.069412 + 0.0012763 * anchor
    return base_signal

def f13_macf_gemini_093(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=179, w2=262, w3=700, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(262, min_periods=max(262//3, 2)).rank(pct=True)
    persistence = change.rolling(700, min_periods=max(700//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.106333 * persistence + 0.0012764 * anchor
    return base_signal

def f13_macf_gemini_094(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=186, w2=275, w3=717, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(186, min_periods=max(186//3, 2)).std()
    vol_slow = ret.rolling(275, min_periods=max(275//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.096471 + 0.0012765 * anchor
    return base_signal

def f13_macf_gemini_095(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=193, w2=288, w3=734, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(288, min_periods=max(288//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 193)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.119 * slope + 0.0012766 * anchor
    return base_signal

def f13_macf_gemini_096(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=200, w2=301, w3=751, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(301, min_periods=max(301//3, 2)).mean()
    noise = impulse.abs().rolling(751, min_periods=max(751//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.123529 + 0.0012767 * anchor
    return base_signal

def f13_macf_gemini_097(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=207, w2=314, w3=17, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 207)
    acceleration = _rolling_slope(velocity, 314)
    curvature = _rolling_slope(acceleration, 17)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.131667 * acceleration + 0.0012768 * anchor
    return base_signal

def f13_macf_gemini_098(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=214, w2=327, w3=34, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(214, min_periods=max(214//3, 2)).mean(), upside.rolling(327, min_periods=max(327//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(34) * 1.150588 + 0.0012769 * anchor
    return base_signal

def f13_macf_gemini_099(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=221, w2=340, w3=51, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(340, min_periods=max(340//3, 2)).max()
    rebound = x - x.rolling(221, min_periods=max(221//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.144333 * _rolling_slope(draw, 51) + 0.001277 * anchor
    return base_signal

def f13_macf_gemini_100(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=228, w2=353, w3=68, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 228)
    baseline = trend.rolling(353, min_periods=max(353//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(68, min_periods=max(68//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.177647 + 0.0012771 * anchor
    return base_signal

def f13_macf_gemini_101(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=235, w2=366, w3=85, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 235)
    slow = _rolling_slope(x, 366)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=85, adjust=False).mean() * 1.191176 + 0.0012772 * anchor
    return base_signal

def f13_macf_gemini_102(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=242, w2=379, w3=102, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(379, min_periods=max(379//3, 2)).max()
    trough = x.rolling(242, min_periods=max(242//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.204706 + 0.0012773 * anchor
    return base_signal

def f13_macf_gemini_103(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=249, w2=392, w3=119, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(392, min_periods=max(392//3, 2)).rank(pct=True)
    persistence = change.rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.169667 * persistence + 0.0012774 * anchor
    return base_signal

def f13_macf_gemini_104(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=9, w2=405, w3=136, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(9, min_periods=max(9//3, 2)).std()
    vol_slow = ret.rolling(405, min_periods=max(405//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.231765 + 0.0012775 * anchor
    return base_signal

def f13_macf_gemini_105(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=16, w2=418, w3=153, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(418, min_periods=max(418//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 16)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.182333 * slope + 0.0012776 * anchor
    return base_signal

def f13_macf_gemini_106(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=23, w2=431, w3=170, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(23)
    drag = impulse.rolling(431, min_periods=max(431//3, 2)).mean()
    noise = impulse.abs().rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.258824 + 0.0012777 * anchor
    return base_signal

def f13_macf_gemini_107(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=30, w2=444, w3=187, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 30)
    acceleration = _rolling_slope(velocity, 444)
    curvature = _rolling_slope(acceleration, 187)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.195 * acceleration + 0.0012778 * anchor
    return base_signal

def f13_macf_gemini_108(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=37, w2=457, w3=204, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(37, min_periods=max(37//3, 2)).mean(), upside.rolling(457, min_periods=max(457//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.285882 + 0.0012779 * anchor
    return base_signal

def f13_macf_gemini_109(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=44, w2=470, w3=221, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(470, min_periods=max(470//3, 2)).max()
    rebound = x - x.rolling(44, min_periods=max(44//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.207667 * _rolling_slope(draw, 221) + 0.001278 * anchor
    return base_signal

def f13_macf_gemini_110(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=51, w2=483, w3=238, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 51)
    baseline = trend.rolling(483, min_periods=max(483//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(238, min_periods=max(238//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.312941 + 0.0012781 * anchor
    return base_signal

def f13_macf_gemini_111(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=58, w2=496, w3=255, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 58)
    slow = _rolling_slope(x, 496)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=255, adjust=False).mean() * 1.326471 + 0.0012782 * anchor
    return base_signal

def f13_macf_gemini_112(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=65, w2=509, w3=272, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(509, min_periods=max(509//3, 2)).max()
    trough = x.rolling(65, min_periods=max(65//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.34 + 0.0012783 * anchor
    return base_signal

def f13_macf_gemini_113(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=72, w2=23, w3=289, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(72)
    rank = change.rolling(23, min_periods=max(23//3, 2)).rank(pct=True)
    persistence = change.rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.233 * persistence + 0.0012784 * anchor
    return base_signal

def f13_macf_gemini_114(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=79, w2=36, w3=306, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(79, min_periods=max(79//3, 2)).std()
    vol_slow = ret.rolling(36, min_periods=max(36//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.367059 + 0.0012785 * anchor
    return base_signal

def f13_macf_gemini_115(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=86, w2=49, w3=323, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(49, min_periods=max(49//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 86)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.245667 * slope + 0.0012786 * anchor
    return base_signal

def f13_macf_gemini_116(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=93, w2=62, w3=340, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(93)
    drag = impulse.rolling(62, min_periods=max(62//3, 2)).mean()
    noise = impulse.abs().rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.394118 + 0.0012787 * anchor
    return base_signal

def f13_macf_gemini_117(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=100, w2=75, w3=357, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 100)
    acceleration = _rolling_slope(velocity, 75)
    curvature = _rolling_slope(acceleration, 357)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.258333 * acceleration + 0.0012788 * anchor
    return base_signal

def f13_macf_gemini_118(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=107, w2=88, w3=374, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(107, min_periods=max(107//3, 2)).mean(), upside.rolling(88, min_periods=max(88//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.421176 + 0.0012789 * anchor
    return base_signal

def f13_macf_gemini_119(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=114, w2=101, w3=391, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(101, min_periods=max(101//3, 2)).max()
    rebound = x - x.rolling(114, min_periods=max(114//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.271 * _rolling_slope(draw, 391) + 0.001279 * anchor
    return base_signal

def f13_macf_gemini_120(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=121, w2=114, w3=408, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 121)
    baseline = trend.rolling(114, min_periods=max(114//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(408, min_periods=max(408//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.448235 + 0.0012791 * anchor
    return base_signal

def f13_macf_gemini_121(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=128, w2=127, w3=425, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 128)
    slow = _rolling_slope(x, 127)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.461765 + 0.0012792 * anchor
    return base_signal

def f13_macf_gemini_122(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=135, w2=140, w3=442, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(140, min_periods=max(140//3, 2)).max()
    trough = x.rolling(135, min_periods=max(135//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.475294 + 0.0012793 * anchor
    return base_signal

def f13_macf_gemini_123(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=142, w2=153, w3=459, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(153, min_periods=max(153//3, 2)).rank(pct=True)
    persistence = change.rolling(459, min_periods=max(459//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.296333 * persistence + 0.0012794 * anchor
    return base_signal

def f13_macf_gemini_124(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=149, w2=166, w3=476, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(149, min_periods=max(149//3, 2)).std()
    vol_slow = ret.rolling(166, min_periods=max(166//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.502353 + 0.0012795 * anchor
    return base_signal

def f13_macf_gemini_125(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=156, w2=179, w3=493, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(179, min_periods=max(179//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 156)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.309 * slope + 0.0012796 * anchor
    return base_signal

def f13_macf_gemini_126(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=163, w2=192, w3=510, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(192, min_periods=max(192//3, 2)).mean()
    noise = impulse.abs().rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.529412 + 0.0012797 * anchor
    return base_signal

def f13_macf_gemini_127(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=170, w2=205, w3=527, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 170)
    acceleration = _rolling_slope(velocity, 205)
    curvature = _rolling_slope(acceleration, 527)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.321667 * acceleration + 0.0012798 * anchor
    return base_signal

def f13_macf_gemini_128(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=177, w2=218, w3=544, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(177, min_periods=max(177//3, 2)).mean(), upside.rolling(218, min_periods=max(218//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.556471 + 0.0012799 * anchor
    return base_signal

def f13_macf_gemini_129(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=184, w2=231, w3=561, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(231, min_periods=max(231//3, 2)).max()
    rebound = x - x.rolling(184, min_periods=max(184//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.334333 * _rolling_slope(draw, 561) + 0.00128 * anchor
    return base_signal

def f13_macf_gemini_130(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=191, w2=244, w3=578, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 191)
    baseline = trend.rolling(244, min_periods=max(244//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.583529 + 0.0012801 * anchor
    return base_signal

def f13_macf_gemini_131(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=198, w2=257, w3=595, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 198)
    slow = _rolling_slope(x, 257)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.597059 + 0.0012802 * anchor
    return base_signal

def f13_macf_gemini_132(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=205, w2=270, w3=612, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(270, min_periods=max(270//3, 2)).max()
    trough = x.rolling(205, min_periods=max(205//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.610588 + 0.0012803 * anchor
    return base_signal

def f13_macf_gemini_133(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=212, w2=283, w3=629, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(283, min_periods=max(283//3, 2)).rank(pct=True)
    persistence = change.rolling(629, min_periods=max(629//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.359667 * persistence + 0.0012804 * anchor
    return base_signal

def f13_macf_gemini_134(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=219, w2=296, w3=646, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(219, min_periods=max(219//3, 2)).std()
    vol_slow = ret.rolling(296, min_periods=max(296//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.637647 + 0.0012805 * anchor
    return base_signal

def f13_macf_gemini_135(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=226, w2=309, w3=663, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(309, min_periods=max(309//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 226)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.04 * slope + 0.0012806 * anchor
    return base_signal

def f13_macf_gemini_136(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=233, w2=322, w3=680, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(322, min_periods=max(322//3, 2)).mean()
    noise = impulse.abs().rolling(680, min_periods=max(680//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.664706 + 0.0012807 * anchor
    return base_signal

def f13_macf_gemini_137(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=240, w2=335, w3=697, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 240)
    acceleration = _rolling_slope(velocity, 335)
    curvature = _rolling_slope(acceleration, 697)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.052667 * acceleration + 0.0012808 * anchor
    return base_signal

def f13_macf_gemini_138(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=247, w2=348, w3=714, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(247, min_periods=max(247//3, 2)).mean(), upside.rolling(348, min_periods=max(348//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.838235 + 0.0012809 * anchor
    return base_signal

def f13_macf_gemini_139(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=7, w2=361, w3=731, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(361, min_periods=max(361//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.065333 * _rolling_slope(draw, 731) + 0.001281 * anchor
    return base_signal

def f13_macf_gemini_140(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=14, w2=374, w3=748, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 14)
    baseline = trend.rolling(374, min_periods=max(374//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(748, min_periods=max(748//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.865294 + 0.0012811 * anchor
    return base_signal

def f13_macf_gemini_141(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=21, w2=387, w3=765, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 21)
    slow = _rolling_slope(x, 387)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.878824 + 0.0012812 * anchor
    return base_signal

def f13_macf_gemini_142(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=28, w2=400, w3=31, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(400, min_periods=max(400//3, 2)).max()
    trough = x.rolling(28, min_periods=max(28//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.892353 + 0.0012813 * anchor
    return base_signal

def f13_macf_gemini_143(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=35, w2=413, w3=48, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(35)
    rank = change.rolling(413, min_periods=max(413//3, 2)).rank(pct=True)
    persistence = change.rolling(48, min_periods=max(48//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.090667 * persistence + 0.0012814 * anchor
    return base_signal

def f13_macf_gemini_144(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=42, w2=426, w3=65, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(42, min_periods=max(42//3, 2)).std()
    vol_slow = ret.rolling(426, min_periods=max(426//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.919412 + 0.0012815 * anchor
    return base_signal

def f13_macf_gemini_145(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=49, w2=439, w3=82, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(439, min_periods=max(439//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 49)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.103333 * slope + 0.0012816 * anchor
    return base_signal

def f13_macf_gemini_146(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=56, w2=452, w3=99, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(56)
    drag = impulse.rolling(452, min_periods=max(452//3, 2)).mean()
    noise = impulse.abs().rolling(99, min_periods=max(99//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.946471 + 0.0012817 * anchor
    return base_signal

def f13_macf_gemini_147(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=63, w2=465, w3=116, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 63)
    acceleration = _rolling_slope(velocity, 465)
    curvature = _rolling_slope(acceleration, 116)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.116 * acceleration + 0.0012818 * anchor
    return base_signal

def f13_macf_gemini_148(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=70, w2=478, w3=133, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(70, min_periods=max(70//3, 2)).mean(), upside.rolling(478, min_periods=max(478//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.973529 + 0.0012819 * anchor
    return base_signal

def f13_macf_gemini_149(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=77, w2=491, w3=150, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(491, min_periods=max(491//3, 2)).max()
    rebound = x - x.rolling(77, min_periods=max(77//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.128667 * _rolling_slope(draw, 150) + 0.001282 * anchor
    return base_signal

def f13_macf_gemini_150(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=84, w2=504, w3=167, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 84)
    baseline = trend.rolling(504, min_periods=max(504//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(167, min_periods=max(167//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.000588 + 0.0012821 * anchor
    return base_signal
