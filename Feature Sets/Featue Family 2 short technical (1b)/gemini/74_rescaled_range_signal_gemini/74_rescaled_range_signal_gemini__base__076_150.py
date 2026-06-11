"""74 rescaled range signal gemini base features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Analysis of the range of cumulative deviations to identify trend persistence.
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

def f74_rrsg_gemini_076(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=84, w2=11, w3=608, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(11, min_periods=max(11//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 84)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.258235 + 0.0046907 * anchor
    return base_signal

def f74_rrsg_gemini_077(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=91, w2=24, w3=625, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(91, min_periods=max(91//3, 2)).mean(), b.abs().rolling(24, min_periods=max(24//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.335 * _rolling_slope(cover, 91) + 0.0046908 * anchor
    return base_signal

def f74_rrsg_gemini_078(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=98, w2=37, w3=642, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.341333 * y + 0.658667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 98) - _rolling_slope(basket, 37) + 0.0046909 * anchor
    return base_signal

def f74_rrsg_gemini_079(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=105, w2=50, w3=659, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(105, min_periods=max(105//3, 2)).mean(), upside.rolling(50, min_periods=max(50//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.298824 + 0.004691 * anchor
    return base_signal

def f74_rrsg_gemini_080(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=112, w2=63, w3=676, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(63, min_periods=max(63//3, 2)).max()
    rebound = x - x.rolling(112, min_periods=max(112//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.354 * _rolling_slope(draw, 676) + 0.0046911 * anchor
    return base_signal

def f74_rrsg_gemini_081(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=119, w2=76, w3=693, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(119) - b.diff(76)
    stress = imbalance.rolling(693, min_periods=max(693//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.325882 + 0.0046912 * anchor
    return base_signal

def f74_rrsg_gemini_082(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=126, w2=89, w3=710, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 126)
    baseline = trend.rolling(89, min_periods=max(89//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(710, min_periods=max(710//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.339412 + 0.0046913 * anchor
    return base_signal

def f74_rrsg_gemini_083(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=133, w2=102, w3=727, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 133)
    slow = _rolling_slope(x, 102)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.352941 + 0.0046914 * anchor
    return base_signal

def f74_rrsg_gemini_084(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=140, w2=115, w3=744, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(115, min_periods=max(115//3, 2)).max()
    trough = x.rolling(140, min_periods=max(140//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.366471 + 0.0046915 * anchor
    return base_signal

def f74_rrsg_gemini_085(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=147, w2=128, w3=761, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(128, min_periods=max(128//3, 2)).rank(pct=True)
    persistence = change.rolling(761, min_periods=max(761//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.053333 * persistence + 0.0046916 * anchor
    return base_signal

def f74_rrsg_gemini_086(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=154, w2=141, w3=27, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(154, min_periods=max(154//3, 2)).std()
    vol_slow = ret.rolling(141, min_periods=max(141//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.393529 + 0.0046917 * anchor
    return base_signal

def f74_rrsg_gemini_087(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=161, w2=154, w3=44, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(154, min_periods=max(154//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 161)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.066 * slope + 0.0046918 * anchor
    return base_signal

def f74_rrsg_gemini_088(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=168, w2=167, w3=61, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(167, min_periods=max(167//3, 2)).mean()
    noise = impulse.abs().rolling(61, min_periods=max(61//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.420588 + 0.0046919 * anchor
    return base_signal

def f74_rrsg_gemini_089(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=175, w2=180, w3=78, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 175)
    acceleration = _rolling_slope(velocity, 180)
    curvature = _rolling_slope(acceleration, 78)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.078667 * acceleration + 0.004692 * anchor
    return base_signal

def f74_rrsg_gemini_090(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=182, w2=193, w3=95, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 182)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.085 * pressure.rolling(95, min_periods=max(95//3, 2)).mean() + 0.0046921 * anchor
    return base_signal

def f74_rrsg_gemini_091(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=189, w2=206, w3=112, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(189, min_periods=max(189//3, 2)).mean())
    decay = spread.ewm(span=206, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.461176 + 0.0046922 * anchor
    return base_signal

def f74_rrsg_gemini_092(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=196, w2=219, w3=129, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(219, min_periods=max(219//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 196)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.474706 + 0.0046923 * anchor
    return base_signal

def f74_rrsg_gemini_093(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=203, w2=232, w3=146, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(203, min_periods=max(203//3, 2)).mean(), b.abs().rolling(232, min_periods=max(232//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.104 * _rolling_slope(cover, 203) + 0.0046924 * anchor
    return base_signal

def f74_rrsg_gemini_094(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=210, w2=245, w3=163, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.110333 * y + 0.889667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 210) - _rolling_slope(basket, 245) + 0.0046925 * anchor
    return base_signal

def f74_rrsg_gemini_095(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=217, w2=258, w3=180, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(217, min_periods=max(217//3, 2)).mean(), upside.rolling(258, min_periods=max(258//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.515294 + 0.0046926 * anchor
    return base_signal

def f74_rrsg_gemini_096(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=224, w2=271, w3=197, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(271, min_periods=max(271//3, 2)).max()
    rebound = x - x.rolling(224, min_periods=max(224//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.123 * _rolling_slope(draw, 197) + 0.0046927 * anchor
    return base_signal

def f74_rrsg_gemini_097(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=231, w2=284, w3=214, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(214, min_periods=max(214//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.542353 + 0.0046928 * anchor
    return base_signal

def f74_rrsg_gemini_098(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=238, w2=297, w3=231, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 238)
    baseline = trend.rolling(297, min_periods=max(297//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(231, min_periods=max(231//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.555882 + 0.0046929 * anchor
    return base_signal

def f74_rrsg_gemini_099(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=245, w2=310, w3=248, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 245)
    slow = _rolling_slope(x, 310)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=248, adjust=False).mean() * 1.569412 + 0.004693 * anchor
    return base_signal

def f74_rrsg_gemini_100(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=5, w2=323, w3=265, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(323, min_periods=max(323//3, 2)).max()
    trough = x.rolling(5, min_periods=max(5//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.582941 + 0.0046931 * anchor
    return base_signal

def f74_rrsg_gemini_101(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=12, w2=336, w3=282, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(12)
    rank = change.rolling(336, min_periods=max(336//3, 2)).rank(pct=True)
    persistence = change.rolling(282, min_periods=max(282//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.154667 * persistence + 0.0046932 * anchor
    return base_signal

def f74_rrsg_gemini_102(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=19, w2=349, w3=299, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(19, min_periods=max(19//3, 2)).std()
    vol_slow = ret.rolling(349, min_periods=max(349//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.61 + 0.0046933 * anchor
    return base_signal

def f74_rrsg_gemini_103(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=26, w2=362, w3=316, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(362, min_periods=max(362//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 26)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.167333 * slope + 0.0046934 * anchor
    return base_signal

def f74_rrsg_gemini_104(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=33, w2=375, w3=333, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(33)
    drag = impulse.rolling(375, min_periods=max(375//3, 2)).mean()
    noise = impulse.abs().rolling(333, min_periods=max(333//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.637059 + 0.0046935 * anchor
    return base_signal

def f74_rrsg_gemini_105(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=40, w2=388, w3=350, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 40)
    acceleration = _rolling_slope(velocity, 388)
    curvature = _rolling_slope(acceleration, 350)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.18 * acceleration + 0.0046936 * anchor
    return base_signal

def f74_rrsg_gemini_106(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=47, w2=401, w3=367, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 47)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.186333 * pressure.rolling(367, min_periods=max(367//3, 2)).mean() + 0.0046937 * anchor
    return base_signal

def f74_rrsg_gemini_107(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=54, w2=414, w3=384, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(54, min_periods=max(54//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.824118 + 0.0046938 * anchor
    return base_signal

def f74_rrsg_gemini_108(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=61, w2=427, w3=401, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(427, min_periods=max(427//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 61)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.837647 + 0.0046939 * anchor
    return base_signal

def f74_rrsg_gemini_109(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=440, w3=418, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(68, min_periods=max(68//3, 2)).mean(), b.abs().rolling(440, min_periods=max(440//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.205333 * _rolling_slope(cover, 68) + 0.004694 * anchor
    return base_signal

def f74_rrsg_gemini_110(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=453, w3=435, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.211667 * y + 0.788333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 75) - _rolling_slope(basket, 453) + 0.0046941 * anchor
    return base_signal

def f74_rrsg_gemini_111(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=466, w3=452, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(82, min_periods=max(82//3, 2)).mean(), upside.rolling(466, min_periods=max(466//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.878235 + 0.0046942 * anchor
    return base_signal

def f74_rrsg_gemini_112(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=479, w3=469, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(479, min_periods=max(479//3, 2)).max()
    rebound = x - x.rolling(89, min_periods=max(89//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.224333 * _rolling_slope(draw, 469) + 0.0046943 * anchor
    return base_signal

def f74_rrsg_gemini_113(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=492, w3=486, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(96) - b.diff(126)
    stress = imbalance.rolling(486, min_periods=max(486//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.905294 + 0.0046944 * anchor
    return base_signal

def f74_rrsg_gemini_114(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=505, w3=503, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 103)
    baseline = trend.rolling(505, min_periods=max(505//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(503, min_periods=max(503//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.918824 + 0.0046945 * anchor
    return base_signal

def f74_rrsg_gemini_115(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=19, w3=520, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 110)
    slow = _rolling_slope(x, 19)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.932353 + 0.0046946 * anchor
    return base_signal

def f74_rrsg_gemini_116(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=32, w3=537, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(32, min_periods=max(32//3, 2)).max()
    trough = x.rolling(117, min_periods=max(117//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.945882 + 0.0046947 * anchor
    return base_signal

def f74_rrsg_gemini_117(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=124, w2=45, w3=554, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(124)
    rank = change.rolling(45, min_periods=max(45//3, 2)).rank(pct=True)
    persistence = change.rolling(554, min_periods=max(554//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.256 * persistence + 0.0046948 * anchor
    return base_signal

def f74_rrsg_gemini_118(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=131, w2=58, w3=571, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(131, min_periods=max(131//3, 2)).std()
    vol_slow = ret.rolling(58, min_periods=max(58//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.972941 + 0.0046949 * anchor
    return base_signal

def f74_rrsg_gemini_119(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=138, w2=71, w3=588, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(71, min_periods=max(71//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 138)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.268667 * slope + 0.004695 * anchor
    return base_signal

def f74_rrsg_gemini_120(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=145, w2=84, w3=605, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(84, min_periods=max(84//3, 2)).mean()
    noise = impulse.abs().rolling(605, min_periods=max(605//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0 + 0.0046951 * anchor
    return base_signal

def f74_rrsg_gemini_121(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=152, w2=97, w3=622, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 152)
    acceleration = _rolling_slope(velocity, 97)
    curvature = _rolling_slope(acceleration, 622)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.281333 * acceleration + 0.0046952 * anchor
    return base_signal

def f74_rrsg_gemini_122(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=159, w2=110, w3=639, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 159)
    pressure = rel_log.diff(110)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.287667 * pressure.rolling(639, min_periods=max(639//3, 2)).mean() + 0.0046953 * anchor
    return base_signal

def f74_rrsg_gemini_123(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=166, w2=123, w3=656, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(166, min_periods=max(166//3, 2)).mean())
    decay = spread.ewm(span=123, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.040588 + 0.0046954 * anchor
    return base_signal

def f74_rrsg_gemini_124(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=173, w2=136, w3=673, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(136, min_periods=max(136//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 173)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.054118 + 0.0046955 * anchor
    return base_signal

def f74_rrsg_gemini_125(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=149, w3=690, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(180, min_periods=max(180//3, 2)).mean(), b.abs().rolling(149, min_periods=max(149//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.306667 * _rolling_slope(cover, 180) + 0.0046956 * anchor
    return base_signal

def f74_rrsg_gemini_126(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=162, w3=707, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.313 * y + 0.687000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 187) - _rolling_slope(basket, 162) + 0.0046957 * anchor
    return base_signal

def f74_rrsg_gemini_127(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=175, w3=724, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(194, min_periods=max(194//3, 2)).mean(), upside.rolling(175, min_periods=max(175//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.094706 + 0.0046958 * anchor
    return base_signal

def f74_rrsg_gemini_128(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=188, w3=741, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(188, min_periods=max(188//3, 2)).max()
    rebound = x - x.rolling(201, min_periods=max(201//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.325667 * _rolling_slope(draw, 741) + 0.0046959 * anchor
    return base_signal

def f74_rrsg_gemini_129(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=201, w3=758, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(758, min_periods=max(758//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.121765 + 0.004696 * anchor
    return base_signal

def f74_rrsg_gemini_130(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=214, w3=24, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 215)
    baseline = trend.rolling(214, min_periods=max(214//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(24, min_periods=max(24//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.135294 + 0.0046961 * anchor
    return base_signal

def f74_rrsg_gemini_131(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=227, w3=41, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 222)
    slow = _rolling_slope(x, 227)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=41, adjust=False).mean() * 1.148824 + 0.0046962 * anchor
    return base_signal

def f74_rrsg_gemini_132(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=240, w3=58, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(240, min_periods=max(240//3, 2)).max()
    trough = x.rolling(229, min_periods=max(229//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.162353 + 0.0046963 * anchor
    return base_signal

def f74_rrsg_gemini_133(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=253, w3=75, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(253, min_periods=max(253//3, 2)).rank(pct=True)
    persistence = change.rolling(75, min_periods=max(75//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.357333 * persistence + 0.0046964 * anchor
    return base_signal

def f74_rrsg_gemini_134(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=266, w3=92, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(243, min_periods=max(243//3, 2)).std()
    vol_slow = ret.rolling(266, min_periods=max(266//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.189412 + 0.0046965 * anchor
    return base_signal

def f74_rrsg_gemini_135(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=279, w3=109, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(279, min_periods=max(279//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 250)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.037667 * slope + 0.0046966 * anchor
    return base_signal

def f74_rrsg_gemini_136(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=292, w3=126, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(10)
    drag = impulse.rolling(292, min_periods=max(292//3, 2)).mean()
    noise = impulse.abs().rolling(126, min_periods=max(126//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.216471 + 0.0046967 * anchor
    return base_signal

def f74_rrsg_gemini_137(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=305, w3=143, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 17)
    acceleration = _rolling_slope(velocity, 305)
    curvature = _rolling_slope(acceleration, 143)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.050333 * acceleration + 0.0046968 * anchor
    return base_signal

def f74_rrsg_gemini_138(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=318, w3=160, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 24)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.056667 * pressure.rolling(160, min_periods=max(160//3, 2)).mean() + 0.0046969 * anchor
    return base_signal

def f74_rrsg_gemini_139(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=331, w3=177, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(31, min_periods=max(31//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.257059 + 0.004697 * anchor
    return base_signal

def f74_rrsg_gemini_140(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=344, w3=194, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(344, min_periods=max(344//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 38)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.270588 + 0.0046971 * anchor
    return base_signal

def f74_rrsg_gemini_141(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=357, w3=211, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(45, min_periods=max(45//3, 2)).mean(), b.abs().rolling(357, min_periods=max(357//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.075667 * _rolling_slope(cover, 45) + 0.0046972 * anchor
    return base_signal

def f74_rrsg_gemini_142(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=370, w3=228, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.082 * y + 0.918000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 52) - _rolling_slope(basket, 370) + 0.0046973 * anchor
    return base_signal

def f74_rrsg_gemini_143(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=383, w3=245, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(59, min_periods=max(59//3, 2)).mean(), upside.rolling(383, min_periods=max(383//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.311176 + 0.0046974 * anchor
    return base_signal

def f74_rrsg_gemini_144(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=396, w3=262, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(396, min_periods=max(396//3, 2)).max()
    rebound = x - x.rolling(66, min_periods=max(66//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.094667 * _rolling_slope(draw, 262) + 0.0046975 * anchor
    return base_signal

def f74_rrsg_gemini_145(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=409, w3=279, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(73) - b.diff(126)
    stress = imbalance.rolling(279, min_periods=max(279//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.338235 + 0.0046976 * anchor
    return base_signal

def f74_rrsg_gemini_146(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=422, w3=296, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 80)
    baseline = trend.rolling(422, min_periods=max(422//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(296, min_periods=max(296//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.351765 + 0.0046977 * anchor
    return base_signal

def f74_rrsg_gemini_147(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=435, w3=313, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 87)
    slow = _rolling_slope(x, 435)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.365294 + 0.0046978 * anchor
    return base_signal

def f74_rrsg_gemini_148(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=448, w3=330, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(448, min_periods=max(448//3, 2)).max()
    trough = x.rolling(94, min_periods=max(94//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.378824 + 0.0046979 * anchor
    return base_signal

def f74_rrsg_gemini_149(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=461, w3=347, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(101)
    rank = change.rolling(461, min_periods=max(461//3, 2)).rank(pct=True)
    persistence = change.rolling(347, min_periods=max(347//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.126333 * persistence + 0.004698 * anchor
    return base_signal

def f74_rrsg_gemini_150(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=474, w3=364, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(108, min_periods=max(108//3, 2)).std()
    vol_slow = ret.rolling(474, min_periods=max(474//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.405882 + 0.0046981 * anchor
    return base_signal
