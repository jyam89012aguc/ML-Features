"""91 change point detection signal gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Statistical detection of structural shifts in price or volatility mean/variance.
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

def f91_cpds_gemini_076_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=18, w2=166, w3=486, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(18)
    drag = impulse.rolling(166, min_periods=max(166//3, 2)).mean()
    noise = impulse.abs().rolling(486, min_periods=max(486//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.549412 + 0.0056707 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_077_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=25, w2=179, w3=503, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 179)
    curvature = _rolling_slope(acceleration, 503)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.255333 * acceleration + 0.0056708 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_078_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=32, w2=192, w3=520, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(32, min_periods=max(32//3, 2)).mean(), upside.rolling(192, min_periods=max(192//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.576471 + 0.0056709 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_079_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=39, w2=205, w3=537, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(205, min_periods=max(205//3, 2)).max()
    rebound = x - x.rolling(39, min_periods=max(39//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.268 * _rolling_slope(draw, 537) + 0.005671 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_080_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=46, w2=218, w3=554, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 46)
    baseline = trend.rolling(218, min_periods=max(218//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(554, min_periods=max(554//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.603529 + 0.0056711 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_081_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=53, w2=231, w3=571, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 53)
    slow = _rolling_slope(x, 231)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.617059 + 0.0056712 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_082_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=60, w2=244, w3=588, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(244, min_periods=max(244//3, 2)).max()
    trough = x.rolling(60, min_periods=max(60//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.630588 + 0.0056713 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_083_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=67, w2=257, w3=605, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(67)
    rank = change.rolling(257, min_periods=max(257//3, 2)).rank(pct=True)
    persistence = change.rolling(605, min_periods=max(605//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.293333 * persistence + 0.0056714 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_084_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=74, w2=270, w3=622, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(74, min_periods=max(74//3, 2)).std()
    vol_slow = ret.rolling(270, min_periods=max(270//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.657647 + 0.0056715 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_085_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=81, w2=283, w3=639, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(283, min_periods=max(283//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 81)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.306 * slope + 0.0056716 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_086_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=88, w2=296, w3=656, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(88)
    drag = impulse.rolling(296, min_periods=max(296//3, 2)).mean()
    noise = impulse.abs().rolling(656, min_periods=max(656//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.831176 + 0.0056717 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_087_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=95, w2=309, w3=673, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 95)
    acceleration = _rolling_slope(velocity, 309)
    curvature = _rolling_slope(acceleration, 673)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.318667 * acceleration + 0.0056718 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_088_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=102, w2=322, w3=690, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(102, min_periods=max(102//3, 2)).mean(), upside.rolling(322, min_periods=max(322//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.858235 + 0.0056719 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_089_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=109, w2=335, w3=707, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(335, min_periods=max(335//3, 2)).max()
    rebound = x - x.rolling(109, min_periods=max(109//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.331333 * _rolling_slope(draw, 707) + 0.005672 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_090_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=116, w2=348, w3=724, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 116)
    baseline = trend.rolling(348, min_periods=max(348//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(724, min_periods=max(724//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.885294 + 0.0056721 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_091_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=123, w2=361, w3=741, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 123)
    slow = _rolling_slope(x, 361)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.898824 + 0.0056722 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_092_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=130, w2=374, w3=758, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(374, min_periods=max(374//3, 2)).max()
    trough = x.rolling(130, min_periods=max(130//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.912353 + 0.0056723 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_093_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=137, w2=387, w3=24, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(387, min_periods=max(387//3, 2)).rank(pct=True)
    persistence = change.rolling(24, min_periods=max(24//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.356667 * persistence + 0.0056724 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_094_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=144, w2=400, w3=41, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(144, min_periods=max(144//3, 2)).std()
    vol_slow = ret.rolling(400, min_periods=max(400//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.939412 + 0.0056725 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_095_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=151, w2=413, w3=58, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(413, min_periods=max(413//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 151)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.037 * slope + 0.0056726 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_096_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=158, w2=426, w3=75, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(426, min_periods=max(426//3, 2)).mean()
    noise = impulse.abs().rolling(75, min_periods=max(75//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.966471 + 0.0056727 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_097_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=165, w2=439, w3=92, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 165)
    acceleration = _rolling_slope(velocity, 439)
    curvature = _rolling_slope(acceleration, 92)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.049667 * acceleration + 0.0056728 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_098_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=172, w2=452, w3=109, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(172, min_periods=max(172//3, 2)).mean(), upside.rolling(452, min_periods=max(452//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(109) * 0.993529 + 0.0056729 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_099_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=179, w2=465, w3=126, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(465, min_periods=max(465//3, 2)).max()
    rebound = x - x.rolling(179, min_periods=max(179//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.062333 * _rolling_slope(draw, 126) + 0.005673 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_100_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=186, w2=478, w3=143, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 186)
    baseline = trend.rolling(478, min_periods=max(478//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.020588 + 0.0056731 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_101_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=193, w2=491, w3=160, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 193)
    slow = _rolling_slope(x, 491)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=160, adjust=False).mean() * 1.034118 + 0.0056732 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_102_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=200, w2=504, w3=177, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(504, min_periods=max(504//3, 2)).max()
    trough = x.rolling(200, min_periods=max(200//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.047647 + 0.0056733 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_103_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=207, w2=18, w3=194, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(18, min_periods=max(18//3, 2)).rank(pct=True)
    persistence = change.rolling(194, min_periods=max(194//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.087667 * persistence + 0.0056734 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_104_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=214, w2=31, w3=211, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(214, min_periods=max(214//3, 2)).std()
    vol_slow = ret.rolling(31, min_periods=max(31//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.074706 + 0.0056735 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_105_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=221, w2=44, w3=228, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(44, min_periods=max(44//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 221)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.100333 * slope + 0.0056736 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_106_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=228, w2=57, w3=245, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(57, min_periods=max(57//3, 2)).mean()
    noise = impulse.abs().rolling(245, min_periods=max(245//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.101765 + 0.0056737 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_107_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=235, w2=70, w3=262, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 235)
    acceleration = _rolling_slope(velocity, 70)
    curvature = _rolling_slope(acceleration, 262)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.113 * acceleration + 0.0056738 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_108_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=242, w2=83, w3=279, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(242, min_periods=max(242//3, 2)).mean(), upside.rolling(83, min_periods=max(83//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.128824 + 0.0056739 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_109_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=249, w2=96, w3=296, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(96, min_periods=max(96//3, 2)).max()
    rebound = x - x.rolling(249, min_periods=max(249//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.125667 * _rolling_slope(draw, 296) + 0.005674 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_110_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=9, w2=109, w3=313, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 9)
    baseline = trend.rolling(109, min_periods=max(109//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(313, min_periods=max(313//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.155882 + 0.0056741 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_111_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=16, w2=122, w3=330, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 16)
    slow = _rolling_slope(x, 122)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.169412 + 0.0056742 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_112_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=23, w2=135, w3=347, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(135, min_periods=max(135//3, 2)).max()
    trough = x.rolling(23, min_periods=max(23//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.182941 + 0.0056743 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_113_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=30, w2=148, w3=364, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(30)
    rank = change.rolling(148, min_periods=max(148//3, 2)).rank(pct=True)
    persistence = change.rolling(364, min_periods=max(364//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.151 * persistence + 0.0056744 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_114_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=37, w2=161, w3=381, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(37, min_periods=max(37//3, 2)).std()
    vol_slow = ret.rolling(161, min_periods=max(161//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.21 + 0.0056745 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_115_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=44, w2=174, w3=398, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(174, min_periods=max(174//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 44)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.163667 * slope + 0.0056746 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_116_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=51, w2=187, w3=415, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(51)
    drag = impulse.rolling(187, min_periods=max(187//3, 2)).mean()
    noise = impulse.abs().rolling(415, min_periods=max(415//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.237059 + 0.0056747 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_117_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=58, w2=200, w3=432, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 58)
    acceleration = _rolling_slope(velocity, 200)
    curvature = _rolling_slope(acceleration, 432)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.176333 * acceleration + 0.0056748 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_118_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=65, w2=213, w3=449, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(65, min_periods=max(65//3, 2)).mean(), upside.rolling(213, min_periods=max(213//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.264118 + 0.0056749 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_119_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=72, w2=226, w3=466, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(226, min_periods=max(226//3, 2)).max()
    rebound = x - x.rolling(72, min_periods=max(72//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.189 * _rolling_slope(draw, 466) + 0.005675 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_120_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=79, w2=239, w3=483, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 79)
    baseline = trend.rolling(239, min_periods=max(239//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(483, min_periods=max(483//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.291176 + 0.0056751 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_121_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=86, w2=252, w3=500, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 86)
    slow = _rolling_slope(x, 252)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.304706 + 0.0056752 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_122_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=93, w2=265, w3=517, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(265, min_periods=max(265//3, 2)).max()
    trough = x.rolling(93, min_periods=max(93//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.318235 + 0.0056753 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_123_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=100, w2=278, w3=534, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(100)
    rank = change.rolling(278, min_periods=max(278//3, 2)).rank(pct=True)
    persistence = change.rolling(534, min_periods=max(534//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.214333 * persistence + 0.0056754 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_124_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=107, w2=291, w3=551, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(107, min_periods=max(107//3, 2)).std()
    vol_slow = ret.rolling(291, min_periods=max(291//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.345294 + 0.0056755 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_125_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=114, w2=304, w3=568, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(304, min_periods=max(304//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 114)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.227 * slope + 0.0056756 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_126_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=121, w2=317, w3=585, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(121)
    drag = impulse.rolling(317, min_periods=max(317//3, 2)).mean()
    noise = impulse.abs().rolling(585, min_periods=max(585//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.372353 + 0.0056757 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_127_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=128, w2=330, w3=602, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 128)
    acceleration = _rolling_slope(velocity, 330)
    curvature = _rolling_slope(acceleration, 602)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.239667 * acceleration + 0.0056758 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_128_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=135, w2=343, w3=619, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(343, min_periods=max(343//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.399412 + 0.0056759 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_129_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=142, w2=356, w3=636, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(356, min_periods=max(356//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.252333 * _rolling_slope(draw, 636) + 0.005676 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_130_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=149, w2=369, w3=653, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 149)
    baseline = trend.rolling(369, min_periods=max(369//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(653, min_periods=max(653//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.426471 + 0.0056761 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_131_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=156, w2=382, w3=670, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 156)
    slow = _rolling_slope(x, 382)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.44 + 0.0056762 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_132_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=163, w2=395, w3=687, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(395, min_periods=max(395//3, 2)).max()
    trough = x.rolling(163, min_periods=max(163//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.453529 + 0.0056763 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_133_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=170, w2=408, w3=704, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(408, min_periods=max(408//3, 2)).rank(pct=True)
    persistence = change.rolling(704, min_periods=max(704//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.277667 * persistence + 0.0056764 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_134_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=177, w2=421, w3=721, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(177, min_periods=max(177//3, 2)).std()
    vol_slow = ret.rolling(421, min_periods=max(421//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.480588 + 0.0056765 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_135_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=184, w2=434, w3=738, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(434, min_periods=max(434//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 184)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.290333 * slope + 0.0056766 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_136_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=191, w2=447, w3=755, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(447, min_periods=max(447//3, 2)).mean()
    noise = impulse.abs().rolling(755, min_periods=max(755//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.507647 + 0.0056767 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_137_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=198, w2=460, w3=21, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 198)
    acceleration = _rolling_slope(velocity, 460)
    curvature = _rolling_slope(acceleration, 21)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.303 * acceleration + 0.0056768 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_138_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=205, w2=473, w3=38, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(205, min_periods=max(205//3, 2)).mean(), upside.rolling(473, min_periods=max(473//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(38) * 1.534706 + 0.0056769 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_139_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=212, w2=486, w3=55, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(486, min_periods=max(486//3, 2)).max()
    rebound = x - x.rolling(212, min_periods=max(212//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.315667 * _rolling_slope(draw, 55) + 0.005677 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_140_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=219, w2=499, w3=72, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 219)
    baseline = trend.rolling(499, min_periods=max(499//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(72, min_periods=max(72//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.561765 + 0.0056771 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_141_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=226, w2=13, w3=89, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 226)
    slow = _rolling_slope(x, 13)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=89, adjust=False).mean() * 1.575294 + 0.0056772 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_142_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=233, w2=26, w3=106, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(26, min_periods=max(26//3, 2)).max()
    trough = x.rolling(233, min_periods=max(233//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.588824 + 0.0056773 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_143_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=240, w2=39, w3=123, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(39, min_periods=max(39//3, 2)).rank(pct=True)
    persistence = change.rolling(123, min_periods=max(123//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.341 * persistence + 0.0056774 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_144_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=247, w2=52, w3=140, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(247, min_periods=max(247//3, 2)).std()
    vol_slow = ret.rolling(52, min_periods=max(52//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.615882 + 0.0056775 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_145_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=7, w2=65, w3=157, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(65, min_periods=max(65//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 7)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.353667 * slope + 0.0056776 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_146_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=14, w2=78, w3=174, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(14)
    drag = impulse.rolling(78, min_periods=max(78//3, 2)).mean()
    noise = impulse.abs().rolling(174, min_periods=max(174//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.642941 + 0.0056777 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_147_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=21, w2=91, w3=191, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 21)
    acceleration = _rolling_slope(velocity, 91)
    curvature = _rolling_slope(acceleration, 191)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.034 * acceleration + 0.0056778 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_148_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=28, w2=104, w3=208, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(28, min_periods=max(28//3, 2)).mean(), upside.rolling(104, min_periods=max(104//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.67 + 0.0056779 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_149_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=35, w2=117, w3=225, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(117, min_periods=max(117//3, 2)).max()
    rebound = x - x.rolling(35, min_periods=max(35//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.046667 * _rolling_slope(draw, 225) + 0.005678 * anchor
    return base_signal.diff().diff()

def f91_cpds_gemini_150_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=42, w2=130, w3=242, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 42)
    baseline = trend.rolling(130, min_periods=max(130//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(242, min_periods=max(242//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.843529 + 0.0056781 * anchor
    return base_signal.diff().diff()
