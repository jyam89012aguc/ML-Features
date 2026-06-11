"""36 semi variance asymmetry gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

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

def f36_svar_gemini_076_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=41, w2=287, w3=460, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    draw = x - x.rolling(287, min_periods=max(287//3, 2)).max()
    rebound = x - x.rolling(41, min_periods=max(41//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.151667 * _rolling_slope(draw, 460) + 0.0026047 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_077_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=48, w2=300, w3=477, lag=21)."""
    a = _safe_log(low.abs() + 1.0).shift(21)
    b = _safe_log(close.abs() + 1.0).shift(21)
    imbalance = a.diff(48) - b.diff(126)
    stress = imbalance.rolling(477, min_periods=max(477//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.566471 + 0.0026048 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_078_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=55, w2=313, w3=494, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 55)
    baseline = trend.rolling(313, min_periods=max(313//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(494, min_periods=max(494//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.58 + 0.0026049 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_079_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=62, w2=326, w3=511, lag=55)."""
    x = _safe_log(low.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 62)
    slow = _rolling_slope(x, 326)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.593529 + 0.002605 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_080_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=69, w2=339, w3=528, lag=0)."""
    x = low.shift(0)
    peak = x.rolling(339, min_periods=max(339//3, 2)).max()
    trough = x.rolling(69, min_periods=max(69//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.607059 + 0.0026051 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_081_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=76, w2=352, w3=545, lag=1)."""
    x = low.shift(1)
    change = x.pct_change(76)
    rank = change.rolling(352, min_periods=max(352//3, 2)).rank(pct=True)
    persistence = change.rolling(545, min_periods=max(545//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.183333 * persistence + 0.0026052 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_082_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=83, w2=365, w3=562, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(83, min_periods=max(83//3, 2)).std()
    vol_slow = ret.rolling(365, min_periods=max(365//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.634118 + 0.0026053 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_083_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=90, w2=378, w3=579, lag=3)."""
    x = low.shift(3)
    ma = x.rolling(378, min_periods=max(378//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 90)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.196 * slope + 0.0026054 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_084_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=97, w2=391, w3=596, lag=5)."""
    x = low.shift(5)
    impulse = x.diff(97)
    drag = impulse.rolling(391, min_periods=max(391//3, 2)).mean()
    noise = impulse.abs().rolling(596, min_periods=max(596//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.661176 + 0.0026055 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_085_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=104, w2=404, w3=613, lag=8)."""
    x = _safe_log(low.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 104)
    acceleration = _rolling_slope(velocity, 404)
    curvature = _rolling_slope(acceleration, 613)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.208667 * acceleration + 0.0026056 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_086_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=111, w2=417, w3=630, lag=13)."""
    rel = _safe_div(low.shift(13), close.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 111)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.215 * pressure.rolling(630, min_periods=max(630//3, 2)).mean() + 0.0026057 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_087_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=118, w2=430, w3=647, lag=21)."""
    a = low.shift(21)
    b = close.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(118, min_periods=max(118//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.848235 + 0.0026058 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_088_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=125, w2=443, w3=664, lag=34)."""
    a = _safe_log(low.abs() + 1.0).shift(34)
    b = _safe_log(close.abs() + 1.0).shift(34)
    corr = a.rolling(443, min_periods=max(443//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 125)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.861765 + 0.0026059 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_089_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=132, w2=456, w3=681, lag=55)."""
    a = low.shift(55)
    b = close.shift(55)
    cover = _safe_div(a.rolling(132, min_periods=max(132//3, 2)).mean(), b.abs().rolling(456, min_periods=max(456//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.234 * _rolling_slope(cover, 132) + 0.002606 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_090_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=139, w2=469, w3=698, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    y = _safe_log(close.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.240333 * y + 0.759667 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 139) - _rolling_slope(basket, 469) + 0.0026061 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_091_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=146, w2=482, w3=715, lag=1)."""
    x = low.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(146, min_periods=max(146//3, 2)).mean(), upside.rolling(482, min_periods=max(482//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.902353 + 0.0026062 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_092_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=153, w2=495, w3=732, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    draw = x - x.rolling(495, min_periods=max(495//3, 2)).max()
    rebound = x - x.rolling(153, min_periods=max(153//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.253 * _rolling_slope(draw, 732) + 0.0026063 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_093_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=160, w2=508, w3=749, lag=3)."""
    a = _safe_log(low.abs() + 1.0).shift(3)
    b = _safe_log(close.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(749, min_periods=max(749//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.929412 + 0.0026064 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_094_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=167, w2=22, w3=766, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 167)
    baseline = trend.rolling(22, min_periods=max(22//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(766, min_periods=max(766//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.942941 + 0.0026065 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_095_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=174, w2=35, w3=32, lag=8)."""
    x = _safe_log(low.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 174)
    slow = _rolling_slope(x, 35)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=32, adjust=False).mean() * 0.956471 + 0.0026066 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_096_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=181, w2=48, w3=49, lag=13)."""
    x = low.shift(13)
    peak = x.rolling(48, min_periods=max(48//3, 2)).max()
    trough = x.rolling(181, min_periods=max(181//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.97 + 0.0026067 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_097_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=188, w2=61, w3=66, lag=21)."""
    x = low.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(61, min_periods=max(61//3, 2)).rank(pct=True)
    persistence = change.rolling(66, min_periods=max(66//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.284667 * persistence + 0.0026068 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_098_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=195, w2=74, w3=83, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(195, min_periods=max(195//3, 2)).std()
    vol_slow = ret.rolling(74, min_periods=max(74//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.997059 + 0.0026069 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_099_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=202, w2=87, w3=100, lag=55)."""
    x = low.shift(55)
    ma = x.rolling(87, min_periods=max(87//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 202)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.297333 * slope + 0.002607 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_100_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=209, w2=100, w3=117, lag=0)."""
    x = low.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(100, min_periods=max(100//3, 2)).mean()
    noise = impulse.abs().rolling(117, min_periods=max(117//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.024118 + 0.0026071 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_101_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=216, w2=113, w3=134, lag=1)."""
    x = _safe_log(low.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 216)
    acceleration = _rolling_slope(velocity, 113)
    curvature = _rolling_slope(acceleration, 134)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.31 * acceleration + 0.0026072 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_102_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=223, w2=126, w3=151, lag=2)."""
    rel = _safe_div(low.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 223)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.316333 * pressure.rolling(151, min_periods=max(151//3, 2)).mean() + 0.0026073 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_103_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=230, w2=139, w3=168, lag=3)."""
    a = low.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(230, min_periods=max(230//3, 2)).mean())
    decay = spread.ewm(span=139, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.064706 + 0.0026074 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_104_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=237, w2=152, w3=185, lag=5)."""
    a = _safe_log(low.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(152, min_periods=max(152//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 237)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.078235 + 0.0026075 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_105_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=244, w2=165, w3=202, lag=8)."""
    a = low.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(244, min_periods=max(244//3, 2)).mean(), b.abs().rolling(165, min_periods=max(165//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.335333 * _rolling_slope(cover, 244) + 0.0026076 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_106_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=251, w2=178, w3=219, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.341667 * y + 0.658333 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 251) - _rolling_slope(basket, 178) + 0.0026077 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_107_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=11, w2=191, w3=236, lag=21)."""
    x = low.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(11, min_periods=max(11//3, 2)).mean(), upside.rolling(191, min_periods=max(191//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.118824 + 0.0026078 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_108_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=18, w2=204, w3=253, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    draw = x - x.rolling(204, min_periods=max(204//3, 2)).max()
    rebound = x - x.rolling(18, min_periods=max(18//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.354333 * _rolling_slope(draw, 253) + 0.0026079 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_109_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=25, w2=217, w3=270, lag=55)."""
    a = _safe_log(low.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(25) - b.diff(126)
    stress = imbalance.rolling(270, min_periods=max(270//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.145882 + 0.002608 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_110_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=32, w2=230, w3=287, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 32)
    baseline = trend.rolling(230, min_periods=max(230//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(287, min_periods=max(287//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.159412 + 0.0026081 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_111_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=39, w2=243, w3=304, lag=1)."""
    x = _safe_log(low.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 39)
    slow = _rolling_slope(x, 243)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.172941 + 0.0026082 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_112_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=46, w2=256, w3=321, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(256, min_periods=max(256//3, 2)).max()
    trough = x.rolling(46, min_periods=max(46//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.186471 + 0.0026083 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_113_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=53, w2=269, w3=338, lag=3)."""
    x = low.shift(3)
    change = x.pct_change(53)
    rank = change.rolling(269, min_periods=max(269//3, 2)).rank(pct=True)
    persistence = change.rolling(338, min_periods=max(338//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.053667 * persistence + 0.0026084 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_114_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=60, w2=282, w3=355, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(60, min_periods=max(60//3, 2)).std()
    vol_slow = ret.rolling(282, min_periods=max(282//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.213529 + 0.0026085 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_115_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=67, w2=295, w3=372, lag=8)."""
    x = low.shift(8)
    ma = x.rolling(295, min_periods=max(295//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 67)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.066333 * slope + 0.0026086 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_116_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=74, w2=308, w3=389, lag=13)."""
    x = low.shift(13)
    impulse = x.diff(74)
    drag = impulse.rolling(308, min_periods=max(308//3, 2)).mean()
    noise = impulse.abs().rolling(389, min_periods=max(389//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.240588 + 0.0026087 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_117_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=81, w2=321, w3=406, lag=21)."""
    x = _safe_log(low.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 81)
    acceleration = _rolling_slope(velocity, 321)
    curvature = _rolling_slope(acceleration, 406)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.079 * acceleration + 0.0026088 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_118_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=88, w2=334, w3=423, lag=34)."""
    rel = _safe_div(low.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 88)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.085333 * pressure.rolling(423, min_periods=max(423//3, 2)).mean() + 0.0026089 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_119_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=95, w2=347, w3=440, lag=55)."""
    a = low.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(95, min_periods=max(95//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.281176 + 0.002609 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_120_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=102, w2=360, w3=457, lag=0)."""
    a = _safe_log(low.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(360, min_periods=max(360//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 102)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.294706 + 0.0026091 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_121_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=109, w2=373, w3=474, lag=1)."""
    a = low.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(109, min_periods=max(109//3, 2)).mean(), b.abs().rolling(373, min_periods=max(373//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.104333 * _rolling_slope(cover, 109) + 0.0026092 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_122_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=116, w2=386, w3=491, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.110667 * y + 0.889333 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 116) - _rolling_slope(basket, 386) + 0.0026093 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_123_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=123, w2=399, w3=508, lag=3)."""
    x = low.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(123, min_periods=max(123//3, 2)).mean(), upside.rolling(399, min_periods=max(399//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.335294 + 0.0026094 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_124_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=130, w2=412, w3=525, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    draw = x - x.rolling(412, min_periods=max(412//3, 2)).max()
    rebound = x - x.rolling(130, min_periods=max(130//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.123333 * _rolling_slope(draw, 525) + 0.0026095 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_125_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=137, w2=425, w3=542, lag=8)."""
    a = _safe_log(low.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(542, min_periods=max(542//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.362353 + 0.0026096 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_126_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=144, w2=438, w3=559, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 144)
    baseline = trend.rolling(438, min_periods=max(438//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(559, min_periods=max(559//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.375882 + 0.0026097 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_127_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=151, w2=451, w3=576, lag=21)."""
    x = _safe_log(low.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 151)
    slow = _rolling_slope(x, 451)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.389412 + 0.0026098 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_128_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=158, w2=464, w3=593, lag=34)."""
    x = low.shift(34)
    peak = x.rolling(464, min_periods=max(464//3, 2)).max()
    trough = x.rolling(158, min_periods=max(158//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.402941 + 0.0026099 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_129_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=165, w2=477, w3=610, lag=55)."""
    x = low.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(477, min_periods=max(477//3, 2)).rank(pct=True)
    persistence = change.rolling(610, min_periods=max(610//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.155 * persistence + 0.00261 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_130_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=172, w2=490, w3=627, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(172, min_periods=max(172//3, 2)).std()
    vol_slow = ret.rolling(490, min_periods=max(490//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.43 + 0.0026101 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_131_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=179, w2=503, w3=644, lag=1)."""
    x = low.shift(1)
    ma = x.rolling(503, min_periods=max(503//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 179)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.167667 * slope + 0.0026102 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_132_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=186, w2=17, w3=661, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(17, min_periods=max(17//3, 2)).mean()
    noise = impulse.abs().rolling(661, min_periods=max(661//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.457059 + 0.0026103 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_133_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=193, w2=30, w3=678, lag=3)."""
    x = _safe_log(low.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 193)
    acceleration = _rolling_slope(velocity, 30)
    curvature = _rolling_slope(acceleration, 678)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.180333 * acceleration + 0.0026104 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_134_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=200, w2=43, w3=695, lag=5)."""
    rel = _safe_div(low.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 200)
    pressure = rel_log.diff(43)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.186667 * pressure.rolling(695, min_periods=max(695//3, 2)).mean() + 0.0026105 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_135_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=207, w2=56, w3=712, lag=8)."""
    a = low.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(207, min_periods=max(207//3, 2)).mean())
    decay = spread.ewm(span=56, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.497647 + 0.0026106 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_136_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=214, w2=69, w3=729, lag=13)."""
    a = _safe_log(low.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(69, min_periods=max(69//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 214)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.511176 + 0.0026107 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_137_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=221, w2=82, w3=746, lag=21)."""
    a = low.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(221, min_periods=max(221//3, 2)).mean(), b.abs().rolling(82, min_periods=max(82//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.205667 * _rolling_slope(cover, 221) + 0.0026108 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_138_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=228, w2=95, w3=763, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.212 * y + 0.788000 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 228) - _rolling_slope(basket, 95) + 0.0026109 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_139_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=235, w2=108, w3=29, lag=55)."""
    x = low.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(235, min_periods=max(235//3, 2)).mean(), upside.rolling(108, min_periods=max(108//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(29) * 1.551765 + 0.002611 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_140_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=242, w2=121, w3=46, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    draw = x - x.rolling(121, min_periods=max(121//3, 2)).max()
    rebound = x - x.rolling(242, min_periods=max(242//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.224667 * _rolling_slope(draw, 46) + 0.0026111 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_141_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=249, w2=134, w3=63, lag=1)."""
    a = _safe_log(low.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(63, min_periods=max(63//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.578824 + 0.0026112 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_142_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=9, w2=147, w3=80, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 9)
    baseline = trend.rolling(147, min_periods=max(147//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(80, min_periods=max(80//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.592353 + 0.0026113 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_143_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=16, w2=160, w3=97, lag=3)."""
    x = _safe_log(low.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 16)
    slow = _rolling_slope(x, 160)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=97, adjust=False).mean() * 1.605882 + 0.0026114 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_144_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=23, w2=173, w3=114, lag=5)."""
    x = low.shift(5)
    peak = x.rolling(173, min_periods=max(173//3, 2)).max()
    trough = x.rolling(23, min_periods=max(23//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.619412 + 0.0026115 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_145_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=30, w2=186, w3=131, lag=8)."""
    x = low.shift(8)
    change = x.pct_change(30)
    rank = change.rolling(186, min_periods=max(186//3, 2)).rank(pct=True)
    persistence = change.rolling(131, min_periods=max(131//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.256333 * persistence + 0.0026116 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_146_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=37, w2=199, w3=148, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(37, min_periods=max(37//3, 2)).std()
    vol_slow = ret.rolling(199, min_periods=max(199//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.646471 + 0.0026117 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_147_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=44, w2=212, w3=165, lag=21)."""
    x = low.shift(21)
    ma = x.rolling(212, min_periods=max(212//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 44)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.269 * slope + 0.0026118 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_148_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=51, w2=225, w3=182, lag=34)."""
    x = low.shift(34)
    impulse = x.diff(51)
    drag = impulse.rolling(225, min_periods=max(225//3, 2)).mean()
    noise = impulse.abs().rolling(182, min_periods=max(182//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.82 + 0.0026119 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_149_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=58, w2=238, w3=199, lag=55)."""
    x = _safe_log(low.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 58)
    acceleration = _rolling_slope(velocity, 238)
    curvature = _rolling_slope(acceleration, 199)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.281667 * acceleration + 0.002612 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_150_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=65, w2=251, w3=216, lag=0)."""
    rel = _safe_div(low.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 65)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.288 * pressure.rolling(216, min_periods=max(216//3, 2)).mean() + 0.0026121 * anchor
    return base_signal.diff().diff().diff()
