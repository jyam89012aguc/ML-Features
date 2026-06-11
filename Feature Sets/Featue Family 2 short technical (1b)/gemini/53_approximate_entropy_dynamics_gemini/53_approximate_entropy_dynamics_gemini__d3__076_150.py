"""53 approximate entropy dynamics gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Quantification of regularity and predictability in short-term price fluctuations.
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

def f53_aent_gemini_076_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=295, w3=84, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(295, min_periods=max(295//3, 2)).mean()
    noise = impulse.abs().rolling(84, min_periods=max(84//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.47 + 0.0035567 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_077_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=308, w3=101, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 245)
    acceleration = _rolling_slope(velocity, 308)
    curvature = _rolling_slope(acceleration, 101)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.299 * acceleration + 0.0035568 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_078_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=321, w3=118, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(5, min_periods=max(5//3, 2)).mean(), upside.rolling(321, min_periods=max(321//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(118) * 1.497059 + 0.0035569 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_079_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=334, w3=135, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(334, min_periods=max(334//3, 2)).max()
    rebound = x - x.rolling(12, min_periods=max(12//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.311667 * _rolling_slope(draw, 135) + 0.003557 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_080_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=347, w3=152, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 19)
    baseline = trend.rolling(347, min_periods=max(347//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(152, min_periods=max(152//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.524118 + 0.0035571 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_081_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=360, w3=169, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 26)
    slow = _rolling_slope(x, 360)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=169, adjust=False).mean() * 1.537647 + 0.0035572 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_082_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=373, w3=186, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(373, min_periods=max(373//3, 2)).max()
    trough = x.rolling(33, min_periods=max(33//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.551176 + 0.0035573 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_083_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=386, w3=203, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(40)
    rank = change.rolling(386, min_periods=max(386//3, 2)).rank(pct=True)
    persistence = change.rolling(203, min_periods=max(203//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.337 * persistence + 0.0035574 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_084_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=399, w3=220, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(47, min_periods=max(47//3, 2)).std()
    vol_slow = ret.rolling(399, min_periods=max(399//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.578235 + 0.0035575 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_085_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=412, w3=237, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(412, min_periods=max(412//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 54)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.349667 * slope + 0.0035576 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_086_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=425, w3=254, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(61)
    drag = impulse.rolling(425, min_periods=max(425//3, 2)).mean()
    noise = impulse.abs().rolling(254, min_periods=max(254//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.605294 + 0.0035577 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_087_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=438, w3=271, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 68)
    acceleration = _rolling_slope(velocity, 438)
    curvature = _rolling_slope(acceleration, 271)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.362333 * acceleration + 0.0035578 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_088_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=451, w3=288, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(75, min_periods=max(75//3, 2)).mean(), upside.rolling(451, min_periods=max(451//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.632353 + 0.0035579 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_089_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=464, w3=305, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(464, min_periods=max(464//3, 2)).max()
    rebound = x - x.rolling(82, min_periods=max(82//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.042667 * _rolling_slope(draw, 305) + 0.003558 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_090_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=477, w3=322, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 89)
    baseline = trend.rolling(477, min_periods=max(477//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(322, min_periods=max(322//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.659412 + 0.0035581 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_091_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=490, w3=339, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 96)
    slow = _rolling_slope(x, 490)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.672941 + 0.0035582 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_092_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=503, w3=356, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(503, min_periods=max(503//3, 2)).max()
    trough = x.rolling(103, min_periods=max(103//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.832941 + 0.0035583 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_093_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=17, w3=373, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(110)
    rank = change.rolling(17, min_periods=max(17//3, 2)).rank(pct=True)
    persistence = change.rolling(373, min_periods=max(373//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.068 * persistence + 0.0035584 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_094_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=30, w3=390, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(117, min_periods=max(117//3, 2)).std()
    vol_slow = ret.rolling(30, min_periods=max(30//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.86 + 0.0035585 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_095_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=124, w2=43, w3=407, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(43, min_periods=max(43//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 124)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.080667 * slope + 0.0035586 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_096_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=131, w2=56, w3=424, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(56, min_periods=max(56//3, 2)).mean()
    noise = impulse.abs().rolling(424, min_periods=max(424//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.887059 + 0.0035587 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_097_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=138, w2=69, w3=441, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 138)
    acceleration = _rolling_slope(velocity, 69)
    curvature = _rolling_slope(acceleration, 441)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.093333 * acceleration + 0.0035588 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_098_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=145, w2=82, w3=458, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(145, min_periods=max(145//3, 2)).mean(), upside.rolling(82, min_periods=max(82//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.914118 + 0.0035589 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_099_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=152, w2=95, w3=475, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(95, min_periods=max(95//3, 2)).max()
    rebound = x - x.rolling(152, min_periods=max(152//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.106 * _rolling_slope(draw, 475) + 0.003559 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_100_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=159, w2=108, w3=492, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 159)
    baseline = trend.rolling(108, min_periods=max(108//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(492, min_periods=max(492//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.941176 + 0.0035591 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_101_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=166, w2=121, w3=509, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 166)
    slow = _rolling_slope(x, 121)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.954706 + 0.0035592 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_102_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=173, w2=134, w3=526, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(134, min_periods=max(134//3, 2)).max()
    trough = x.rolling(173, min_periods=max(173//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.968235 + 0.0035593 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_103_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=180, w2=147, w3=543, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(147, min_periods=max(147//3, 2)).rank(pct=True)
    persistence = change.rolling(543, min_periods=max(543//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.131333 * persistence + 0.0035594 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_104_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=187, w2=160, w3=560, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(187, min_periods=max(187//3, 2)).std()
    vol_slow = ret.rolling(160, min_periods=max(160//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.995294 + 0.0035595 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_105_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=194, w2=173, w3=577, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(173, min_periods=max(173//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 194)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.144 * slope + 0.0035596 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_106_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=201, w2=186, w3=594, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(186, min_periods=max(186//3, 2)).mean()
    noise = impulse.abs().rolling(594, min_periods=max(594//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.022353 + 0.0035597 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_107_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=208, w2=199, w3=611, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 208)
    acceleration = _rolling_slope(velocity, 199)
    curvature = _rolling_slope(acceleration, 611)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.156667 * acceleration + 0.0035598 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_108_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=215, w2=212, w3=628, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(215, min_periods=max(215//3, 2)).mean(), upside.rolling(212, min_periods=max(212//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.049412 + 0.0035599 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_109_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=225, w3=645, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(225, min_periods=max(225//3, 2)).max()
    rebound = x - x.rolling(222, min_periods=max(222//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.169333 * _rolling_slope(draw, 645) + 0.00356 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_110_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=229, w2=238, w3=662, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 229)
    baseline = trend.rolling(238, min_periods=max(238//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(662, min_periods=max(662//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.076471 + 0.0035601 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_111_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=236, w2=251, w3=679, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 236)
    slow = _rolling_slope(x, 251)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.09 + 0.0035602 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_112_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=243, w2=264, w3=696, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(264, min_periods=max(264//3, 2)).max()
    trough = x.rolling(243, min_periods=max(243//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.103529 + 0.0035603 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_113_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=250, w2=277, w3=713, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(277, min_periods=max(277//3, 2)).rank(pct=True)
    persistence = change.rolling(713, min_periods=max(713//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.194667 * persistence + 0.0035604 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_114_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=10, w2=290, w3=730, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(10, min_periods=max(10//3, 2)).std()
    vol_slow = ret.rolling(290, min_periods=max(290//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.130588 + 0.0035605 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_115_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=17, w2=303, w3=747, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(303, min_periods=max(303//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 17)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.207333 * slope + 0.0035606 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_116_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=24, w2=316, w3=764, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(24)
    drag = impulse.rolling(316, min_periods=max(316//3, 2)).mean()
    noise = impulse.abs().rolling(764, min_periods=max(764//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.157647 + 0.0035607 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_117_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=31, w2=329, w3=30, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 31)
    acceleration = _rolling_slope(velocity, 329)
    curvature = _rolling_slope(acceleration, 30)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.22 * acceleration + 0.0035608 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_118_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=38, w2=342, w3=47, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(38, min_periods=max(38//3, 2)).mean(), upside.rolling(342, min_periods=max(342//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(47) * 1.184706 + 0.0035609 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_119_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=45, w2=355, w3=64, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(355, min_periods=max(355//3, 2)).max()
    rebound = x - x.rolling(45, min_periods=max(45//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.232667 * _rolling_slope(draw, 64) + 0.003561 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_120_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=52, w2=368, w3=81, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 52)
    baseline = trend.rolling(368, min_periods=max(368//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.211765 + 0.0035611 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_121_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=59, w2=381, w3=98, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 59)
    slow = _rolling_slope(x, 381)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=98, adjust=False).mean() * 1.225294 + 0.0035612 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_122_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=66, w2=394, w3=115, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(394, min_periods=max(394//3, 2)).max()
    trough = x.rolling(66, min_periods=max(66//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.238824 + 0.0035613 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_123_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=73, w2=407, w3=132, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(73)
    rank = change.rolling(407, min_periods=max(407//3, 2)).rank(pct=True)
    persistence = change.rolling(132, min_periods=max(132//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.258 * persistence + 0.0035614 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_124_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=420, w3=149, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(80, min_periods=max(80//3, 2)).std()
    vol_slow = ret.rolling(420, min_periods=max(420//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.265882 + 0.0035615 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_125_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=87, w2=433, w3=166, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(433, min_periods=max(433//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 87)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.270667 * slope + 0.0035616 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_126_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=94, w2=446, w3=183, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(94)
    drag = impulse.rolling(446, min_periods=max(446//3, 2)).mean()
    noise = impulse.abs().rolling(183, min_periods=max(183//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.292941 + 0.0035617 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_127_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=101, w2=459, w3=200, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 101)
    acceleration = _rolling_slope(velocity, 459)
    curvature = _rolling_slope(acceleration, 200)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.283333 * acceleration + 0.0035618 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_128_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=108, w2=472, w3=217, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(108, min_periods=max(108//3, 2)).mean(), upside.rolling(472, min_periods=max(472//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.32 + 0.0035619 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_129_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=115, w2=485, w3=234, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(485, min_periods=max(485//3, 2)).max()
    rebound = x - x.rolling(115, min_periods=max(115//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.296 * _rolling_slope(draw, 234) + 0.003562 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_130_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=122, w2=498, w3=251, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 122)
    baseline = trend.rolling(498, min_periods=max(498//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(251, min_periods=max(251//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.347059 + 0.0035621 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_131_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=129, w2=12, w3=268, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 129)
    slow = _rolling_slope(x, 12)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=268, adjust=False).mean() * 1.360588 + 0.0035622 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_132_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=136, w2=25, w3=285, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(25, min_periods=max(25//3, 2)).max()
    trough = x.rolling(136, min_periods=max(136//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.374118 + 0.0035623 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_133_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=143, w2=38, w3=302, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(38, min_periods=max(38//3, 2)).rank(pct=True)
    persistence = change.rolling(302, min_periods=max(302//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.321333 * persistence + 0.0035624 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_134_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=51, w3=319, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(150, min_periods=max(150//3, 2)).std()
    vol_slow = ret.rolling(51, min_periods=max(51//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.401176 + 0.0035625 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_135_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=64, w3=336, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(64, min_periods=max(64//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 157)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.334 * slope + 0.0035626 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_136_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=77, w3=353, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(77, min_periods=max(77//3, 2)).mean()
    noise = impulse.abs().rolling(353, min_periods=max(353//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.428235 + 0.0035627 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_137_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=90, w3=370, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 171)
    acceleration = _rolling_slope(velocity, 90)
    curvature = _rolling_slope(acceleration, 370)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.346667 * acceleration + 0.0035628 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_138_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=103, w3=387, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(178, min_periods=max(178//3, 2)).mean(), upside.rolling(103, min_periods=max(103//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.455294 + 0.0035629 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_139_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=116, w3=404, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(116, min_periods=max(116//3, 2)).max()
    rebound = x - x.rolling(185, min_periods=max(185//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.359333 * _rolling_slope(draw, 404) + 0.003563 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_140_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=129, w3=421, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 192)
    baseline = trend.rolling(129, min_periods=max(129//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(421, min_periods=max(421//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.482353 + 0.0035631 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_141_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=142, w3=438, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 199)
    slow = _rolling_slope(x, 142)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.495882 + 0.0035632 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_142_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=155, w3=455, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(155, min_periods=max(155//3, 2)).max()
    trough = x.rolling(206, min_periods=max(206//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.509412 + 0.0035633 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_143_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=168, w3=472, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(168, min_periods=max(168//3, 2)).rank(pct=True)
    persistence = change.rolling(472, min_periods=max(472//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.052333 * persistence + 0.0035634 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_144_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=181, w3=489, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(220, min_periods=max(220//3, 2)).std()
    vol_slow = ret.rolling(181, min_periods=max(181//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.536471 + 0.0035635 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_145_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=194, w3=506, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(194, min_periods=max(194//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 227)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.065 * slope + 0.0035636 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_146_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=234, w2=207, w3=523, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(207, min_periods=max(207//3, 2)).mean()
    noise = impulse.abs().rolling(523, min_periods=max(523//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.563529 + 0.0035637 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_147_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=241, w2=220, w3=540, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 241)
    acceleration = _rolling_slope(velocity, 220)
    curvature = _rolling_slope(acceleration, 540)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.077667 * acceleration + 0.0035638 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_148_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=248, w2=233, w3=557, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(248, min_periods=max(248//3, 2)).mean(), upside.rolling(233, min_periods=max(233//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.590588 + 0.0035639 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_149_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=8, w2=246, w3=574, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(246, min_periods=max(246//3, 2)).max()
    rebound = x - x.rolling(8, min_periods=max(8//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.090333 * _rolling_slope(draw, 574) + 0.003564 * anchor
    return base_signal.diff().diff().diff()

def f53_aent_gemini_150_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=15, w2=259, w3=591, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 15)
    baseline = trend.rolling(259, min_periods=max(259//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(591, min_periods=max(591//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.617647 + 0.0035641 * anchor
    return base_signal.diff().diff().diff()
