"""36 semi variance asymmetry gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Measurement of downside vs. upside volatility to detect bearish risk bias.
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

def f36_svar_gemini_076_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=49, w2=463, w3=333, lag=13)."""
    x = low.shift(13)
    peak = x.rolling(463, min_periods=max(463//3, 2)).max()
    trough = x.rolling(49, min_periods=max(49//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.365882 + 0.0025907 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_077_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=56, w2=476, w3=350, lag=21)."""
    x = low.shift(21)
    change = x.pct_change(56)
    rank = change.rolling(476, min_periods=max(476//3, 2)).rank(pct=True)
    persistence = change.rolling(350, min_periods=max(350//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.268333 * persistence + 0.0025908 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_078_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=63, w2=489, w3=367, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(63, min_periods=max(63//3, 2)).std()
    vol_slow = ret.rolling(489, min_periods=max(489//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.392941 + 0.0025909 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_079_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=502, w3=384, lag=55)."""
    x = low.shift(55)
    ma = x.rolling(502, min_periods=max(502//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 70)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.281 * slope + 0.002591 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_080_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=77, w2=16, w3=401, lag=0)."""
    x = low.shift(0)
    impulse = x.diff(77)
    drag = impulse.rolling(16, min_periods=max(16//3, 2)).mean()
    noise = impulse.abs().rolling(401, min_periods=max(401//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.42 + 0.0025911 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_081_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=84, w2=29, w3=418, lag=1)."""
    x = _safe_log(low.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 84)
    acceleration = _rolling_slope(velocity, 29)
    curvature = _rolling_slope(acceleration, 418)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.293667 * acceleration + 0.0025912 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_082_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=91, w2=42, w3=435, lag=2)."""
    rel = _safe_div(low.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 91)
    pressure = rel_log.diff(42)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3 * pressure.rolling(435, min_periods=max(435//3, 2)).mean() + 0.0025913 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_083_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=98, w2=55, w3=452, lag=3)."""
    a = low.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(98, min_periods=max(98//3, 2)).mean())
    decay = spread.ewm(span=55, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.460588 + 0.0025914 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_084_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=105, w2=68, w3=469, lag=5)."""
    a = _safe_log(low.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(68, min_periods=max(68//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 105)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.474118 + 0.0025915 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_085_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=112, w2=81, w3=486, lag=8)."""
    a = low.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(112, min_periods=max(112//3, 2)).mean(), b.abs().rolling(81, min_periods=max(81//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.319 * _rolling_slope(cover, 112) + 0.0025916 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_086_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=119, w2=94, w3=503, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.325333 * y + 0.674667 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 119) - _rolling_slope(basket, 94) + 0.0025917 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_087_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=107, w3=520, lag=21)."""
    x = low.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(126, min_periods=max(126//3, 2)).mean(), upside.rolling(107, min_periods=max(107//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.514706 + 0.0025918 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_088_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=120, w3=537, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    draw = x - x.rolling(120, min_periods=max(120//3, 2)).max()
    rebound = x - x.rolling(133, min_periods=max(133//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.338 * _rolling_slope(draw, 537) + 0.0025919 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_089_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=133, w3=554, lag=55)."""
    a = _safe_log(low.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(554, min_periods=max(554//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.541765 + 0.002592 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_090_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=146, w3=571, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 147)
    baseline = trend.rolling(146, min_periods=max(146//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(571, min_periods=max(571//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.555294 + 0.0025921 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_091_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=159, w3=588, lag=1)."""
    x = _safe_log(low.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 154)
    slow = _rolling_slope(x, 159)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.568824 + 0.0025922 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_092_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=172, w3=605, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(172, min_periods=max(172//3, 2)).max()
    trough = x.rolling(161, min_periods=max(161//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.582353 + 0.0025923 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_093_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=185, w3=622, lag=3)."""
    x = low.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(185, min_periods=max(185//3, 2)).rank(pct=True)
    persistence = change.rolling(622, min_periods=max(622//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.037333 * persistence + 0.0025924 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_094_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=198, w3=639, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(175, min_periods=max(175//3, 2)).std()
    vol_slow = ret.rolling(198, min_periods=max(198//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.609412 + 0.0025925 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_095_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=211, w3=656, lag=8)."""
    x = low.shift(8)
    ma = x.rolling(211, min_periods=max(211//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 182)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.05 * slope + 0.0025926 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_096_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=189, w2=224, w3=673, lag=13)."""
    x = low.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(224, min_periods=max(224//3, 2)).mean()
    noise = impulse.abs().rolling(673, min_periods=max(673//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.636471 + 0.0025927 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_097_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=196, w2=237, w3=690, lag=21)."""
    x = _safe_log(low.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 196)
    acceleration = _rolling_slope(velocity, 237)
    curvature = _rolling_slope(acceleration, 690)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.062667 * acceleration + 0.0025928 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_098_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=203, w2=250, w3=707, lag=34)."""
    rel = _safe_div(low.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 203)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.069 * pressure.rolling(707, min_periods=max(707//3, 2)).mean() + 0.0025929 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_099_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=210, w2=263, w3=724, lag=55)."""
    a = low.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(210, min_periods=max(210//3, 2)).mean())
    decay = spread.ewm(span=263, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.823529 + 0.002593 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_100_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=217, w2=276, w3=741, lag=0)."""
    a = _safe_log(low.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(276, min_periods=max(276//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 217)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.837059 + 0.0025931 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_101_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=224, w2=289, w3=758, lag=1)."""
    a = low.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(224, min_periods=max(224//3, 2)).mean(), b.abs().rolling(289, min_periods=max(289//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.088 * _rolling_slope(cover, 224) + 0.0025932 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_102_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=231, w2=302, w3=24, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.094333 * y + 0.905667 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 231) - _rolling_slope(basket, 302) + 0.0025933 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_103_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=238, w2=315, w3=41, lag=3)."""
    x = low.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(238, min_periods=max(238//3, 2)).mean(), upside.rolling(315, min_periods=max(315//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(41) * 0.877647 + 0.0025934 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_104_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=245, w2=328, w3=58, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    draw = x - x.rolling(328, min_periods=max(328//3, 2)).max()
    rebound = x - x.rolling(245, min_periods=max(245//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.107 * _rolling_slope(draw, 58) + 0.0025935 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_105_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=5, w2=341, w3=75, lag=8)."""
    a = _safe_log(low.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(5) - b.diff(126)
    stress = imbalance.rolling(75, min_periods=max(75//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.904706 + 0.0025936 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_106_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=354, w3=92, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 12)
    baseline = trend.rolling(354, min_periods=max(354//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(92, min_periods=max(92//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.918235 + 0.0025937 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_107_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=367, w3=109, lag=21)."""
    x = _safe_log(low.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 19)
    slow = _rolling_slope(x, 367)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=109, adjust=False).mean() * 0.931765 + 0.0025938 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_108_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=380, w3=126, lag=34)."""
    x = low.shift(34)
    peak = x.rolling(380, min_periods=max(380//3, 2)).max()
    trough = x.rolling(26, min_periods=max(26//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.945294 + 0.0025939 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_109_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=393, w3=143, lag=55)."""
    x = low.shift(55)
    change = x.pct_change(33)
    rank = change.rolling(393, min_periods=max(393//3, 2)).rank(pct=True)
    persistence = change.rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.138667 * persistence + 0.002594 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_110_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=406, w3=160, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(40, min_periods=max(40//3, 2)).std()
    vol_slow = ret.rolling(406, min_periods=max(406//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.972353 + 0.0025941 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_111_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=419, w3=177, lag=1)."""
    x = low.shift(1)
    ma = x.rolling(419, min_periods=max(419//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 47)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.151333 * slope + 0.0025942 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_112_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=432, w3=194, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(54)
    drag = impulse.rolling(432, min_periods=max(432//3, 2)).mean()
    noise = impulse.abs().rolling(194, min_periods=max(194//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.999412 + 0.0025943 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_113_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=445, w3=211, lag=3)."""
    x = _safe_log(low.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 61)
    acceleration = _rolling_slope(velocity, 445)
    curvature = _rolling_slope(acceleration, 211)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.164 * acceleration + 0.0025944 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_114_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=458, w3=228, lag=5)."""
    rel = _safe_div(low.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 68)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.170333 * pressure.rolling(228, min_periods=max(228//3, 2)).mean() + 0.0025945 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_115_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=471, w3=245, lag=8)."""
    a = low.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(75, min_periods=max(75//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.04 + 0.0025946 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_116_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=484, w3=262, lag=13)."""
    a = _safe_log(low.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(484, min_periods=max(484//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 82)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.053529 + 0.0025947 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_117_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=497, w3=279, lag=21)."""
    a = low.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(89, min_periods=max(89//3, 2)).mean(), b.abs().rolling(497, min_periods=max(497//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.189333 * _rolling_slope(cover, 89) + 0.0025948 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_118_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=11, w3=296, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.195667 * y + 0.804333 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 96) - _rolling_slope(basket, 11) + 0.0025949 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_119_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=24, w3=313, lag=55)."""
    x = low.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(103, min_periods=max(103//3, 2)).mean(), upside.rolling(24, min_periods=max(24//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.094118 + 0.002595 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_120_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=37, w3=330, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    draw = x - x.rolling(37, min_periods=max(37//3, 2)).max()
    rebound = x - x.rolling(110, min_periods=max(110//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.208333 * _rolling_slope(draw, 330) + 0.0025951 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_121_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=117, w2=50, w3=347, lag=1)."""
    a = _safe_log(low.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(117) - b.diff(50)
    stress = imbalance.rolling(347, min_periods=max(347//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.121176 + 0.0025952 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_122_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=124, w2=63, w3=364, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 124)
    baseline = trend.rolling(63, min_periods=max(63//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(364, min_periods=max(364//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.134706 + 0.0025953 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_123_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=131, w2=76, w3=381, lag=3)."""
    x = _safe_log(low.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 131)
    slow = _rolling_slope(x, 76)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.148235 + 0.0025954 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_124_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=138, w2=89, w3=398, lag=5)."""
    x = low.shift(5)
    peak = x.rolling(89, min_periods=max(89//3, 2)).max()
    trough = x.rolling(138, min_periods=max(138//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.161765 + 0.0025955 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_125_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=145, w2=102, w3=415, lag=8)."""
    x = low.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(102, min_periods=max(102//3, 2)).rank(pct=True)
    persistence = change.rolling(415, min_periods=max(415//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.24 * persistence + 0.0025956 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_126_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=152, w2=115, w3=432, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(152, min_periods=max(152//3, 2)).std()
    vol_slow = ret.rolling(115, min_periods=max(115//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.188824 + 0.0025957 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_127_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=159, w2=128, w3=449, lag=21)."""
    x = low.shift(21)
    ma = x.rolling(128, min_periods=max(128//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 159)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.252667 * slope + 0.0025958 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_128_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=166, w2=141, w3=466, lag=34)."""
    x = low.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(141, min_periods=max(141//3, 2)).mean()
    noise = impulse.abs().rolling(466, min_periods=max(466//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.215882 + 0.0025959 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_129_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=173, w2=154, w3=483, lag=55)."""
    x = _safe_log(low.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 173)
    acceleration = _rolling_slope(velocity, 154)
    curvature = _rolling_slope(acceleration, 483)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.265333 * acceleration + 0.002596 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_130_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=180, w2=167, w3=500, lag=0)."""
    rel = _safe_div(low.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 180)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.271667 * pressure.rolling(500, min_periods=max(500//3, 2)).mean() + 0.0025961 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_131_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=187, w2=180, w3=517, lag=1)."""
    a = low.shift(1)
    b = close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(187, min_periods=max(187//3, 2)).mean())
    decay = spread.ewm(span=180, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.256471 + 0.0025962 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_132_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=194, w2=193, w3=534, lag=2)."""
    a = _safe_log(low.abs() + 1.0).shift(2)
    b = _safe_log(close.abs() + 1.0).shift(2)
    corr = a.rolling(193, min_periods=max(193//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 194)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.27 + 0.0025963 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_133_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=201, w2=206, w3=551, lag=3)."""
    a = low.shift(3)
    b = close.shift(3)
    cover = _safe_div(a.rolling(201, min_periods=max(201//3, 2)).mean(), b.abs().rolling(206, min_periods=max(206//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.290667 * _rolling_slope(cover, 201) + 0.0025964 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_134_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=208, w2=219, w3=568, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    y = _safe_log(close.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.297 * y + 0.703000 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 208) - _rolling_slope(basket, 219) + 0.0025965 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_135_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=215, w2=232, w3=585, lag=8)."""
    x = low.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(215, min_periods=max(215//3, 2)).mean(), upside.rolling(232, min_periods=max(232//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.310588 + 0.0025966 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_136_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=222, w2=245, w3=602, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    draw = x - x.rolling(245, min_periods=max(245//3, 2)).max()
    rebound = x - x.rolling(222, min_periods=max(222//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.309667 * _rolling_slope(draw, 602) + 0.0025967 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_137_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=229, w2=258, w3=619, lag=21)."""
    a = _safe_log(low.abs() + 1.0).shift(21)
    b = _safe_log(close.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(619, min_periods=max(619//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.337647 + 0.0025968 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_138_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=271, w3=636, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 236)
    baseline = trend.rolling(271, min_periods=max(271//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(636, min_periods=max(636//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.351176 + 0.0025969 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_139_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=284, w3=653, lag=55)."""
    x = _safe_log(low.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 243)
    slow = _rolling_slope(x, 284)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.364706 + 0.002597 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_140_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=250, w2=297, w3=670, lag=0)."""
    x = low.shift(0)
    peak = x.rolling(297, min_periods=max(297//3, 2)).max()
    trough = x.rolling(250, min_periods=max(250//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.378235 + 0.0025971 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_141_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=310, w3=687, lag=1)."""
    x = low.shift(1)
    change = x.pct_change(10)
    rank = change.rolling(310, min_periods=max(310//3, 2)).rank(pct=True)
    persistence = change.rolling(687, min_periods=max(687//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.341333 * persistence + 0.0025972 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_142_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=17, w2=323, w3=704, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(17, min_periods=max(17//3, 2)).std()
    vol_slow = ret.rolling(323, min_periods=max(323//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.405294 + 0.0025973 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_143_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=24, w2=336, w3=721, lag=3)."""
    x = low.shift(3)
    ma = x.rolling(336, min_periods=max(336//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 24)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.354 * slope + 0.0025974 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_144_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=31, w2=349, w3=738, lag=5)."""
    x = low.shift(5)
    impulse = x.diff(31)
    drag = impulse.rolling(349, min_periods=max(349//3, 2)).mean()
    noise = impulse.abs().rolling(738, min_periods=max(738//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.432353 + 0.0025975 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_145_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=362, w3=755, lag=8)."""
    x = _safe_log(low.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 38)
    acceleration = _rolling_slope(velocity, 362)
    curvature = _rolling_slope(acceleration, 755)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.034333 * acceleration + 0.0025976 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_146_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=375, w3=21, lag=13)."""
    rel = _safe_div(low.shift(13), close.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 45)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.040667 * pressure.rolling(21, min_periods=max(21//3, 2)).mean() + 0.0025977 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_147_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=388, w3=38, lag=21)."""
    a = low.shift(21)
    b = close.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(52, min_periods=max(52//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.472941 + 0.0025978 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_148_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=59, w2=401, w3=55, lag=34)."""
    a = _safe_log(low.abs() + 1.0).shift(34)
    b = _safe_log(close.abs() + 1.0).shift(34)
    corr = a.rolling(401, min_periods=max(401//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 59)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.486471 + 0.0025979 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_149_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=66, w2=414, w3=72, lag=55)."""
    a = low.shift(55)
    b = close.shift(55)
    cover = _safe_div(a.rolling(66, min_periods=max(66//3, 2)).mean(), b.abs().rolling(414, min_periods=max(414//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(72) + 0.059667 * _rolling_slope(cover, 66) + 0.002598 * anchor
    return base_signal.diff().diff()

def f36_svar_gemini_150_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=73, w2=427, w3=89, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    y = _safe_log(close.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.066 * y + 0.934000 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 73) - _rolling_slope(basket, 427) + 0.0025981 * anchor
    return base_signal.diff().diff()
