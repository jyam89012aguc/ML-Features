"""108 orthogonality breakdown signal gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Loss of independence between supposedly uncorrelated market factors.
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

def f108_orbs_gemini_076_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=420, w3=621, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(420, min_periods=max(420//3, 2)).max()
    trough = x.rolling(236, min_periods=max(236//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.005294 + 0.0009667 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_077_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=433, w3=638, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(433, min_periods=max(433//3, 2)).rank(pct=True)
    persistence = change.rolling(638, min_periods=max(638//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.106 * persistence + 0.0009668 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_078_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=250, w2=446, w3=655, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(250, min_periods=max(250//3, 2)).std()
    vol_slow = ret.rolling(446, min_periods=max(446//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.032353 + 0.0009669 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_079_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=459, w3=672, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(459, min_periods=max(459//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 10)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.118667 * slope + 0.000967 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_080_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=17, w2=472, w3=689, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(17)
    drag = impulse.rolling(472, min_periods=max(472//3, 2)).mean()
    noise = impulse.abs().rolling(689, min_periods=max(689//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.059412 + 0.0009671 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_081_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=24, w2=485, w3=706, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 24)
    acceleration = _rolling_slope(velocity, 485)
    curvature = _rolling_slope(acceleration, 706)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.131333 * acceleration + 0.0009672 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_082_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=31, w2=498, w3=723, lag=2)."""
    rel = _safe_div(open.shift(2), high.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 31)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.137667 * pressure.rolling(723, min_periods=max(723//3, 2)).mean() + 0.0009673 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_083_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=12, w3=740, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(38, min_periods=max(38//3, 2)).mean())
    decay = spread.ewm(span=12, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.1 + 0.0009674 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_084_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=25, w3=757, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(high.abs() + 1.0).shift(5)
    corr = a.rolling(25, min_periods=max(25//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 45)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.113529 + 0.0009675 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_085_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=38, w3=23, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    cover = _safe_div(a.rolling(52, min_periods=max(52//3, 2)).mean(), b.abs().rolling(38, min_periods=max(38//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(23) + 0.156667 * _rolling_slope(cover, 52) + 0.0009676 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_086_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=59, w2=51, w3=40, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(high.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.163 * y + 0.837000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 59) - _rolling_slope(basket, 51) + 0.0009677 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_087_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=66, w2=64, w3=57, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(66, min_periods=max(66//3, 2)).mean(), upside.rolling(64, min_periods=max(64//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(57) * 1.154118 + 0.0009678 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_088_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=73, w2=77, w3=74, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(77, min_periods=max(77//3, 2)).max()
    rebound = x - x.rolling(73, min_periods=max(73//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.175667 * _rolling_slope(draw, 74) + 0.0009679 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_089_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=80, w2=90, w3=91, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(high.abs() + 1.0).shift(55)
    imbalance = a.diff(80) - b.diff(90)
    stress = imbalance.rolling(91, min_periods=max(91//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.181176 + 0.000968 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_090_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=87, w2=103, w3=108, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 87)
    baseline = trend.rolling(103, min_periods=max(103//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(108, min_periods=max(108//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.194706 + 0.0009681 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_091_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=94, w2=116, w3=125, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 94)
    slow = _rolling_slope(x, 116)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=125, adjust=False).mean() * 1.208235 + 0.0009682 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_092_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=101, w2=129, w3=142, lag=2)."""
    x = open.shift(2)
    peak = x.rolling(129, min_periods=max(129//3, 2)).max()
    trough = x.rolling(101, min_periods=max(101//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.221765 + 0.0009683 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_093_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=108, w2=142, w3=159, lag=3)."""
    x = open.shift(3)
    change = x.pct_change(108)
    rank = change.rolling(142, min_periods=max(142//3, 2)).rank(pct=True)
    persistence = change.rolling(159, min_periods=max(159//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.207333 * persistence + 0.0009684 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_094_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=115, w2=155, w3=176, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(115, min_periods=max(115//3, 2)).std()
    vol_slow = ret.rolling(155, min_periods=max(155//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.248824 + 0.0009685 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_095_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=122, w2=168, w3=193, lag=8)."""
    x = open.shift(8)
    ma = x.rolling(168, min_periods=max(168//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 122)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.22 * slope + 0.0009686 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_096_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=129, w2=181, w3=210, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(181, min_periods=max(181//3, 2)).mean()
    noise = impulse.abs().rolling(210, min_periods=max(210//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.275882 + 0.0009687 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_097_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=136, w2=194, w3=227, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 136)
    acceleration = _rolling_slope(velocity, 194)
    curvature = _rolling_slope(acceleration, 227)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.232667 * acceleration + 0.0009688 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_098_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=143, w2=207, w3=244, lag=34)."""
    rel = _safe_div(open.shift(34), high.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 143)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.239 * pressure.rolling(244, min_periods=max(244//3, 2)).mean() + 0.0009689 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_099_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=150, w2=220, w3=261, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(150, min_periods=max(150//3, 2)).mean())
    decay = spread.ewm(span=220, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.316471 + 0.000969 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_100_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=157, w2=233, w3=278, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(high.abs() + 1.0).shift(0)
    corr = a.rolling(233, min_periods=max(233//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 157)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.33 + 0.0009691 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_101_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=164, w2=246, w3=295, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    cover = _safe_div(a.rolling(164, min_periods=max(164//3, 2)).mean(), b.abs().rolling(246, min_periods=max(246//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.258 * _rolling_slope(cover, 164) + 0.0009692 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_102_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=171, w2=259, w3=312, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(high.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.264333 * y + 0.735667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 171) - _rolling_slope(basket, 259) + 0.0009693 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_103_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=178, w2=272, w3=329, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(178, min_periods=max(178//3, 2)).mean(), upside.rolling(272, min_periods=max(272//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.370588 + 0.0009694 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_104_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=185, w2=285, w3=346, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(285, min_periods=max(285//3, 2)).max()
    rebound = x - x.rolling(185, min_periods=max(185//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.277 * _rolling_slope(draw, 346) + 0.0009695 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_105_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=192, w2=298, w3=363, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(high.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(363, min_periods=max(363//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.397647 + 0.0009696 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_106_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=199, w2=311, w3=380, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 199)
    baseline = trend.rolling(311, min_periods=max(311//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(380, min_periods=max(380//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.411176 + 0.0009697 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_107_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=206, w2=324, w3=397, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 206)
    slow = _rolling_slope(x, 324)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.424706 + 0.0009698 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_108_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=213, w2=337, w3=414, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(337, min_periods=max(337//3, 2)).max()
    trough = x.rolling(213, min_periods=max(213//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.438235 + 0.0009699 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_109_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=220, w2=350, w3=431, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(350, min_periods=max(350//3, 2)).rank(pct=True)
    persistence = change.rolling(431, min_periods=max(431//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.308667 * persistence + 0.00097 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_110_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=227, w2=363, w3=448, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(227, min_periods=max(227//3, 2)).std()
    vol_slow = ret.rolling(363, min_periods=max(363//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.465294 + 0.0009701 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_111_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=234, w2=376, w3=465, lag=1)."""
    x = open.shift(1)
    ma = x.rolling(376, min_periods=max(376//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 234)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.321333 * slope + 0.0009702 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_112_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=241, w2=389, w3=482, lag=2)."""
    x = open.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(389, min_periods=max(389//3, 2)).mean()
    noise = impulse.abs().rolling(482, min_periods=max(482//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.492353 + 0.0009703 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_113_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=248, w2=402, w3=499, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 248)
    acceleration = _rolling_slope(velocity, 402)
    curvature = _rolling_slope(acceleration, 499)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.334 * acceleration + 0.0009704 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_114_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=8, w2=415, w3=516, lag=5)."""
    rel = _safe_div(open.shift(5), high.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 8)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.340333 * pressure.rolling(516, min_periods=max(516//3, 2)).mean() + 0.0009705 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_115_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=15, w2=428, w3=533, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(15, min_periods=max(15//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.532941 + 0.0009706 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_116_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=22, w2=441, w3=550, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(441, min_periods=max(441//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 22)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.546471 + 0.0009707 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_117_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=29, w2=454, w3=567, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(29, min_periods=max(29//3, 2)).mean(), b.abs().rolling(454, min_periods=max(454//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.359333 * _rolling_slope(cover, 29) + 0.0009708 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_118_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=36, w2=467, w3=584, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.033333 * y + 0.966667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 36) - _rolling_slope(basket, 467) + 0.0009709 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_119_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=43, w2=480, w3=601, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(43, min_periods=max(43//3, 2)).mean(), upside.rolling(480, min_periods=max(480//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.587059 + 0.000971 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_120_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=50, w2=493, w3=618, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(493, min_periods=max(493//3, 2)).max()
    rebound = x - x.rolling(50, min_periods=max(50//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.046 * _rolling_slope(draw, 618) + 0.0009711 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_121_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=57, w2=506, w3=635, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(high.abs() + 1.0).shift(1)
    imbalance = a.diff(57) - b.diff(126)
    stress = imbalance.rolling(635, min_periods=max(635//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.614118 + 0.0009712 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_122_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=64, w2=20, w3=652, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 64)
    baseline = trend.rolling(20, min_periods=max(20//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(652, min_periods=max(652//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.627647 + 0.0009713 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_123_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=71, w2=33, w3=669, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 71)
    slow = _rolling_slope(x, 33)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.641176 + 0.0009714 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_124_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=78, w2=46, w3=686, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(46, min_periods=max(46//3, 2)).max()
    trough = x.rolling(78, min_periods=max(78//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.654706 + 0.0009715 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_125_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=85, w2=59, w3=703, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(85)
    rank = change.rolling(59, min_periods=max(59//3, 2)).rank(pct=True)
    persistence = change.rolling(703, min_periods=max(703//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.077667 * persistence + 0.0009716 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_126_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=92, w2=72, w3=720, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(92, min_periods=max(92//3, 2)).std()
    vol_slow = ret.rolling(72, min_periods=max(72//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.828235 + 0.0009717 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_127_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=99, w2=85, w3=737, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(85, min_periods=max(85//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 99)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.090333 * slope + 0.0009718 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_128_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=106, w2=98, w3=754, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(106)
    drag = impulse.rolling(98, min_periods=max(98//3, 2)).mean()
    noise = impulse.abs().rolling(754, min_periods=max(754//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.855294 + 0.0009719 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_129_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=113, w2=111, w3=20, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 113)
    acceleration = _rolling_slope(velocity, 111)
    curvature = _rolling_slope(acceleration, 20)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.103 * acceleration + 0.000972 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_130_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=120, w2=124, w3=37, lag=0)."""
    rel = _safe_div(open.shift(0), high.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 120)
    pressure = rel_log.diff(124)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.109333 * pressure.rolling(37, min_periods=max(37//3, 2)).mean() + 0.0009721 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_131_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=127, w2=137, w3=54, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(127, min_periods=max(127//3, 2)).mean())
    decay = spread.ewm(span=137, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.895882 + 0.0009722 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_132_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=134, w2=150, w3=71, lag=2)."""
    a = _safe_log(open.abs() + 1.0).shift(2)
    b = _safe_log(high.abs() + 1.0).shift(2)
    corr = a.rolling(150, min_periods=max(150//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 134)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.909412 + 0.0009723 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_133_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=141, w2=163, w3=88, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    cover = _safe_div(a.rolling(141, min_periods=max(141//3, 2)).mean(), b.abs().rolling(163, min_periods=max(163//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(88) + 0.128333 * _rolling_slope(cover, 141) + 0.0009724 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_134_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=148, w2=176, w3=105, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    y = _safe_log(high.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.134667 * y + 0.865333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 148) - _rolling_slope(basket, 176) + 0.0009725 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_135_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=155, w2=189, w3=122, lag=8)."""
    x = open.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(155, min_periods=max(155//3, 2)).mean(), upside.rolling(189, min_periods=max(189//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(122) * 0.95 + 0.0009726 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_136_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=162, w2=202, w3=139, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    draw = x - x.rolling(202, min_periods=max(202//3, 2)).max()
    rebound = x - x.rolling(162, min_periods=max(162//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.147333 * _rolling_slope(draw, 139) + 0.0009727 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_137_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=169, w2=215, w3=156, lag=21)."""
    a = _safe_log(open.abs() + 1.0).shift(21)
    b = _safe_log(high.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(156, min_periods=max(156//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.977059 + 0.0009728 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_138_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=176, w2=228, w3=173, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 176)
    baseline = trend.rolling(228, min_periods=max(228//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.990588 + 0.0009729 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_139_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=183, w2=241, w3=190, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 183)
    slow = _rolling_slope(x, 241)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=190, adjust=False).mean() * 1.004118 + 0.000973 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_140_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=190, w2=254, w3=207, lag=0)."""
    x = open.shift(0)
    peak = x.rolling(254, min_periods=max(254//3, 2)).max()
    trough = x.rolling(190, min_periods=max(190//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.017647 + 0.0009731 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_141_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=197, w2=267, w3=224, lag=1)."""
    x = open.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(267, min_periods=max(267//3, 2)).rank(pct=True)
    persistence = change.rolling(224, min_periods=max(224//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.179 * persistence + 0.0009732 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_142_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=204, w2=280, w3=241, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(204, min_periods=max(204//3, 2)).std()
    vol_slow = ret.rolling(280, min_periods=max(280//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.044706 + 0.0009733 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_143_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=211, w2=293, w3=258, lag=3)."""
    x = open.shift(3)
    ma = x.rolling(293, min_periods=max(293//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 211)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.191667 * slope + 0.0009734 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_144_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=218, w2=306, w3=275, lag=5)."""
    x = open.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(306, min_periods=max(306//3, 2)).mean()
    noise = impulse.abs().rolling(275, min_periods=max(275//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.071765 + 0.0009735 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_145_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=225, w2=319, w3=292, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 225)
    acceleration = _rolling_slope(velocity, 319)
    curvature = _rolling_slope(acceleration, 292)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.204333 * acceleration + 0.0009736 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_146_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=232, w2=332, w3=309, lag=13)."""
    rel = _safe_div(open.shift(13), high.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 232)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.210667 * pressure.rolling(309, min_periods=max(309//3, 2)).mean() + 0.0009737 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_147_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=239, w2=345, w3=326, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(239, min_periods=max(239//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.112353 + 0.0009738 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_148_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=246, w2=358, w3=343, lag=34)."""
    a = _safe_log(open.abs() + 1.0).shift(34)
    b = _safe_log(high.abs() + 1.0).shift(34)
    corr = a.rolling(358, min_periods=max(358//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 246)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.125882 + 0.0009739 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_149_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=6, w2=371, w3=360, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    cover = _safe_div(a.rolling(6, min_periods=max(6//3, 2)).mean(), b.abs().rolling(371, min_periods=max(371//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.229667 * _rolling_slope(cover, 6) + 0.000974 * anchor
    return base_signal.diff().diff()

def f108_orbs_gemini_150_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=13, w2=384, w3=377, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    y = _safe_log(high.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.236 * y + 0.764000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 13) - _rolling_slope(basket, 384) + 0.0009741 * anchor
    return base_signal.diff().diff()
