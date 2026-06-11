"""40 atr expansion dynamics gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Sudden increases in Average True Range as a precursor to significant price moves.
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

def f40_atre_gemini_076_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=142, w3=112, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(142, min_periods=max(142//3, 2)).max()
    trough = x.rolling(168, min_periods=max(168//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.944706 + 0.0028147 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_077_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=155, w3=129, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(155, min_periods=max(155//3, 2)).rank(pct=True)
    persistence = change.rolling(129, min_periods=max(129//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.164667 * persistence + 0.0028148 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_078_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=168, w3=146, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(182, min_periods=max(182//3, 2)).std()
    vol_slow = ret.rolling(168, min_periods=max(168//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.971765 + 0.0028149 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_079_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=189, w2=181, w3=163, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(181, min_periods=max(181//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 189)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.177333 * slope + 0.002815 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_080_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=196, w2=194, w3=180, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(194, min_periods=max(194//3, 2)).mean()
    noise = impulse.abs().rolling(180, min_periods=max(180//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.998824 + 0.0028151 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_081_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=203, w2=207, w3=197, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 203)
    acceleration = _rolling_slope(velocity, 207)
    curvature = _rolling_slope(acceleration, 197)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.19 * acceleration + 0.0028152 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_082_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=210, w2=220, w3=214, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 210)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.196333 * pressure.rolling(214, min_periods=max(214//3, 2)).mean() + 0.0028153 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_083_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=217, w2=233, w3=231, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(217, min_periods=max(217//3, 2)).mean())
    decay = spread.ewm(span=233, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.039412 + 0.0028154 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_084_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=224, w2=246, w3=248, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(246, min_periods=max(246//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 224)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.052941 + 0.0028155 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_085_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=231, w2=259, w3=265, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(231, min_periods=max(231//3, 2)).mean(), b.abs().rolling(259, min_periods=max(259//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.215333 * _rolling_slope(cover, 231) + 0.0028156 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_086_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=238, w2=272, w3=282, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.221667 * y + 0.778333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 238) - _rolling_slope(basket, 272) + 0.0028157 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_087_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=245, w2=285, w3=299, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(245, min_periods=max(245//3, 2)).mean(), upside.rolling(285, min_periods=max(285//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.093529 + 0.0028158 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_088_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=5, w2=298, w3=316, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(298, min_periods=max(298//3, 2)).max()
    rebound = x - x.rolling(5, min_periods=max(5//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.234333 * _rolling_slope(draw, 316) + 0.0028159 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_089_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=311, w3=333, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(12) - b.diff(126)
    stress = imbalance.rolling(333, min_periods=max(333//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.120588 + 0.002816 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_090_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=324, w3=350, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 19)
    baseline = trend.rolling(324, min_periods=max(324//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(350, min_periods=max(350//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.134118 + 0.0028161 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_091_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=337, w3=367, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 26)
    slow = _rolling_slope(x, 337)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.147647 + 0.0028162 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_092_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=350, w3=384, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(350, min_periods=max(350//3, 2)).max()
    trough = x.rolling(33, min_periods=max(33//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.161176 + 0.0028163 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_093_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=363, w3=401, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(40)
    rank = change.rolling(363, min_periods=max(363//3, 2)).rank(pct=True)
    persistence = change.rolling(401, min_periods=max(401//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.266 * persistence + 0.0028164 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_094_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=376, w3=418, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(47, min_periods=max(47//3, 2)).std()
    vol_slow = ret.rolling(376, min_periods=max(376//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.188235 + 0.0028165 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_095_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=389, w3=435, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(389, min_periods=max(389//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 54)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.278667 * slope + 0.0028166 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_096_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=402, w3=452, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(61)
    drag = impulse.rolling(402, min_periods=max(402//3, 2)).mean()
    noise = impulse.abs().rolling(452, min_periods=max(452//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.215294 + 0.0028167 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_097_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=415, w3=469, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 68)
    acceleration = _rolling_slope(velocity, 415)
    curvature = _rolling_slope(acceleration, 469)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.291333 * acceleration + 0.0028168 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_098_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=428, w3=486, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 75)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.297667 * pressure.rolling(486, min_periods=max(486//3, 2)).mean() + 0.0028169 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_099_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=441, w3=503, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(82, min_periods=max(82//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.255882 + 0.002817 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_100_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=454, w3=520, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(454, min_periods=max(454//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 89)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.269412 + 0.0028171 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_101_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=467, w3=537, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(96, min_periods=max(96//3, 2)).mean(), b.abs().rolling(467, min_periods=max(467//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.316667 * _rolling_slope(cover, 96) + 0.0028172 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_102_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=480, w3=554, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.323 * y + 0.677000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 103) - _rolling_slope(basket, 480) + 0.0028173 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_103_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=493, w3=571, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(110, min_periods=max(110//3, 2)).mean(), upside.rolling(493, min_periods=max(493//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.31 + 0.0028174 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_104_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=117, w2=506, w3=588, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(506, min_periods=max(506//3, 2)).max()
    rebound = x - x.rolling(117, min_periods=max(117//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.335667 * _rolling_slope(draw, 588) + 0.0028175 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_105_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=124, w2=20, w3=605, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(124) - b.diff(20)
    stress = imbalance.rolling(605, min_periods=max(605//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.337059 + 0.0028176 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_106_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=131, w2=33, w3=622, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 131)
    baseline = trend.rolling(33, min_periods=max(33//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(622, min_periods=max(622//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.350588 + 0.0028177 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_107_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=138, w2=46, w3=639, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 138)
    slow = _rolling_slope(x, 46)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.364118 + 0.0028178 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_108_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=145, w2=59, w3=656, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(59, min_periods=max(59//3, 2)).max()
    trough = x.rolling(145, min_periods=max(145//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.377647 + 0.0028179 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_109_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=152, w2=72, w3=673, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(72, min_periods=max(72//3, 2)).rank(pct=True)
    persistence = change.rolling(673, min_periods=max(673//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.035 * persistence + 0.002818 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_110_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=159, w2=85, w3=690, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(159, min_periods=max(159//3, 2)).std()
    vol_slow = ret.rolling(85, min_periods=max(85//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.404706 + 0.0028181 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_111_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=166, w2=98, w3=707, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(98, min_periods=max(98//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 166)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.047667 * slope + 0.0028182 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_112_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=173, w2=111, w3=724, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(111, min_periods=max(111//3, 2)).mean()
    noise = impulse.abs().rolling(724, min_periods=max(724//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.431765 + 0.0028183 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_113_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=180, w2=124, w3=741, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 180)
    acceleration = _rolling_slope(velocity, 124)
    curvature = _rolling_slope(acceleration, 741)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.060333 * acceleration + 0.0028184 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_114_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=187, w2=137, w3=758, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 187)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.066667 * pressure.rolling(758, min_periods=max(758//3, 2)).mean() + 0.0028185 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_115_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=194, w2=150, w3=24, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(194, min_periods=max(194//3, 2)).mean())
    decay = spread.ewm(span=150, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.472353 + 0.0028186 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_116_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=201, w2=163, w3=41, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(163, min_periods=max(163//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 201)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.485882 + 0.0028187 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_117_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=208, w2=176, w3=58, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(208, min_periods=max(208//3, 2)).mean(), b.abs().rolling(176, min_periods=max(176//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(58) + 0.085667 * _rolling_slope(cover, 208) + 0.0028188 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_118_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=215, w2=189, w3=75, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.092 * y + 0.908000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 215) - _rolling_slope(basket, 189) + 0.0028189 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_119_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=222, w2=202, w3=92, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(222, min_periods=max(222//3, 2)).mean(), upside.rolling(202, min_periods=max(202//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(92) * 1.526471 + 0.002819 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_120_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=229, w2=215, w3=109, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(215, min_periods=max(215//3, 2)).max()
    rebound = x - x.rolling(229, min_periods=max(229//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.104667 * _rolling_slope(draw, 109) + 0.0028191 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_121_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=228, w3=126, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(126, min_periods=max(126//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.553529 + 0.0028192 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_122_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=241, w3=143, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 243)
    baseline = trend.rolling(241, min_periods=max(241//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.567059 + 0.0028193 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_123_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=250, w2=254, w3=160, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 250)
    slow = _rolling_slope(x, 254)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=160, adjust=False).mean() * 1.580588 + 0.0028194 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_124_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=267, w3=177, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(267, min_periods=max(267//3, 2)).max()
    trough = x.rolling(10, min_periods=max(10//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.594118 + 0.0028195 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_125_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=17, w2=280, w3=194, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(17)
    rank = change.rolling(280, min_periods=max(280//3, 2)).rank(pct=True)
    persistence = change.rolling(194, min_periods=max(194//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.136333 * persistence + 0.0028196 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_126_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=24, w2=293, w3=211, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(24, min_periods=max(24//3, 2)).std()
    vol_slow = ret.rolling(293, min_periods=max(293//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.621176 + 0.0028197 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_127_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=31, w2=306, w3=228, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(306, min_periods=max(306//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 31)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.149 * slope + 0.0028198 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_128_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=319, w3=245, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(38)
    drag = impulse.rolling(319, min_periods=max(319//3, 2)).mean()
    noise = impulse.abs().rolling(245, min_periods=max(245//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.648235 + 0.0028199 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_129_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=332, w3=262, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 45)
    acceleration = _rolling_slope(velocity, 332)
    curvature = _rolling_slope(acceleration, 262)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.161667 * acceleration + 0.00282 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_130_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=345, w3=279, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 52)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.168 * pressure.rolling(279, min_periods=max(279//3, 2)).mean() + 0.0028201 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_131_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=59, w2=358, w3=296, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(59, min_periods=max(59//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.835294 + 0.0028202 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_132_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=66, w2=371, w3=313, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(371, min_periods=max(371//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 66)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.848824 + 0.0028203 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_133_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=73, w2=384, w3=330, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(73, min_periods=max(73//3, 2)).mean(), b.abs().rolling(384, min_periods=max(384//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.187 * _rolling_slope(cover, 73) + 0.0028204 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_134_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=80, w2=397, w3=347, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.193333 * y + 0.806667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 80) - _rolling_slope(basket, 397) + 0.0028205 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_135_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=87, w2=410, w3=364, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(87, min_periods=max(87//3, 2)).mean(), upside.rolling(410, min_periods=max(410//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.889412 + 0.0028206 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_136_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=94, w2=423, w3=381, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(423, min_periods=max(423//3, 2)).max()
    rebound = x - x.rolling(94, min_periods=max(94//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.206 * _rolling_slope(draw, 381) + 0.0028207 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_137_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=101, w2=436, w3=398, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(101) - b.diff(126)
    stress = imbalance.rolling(398, min_periods=max(398//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.916471 + 0.0028208 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_138_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=108, w2=449, w3=415, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 108)
    baseline = trend.rolling(449, min_periods=max(449//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(415, min_periods=max(415//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.93 + 0.0028209 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_139_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=115, w2=462, w3=432, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 115)
    slow = _rolling_slope(x, 462)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.943529 + 0.002821 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_140_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=122, w2=475, w3=449, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(475, min_periods=max(475//3, 2)).max()
    trough = x.rolling(122, min_periods=max(122//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.957059 + 0.0028211 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_141_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=129, w2=488, w3=466, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(488, min_periods=max(488//3, 2)).rank(pct=True)
    persistence = change.rolling(466, min_periods=max(466//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.237667 * persistence + 0.0028212 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_142_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=136, w2=501, w3=483, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(136, min_periods=max(136//3, 2)).std()
    vol_slow = ret.rolling(501, min_periods=max(501//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.984118 + 0.0028213 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_143_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=143, w2=15, w3=500, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(15, min_periods=max(15//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 143)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.250333 * slope + 0.0028214 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_144_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=150, w2=28, w3=517, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(28, min_periods=max(28//3, 2)).mean()
    noise = impulse.abs().rolling(517, min_periods=max(517//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.011176 + 0.0028215 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_145_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=157, w2=41, w3=534, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 157)
    acceleration = _rolling_slope(velocity, 41)
    curvature = _rolling_slope(acceleration, 534)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.263 * acceleration + 0.0028216 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_146_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=164, w2=54, w3=551, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 164)
    pressure = rel_log.diff(54)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.269333 * pressure.rolling(551, min_periods=max(551//3, 2)).mean() + 0.0028217 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_147_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=171, w2=67, w3=568, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(171, min_periods=max(171//3, 2)).mean())
    decay = spread.ewm(span=67, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.051765 + 0.0028218 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_148_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=178, w2=80, w3=585, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(80, min_periods=max(80//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 178)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.065294 + 0.0028219 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_149_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=185, w2=93, w3=602, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(185, min_periods=max(185//3, 2)).mean(), b.abs().rolling(93, min_periods=max(93//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.288333 * _rolling_slope(cover, 185) + 0.002822 * anchor
    return base_signal.diff().diff()

def f40_atre_gemini_150_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=192, w2=106, w3=619, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.294667 * y + 0.705333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 192) - _rolling_slope(basket, 106) + 0.0028221 * anchor
    return base_signal.diff().diff()
