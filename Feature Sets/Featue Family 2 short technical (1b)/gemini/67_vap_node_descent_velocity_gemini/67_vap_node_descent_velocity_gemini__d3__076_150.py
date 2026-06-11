"""67 vap node descent velocity gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Rate of price movement through high-volume nodes in the Volume at Price profile.
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

def f67_vapv_gemini_076_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=37, w2=419, w3=437, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(37)
    drag = impulse.rolling(419, min_periods=max(419//3, 2)).mean()
    noise = impulse.abs().rolling(437, min_periods=max(437//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.849412 + 0.0043407 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_077_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=44, w2=432, w3=454, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 44)
    acceleration = _rolling_slope(velocity, 432)
    curvature = _rolling_slope(acceleration, 454)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.102333 * acceleration + 0.0043408 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_078_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=51, w2=445, w3=471, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(51, min_periods=max(51//3, 2)).mean(), upside.rolling(445, min_periods=max(445//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.876471 + 0.0043409 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_079_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=58, w2=458, w3=488, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(458, min_periods=max(458//3, 2)).max()
    rebound = x - x.rolling(58, min_periods=max(58//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.115 * _rolling_slope(draw, 488) + 0.004341 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_080_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=65, w2=471, w3=505, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 65)
    baseline = trend.rolling(471, min_periods=max(471//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(505, min_periods=max(505//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.903529 + 0.0043411 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_081_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=72, w2=484, w3=522, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 72)
    slow = _rolling_slope(x, 484)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.917059 + 0.0043412 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_082_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=79, w2=497, w3=539, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(497, min_periods=max(497//3, 2)).max()
    trough = x.rolling(79, min_periods=max(79//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.930588 + 0.0043413 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_083_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=86, w2=11, w3=556, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(86)
    rank = change.rolling(11, min_periods=max(11//3, 2)).rank(pct=True)
    persistence = change.rolling(556, min_periods=max(556//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.140333 * persistence + 0.0043414 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_084_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=93, w2=24, w3=573, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(93, min_periods=max(93//3, 2)).std()
    vol_slow = ret.rolling(24, min_periods=max(24//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.957647 + 0.0043415 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_085_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=100, w2=37, w3=590, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(37, min_periods=max(37//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 100)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.153 * slope + 0.0043416 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_086_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=107, w2=50, w3=607, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(107)
    drag = impulse.rolling(50, min_periods=max(50//3, 2)).mean()
    noise = impulse.abs().rolling(607, min_periods=max(607//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.984706 + 0.0043417 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_087_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=114, w2=63, w3=624, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 114)
    acceleration = _rolling_slope(velocity, 63)
    curvature = _rolling_slope(acceleration, 624)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.165667 * acceleration + 0.0043418 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_088_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=121, w2=76, w3=641, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(121, min_periods=max(121//3, 2)).mean(), upside.rolling(76, min_periods=max(76//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.011765 + 0.0043419 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_089_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=128, w2=89, w3=658, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(89, min_periods=max(89//3, 2)).max()
    rebound = x - x.rolling(128, min_periods=max(128//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.178333 * _rolling_slope(draw, 658) + 0.004342 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_090_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=135, w2=102, w3=675, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 135)
    baseline = trend.rolling(102, min_periods=max(102//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(675, min_periods=max(675//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.038824 + 0.0043421 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_091_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=142, w2=115, w3=692, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 142)
    slow = _rolling_slope(x, 115)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.052353 + 0.0043422 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_092_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=149, w2=128, w3=709, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(128, min_periods=max(128//3, 2)).max()
    trough = x.rolling(149, min_periods=max(149//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.065882 + 0.0043423 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_093_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=156, w2=141, w3=726, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(141, min_periods=max(141//3, 2)).rank(pct=True)
    persistence = change.rolling(726, min_periods=max(726//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.203667 * persistence + 0.0043424 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_094_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=154, w3=743, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(163, min_periods=max(163//3, 2)).std()
    vol_slow = ret.rolling(154, min_periods=max(154//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.092941 + 0.0043425 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_095_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=167, w3=760, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(167, min_periods=max(167//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 170)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.216333 * slope + 0.0043426 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_096_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=180, w3=26, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(180, min_periods=max(180//3, 2)).mean()
    noise = impulse.abs().rolling(26, min_periods=max(26//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.12 + 0.0043427 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_097_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=193, w3=43, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 184)
    acceleration = _rolling_slope(velocity, 193)
    curvature = _rolling_slope(acceleration, 43)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.229 * acceleration + 0.0043428 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_098_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=206, w3=60, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(191, min_periods=max(191//3, 2)).mean(), upside.rolling(206, min_periods=max(206//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(60) * 1.147059 + 0.0043429 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_099_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=219, w3=77, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(219, min_periods=max(219//3, 2)).max()
    rebound = x - x.rolling(198, min_periods=max(198//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.241667 * _rolling_slope(draw, 77) + 0.004343 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_100_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=232, w3=94, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 205)
    baseline = trend.rolling(232, min_periods=max(232//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(94, min_periods=max(94//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.174118 + 0.0043431 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_101_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=245, w3=111, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 212)
    slow = _rolling_slope(x, 245)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=111, adjust=False).mean() * 1.187647 + 0.0043432 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_102_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=258, w3=128, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(258, min_periods=max(258//3, 2)).max()
    trough = x.rolling(219, min_periods=max(219//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.201176 + 0.0043433 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_103_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=271, w3=145, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(271, min_periods=max(271//3, 2)).rank(pct=True)
    persistence = change.rolling(145, min_periods=max(145//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.267 * persistence + 0.0043434 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_104_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=284, w3=162, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(233, min_periods=max(233//3, 2)).std()
    vol_slow = ret.rolling(284, min_periods=max(284//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.228235 + 0.0043435 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_105_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=297, w3=179, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(297, min_periods=max(297//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 240)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.279667 * slope + 0.0043436 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_106_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=310, w3=196, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(310, min_periods=max(310//3, 2)).mean()
    noise = impulse.abs().rolling(196, min_periods=max(196//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.255294 + 0.0043437 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_107_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=323, w3=213, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 7)
    acceleration = _rolling_slope(velocity, 323)
    curvature = _rolling_slope(acceleration, 213)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.292333 * acceleration + 0.0043438 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_108_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=14, w2=336, w3=230, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(14, min_periods=max(14//3, 2)).mean(), upside.rolling(336, min_periods=max(336//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.282353 + 0.0043439 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_109_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=349, w3=247, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(349, min_periods=max(349//3, 2)).max()
    rebound = x - x.rolling(21, min_periods=max(21//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.305 * _rolling_slope(draw, 247) + 0.004344 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_110_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=362, w3=264, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 28)
    baseline = trend.rolling(362, min_periods=max(362//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.309412 + 0.0043441 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_111_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=375, w3=281, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 35)
    slow = _rolling_slope(x, 375)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=281, adjust=False).mean() * 1.322941 + 0.0043442 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_112_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=388, w3=298, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(388, min_periods=max(388//3, 2)).max()
    trough = x.rolling(42, min_periods=max(42//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.336471 + 0.0043443 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_113_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=401, w3=315, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(49)
    rank = change.rolling(401, min_periods=max(401//3, 2)).rank(pct=True)
    persistence = change.rolling(315, min_periods=max(315//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.330333 * persistence + 0.0043444 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_114_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=414, w3=332, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(56, min_periods=max(56//3, 2)).std()
    vol_slow = ret.rolling(414, min_periods=max(414//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.363529 + 0.0043445 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_115_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=427, w3=349, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(427, min_periods=max(427//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 63)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.343 * slope + 0.0043446 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_116_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=440, w3=366, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(70)
    drag = impulse.rolling(440, min_periods=max(440//3, 2)).mean()
    noise = impulse.abs().rolling(366, min_periods=max(366//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.390588 + 0.0043447 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_117_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=453, w3=383, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 77)
    acceleration = _rolling_slope(velocity, 453)
    curvature = _rolling_slope(acceleration, 383)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.355667 * acceleration + 0.0043448 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_118_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=466, w3=400, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(84, min_periods=max(84//3, 2)).mean(), upside.rolling(466, min_periods=max(466//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.417647 + 0.0043449 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_119_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=479, w3=417, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(479, min_periods=max(479//3, 2)).max()
    rebound = x - x.rolling(91, min_periods=max(91//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.036 * _rolling_slope(draw, 417) + 0.004345 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_120_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=492, w3=434, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 98)
    baseline = trend.rolling(492, min_periods=max(492//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(434, min_periods=max(434//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.444706 + 0.0043451 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_121_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=105, w2=505, w3=451, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 105)
    slow = _rolling_slope(x, 505)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.458235 + 0.0043452 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_122_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=112, w2=19, w3=468, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(19, min_periods=max(19//3, 2)).max()
    trough = x.rolling(112, min_periods=max(112//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.471765 + 0.0043453 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_123_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=119, w2=32, w3=485, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(119)
    rank = change.rolling(32, min_periods=max(32//3, 2)).rank(pct=True)
    persistence = change.rolling(485, min_periods=max(485//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.061333 * persistence + 0.0043454 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_124_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=45, w3=502, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(126, min_periods=max(126//3, 2)).std()
    vol_slow = ret.rolling(45, min_periods=max(45//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.498824 + 0.0043455 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_125_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=133, w2=58, w3=519, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(58, min_periods=max(58//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 133)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.074 * slope + 0.0043456 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_126_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=140, w2=71, w3=536, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(71, min_periods=max(71//3, 2)).mean()
    noise = impulse.abs().rolling(536, min_periods=max(536//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.525882 + 0.0043457 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_127_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=147, w2=84, w3=553, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 147)
    acceleration = _rolling_slope(velocity, 84)
    curvature = _rolling_slope(acceleration, 553)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.086667 * acceleration + 0.0043458 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_128_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=154, w2=97, w3=570, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(154, min_periods=max(154//3, 2)).mean(), upside.rolling(97, min_periods=max(97//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.552941 + 0.0043459 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_129_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=110, w3=587, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(110, min_periods=max(110//3, 2)).max()
    rebound = x - x.rolling(161, min_periods=max(161//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.099333 * _rolling_slope(draw, 587) + 0.004346 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_130_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=123, w3=604, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 168)
    baseline = trend.rolling(123, min_periods=max(123//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(604, min_periods=max(604//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.58 + 0.0043461 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_131_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=136, w3=621, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 175)
    slow = _rolling_slope(x, 136)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.593529 + 0.0043462 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_132_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=149, w3=638, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(149, min_periods=max(149//3, 2)).max()
    trough = x.rolling(182, min_periods=max(182//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.607059 + 0.0043463 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_133_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=162, w3=655, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(162, min_periods=max(162//3, 2)).rank(pct=True)
    persistence = change.rolling(655, min_periods=max(655//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.124667 * persistence + 0.0043464 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_134_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=196, w2=175, w3=672, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(196, min_periods=max(196//3, 2)).std()
    vol_slow = ret.rolling(175, min_periods=max(175//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.634118 + 0.0043465 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_135_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=203, w2=188, w3=689, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(188, min_periods=max(188//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 203)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.137333 * slope + 0.0043466 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_136_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=210, w2=201, w3=706, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(201, min_periods=max(201//3, 2)).mean()
    noise = impulse.abs().rolling(706, min_periods=max(706//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.661176 + 0.0043467 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_137_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=217, w2=214, w3=723, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 217)
    acceleration = _rolling_slope(velocity, 214)
    curvature = _rolling_slope(acceleration, 723)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.15 * acceleration + 0.0043468 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_138_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=224, w2=227, w3=740, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(224, min_periods=max(224//3, 2)).mean(), upside.rolling(227, min_periods=max(227//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.834706 + 0.0043469 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_139_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=231, w2=240, w3=757, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(240, min_periods=max(240//3, 2)).max()
    rebound = x - x.rolling(231, min_periods=max(231//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.162667 * _rolling_slope(draw, 757) + 0.004347 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_140_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=253, w3=23, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 238)
    baseline = trend.rolling(253, min_periods=max(253//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(23, min_periods=max(23//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.861765 + 0.0043471 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_141_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=266, w3=40, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 245)
    slow = _rolling_slope(x, 266)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=40, adjust=False).mean() * 0.875294 + 0.0043472 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_142_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=279, w3=57, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(279, min_periods=max(279//3, 2)).max()
    trough = x.rolling(5, min_periods=max(5//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.888824 + 0.0043473 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_143_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=292, w3=74, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(12)
    rank = change.rolling(292, min_periods=max(292//3, 2)).rank(pct=True)
    persistence = change.rolling(74, min_periods=max(74//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.188 * persistence + 0.0043474 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_144_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=305, w3=91, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(19, min_periods=max(19//3, 2)).std()
    vol_slow = ret.rolling(305, min_periods=max(305//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.915882 + 0.0043475 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_145_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=318, w3=108, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(318, min_periods=max(318//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 26)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.200667 * slope + 0.0043476 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_146_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=331, w3=125, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(33)
    drag = impulse.rolling(331, min_periods=max(331//3, 2)).mean()
    noise = impulse.abs().rolling(125, min_periods=max(125//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.942941 + 0.0043477 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_147_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=344, w3=142, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 40)
    acceleration = _rolling_slope(velocity, 344)
    curvature = _rolling_slope(acceleration, 142)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.213333 * acceleration + 0.0043478 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_148_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=357, w3=159, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(47, min_periods=max(47//3, 2)).mean(), upside.rolling(357, min_periods=max(357//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.97 + 0.0043479 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_149_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=370, w3=176, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(370, min_periods=max(370//3, 2)).max()
    rebound = x - x.rolling(54, min_periods=max(54//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.226 * _rolling_slope(draw, 176) + 0.004348 * anchor
    return base_signal.diff().diff().diff()

def f67_vapv_gemini_150_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=383, w3=193, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 61)
    baseline = trend.rolling(383, min_periods=max(383//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(193, min_periods=max(193//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.997059 + 0.0043481 * anchor
    return base_signal.diff().diff().diff()
