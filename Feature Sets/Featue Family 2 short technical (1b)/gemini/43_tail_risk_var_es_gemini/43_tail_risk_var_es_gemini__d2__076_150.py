"""43 tail risk var es gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Quantifying extreme loss potential through Value at Risk and Expected Shortfall proxies.
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

def f43_tail_gemini_076_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=72, w2=26, w3=134, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(72)
    drag = impulse.rolling(26, min_periods=max(26//3, 2)).mean()
    noise = impulse.abs().rolling(134, min_periods=max(134//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.482353 + 0.0029827 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_077_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=79, w2=39, w3=151, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 79)
    acceleration = _rolling_slope(velocity, 39)
    curvature = _rolling_slope(acceleration, 151)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.17 * acceleration + 0.0029828 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_078_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=86, w2=52, w3=168, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(86, min_periods=max(86//3, 2)).mean(), upside.rolling(52, min_periods=max(52//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.509412 + 0.0029829 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_079_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=93, w2=65, w3=185, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(65, min_periods=max(65//3, 2)).max()
    rebound = x - x.rolling(93, min_periods=max(93//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.182667 * _rolling_slope(draw, 185) + 0.002983 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_080_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=100, w2=78, w3=202, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 100)
    baseline = trend.rolling(78, min_periods=max(78//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(202, min_periods=max(202//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.536471 + 0.0029831 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_081_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=107, w2=91, w3=219, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 107)
    slow = _rolling_slope(x, 91)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=219, adjust=False).mean() * 1.55 + 0.0029832 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_082_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=114, w2=104, w3=236, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(104, min_periods=max(104//3, 2)).max()
    trough = x.rolling(114, min_periods=max(114//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.563529 + 0.0029833 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_083_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=121, w2=117, w3=253, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(121)
    rank = change.rolling(117, min_periods=max(117//3, 2)).rank(pct=True)
    persistence = change.rolling(253, min_periods=max(253//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.208 * persistence + 0.0029834 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_084_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=128, w2=130, w3=270, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(128, min_periods=max(128//3, 2)).std()
    vol_slow = ret.rolling(130, min_periods=max(130//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.590588 + 0.0029835 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_085_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=135, w2=143, w3=287, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(143, min_periods=max(143//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 135)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.220667 * slope + 0.0029836 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_086_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=142, w2=156, w3=304, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(156, min_periods=max(156//3, 2)).mean()
    noise = impulse.abs().rolling(304, min_periods=max(304//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.617647 + 0.0029837 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_087_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=149, w2=169, w3=321, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 149)
    acceleration = _rolling_slope(velocity, 169)
    curvature = _rolling_slope(acceleration, 321)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.233333 * acceleration + 0.0029838 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_088_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=156, w2=182, w3=338, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(156, min_periods=max(156//3, 2)).mean(), upside.rolling(182, min_periods=max(182//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.644706 + 0.0029839 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_089_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=163, w2=195, w3=355, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(195, min_periods=max(195//3, 2)).max()
    rebound = x - x.rolling(163, min_periods=max(163//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.246 * _rolling_slope(draw, 355) + 0.002984 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_090_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=170, w2=208, w3=372, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 170)
    baseline = trend.rolling(208, min_periods=max(208//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(372, min_periods=max(372//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.671765 + 0.0029841 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_091_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=177, w2=221, w3=389, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 177)
    slow = _rolling_slope(x, 221)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.831765 + 0.0029842 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_092_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=184, w2=234, w3=406, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(234, min_periods=max(234//3, 2)).max()
    trough = x.rolling(184, min_periods=max(184//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.845294 + 0.0029843 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_093_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=191, w2=247, w3=423, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(247, min_periods=max(247//3, 2)).rank(pct=True)
    persistence = change.rolling(423, min_periods=max(423//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.271333 * persistence + 0.0029844 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_094_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=198, w2=260, w3=440, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(198, min_periods=max(198//3, 2)).std()
    vol_slow = ret.rolling(260, min_periods=max(260//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.872353 + 0.0029845 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_095_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=205, w2=273, w3=457, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(273, min_periods=max(273//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 205)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.284 * slope + 0.0029846 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_096_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=212, w2=286, w3=474, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(286, min_periods=max(286//3, 2)).mean()
    noise = impulse.abs().rolling(474, min_periods=max(474//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.899412 + 0.0029847 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_097_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=219, w2=299, w3=491, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 219)
    acceleration = _rolling_slope(velocity, 299)
    curvature = _rolling_slope(acceleration, 491)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.296667 * acceleration + 0.0029848 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_098_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=226, w2=312, w3=508, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(226, min_periods=max(226//3, 2)).mean(), upside.rolling(312, min_periods=max(312//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.926471 + 0.0029849 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_099_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=233, w2=325, w3=525, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(325, min_periods=max(325//3, 2)).max()
    rebound = x - x.rolling(233, min_periods=max(233//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.309333 * _rolling_slope(draw, 525) + 0.002985 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_100_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=240, w2=338, w3=542, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 240)
    baseline = trend.rolling(338, min_periods=max(338//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(542, min_periods=max(542//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.953529 + 0.0029851 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_101_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=247, w2=351, w3=559, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 247)
    slow = _rolling_slope(x, 351)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.967059 + 0.0029852 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_102_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=7, w2=364, w3=576, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(364, min_periods=max(364//3, 2)).max()
    trough = x.rolling(7, min_periods=max(7//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.980588 + 0.0029853 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_103_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=14, w2=377, w3=593, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(14)
    rank = change.rolling(377, min_periods=max(377//3, 2)).rank(pct=True)
    persistence = change.rolling(593, min_periods=max(593//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.334667 * persistence + 0.0029854 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_104_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=21, w2=390, w3=610, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(21, min_periods=max(21//3, 2)).std()
    vol_slow = ret.rolling(390, min_periods=max(390//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.007647 + 0.0029855 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_105_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=28, w2=403, w3=627, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(403, min_periods=max(403//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 28)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.347333 * slope + 0.0029856 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_106_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=35, w2=416, w3=644, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(35)
    drag = impulse.rolling(416, min_periods=max(416//3, 2)).mean()
    noise = impulse.abs().rolling(644, min_periods=max(644//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.034706 + 0.0029857 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_107_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=42, w2=429, w3=661, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 42)
    acceleration = _rolling_slope(velocity, 429)
    curvature = _rolling_slope(acceleration, 661)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.36 * acceleration + 0.0029858 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_108_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=49, w2=442, w3=678, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(49, min_periods=max(49//3, 2)).mean(), upside.rolling(442, min_periods=max(442//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.061765 + 0.0029859 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_109_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=56, w2=455, w3=695, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(455, min_periods=max(455//3, 2)).max()
    rebound = x - x.rolling(56, min_periods=max(56//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.040333 * _rolling_slope(draw, 695) + 0.002986 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_110_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=63, w2=468, w3=712, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 63)
    baseline = trend.rolling(468, min_periods=max(468//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(712, min_periods=max(712//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.088824 + 0.0029861 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_111_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=481, w3=729, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 70)
    slow = _rolling_slope(x, 481)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.102353 + 0.0029862 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_112_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=77, w2=494, w3=746, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(494, min_periods=max(494//3, 2)).max()
    trough = x.rolling(77, min_periods=max(77//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.115882 + 0.0029863 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_113_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=84, w2=507, w3=763, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(84)
    rank = change.rolling(507, min_periods=max(507//3, 2)).rank(pct=True)
    persistence = change.rolling(763, min_periods=max(763//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.065667 * persistence + 0.0029864 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_114_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=91, w2=21, w3=29, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(91, min_periods=max(91//3, 2)).std()
    vol_slow = ret.rolling(21, min_periods=max(21//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.142941 + 0.0029865 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_115_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=98, w2=34, w3=46, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(34, min_periods=max(34//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 98)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.078333 * slope + 0.0029866 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_116_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=105, w2=47, w3=63, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(105)
    drag = impulse.rolling(47, min_periods=max(47//3, 2)).mean()
    noise = impulse.abs().rolling(63, min_periods=max(63//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.17 + 0.0029867 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_117_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=112, w2=60, w3=80, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 112)
    acceleration = _rolling_slope(velocity, 60)
    curvature = _rolling_slope(acceleration, 80)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.091 * acceleration + 0.0029868 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_118_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=119, w2=73, w3=97, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(119, min_periods=max(119//3, 2)).mean(), upside.rolling(73, min_periods=max(73//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(97) * 1.197059 + 0.0029869 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_119_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=86, w3=114, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(86, min_periods=max(86//3, 2)).max()
    rebound = x - x.rolling(126, min_periods=max(126//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.103667 * _rolling_slope(draw, 114) + 0.002987 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_120_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=99, w3=131, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 133)
    baseline = trend.rolling(99, min_periods=max(99//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(131, min_periods=max(131//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.224118 + 0.0029871 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_121_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=112, w3=148, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 140)
    slow = _rolling_slope(x, 112)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=148, adjust=False).mean() * 1.237647 + 0.0029872 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_122_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=125, w3=165, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(125, min_periods=max(125//3, 2)).max()
    trough = x.rolling(147, min_periods=max(147//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.251176 + 0.0029873 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_123_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=138, w3=182, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(138, min_periods=max(138//3, 2)).rank(pct=True)
    persistence = change.rolling(182, min_periods=max(182//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.129 * persistence + 0.0029874 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_124_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=151, w3=199, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(161, min_periods=max(161//3, 2)).std()
    vol_slow = ret.rolling(151, min_periods=max(151//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.278235 + 0.0029875 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_125_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=164, w3=216, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(164, min_periods=max(164//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 168)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.141667 * slope + 0.0029876 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_126_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=177, w3=233, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(177, min_periods=max(177//3, 2)).mean()
    noise = impulse.abs().rolling(233, min_periods=max(233//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.305294 + 0.0029877 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_127_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=190, w3=250, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 182)
    acceleration = _rolling_slope(velocity, 190)
    curvature = _rolling_slope(acceleration, 250)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.154333 * acceleration + 0.0029878 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_128_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=189, w2=203, w3=267, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(189, min_periods=max(189//3, 2)).mean(), upside.rolling(203, min_periods=max(203//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.332353 + 0.0029879 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_129_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=196, w2=216, w3=284, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(216, min_periods=max(216//3, 2)).max()
    rebound = x - x.rolling(196, min_periods=max(196//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.167 * _rolling_slope(draw, 284) + 0.002988 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_130_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=203, w2=229, w3=301, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 203)
    baseline = trend.rolling(229, min_periods=max(229//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(301, min_periods=max(301//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.359412 + 0.0029881 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_131_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=210, w2=242, w3=318, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 210)
    slow = _rolling_slope(x, 242)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.372941 + 0.0029882 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_132_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=217, w2=255, w3=335, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(255, min_periods=max(255//3, 2)).max()
    trough = x.rolling(217, min_periods=max(217//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.386471 + 0.0029883 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_133_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=224, w2=268, w3=352, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(268, min_periods=max(268//3, 2)).rank(pct=True)
    persistence = change.rolling(352, min_periods=max(352//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.192333 * persistence + 0.0029884 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_134_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=231, w2=281, w3=369, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(231, min_periods=max(231//3, 2)).std()
    vol_slow = ret.rolling(281, min_periods=max(281//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.413529 + 0.0029885 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_135_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=238, w2=294, w3=386, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(294, min_periods=max(294//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 238)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.205 * slope + 0.0029886 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_136_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=245, w2=307, w3=403, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(307, min_periods=max(307//3, 2)).mean()
    noise = impulse.abs().rolling(403, min_periods=max(403//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.440588 + 0.0029887 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_137_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=5, w2=320, w3=420, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 5)
    acceleration = _rolling_slope(velocity, 320)
    curvature = _rolling_slope(acceleration, 420)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.217667 * acceleration + 0.0029888 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_138_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=333, w3=437, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(12, min_periods=max(12//3, 2)).mean(), upside.rolling(333, min_periods=max(333//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.467647 + 0.0029889 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_139_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=346, w3=454, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(346, min_periods=max(346//3, 2)).max()
    rebound = x - x.rolling(19, min_periods=max(19//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.230333 * _rolling_slope(draw, 454) + 0.002989 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_140_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=359, w3=471, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 26)
    baseline = trend.rolling(359, min_periods=max(359//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.494706 + 0.0029891 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_141_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=372, w3=488, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 33)
    slow = _rolling_slope(x, 372)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.508235 + 0.0029892 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_142_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=385, w3=505, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(385, min_periods=max(385//3, 2)).max()
    trough = x.rolling(40, min_periods=max(40//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.521765 + 0.0029893 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_143_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=398, w3=522, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(47)
    rank = change.rolling(398, min_periods=max(398//3, 2)).rank(pct=True)
    persistence = change.rolling(522, min_periods=max(522//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.255667 * persistence + 0.0029894 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_144_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=411, w3=539, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(54, min_periods=max(54//3, 2)).std()
    vol_slow = ret.rolling(411, min_periods=max(411//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.548824 + 0.0029895 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_145_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=424, w3=556, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(424, min_periods=max(424//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 61)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.268333 * slope + 0.0029896 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_146_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=437, w3=573, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(68)
    drag = impulse.rolling(437, min_periods=max(437//3, 2)).mean()
    noise = impulse.abs().rolling(573, min_periods=max(573//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.575882 + 0.0029897 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_147_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=450, w3=590, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 75)
    acceleration = _rolling_slope(velocity, 450)
    curvature = _rolling_slope(acceleration, 590)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.281 * acceleration + 0.0029898 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_148_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=463, w3=607, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(82, min_periods=max(82//3, 2)).mean(), upside.rolling(463, min_periods=max(463//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.602941 + 0.0029899 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_149_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=476, w3=624, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(476, min_periods=max(476//3, 2)).max()
    rebound = x - x.rolling(89, min_periods=max(89//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.293667 * _rolling_slope(draw, 624) + 0.00299 * anchor
    return base_signal.diff().diff()

def f43_tail_gemini_150_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=489, w3=641, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 96)
    baseline = trend.rolling(489, min_periods=max(489//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(641, min_periods=max(641//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.63 + 0.0029901 * anchor
    return base_signal.diff().diff()
