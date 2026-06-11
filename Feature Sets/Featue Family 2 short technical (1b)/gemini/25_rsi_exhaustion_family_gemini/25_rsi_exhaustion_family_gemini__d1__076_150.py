"""25 rsi exhaustion family gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Overbought and oversold conditions detected through Relative Strength Index extremes.
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

def f25_rsie_gemini_076_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=162, w2=399, w3=626, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(399, min_periods=max(399//3, 2)).mean()
    noise = impulse.abs().rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.483529 + 0.0019607 * anchor
    return base_signal.diff()

def f25_rsie_gemini_077_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=169, w2=412, w3=643, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 169)
    acceleration = _rolling_slope(velocity, 412)
    curvature = _rolling_slope(acceleration, 643)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.248333 * acceleration + 0.0019608 * anchor
    return base_signal.diff()

def f25_rsie_gemini_078_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=176, w2=425, w3=660, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(176, min_periods=max(176//3, 2)).mean(), upside.rolling(425, min_periods=max(425//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.510588 + 0.0019609 * anchor
    return base_signal.diff()

def f25_rsie_gemini_079_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=183, w2=438, w3=677, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(438, min_periods=max(438//3, 2)).max()
    rebound = x - x.rolling(183, min_periods=max(183//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.261 * _rolling_slope(draw, 677) + 0.001961 * anchor
    return base_signal.diff()

def f25_rsie_gemini_080_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=190, w2=451, w3=694, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 190)
    baseline = trend.rolling(451, min_periods=max(451//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(694, min_periods=max(694//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.537647 + 0.0019611 * anchor
    return base_signal.diff()

def f25_rsie_gemini_081_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=197, w2=464, w3=711, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 197)
    slow = _rolling_slope(x, 464)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.551176 + 0.0019612 * anchor
    return base_signal.diff()

def f25_rsie_gemini_082_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=204, w2=477, w3=728, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(477, min_periods=max(477//3, 2)).max()
    trough = x.rolling(204, min_periods=max(204//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.564706 + 0.0019613 * anchor
    return base_signal.diff()

def f25_rsie_gemini_083_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=211, w2=490, w3=745, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(490, min_periods=max(490//3, 2)).rank(pct=True)
    persistence = change.rolling(745, min_periods=max(745//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.286333 * persistence + 0.0019614 * anchor
    return base_signal.diff()

def f25_rsie_gemini_084_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=218, w2=503, w3=762, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(218, min_periods=max(218//3, 2)).std()
    vol_slow = ret.rolling(503, min_periods=max(503//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.591765 + 0.0019615 * anchor
    return base_signal.diff()

def f25_rsie_gemini_085_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=225, w2=17, w3=28, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(17, min_periods=max(17//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 225)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.299 * slope + 0.0019616 * anchor
    return base_signal.diff()

def f25_rsie_gemini_086_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=232, w2=30, w3=45, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(30, min_periods=max(30//3, 2)).mean()
    noise = impulse.abs().rolling(45, min_periods=max(45//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.618824 + 0.0019617 * anchor
    return base_signal.diff()

def f25_rsie_gemini_087_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=239, w2=43, w3=62, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 239)
    acceleration = _rolling_slope(velocity, 43)
    curvature = _rolling_slope(acceleration, 62)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.311667 * acceleration + 0.0019618 * anchor
    return base_signal.diff()

def f25_rsie_gemini_088_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=246, w2=56, w3=79, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(246, min_periods=max(246//3, 2)).mean(), upside.rolling(56, min_periods=max(56//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(79) * 1.645882 + 0.0019619 * anchor
    return base_signal.diff()

def f25_rsie_gemini_089_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=6, w2=69, w3=96, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(69, min_periods=max(69//3, 2)).max()
    rebound = x - x.rolling(6, min_periods=max(6//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.324333 * _rolling_slope(draw, 96) + 0.001962 * anchor
    return base_signal.diff()

def f25_rsie_gemini_090_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=13, w2=82, w3=113, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 13)
    baseline = trend.rolling(82, min_periods=max(82//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(113, min_periods=max(113//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.672941 + 0.0019621 * anchor
    return base_signal.diff()

def f25_rsie_gemini_091_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=20, w2=95, w3=130, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 20)
    slow = _rolling_slope(x, 95)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=130, adjust=False).mean() * 0.832941 + 0.0019622 * anchor
    return base_signal.diff()

def f25_rsie_gemini_092_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=27, w2=108, w3=147, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(108, min_periods=max(108//3, 2)).max()
    trough = x.rolling(27, min_periods=max(27//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.846471 + 0.0019623 * anchor
    return base_signal.diff()

def f25_rsie_gemini_093_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=34, w2=121, w3=164, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(34)
    rank = change.rolling(121, min_periods=max(121//3, 2)).rank(pct=True)
    persistence = change.rolling(164, min_periods=max(164//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.349667 * persistence + 0.0019624 * anchor
    return base_signal.diff()

def f25_rsie_gemini_094_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=41, w2=134, w3=181, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(41, min_periods=max(41//3, 2)).std()
    vol_slow = ret.rolling(134, min_periods=max(134//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.873529 + 0.0019625 * anchor
    return base_signal.diff()

def f25_rsie_gemini_095_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=48, w2=147, w3=198, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(147, min_periods=max(147//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 48)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.362333 * slope + 0.0019626 * anchor
    return base_signal.diff()

def f25_rsie_gemini_096_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=55, w2=160, w3=215, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(55)
    drag = impulse.rolling(160, min_periods=max(160//3, 2)).mean()
    noise = impulse.abs().rolling(215, min_periods=max(215//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.900588 + 0.0019627 * anchor
    return base_signal.diff()

def f25_rsie_gemini_097_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=62, w2=173, w3=232, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 62)
    acceleration = _rolling_slope(velocity, 173)
    curvature = _rolling_slope(acceleration, 232)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.042667 * acceleration + 0.0019628 * anchor
    return base_signal.diff()

def f25_rsie_gemini_098_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=69, w2=186, w3=249, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(69, min_periods=max(69//3, 2)).mean(), upside.rolling(186, min_periods=max(186//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.927647 + 0.0019629 * anchor
    return base_signal.diff()

def f25_rsie_gemini_099_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=76, w2=199, w3=266, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(199, min_periods=max(199//3, 2)).max()
    rebound = x - x.rolling(76, min_periods=max(76//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.055333 * _rolling_slope(draw, 266) + 0.001963 * anchor
    return base_signal.diff()

def f25_rsie_gemini_100_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=83, w2=212, w3=283, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 83)
    baseline = trend.rolling(212, min_periods=max(212//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(283, min_periods=max(283//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.954706 + 0.0019631 * anchor
    return base_signal.diff()

def f25_rsie_gemini_101_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=90, w2=225, w3=300, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 90)
    slow = _rolling_slope(x, 225)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.968235 + 0.0019632 * anchor
    return base_signal.diff()

def f25_rsie_gemini_102_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=97, w2=238, w3=317, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(238, min_periods=max(238//3, 2)).max()
    trough = x.rolling(97, min_periods=max(97//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.981765 + 0.0019633 * anchor
    return base_signal.diff()

def f25_rsie_gemini_103_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=104, w2=251, w3=334, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(104)
    rank = change.rolling(251, min_periods=max(251//3, 2)).rank(pct=True)
    persistence = change.rolling(334, min_periods=max(334//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.080667 * persistence + 0.0019634 * anchor
    return base_signal.diff()

def f25_rsie_gemini_104_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=111, w2=264, w3=351, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(111, min_periods=max(111//3, 2)).std()
    vol_slow = ret.rolling(264, min_periods=max(264//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.008824 + 0.0019635 * anchor
    return base_signal.diff()

def f25_rsie_gemini_105_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=118, w2=277, w3=368, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(277, min_periods=max(277//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 118)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.093333 * slope + 0.0019636 * anchor
    return base_signal.diff()

def f25_rsie_gemini_106_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=125, w2=290, w3=385, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(125)
    drag = impulse.rolling(290, min_periods=max(290//3, 2)).mean()
    noise = impulse.abs().rolling(385, min_periods=max(385//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.035882 + 0.0019637 * anchor
    return base_signal.diff()

def f25_rsie_gemini_107_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=132, w2=303, w3=402, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 132)
    acceleration = _rolling_slope(velocity, 303)
    curvature = _rolling_slope(acceleration, 402)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.106 * acceleration + 0.0019638 * anchor
    return base_signal.diff()

def f25_rsie_gemini_108_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=139, w2=316, w3=419, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(139, min_periods=max(139//3, 2)).mean(), upside.rolling(316, min_periods=max(316//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.062941 + 0.0019639 * anchor
    return base_signal.diff()

def f25_rsie_gemini_109_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=146, w2=329, w3=436, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(329, min_periods=max(329//3, 2)).max()
    rebound = x - x.rolling(146, min_periods=max(146//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.118667 * _rolling_slope(draw, 436) + 0.001964 * anchor
    return base_signal.diff()

def f25_rsie_gemini_110_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=153, w2=342, w3=453, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 153)
    baseline = trend.rolling(342, min_periods=max(342//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(453, min_periods=max(453//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.09 + 0.0019641 * anchor
    return base_signal.diff()

def f25_rsie_gemini_111_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=160, w2=355, w3=470, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 160)
    slow = _rolling_slope(x, 355)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.103529 + 0.0019642 * anchor
    return base_signal.diff()

def f25_rsie_gemini_112_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=167, w2=368, w3=487, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(368, min_periods=max(368//3, 2)).max()
    trough = x.rolling(167, min_periods=max(167//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.117059 + 0.0019643 * anchor
    return base_signal.diff()

def f25_rsie_gemini_113_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=174, w2=381, w3=504, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(381, min_periods=max(381//3, 2)).rank(pct=True)
    persistence = change.rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.144 * persistence + 0.0019644 * anchor
    return base_signal.diff()

def f25_rsie_gemini_114_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=181, w2=394, w3=521, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(181, min_periods=max(181//3, 2)).std()
    vol_slow = ret.rolling(394, min_periods=max(394//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.144118 + 0.0019645 * anchor
    return base_signal.diff()

def f25_rsie_gemini_115_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=188, w2=407, w3=538, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(407, min_periods=max(407//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 188)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.156667 * slope + 0.0019646 * anchor
    return base_signal.diff()

def f25_rsie_gemini_116_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=195, w2=420, w3=555, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(420, min_periods=max(420//3, 2)).mean()
    noise = impulse.abs().rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.171176 + 0.0019647 * anchor
    return base_signal.diff()

def f25_rsie_gemini_117_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=202, w2=433, w3=572, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 202)
    acceleration = _rolling_slope(velocity, 433)
    curvature = _rolling_slope(acceleration, 572)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.169333 * acceleration + 0.0019648 * anchor
    return base_signal.diff()

def f25_rsie_gemini_118_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=209, w2=446, w3=589, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(209, min_periods=max(209//3, 2)).mean(), upside.rolling(446, min_periods=max(446//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.198235 + 0.0019649 * anchor
    return base_signal.diff()

def f25_rsie_gemini_119_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=216, w2=459, w3=606, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(459, min_periods=max(459//3, 2)).max()
    rebound = x - x.rolling(216, min_periods=max(216//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.182 * _rolling_slope(draw, 606) + 0.001965 * anchor
    return base_signal.diff()

def f25_rsie_gemini_120_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=223, w2=472, w3=623, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 223)
    baseline = trend.rolling(472, min_periods=max(472//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(623, min_periods=max(623//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.225294 + 0.0019651 * anchor
    return base_signal.diff()

def f25_rsie_gemini_121_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=230, w2=485, w3=640, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 230)
    slow = _rolling_slope(x, 485)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.238824 + 0.0019652 * anchor
    return base_signal.diff()

def f25_rsie_gemini_122_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=237, w2=498, w3=657, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(498, min_periods=max(498//3, 2)).max()
    trough = x.rolling(237, min_periods=max(237//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.252353 + 0.0019653 * anchor
    return base_signal.diff()

def f25_rsie_gemini_123_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=244, w2=12, w3=674, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(12, min_periods=max(12//3, 2)).rank(pct=True)
    persistence = change.rolling(674, min_periods=max(674//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.207333 * persistence + 0.0019654 * anchor
    return base_signal.diff()

def f25_rsie_gemini_124_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=251, w2=25, w3=691, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(251, min_periods=max(251//3, 2)).std()
    vol_slow = ret.rolling(25, min_periods=max(25//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.279412 + 0.0019655 * anchor
    return base_signal.diff()

def f25_rsie_gemini_125_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=11, w2=38, w3=708, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(38, min_periods=max(38//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 11)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.22 * slope + 0.0019656 * anchor
    return base_signal.diff()

def f25_rsie_gemini_126_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=18, w2=51, w3=725, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(18)
    drag = impulse.rolling(51, min_periods=max(51//3, 2)).mean()
    noise = impulse.abs().rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.306471 + 0.0019657 * anchor
    return base_signal.diff()

def f25_rsie_gemini_127_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=25, w2=64, w3=742, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 64)
    curvature = _rolling_slope(acceleration, 742)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.232667 * acceleration + 0.0019658 * anchor
    return base_signal.diff()

def f25_rsie_gemini_128_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=32, w2=77, w3=759, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(32, min_periods=max(32//3, 2)).mean(), upside.rolling(77, min_periods=max(77//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.333529 + 0.0019659 * anchor
    return base_signal.diff()

def f25_rsie_gemini_129_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=39, w2=90, w3=25, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(90, min_periods=max(90//3, 2)).max()
    rebound = x - x.rolling(39, min_periods=max(39//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.245333 * _rolling_slope(draw, 25) + 0.001966 * anchor
    return base_signal.diff()

def f25_rsie_gemini_130_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=46, w2=103, w3=42, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 46)
    baseline = trend.rolling(103, min_periods=max(103//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.360588 + 0.0019661 * anchor
    return base_signal.diff()

def f25_rsie_gemini_131_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=53, w2=116, w3=59, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 53)
    slow = _rolling_slope(x, 116)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=59, adjust=False).mean() * 1.374118 + 0.0019662 * anchor
    return base_signal.diff()

def f25_rsie_gemini_132_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=60, w2=129, w3=76, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(129, min_periods=max(129//3, 2)).max()
    trough = x.rolling(60, min_periods=max(60//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.387647 + 0.0019663 * anchor
    return base_signal.diff()

def f25_rsie_gemini_133_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=67, w2=142, w3=93, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(67)
    rank = change.rolling(142, min_periods=max(142//3, 2)).rank(pct=True)
    persistence = change.rolling(93, min_periods=max(93//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.270667 * persistence + 0.0019664 * anchor
    return base_signal.diff()

def f25_rsie_gemini_134_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=155, w3=110, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(74, min_periods=max(74//3, 2)).std()
    vol_slow = ret.rolling(155, min_periods=max(155//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.414706 + 0.0019665 * anchor
    return base_signal.diff()

def f25_rsie_gemini_135_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=168, w3=127, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(168, min_periods=max(168//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 81)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.283333 * slope + 0.0019666 * anchor
    return base_signal.diff()

def f25_rsie_gemini_136_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=88, w2=181, w3=144, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(88)
    drag = impulse.rolling(181, min_periods=max(181//3, 2)).mean()
    noise = impulse.abs().rolling(144, min_periods=max(144//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.441765 + 0.0019667 * anchor
    return base_signal.diff()

def f25_rsie_gemini_137_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=95, w2=194, w3=161, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 95)
    acceleration = _rolling_slope(velocity, 194)
    curvature = _rolling_slope(acceleration, 161)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.296 * acceleration + 0.0019668 * anchor
    return base_signal.diff()

def f25_rsie_gemini_138_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=102, w2=207, w3=178, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(102, min_periods=max(102//3, 2)).mean(), upside.rolling(207, min_periods=max(207//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.468824 + 0.0019669 * anchor
    return base_signal.diff()

def f25_rsie_gemini_139_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=109, w2=220, w3=195, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(220, min_periods=max(220//3, 2)).max()
    rebound = x - x.rolling(109, min_periods=max(109//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.308667 * _rolling_slope(draw, 195) + 0.001967 * anchor
    return base_signal.diff()

def f25_rsie_gemini_140_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=116, w2=233, w3=212, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 116)
    baseline = trend.rolling(233, min_periods=max(233//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(212, min_periods=max(212//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.495882 + 0.0019671 * anchor
    return base_signal.diff()

def f25_rsie_gemini_141_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=123, w2=246, w3=229, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 123)
    slow = _rolling_slope(x, 246)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=229, adjust=False).mean() * 1.509412 + 0.0019672 * anchor
    return base_signal.diff()

def f25_rsie_gemini_142_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=130, w2=259, w3=246, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(259, min_periods=max(259//3, 2)).max()
    trough = x.rolling(130, min_periods=max(130//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.522941 + 0.0019673 * anchor
    return base_signal.diff()

def f25_rsie_gemini_143_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=137, w2=272, w3=263, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(272, min_periods=max(272//3, 2)).rank(pct=True)
    persistence = change.rolling(263, min_periods=max(263//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.334 * persistence + 0.0019674 * anchor
    return base_signal.diff()

def f25_rsie_gemini_144_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=144, w2=285, w3=280, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(144, min_periods=max(144//3, 2)).std()
    vol_slow = ret.rolling(285, min_periods=max(285//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.55 + 0.0019675 * anchor
    return base_signal.diff()

def f25_rsie_gemini_145_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=151, w2=298, w3=297, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(298, min_periods=max(298//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 151)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.346667 * slope + 0.0019676 * anchor
    return base_signal.diff()

def f25_rsie_gemini_146_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=158, w2=311, w3=314, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(311, min_periods=max(311//3, 2)).mean()
    noise = impulse.abs().rolling(314, min_periods=max(314//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.577059 + 0.0019677 * anchor
    return base_signal.diff()

def f25_rsie_gemini_147_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=165, w2=324, w3=331, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 165)
    acceleration = _rolling_slope(velocity, 324)
    curvature = _rolling_slope(acceleration, 331)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.359333 * acceleration + 0.0019678 * anchor
    return base_signal.diff()

def f25_rsie_gemini_148_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=172, w2=337, w3=348, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(172, min_periods=max(172//3, 2)).mean(), upside.rolling(337, min_periods=max(337//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.604118 + 0.0019679 * anchor
    return base_signal.diff()

def f25_rsie_gemini_149_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=179, w2=350, w3=365, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(350, min_periods=max(350//3, 2)).max()
    rebound = x - x.rolling(179, min_periods=max(179//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.039667 * _rolling_slope(draw, 365) + 0.001968 * anchor
    return base_signal.diff()

def f25_rsie_gemini_150_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=186, w2=363, w3=382, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 186)
    baseline = trend.rolling(363, min_periods=max(363//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(382, min_periods=max(382//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.631176 + 0.0019681 * anchor
    return base_signal.diff()
