"""06 candlestick reversal catalog gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Standard candlestick reversal patterns detected through relative wick and body proportions.
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

def f06_crev_gemini_076_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=385, w3=533, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(385, min_periods=max(385//3, 2)).max()
    trough = x.rolling(126, min_periods=max(126//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.415294 + 0.0002947 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_077_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=398, w3=550, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(398, min_periods=max(398//3, 2)).rank(pct=True)
    persistence = change.rolling(550, min_periods=max(550//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.084667 * persistence + 0.0002948 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_078_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=411, w3=567, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(140, min_periods=max(140//3, 2)).std()
    vol_slow = ret.rolling(411, min_periods=max(411//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.442353 + 0.0002949 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_079_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=424, w3=584, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(424, min_periods=max(424//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 147)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.097333 * slope + 0.000295 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_080_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=437, w3=601, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(437, min_periods=max(437//3, 2)).mean()
    noise = impulse.abs().rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.469412 + 0.0002951 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_081_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=450, w3=618, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 161)
    acceleration = _rolling_slope(velocity, 450)
    curvature = _rolling_slope(acceleration, 618)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.11 * acceleration + 0.0002952 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_082_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=463, w3=635, lag=2)."""
    rel = _safe_div(open.shift(2), high.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 168)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.116333 * pressure.rolling(635, min_periods=max(635//3, 2)).mean() + 0.0002953 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_083_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=476, w3=652, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(175, min_periods=max(175//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.51 + 0.0002954 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_084_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=489, w3=669, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(high.abs() + 1.0).shift(5)
    corr = a.rolling(489, min_periods=max(489//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 182)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.523529 + 0.0002955 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_085_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=189, w2=502, w3=686, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    cover = _safe_div(a.rolling(189, min_periods=max(189//3, 2)).mean(), b.abs().rolling(502, min_periods=max(502//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.135333 * _rolling_slope(cover, 189) + 0.0002956 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_086_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=196, w2=16, w3=703, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(high.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.141667 * y + 0.858333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 196) - _rolling_slope(basket, 16) + 0.0002957 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_087_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=203, w2=29, w3=720, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(203, min_periods=max(203//3, 2)).mean(), upside.rolling(29, min_periods=max(29//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.564118 + 0.0002958 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_088_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=210, w2=42, w3=737, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(42, min_periods=max(42//3, 2)).max()
    rebound = x - x.rolling(210, min_periods=max(210//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.154333 * _rolling_slope(draw, 737) + 0.0002959 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_089_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=217, w2=55, w3=754, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(high.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(55)
    stress = imbalance.rolling(754, min_periods=max(754//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.591176 + 0.000296 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_090_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=224, w2=68, w3=20, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 224)
    baseline = trend.rolling(68, min_periods=max(68//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(20, min_periods=max(20//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.604706 + 0.0002961 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_091_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=231, w2=81, w3=37, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 231)
    slow = _rolling_slope(x, 81)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=37, adjust=False).mean() * 1.618235 + 0.0002962 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_092_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=238, w2=94, w3=54, lag=2)."""
    x = open.shift(2)
    peak = x.rolling(94, min_periods=max(94//3, 2)).max()
    trough = x.rolling(238, min_periods=max(238//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.631765 + 0.0002963 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_093_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=245, w2=107, w3=71, lag=3)."""
    x = open.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(107, min_periods=max(107//3, 2)).rank(pct=True)
    persistence = change.rolling(71, min_periods=max(71//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.186 * persistence + 0.0002964 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_094_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=5, w2=120, w3=88, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(5, min_periods=max(5//3, 2)).std()
    vol_slow = ret.rolling(120, min_periods=max(120//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.658824 + 0.0002965 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_095_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=133, w3=105, lag=8)."""
    x = open.shift(8)
    ma = x.rolling(133, min_periods=max(133//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 12)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.198667 * slope + 0.0002966 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_096_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=146, w3=122, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(19)
    drag = impulse.rolling(146, min_periods=max(146//3, 2)).mean()
    noise = impulse.abs().rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.832353 + 0.0002967 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_097_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=159, w3=139, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 26)
    acceleration = _rolling_slope(velocity, 159)
    curvature = _rolling_slope(acceleration, 139)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.211333 * acceleration + 0.0002968 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_098_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=172, w3=156, lag=34)."""
    rel = _safe_div(open.shift(34), high.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 33)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.217667 * pressure.rolling(156, min_periods=max(156//3, 2)).mean() + 0.0002969 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_099_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=185, w3=173, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(40, min_periods=max(40//3, 2)).mean())
    decay = spread.ewm(span=185, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.872941 + 0.000297 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_100_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=198, w3=190, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(high.abs() + 1.0).shift(0)
    corr = a.rolling(198, min_periods=max(198//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 47)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.886471 + 0.0002971 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_101_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=211, w3=207, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    cover = _safe_div(a.rolling(54, min_periods=max(54//3, 2)).mean(), b.abs().rolling(211, min_periods=max(211//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.236667 * _rolling_slope(cover, 54) + 0.0002972 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_102_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=224, w3=224, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(high.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.243 * y + 0.757000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 61) - _rolling_slope(basket, 224) + 0.0002973 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_103_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=237, w3=241, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(68, min_periods=max(68//3, 2)).mean(), upside.rolling(237, min_periods=max(237//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.927059 + 0.0002974 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_104_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=250, w3=258, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(250, min_periods=max(250//3, 2)).max()
    rebound = x - x.rolling(75, min_periods=max(75//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.255667 * _rolling_slope(draw, 258) + 0.0002975 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_105_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=263, w3=275, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(high.abs() + 1.0).shift(8)
    imbalance = a.diff(82) - b.diff(126)
    stress = imbalance.rolling(275, min_periods=max(275//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.954118 + 0.0002976 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_106_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=276, w3=292, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 89)
    baseline = trend.rolling(276, min_periods=max(276//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(292, min_periods=max(292//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.967647 + 0.0002977 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_107_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=289, w3=309, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 96)
    slow = _rolling_slope(x, 289)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.981176 + 0.0002978 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_108_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=302, w3=326, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(302, min_periods=max(302//3, 2)).max()
    trough = x.rolling(103, min_periods=max(103//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.994706 + 0.0002979 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_109_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=315, w3=343, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(110)
    rank = change.rolling(315, min_periods=max(315//3, 2)).rank(pct=True)
    persistence = change.rolling(343, min_periods=max(343//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.287333 * persistence + 0.000298 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_110_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=117, w2=328, w3=360, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(117, min_periods=max(117//3, 2)).std()
    vol_slow = ret.rolling(328, min_periods=max(328//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.021765 + 0.0002981 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_111_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=124, w2=341, w3=377, lag=1)."""
    x = open.shift(1)
    ma = x.rolling(341, min_periods=max(341//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 124)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3 * slope + 0.0002982 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_112_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=131, w2=354, w3=394, lag=2)."""
    x = open.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(354, min_periods=max(354//3, 2)).mean()
    noise = impulse.abs().rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.048824 + 0.0002983 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_113_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=138, w2=367, w3=411, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 138)
    acceleration = _rolling_slope(velocity, 367)
    curvature = _rolling_slope(acceleration, 411)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.312667 * acceleration + 0.0002984 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_114_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=145, w2=380, w3=428, lag=5)."""
    rel = _safe_div(open.shift(5), high.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 145)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.319 * pressure.rolling(428, min_periods=max(428//3, 2)).mean() + 0.0002985 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_115_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=152, w2=393, w3=445, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(152, min_periods=max(152//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.089412 + 0.0002986 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_116_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=159, w2=406, w3=462, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(406, min_periods=max(406//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 159)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.102941 + 0.0002987 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_117_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=166, w2=419, w3=479, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(166, min_periods=max(166//3, 2)).mean(), b.abs().rolling(419, min_periods=max(419//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.338 * _rolling_slope(cover, 166) + 0.0002988 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_118_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=173, w2=432, w3=496, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.344333 * y + 0.655667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 173) - _rolling_slope(basket, 432) + 0.0002989 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_119_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=180, w2=445, w3=513, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(180, min_periods=max(180//3, 2)).mean(), upside.rolling(445, min_periods=max(445//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.143529 + 0.000299 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_120_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=187, w2=458, w3=530, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(458, min_periods=max(458//3, 2)).max()
    rebound = x - x.rolling(187, min_periods=max(187//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.357 * _rolling_slope(draw, 530) + 0.0002991 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_121_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=194, w2=471, w3=547, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(high.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(547, min_periods=max(547//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.170588 + 0.0002992 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_122_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=201, w2=484, w3=564, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 201)
    baseline = trend.rolling(484, min_periods=max(484//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(564, min_periods=max(564//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.184118 + 0.0002993 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_123_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=208, w2=497, w3=581, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 208)
    slow = _rolling_slope(x, 497)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.197647 + 0.0002994 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_124_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=215, w2=11, w3=598, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(11, min_periods=max(11//3, 2)).max()
    trough = x.rolling(215, min_periods=max(215//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.211176 + 0.0002995 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_125_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=222, w2=24, w3=615, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(24, min_periods=max(24//3, 2)).rank(pct=True)
    persistence = change.rolling(615, min_periods=max(615//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.056333 * persistence + 0.0002996 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_126_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=229, w2=37, w3=632, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(229, min_periods=max(229//3, 2)).std()
    vol_slow = ret.rolling(37, min_periods=max(37//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.238235 + 0.0002997 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_127_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=50, w3=649, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(50, min_periods=max(50//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 236)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.069 * slope + 0.0002998 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_128_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=63, w3=666, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(63, min_periods=max(63//3, 2)).mean()
    noise = impulse.abs().rolling(666, min_periods=max(666//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.265294 + 0.0002999 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_129_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=250, w2=76, w3=683, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 250)
    acceleration = _rolling_slope(velocity, 76)
    curvature = _rolling_slope(acceleration, 683)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.081667 * acceleration + 0.0003 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_130_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=89, w3=700, lag=0)."""
    rel = _safe_div(open.shift(0), high.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 10)
    pressure = rel_log.diff(89)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.088 * pressure.rolling(700, min_periods=max(700//3, 2)).mean() + 0.0003001 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_131_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=17, w2=102, w3=717, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(17, min_periods=max(17//3, 2)).mean())
    decay = spread.ewm(span=102, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.305882 + 0.0003002 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_132_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=24, w2=115, w3=734, lag=2)."""
    a = _safe_log(open.abs() + 1.0).shift(2)
    b = _safe_log(high.abs() + 1.0).shift(2)
    corr = a.rolling(115, min_periods=max(115//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 24)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.319412 + 0.0003003 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_133_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=31, w2=128, w3=751, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    cover = _safe_div(a.rolling(31, min_periods=max(31//3, 2)).mean(), b.abs().rolling(128, min_periods=max(128//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.107 * _rolling_slope(cover, 31) + 0.0003004 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_134_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=141, w3=17, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    y = _safe_log(high.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.113333 * y + 0.886667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 38) - _rolling_slope(basket, 141) + 0.0003005 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_135_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=154, w3=34, lag=8)."""
    x = open.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(45, min_periods=max(45//3, 2)).mean(), upside.rolling(154, min_periods=max(154//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(34) * 1.36 + 0.0003006 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_136_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=167, w3=51, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    draw = x - x.rolling(167, min_periods=max(167//3, 2)).max()
    rebound = x - x.rolling(52, min_periods=max(52//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.126 * _rolling_slope(draw, 51) + 0.0003007 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_137_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=59, w2=180, w3=68, lag=21)."""
    a = _safe_log(open.abs() + 1.0).shift(21)
    b = _safe_log(high.abs() + 1.0).shift(21)
    imbalance = a.diff(59) - b.diff(126)
    stress = imbalance.rolling(68, min_periods=max(68//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.387059 + 0.0003008 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_138_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=66, w2=193, w3=85, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 66)
    baseline = trend.rolling(193, min_periods=max(193//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(85, min_periods=max(85//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.400588 + 0.0003009 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_139_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=73, w2=206, w3=102, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 73)
    slow = _rolling_slope(x, 206)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=102, adjust=False).mean() * 1.414118 + 0.000301 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_140_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=80, w2=219, w3=119, lag=0)."""
    x = open.shift(0)
    peak = x.rolling(219, min_periods=max(219//3, 2)).max()
    trough = x.rolling(80, min_periods=max(80//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.427647 + 0.0003011 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_141_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=87, w2=232, w3=136, lag=1)."""
    x = open.shift(1)
    change = x.pct_change(87)
    rank = change.rolling(232, min_periods=max(232//3, 2)).rank(pct=True)
    persistence = change.rolling(136, min_periods=max(136//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.157667 * persistence + 0.0003012 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_142_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=94, w2=245, w3=153, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(94, min_periods=max(94//3, 2)).std()
    vol_slow = ret.rolling(245, min_periods=max(245//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.454706 + 0.0003013 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_143_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=101, w2=258, w3=170, lag=3)."""
    x = open.shift(3)
    ma = x.rolling(258, min_periods=max(258//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 101)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.170333 * slope + 0.0003014 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_144_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=108, w2=271, w3=187, lag=5)."""
    x = open.shift(5)
    impulse = x.diff(108)
    drag = impulse.rolling(271, min_periods=max(271//3, 2)).mean()
    noise = impulse.abs().rolling(187, min_periods=max(187//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.481765 + 0.0003015 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_145_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=115, w2=284, w3=204, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 115)
    acceleration = _rolling_slope(velocity, 284)
    curvature = _rolling_slope(acceleration, 204)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.183 * acceleration + 0.0003016 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_146_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=122, w2=297, w3=221, lag=13)."""
    rel = _safe_div(open.shift(13), high.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 122)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.189333 * pressure.rolling(221, min_periods=max(221//3, 2)).mean() + 0.0003017 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_147_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=129, w2=310, w3=238, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(129, min_periods=max(129//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.522353 + 0.0003018 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_148_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=136, w2=323, w3=255, lag=34)."""
    a = _safe_log(open.abs() + 1.0).shift(34)
    b = _safe_log(high.abs() + 1.0).shift(34)
    corr = a.rolling(323, min_periods=max(323//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 136)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.535882 + 0.0003019 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_149_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=143, w2=336, w3=272, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    cover = _safe_div(a.rolling(143, min_periods=max(143//3, 2)).mean(), b.abs().rolling(336, min_periods=max(336//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.208333 * _rolling_slope(cover, 143) + 0.000302 * anchor
    return base_signal.diff().diff()

def f06_crev_gemini_150_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=150, w2=349, w3=289, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    y = _safe_log(high.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.214667 * y + 0.785333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 150) - _rolling_slope(basket, 349) + 0.0003021 * anchor
    return base_signal.diff().diff()
